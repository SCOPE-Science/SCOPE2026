# The Wiener index determines the VC-shattering profile of tree-geodesic halfspaces

## Finding
Let \(T=(V,E)\) be any finite, nonempty, simple undirected tree with \(n=|V|\). A subset \(H\subseteq V\) is a *geodesic halfspace* when both \(H\) and \(V\setminus H\) are geodesically convex; include \(\varnothing\) and \(V\). Let \(\mathscr H(T)\) be this Boolean vertex-membership concept class. For each \(j\ge0\), write \(s_j(T)\) for the number of \(j\)-vertex supports shattered by \(\mathscr H(T)\), and let \(\Phi_T(z)=\sum_j s_j(T)z^j\). Define the Wiener index \(W(T)=\sum_{\{u,v\}\subseteq V}d_T(u,v)\), with the empty sum equal to zero.

**Theorem.** All geodesic halfspaces are \(\varnothing\), \(V\), and the two components of \(T-e\), for each \(e\in E\). A support is shattered precisely when it has at most two vertices, or has exactly three vertices with no one vertex on the unique path between the other two. Consequently, for all \(n\ge1\),
\[
\boxed{\Phi_T(z)=1+nz+\binom n2z^2+\left(\binom n3+\binom n2-W(T)\right)z^3.}
\]
Here \(\binom nj=0\) for \(j>n\). In particular, the coefficient of \(z^3\) recovers the Wiener index exactly, and the VC dimension is \(1\) for \(n=1\), \(2\) for paths with \(n\ge2\), and \(3\) for nonpath trees.

For \(n\ge4\), the sharp coefficient extremes over all \(n\)-vertex trees are
\[
0\le [z^3]\Phi_T(z)\le\binom{n-1}{3},
\]
with equality on the left only for the path and on the right only for the star. Thus the complete halfspace shattering polynomial is identical for two trees of the same order exactly when their Wiener indices agree.

## Assumptions and scope
Graphs are finite, undirected, unweighted, loopless trees. Geodesic convexity means containing **every** vertex of the unique path between any two vertices in the set. The concept family contains the two trivial halfspaces; omitting them would change the shattering polynomial. Shattering means realizing **all** \(2^{|S|}\) Boolean membership traces on \(S\), not merely isolating each member. Singleton trees and two-vertex trees are included. No probabilistic, weighted, directed, or online-learning claim is made.

## Proof
**1. Characterization of halfspaces.** Every convex subset of a tree is a connected induced subtree, with empty sets allowed. If both \(H\) and \(V\setminus H\) are nonempty and connected, exactly one edge joins them: at least one by connectedness of \(T\), and two would form a cycle with paths inside the two sides. Therefore \(H\) is a component of deleting this unique edge. Conversely every component of \(T-e\) and its complement are connected, hence convex. Distinct oriented edges give distinct nontrivial halfspaces; thus \(|\mathscr H(T)|=2n\).

**2. Supports of size at most two.** On a singleton, both labels are realized by the trivial halfspaces. For two distinct vertices \(a,b\), any edge on their unique path yields the two singleton traces, and the trivial halfspaces yield the empty and full traces. Hence all supports of cardinality zero, one, or two are shattered.

**3. Triple characterization.** If \(b\) lies strictly on the path from \(a\) to \(c\), a convex concept cannot contain \(a,c\) while excluding \(b\), so \(\{a,b,c\}\) is not shattered. Otherwise the three paths between the vertices meet at a unique median vertex \(m\) *not among the three*. Each of the three vertices lies in a different component of \(T-m\). Cutting the first edge in each of the three branches yields one halfspace whose trace on the support is the indicated singleton; cutting the same edge in the opposite orientation yields the complementary two-element trace. The trivial halfspaces give the other two traces. Thus the triple is shattered.

**4. No larger supports.** Every pair of tree edge-splits is compatible: of the four intersections of their two unordered bipartition sides, at least one is empty. Indeed, deleting both edges gives exactly three components, and a side of one edge-cut is contained within a side of the other. On four distinct support vertices \(a,b,c,d\), the three distinct two-versus-two dichotomies \(ab|cd\), \(ac|bd\), and \(ad|bc\) are pairwise crossing; any two realize all four quadrant intersections on the support. A shattered four-point support would require at least two crossing edge-splits, impossible. The trivial halfspaces do not realize a two-versus-two dichotomy. Therefore no four-point support is shattered. Heredity of shattering excludes all larger supports.

