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

# Reproduction

Execute `python verify.py` with Python 3.10+ from this directory. The program has no third-party dependencies and constructs every weak-order poset with total size one through eight using all ordered compositions of the total size, plus five larger selected tuples.

For each frame, it constructs every upset from the order relation, directly evaluates Heyting implication through upper cones, and checks the exact Peirce equation for all ordered pairs. The expected principal filters, the multiplicity polynomial, the inverse recovery of the level-size sequence, and the resulting two-variable satisfaction degree are compared independently to this exhaustive evaluation. With at most five points, the implication operation is also independently recomputed as the join of all upsets satisfying the defining residuation condition.

Observed successful output on execution:

`VERIFY_OK families=260 peirce_pairs=328293 direct_residuation_families=31`

The program is bounded finite verification. The general theorem is established by the symbolic argument in `RESULT.md`, not by an infinite computational certificate. Publication priority and independent external auditing have not been verified.
