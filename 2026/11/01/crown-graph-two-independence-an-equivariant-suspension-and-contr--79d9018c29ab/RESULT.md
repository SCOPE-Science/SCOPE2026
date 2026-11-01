# Crown-graph two-independence: an equivariant suspension and contractible symmetry quotients

## Finding
For every integer \(n\ge3\), let \(C_n=K_{n,n}\setminus\{a_i b_i:1\le i\le n\}\) be the crown graph, equivalently the bipartite Kneser graph \(H(n,1)\). Let \(X_n=\operatorname{Ind}_2(C_n)\) be its simplicial complex of vertex subsets whose induced connected components each contain at most two vertices. Write \(U_n=\ker(\mathbb Z^n\xrightarrow{\text{sum}}\mathbb Z)\), with coordinates permuted by \(S_n\). The full automorphism group is \(G=S_n\times C_2\), where the second factor exchanges the two vertex classes.

There is a \(G\)-equivariant homotopy equivalence
\[
|X_n|\simeq_G\Sigma|K_n|,
\]
where \(K_n\) on the right denotes the complete graph as a one-dimensional CW complex, \(S_n\) acts by vertex permutations, and \(C_2\) exchanges the two suspension points and fixes the equatorial graph. In particular,
\[
X_n\simeq\bigvee^{\binom{n-1}{2}}S^2,
\qquad
\widetilde H_2(X_n;\mathbb Z)\cong\bigwedge^2 U_n\otimes\varepsilon,
\]
where \(\varepsilon\) is the integral sign representation of the class-exchange involution. All other reduced integral homology groups vanish. Both the class-exchange quotient \(|X_n|/C_2\) and the full automorphism quotient \(|X_n|/G\) are contractible up to homotopy. At \(n=4\) the complex is pure three-dimensional and non-shellable, because its integral second homology is \(\mathbb Z^3\).

## Assumptions and scope
Graph vertices are \(a_1,\ldots,a_n,b_1,\ldots,b_n\), with \(a_i\sim b_j\) exactly when \(i\ne j\); there are no within-class edges. The simplicial complex includes the empty face. The suspension is the *unreduced* simplicial suspension with two nonadjacent new cone vertices. The notation \(\bigwedge^2 U_n\) means the second exterior power over \(\mathbb Z\), not merely a rational representation. Quotients are quotients of geometric realizations, not graphs formed by identifying vertices and then rebuilding a complex. The claim concerns all integers \(n\ge3\); no claim is made about higher independence parameters.

## Proof
**1. Complete facet cover.** Let \(A=\{a_i\}_{i=1}^n\), \(B=\{b_i\}_{i=1}^n\), and \(Q_{ij}=\{a_i,a_j,b_i,b_j\}\) for \(i<j\). Each \(Q_{ij}\) spans two disjoint graph edges, so the full tetrahedron \(\Delta(Q_{ij})\) lies in \(X_n\). Both full class simplices \(\Delta(A),\Delta(B)\) lie in \(X_n\). Conversely, if a face meets both classes and selects three or more vertices on one side, any vertex on the other side is adjacent to at least two selected vertices and produces a component of size at least three. Thus both chosen class sizes are at most two. A selected \(2+1\) face must contain a diagonal pair of equal indices; a selected \(2+2\) face must use precisely the same pair of indices on both sides. Every \(1+1\) face also lies in some \(Q_{ij}\) (when the indices agree, choose a distinct second index). Therefore
\[
X_n=\Delta(A)\cup\Delta(B)\cup\bigcup_{i<j}\Delta(Q_{ij}).\tag{1}
\]
All intersections of members of this cover are either empty or full simplices on their common vertices.

**2. The cover nerve.** Let \(L_n\) be the nerve of the family \(\{\Delta(Q_{ij})\}_{i<j}\). A set of such tetrahedra intersects nontrivially precisely when their index-pairs have a *common index* (not merely pairwise intersections). Consequently, \(L_n\) is the union of \(n\) simplices \(T_i\), each on the \(n-1\) symbols \(Q_{ij}\) incident with \(i\). For distinct \(i,j\), \(T_i\cap T_j\) is the one vertex \(Q_{ij}\), and any intersection involving at least three different \(T_i\)'s is empty. The nerve of the \(T_i\)-cover is therefore exactly the one-dimensional complete graph \(K_n\). Each nonempty intersection in either cover is a simplex. The simplicial nerve lemma gives \(|L_n|\simeq|K_n|\).

