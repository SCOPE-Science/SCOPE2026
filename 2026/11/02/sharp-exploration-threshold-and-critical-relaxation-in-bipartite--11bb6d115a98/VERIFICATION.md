---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the mathematical result

The self-contained source file `verify.py` uses only the Python standard library. Run `python3 verify.py` and expect a line reporting PASS for 480 numerical reward-gradient/free-energy checks, 400 high-temperature weighted contraction steps, 15 polarized root/onset comparisons, three critical-relaxation integrations, and 100 numerical cubic-coefficient checks. The second line reports the observed ratios of critical center amplitudes to their \(t^{-1/2}\) prediction at time 2000, for three graph sizes.

The calculations compare two independent representations of the Q-learning reward-gradient field and finite-difference derivatives of the potential; integrate the full vector ODE by fourth-order Runge–Kutta; solve positive scalar fixed-point equations by bisection; and numerically project the cubic Taylor term onto the normalized center direction. All embedded test assertions passed prior to packaging.

**Proof-level checks:** the log-odds equation follows exactly from payoff differences; the potential derivative is a nonnegative sum of squares; all trajectories are bounded in logits. The positive fixed-point map is strictly concave, giving exact equilibrium count. Its derivative at the positive fixed point is less than one, giving stable transverse eigenvalues. The weighted Dini maximum-norm derivative gives the optimal global exponential bound. The critical center projection has coefficient \(-T_c(a+b)/24\), with \(q\cdot q=2ab\); hence the exact leading square-root time coefficient is \(\sqrt{12/[T_c(a+b)]}\) for the normalized amplitude. The unfolding gives the two opposing \(\sqrt{T_c-T}\) branches.

Finite-step computations cannot certify all real parameters or the infinite family. Smooth center-manifold existence and exponential tracking are standard local dynamical-systems results invoked analytically. The theorem concerns the continuous-time deterministic ODE only. No independent external audit has been conducted.
