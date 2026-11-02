# Bridge factorization of chromatic polynomials of graph squares

## Finding

**Theorem (bridge factorization).** Let \(G\) be a finite, nonempty, simple connected graph. Delete all bridges of \(G\), obtaining connected components \(H_1,\ldots,H_r\). For each \(v\in V(H_i)\), write \(d_i(v)=\deg_{H_i}(v)\) and let \(t(v)\) be the number of original bridges incident with \(v\). Let \(P_X(q)\) denote the ordinary chromatic polynomial of the square \(X^2\), where vertices are adjacent in \(X^2\) when their distance in \(X\) is one or two. Set \((z)_{\underline k}=\prod_{j=0}^{k-1}(z-j)\), with empty product equal to one. Then

\[
P_G(q)=\frac{\displaystyle\prod_{i=1}^{r}P_{H_i}(q)}{[q(q-1)]^{r-1}}\prod_{i=1}^{r}\prod_{v\in V(H_i)}\bigl(q-d_i(v)-1\bigr)_{\underline{t(v)}}.
\]

The displayed rational expression has exact polynomial cancellation and equals the chromatic polynomial for all integers \(q\ge0\). In particular, with \(\chi\) denoting ordinary chromatic number,
\[
\chi(G^2)=\max\!\left\{\Delta(G)+1,\ \max_{1\le i\le r}\chi(H_i^2)\right\}.
\]
The convention \(\Delta(K_1)=0\) makes both assertions valid for a one-vertex graph.

**Arrangement-invariance consequence.** The polynomial \(P_G\) is determined by the multiset of core-square polynomials \(P_{H_i}\) together with the multiset of pairs \((d_i(v),t(v))\) over all core vertices, irrespective of the arrangement of the bridges among the cores. In particular, connecting four vertex-disjoint triangles by bridges using six distinct triangle attachment vertices yields
\[
P_G(q)=q(q-1)(q-2)^4(q-3)^6.
\]
One can arrange those bridges with a four-node path as core contraction or a four-node star. Those graphs have diameters seven and five, respectively, so they are nonisomorphic despite having identical square-chromatic polynomials; each has exactly \(192\) proper four-colorings of its square.

## Assumptions and scope

All graphs are finite, undirected and simple. An edge is a bridge when deleting it increases the number of connected components. The graph on the connected components of \(G\) minus its bridges, with one edge for each bridge, is a tree: connectivity is immediate, and a cycle of such bridge edges would contradict their being bridges. The notation \(P_X(q)\) counts proper named-color assignments to the vertices of \(X^2\); it is not the chromatic polynomial of \(X\) itself. Every core may be a singleton. No planarity, cactus, degree, or chordality assumption is needed.

## Proof

**Exact two-core extension.** Suppose a connected graph \(A\) is joined to a disjoint connected graph \(H\) by a *single* edge \(ca\), with \(c\in A\) and \(a\in H\). The square of the joined graph, restricted to \(A\), is precisely \(A^2\): no shortest path between two old vertices can be shortened by a detour entering and leaving the new graph through the same bridge. Fix any proper named \(q\)-coloring of \(A^2\), for an integer \(q\) sufficiently large for the following divisions. The closed neighborhood \(N_A[c]\) is a clique of \(A^2\), so its \(\deg_A(c)+1\) vertex colors are distinct.

The new vertex \(a\) has square-distance at most two to the old vertices *exactly* in \(N_A[c]\). Thus there are \(q-\deg_A(c)-1\) choices for its color \(\alpha\). Let \(\beta\) be the existing color at \(c\), necessarily distinct from \(\alpha\). Within \(H\), the only further restriction coming from an old vertex is that **every neighbor of \(a\)** avoid \(\beta\), because such vertices are distance two from \(c\). Vertices deeper in \(H\) lie at distance at least three from every vertex in \(A\), and the neighbors of \(a\) are distance at least three from old vertices other than \(c\).

Write \(d=\deg_H(a)\). In every proper coloring of \(H^2\), the \(d+1\) vertices of \(N_H[a]\) have pairwise different colors. Permuting the \(q\) named colors acts transitively, so exactly \(P_H(q)/q\) such colorings have the prescribed color \(\alpha\) at \(a\). Conditional on this, each of the \(q-1\) colors other than \(\alpha\) occurs on the \(d\) neighbors of \(a\) equally often, and their colors are distinct. Hence the fraction for which \(\beta\) is absent from these neighbors is \((q-1-d)/(q-1)\). The number of extensions of the fixed coloring is therefore
\[
\bigl(q-\deg_A(c)-1\bigr)\frac{P_H(q)}q\frac{q-d-1}{q-1}.
\]
This extension count does not depend on which proper coloring of \(A^2\) was fixed.

