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

The ordinary script `verify.py` uses only Python's standard library and can be run with `python3 verify.py`. It reconstructs the original adjacency structure, enumerates all cardinality-half subsets for three small instances, and checks the complete period-twenty binary-spin census separately. It also checks the Laurent polynomial factorization by exact integer coefficients and the proposed constructions through \(n=100\). The recorded successful checks are scientific corroboration, not an infinite exhaustive certificate; the proof of all dimensions is in `RESULT.md`.

No independent mathematical audit has been performed.
