---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational check of the independence criterion

Run `python3 check_commutator_matroid.py` using only the Python standard library. It computes the commutator vector for every ordered pair in a five-vertex, five-arrow example. The complete marginal law on each of 32 arrow subsets is checked by exact integer arithmetic for factorization. Independently, a leaf-deletion algorithm classifies the forest subsets, including the empty one. Expected terminal output is `MATROID_FACTORISATION_OK 1048576 32 22`. These checks corroborate, but do not replace, the proof in `RESULT.md`.
