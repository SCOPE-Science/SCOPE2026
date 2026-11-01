---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Let the 16 graph vertices be even-parity five-bit masks, with edges when XOR weight is four; this is the 5-regular folded five-cube with exactly 40 edges. Ind_2 consists exactly of subsets whose induced degrees are <=1 (every connected component at most two vertices). Fresh complete enumeration of 65,535 nonempty masks produced exactly 2,142 faces with f=(16,120,400,660,576,280,80,10). Independently reconstructed sequential 16-vertex toggle pairing gave 1,070 pairs and precisely two critical simplices (a 0-cell and a 4-cell); complete 9,280-incidence reversed-Hasse topological sort visited all 2,142 faces, establishing a Morse CW model S4, not just its homology. Even-bit translations and permutations of five coordinates act faithfully, giving subgroup T⋊S5 of size 16×120=1920. A graph automorphism fixing zero injects into permutations of its five weight-four neighbors since other vertices are uniquely specified by common-neighbor patterns, so this is the full group. Fresh independent signed invariant-face Lefschetz calculations for every one of all 1,920 automorphisms obtained degree sgn(permutation) on top integral H4 (960 positive, 960 negative). This is a statement about H4 as an integral rank-one character, not an equivariant S4 homotopy equivalence.

## originality

PASS

Qualified originality PASS: Deshpande-Singh 2021 primary arXiv full HTML defines identical higher-independence functor and develops homotopy formulas for complete multipartite, fully whiskered, paths, cycles and perfect trees; its theorem list and Section 6 contain no Clebsch graph classification. The general known sequential matching method is credited as an antecedent. Sawant 2026 is restricted to tree r-independence complexes. The same 5-regular Clebsch model appears in Xu et al. 2025 for Hadwiger/minor questions, not Ind_2 homotopy. Prior ordinary Clebsch Ind_1 and open-neighborhood complexes are different functors. No earlier exact Ind_2(Clebsch) sphere plus affine orientation character was located; hidden computation and tables remain priority risks.

## value

PASS

The 5-regular Clebsch/folded-five-cube graph is a canonical small nonchordal strongly regular graph, outside available general Ind_2 graph families. Determining its nonpure eight-dimensional face complex is nonetheless homotopy S4 and identifying its full 1920-element affine orientation character is a motivated exact invariant: neither follows from ordinary independent-set homology or abstract group order. The result is bounded to one naturally selected graph and functor, consistent with an exact self-contained classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
