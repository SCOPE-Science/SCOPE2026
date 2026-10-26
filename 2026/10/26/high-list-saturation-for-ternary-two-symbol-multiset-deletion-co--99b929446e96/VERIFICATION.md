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

The proof is symbolic; no finite computation is used to infer the theorem at untested lengths. To replay finite checks, execute `python CHECKER.py` with Python 3; the file uses only the standard library.

Observed checks:

- Length-four complete census: all \(2^{15}=32768\) code subsets were examined; optimum counts for list bounds \(1,\ldots,7\) were \(3,6,9,11,13,15,15\).
- For each list bound \(5,\ldots,70\), three consecutive allowed source lengths were checked (198 cases), including distinctness, six direct received-pair loads, the claimed size, and even-list equality restrictions.
- The maximal-coordinate lift was checked for all 9,119 source multisets at lengths 4 through 36; no collision or changed received-pair signature occurred.

The proof separately establishes the upper bound and all attaining constructions for arbitrary parameters in scope. No independent external validation is asserted.
