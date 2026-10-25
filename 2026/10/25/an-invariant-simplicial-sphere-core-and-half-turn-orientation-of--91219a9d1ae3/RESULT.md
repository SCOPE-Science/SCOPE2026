# An invariant simplicial sphere core and half-turn orientation of honeycomb perfect-matching complexes

## Finding
For every integer \(n\ge 2\), let \(H_{1\times2\times n}\) be the standard hexagonal honeycomb graph with three pairs of opposite side lengths \(1,2,n\). Let \(K_n=\mathcal M_p(H_{1\times2\times n})\) be its perfect-matching complex: its vertices are graph edges, and its faces are precisely edge subsets extendible to a perfect matching. Use the edge labels of Bayer--Jelić Milutinović--Vega [1]. Put
\[
x=d_{0,0},\qquad y=d_{2,n},\qquad D_n=\{d_{1,j}:1\le j\le n-1\},\qquad F_n=\{x,y\}\cup D_n.
\]
**Claim.** The induced subcomplex on \(F_n\) is the full boundary \(\partial\Delta(F_n)\) of an \(n\)-simplex, and the entire complex \(K_n\) *simplicially collapses* onto this explicitly embedded \((n-1)\)-sphere. The central half-turn \(\rho\) of the honeycomb preserves this sphere subcomplex. On its integral top homology it acts by the four-periodic orientation character
\[
\rho_*\big|_{\widetilde H_{n-1}(K_n;\mathbb Z)}=(-1)^{1+\lfloor(n-1)/2\rfloor}.
\]
In particular, \(\widetilde H_{n-1}(K_n;\mathbb Z)\cong\mathbb Z\), all other reduced integral homology groups vanish, and the quotient \(|K_n|/\langle\rho\rangle\) has one-dimensional top reduced rational homology exactly when \(n\equiv0,3\pmod4\), and zero reduced rational homology otherwise.

## Assumptions and scope
The integer parameter is \(n\ge2\); no claim is made for \(n=1\) or for the ordinary matching complex (which includes nonextendible matchings). Edges are labeled as in [1]: \(a_{i,j}\) for \(1\le i\le2,0\le j\le n\); \(b_{i,j}\) for \(0\le i\le2,1\le j\le n\); and \(d_{i,j}\) for \(0\le i\le2,0\le j\le n\) with \(d_{0,n}\) and \(d_{2,0}\) omitted. A perfect matching corresponds to a pair of integers \(n\ge u\ge v\ge0\), denoted \(P_{u,v}\). The edge-membership rules follow Proposition 10 of [1]:
\[
\begin{aligned}
a_{1,j}\in P_{u,v}&\iff j=u,&a_{2,j}\in P_{u,v}&\iff j=v,\\
b_{0,j}\in P_{u,v}&\iff j>u,&b_{1,j}\in P_{u,v}&\iff v<j\le u,&b_{2,j}\in P_{u,v}&\iff j\le v,\\
d_{0,j}\in P_{u,v}&\iff j<u,&d_{1,j}\in P_{u,v}&\iff j>u\ \text{or}\ j<v,&d_{2,j}\in P_{u,v}&\iff j>v.
\end{aligned}
\]
The graph half-turn is the edge-label involution
\[
\rho(a_{i,j})=a_{3-i,n-j},\qquad
\rho(b_{i,j})=b_{2-i,n+1-j},\qquad
\rho(d_{i,j})=d_{2-i,n-j}.
\]
The rules show that \(\rho(P_{u,v})=P_{n-v,n-u}\). The assertions concern integral simplicial homology of the geometric realization, and its rational finite-group quotient. The collapse need not be equivariant; the *included target* and the inclusion map are equivariant.

## Proof
**1. An explicit missing simplex.** The perfect matchings \(P_{0,0}\) and \(P_{n,n}\) intersect exactly in the edge set \(D_n\); this also follows immediately from the displayed membership criteria. Furthermore \(x\) belongs to every \(P_{u,v}\) except \(P_{0,0}\), and \(y\) belongs to every \(P_{u,v}\) except \(P_{n,n}\). For every \(1\le i\le n-1\), the matching \(P_{i,i}\) contains \(x,y\) and every edge of \(D_n\) except \(d_{1,i}\). Hence every codimension-one subset of \(F_n\) is a face: omission of \(x\) is witnessed by \(P_{0,0}\), omission of \(y\) by \(P_{n,n}\), and omission of \(d_{1,i}\) by \(P_{i,i}\).

The complete set \(F_n\) is not a face. An extending perfect matching would have to contain \(x,y\), hence would be a nonextremal \(P_{u,v}\) with \(u>0\) and \(v<n\). Such a matching omits \(d_{1,j}\) whenever \(v\le j\le u\); there is at least one such \(j\in\{1,\ldots,n-1\}\). This proves \(K_n[F_n]=\partial\Delta(F_n)\), including the boundary case \(n=2\).

**2. Relative elementary collapse.** On the face poset of \(K_n\), including the empty face, first pair every face \(\sigma\) not containing \(x\) with \(\sigma\cup\{x\}\) whenever the latter is a face. On the faces not used in those pairs, perform the same element-pairing operation with \(y\). The union is acyclic by the ordered-element-matching lemma (Theorem 8 of [1], also an instance of the acyclic matching patchwork principle). We directly determine the critical faces.

