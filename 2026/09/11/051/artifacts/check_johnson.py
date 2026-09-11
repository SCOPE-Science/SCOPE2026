"""Johnson-side audit for lane-831: folded distance, pairwise cap, list-size cap.

Folded code: N=16 bundles of s=4 over alphabet F_257^4, dimension k=16 (rate 1/4).
- Two distinct codewords agree on <= k-1 = 15 unfolded positions (RS distance).
- A bundle-agreement consumes 4 distinct agreeing positions -> pairwise bundle
  agreement <= floor(15/4) = 3; folded distance >= 13 bundles.
- Radius rho=0.52 -> bundle errors <= floor(0.52*16) = 8 -> agreement >= 8.
- Second-moment (Johnson) bound: L codewords with agreement >= A=8 each,
  pairwise agreement <= C=3  ==>  L <= 5 (checked numerically below).
- Folded q-ary Johnson radius 1-sqrt(1-13/16) ~= 0.567 > 0.52 (large alphabet):
  radius sits INSIDE the folded Johnson bound, so the (rho,L) consequence is a
  textbook Johnson corollary, not a beyond-Johnson certificate.
"""
import math

N, S, K = 16, 4, 16
CMAX = (K - 1) // S          # max pairwise bundle agreement = 3
AMIN = N - int(math.floor(0.52 * N))  # min agreement = 8
print(f"pairwise bundle-agreement cap = {CMAX}, min agreement = {AMIN}")
print(f"folded distance >= {N - CMAX}, folded Johnson radius = {1 - math.sqrt(1 - (N - CMAX) / N):.4f}")

# Necessary coexistence condition: with S_i = total agreements >= AMIN*L,
# sum_i C(t_i,2) >= N*C(S_i/N,2) (convexity) must be <= C(L,2)*CMAX.
excluded = []
for L in range(1, 17):
    Ssum = AMIN * L
    lhs = Ssum * (Ssum - N) / (2 * N)   # N*C(S/N,2) generalized
    rhs = L * (L - 1) / 2 * CMAX
    print(f"L={L:2d}: need {lhs:8.2f} <= {rhs:8.2f} -> {'possible' if lhs <= rhs else 'EXCLUDED'}")
    if lhs > rhs:
        excluded.append(L)
assert all(L >= 6 for L in excluded) and 6 in excluded
print("RESULT: L>=6 impossible by counting ==> L<=5 (hence L<=16 holds trivially).")
print("NOTE: textbook Johnson corollary; carries no originality.")