Both \(\Delta(A)\) and \(\Delta(B)\) meet an intersection of any selected \(Q_{ij}\)'s exactly when those index-pairs share a common index, whereas \(\Delta(A)\cap\Delta(B)=\varnothing\) as geometric subcomplexes. Hence the nerve of the entire cover (1) is exactly the union of two cones on \(L_n\) with disjoint apexes, namely \(\Sigma L_n\). Thus \(|X_n|\simeq\Sigma|L_n|\simeq\Sigma|K_n|\). A connected graph \(K_n\) has a spanning tree with \(n-1\) edges among its \(\binom n2\) edges; collapsing the tree gives a wedge of \(\binom{n-1}{2}\) circles. Suspending establishes the integral homotopy statement.

**3. Equivariance and quotients.** The family (1) is permuted by \(G\); \(S_n\) relabels all the pieces and \(C_2\) exchanges \(\Delta(A)\) with \(\Delta(B)\) while fixing each \(\Delta(Q_{ij})\). The \(T_i\)-cover is likewise \(S_n\)-invariant. For both covers, each nonempty intersection is a simplex; its barycenter is fixed by any subgroup preserving that intersection. The standard equivariant nerve construction, using the incidence/blowup space and these canonical contractions, therefore yields the asserted equivariant homotopy equivalence. Under it, the exchange involution switches the suspension apexes and fixes the base. The quotient by this involution is \(\operatorname{Cone}(|K_n|)\), which is contractible. The further quotient by \(S_n\) is \(\operatorname{Cone}(|K_n|/S_n)\), likewise contractible.

**4. Integral character.** In the oriented cellular chain complex of \(K_n\), identify \(C_1(K_n;\mathbb Z)=\bigwedge^2\mathbb Z^n\), with \(e_i\wedge e_j\) the edge \(i\to j\). Its boundary is \(e_i\wedge e_j\mapsto e_j-e_i\), which surjects onto \(U_n\). Since \(\mathbb Z^n=U_n\oplus\mathbb Ze_1\), its kernel is \(\bigwedge^2 U_n\) over \(\mathbb Z\). Suspension shifts this first homology to degree two. Exchanging its apexes acts by degree \(-1\) on the suspension coordinate, proving the claimed signed exterior-square integral module. The \(n=4\) facet cover has exactly eight three-simplices (two class simplices and six tetrahedra), and its nonzero second homology precludes pure shellability.

## Verification
`VERIFY_CROWN.py` enumerates the induced components and all faces for \(3\le n\le6\), independently reconstructs the facet cover, calculates reduced homology ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), and checks the predicted rational character for *every* element of \(S_n\times C_2\) using oriented simplicial Lefschetz traces. It checks 12, 48, 240 and 1440 group elements respectively, with a matching \(\binom{n-1}{2}\)-dimensional second homology in each case. Those finite checks are corroboration only; the preceding cover/nerve argument proves the theorem for every \(n\ge3\) and over \(\mathbb Z\).

## Relationship to prior work
Deshpande and Singh (arXiv:2001.05448, first public January 15, 2020) developed higher-independence homotopy calculations for complete multipartite graphs, cycles, fully whiskered graphs and trees. Their complete multipartite theorem does not include the removal of the matched cross-edges, and their cycle theorem covers the isolated \(n=3\) crown \(C_6\), not the general crown family. Abdelmalek and collaborators (arXiv:2106.10863, June 21, 2021) treat chordal families and shellability rather than this nonchordal family. Mirafzal and Zafari (arXiv:1804.04570, April 12, 2018) identified \(H(n,1)\), its distance-transitivity, and its full automorphism group, but not its higher-independence homology action. Related indexed results about other graph complexes do not imply (1) or the signed integral module.

## Limitations
The theorem does not classify \(\operatorname{Ind}_r(C_n)\) for \(r\ne2\), nor does it claim an equivariant simplicial collapse or a particular triangulation of the geometric quotients. A finite computation alone does not establish the universal theorem. Bibliographic searches cannot exclude unpublished or unindexed equivalent calculations, and no independent audit has been conducted.

## References
- S. M. Mirafzal and A. Zafari, *Some algebraic properties of bipartite Kneser graphs*, arXiv:1804.04570v1 (April 12, 2018), https://arxiv.org/html/1804.04570v1, especially Theorem 3.6.
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1 (January 15, 2020); https://arxiv.org/html/2001.05448v2, especially Theorems 3.5 and 4.6.
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1 (June 21, 2021), https://arxiv.org/abs/2106.10863.
