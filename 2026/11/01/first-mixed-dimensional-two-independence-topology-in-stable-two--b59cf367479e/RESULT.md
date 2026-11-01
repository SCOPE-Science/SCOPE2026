# First mixed-dimensional two-independence topology in stable two-subset Kneser graphs

## Finding
For each integer \(k\) with \(0\le k\le6\), let \(SG_{2,k}\) denote the stable two-subset Kneser graph defined below. Its two-independence complex has the following **integral homotopy classification**:

\[
\begin{array}{c|c}
k&\operatorname{Ind}_2(SG_{2,k})\\\hline
0&*\\
1&S^1\\
2&S^2\\
3&\bigvee^{6}S^2\\
4&\bigvee^{13}S^2\\
5&\bigvee^{20}S^2\\
6&\bigvee^{26}S^2\vee\bigvee^{2}S^3.
\end{array}
\]

Thus the first nonzero reduced integral third homology within the entire nonnegative-parameter family occurs at \(k=6\), where it is \(\mathbb Z^2\). This is a statement about the **higher** two-independence complexes, not the ordinary independence complexes. The claim does not extend beyond \(k=6\).

## Assumptions and scope
For \(k\ge0\), write \(m=k+4\) and regard \(\{0,1,\ldots,m-1\}\) as vertices of a cyclic \(m\)-gon. A stable pair is an unordered pair \(\{i,j\}\) that is not an edge of this cyclic polygon. The vertices of \(SG_{2,k}\) are the stable pairs, with two vertices adjacent exactly when the corresponding pairs are disjoint. For every simple graph \(G\), \(\operatorname{Ind}_2(G)\) is the simplicial complex of vertex subsets \(A\) such that every connected component of \(G[A]\) has at most two vertices. Equivalently \(G[A]\) has maximum degree at most one. The empty face is included. All homotopy equivalences are of geometric realizations, and all homology groups are over \(\mathbb Z\) unless stated otherwise.

## Proof
**1. Exhaustive face construction.** Index the \(\binom{m}{2}-m\) stable pairs lexicographically. Encode every selected family of stable pairs by a nonnegative bit mask. Enumerate faces recursively in increasing maximum selected index. To add index \(j\) to a valid face \(A\), count its already selected neighbors \(N(j)\cap A\). The enlarged set is valid precisely when there are at most one such neighbor and, if one exists, that neighbor has degree zero in \(G[A]\). This is necessary and sufficient because only degrees of \(j\) and its old neighbors can change. Every nonempty valid face has a unique parent obtained by deleting its largest indexed vertex, so the enumeration is exhaustive, not a sample.

**2. Finite discrete-Morse reductions.** Use the explicit vertex permutations in `verify_stable_kneser_two_independence.py`. At each vertex in that permutation, pair each still unmatched face omitting the vertex with its one-vertex enlargement when both are still unmatched. The checker constructs every codimension-one face-poset incidence and reverses precisely the matched incidences. A complete topological sort traverses all vertices of every resulting directed incidence graph, verifying acyclicity. This supplies an actual acyclic discrete-Morse matching for each finite complex. Matching the empty face removes the ordinary base-point critical cell; in the reduced Morse description a base point is implicit.

**3. Exact integral Morse differentials.** Orient each simplex by increasing vertex index. If a lower simplex \(f\) is matched to an upper simplex \(u\), express the projection of \(f\) to the critical chain group via
\[
 P(f)=-\varepsilon(f,u)^{-1}\sum_{\substack{g\subset u\\|g|=|f|\\g\ne f}}\varepsilon(g,u)P(g),
\]
where \(\varepsilon(g,u)\in\{+1,-1\}\) is the simplicial incidence sign. Put \(P(f)=f\) for a critical simplex and \(P(f)=0\) for an upper member of a matched pair. The acyclic directed incidence graph makes the recursive expression well founded. The exact integral critical boundary is \(\partial^M(c)=\sum_{f\subset c}\varepsilon(f,c)P(f)\). The checker constructs all such coefficients and verifies \(\partial^M\circ\partial^M=0\).

The following are the **actual certificate counts**. The face total includes the empty face. The columns \(c_i\) count the critical \(i\)-cells; \(r_i\) are the integer ranks of \(\partial_i^M\). Unlisted critical dimensions are absent.

