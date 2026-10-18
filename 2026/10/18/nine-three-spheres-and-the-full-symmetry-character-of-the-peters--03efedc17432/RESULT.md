# Nine three-spheres and the full symmetry character of the Petersen non-matching complex

## Finding
For the Petersen graph \(P\), the third non-matching complex of its graph edges is
\[
\operatorname{NM}_{3}(P)=\{F\subseteq E(P):\nu(F)<3\},
\qquad
\operatorname{NM}_{3}(P)\simeq\bigvee^{9}S^{3}.
\]
Here \(\nu(F)\) is the maximum size of a pairwise vertex-disjoint collection of edges belonging to \(F\). In particular, its only nonzero reduced integral homology is \(\widetilde H_3\cong\mathbb Z^9\). The natural action of \(\operatorname{Aut}(P)\cong S_5\) on rational third homology is
\[
\widetilde H_3(\operatorname{NM}_{3}(P);\mathbb Q)
\cong \mathbb Q[\tbinom{[5]}{2}]\ominus\mathbb Q
\cong S^{(4,1)}\oplus S^{(3,2)}.
\]
The first expression means the nine-dimensional augmentation subspace of the ten-dimensional permutation representation on two-subsets; the second denotes the two standard rational Specht modules of dimensions four and five. The direct summand symbol in the middle identifies a representation in characteristic zero, not an integral splitting assertion.

## Assumptions and scope
The graph \(P\) is the ten-vertex Petersen graph, equivalently the Kneser graph on the two-element subsets of a five-element set: two such vertices are adjacent precisely when their two-subsets are disjoint. The simplicial vertices of \(\operatorname{NM}_{3}(P)\) are the fifteen edges of \(P\), not the ten graph vertices. The empty face belongs to the augmented face set. Each nonempty face is an edge subset with matching number at most two. The homotopy and homology are integral and nonequivariant; the symmetry decomposition is rational and equivariant. No claim is made for other graphs or other matching thresholds.

For direct reproducibility, the checker uses a second isomorphic labeling: outer cycle edges \(i\)--\(i+1\), spokes \(i\)--\((i+5)\), and inner star edges \((i+5)\)--\((i+2+5)\), with indices interpreted modulo five in their respective layers. Its graph-isomorphism search explicitly constructs the relabeling to the two-subset Kneser model.

## Proof
**Complete face description.** A subset of the fifteen edge labels is a face if and only if it contains none of the 145 distinct three-edge matchings in the graph. Enumerating subsets against these precisely specified obstructions gives the augmented face counts
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5)
=(1,15,105,310,405,207,30).
\]
This is exhaustive because a graph edge set has matching number at least three exactly when it contains a three-edge matching. The checker constructs the forbidden matching triples from endpoints, rather than a stored list.

**Acyclic discrete-Morse matching.** Order the fifteen graph edges as five outer-cycle edges, five spokes, and five inner-star edges. Reserve the singleton containing the first edge. On the remaining nonempty face poset, at each successive edge index, pair every currently remaining face not containing that edge to its union with the edge whenever that union is also present. Remove paired faces before the next index. This fully specified algorithm yields 530 matched lower/upper face pairs and exactly 12 unmatched cells: a single vertex, ten three-dimensional cells, and one four-dimensional cell. Orient every cover relation in the face Hasse graph downward, except the 530 matched relations which point upward. The checker exhaustively topologically sorts all 1072 nonempty faces under these orientations; all nodes are visited, proving acyclicity of this finite matching and hence the validity of the integral Morse CW model.

