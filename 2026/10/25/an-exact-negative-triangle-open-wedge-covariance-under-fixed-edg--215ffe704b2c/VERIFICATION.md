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

The included `verify.py` independently enumerates every simple labelled graph on \(n=4,5,6\), grouped into all 34 fixed-edge strata. It compares the exact expected triangle and open-wedge counts, covariance, and two individual variances against the analytical overlap formulas; every rational comparison passed. It also sums fixed-edge moments to establish the independent-edge covariance polynomial for \(n=5\) by symbolic identity. Symbolic rational simplification establishes the displayed closed factorization for variables \(n,m\); three symbolic limits recover the fixed-density covariance and both variance constants.

Run: `python verify.py`. Python 3 and SymPy are needed. Successful output contains `VERIFY_OK` and describes the number of strata. All enumerations and identities are deterministic. The infinite-size statements and all-parameter negativity rely on the mathematical proof and are not inferred from the finite enumeration. No independent audit or independent validation has been performed.
