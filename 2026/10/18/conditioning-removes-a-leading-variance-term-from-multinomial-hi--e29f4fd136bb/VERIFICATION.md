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

# Verification and scope

Run `python verify.py` with Python 3.9 or later. It uses only the Python standard library, enumerates exact multinomial compositions for small samples, independently evaluates Poisson expectations for the coefficient, compares with reproducibly seeded fixed-sample multinomial simulations, and checks the endpoint constants. It executed successfully with 175 checks.

The proof of the infinite variance limit does not rely on simulation or numerical truncation. Its critical ingredients are the exact multinomial marginal mass, the explicit first-order Poisson correction for up to four cells, and the count of disjoint versus adjacent edge pairs. The strict-positivity argument is analytical, via a nonzero degenerate Hoeffding kernel. The small-load expansion requires order-four Poisson terms; the large-load expansion requires the bivariate absolute-Gaussian expectation at correlation \(-1/2\).

The numerical verifier provides finite corroboration only. It does not verify the novelty of the claim or establish any asymptotic theorem by exhaustive computation. Relevant primary full texts were not accessible at the time of this investigation, so originality remains subject to possible implicit coverage.