**Induction over the bridge tree.** Root its tree of components at \(H_1\), color that core first, then attach its child cores one by one, always along one bridge. Each added core \(H_i\) contributes the factor \(P_{H_i}(q)/[q(q-1)]\). For a bridge whose endpoints are \(c\) in the already attached graph and \(a\) in the fresh core, the numerator factors are \(q-\deg_A(c)-1\) and \(q-\deg_{H_i}(a)-1\). Whenever a vertex \(v\) of some core is incident with its successive attached bridges, its old degree is its internal degree \(d_i(v)\) plus the number of previously attached bridges. Thus its accumulated numerator is precisely \((q-d_i(v)-1)_{\underline{t(v)}}\). The one bridge leading from a nonroot core to its parent provides its first factor; later bridges provide the remaining ones. There are exactly \(r-1\) bridges, establishing the displayed product for all sufficiently large positive integers \(q\). Both sides are rational functions of \(q\), while the left is a polynomial. Equality at infinitely many integers yields the claimed polynomial identity and exact cancellation.

**Chromatic number.** For each core \(H_i\), its closed neighborhoods are square-cliques, so \(\chi(H_i^2)\ge d_i(v)+1\) for every \(v\in H_i\). If \(G\) has at least one bridge and \(q\ge\max_i\chi(H_i^2)\), a factor \((q-d_i(v)-1)_{\underline{t(v)}}\) is positive exactly when \(q\ge d_i(v)+t(v)+1\); otherwise that product contains a zero factor. Since \(\deg_G(v)=d_i(v)+t(v)\), the full factorization is positive exactly when \(q\) is at least the maximum in the corollary. For connected \(G\) with bridges, this threshold is at least two, so the denominator has no singularity there. If no bridges exist, \(r=1\) and the conclusion is immediate. \(G=K_1\) also follows directly. This proves the corollary.

**Chromatic equivalence example.** Four core triangles each have square polynomial \(q(q-1)(q-2)\). Any three bridges connecting the four cores at six distinct attachment vertices contribute six factors of \(q-3\). Cancelling three copies of \(q(q-1)\) gives \(q(q-1)(q-2)^4(q-3)^6\). Joining the four cores in path or star shape changes the diameter of the graph (seven versus five), so the two graphs are nonisomorphic. Substitution at \(q=4\) gives \(192\).

## Verification

A stand-alone Python 3 standard-library checker, `verify.py`, constructs each original graph, computes its distance-two adjacency, and counts its proper named-colorings by backtracking. The other side is independently constructed by deleting each edge in turn, identifying bridges via connectivity, forming bridge-free components, and evaluating the stated product as an exact rational number. Direct agreement was obtained for every connected labelled graph on at most five vertices, for palettes of sizes two through five: \(3088\) graph/palette checks. A further \(340\) randomly generated block-tree/palette checks agreed. Direct tests also confirm the nonisomorphic path/star bridge-tree pair, its value \(192\), and the nonchordal example of two length-six cycles joined by a bridge (\(768\) four-colorings of the square). Reproduce with `python verify.py`. These finite checks do not replace the preceding proof for arbitrary finite graphs.

## Relationship to prior work

Suvagiya's 2026 work determines two-distance chromatic and list-chromatic numbers for cactus graphs, including the role of five-cycles, but it does not provide this all-graphs exact coloring-count product. Its leaf-block technique is conceptually related, and the displayed chromatic-number formula specializes to that setting when combined with known cycle-square chromatic numbers. Agnarsson's 2003 work discusses clique-gluing identities for chromatic polynomials and chordal graph constructions. Clique-gluing is an acknowledged standard ingredient here; the contribution claimed is the explicit bridge-core factorization for **arbitrary graph squares**, including nonchordal ones, together with its arrangement-invariance and chromatic-number consequences. Other background on cycle-square colorability concerns the number of required colors rather than the full named-color enumeration. Priority remains subject to independently checking all differently phrased prior results.

## Limitations

The theorem concerns **ordinary** named-colorings of graph squares; it does not count list-colorings or extend the factorization to higher powers without modification. Computational checks are finite, while the proof covers all finite connected simple graphs. A complete historical-priority determination and independent mathematical review have not been performed. The formula can be evaluated numerically only to the extent that the core-square chromatic polynomials can be computed; no claim is made that those general computations are easy.

## References

1. V. Suvagiya, *Two-distance and list-two-distance coloring of cacti: the subcubic case and the C5 obstruction* (2026), arXiv:2609.20204v1, earliest publicly displayed date 2026-07-25; https://arxiv.org/abs/2609.20204.
2. G. Agnarsson, *On chordal graphs and their chromatic polynomials*, Mathematica Scandinavica 93 (2003), DOI:10.7146/math.scand.a-14421; https://doi.org/10.7146/math.scand.a-14421.
3. A. Prowse and D. R. Woodall, *Choosability of powers of circuits* (2003), used only as background for cycle-power coloring, as cited in Suvagiya (2026).
