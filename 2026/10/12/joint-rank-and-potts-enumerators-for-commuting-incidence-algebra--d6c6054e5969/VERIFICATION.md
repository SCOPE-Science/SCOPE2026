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

Execute `python3 checker.py` with a Python 3 standard library only. It exhaustively constructs incidence-algebra matrices over the finite fields of sizes 2, 3, and 4, checks direct multiplication and pairwise commutation, tests all distinct color-affine parameterizations, and matches complete joint-rank multiplicities. Its independent edge-subset implementation of the Fortuin–Kasteleyn count matches the directly enumerated tuples in all nine listed configurations. Expected last line: `VERIFY_OK`.

The exact symbolic proof, not the finite-field experiments, establishes the theorem in arbitrary characteristic and arbitrary finite-poset size. The computational tests are limited to the finite examples printed by the script, and do not resolve novelty or provide independent audit.