**Integral attaching map.** Give every simplex the orientation of its sorted graph-edge labels and use the alternating simplicial boundary. For each matched three-to-four-dimensional pair, eliminate its three-cell by replacing it with the remaining signed boundary of its paired four-cell. Recursive gradient elimination is finite by the verified acyclicity. In the ordered basis of the ten critical three-cells, the boundary of the unique critical four-cell is
\[
(0,0,1,0,1,1,1,1,1,1).
\]
Every nonzero coefficient is a unit. Thus the attaching map from the three-sphere boundary of the four-cell to the wedge of ten three-spheres represents a primitive element of \(\pi_3(\bigvee^{10}S^3)\cong\mathbb Z^{10}\). A unimodular change of degree-three sphere basis sends that attaching map to the inclusion of one sphere, and the attached four-cell cancels it homotopically. Since the CW model has no positive-dimensional cells below degree three, the remaining space is a wedge of nine three-spheres, with no torsion. This is a homotopy conclusion, not an inference solely from Betti numbers.

**Equivariant character.** Every element of \(S_5\) permutes the Petersen graph vertices viewed as two-subsets of five letters, hence induces a signed simplicial permutation on the face chains of this non-matching complex. By the Hopf trace formula the reduced Lefschetz number is the alternating sum of signs of invariant nonempty faces, minus one for the empty augmented simplex. Since all reduced homology is in degree three, the third-homology trace is the negative of that Lefschetz number. Exhaustive signed fixed-face enumeration for all 120 permutations yields:

| Cycle type in \(S_5\) | \((1^5)\) | \((2,1^3)\) | \((2^2,1)\) | \((3,1^2)\) | \((3,2)\) | \((4,1)\) | \((5)\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Trace on \(\widetilde H_3\) | 9 | 3 | 1 | 0 | 0 | -1 | -1 |

For every permutation this trace is exactly its number of fixed two-subsets minus one. Thus its character is the augmentation character of the ten-vertex permutation representation. The standard multiplicity-free decomposition of the two-subset permutation module, \(\mathbf 1\oplus S^{(4,1)}\oplus S^{(3,2)}\), gives the stated rational isomorphism.

## Verification
Run `python -S verify_nm3_petersen.py` with ordinary Python 3; no third-party packages or external datasets are required. The program generates all graph edges, forbidden matchings, faces, matched pairs, directed Hasse arcs, critical cells, signed Morse differential, the explicit Kneser-graph isomorphism, and all \(120\) signed Lefschetz traces. Assertions fail if any stated number, primitive coefficient, acyclicity certificate, or character equality fails. The computation takes place in exact integer arithmetic. In particular, the finite computation exhausts the *entire stated finite complex*; it is not a sampled experiment or an extrapolation to a graph family.

## Relationship to prior work
Linusson, Shareshian, and Welker classify the non-matching complexes of complete graphs and complete bipartite graphs, whose graphs are different from the Petersen graph. Holmsen and Lee give general Leray-number bounds for non-matching complexes of arbitrary graphs and stronger bounds for bipartite graphs. Those bounds do not determine the Petersen complex's integral homotopy type or its automorphism representation. Shan and Wang study edge-addition maps and algebraic invariants for non-matching complexes of bipartite graphs; the Petersen graph is not bipartite. The present exact classification thus supplies a nonbipartite benchmark and an equivariant refinement, not a restatement of the cited complete-graph classification. The ordinary matching complex, the vertex-degree-restricted two-matching complex, and graph cut complexes use different face conditions and cannot be substituted for this one.

## Limitations
This is a finite Petersen-graph result, not an arbitrary-graph structure theorem. The integral claim is nonequivariant; only the rational character is calculated equivariantly. General upper bounds alone do not establish this result. A complete-text comparison with the September 2026 bipartite edge-addition preprint was unavailable, so an unexpected discussion of nonbipartite examples there remains an originality risk; its accessible statement and abstract impose bipartiteness on the principal theorem. Other unindexed equivalent calculations may exist. The computational proof is fully specified and independently replayable but has not received independent scientific audit.

## References
1. J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley–Reisner ideals*, arXiv:2609.02621, first posted 2026-09-02, https://arxiv.org/abs/2609.02621.
2. S. Linusson, J. Shareshian, and V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345, first posted 2004-10-15, https://arxiv.org/abs/math/0410345.
3. A. F. Holmsen and S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270, first posted 2020-03-25, https://arxiv.org/abs/2003.11270.
