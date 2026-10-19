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

The exact finite-sample covariance identity was checked in two algebraic forms with rational arithmetic on 20,800 parameter triples for \(2\le m\le14\). The script explicitly checks the \(m=2,t=1/2\) deterministic exception, positivity at the mean-gap threshold for \(m\ge3\), saturation-branch signs, and 15 large-dimension evaluations against the predicted limiting covariance kernel. Run `python3 verify_nested_spacings.py` with Python 3; no external dependencies are required.

No finite calculation proves uniqueness over the continuum of thresholds, strict zero-curve monotonicity, or the infinite-dimensional limiting law. Those statements follow from the derivative and asymptotic proof in `RESULT.md`. The independent-audit status is not performed; no external certificate is provided.
