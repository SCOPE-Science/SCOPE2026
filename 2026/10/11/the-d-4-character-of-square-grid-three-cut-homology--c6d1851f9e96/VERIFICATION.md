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

Independently checked the final all-integer n>=3 theorem for the ORDINARY three-cut complex, its reduced homology degree d=n^2-4, geometric D4 action, orientation signs and rational isotypic multiplicities. In the cited primary paper, Proposition 2.18 gives the truncated Boolean face poset minus complements of connected three-vertex paths and unit 4-cycles; Propositions 5.6 and 5.8 ensure shellability and unique top rational (indeed free integral) homology, with Betti number B=(n^4-13n^2+20n-4)/2. A fixed oriented face contributes its permutation sign; the reduced alternating full Boolean chain trace cancels, while deletion of complements of sizes 0,1,2 and the two exceptional strata gives χ(g)=ε(g)[1-f(g)+C(f(g),2)-t(g)-p(g)+q(g)] with exact alternating and complement-orientation signs. Enumerated symbolically the orbit types for identity, quarter-turn, half-turn, axial and diagonal reflections, including odd-center paths, even-center square, fixed squares across axes, and diagonal reversed squares. These yield (B,0,2-floor(n^2/2),X,0), with X=n-n^2/2 even and (-1)^((n-1)/2)(3-n) odd. D4 character inner products give (B+H+2X)/8 twice, (B+H-2X)/8 twice, (B-H)/4 copies of the rational 2D standard irrep; positivity follows from the actual rational module. Separate independent Python code built grid actions and connected paths/squares from scratch, checked signed traces and multiplicities for every 3<=n<=14, and performed COMPLETE defining-face signed reduced supertraces for n=3,4 (n=3: (10,0,-2,0,0); n=4: (62,0,-6,-4,0)). The universal proof is combinatorial and uses the actual source theorem; bounded checks are only corroborative. Seven current frozen Git blobs were directly read and independently SHA-1 matched to the assigned source tree.

## originality

PASS

Best-of-knowledge novelty attaches ONLY to the explicit all-n five-class D4 homology character and full Q[D4] multiplicities for square-grid ORDINARY three-cut complexes. The 2024/2025 primary grid theorem covers the ordinary 3-cut face lattice, shellability and scalar top Betti rank B, not the symmetry character; the same paper uses Hopf trace to compute modules for disjoint unions of complete graphs and for paths and cycles, not square grids. The closer 2026 grid paper concerns total 3-cut complexes of fixed-height grids and ordinary k-cut shellability in 2-row grids. Fresh Resultary and literature searches found a record with the same title and statement (the TARGET itself, not independent prior art), but the nearest separately published square-grid D4 calculation concerns a total three-cut complex of the 4x4 grid, which is a distinct subcomplex and has degree-10 homology rank 36 rather than degree-12 ordinary rank 62. Generic Hopf trace can theoretically derive the character, but the signed invariant-path and square-count computations and parity-sensitive all-n representation were not stated or immediately implied as an evaluated special case. No earlier mathematical statement was located that dominates this complete equivariant classification. Search incompleteness and ease of derivation from published ingredients remain explicit originality risks.

## value

PASS

For a canonical square grid the natural dihedral automorphism group acts on an already-known top-homology group, but the non-equivariant rank does not specify the isotypic decomposition. Determining the entire D4-character and four rational one-dimensional isotypic multiplicities plus standard two-dimensional multiplicity for EVERY n>=3 is a complete structural invariant, not a one-off enumeration. The parity-dependent axial traces, nontrivial half-turn traces and exactly vanishing diagonal/quarter-turn traces distinguish geometrically different symmetries. The computation requires signed orientation and combinatorial orbit analysis, is motivated by equivariant topology/symmetry-sensitive comparisons, and is not a routine re-expression of the scalar Betti count. Exact dimensions could inform future equivariant comparisons; no theorem beyond the explicit module, no integral action and no canonical generator basis is promised.

The dated certificate retains the supplied scientific assessment, sources and limitations.
