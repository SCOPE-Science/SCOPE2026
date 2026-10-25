# Integral automorphism modules of clique-prism neighborhood complexes
## Finding
Let \(n\ge5\) and \(R_n=K_n\square K_2\). The natural automorphism group \(S_n\times C_2\) acts on its ordinary *open*-neighborhood complex \(\mathcal N(R_n)\). Define the integral crown-cycle lattice
\[
\mathscr L_n=\left\{M=(m_{ij})\in\mathbb Z^{n\times n}:\ m_{ii}=0,\ \sum_jm_{ij}=\sum_im_{ij}=0\text{ for each index}\right\}.
\]
With \(\sigma\in S_n\) acting by simultaneous row-and-column permutation and the nontrivial element \(h\in C_2\) acting by transposition, there is a natural integral module isomorphism
\[
\widetilde H_2(\mathcal N(R_n);\mathbb Z)\cong\mathscr L_n,\quad
(\sigma M)_{ij}=m_{\sigma^{-1}(i),\sigma^{-1}(j)},\quad hM=M^{\mathsf T}.
\]
In degree \(n-2\), the integral module is \(\operatorname{sgn}_{S_n}\otimes\mathbb Z\{u_A,u_B\}\), with \(h\) exchanging \(u_A,u_B\). All other reduced integral homology groups vanish. The ranks in degrees \(2,n-2\) are respectively \(n^2-3n+1\) and \(2\). Over \(\mathbb Q\), writing \(\varepsilon\) for the nontrivial character of \(C_2\), the first module splits as
\[
\widetilde H_2(\mathcal N(R_n);\mathbb Q)\cong
\bigl(S^{(n-2,2)}\boxtimes\mathbf1\bigr)\oplus
\bigl(S^{(n-2,1,1)}\boxtimes\varepsilon\bigr).
\]
If \(f(\sigma)\) and \(t(\sigma)\) are respectively the numbers of fixed points and two-cycles of \(\sigma\), then the full character is
\[
\begin{array}{c|cc}
 & (\sigma,1)&(\sigma,h)\\\hline
\operatorname{tr}_{\widetilde H_2}&f(\sigma)^2-3f(\sigma)+1&2t(\sigma)-1\\
\operatorname{tr}_{\widetilde H_{n-2}}&2\operatorname{sgn}(\sigma)&0.
\end{array}
\]
The existing nonequivariant sphere-wedge classification is a prerequisite, not the claimed new contribution; the new result is the integral action, including the layer-exchange sign and rational decomposition.

## Assumptions and scope
For each integer \(n\ge5\), let \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). The graph \(R_n\) has every edge among distinct vertices in each of \(A\) and \(B\), together with the matching edges \(a_i b_i\). The open-neighborhood simplicial complex consists of all finite vertex subsets lying in the set of neighbors of some graph vertex, excluding that vertex. Simultaneous relabeling gives \(\sigma\in S_n\), and interchanging the two parts gives \(h\in C_2\). For \(n\ge5\), the two size-\(n\) graph cliques are the only maximal cliques of that size, forcing every graph automorphism to preserve or exchange the parts; the cross matching forces simultaneous relabeling. Hence these are all graph automorphisms. The two nonzero homology degrees are different because \(n\ge5\); this is why the result excludes \(n=4\).

The representation \(S^{\lambda}\) denotes the rational Specht module indexed by partition \(\lambda\). The integral lattice is *not claimed* to split as an integral symmetric-plus-skew direct sum; rational decomposition uses division by two.

## Proof
**1. An invariant simplicial cover.** For each index \(i\),
\[
N(a_i)=(A\setminus\{a_i\})\cup\{b_i\},\qquad
N(b_i)=(B\setminus\{b_i\})\cup\{a_i\}.
\]
Let \(X=\bigcup_i\Delta(N(a_i))\), \(Y=\bigcup_i\Delta(N(b_i))\). The full complex is \(X\cup Y\). Each \(b_i\) occurs in one facet of \(X\), allowing a relative elementary collapse of that facet onto \(\Delta(A\setminus\{a_i\})\); hence \(X\) collapses to \(\partial\Delta(A)\), and similarly \(Y\) to \(\partial\Delta(B)\). These inclusions of the boundary simplices are equivariant under simultaneous index permutations and induce isomorphisms on integral homology because the removed facets form cones on proper boundary faces. Thus the top-dimensional homology action is the orientation sign of the permutation of the corresponding part vertices.

A face common to \(X\) and \(Y\) has at most one vertex from each part. A mixed edge \(\{a_i,b_j\}\) occurs precisely when \(i\ne j\). Therefore the intersection \(I=X\cap Y\) is the connected crown graph \(K_{n,n}\setminus\{a_i b_i\}\), with \(2n\) vertices and \(n(n-1)\) edges. Its integral cycle lattice has rank \(n^2-3n+1\).

**2. Integral Mayer–Vietoris and its exchange sign.** Because \(X\simeq Y\simeq S^{n-2}\) and \(I\) is one-dimensional, the reduced integral Mayer–Vietoris long exact sequence gives a canonical connecting isomorphism
\[
\delta:\widetilde H_2(X\cup Y;\mathbb Z)\xrightarrow{\sim}H_1(I;\mathbb Z)
\]
and, independently, an isomorphism
\[
\widetilde H_{n-2}(X;\mathbb Z)\oplus\widetilde H_{n-2}(Y;\mathbb Z)
\xrightarrow{\sim}\widetilde H_{n-2}(X\cup Y;\mathbb Z).
\]
All remaining reduced groups vanish. The first isomorphism identifies chains of \(I\) with matrices by orienting the edge \(a_i b_j\) from \(a_i\) to \(b_j\): zero boundary means exactly that every row sum and column sum vanishes. The simultaneous permutation acts on this matrix lattice in the stated manner.

