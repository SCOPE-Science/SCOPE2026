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
# Verification details

Run `sh reproduce.sh` with a C++17 compiler and Python 3. It compares independent, complete finite-game-type computations, not a sample of randomly chosen triples. The tests cover each unordered \((m,n)\) with \(1\le m\le n\le7\), enumerate repeated points, record equality and every directed relation atom, and verify all sixteen exact type fibres. The output must match `verification_output.txt`. The infinite reduction to dimensions seven follows from the independently stated three-round EF coordinate-game argument in `RESULT.md` and is not automatically machine-checked. The original literature-priority comparison is not exhaustive, and no independent mathematical audit has been performed.
