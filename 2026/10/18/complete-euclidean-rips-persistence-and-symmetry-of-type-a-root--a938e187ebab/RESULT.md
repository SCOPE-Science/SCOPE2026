# Complete Euclidean Rips persistence and symmetry of type-A root configurations

## Finding
For every integer \(n\ge5\), set
\[
 A_{n-1}=\{e_i-e_j:1\le i,j\le n,\ i\ne j\}\subset\mathbb R^n,
 \qquad K_r=\operatorname{VR}_{\le r}(A_{n-1}),
\]
where the metric is the ambient Euclidean distance, the standard basis vectors have unit norm, and the Vietoris--Rips threshold is **inclusive**. Put \(b_n=n^2-3n+1\) and \(m=\binom n2\). The complete homotopy classification is
\[
K_r\simeq
\begin{cases}
\bigsqcup^{n(n-1)}\mathrm{pt},&0\le r<\sqrt2,\\
\bigvee^{b_n}S^1,&\sqrt2\le r<2,\\
S^{n-2},&2\le r<\sqrt6,\\
S^{m-1},&\sqrt6\le r<2\sqrt2,\\
\mathrm{pt},&r\ge2\sqrt2.
\end{cases}
\]
These describe **integral homotopy types**, not merely field-dependent homology. Consequently, all positive-degree integral persistent homology is free and consists of \(b_n\) intervals \([\sqrt2,2)\) in degree \(1\), one \([2,\sqrt6)\) in degree \(n-2\), and one \([\sqrt6,2\sqrt2)\) in degree \(m-1\). In degree zero, there are \(n(n-1)-1\) finite intervals \([0,\sqrt2)\) and one infinite interval.

The natural symmetry group \(S_n\times C_2\) acts by simultaneous permutation of coordinates and root negation. For \(g=(\sigma,\epsilon)\) with \(\epsilon\in\{0,1\}\), let \(f(\sigma)\) be the number of fixed letters and \(t_2(\sigma)\) the number of disjoint two-cycles in \(\sigma\). The entire rational homology character at each nontrivial scale is:
\[
\operatorname{tr}\bigl(g\mid\widetilde H_1(K_{\sqrt2};\mathbb Q)\bigr)=
\begin{cases}
 f(\sigma)^2-3f(\sigma)+1,&\epsilon=0,\\
 1-2t_2(\sigma),&\epsilon=1;
\end{cases}
\]
\[
\operatorname{tr}\bigl(g\mid\widetilde H_{n-2}(K_2;\mathbb Q)\bigr)
 =\operatorname{sgn}(\sigma)(-1)^{(n-1)\epsilon},
\]
\[
\operatorname{tr}\bigl(g\mid\widetilde H_{m-1}(K_{\sqrt6};\mathbb Q)\bigr)
 =\operatorname{sgn}(\sigma)^{n-1}(-1)^{m\epsilon}.
\]
All other reduced rational homology groups at these stages vanish. The integral top homology groups in the two spherical stages are rank-one lattices carrying the same sign characters.

## Assumptions and scope
The root vectors are unscaled and labelled by ordered pairs \((i,j)\), representing \(e_i-e_j\). The statement applies to every integer \(n\ge5\), and no limit in \(n\) is inferred from finite data. Graph shortest-path distance, spherical arc distance, and open Rips thresholds are not used. All group actions are induced from actual isometries of the root set; the involution in \(C_2\) exchanges \((i,j)\) with \((j,i)\). Homology uses ordinary integral simplicial chains or rational coefficients as explicitly indicated.

## Proof
**1. Exact metric adjacency.** For distinct ordered pairs \((i,j)\) and \((k,l)\),
\[
\lVert(e_i-e_j)-(e_k-e_l)\rVert^2
=4-2(\delta_{ik}-\delta_{il}-\delta_{jk}+\delta_{jl}).
\]
The possible squared distances are \(2,4,6,8\): respectively a common initial coordinate or common terminal coordinate, four distinct indices, a terminal-to-initial coincidence (without reversal), and reversed ordered pairs. Every value occurs for \(n\ge5\), so these are exactly the four positive change thresholds.

**2. First nontrivial stage.** At squared threshold \(2\), the maximal simplices are \(R_i=\{(i,j):j\ne i\}\) and \(C_j=\{(i,j):i\ne j\}\). Two distinct rows, or two distinct columns, do not meet. Moreover \(R_i\cap C_j\) is the single vertex \((i,j)\) for \(i\ne j\), and is empty otherwise. No three maximal simplices intersect. The finite nerve theorem therefore identifies the complex with the bipartite graph on symbols \(R_i,C_j\), with all edges except \(R_iC_i\). This graph is connected and has \(2n\) vertices and \(n(n-1)\) edges. Its first Betti number is \(n(n-1)-2n+1=b_n\), yielding the circle wedge.

**3. Intermediate sphere.** A pair of roots is adjacent at squared threshold \(4\) precisely when the corresponding two directed arcs can simultaneously belong to a directed bipartite cut \(S\to T\) with disjoint source and target sets. Thus a simplex \(F\) of \(K_2\) consists of arcs whose nonempty source set \(S(F)\) and nonempty target set \(T(F)\) are disjoint; conversely, every nonempty collection of arcs from \(S\times T\) is a simplex whenever \(S,T\subseteq[n]\) are disjoint nonempty sets.

