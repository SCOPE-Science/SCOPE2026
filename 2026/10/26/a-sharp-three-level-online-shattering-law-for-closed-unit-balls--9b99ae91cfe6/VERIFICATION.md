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

# Reproducibility

Run `python3 verify.py` with Python 3 and no external packages. `verification-output.txt` records the actual run. The program independently defines closed neighborhoods as Boolean functions and evaluates the full Littlestone split recurrence on subsets of distinct functions. It compares that game value with the claimed graph criterion for every unlabeled tree of order at most eight, enumerated exhaustively from Prüfer sequences.

At order eight it visits all 262144 labeled trees and obtains 23 isomorphism classes. It checks the VC-dimension upper bound for each representative by explicit trace enumeration on up to three queried vertices. The separate witness check verifies all eight complete depth-three paths, including their center witnesses. The terminal line is `ALL_CHECKS_PASS`.

This code validates only finite cases and the finite order-eight count. The all-order statement is proved in `RESULT.md` by a structural argument; neither the finite census nor its terminal line is evidence of an infinite proof. The implementation has not undergone independent audit.
