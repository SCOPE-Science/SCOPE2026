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

Use `python verify.py` with a standard Python 3 interpreter. The script performs exact-fraction conditional-root-split moment recurrences through 100 nodes, independently computes bivariate subtree distributions through 8 nodes, and enumerates every permutation of up to 8 keys to compare the complete distribution. The test includes the four n=7 conditional CDF coefficients that witness non-stochastic-ordering. The analytic proof, not the finite checks, establishes the uniform formula for unbounded n. The historical-priority comparison remains non-exhaustive. Independent audit has not been performed.
