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

The independent audit has not been performed. The algebraic identity for the derivative of the hazard is checked by the included standard-library script `verify.py` using exact rational arithmetic. The script tests the independent-power curvature identity at 3,344 triples, 2,190 integer-rate positivity cases, exact negative-curvature examples at rates \(b/a=1/2\) and \(b/a=3/2\), and quadratic coefficient identities. The program also conducts supplementary floating-point stress tests, which are not infinite-domain certificates.

The all-parameter proof is in `RESULT.md`: its essential steps are the exact curvature identity, an asymptotic negative-sign limit for \(0<b/a<2\) away from equality, a direct positive factorization for equality, and an exponential/logarithmic inequality for all \(b/a\ge2\). This reasoning requires no numerical extrapolation and no external calculation package.

Independent literature priority checking and independent scientific validation remain unperformed. The related 2010 two-component hazard-rate paper has not been examined in full; its published abstract does not identify the present three-component criterion.
