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

For crown Cr_n, mixed two-independence faces admit at most two vertices per layer; the neighbor counts force the occupied index sets to coincide in the 2+2 case or share indices in 2+1, so every mixed face lies in tetrahedron T_ij={a_i,a_j,b_i,b_j}; hence X=Delta_A union Delta_B union L, L=union T_ij. Each b_i is dominated by a_i within L, so L strongly collapses to the complete-graph one-skeleton E_A; symmetrically L->E_B. Attaching the two contractible row simplices along E_A,E_B identifies X homotopically with Sigma E_B, a wedge of choose(n-1,2) copies S². Relative integral H2(X,L)≈V⊕V with connecting map (u,v)->u+v; its kernel is anti-diagonal V and layer-swap acts as -1. The boundary map wedge² Z^n -> I_n, e_i wedge e_j -> e_j-e_i, has kernel wedge² I_n as a free integral lattice using split exact Z^n=I_n⊕Z. The exterior-square trace identity yields the exact S_n×C_2 character. Independently enumerated direct-vs-predicted face masks for n=2..5 match 15,38,76,137; other computer proof channels were not upgraded from mod-2 to integral.

## originality

PASS

Previously published results for higher independence of trees, cycles and complete multipartite graphs do not directly cover the crown family for n>3; its uniform integral symmetric-group module and row-swap sign are additional invariants. The Cr3=C6 special case is explicitly recognized as previously covered by cycle work; the global family and lattice are originality target.

## value

PASS

This is a natural infinite matching-deleted complete bipartite graph family, and the complete integral representation distinguishes the result from a finite mod-two Betti table or merely a graph homotopy rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