**5. Distance enumeration.** Each unshattered triple has exactly one point strictly between its other two points on a tree path. For every unordered endpoint pair \(\{u,v\}\), there are exactly \(d_T(u,v)-1\) choices of that third point. Every collinear triple is counted exactly once, since its middle vertex is unique. Hence the number of unshattered triples is
\[
\sum_{\{u,v\}}(d_T(u,v)-1)=W(T)-\binom n2.
\]
Subtracting this from the \(\binom n3\) total triples gives the stated cubic coefficient, while Steps 2 and 4 give all other coefficients.

**6. Extremal and equality statements.** For each edge \(e\), let \(s_e\) be the size of one component of \(T-e\). Counting contributions of edges to vertex-pair distances gives
\[
W(T)=\sum_{e\in E}s_e(n-s_e).
\]
For \(1\le s_e\le n-1\), each summand is at least \(n-1\), with equality only when one side is a singleton. Thus \(W(T)\ge(n-1)^2\), with equality for \(n\ge4\) precisely when every edge is pendant, namely for the star. This gives the maximum shattered-triple count \(\binom{n-1}{3}\). The minimum is zero, attained precisely when no triple has a median strictly outside it, equivalently when every vertex has degree at most two; a connected tree with this property is a path. When \(n\le3\), the path/star descriptions naturally coincide or degenerate.

## Verification
`VERIFY.py` is a standalone standard-library program. It constructs tree distances with breadth-first search; independently enumerates geodesically convex subsets by checking path containment and then keeps those whose complements are convex; separately constructs the edge-cut family; and independently enumerates all Boolean traces on all supports. It checks the coefficient identity, the precise support criterion, the edge-split Wiener formula, and star/path boundaries. It exhaustively covers all \(1+1+3+16+125+1296=1442\) labeled trees with at most six vertices, generated from Prüfer words, plus 120 deterministically generated trees of orders seven through ten. The program is finite corroboration and is not used to establish the universal quantifiers.

Run with `python3 VERIFY.py`; the final success marker is `ALL_TREE_HALFSPACE_WIENER_CHECKS_PASS`.

## Relationship to prior work
Thiessen and Gärtner (2021) study geodesically convex graph halfspaces, active membership-query complexity and VC-dimension bounds. Their Proposition 14 gives the already-known bound \(\operatorname{VCdim}\le2\operatorname{tw}(G)+1\); for trees this is three. This upper bound and the basic halfspace definition are *not* claimed as new. The present statement instead determines **all shattered supports** and **every coefficient** on every tree, and identifies its triple coefficient with the classical Wiener index. Their main text, including the VC-dimension proposition and tree discussion, was examined; it does not state this coefficientwise distance identity.

Anthony and Ratsaby (2018) study a different notion of a distance halfspace defined by proximity to two prototypes; the inspected definition is not the class of subsets with both sides geodesically convex. Thiessen and Gärtner (2022) investigate online learning of convex sets on graphs; their accessible descriptive record was checked, but the full text could not be retrieved for a comprehensive priority comparison. A published mathematical record on tree-Wiener energy concerns Euclidean configurations on simplex edges rather than shattered supports of tree cuts. The relationship to general tree split systems and the classical Wiener index remains a historical-priority risk: an equivalent count may have appeared without the learning-theoretic terminology.

## Limitations
This is an exact mathematical identity, not a claim of a new VC-dimension upper bound or a new theorem about the extremal Wiener index by itself. The result excludes arbitrary convex subsets (which need not have convex complements), and it does not determine Littlestone dimension, active query complexity, or graph families with cycles. The formal proof is self-contained, with finite computations used only as corroboration. Independent scientific validation has not been performed; historical completeness of the literature comparison is not guaranteed.

## References
1. M. Thiessen and T. Gärtner, *Active Learning of Convex Halfspaces on Graphs*, NeurIPS 34 (2021). Full text: https://papers.nips.cc/paper/2021/file/c4bf1e24f3e6f92ca9dfd9a7a1a1049c-Paper.pdf ; DOI 10.34726/1841.
2. M. Thiessen and T. Gärtner, *Active Learning Convex Halfspaces on Graphs*, SubSetML at ICML (24 July 2021), DOI 10.34726/3901.
3. M. Thiessen and T. Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD (2022), DOI 10.1007/978-3-031-26412-2_22.
4. M. Anthony and J. Ratsaby, *Large-width bounds for learning half-spaces on distance spaces*, Discrete Applied Mathematics 243 (2018), 73–89, DOI 10.1016/j.dam.2018.02.004. The relevant distance-prototype halfspace definition differs from geodesic convex halfspaces.
