# The integral hook-tensor theorem for bipartite three-matching avoidance

## Finding

Let \(r,s\ge 3\) be integers, and let \(\mathcal B_{r,s}\) be the abstract simplicial complex whose vertex set consists of the \(rs\) edges of \(K_{r,s}\) and whose faces are exactly the edge sets with matching number at most two. Write
\[
U_m=\ker\bigl(\varepsilon_m:\mathbb Z^m\longrightarrow\mathbb Z\bigr),
\qquad \varepsilon_m(e_i)=1.
\]
Then the natural permutation action on the two vertex classes induces an **integral** isomorphism
\[
\boxed{\widetilde H_3(\mathcal B_{r,s};\mathbb Z)
\ \cong_{\mathbb Z[S_r\times S_s]}\
\bigwedge\nolimits^2 U_r\otimes_{\mathbb Z}\bigwedge\nolimits^2 U_s.}
\]
For \(i>0\) with \(i\ne3\), reduced integral homology vanishes, and the degree-three rank is \(\binom{r-1}{2}\binom{s-1}{2}\). In particular, over \(\mathbb Q\) the homology is the external tensor product of the hook Specht modules \(S^{(r-2,1,1)}\boxtimes S^{(s-2,1,1)}\).

For every increasing three-element row set \(I\subseteq[r]\) and column set \(J\subseteq[s]\), there is an explicitly constructed geometric three-sphere cycle \(z_{I,J}\) supported on sixteen tetrahedra inside the induced \(3\times3\) subcomplex. Those with \(I=\{0,a,b\}\), \(J=\{0,c,d\}\), and \(0<a<b<r\), \(0<c<d<s\) form an **integral homology basis**. The complete relations between all these geometric classes are the alternating four-term relations separately in the row and column triples. This gives the \(k=3\) instance of the hook-tensor prediction in Conjecture 1.15 of Linusson--Shareshian--Welker, including an integral refinement.

## Assumptions and scope

Use zero-based row indices \([r]=\{0,\ldots,r-1\}\), similarly for columns. A face of \(\mathcal B_{r,s}\) is a subset \(F\subseteq[r]\times[s]\) whose bipartite graph has no three pairwise vertex-disjoint edges. A graph-edge \((i,j)\) is a **simplicial vertex**, not a zero-cell of the original graph. Orient simplices by increasing row-major edge index. Homology has constant integral coefficients and its group action is induced by the natural simplicial permutations. The theorem is confined to complete bipartite graphs and avoidance of matchings of size three; it does not assert the analogous integral statement for larger forbidden matchings.

## Proof

**1. A unit primitive class in the \(3\times3\) complex.** Number the nine graph edges \((i,j)\) by \(v_{3i+j}\), for \(0\le i,j\le2\). Take the four disjoint pairs of simplicial vertices
\[
(v_1,v_5),\quad(v_2,v_7),\quad(v_3,v_8),\quad(v_4,v_6).
\]
All sixteen four-vertex transversals (one vertex from each pair) avoid a three-matching: this is verified by comparison with the six possible perfect matchings on the three-by-three bipartite graph. They form a simplicial octahedral three-sphere. Its oriented fundamental cycle is the alternating sum
\[
z=\sum_{\alpha\in\{0,1\}^4}(-1)^{\alpha_1+\cdots+\alpha_4}
[\,v_{p_{1,\alpha_1}},v_{p_{2,\alpha_2}},
 v_{p_{3,\alpha_3}},v_{p_{4,\alpha_4}}\,],
\]
where the displayed ordered pairs \((p_{q,0},p_{q,1})\) are \((1,5),(2,7),(3,8),(4,6)\) and bracket orientations are interpreted in the stated order. Every codimension-one face occurs twice with opposite signs; hence \(\partial z=0\).

