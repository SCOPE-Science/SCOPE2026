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

The proof is symbolic for all integers \(n\ge1\) and all finite groups \(G\) of order \(g\ge1\), without an assumption that \(G\) is abelian. The direct multiplication checker uses cyclic groups as finite test cases; no finite enumeration is claimed to establish the universal result.

To replay the complete finite tests from this package, place `verify.py` and `verify_output.txt` together, run `python verify.py`, and compare stdout byte-for-byte with `verify_output.txt`. This checker uses only the Python standard library.

Checks exercised: independent weighted-DAG enumeration against the closed longest-path-level formula at all indices for \(1\le n\le4\), \(g\in\{1,2,4\}\); independent exhaustive multiplication of *all nonempty subsets* for the seven cases enumerated in the RESULT document. The arithmetic uses exact integers, including very large weighted counts. Successful execution emits `VERIFY_OK`. Scientific limits include the fact that the direct subset tests only cover listed small instances and cyclic groups; all-group extension is derived from the symbolic support criterion.
