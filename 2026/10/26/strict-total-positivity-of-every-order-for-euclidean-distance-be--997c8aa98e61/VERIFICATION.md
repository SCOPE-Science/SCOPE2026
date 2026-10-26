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

## Reproducible checks
Execute `python checker.py` with `mpmath` installed. It recomputes the coefficient series, the odd-binomial closed form, and sample ordered minors of sizes two through five including squared-radius zero, printing `CHECK_OK` only when they satisfy its numerical tolerances. The gamma minor identity, Vandermonde positivity, and Cauchy–Binet convergence are established analytically in `RESULT.md`; no finite numerical sample certifies them for every parameter or order.

## Limits
This verification does not prove historical priority or extend the theorem beyond the unit disk and the weight \((1-|z|)^t\). No independent audit has been performed.
