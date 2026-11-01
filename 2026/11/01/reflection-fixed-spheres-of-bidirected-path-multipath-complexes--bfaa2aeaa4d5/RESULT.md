# Reflection-fixed spheres of bidirected-path multipath complexes

## Finding
Let \(B_n\) be the bidirected path on \(n+1\) labeled vertices \(0,1,\ldots,n\), containing both directed arcs between consecutive vertices, and let \(X_n\) be its multipath simplicial complex. Reflection \(\rho(v)=n-v\) acts on \(X_n\). For every integer \(n\ge3\), the **geometric** fixed-point space is a sphere up to homotopy:
\[
 |X_n|^{\langle\rho\rangle}\simeq S^{\lfloor(n-3)/4\rfloor}.
\]
More precisely, put \(t=\lfloor(n-1)/2\rfloor\), and let \(B(t)\) be the bipartite graph with vertices \(L_i,H_i\), \(0\le i<t\), and edges \(L_iH_j\) precisely when \(|i-j|\le1\). The geometric fixed-point space is PL-homeomorphic to \(|\operatorname{Ind}(B(t))|\), and this complex simplicially collapses onto the boundary of a \(\lceil t/2\rceil\)-dimensional cross-polytope. For \(n=1,2\), the geometric fixed-point space is empty.

There is also an integral symmetry consequence. The known ambient homotopy equivalence \(|X_n|\simeq S^{a}\), \(a=\lfloor(n-1)/2\rfloor\), gives \(\widetilde H_a(X_n;\mathbb Z)\cong\mathbb Z\). Reflection acts on that rank-one lattice by multiplication by
\[
(-1)^{a+\lfloor(n-3)/4\rfloor}=
\begin{cases}
-1,&n\equiv1,2,3,4\pmod8,\\
+1,&n\equiv0,5,6,7\pmod8.
\end{cases}
\]
The statement about the representation applies to \(n\ge3\).

## Assumptions and scope
A face of \(X_n\) is a set of directed arcs whose spanning subgraph is a disjoint union of directed simple paths and isolated vertices. The vertices of the simplicial complex are *arcs*, not the underlying path vertices. The fixed points are points in the geometric realization, so a reflection may permute the arc vertices of a fixed simplex; the fixed-point space is not merely the full subcomplex on individually fixed arc vertices. All graphs are finite. Homotopy and homology use ordinary topological realization and integral coefficients unless stated otherwise.

## Proof
Write \(p_i=(i,i+1)\) and \(q_i=(i+1,i)\) for \(0\le i<n\). Two forward arcs are always compatible, as are two backward arcs. The pair \(p_i,q_j\) is forbidden exactly when \(|i-j|\le1\): at equality the two arcs form a directed two-cycle; at adjacent indices they create two incoming or two outgoing arcs at a common vertex. These pairwise exclusions are sufficient: the underlying graph is a path, so its only possible directed cycles using these arcs are two-cycles, and the indegree/outdegree constraints are pairwise. Thus \(X_n\) is the independence complex of a bipartite band graph on \(\{p_i,q_i\}\).

Reflection interchanges \(p_i\) and \(q_{n-1-i}\). Each arc orbit is \(O_i=\{p_i,q_{n-1-i}\}\). The orbit \(O_i\) itself spans a simplex precisely when \(|2i-(n-1)|>1\). For \(n\ge3\), the admissible indices are exactly the two tails
\[
 0\le i<t\qquad\text{and}\qquad n-t\le i<n,
 \quad t=\lfloor(n-1)/2\rfloor.
\]
No two distinct admissible orbits in the same tail conflict. For opposite-tail orbits \(O_i,O_j\), compatibility fails precisely when \(|i+j-(n-1)|\le1\). Relabel the low tail by \(L_i=O_i\), and the high tail by \(H_j=O_{n-1-j}\) for \(0\le i,j<t\). Their conflict condition is exactly \(|i-j|\le1\). The simplicial complex formed by unions of pairwise compatible admissible orbits is therefore \(\operatorname{Ind}(B(t))\).

For completeness, the orbit model gives the **actual** fixed space. On a simplex invariant under the order-two action, a fixed geometric point has equal barycentric coordinates on both arcs in each orbit. Replacing each orbit with its midpoint identifies its fixed affine subset with the simplex of orbit barycenters. These identifications agree on faces and give a canonical PL-homeomorphism \(|X_n|^{\langle\rho\rangle}\cong_{\mathrm{PL}}|\operatorname{Ind}(B(t))|\).

