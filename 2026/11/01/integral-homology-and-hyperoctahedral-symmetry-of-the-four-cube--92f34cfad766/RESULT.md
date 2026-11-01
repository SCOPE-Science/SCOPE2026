# Integral homology and hyperoctahedral symmetry of the four-cube dominance complex

## Finding

Let \(Q_4\) be the graph on the sixteen binary words \(\{0,1\}^4\), with edges joining words of Hamming distance one. Let its **dominance complex** be
\[
\mathcal D(Q_4)=\{\sigma\subseteq V(Q_4):V(Q_4)\setminus\sigma\text{ is a dominating set}\}.
\]
Its complete reduced **integral** homology is
\[
\widetilde H_j(\mathcal D(Q_4);\mathbb Z)\cong
\begin{cases}\mathbb Z^{10},&j=7,\\ \mathbb Z,&j=9,\\0,&\text{otherwise.}\end{cases}
\]

The full automorphism group \(B_4=(\mathbb Z/2)^4\rtimes\mathfrak S_4\), of order \(384\), acts on these groups. Its rational ninth-homology character satisfies \(\chi_9(t,\pi)=\operatorname{sgn}(\pi)\), where \(t\) flips coordinates and \(\pi\) permutes them. Its rational seventh-homology character is determined by the following exact finite orbit formula. For \(g=(t,\pi)\), let \(\mathcal O(g)\) be the partition of the sixteen graph vertices into cycles under \(g\); put \(U_{\mathcal J}=\bigcup_{O\in\mathcal J}O\). Then
\[
\chi_7(g)=\sum_{\substack{\mathcal J\subseteq\mathcal O(g)\\U_{\mathcal J}\in\mathcal D(Q_4)}}(-1)^{|\mathcal J|}-\operatorname{sgn}(\pi).
\]
The values of \(\chi_7\) occur with multiplicities \(116,177,68,22,1\) at character values \(0,2,4,6,10\), respectively. Consequently the quotient by the complete graph symmetry group satisfies
\[
\widetilde H_j(\mathcal D(Q_4)/B_4;\mathbb Q)\cong
\begin{cases}\mathbb Q^2,&j=7,\\0,&\text{otherwise.}\end{cases}
\]

As a further consequence of the published dominance-complex/independence-complex suspension theorem and combinatorial Alexander duality, the *ordinary* independence complex of the five-cube has complete integral homology
\[
\widetilde H_j(\operatorname{Ind}(Q_5);\mathbb Z)\cong
\begin{cases}\mathbb Z,&j=5,\\\mathbb Z^{10},&j=7,\\0,&\text{otherwise.}\end{cases}
\]
No sphere-wedge homotopy decomposition or equivariant homotopy splitting is claimed.

## Assumptions and scope

For a graph \(G\), a set \(S\) dominates if each vertex lies in \(S\) or has a neighbor in \(S\). Write \(N[v]\) for the *closed* graph neighborhood of \(v\). The defining face predicate above is exactly
\[
\sigma\in\mathcal D(G)\iff (\forall v\in V(G))\ N[v]\nsubseteq\sigma.
\]
Here \(Q_4\) has exactly sixteen vertices, thirty-two edges, and sixteen forbidden closed neighborhoods of size five. Vertex labels are integers \(0,\ldots,15\) interpreted as four-bit words; a simplex is represented by its sixteen-bit vertex-membership mask. All integral chain groups are oriented by ascending vertex labels. The group acts by coordinate permutations followed by binary translation. Statements concern only this fixed graph and, via a previously published equivalence, the fixed graph \(Q_5\).

## Proof

**Complete finite face enumeration and integral Morse reduction.** In the independently executable `four_cube_dominance_verify.py`, every one of the \(2^{16}=65536\) vertex masks is tested twice, first by avoiding each closed neighborhood and independently by explicitly testing domination by its complement. These tests agree on every mask. There are exactly \(45706\) nonempty faces, with face numbers in dimensions zero through eleven
\[
(16,120,560,1820,4352,7832,10560,10310,6800,2736,560,40).
\]
On this *entire* face set, repeatedly pair any remaining face not containing a chosen vertex with its available one-vertex extension, choosing vertices in increasing label order; no pair is reused. This produces \(22847\) pairs and leaves exactly one unmatched vertex, ten unmatched seven-simplices, and one unmatched nine-simplex. To certify the crucial acyclicity independently of any unproved matching lemma, form every directed cover incidence of the face poset, reverse the matched incidences and orient all others downward. A complete topological sorting removes all \(45706\) face-poset vertices after checking all \(329552\) cover incidences. Hence the matching is acyclic. Forman's discrete Morse theorem supplies a CW complex homotopy equivalent to the original with exactly one zero-cell, ten seven-cells and one nine-cell. All cellular differentials vanish *by the absence of cells in adjacent dimensions*. Thus the stated integral homology groups follow, without assuming torsion-freeness from a field computation. An independent simplicial boundary-rank computation over \(\mathbb F_2\) confirms the Betti numbers.