Any face left after the \(x\)-pairing cannot be extended by \(x\), so it can only lie in the exceptional facet \(P_{0,0}\). If such a face omits \(y\), adding \(y\) stays within \(P_{0,0}\), and both it and the augmented face were unmatched at the first stage; they are paired at the second stage. Therefore any remaining face is \(\{y\}\cup B\), where \(B\subseteq P_{0,0}\), where \(B\cup\{x\}\) is a face but \(B\cup\{x,y\}\) is not. Since a witness to \(B\cup\{x\}\) cannot be an interior facet (which would also contain \(y\)), the witness must be \(P_{n,n}\). Thus \(B\subseteq P_{0,0}\cap P_{n,n}=D_n\). If \(B\ne D_n\), select an omitted \(d_{1,i}\); the interior perfect matching \(P_{i,i}\) contains \(B\cup\{x,y\}\), a contradiction. The unique critical face is therefore \(\{y\}\cup D_n=F_n\setminus\{x\}\).

Restrict these pairings to the induced boundary sphere \(L_n=K_n[F_n]\). Every face of \(L_n\) other than \(F_n\setminus\{x\}\) is paired at the *first* stage by toggling \(x\). Indeed every proper subset of \(F_n\) that is not \(F_n\setminus\{x\}\) can be extended by \(x\) inside the boundary sphere. The second-stage \(y\)-pairing has no face of \(L_n\) left to use. In both stages, toggling \(x\) or \(y\) preserves the property of having a vertex outside \(F_n\); consequently no matched pair crosses from \(L_n\) to its complement. Since all critical faces lie in \(L_n\), the relative face poset \(K_n\setminus L_n\) has a complete acyclic matching. The relative discrete-Morse collapse theorem, or equivalently deletion of the matched pairs in reverse topological order, gives a finite sequence of elementary simplicial collapses \(K_n\searrow L_n\). This is stronger than an abstract sphere homotopy equivalence.

**3. Half-turn character.** The stated edge involution interchanges \(x\) and \(y\), and sends \(d_{1,j}\) to \(d_{1,n-j}\), preserving \(F_n\). Its vertex permutation on the \(n+1\) vertices of the boundary simplex consists of the transposition \((x\ y)\) together with \(\lfloor(n-1)/2\rfloor\) transpositions among the significant edges. Its orientation degree on \(\partial\Delta(F_n)\) is exactly the sign of that permutation, \((-1)^{1+\lfloor(n-1)/2\rfloor}\). The inclusion \(L_n\hookrightarrow K_n\) is both a homotopy equivalence and \(\rho\)-equivariant, so it identifies these two integral top-homology actions. Finally, rational homology of a finite simplicial group-action quotient equals the invariant rational homology after barycentric subdivision, giving the stated quotient consequence.

## Verification
Execute the standalone `verify_honeycomb.py` using Python 3. It constructs the exact perfect-matching facets from the membership rules, independently verifies the edge involution on each facet, checks the missing-simplex boundary and relative pivot matching, performs actual elementary-collapse replay, and calculates the signed simplicial Lefschetz trace. For \(n=2,3,4\), the exhaustive face counts are respectively \(1347,17487,206127\), and the numbers of elementary collapses outside the embedded sphere are \(670,8736,103048\). The reduced Lefschetz values are \(1,1,-1\), agreeing with \((-1)^{n-1}\) times the claimed half-turn degree. These finite checks support but do not replace the uniform argument.

## Relationship to prior work
Bayer--Jelić Milutinović--Vega [1, Theorem 14] proved \(\mathcal M_p(H_{1\times2\times n})\simeq S^{n-1}\), and their proof supplies the same two ordered element pivots. The proof above credits that existing matching rather than claiming it as new. The additional observations are an explicitly located *invariant induced sphere* that is a simplicial collapse target, and the resulting exact integral central-half-turn orientation character. The nonequivariant homotopy type by itself does not determine either the embedded collapse or the group action. The distinct results [2,3] concern the ordinary (all matchings, not only extendible matchings) complex. Searches for equivalent half-turn, equivariant sphere and perfect-matching formulations did not locate a statement implying this joint conclusion.

## Limitations
The explicit collapse is not asserted to be equivariant; what is equivariant is the inclusion of its invariant target. No assertion is made about geometric fixed-point homotopy equivalence, quotient integral torsion, the larger exceptional automorphism group when parameters coincide, or other honeycomb dimensions. The novelty comparison is limited by indexing and by material accessible at the time of the literature inspection; an equivalent unindexed presentation remains possible.

## References
[1] M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (public 2022-09-06), Sections 1 and 3, Proposition 10 and Theorem 14. Published in Electronic Journal of Combinatorics 30(2), P2.45 (2023), doi:10.37236/11525. https://arxiv.org/html/2209.02803v1

[2] T. Matsushita, *Matching complexes of polygonal line tilings*, arXiv:1910.00186 (2019). https://arxiv.org/abs/1910.00186

[3] M. Bayer, B. Goeckner, M. Jelić Milutinović, *Manifold matching complexes*, Mathematika 66 (2020), 973-1002, doi:10.1112/mtk.12049. https://doi.org/10.1112/mtk.12049
