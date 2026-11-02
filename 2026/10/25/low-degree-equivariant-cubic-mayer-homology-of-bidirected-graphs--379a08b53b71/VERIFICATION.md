---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For finite connected simple graph n>=2 with no triangles/four-cycles, the directed graph uses BOTH orientations of every edge and the nonregular cubic Mayer differential ∂(v0,...,vk)=sum ξ^j delete_j, with ξ a primitive cube root. Distinguish allowed words and unallowed repeated-coordinate faces. Ω0=CV and Ω1=C^(oriented edges); opposite arc boundary columns give rank ∂1=n. A length-two walk with distinct endpoints has a uniquely inadmissible middle deletion by girth>=5, so Ω2 contains only backtracks with local coefficients summing to zero, giving dim Ω2=2m-n. In degree three successive unique forbidden faces force every walk coefficient zero, hence Ω3=0. On the backtrack balance lattice, ∂ is injective by invertible opposite-arc 2x2 blocks, whereas ∂²b_vw=e_v-e_w and its image is the span of equal-neighbor vertex differences, rank n-c(G), c=2 for bipartite and 1 otherwise. The two distinct q-homologies are therefore β^(3,1)=(c,2m-n,0,0), β^(3,2)=(0,n,2m-2n+c,0); the equivariant port exact sequence gives automorphism trace formulas f_evenclass, f_arcs-f_vertices, f_vertices, f_arcs-2f_vertices+f_evenclass. Finite-field independent construction verifies representative cases but the graph-general forbidden-face proof supplies universality.

## originality

PASS

Qualified new low-degree complete homology and graph-automorphism character classification for the girth>=5 bidirected specialization. Karaguler–Wei 2026 supply the general cubic Mayer differential and local Ω2/Ω3 generator classification, making them substantive prior coverage, but the inspected primary statements do not provide this specialized all-n rank/even-walk-character exact sequence.

## value

PASS

For all connected graph families excluding only 3- and 4-cycles, it supplies complete low-dimensional cubic Mayer homology and every graph-automorphism trace in natural even-walk terms. This is a natural broad structural test class and substantially stronger than checking small graph examples or listing local generators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
