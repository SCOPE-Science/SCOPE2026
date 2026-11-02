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

## Checks actually performed

Run `python3 checker.py` using standard Python 3. The checker enumerates 153 nonempty faces of the Paley-17 independence complex and excludes all size-four independent sets. It tests an explicit nonresidue complement map, constructs 68 disjoint face pairs, forms every one of the 340 Hasse covers and proves the oriented matching graph acyclic via a complete topological sort. The unmatched cells have dimension profile one in degree zero and sixteen in degree two. Independent mod-two chain-boundary ranks are 16 and 52. It then checks all 136 affine simplicial automorphisms by exact signed chain Lefschetz traces, including the order-two multiplier's four orientation-reversing fixed edges and four fixed triangles. Character frequencies are 16 once, -1 sixteen times and 0 one hundred nineteen times.

The finite checker proves exhaustive finite assertions but does not verify statements about Paley graphs of other orders, classify larger automorphism groups, or determine integral torsion in the quotient. The final theoretical steps are the standard discrete-Morse CW theorem, the rational character theorem for finite groups, and rational chain averaging for finite quotients. The accompanying script does not constitute independent external validation.
