# Two-independence homotopy distinguishes the Shrikhande and rook graphs

## Finding
Let \(S\) denote the Shrikhande graph and let \(R=K_4\square K_4\) denote the \(4\times4\) rook graph. These are nonisomorphic strongly regular graphs with the same parameters \((16,6,2,2)\). Define the two-independence complex \(X_G=\operatorname{Ind}_2(G)\), whose faces are the vertex subsets inducing connected components with at most two vertices. Then
\[
\boxed{X_S\simeq\bigvee^{57}S^3,\qquad X_R\simeq\bigvee^{105}S^3.}
\]
Both equivalences are *integral homotopy equivalences*, not conclusions obtained from a finite-field homology computation. In particular, the only nonzero reduced integral homology groups are \(\widetilde H_3(X_S;\mathbb Z)\cong\mathbb Z^{57}\) and \(\widetilde H_3(X_R;\mathbb Z)\cong\mathbb Z^{105}\).

A structural contrast is that the ordinary independence complexes of these two graphs, determined previously, are wedges of \(23\) and \(15\) two-spheres respectively. Thus the rank ordering reverses at the natural next parameter, even though the graphs have equal adjacency spectra.

## Assumptions and scope
The vertex set of either graph is \(V=(\mathbb Z/4\mathbb Z)^2\); encode \((i,j)\) as the integer \(4i+j\), with representatives \(0,1,2,3\). The Shrikhande graph has edges corresponding to the undirected Cayley differences
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}\pmod4.
\]
In the rook graph, two different vertices are adjacent exactly when they share a coordinate. All graphs are finite, simple and loopless, and complexes include the empty face. Since a simple graph has components of size at most two precisely when its maximum vertex degree is at most one, \(X_G\) is equivalently the complex of sets inducing no copy of the three-vertex path \(P_3\) as a not-necessarily-induced subgraph. This is the devoid complex \(\mathcal D(G;P_3)\) in the terminology of Taylan's 2015 paper.

The result is only about these two graphs at parameter two. It does not assert equivariance, a classification of all strongly regular parameter families, or a formula at other parameters.

## Proof
**Graph identification and face criterion.** Let \(N_i\) be the bit mask of neighbors of vertex \(i\). For a subset represented by a \(16\)-bit integer \(m\), the exact face predicate is
\[
\forall i\in V:\quad i\in m\Longrightarrow |N_i\cap m|\le1.
\]
An independent component-search predicate gives the same result on all \(2^{16}\) masks. The graph constructors verify degree six and exactly two common neighbors for each pair of distinct vertices. The induced neighborhood of any vertex is a six-cycle for \(S\), but two disjoint triangles for \(R\), verifying nonisomorphism without invoking a spectral inference.

**Exact face sets.** Exhaustive enumeration yields the nonempty face vectors, in ascending simplex dimension,
\[
 f(X_S)=(16,120,384,544,240,32),\qquad
 f(X_R)=(16,120,384,528,144).
\]
Thus \(X_S\) has \(1336\) nonempty simplices and \(X_R\) has \(1192\). Their maximal faces have dimensions \(3,4,5\) in numbers \(64,48,32\) for \(S\), and dimensions \(3,4\) in numbers \(96,144\) for \(R\); both complexes are nonpure. Each displayed number is checked by `verify.py`.

**Complete acyclic Morse matchings.** Start with every face, including the empty face, unmatched. At successive pivots (integer vertex labels)

`[11, 6, 4, 10, 14, 5, 3, 13, 8, 12, 7, 1, 15, 9, 0, 2]`

match every currently unmatched face \(\sigma\) omitting pivot \(v\) with \(\sigma\cup\{v\}\), provided the latter remains unmatched and is a face. Remove both from later stages. This procedure makes one pair involving the empty face and a vertex. Release that pair, so the ordinary nonempty face poset has one critical vertex instead; retain every other pair. The final numbers of ordinary matched pairs are \(639\) for \(S\) and \(543\) for \(R\). Their unmatched cells are, respectively, exactly one vertex and \(57\) three-simplices, and exactly one vertex and \(105\) three-simplices. There are **no other critical cells** in either dimension.

