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

Verified the face predicate Ind2(G)=subsets whose induced connected components have ≤2 vertices, equivalently induced maximum degree≤1, on exactly labeled GP(10,k). Independently enumerated all 2^20 subsets, obtaining 63,142 and 62,048 nonempty faces, and independently rebuilt the staged discrete Morse matchings with full global acyclicity topological sorts over every nonempty simplex; matched pairs 31,565 and 31,000, critical cells for k2 (one 0,one 5,six 6,four 7) and k3 (one 0,three 6,fortyfour 7). Independently constructed signed gradient-path boundary matrices: for k2 ∂6=[0,0,−1,0,1,0] and ∂7 rank4 with four unit Smith factors and ∂6∂7=0; k3 ∂7 3×44 with three unit factors. These integral primitive attaching maps allow high-dimensional cell cancellation, because relevant maps S^m→∨S^m are classified by degree in dimensions m≥2; the spaces are S6 and wedge^41 S7, not merely spaces with these Betti groups. No general GP(n,k) or equivariant claim.

## originality

PASS

Best-of-knowledge PASS against true same-graph and same-complex comparisons. Deshpande–Singh introduced higher independence and treat multipartite graphs, cycles, whiskered graphs and trees, not these GP(10,k) pair cases. Kim–Lew I_n(G) imposes absence of an independent set of size n, a different face predicate. Published dodecahedral and Desargues exact ordinary independence calculations classify Ind1, whose homotopy types wedge4 S5 and S4∨5S5 do not imply Ind2. Resultary searches under dissociation/degree-one induced complexes found no exact pair table. Remaining unindexed equivalence risk explicitly retained.

## value

PASS

The dodecahedron and Desargues graph are a canonical matched 20-vertex cubic pair; the first higher-independence level changes ordinary independence topology in a substantial, sharply contrasting way: one single S6 against 41 S7. Complete acyclic matchings and primitive attaching matrices prove genuine integral homotopy, not only finite-field ranks. This is a natural complete two-object classification rather than an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
