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

The exact rational verifier uses only the Python 3 standard library. Run `python3 verify.py` from a directory containing the extracted verification script.

The script computes beta-tail moments by an independent finite binomial expansion for integer shape parameters. It compares exact covariance integrals against the explicit quadratic formula for every \(2\le n\le9\), \(1\le\alpha\le5\) integral, and \(t=j/20\) with \(1\le j\le19\); it also checks the exact zero and sign on either side for those parameter pairs. Higher polynomial convex scores \(s^3,s^4,s^5\) are evaluated by direct rational beta-tail integrations over the displayed finite grids. The completed execution returned `PASS: 4156 exact Fraction comparisons`.

The unbounded statement for arbitrary real \(\alpha>0\), dimensions, and twice-differentiable strictly convex functions is proved analytically; finite checks alone do not establish it. No independent audit or external replication has been performed.