Let \(P\) be the poset of ordered pairs \((S,T)\) of disjoint nonempty subsets of \([n]\), ordered by inclusion in each coordinate. The map from the face poset of \(K_2\) to \(P\), sending \(F\) to \((S(F),T(F))\), is order preserving. For every \((S,T)\in P\), the lower fiber consists of the face poset of the entire simplex on \(S\times T\), with maximal element \(S\times T\). Quillen's fiber lemma shows that its induced map on order complexes is a homotopy equivalence. The construction commutes with permutations and the source-target swap. In fact each fixed-subgroup lower fiber also has the invariant maximum \(S\times T\), so applying the same criterion on fixed-point posets yields an \(S_n\times C_2\)-equivariant homotopy equivalence.

The order complex of \(P\) is the barycentric subdivision of the graph-homomorphism cell complex \(\operatorname{Hom}(K_2,K_n)\). Its cell labelled \((S,T)\) is \(\Delta^S\times\Delta^T\). The map \((p,q)\mapsto p-q\) is a homeomorphism from this cell complex onto
\[
 B=\{z\in\mathbb R^n:\textstyle\sum_i z_i=0,\ \sum_i|z_i|=2\}.
\]
Indeed the positive and negative coordinate parts of any \(z\in B\) are the unique disjoint-support probability vectors \(p,q\) with \(p-q=z\). The set \(B\) is the boundary of the \(\ell^1\) unit ball in the \((n-1)\)-dimensional zero-sum subspace, up to scaling; radial projection shows \(B\cong S^{n-2}\). Coordinate permutations and source-target exchange act on this sphere by the corresponding permutation matrix and \(-I\), respectively. The top-homology degree is therefore \(\operatorname{sgn}(\sigma)(-1)^{(n-1)\epsilon}\).

**4. Penultimate sphere.** At squared threshold \(6\) the only missing edges are \((i,j)(j,i)\). For each unordered pair \(\{i,j\}\), precisely one of its two oriented roots can be selected in a face. Hence the complex is the simplicial join of \(m\) copies of a discrete two-point complex: \(K_{\sqrt6}=(S^0)^{*m}\cong S^{m-1}\). Orient its signed coordinate factors by \(e_i\wedge e_j\) with \(i<j\). A coordinate permutation acts on these factors through its exterior-square permutation matrix, whose determinant is \(\operatorname{sgn}(\sigma)^{n-1}\); simultaneous root negation changes every factor sign, contributing \((-1)^{m\epsilon}\). Their product is the asserted integral top-homology character. At squared threshold \(8\), all pairs become edges, so the final complex is a simplex.

**5. Initial character and persistence.** The cover by the simplices \(R_i,C_j\) is preserved by the symmetry group. Its equivariant nerve is the oriented bipartite graph from step 2, orienting edges from rows to columns. In its augmented chain complex, a non-inverting \(\sigma\) fixes \(f(\sigma)(f(\sigma)-1)\) oriented edges and \(2f(\sigma)\) vertices. Thus the trace on first homology is \(f(\sigma)^2-3f(\sigma)+1\). A source-target swap fixes no vertices, reverses every edge orientation, and fixes exactly \(2t_2(\sigma)\) undirected edges as oriented cells up to the minus sign. Since the trace on connected degree-zero homology is one, the degree-one trace is \(1-2t_2(\sigma)\). Finally, for \(n\ge5\) the three positive homology degrees \(1,n-2,m-1\) are distinct. Every persistence map between consecutive nontrivial stages on any given positive homology degree therefore has zero codomain or zero domain; this proves the complete integral interval decomposition. Ordinary degree-zero components merge at the first threshold.

## Verification
The standalone standard-library program `verify_a_root_rips.py` constructs all roots and exact squared distances for \(n=4,5,6\). At the first two nontrivial squared thresholds it independently enumerates all faces, computes the Euler characteristics, and for \(n=4,5\) computes boundary ranks over \(\mathbb F_2\) and \(\mathbb F_3\). For \(n=5\), it checks signed simplicial Lefschetz numbers against the claimed two character formulas for all \(120\times2=240\) group elements. Its successful terminal marker is `VERIFY_OK`. These are finite consistency checks, not replacements for the general nerve, poset-fiber, and join arguments above.

## Relationship to prior work
Babson and Kozlov established the sphere topology of \(\operatorname{Hom}(K_2,K_n)\), including its flip action, in *Complexes of graph homomorphisms* (2003 preprint, Section 4.2). That topology is **used**, not claimed as new. Azenberg, Beketov, and Magai (2023) identify the open-hemisphere complex of the same type-A roots with the larger complex of all directed acyclic graphs; that distinct directed-graph condition does not imply the Euclidean distance filtration. The previously published twelve-vertex cuboctahedral Rips computation treats only the rank-three root configuration (the \(n=4\) case), with no arbitrary-\(n\) homotopy or symmetry statement. The contribution here is the exact all-\(n\) Euclidean Rips reduction to those known structures, the resulting four-transition integral filtration, and its complete natural symmetry characters.

## Limitations
The theorem is confined to type-A complete root systems and unscaled Euclidean chordal distance. It does not address other irreducible root types, partial root subsets, non-Euclidean metrics, or a homotopy-coherent equivariant persistent equivalence between distinct filtration stages. The genus and coefficients of any quotient spaces are not determined. Although the relevant source sections and a matching finite-case publication were examined, equivalent differently named treatments may exist; no claim of absolute literature completeness or external certification is made.

## References
1. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056 (first submitted 2003-10-05), Section 4.2, especially Proposition 4.3.
2. A. Ayzenberg, M. Beketov and G. Magai, *Coverings by open and closed hemispheres*, arXiv:2310.02827 (2023), Section 3 and its type-A root construction.
3. *Complete Vietoris--Rips filtration of the Euclidean cuboctahedron*, published-finding corpus public record dated 2026-10-04, identifier c10ad684de7e (finite \(n=4\) case).
