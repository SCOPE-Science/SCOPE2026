"""Quantitative finite Morse-index bound across spherical-harmonic sectors.

For the energy-supercritical focusing NLS linearized around the MRR ground
state Q (radial Emden solution  Q'' + (d-1)/r Q' + Q^p = 0, Q(0)=1, Q'(0)=0):
  sector operators  L^{(n)}_+ = -d_rr - (d-1)/r d_r + n(d+n-2)/r^2 + V_+(r)
  with V_+(r) = -p Q(r)^{p-1} (and similarly V_- = -Q^{p-1}).

Since r^2 Q(r)^{p-1} is globally bounded (continuous at 0, ~r^{-2} decay at
infinity), write C_V = sup_r r^2 p Q^{p-1}. Then for the radial measure
r^{d-1}dr, Hardy gives positivity once n(d+n-2) > C_V + (d-2)^2/4 margin.
More directly: effective potential [n(d+n-2) - C_V]/r^2 is pointwise
nonnegative when n(d+n-2) >= C_V, so the sector form is nonnegative
(no negatives) there. Hence only n < N_0 can carry instabilities and the
total nonradial Morse index is finite.

This script: integrates the Emden ODE by RK4 (no scipy), estimates C_V,
and prints the explicit threshold N_0 for representative admissible pairs
(d=11,p=7) and (d=12,p=5) with Joseph-Lundgren check.
"""
import math

def integrate_Q(d, p, rmax=60.0, dr=0.0005):
    n = int(rmax / dr)
    r = 0.0
    Q = 1.0
    Qp = 0.0
    max_cv = 0.0
    r_vals = []
    # sample sup of r^2 p Q^{p-1}
    for i in range(n):
        # RK4 step for system (Q, Qp); handle r=0 singularity via series start
        def f(r_, Q_, Qp_):
            if r_ < 1e-12:
                return (Qp_, -Q_**p / d)
            return (Qp_, -(d - 1) / r_ * Qp_ - Q_**p)
        if Q < 0:
            break  # crossed zero; Emden ground state stays positive for JL-supercritical
        if r > 1e-9 and Q > 0:
            cv = r * r * p * (Q ** (p - 1))
            if cv > max_cv:
                max_cv = cv
                r_star = r
        # RK4
        k1Q, k1P = f(r, Q, Qp)
        k2Q, k2P = f(r + dr/2, Q + dr/2*k1Q, Qp + dr/2*k1P)
        k3Q, k3P = f(r + dr/2, Q + dr/2*k2Q, Qp + dr/2*k2P)
        k4Q, k4P = f(r + dr, Q + dr*k3Q, Qp + dr*k3P)
        Q += dr/6*(k1Q + 2*k2Q + 2*k3Q + k4Q)
        Qp += dr/6*(k1P + 2*k2P + 2*k3P + k4P)
        r += dr
    return max_cv, r, Q

def jl_exponent(d):
    if d <= 10:
        return float('inf')
    return 1 + 4.0 / (d - 4 - 2*math.sqrt(d - 1))

def threshold_N0(d, C_V):
    n = 0
    while n*(d + n - 2) < C_V:
        n += 1
    return n

if __name__ == "__main__":
    for (d, p) in [(11, 7), (12, 5), (11, 9)]:
        g = 2/(p-1)
        D = (d-2)**2 - 4*p*g*(d-2-g)
        pjl = jl_exponent(d)
        Cv, rend, Qend = integrate_Q(d, p)
        N0 = threshold_N0(d, Cv)
        # finite-index count bound: sum over n<N0 of (sector multiplicity bound)
        print(f"d={d} p={p}: g={g:.4f} JLdisc D={D:.3f} p_JL={pjl:.3f} "
              f"p>p_JL={p > pjl} sup r^2 pQ^(p-1)={Cv:.3f} "
              f"N0(positivity for n>=N0)={N0} Q({rend:.1f})={Qend:.4f}")
