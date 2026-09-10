"""Bounded recovery test for concurring-bush sqrt-log target (lane-586).

Model (generous to target):
- R0 = 65536, R0^{1/2} = 256. Concurrence cube Q side L=256 (vol ~ R^{3/2}).
- N = 64 distinct canonical caps, centres on 8x8 grid in [0,1]^2.
- On Q, Ef_theta(x) ~= R^{-1} * exp(i(x'.w + x3|w|^2)) with envelope 1
  (ignores tube-envelope decay -> overestimates coherence, favors target).
- S(x) = sum_theta exp(i Phi_theta(x)).
- Q-contribution ratio R_Q = ||S||_{L^4(Q)} / (sqrt(N) R^{1/2})
  (see WORKLOG derivation). Fully coherent value would be N|Q|^{1/4}/(sqrt(N)R^{1/2})
  = sqrt(N) R^{-1/8} = R^{1/8}/2 = 2.0 at R0.
- Random-phase prediction: mean|S|^4 ~= 2N^2 - N -> A=(mean|S|^4)^{1/4} ~= 9.5,
  R_Q ~= A|Q|^{1/4}/(sqrt(N)R^{1/2}) = A/(32) ~= 0.3.
- Ceiling check: ratio^4 <=~ 1/N + N R^{-1/2} = 1/64+1/4 (closed form).

This script: Monte Carlo estimate of A and R_Q + closed-form ceiling.
Stdlib only, seeded.
"""
import random, math

R0 = 65536
sqR = 256.0
N = 64
L = 256.0

# 8x8 grid centres in [0,1]^2
centres = []
for i in range(8):
    for j in range(8):
        centres.append(((i+0.5)/8.0, (j+0.5)/8.0))

def sample_S(x1, x2, x3):
    s_re, s_im = 0.0, 0.0
    for (w1, w2) in centres:
        ph = x1*w1 + x2*w2 + x3*(w1*w1+w2*w2)
        s_re += math.cos(ph)
        s_im += math.sin(ph)
    return s_re*s_re + s_im*s_im  # |S|^2

random.seed(0)
M = 20000
# sample uniformly in Q = [-L/2,L/2]^3
acc2 = 0.0  # mean |S|^2
acc4 = 0.0  # mean |S|^4
for _ in range(M):
    x1 = random.uniform(-L/2, L/2)
    x2 = random.uniform(-L/2, L/2)
    x3 = random.uniform(-L/2, L/2)
    p = sample_S(x1, x2, x3)  # |S|^2
    acc2 += p
    acc4 += p*p
mean2 = acc2/M
mean4 = acc4/M
A = mean4**0.25
pred = 2*N*N - N
Apred = pred**0.25
Qvol = L**3
# R_Q = ||S||_4(Q)/(sqrt(N)*R^{1/2}) = (mean4*Qvol)^{1/4}/(sqrt(N)*256)
RQ = (mean4*Qvol)**0.25/(math.sqrt(N)*256.0)
RQ_pred = Apred*(Qvol**0.25)/(math.sqrt(N)*256.0)
coherent = float(N)*(Qvol**0.25)/(math.sqrt(N)*256.0)
ceil4 = 1.0/N + N/sqR
ceil1 = ceil4**0.25
target_base = 4.0/3.0

print(f"N={N} R0={R0} samples={M}")
print(f"Monte Carlo mean|S|^2 = {mean2:.2f} (incoherent prediction N={N})")
print(f"Monte Carlo mean|S|^4 = {mean4:.1f} (random-phase prediction {pred})")
print(f"A = (mean|S|^4)^1/4 = {A:.3f} (prediction {Apred:.3f}, coherent {N})")
print(f"R_Q Monte Carlo = {RQ:.4f} (prediction {RQ_pred:.4f}, coherent {coherent:.4f})")
print(f"closed-form ceiling ratio <= (1/N + N/sqrtR)^{{1/4}} = ({ceil4:.5f})^{{1/4}} = {ceil1:.4f}")
print(f"target base-case threshold = {target_base:.4f}")
ok = (RQ < 0.6) and (ceil1 < target_base) and (coherent >= target_base)
print("CEILING_CONFIRMED" if ok else "INCONCLUSIVE")
print(f"Heuristic gap: coherent {coherent:.2f} assumes O(R^{{3/2}}) coherence volume; "
      f"true coherence volume is O(1), giving R_Q ~ {RQ_pred:.2f} << 4/3.")