Represent a four-edge simplex by its nine-bit mask \(m=\sum_{v_i\text{ chosen}}2^i\), with its vertices sorted by increasing index. The degree-three cochain \(\phi\) takes the values
\[
\begin{array}{c|rrrrrr}
m&29&30&43&46&51&53\\\hline
\phi(m)&1&1&-1&1&-1&-1
\end{array}
\]
and vanishes on all other tetrahedra. Direct incidence checks over **all 45 five-edge faces** give \(\delta\phi=0\), while the sixteen-term evaluation is \(\langle\phi,z\rangle=1\). These are finite, exact calculations and the provided verifier reconstructs both. Thus \([z]\) is nonzero and primitive. By Theorem 1.4 of Linusson--Shareshian--Welker, \(\mathcal B_{3,3}\simeq S^3\), so \([z]\) is an integral generator.

**2. The orientation character of the seed sphere.** By the same theorem the only positive-degree rational homology of \(\mathcal B_{3,3}\) is its one-dimensional degree-three group. An interchange of two rows fixes, in dimensions zero through five, signed simplicial chain traces
\[
(3,0,-8,-6,3,2).
\]
Their alternating sum is \(2\). The ordinary Lefschetz formula gives \(1-\operatorname{tr}(\sigma\mid H_3)=2\), so a row transposition acts by \(-1\). Column transpositions give the identical computation. These transpositions generate \(S_3\times S_3\); therefore \([z]\) transforms as \(\operatorname{sgn}_3\boxtimes\operatorname{sgn}_3\). In particular the fundamental class transported to any **ordered** pair of row and column triples is alternating separately in those triples.

**3. Retractions detecting every integral basis element.** For every pair \(0<a<b<r\), let \(p_{ab}:[r]\to[3]\) fix the symbols \(a\mapsto1\), \(b\mapsto2\), and send every other row, including row zero, to zero. Define \(q_{cd}:[s]\to[3]\) similarly for \(0<c<d<s\). The edge map
\[
(i,j)\longmapsto (p_{ab}(i),q_{cd}(j))
\]
induces a simplicial map \(P_{ab,cd}:\mathcal B_{r,s}\to\mathcal B_{3,3}\). Indeed, a three-matching in the image would lift to three edges in the original face with distinct row and column fibers, producing an impossible three-matching in the source. No injectivity of the edge map is required to define this simplicial map.

Embed the seed octahedron into the three rows \(I\) and three columns \(J\), in increasing order, and call its homology class \(z_{I,J}\). If fewer than three distinct rows or columns survive a projection, its image is supported on a full simplex of graph edges with at most two rows or at most two columns and hence is nullhomologous. Otherwise the restricted map is a \(3\times3\) permutation and its degree is the product of the two permutation signs established above. Consequently
\[
(P_{ab,cd})_*z_{\{0,a',b'\},\{0,c',d'\}}
=\delta_{aa'}\delta_{bb'}\delta_{cc'}\delta_{dd'}[z].
\]
Taking all \(\binom{r-1}{2}\binom{s-1}{2}\) projections gives a split surjection
\[
\Phi:\widetilde H_3(\mathcal B_{r,s};\mathbb Z)
\longrightarrow\mathbb Z^{\binom{r-1}{2}\binom{s-1}{2}}
\]
with the indicated geometric section. Theorem 1.4 of Linusson--Shareshian--Welker says that the source is **free of precisely this rank**, so \(\Phi\) is an isomorphism. In particular the displayed classes form an integral basis, without any unproved finite-index assumption.

**4. The exact integral representation and all relations.** The signed triple classes give an \(S_r\times S_s\)-equivariant surjection
\[
T:\bigwedge^3\mathbb Z^r\otimes\bigwedge^3\mathbb Z^s
\longrightarrow\widetilde H_3(\mathcal B_{r,s};\mathbb Z),
\quad
(e_i\wedge e_j\wedge e_k)\otimes
(e_a\wedge e_b\wedge e_c)\mapsto z_{ijk,abc}.
\]
Let \(\iota_{\varepsilon_m}:\bigwedge^3\mathbb Z^m\to\bigwedge^2 U_m\) be contraction with \(\varepsilon_m\). It is explicitly
\[
\iota_{\varepsilon_m}(e_i\wedge e_j\wedge e_k)
=(e_j-e_i)\wedge(e_k-e_i).
\]
The root-triple basis \((e_a-e_0)\wedge(e_b-e_0)\) identifies \(\bigwedge^2U_m\) with \(\mathbb Z^{\binom{m-1}{2}}\). By the projection calculation, the \((ab,cd)\)-coordinate of \(\Phi\circ T\) on any triple pair is exactly the coefficient of the corresponding root-triple wedge in
\(\iota_{\varepsilon_r}\otimes\iota_{\varepsilon_s}\). Thus \(\Phi\circ T\) is, in these bases, precisely the tensor product of the two contraction maps. Both contraction maps are surjective. Since \(\Phi\) is an isomorphism, this proves the asserted natural integral representation.

