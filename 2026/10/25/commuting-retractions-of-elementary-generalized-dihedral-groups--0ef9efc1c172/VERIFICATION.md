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

# Direct checks and scope

Run `python verify_dihedral.py` with Python 3 standard library. The code reconstructs projection matrices over \(\mathbb F_p\), adds exactly the allowed translation vectors and the distinct trivial group endomorphism, tests the affine composition-commutation condition for all pairs and compares every individual degree to the closed formula. For \((p,d)=(3,1),(3,2),(5,2)\), a graph maximal-clique search verifies both the expected number and uniform size. For \((p,d)=(3,3)\), all pairwise commutation and centralizer degrees are checked (no full maximal-clique search). For \((p,d)=(3,2)\), every enumerated map is also verified directly as a homomorphism and idempotent on group elements, with composition commutation recomputed directly on all group elements.

Observed outputs: `PASS 3 1 idempotents 5 commuting ordered pairs 19 maximal cliques checked True`; `PASS 3 2 idempotents 47 commuting ordered pairs 553 maximal cliques checked True`; `PASS 5 2 idempotents 177 commuting ordered pairs 3129 maximal cliques checked True`; `PASS 3 3 idempotents 1433 commuting ordered pairs 101929 maximal cliques checked False`; final `VERIFY_OK`. This finite evidence does not prove the theorem for untested parameters. Its general proof uses the algebraic reasoning in `RESULT.md`. No independent external audit has occurred.
