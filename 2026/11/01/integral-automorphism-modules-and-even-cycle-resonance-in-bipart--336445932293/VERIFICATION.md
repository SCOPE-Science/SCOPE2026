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

# Verification instructions

Run `python3 verify.py` with the Python standard library. The checker directly constructs all orientations, legal flex edges, and cubical cells of the graph \(K_{2,n}\) for \(n=3,4,5\). It checks connected components and their labels; the exact action of every leaf permutation and hub exchange; and the signed cellular Lefschetz number against the predicted first-homology character.

Executed checks gave `TEST_OK (3, 19, 4, 142, 12)`, `TEST_OK (4, 65, 5, 658, 48)`, `TEST_OK (5, 211, 6, 3190, 240)`, and `VERIFY_OK`. The five entries in each `TEST_OK` line are number of leaves, number of connected components, number of cubical degrees, total cubical cells, and tested graph automorphisms.

The proof in `RESULT.md` applies for all \(n\ge3\) and relies on the cited, independently published component enumeration. The computational checks establish only the cases explicitly run; they do not prove arbitrary-parameter correctness or establish the absence of unindexed prior literature. Independent mathematical audit has not been performed.
