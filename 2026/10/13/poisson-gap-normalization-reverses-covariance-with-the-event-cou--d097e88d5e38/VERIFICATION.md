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

Conditional on \(N=n\), the normalized complete-window gaps are uniform on the simplex, giving \(\mathbb E[Q_t\mid N=n]=2/(n+2)\) and \(\mathbb E[C_t^2\mid N=n]=n/(n+2)\). A direct Poisson index shift converts these regressions into covariances, a beta integral evaluates the remaining expectation, and \(e^\mu>1+\mu\) proves positivity.

The accompanying `verify.py` checks the conditional identities exactly for \(0\le n\le1000\), compares direct Poisson summation with both covariance formulas at ten intensities, and checks the small-intensity expansion at three high-precision values. Its expected terminal line is `VERIFY_OK conditional=1001 poisson=10 small_mu=3`.

The checker is supplementary and does not establish originality or extend the theorem beyond the stated assumptions.
