# A boundary-sensitive eight-column classification of three-row perfect-matching complexes

## Finding

Let \(P_n\) be the path on \(n\) vertices and \(C_3\) the triangle. For \(n\in\{2,4,6,8\}\), put \(B_n=P_3\square P_n\) and \(T_n=C_3\square P_n\). For a finite graph \(G\) admitting a perfect matching, let \(\mathcal P(G)\) be the simplicial complex whose facets are precisely its perfect matchings, viewed as sets of edges. The exact homotopy types are:

| \(n\) | Open three-row strip \(\mathcal P(B_n)\) | Periodic three-row strip \(\mathcal P(T_n)\) |
|---|---|---|
| \(2\) | Contractible | Contractible |
| \(4\) | \(S^1\) | \(\bigvee^3 S^1\) |
| \(6\) | \(S^2\) | \(\bigvee^3 S^2\) |
| \(8\) | \(\bigvee^2 S^3\) | \(\bigvee^{12} S^3\) |

In particular, closing the transverse three-row boundary in the eight-column graph changes the third reduced integral Betti number from \(2\) to \(12\). This comparison is not a general formula for longer strips. All six noncontractible complexes displayed above have free integral reduced homology in the indicated degree and no reduced homology elsewhere. They are nonshellable because they are pure of dimension \(3n/2-1\) but have nonzero homology in dimension \(n/2-1\).

## Assumptions and scope

The graphs are finite and simple. Vertices of both strips are \(v_{r,c}\), with \(r\in\{0,1,2\}\) and \(0\le c<n\). Both contain the longitudinal edges \(v_{r,c}v_{r,c+1}\) for \(c<n-1\). The open strip has transverse edges \(v_{0,c}v_{1,c}\) and \(v_{1,c}v_{2,c}\); the periodic strip also has \(v_{0,c}v_{2,c}\). This latter edge closes each three-vertex cross-section into a triangle, not a second longitudinal cycle. The edge order used in the certificate sorts the unordered endpoint pairs lexicographically after identifying \(v_{r,c}\) with the integer \(rn+c\). Only the four even lengths stated in the table are asserted; odd lengths have an odd number of vertices and hence no perfect matching.

## Proof

**Exact construction of the simplices.** For each graph enumerate all perfect matchings recursively: choose the least uncovered graph vertex, pair it in turn with each uncovered neighbor, and recurse on the remaining vertices. Store the chosen graph edges as bits in the specified lexicographic edge order. Every perfect matching has \(3n/2\) edges. The set of all faces of \(\mathcal P(G)\), including the empty face, is exactly the union of the submask sets of the enumerated perfect matchings. No matching that cannot extend to a perfect matching is included.

**A complete Morse matching.** Starting with all faces, visit the edge-vertices \(e_0,e_1,\ldots\) of \(\mathcal P(G)\) in lexicographic order. At stage \(i\), pair every still-unpaired face \(\sigma\) with \(e_i\notin\sigma\) with \(\sigma\cup\{e_i\}\), provided that this larger face is also still unpaired. Remove both faces and proceed. Each stage has disjoint face pairs and every pair is a codimension-one inclusion. The union is an acyclic discrete-Morse matching; the package additionally proves this directly by orienting every cover incidence downward except for the chosen matched incidences, which are reversed, and performing an exhaustive topological sort of that directed Hasse graph.

The independent full-Hasse acyclicity check, face counts, and critical-cell dimensions are:

| Graph | Perfect matchings | Faces including empty | Hasse cover incidences | Unmatched nonempty cells |
|---|---:|---:|---:|---|
| \(B_2\) | 3 | 20 | 34 | None |
| \(B_4\) | 11 | 495 | 1,679 | One 1-cell |
| \(B_6\) | 41 | 12,375 | 62,994 | One 2-cell |
| \(B_8\) | 153 | 309,480 | 2,101,259 | Two 3-cells |
| \(T_2\) | 4 | 26 | 45 | None |
| \(T_4\) | 19 | 817 | 2,817 | Three 1-cells |
| \(T_6\) | 91 | 25,769 | 133,212 | Three 2-cells |
| \(T_8\) | 436 | 812,758 | 5,600,955 | Twelve 3-cells |

In every row the empty face is paired. The exact counts follow from the attached terminating integer/bitset enumeration, rather than an induction or extrapolation. The acyclic matching theorem of discrete Morse theory therefore yields a CW complex with one 0-cell and only the listed positive-dimensional cells. Since there are no other positive-dimensional cells, all attaching maps are constant (for 1-cells, both endpoints attach to the single vertex). The resulting CW complex is the asserted wedge of spheres, or a point when no unmatched cells remain.

Finally, every facet of \(\mathcal P(G)\) is a perfect matching containing exactly \(3n/2\) edges, so the complex is pure of dimension \(3n/2-1\). For \(n=4,6,8\) the positive-dimensional reduced homology occurs strictly below the facet dimension, contradicting the homology concentration of a pure shellable complex. This proves the nonshellability assertion.

## Verification

Run `python3 verify_strip_boundary.py` using Python 3's standard library; the complete recorded output is `verification_output.json`. The checker regenerates both graph families and the perfect matchings, verifies each matching covers every graph vertex exactly once, enumerates every simplicial face, constructs every stage of the toggle pairing, checks pair disjointness and codimension, enumerates all Hasse cover incidences, reverses precisely the paired incidences, and topologically sorts the full directed Hasse graph. It checks that every directed vertex is visited and that the processed incidence total equals the enumerated total; thus this is a complete finite acyclicity certificate, not a sampled test. It independently compares the alternating face count against the critical-cell alternating count. The marker is `THREE_ROW_BOUNDARY_PERFECT_MATCHING_MORSE_OK`.

## Relationship to prior work

Chandrakar and Singh (arXiv:2407.05809, initially public July 8, 2024) classify the two-row open rectangular case and conjecture in their Section 6 that all rectangular grid perfect-matching complexes are wedges of spheres. The present open \(B_8\) calculation is a finite width-three instance of that conjecture, while \(T_8\) changes the *transverse* boundary to a triangle and does not follow from the cited two-row result. The same paper's polygonal line tilings are single chains of polygons; a triangular cross-section linked by multiple square faces is not such a line tiling. Bayer, Jelić Milutinović, and Vega (arXiv:2209.02803) analyze honeycomb tilings, rather than these square/triangular strips. Agarwal and Basak (arXiv:2608.30601) analyze Möbius ladders, which are cubic and have a different vertex and edge structure. No inspected result covers the complete boundary comparison above; unseen equivalent calculations remain a literature risk.

## Limitations

The proof is an exact finite exhaustive computation for eight explicitly defined complexes, not a uniform classification of all \(n\). The nondiagonal rank jump at \(n=8\) is observed within the verified cutoff; no recurrence, asymptotic law, or claim about the next even length is established. The certificates prove homotopy types without an externally performed audit. The use of discrete Morse theory depends on the standard acyclic-matching theorem; correctness of the numerical claims depends on executing or independently reproducing the included finite checker.

## References

1. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first public July 8, 2024, especially Theorem 3.3, Conjecture 6.1, and the element-pairing theorem in Section 2. https://arxiv.org/abs/2407.05809
2. M. Bayer, M. Jelić Milutinović, and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803, first public September 6, 2022. https://arxiv.org/abs/2209.02803
3. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601, first public August 31, 2026, particularly Theorem 18. https://arxiv.org/abs/2608.30601
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
