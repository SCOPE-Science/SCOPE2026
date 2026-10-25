---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The definitions force mixed simplices either to have exactly one vertex on A or one on B and at most d on the opposite side, because any induced K_{2,2} is cyclic. At d>=2 cover by X_d = Delta_A plus B-cones on sk_{d-1}Delta_A and Y_d analog; intersection is the literal 1-complex K_{a,b}. For the two covers the skeleton’s augmented boundary contraction kernel is wedge^d U; this gives Hd(X_d)=P_B tensor wedge^d U_A, and the analogous Y term, with no other positive homology. H1(K_{a,b}) is the row/column-sum-zero lattice U_A tensor U_B. Natural integral Mayer–Vietoris yields at d=2 the short exact sequence with T2 and W; for d>=3 the H2 connecting map to W is an isomorphism and Hd=T_d; the inclusion maps and torsion-freeness follow. Stage 1 relative to Delta_A disjoint Delta_B has ab cross-edge generators mapped to the same H0 generator, giving ker augmentation; F0 has reduced H0=Z. Exterior-power trace from det(1+t sigma|U) gives rational characters. Independently reconstructed full simplicial mod3 boundary ranks for K_{2,2}, K_{2,3}, K_{3,3}, K_{3,4} at all stages, consistent with the universal argument; this bounded check does NOT establish all parameters. The stage-two equivariant extension is not asserted to split integrally and part swapping for a=b is excluded.

## originality

PASS

The analysis must distinguish the prior full stagewise homotopy types of F_d(Kab) in Carnero Bravo (Theorem 34 current arXiv rendering; package refers to 33) from new natural persistence maps and S_a x S_b lattice structure. None of the retrieved Resultary analogs identifies the same induced-forest filtration with those natural equivariant maps. This is a bounded best-of-knowledge scientific judgment: an unsuccessful search cannot prove absolute priority.

## value

PASS

The integral side-preserving equivariant persistence for an infinite bipartite family isolates persistent rectangle two-cycles from transient skeleton classes; it is a structural computation useful for equivariant graph-filtration comparisons, not merely known stagewise Betti numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