Finally \(\ker\iota_{\varepsilon_m}=\bigwedge^3U_m\), also the image of contraction \(\bigwedge^4\mathbb Z^m\to\bigwedge^3\mathbb Z^m\). Both contraction maps are split surjections between free abelian groups (split off the summand generated by \(e_0\)); therefore their tensor-product kernel is exactly the sum of the two separate kernels tensored with the opposite exterior cube, with no additional torsion. Hence the kernel of \(T\) is generated over \(\mathbb Z\) by the alternating four-term row-triple relations and the analogous column-triple relations, tensored with arbitrary triples on the opposite side. This describes every integral relation without hidden torsion. Over \(\mathbb Q\), the second exterior power of the standard representation is the hook Specht module of partition \((m-2,1,1)\), giving the stated representation-theoretic corollary.

## Verification

The standalone `verify.py` uses only Python's standard library. Run `python3 verify.py` from the directory containing the program. It reconstructs the nine-edge seed complex and all its 264 nonempty faces, checks the sixteen-term cycle boundary, verifies the six-entry cocycle against all 45 relevant four-dimensional simplices and its unit evaluation, and computes both transposition Lefschetz numbers. It then checks all 36 seed automorphism actions, 5,329 projection identities for sizes \(3\le r,s\le5\), and all 25 conjugacy-type character pairs of \(S_4\times S_4\) through independent signed fixed-face enumeration. The final expected line is `VERIFY_OK_INTEGRAL_BIPARTITE_NONMATCHING_K3_HOOK_TENSOR`.

These finite checks support the local seed and verify examples; **the theorem for arbitrary \(r,s\) follows from the projection-and-rank proof**, not from the finite range of the verifier. The published rank theorem is taken as an explicit external mathematical input rather than silently re-proved here.

## Relationship to prior work

Linusson--Shareshian--Welker (first public preprint 2004-10-15) prove the exact nonequivariant wedge-of-spheres theorem and rank (their Theorem 1.4) and formulate the hook-tensor statement as Conjecture 1.15. Their pages 3, 6, and 19--20 were inspected, including the proof's Morse-theoretic enumeration of critical cells; that argument does not supply a canonical integral group-action lattice or the explicit three-by-three geometric generators above. The new statement settles **only the \(k=3\) instance**, but strengthens it from rational characters to the full \(\mathbb Z[S_r\times S_s]\)-module and an explicit integral basis/relations. Holmsen--Lee (first public preprint 2020-03-25) establish Leray bounds for graph nonmatching complexes; these do not imply this particular integral representation. This assessment does not assert exhaustive coverage of every unindexed source.

## Limitations

The conclusion relies on the published all-rank wedge theorem, plus the exact finite seed computations reproduced by `verify.py`. This package is not an independent audit or a machine-checked proof of the cited theorem. No result is claimed for \(k\ge4\), for general bipartite graphs, or for unstable coefficient systems. Searches did not identify a published identical formula, but an equivalent treatment under another terminology or a stronger unpublished argument could exist. Bibliographic priority and independent mathematical review are outstanding.

## References

1. S. Linusson, J. Shareshian, V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345 (first public 2004-10-15), subsequently *Journal of Algebraic Combinatorics* **27** (2008), 331--349. Theorem 1.4; Conjecture 1.15; proof in Section 4.2. https://arxiv.org/abs/math/0410345 ; author full text: https://www.mathematik.uni-marburg.de/~welker/preprints/lsw.pdf
2. A. F. Holmsen, S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270 (first public 2020-03-25), subsequently *Journal of Combinatorial Theory, Series A*. Theorems 1.1--1.2 concern vanishing/Leray bounds rather than the \(S_r\times S_s\)-module. https://arxiv.org/abs/2003.11270
