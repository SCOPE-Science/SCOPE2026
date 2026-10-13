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
Run `python3 verify.py` with a standard Python 3 interpreter. The expected final line is `VERIFY_OK_FULL`.

The script builds exactly the stated four-marker directed relation, checks its transitivity, and enumerates all labeled connected bipartite graphs on two, three, and four vertices (one, three, and nineteen respectively). For all 529 ordered pairs, it independently checks equivalence between a color-preserving surjective graph homomorphism and a surjective stable map of the associated frames. Frame-map enumeration permits arbitrary marker permutations and arbitrary images of reflexive points consistent with reflexivity; it does not assume the fixed-marker conclusion. Twenty-one explicit cycle fold maps are checked, and the six-vertex path/star pair has no stable maps in either direction.

Limits: these are finite checks only. The global order theorem, all cyclic sizes, and the modal-theoretic infimum follow from the symbolic argument in RESULT.md and cited standard semantic machinery, not from bounded tests. Independent audit has not been performed.
