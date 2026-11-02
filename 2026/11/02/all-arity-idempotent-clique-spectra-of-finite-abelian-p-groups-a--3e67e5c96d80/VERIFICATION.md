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

Run `python verify.py` using Python 3 and only its standard library. The program enumerates every permissible matrix coefficient in the endomorphism ring of each listed small finite abelian p-group, tests idempotence by explicit modular multiplication, and constructs the commuting graph independently of orbit-count formulas. It compares direct counts of ordered commuting tuples of lengths one, two, and three, and computes every maximal clique by Bron–Kerbosch recursion.

The verified groups are \((p; a_1,\ldots,a_n)=(2;1,2),(2;1,3),(2;1,1,2),(2;1,1,3),(3;1,2),(3;1,3)\). The output is `CHECK_OK` for each group and ends in `VERIFY_OK`.

For \(p=2\), the rank-two pairs both have \((T_1,T_2,T_3,M)=(10,52,232,4)\), and the rank-three pairs both have \((82,1636,18376,48)\). For \(p=3\), the two rank-two groups both have \((20,112,512,9)\). Their maximal clique sizes are respectively \(4\) and \(8\). The verifier depends on no unseen data or files.

These finite checks do not prove an arbitrary-prime, arbitrary-rank, arbitrary-exponent, or arbitrary-arity theorem. The infinite result follows from the direct-sum, automorphism and orbit-stabilizer proof in `RESULT.md`. Literature priority remains qualified as specified in `REVIEW.md`.
