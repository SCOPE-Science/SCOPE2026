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

Run `python3 checker.py` using Python 3. The script independently builds every cyclic rotation, sorts them lexicographically, and extracts predecessor letters. It tests the two universal transport laws on all \(1022\) nonempty binary words through length nine, checks the morphism intertwining on Chacon iterates, and compares the whole explicit BWT formula and run counts for ranks zero to seven. These finite tests passed.

The unrestricted proof is given in `RESULT.md`: lexicographic rotation-class separation, the substitution intertwining, and run-length induction. This verification does not amount to independent audit, exhaustive search for historical priority, or a computational proof of the infinite assertions.