| \(k\) | faces | critical \((c_1,c_2,c_3)\) | \((r_2,r_3)\) | reduced integral Betti ranks \((\beta_1,\beta_2,\beta_3)\) |
|---:|---:|---:|---:|---:|
| 0 | 4 | (0,0,0) | (0,0) | (0,0,0) |
| 1 | 21 | (1,0,0) | (0,0) | (1,0,0) |
| 2 | 93 | (0,1,0) | (0,0) | (0,1,0) |
| 3 | 316 | (1,7,0) | (1,0) | (0,6,0) |
| 4 | 851 | (1,14,0) | (1,0) | (0,13,0) |
| 5 | 1948 | (1,30,9) | (1,9) | (0,20,0) |
| 6 | 4006 | (1,48,23) | (1,21) | (0,26,2) |

The integer boundary matrices undergo exact unimodular row and column elimination using only pivots \(+1\) and \(-1\), leaving the zero matrix after the stated number of pivots. In particular, there are **no nonunit Smith factors** and no torsion in any listed homology group. An independent reduction of the original full simplicial boundary matrices over \(\mathbb F_2\) reproduces every Betti rank; it is an independent check but not used as an integral proof.

**4. From chain data to the asserted homotopy types.** For \(k=0,1,2\), the critical-cell descriptions directly give a point, a circle, and a two-sphere, respectively. For \(k=3,4,5,6\), there is exactly one critical one-cell and the integral Morse two-boundary contains a unit. The corresponding two-cell attaching map to the one-skeleton has degree \(\pm1\), and the one-cell/two-cell pair cancels homotopically. The remaining two-skeleton is a wedge of two-spheres. Because it is simply connected, the Hurewicz map \(\pi_2\to H_2\) is an isomorphism. Thus each attaching map of a critical three-cell is completely represented by its integral degree column in the remaining two-sphere basis. The unit Smith reductions split off \(r_3\) contractible two-cell/three-cell pairs, leaving precisely \(\beta_2\) two-spheres and \(\beta_3\) three-spheres. There are no critical cells of dimension at least four. This proves the claimed **homotopy equivalences**, rather than merely an assertion about homology.

## Verification
Execute the self-contained Python standard-library checker:

`python3 verify_stable_kneser_two_independence.py`

It regenerates the seven graphs, all faces and Morse pairs; verifies all directed Hasse incidences by exhaustive topological sorting; computes signed Morse boundaries from the actual matching; checks that their compositions vanish; and carries out exact integer unit-pivot eliminations. It separately computes mod-two homology directly from original simplicial boundaries. The expected final output is `STABLE_KNESER_TWO_INDEPENDENCE_TRANSITION_VERIFIED`. The supplied `verification_output.txt` was obtained by running the embedded checker. The finite certificate covers exactly \(0\le k\le6\).

## Relationship to prior work
Braun's *Independence Complexes of Stable Kneser Graphs* (arXiv:0912.0720, Theorem 1.4 and Section 3) classifies **ordinary** \(\operatorname{Ind}(SG_{2,k})\), which is a wedge of two-spheres for \(k\ge4\). It does not determine \(\operatorname{Ind}_2(SG_{2,k})\). Deshpande and Singh's *Higher Independence Complexes of Graphs and Their Homotopy Types* (arXiv:2001.05448, publicly available January 15, 2020) develops the higher complex and classifies complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect \(m\)-ary trees, not stable Kneser graphs. The chordal-graph results of Abdelmalek et al. (arXiv:2106.10863) cannot subsume the present claim: \(SG_{2,6}\) has an induced four-cycle on the stable pairs \(\{0,2\},\{0,3\},\{1,4\},\{1,5\}\), and is not chordal. Previously indexed work on dihedral representations of the **ordinary** stable-Kneser independence complex and on \(\operatorname{Ind}(SG_{4,2})\) likewise concerns distinct complexes. No stronger covering calculation was identified in the checked literature. This is a best-knowledge originality comparison, not a claim that unpublished work cannot exist.

## Limitations
The theorem is an exact initial-segment classification, **not** an infinite-family formula or an extrapolation to \(k\ge7\). The largest enumerated complex has 4,006 augmented faces; while its graph has 35 vertices, the face enumeration is exhaustive by the recursive criterion. The proof does not determine equivariant homology, shellability, or filtration inclusion maps. A complete search of unpublished manuscripts is impossible; an unindexed equivalent remains a residual originality risk. Independent audit is not asserted.

## References
1. Benjamin Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720 (public December 3, 2009), Theorem 1.4 and Section 3; Electronic Journal of Combinatorics 18 (2011), P118.
2. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first posted January 15, 2020), especially Sections 1–3 and the classification list in the introduction.
3. Fred M. Abdelmalek, Priyavrat Deshpande, Shuchita Goyal, Amit Roy, and Anurag Singh, *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863 (first posted June 21, 2021), introduction and main chordal/tree results.
