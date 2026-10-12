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
# Verification

The standalone checker `verification/verify.py` reconstructs Equation (13) in the full three-dimensional variables and the two-step Jacobian product symbolically, rather than trusting previously computed eigenvalues.

It checks that
\[
h_-=\frac{49}4\log7,\qquad h_+=2h_-
\]
is an exact period-two orbit for \(\sigma=1/4\), \(r_0=49/4\), \(\nu=1\), that the Jacobian product has diagonal entries
\[
\frac{(7\log7-8)(\log7-1)}8,
\qquad\frac78,
\qquad\frac98,
\]
and that the equilibrium replacement factors coincide. An exact bound on \(\log7\) is obtained from rational upper and lower bounds on the exponential series, so the prey multiplier is analytically inside \((0,3/4)\); numerical approximations play no role in certifying stability.

The checker also differentiates \(\log(e^u-\sigma)\) symbolically to reproduce strict concavity. This finite algebraic replay supports, but does not replace, the general Jensen proof in `RESULT.md`. No claim of independent validation or exhaustive search is made.
