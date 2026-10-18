# Complete higher-independence homotopy and persistence of the Petersen graph

## Finding
For the Petersen graph \(P=KG(5,2)\), let \(K_r=\operatorname{Ind}_r(P)\) be the simplicial complex of vertex subsets whose induced connected components each have at most \(r\) vertices. For all integers \(r\ge 1\), the **integral homotopy type** is completely classified:

| \(r\) | Homotopy type of \(K_r\) |
|---|---|
| \(1\) | \(\bigvee^4 S^2\) |
| \(2\) | \(S^3\) |
| \(3\) | \(S^3\) |
| \(4\) | \(\bigvee^{11} S^3\) |
| \(5\) | \(\bigvee^{61} S^4\) |
| \(6\) | \(\bigvee^{74} S^5\) |
| \(7\) | \(\bigvee^{36} S^6\) |
| \(8\) | \(\bigvee^{9} S^7\) |
| \(9\) | \(S^8\) |
| \(r\ge 10\) | a point |

Moreover, the complete **reduced persistence barcode over \(\mathbb F_2\)** of the inclusions \(K_1\subseteq K_2\subseteq\cdots\) comprises the following half-open intervals (the last column gives multiplicity):

| Homological dimension | Parameter interval | Multiplicity |
|---|---|---|
| \(2\) | \([1,2)\) | \(4\) |
| \(3\) | \([2,5)\) | \(1\) |
| \(3\) | \([4,5)\) | \(10\) |
| \(4\) | \([5,6)\) | \(61\) |
| \(5\) | \([6,7)\) | \(74\) |
| \(6\) | \([7,8)\) | \(36\) |
| \(7\) | \([8,9)\) | \(9\) |
| \(8\) | \([9,10)\) | \(1\) |

In particular, the existing three-dimensional mod-two homology class survives both steps \(K_2\hookrightarrow K_3\hookrightarrow K_4\); ten new independent classes appear in dimension three at parameter four. This persistence statement is **over \(\mathbb F_2\) only**. The ordinary homotopy equivalences above are integral. The one-dimensional unreduced degree-zero class persists indefinitely.

## Assumptions and scope
The Petersen graph is defined without relying on a picture: its ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), and two vertices are joined when their sets are disjoint. Thus \(P=KG(5,2)\), a connected cubic graph with fifteen edges. For \(S\subseteq V(P)\), let \(c(S)\) be the largest number of vertices in one connected component of the induced graph \(P[S]\); put \(c(\varnothing)=0\). Then \(K_r\) consists of the subsets satisfying \(c(S)\le r\). This family is nested because deleting vertices cannot increase the largest component size. The bar convention is \([b,d)\): a class is present at integer stages \(r\) satisfying \(b\le r<d\).

## Proof
Every step is a finite combinatorial statement, completely reproducible from the three accompanying artifacts. Label the Petersen vertices in lexicographic order as `01,02,03,04,12,13,14,23,24,34`, and encode a nonempty subset \(S\) by the integer bit mask \(\sum_{i\in S}2^i\). There are exactly \(2^{10}-1=1023\) possible nonempty faces across the filtration. Membership in \(K_r\) is decided by a breadth-first traversal of the induced adjacency masks. In each of the ten stages, the artifact `certificate.json` gives an exhaustive sequence of two types of steps on the current face family.

A `P` step `["P",lower,upper]` removes a codimension-one face and its **unique currently remaining codimension-one coface**. The verifier checks that both masks are present, that their dimensions differ by one, and that no other codimension-one coface remains. Because the remaining face family is downward-closed at each stage, this also implies that the upper face is maximal; the removal is therefore an elementary simplicial collapse. A `C` step `["C",cell]` removes a currently maximal face and declares it an unmatched critical cell. The verifier confirms maximality and eventually exhausts every nonempty face.

These removals provide an acyclic matching on the face poset: any alternating gradient path leaving a matched upper face for a distinct lower face must move to a pair removed **later** than the starting pair. It cannot return to an earlier pair, so no closed gradient path exists. The numbers of remaining critical cells (all dimensions are geometric face dimensions) are:

| \(r\) | Nonempty faces | Matched pairs | Critical cells |
|---|---:|---:|---|
| \(1\) | 75 | 35 | one vertex, four 2-cells |
| \(2\) | 260 | 129 | one vertex, one 3-cell |
| \(3\) | 380 | 189 | one vertex, one 3-cell |
| \(4\) | 510 | 249 | one vertex, eleven 3-cells |
| \(5\) | 702 | 320 | one vertex, sixty-one 4-cells |
| \(6\) | 857 | 391 | one vertex, seventy-four 5-cells |
| \(7\) | 967 | 465 | one vertex, thirty-six 6-cells |
| \(8\) | 1012 | 501 | one vertex, nine 7-cells |
| \(9\) | 1022 | 510 | one vertex, one 8-cell |
| \(10\) | 1023 | 511 | one vertex |

Discrete Morse theory supplies a CW complex with exactly these cells. Because no positive-dimensional critical cell occurs below dimension two, every positive-dimensional cell is attached to the single vertex and has a constant attaching map. Hence each stage is homotopy equivalent to the stated wedge of spheres. The ten-vertex simplex is \(K_{10}\), and thus also \(K_r\) for all \(r\ge10\). This proves the homotopy classification over the integers, not merely the ranks over a field.

For persistence, assign filtration index \(c(S)\) to each nonempty face, and order all 1023 faces by the triple `(largest component size, face cardinality, numerical mask)`. Every boundary face precedes its coface. The accompanying independent calculation constructs every unsigned simplicial boundary matrix over \(\mathbb F_2\) and performs exact left-to-right column reduction. A nonzero reduced boundary column pairs its pivot birth with the present death; reducing to zero produces a birth. The difference between the filtration indices of each birth and death yields exactly the eight displayed types of nonzero-length bars. Zero-length bars are excluded. One unpaired zero-dimensional class remains. The same verifier separately computes all ten ordinary reduced \(\mathbb F_2\) homology vectors, providing a cross-check of both the critical-cell counts and the interval endpoints.

## Verification
Run `python3 verify.py certificate.json` with standard Python 3 from the directory containing the artifacts. `verify.py` independently constructs graph adjacency, determines every face at each parameter, and verifies every recorded match, free-face condition, critical-face condition, final exhaustion, and critical-cell dimension. It also computes full boundary ranks and filtration-reduction intervals over \(\mathbb F_2\). The actual recorded output is `verifier_output.txt`. All assertions passed. These exhaustive finite checks verify the entire object, rather than extrapolating from small samples; the topological inference is given explicitly above.

## Relationship to prior work
Higher independence complexes are established objects. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees* (2026), establishes vertex decomposability for trees, but the Petersen graph contains induced 5-cycles and is not a tree. Deshpande and Singh study general constructions as well as special graph classes, but do not give this Petersen filtration. Ghosh and Selvaraja establish general shellability for parameters near the number of vertices; their theorem already applies at parameters eight and nine but does not specify the ranks or the inclusion maps here. Deshpande, Roy and Sawant examine the Alexander dual and Fröberg-type criteria for particular graph classes; this does not determine the complete integral homotopy profile or this mod-two persistence barcode.

The already recorded Petersen two-independence homotopy type \(K_2\simeq S^3\) is **not** claimed as new, nor is the ordinary independence complex at parameter one. The new combined finding determines the higher stages \(3\) through \(9\) and every nonzero mod-two persistence interval. This is not a calculation of the graph-metric Čech or Vietoris–Rips filtration, nor of an ordinary matching complex.

## Limitations
Only one fixed canonical ten-vertex graph is classified; there is no claim of a formula for other graphs. The persistence decomposition is proved over \(\mathbb F_2\), not as a decomposition of persistence modules over \(\mathbb Z\). The computation does not determine equivariant actions or explicit integral attaching maps between consecutive stages. Originality cannot be guaranteed against unindexed or unpublished equivalent classifications. Independent scientific audit has not been performed.

## References
- Rutuja Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (first posted 2026-05-24), https://arxiv.org/abs/2605.25150 .
- Priyavrat Deshpande and Anurag Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, https://arxiv.org/abs/2001.05448 .
- Arka Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614v3, https://arxiv.org/abs/2505.06614 .
- Priyavrat Deshpande, Amit Roy and Rutuja Sawant, *The complex of \(r\)-co-connected subgraphs, chordality and Fröberg's theorem*, arXiv:2510.25710v2, https://arxiv.org/abs/2510.25710 .
- Related exact published Petersen results: published-finding corpus records `2026/10/11/SCOPE-the-2-independence-complex-of-the-petersen-graph-is-a-3-sphere--156dc9567f6a` and `2026/10/11/SCOPE-the-petersen-two-independence-complex-is-a-three-sphere--0d53a7f4e76a` (parameter two only).