It remains to identify the homotopy type. For a finite graph \(G\), if two distinct nonadjacent vertices \(u,v\) satisfy \(N_G(u)\subseteq N_G(v)\), then \(\operatorname{Ind}(G)\) simplicially collapses onto \(\operatorname{Ind}(G\setminus v)\): the link of \(v\) is a cone with apex \(u\), and its faces can be removed by a descending-dimension elementary matching. For \(t\ge2\), \(N(L_0)\subseteq N(L_1)\); delete \(L_1\). In the residual graph, \(N(H_0)\subseteq N(H_1)\); delete \(H_1\). The edge \(L_0H_0\) is then isolated, and the remaining graph on indices \(2,\ldots,t-1\) is a copy of \(B(t-2)\). Repeat. When \(t\) is odd, the final piece is one edge; when \(t\) is even, the final piece reduces from \(B(2)\) to one edge. Consequently \(\operatorname{Ind}(B(t))\) collapses onto the independence complex of \(\lceil t/2\rceil\) disjoint edges. This is the join of \(\lceil t/2\rceil\) zero-spheres, namely the boundary of a cross-polytope and hence \(S^{\lceil t/2\rceil-1}=S^{\lfloor(n-3)/4\rfloor}\). For \(n=1,2\) no orbit is individually admissible, so the geometric fixed set is empty.

Finally, the known ambient sphere theorem gives just one nonzero reduced integral homology group, in degree \(a\). By the simplicial Lefschetz fixed-point formula the alternating trace on unreduced homology equals the Euler characteristic of the geometric fixed locus. With \(b=\lfloor(n-3)/4\rfloor\), this reads \(1+(-1)^a\operatorname{tr}(\rho\mid\widetilde H_a)=1+(-1)^b\). Thus the integral rank-one action is multiplication by \((-1)^{a+b}\), giving the stated residue classes modulo eight.

## Verification
A standalone script `verify.py` reconstructs arcs, directed multipaths, reflection orbits, and admissible orbit faces without assuming the band-graph reduction. It exhaustively compares every orbit subset with the predicted independence-complex face condition for \(3\le n\le13\), checks Euler characteristics, and verifies the empty cases \(n=1,2\). Separately it validates each neighborhood-containment deletion and the residual matching for \(1\le t\le120\), totaling 3,600 deleted vertex pairs, and checks the period-eight homology sign. Run `python verify.py` with Python 3. No third-party modules are required. These finite checks are consistency evidence; the all-width statement follows from the symbolic proof above.

## Relationship to prior work
Caputi, Collari, and Smith, *Multipath complexes of bidirectional polygonal digraphs* (arXiv:2601.05670, publicly submitted January 9, 2026), Proposition 2.2, prove \(|X_n|\simeq S^{\lfloor(n-1)/2\rfloor}\), and give an explicit nonequivariant suspension construction. That theorem does not specify the geometric reversal-fixed locus or the integral reversal sign. Caputi, Collari, Di Trani, and Smith, *On the homotopy type of multipath complexes* (arXiv:2208.04656), study multipath homotopy types of directed graph families but do not classify this reversal-fixed family. Published results on dihedral rational homology of **bidirected polygons** concern a different underlying graph and do not determine the fixed spaces of **linear** bidirected paths. The present theorem uses a new orbit-barycenter band-graph reduction to supply those missing geometric data.

## Limitations
This is a nonequivariant homotopy classification of the **geometric fixed locus** for the single end-reversal involution. It is not an equivariant sphere homeomorphism for the ambient complex, and it does not classify arbitrary graph actions or all bidirected trees. The PL assertion is for the orbit-barycenter model; the subsequent simplification to a sphere is a simplicial collapse/homotopy equivalence, not in general a PL-homeomorphism to a sphere. An equivalent formula in unindexed work remains possible. Independent external validation has not been performed.

## References
1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (January 9, 2026), especially Proposition 2.2, https://arxiv.org/abs/2601.05670 .
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (August 9, 2022), https://arxiv.org/abs/2208.04656 .
3. The graph-folding lemma for independence complexes (the elementary conical-link argument is proved in the text); general background: D. Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008.