**Exact top-degree symmetry.** The unique critical nine-simplex supplies a coefficient-one generator of the ninth Morse chain group. Starting with that oriented simplex, eliminate each nonzero eight-boundary coordinate by adding an integral multiple of its corresponding matched nine-simplex; the acyclic ordering of the 2215 eight-to-nine matched pairs makes the elimination finite and triangular. This produces an explicit integral nine-cycle supported on \(448\) oriented nine-simplices, with coefficients \(\pm1\) and *zero signed boundary*. Elimination modulo boundaries of the \(520\) matched ten-to-nine pairs defines an exact homology-coordinate map to the coefficient of the unique critical nine-simplex. Applying every one of the \(384\) graph automorphisms to the explicit cycle, accounting for the sign of the induced simplex-vertex permutation, and reducing integrally by this map gives \(\operatorname{sgn}(\pi)\) in every case. Since the ninth homology is free of rank one, this proves the ninth-homology character.

**Seventh-degree symmetry and quotient.** A fixed simplex under a vertex permutation is a union of its vertex orbits. If it consists of \(k\) vertices and \(r\) vertex-orbits, the induced orientation sign equals \((-1)^{k-r}\). Its signed contribution to the reduced Lefschetz alternating trace is therefore \((-1)^{r-1}\); including the empty face gives reduced Lefschetz number \(-\sum_{\mathcal J}(-1)^{|\mathcal J|}\). The only nonzero reduced rational homology groups are in odd degrees seven and nine, so this Lefschetz number is \(-\chi_7(g)-\chi_9(g)\). Substitution of the ninth-degree character gives exactly the stated finite orbit formula. Its exhaustive evaluation over the \(384\) automorphisms produces the character histogram above and sums \(\sum_g\chi_7(g)=768\) and \(\sum_g\chi_9(g)=0\). Character averaging gives invariant dimensions two and zero. In characteristic zero, barycentrically subdividing makes the finite simplicial action admissible and rational homology of the orbit-space quotient equals the invariant part, yielding the claimed quotient homology.

**Five-cube consequence.** Matsushita's suspension equivalence and Matsushita--Wakatsuki's exposition give \(\Sigma(\mathcal D(G)^\vee)\simeq\operatorname{Ind}(G^{\bowtie})\), with \(G^{\bowtie}\cong G\square K_2\) for bipartite \(G\). Here \(Q_4\) is bipartite, and \(Q_4\square K_2=Q_5\). Combinatorial Alexander duality on the sixteen-vertex ground set identifies \(\widetilde H_i(\mathcal D(Q_4)^\vee;\mathbb Z)\) with \(\widetilde H^{13-i}(\mathcal D(Q_4);\mathbb Z)\). After suspension, each original cohomological degree \(j\) appears in new homological degree \(14-j\). Since the proven integral homology is free, the universal-coefficient theorem introduces no extra torsion or shifted summands. Degrees nine and seven therefore give degrees five and seven, respectively.

## Verification

Run the standalone Python 3.10+ file `four_cube_dominance_verify.py` without any nonstandard library; its complete recorded output is `four_cube_dominance_verification.txt`. The script reconstructs graph and faces, uses two independent face predicates, exhaustively verifies each directed Hasse incidence and the entire acyclicity certificate, independently checks all simplicial boundary ranks over \(\mathbb F_2\), constructs and boundary-checks the signed integral ninth cycle, and evaluates the action and Lefschetz formula for all \(384\) automorphisms. Recorded verification marker: `DOMINANCE_Q4_INTEGRAL_AND_SYMMETRY_VERIFIED`. The homological claim is supported by the *complete finite Morse certificate*, not extrapolated from partial enumeration or the mod-two calculations.

## Relationship to prior work

Matsushita (2020, arXiv:2009.04145) defines the same dominance complex and gives a general connectivity bound in terms of vertex covers, not the exact mixed-dimensional homology of the four-cube. Matsushita and Wakatsuki (2023, arXiv:2312.02639) establish the Alexander dual relationship to neighborhood complexes, the suspension/independence-complex method and exact computations for paths, cycles and rectangular grids. Their studied open rectangular grids are not the four-cube (which is a Cartesian product of cycles). The suspension equivalence and Alexander duality are **prior theorems**, not newly discovered. Previously indexed results for the ordinary four-cube independence complex, its Čech and cut complexes, and neighborhood complexes of *the cube itself* concern different simplicial complexes; in particular they do not imply this dominance-complex calculation or the ordinary five-cube independence homology. The new contribution is the exact integral four-cube calculation and its complete hyperoctahedral character, with the five-cube corollary.

## Limitations

The theorem is for the ordinary dominance complex with **closed-neighborhood** forbidden faces. An unrelated simplicial complex of graphs whose *graph domination number* exceeds a cutoff is not considered. No classification for all hypercubes, no integral homotopy wedge decomposition, no nontrivial cup-product computation, no equivariant stable splitting and no quotient homotopy type are established. The ninth-character statement is for the full automorphism group of the four-cube, while the independence-complex corollary is nonequivariant. An equivalent unindexed independent calculation might exist; originality is assessed against the inspected evidence and is not guaranteed solely by the absence of search matches.

## References

1. T. Matsushita, *Dominance complexes and vertex cover numbers of graphs*, first available 2020-09-09, arXiv:2009.04145, https://arxiv.org/abs/2009.04145.
2. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, first available 2023-12-05, arXiv:2312.02639, https://arxiv.org/abs/2312.02639.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90--145. Its discrete Morse theorem is used only with an explicitly exhaustive acyclicity certificate.
