"""Disproof ledger for lane-1019 target (deterministic, stdlib only).

Target: ||S(t)(I-Pi)||_{E->H} <= 60 t^{-5/2}, 0<t<=1,
E = L^1_v(<v>^12) L^infty_x, H = L^2_{x,v}, T^3=(R/2piZ)^3.

Witness: x-homogeneous velocity-ball indicators psi_e = c_e 1_{|v|<=e},
||psi_e||_E = 1, ||psi_e||_H >= c_H e^{-3/2} with exact c_H below.
Free/loss Dyson term preserves the peak; Pi and all remainders live in the
fixed 5-dim Schwartz space span{phi_j mu} with e-uniform bounds via the
standard L^2(mu^{-1/2}) semigroup theory. Hence for every fixed t>0,
||S(t)(I-Pi) psi_e||_H -> +infinity as e->0: the E->H norm is +infinity.

All constants below are exact integers / closed-form Gamma evaluations.
"""
import math

PI = math.pi

# ---- 1. Data H-lower constant (exact closed form) --------------------------
# c_e >= 1/(64 (4pi/3) e^3); ||psi||_H = (2pi)^{3/2} c_e ((4pi/3)e^3)^{1/2}
c_H = (2*PI)**1.5 / (64*math.sqrt(4*PI/3))
print(f"c_H = {c_H:.6f}  (>= 0.12: {c_H >= 0.12})")

# ---- 2. Collision frequency on support -------------------------------------
# nu(v) <= |v| + E|w|, E|w| = sqrt(8/pi) for N(0,I_3) (unit angular norm.;
# with angular mass beta use beta*(1+sqrt(8/pi)) -- still finite).
Eabs = math.sqrt(8/PI)
nubar = 1.0 + Eabs
print(f"E|w| = {Eabs:.6f}, nubar(|v|<=1) = {nubar:.6f} (<= 2.6: {nubar <= 2.6})")

# ---- 3. Projection weights (exact) -----------------------------------------
# m_j = sup |phi_j| <v>^-12: m_0 = 1; m_1 = max r(1+r^2)^-6 at r=1/sqrt(11);
# m_4 = max |r^2-3|/sqrt(6) (1+r^2)^-6 at r=0.
m0 = 1.0
m1 = (12/11)**(-6)/math.sqrt(11)
m4 = math.sqrt(3/2)
print(f"m0 = {m0:.6f}, m1 = {m1:.6f}, m4 = {m4:.6f}")
VOL = (2*PI)**3
print(f"|T^3| = {VOL:.6f}")

# ---- 4. Exact E-moments of the collision-invariant densities ---------------
def dfact_odd(n):
    # n!! for odd n >= 1; (-1)!!/1!! edge: returns 1 for n <= 1
    p = 1
    k = n
    while k > 1:
        p *= k
        k -= 2
    return p

C = math.comb
# L1_0 = E[(1+R^2)^6], R^2 ~ chi^2_3, E[(chi^2_3)^k] = (2k+1)!!
L1_0 = sum(C(6, k)*dfact_odd(2*k+1) for k in range(7))
print(f"L1_0 = E[(1+R^2)^6] = {L1_0}  (exact integer)")
# L1_1 = E[|v1|(1+R^2)^6] = (1/2) sum C(6,k) E[R^{2k+1}],
# E[R^{2k+1}] = 2^{k+1/2} (k+1)! / Gamma(3/2), Gamma(3/2)=sqrt(pi)/2
L1_1 = sum(C(6, k)*2**(k+0.5)*math.factorial(k+1)/(math.sqrt(PI)/2)
           for k in range(7))/2
print(f"L1_1 = E[|v1|(1+R^2)^6] = {L1_1:.4f}  (closed-form Gamma sum)")
# L1_4 <= E[(R^2+3)(1+R^2)^6]/sqrt(6)  (triangle inequality), exact integers
L1_4 = sum(C(6, k)*(dfact_odd(2*k+3) + 3*dfact_odd(2*k+1))
           for k in range(7))/math.sqrt(6)
print(f"L1_4 <= {L1_4:.4f}  (exact integer sum / sqrt(6))")

C_Pi_E = VOL*(m0*L1_0 + 3*m1*L1_1 + m4*L1_4)
print(f"||Pi||_E->E <= |T^3|(m0 L1_0 + 3 m1 L1_1 + m4 L1_4) = {C_Pi_E:.3f} (<inf)")

# ---- 5. H-norms of phi_j mu (exact Gaussian moments) ------------------------
nmu2 = (2*PI)**-3 * PI**1.5
nvmu2 = (2*PI)**-3 * PI**1.5 / 2
n42 = (2*PI)**-3 * PI**1.5 * (15/4) / 6
import math as _m
C_Pi_H = VOL*(m0*_m.sqrt(VOL)*_m.sqrt(nmu2)
              + 3*m1*_m.sqrt(VOL)*_m.sqrt(nvmu2)
              + m4*_m.sqrt(VOL)*_m.sqrt(n42))
print(f"||Pi||_E->H <= {C_Pi_H:.4f} (<inf)")

# ---- 6. Violation thresholds -------------------------------------------------
# At fixed t: ||S(t)(I-Pi)psi_e||_H >= A(t) e^{-3/2} - C'(t),
# A(t) = e^{-2.6 t} c_H, C'(t) < inf (e-independent). For ANY assumed finite
# cap R on C'(t), violation of the envelope E(t)=60 t^{-5/2} is certified for
# e < (A(t)/(E(t)+R))^{2/3}. At t=1, E(1)=60:
A1 = math.exp(-2.6)*c_H
print(f"\nA(1) = e^-2.6 c_H = {A1:.6f}; claimed envelope at t=1 is 60.")
for R in [1e2, 1e4, 1e6, 1e9]:
    estar = (A1/(60+R))**(2/3)
    print(f"  remainder cap R={R:>10.0f}: certified violation for e < {estar:.3e} "
          f"(then A(1)e^-1.5 - R > 60)")
print("\nSince C'(1) is finite, taking e small violates EVERY finite envelope:")
print("||S(1)(I-Pi)||_{E->H} = +infinity. The 60 t^{-5/2} claim is false.")
print("Smooth data: v-mollifications inherit the bound (DRAFT.md Sec.6).")
