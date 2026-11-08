---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independently reconstructed cubic Franklin graph and enumerated all 4096 vertex subsets; precisely 723 augmented faces with cardinalities 1,12,66,184,264,168,28. Exhaustive toggle matching gives 357 augmented pairs and 9 critical faces, equivalently 356 nonempty pairs with one critical vertex, two 3-cells and seven 4-cells; 2748 Hasse incidences have no directed cycle. Fresh signed integral Morse reduction independently reproduces the 2-by-7 differential with columns (1,0),(1,0),(1,-1),(0,-1),(0,0),(0,-1),(-1,1), containing unit minor -1. The 3-skeleton is two S3 spheres, and unimodular attachment cancellation gives wedge5 S4, not merely mod2 homology. Independent automorphism enumeration finds order48 and signed fixed-simplex Lefschetz traces by cycle type [id:5, 1^8 2^2:-3 x3, 1^4 2^4:1 x3, 2^6:-1 x12 and +1 x1, 2^2 4^2:1 x12, 3^4:-1 x8, 6^2:1 x8]. Weighted trace sum is zero, so rational H4 has no invariants; rational homology of finite simplicial quotient equals invariants after subdivision, proving rationally acyclic quotient (not contractible).

## originality

PASS

Primary-theorem/parameter/complex comparison and semantic Resultary query ('Franklin graph 2-independence complex homotopy automorphism character quotient rational homology') found no examined theorem that implies the precise claim. Matching graph names, smaller parameters, different simplicial constructions and broad hypotheses were compared by mathematical implication; failed retrieval is not absolute novelty proof. See four structured comparisons and residual risks.

## value

PASS

The Franklin graph is a canonical symmetric 12-vertex cubic graph with a nontrivial order48 automorphism group. This finite classification couples a nontrivial integral Morse attaching-matrix unit minor to the full equivariant homology character and a surprising rationally acyclic quotient, natural exact invariants beyond routine Betti recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
