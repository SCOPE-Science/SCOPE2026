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

# Reproducibility and proof dependencies

Run the accompanying standard-library-only `verify.py` using Python 3. The execution completed with:

`VERIFY_OK exact_integrals=16 hull_geometry=983 product_samples=140000 moment_estimates=(1.99856,2.99274)`

Sixteen rational integrations compare the closed double-survival formula with direct binomial expansion. The hull checks compare the deterministic corner-triangle missing area with an independently constructed monotone-chain convex hull for various strictly convex triangles and irregular four- and five-gons. The exponential-product Monte Carlo phase checks the predicted mean 2 and variance 3 for four equal right-angle corner coefficients.

The infinite-sample theorem needs the full deterministic dissection, survival integration, joint Poisson/exponential argument, moment uniform integrability, Laplace saddle analysis, and convex-order proof written in RESULT.md. Neither the finite numerical samples nor this verification file independently certifies a theorem. No formal proof assistant, third-party verification, or independent audit is claimed.
