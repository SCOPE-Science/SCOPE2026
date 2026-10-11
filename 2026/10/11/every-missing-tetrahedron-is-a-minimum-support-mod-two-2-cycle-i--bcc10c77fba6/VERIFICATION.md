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

The packaged `verify.py` reconstructs the 68 published 4-simplices and all lower-dimensional faces. It verifies the face vector \((11,55,150,170,68)\), exact mod-two ranks \(\operatorname{rank}\partial_2=45\) and \(\operatorname{rank}\partial_3=103\), and hence \(\dim H_2=2\).

It enumerates all four-vertex sets. Exactly 58 have all four triangular faces present but are not tetrahedra. For every one, its boundary is checked to lie outside \(\operatorname{im}\partial_3\) both by canonical reduction and by an independent rank-increase test. Pairwise differences modulo \(\operatorname{im}\partial_3\) partition them into the three nonzero homology classes with support counts \(6\), \(24\), and \(28\).

The proof that support four is minimal is not inferred from finite search alone: a nonzero simplicial mod-two 2-cycle requires at least four vertices, and on exactly four vertices the even-edge condition forces the full tetrahedral boundary. Thus the exhaustive four-set computation classifies all minimum supports.

The verification does not address integral homology classes or other triangulations of \(S^2\times S^2\).