**Acyclicity is separately certified.** Direct every codimension-one incidence of nonempty faces downward, except an incidence in the specified matching, which points upward. This defines the directed Hasse graph of each Morse matching. The complete graphs have, respectively, \(1336\) nodes and \(4960\) directed covering incidences for \(S\), and \(1192\) nodes and \(4224\) incidences for \(R\). A full topological sort visits every node in each graph. This proves acyclicity, not just the pair count. In addition, `verify.py` checks that every pair is a genuine codimension-one face-coface pair and that no face is paired twice. The stages are also of the standard element-matching form described in Deshpande–Singh, Proposition 2.10.

**Integral homotopy deduction.** The acyclic discrete-Morse matching theorem supplies, for each \(X_G\), a CW model with one zero-cell, no one- or two-cells, and exactly the stated number of three-cells, with no other cells. Since every attaching map of a three-cell lands in the single zero-cell, each is constant. The CW model is consequently the displayed wedge of three-spheres. This argument determines integral homotopy type and rules out hidden torsion or higher attaching-map obstructions for these two complexes. The sphere counts differ, so the homotopy types differ, notwithstanding identical strongly regular parameters.

## Verification
The standalone standard-library Python program `verify.py` is a complete finite certificate for the constructions and the Morse steps. Run it with `python3 verify.py` in the extracted scientific package. It checks both graph presentations, every vertex subset using two logically different predicates, all face and facet counts, each matched covering pair, the complete oriented Hasse diagram, and an exhaustive topological sort. It separately computes ordinary simplicial boundary ranks over \(\mathbb F_2\) to cross-check the reduced Betti numbers. Its expected complete output is embedded as `verification_output.txt`. The terminal marker is `ALL_CHECKS_PASS`.

The mod-two cross-check gives only \(\widetilde\beta_3=57\) for \(S\) and \(\widetilde\beta_3=105\) for \(R\). The *integral* assertion instead follows from the full acyclic matching and the resulting CW cell dimensions; no mod-two-to-integral leap is used.

## Relationship to prior work
Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs* (arXiv:1501.06754v1, first public January 27, 2015), introduced the relevant devoid-complex formalism and analyzed \(\mathcal D(F;P_3)\) for forests and \(\mathcal D(C_n;P_k)\) for cycles. Neither of the two graphs here is a forest or a cycle. The explicit pair of present homotopy types is not among Taylan's inspected statements. Deshpande and Singh (arXiv:2001.05448) study higher independence complexes of complete multipartite and whiskered graphs, paths, cycles and perfect rooted trees, with a further chordal-graph existence assertion. Our graphs have induced four-cycles and are not chordal, and neither is a graph from those classified families.

A published computation of the **ordinary** independence complexes of \(S\) and \(R\) gives \(\operatorname{Ind}_1(S)\simeq\bigvee^{23}S^2\) and \(\operatorname{Ind}_1(R)\simeq\bigvee^{15}S^2\). These are different complexes, and neither ordinary homotopy type determines the higher-independence homotopy type. Another published comparison gives their radius-one intrinsic Čech nerves as wedges of \(23\) and \(63\) two-spheres. Those nerves have entirely different face definitions and do not imply the present result.

A preceding computation on the **same two graphs** concerns \(\mathcal D(G;P_4)\), which allows induced triples with a two-edge path. It calculates integral homology in several dimensions for that larger simplicial complex. Since \(\mathcal D(G;P_3)\subsetneq\mathcal D(G;P_4)\), its results do not determine either present subcomplex's homotopy type. The specific new information here is the exact three-sphere wedge classification at the natural first nontrivial devoid/higher-independence parameter, including its reversal of the ordinary-independence comparison.

## Limitations
These are exact finite calculations for two named graphs, not a general formula for all strongly regular graphs. The full Morse certificate depends on the specified pivot ordering; it is independently checkable but does not produce a conceptual equivariant splitting. It makes no claim for integral graph-automorphism representations, and no assertion concerning homotopy maps induced by inclusion between successive higher-independence complexes. The comparisons cannot exclude an identical result in unindexed or unpublished work. Independent mathematical audit is not asserted.

## References
1. Demet Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1 (2015), especially Definition 3.8, Theorem 3.14 and Theorem 5.2. https://arxiv.org/abs/1501.06754.
2. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448 (first posted 2020), especially Theorem 2.4, Proposition 2.10 and the classification list. https://arxiv.org/abs/2001.05448.
3. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, publicly accessible 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187.
4. *Scale-two Čech homotopy distinguishes the Shrikhande and rook graphs*, publicly accessible 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-scale-two-ech-homotopy-distinguishes-the-shrikhande-and-rook-gra--5b6e4436155e.
5. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, the discrete Morse CW theorem.
