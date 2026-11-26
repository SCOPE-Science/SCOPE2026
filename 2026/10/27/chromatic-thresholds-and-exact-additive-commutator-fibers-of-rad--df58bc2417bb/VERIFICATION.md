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

# Finite verification of repeated-commutator fibers

`python3 verify.py` uses standard Python. On a three-vertex quiver over \(\mathbb F_2\) with a loop and repeated arrows, it forms the commutator distribution by direct multiplication. Exact convolution gives two- and three-pair fibers, which are compared target by target with the coloring expression. The terminal line is `MULTIPLE_COMMUTATOR_FIBERS_OK`. The proof in `RESULT.md`, not the finite check, handles arbitrary finite fields and numbers of pairs.