To determine the layer exchange, use the standard ordered Mayer–Vietoris boundary: write a cycle \(c=x+y\) with \(x\) in the chains of \(X\), \(y\) in those of \(Y\), and set \(\delta[c]=[\partial x]\). Under \(h\), the two pieces exchange. Since \(\partial y=-\partial x\), one obtains \(\delta(h[c])=-h_I\delta[c]\). Yet the graph layer swap sends the oriented edge \(a_i\to b_j\) to \(b_i\to a_j=-(a_j\to b_i)\), so its action on oriented cycle matrices is \(-M^{\mathsf T}\). The two minus signs cancel: the *homology* action is \(M\mapsto M^{\mathsf T}\), integrally. On the two boundary-sphere classes, relabeling acts by the orientation character \(\operatorname{sgn}(\sigma)\), while \(h\) interchanges the two classes without another sign after choosing the same index orientation in both parts. This establishes the complete integral module description.

**3. Rational irreducibles and characters.** Over \(\mathbb Q\), transposition decomposes \(\mathscr L_n\otimes\mathbb Q\) into symmetric and skew-symmetric zero-diagonal matrices with zero row sums. The symmetric sector is the kernel of the row-incidence map from the permutation representation on unordered pairs to the point permutation representation, hence the Specht module \(S^{(n-2,2)}\). The skew sector is naturally \(\bigwedge^2 V\), where \(V\) is the standard augmentation representation of \(S_n\), hence \(S^{(n-2,1,1)}\). Symmetric and skew sectors have respective \(h\)-eigenvalues \(+1\) and \(-1\).

For an independent character derivation, act on the cellular chain complex of the crown graph \(I\). For \(\sigma\), the signed trace on edges is \(f(f-1)\), on vertices \(2f\), and on \(H_0(I)\) it is \(1\). Euler–Poincaré gives trace \(f(f-1)-2f+1=f^2-3f+1\) on \(H_1(I)\). For \(\sigma h\), no vertices are fixed, while each two-cycle of \(\sigma\) fixes two crown edges *with opposite orientation*, so the edge-chain trace is \(-2t\), giving trace \(1-2t\) on \(H_1(I)\). The Mayer–Vietoris exchange sign converts this to \(2t-1\) on \(\widetilde H_2\). In the top sphere pair, \(\sigma\) has trace \(2\operatorname{sgn}(\sigma)\) and \(\sigma h\) exchanges summands, giving trace zero. All assertions follow.

## Verification
Run `python3 verify.py` using the standard Python library. The script reconstructs all neighborhood facets from graph adjacency, enumerates every simplex for sizes \(n=5,6,7\), verifies the cover and its exact crown intersection, and computes mod-two homology ranks at \(n=5,6\). It independently computes signed Lefschetz numbers directly from all simplices under every automorphism at \(n=5,6\), and ten more automorphisms at \(n=7\), obtaining 1690 successful comparisons to the two displayed character formulas. This is corroboration, not the proof of any infinite-family or integral claim: the Mayer–Vietoris argument supplies that proof.

## Relationship to prior work
The previously published nonequivariant classification of \(\mathcal N(K_n\square K_2)\), appearing under both the names *clique prism* and *two-row rook graph*, determines the wedge of two \((n-2)\)-spheres and \(n^2-3n+1\) two-spheres, but does not identify the integral automorphism modules, rational irreducibles, or layer-exchange character. The present proof starts from the same invariant cover but must additionally resolve the sign in the ordered Mayer–Vietoris connecting map. This is a statement-level, not title-level, distinction.

Matsushita's 2025 closed-neighborhood-complex paper studies a graph-product construction including \(K_n\square K_2\), but *closed* neighborhoods of the prism are not the *open* neighborhoods considered here. There is also an equivalent expression of the present complex as the closed-neighborhood complex of the complementary crown graph \(K_{n,n}-M_n\), since its closed neighborhoods are exactly the open neighborhoods of the prism. This alias was specifically searched. General equivariant box- and Hom-complex literature establishes frameworks but does not, in the inspected materials, furnish this explicit integral crown-cycle module. No unconditional priority is claimed.

## Limitations
Only \(n\ge5\) is asserted. At \(n=4\) the two homology dimensions coincide, so a separate extension problem can occur, and this theorem does not classify it. The statement concerns homology modules, not a globally equivariant wedge decomposition of spaces. The integral lattice generally cannot be split by the rational symmetric/skew projectors without a factor of two. Independent review and a search of every possible historical paper have not been performed, and an equivalent representation calculation in unindexed literature is a residual originality risk.

## References
1. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first public 2025-11-16, especially the clique-prism example and definitions. https://arxiv.org/abs/2511.12608
2. *Open-neighborhood complexes of clique prisms: a mixed-dimensional sphere decomposition*, public mathematical research result, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-open-neighborhood-complexes-of-clique-prisms-a-mixed-dimensional--d1fca5b06808
3. *Neighborhood complexes of two-row rook graphs split into two spheres and a crown suspension*, public mathematical research result, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-neighborhood-complexes-of-two-row-rook-graphs-split-into-two-sph--9b16e10ce620
4. M. Bayer et al., *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, Theorem 7.18 for a different associated simplicial complex. https://arxiv.org/abs/2304.13675
