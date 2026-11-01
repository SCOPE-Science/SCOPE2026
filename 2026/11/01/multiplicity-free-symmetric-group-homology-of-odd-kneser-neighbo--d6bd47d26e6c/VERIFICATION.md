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

# Reproduction and scope

Run `python3 verify.py` with Python 3.10 or newer and its standard library. Expected complete stdout is included in `verify_output.txt`; the last line is `VERIFY_OK`.

The script reconstructs odd Kneser neighborhood facets for \(k=2,3,4\) and verifies pairwise intersection bounds, the middle-level graph's connectivity, its edge/vertex counts and first Betti rank. It computes Specht dimensions from hook lengths and, for every permutation on 5 and 7 symbols, checks the graph-cycle trace formula against a Schur-character calculation by Jacobi–Trudi expansion into power-sum symmetric functions. The fixed-branch property of the retraction is checked with exact rational sample coordinates. The general \(k\ge2\) theorem is proved symbolically in RESULT.md; no finite test is represented as an infinite certificate.

Only self-review has been performed; no independent mathematical audit has been performed.
