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

# Exact arithmetic and finite enumeration

Reproduce by running `python verify.py` with Python 3 and SymPy. The program constructs the two overlapping-triple joint tables directly from all permutations of size four and five. It verifies exact rational entrywise covariance coefficients and an exact symbolic factorization of the characteristic polynomial. It then enumerates every permutation of sizes four through eight to compare the covariance and mean counts and verify the endpoint telescoping relation, and tests the analytic eigenvalue ordering numerically for \(4\le n\le300\). The infinite-range theorem follows from the displayed overlap calculation and elementary algebra, not from the finite enumeration. The reported verification is reproducibility evidence, not external certification or an independent audit.
