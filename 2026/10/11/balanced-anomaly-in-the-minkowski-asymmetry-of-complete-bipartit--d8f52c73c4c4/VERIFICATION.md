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

# Verification and scope

The mathematical proof is given in `RESULT.md`. In particular, the deletion-component computation proves the critical minimum-support lemma for every \(p,q\ge2\), and the graph-edge-transitive averaging argument proves that no off-center choice improves the minimum reflection factor.

To reproduce finite exact-rational checks, execute `python verify.py` using Python 3's standard library. The verifier exhaustively builds spanning-tree indicators and independently enumerates their intersections with all nontrivial induced-edge sets for eight parameter profiles: (2,2), (2,3), (2,4), (2,5), (3,3), (3,4), (3,5), (4,4). It confirms 6,762 spanning trees, 1,412,760 vertex-subset/tree comparisons, the predicted factor in each case, and the balance dichotomy. Output ends in `PASS profiles=8 trees=6762 vertex-subset-comparisons=1412760`.

The finite checks cannot certify all dimensions, literature priority, or uniqueness of the center. The full algebraic argument covers the infinite parameter family; no independent external assessment has been performed.
