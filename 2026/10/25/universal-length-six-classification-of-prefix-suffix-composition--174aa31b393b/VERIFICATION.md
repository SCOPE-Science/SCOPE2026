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

# Verification record

The mathematical proof uses an explicitly proved unique-matching lemma for two unordered upward paths in the lattice of Parikh vectors. It shows precisely when a new reversal-inequivalent path pairing can occur and classifies the only exceptional depth-two meeting at word length six. A separate counting argument derives the number of fibers of each size.

Execute `python3 CHECK.py` in this package to enumerate words of lengths one through six over alphabets of sizes two through seven. The checker uses two independently constructed observation representations and compares every nontrivial fiber against the explicit pair-of-two-subsets formula. Expected final line:

`PREFIX_SUFFIX_FIRST_COLLISION_PASS alphabets=2..7 lengths=1..6 methods=two-deck-representations all-fibers=classified`

These finite computations do not verify arbitrary \(q\), nor do they substitute for the full proof. No independent audit or external validation is asserted.
