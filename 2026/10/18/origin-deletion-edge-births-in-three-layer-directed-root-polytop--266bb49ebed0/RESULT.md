# Origin-deletion edge births in three-layer directed root polytopes

## Finding
Let \(A,B,C\) be three pairwise disjoint nonempty finite sets, with sizes \(a,b,c\), respectively. Form the directed graph with **all** arcs from \(A\) to \(B\), from \(A\) to \(C\), and from \(B\) to \(C\), and no other arcs. Its directed edge polytope is
\[
P_{a,b,c}=\operatorname{conv}\{e_u-e_v:u\in A,v\in B\text{ or }u\in A,v\in C\text{ or }u\in B,v\in C\}\subset\mathbb R^{a+b+c}.
\]
Write \(\widetilde P_{a,b,c}=\operatorname{conv}(P_{a,b,c}\cup\{0\})\). For **all** positive integers \(a,b,c\), the polytope \(P_{a,b,c}\) has affine dimension \(a+b+c-1\), exactly \(ab+ac+bc\) vertices, and the following *complete* one-skeleton classification.

Denote a vertex by its directed arc, of type \(AB\), \(AC\), or \(BC\). Two distinct vertices are adjacent exactly in the following cases:

1. **Same arc type:** the arcs have a common tail or a common head.
2. **Types \(AB,AC\):** the arcs have the same tail in \(A\).
3. **Types \(AC,BC\):** the arcs have the same head in \(C\).
4. **Types \(AB,BC\):** if the \(AB\) head and \(BC\) tail are *different* members of \(B\), the vertices are adjacent. If they are the *same* member of \(B\), they are adjacent **if and only if** \(b=1\).

Consequently, its exact number of edges is
\[
\boxed{f_1(P_{a,b,c})=
\frac{ab(a+b-2)+ac(a+c-2)+bc(b+c-2)}{2}
+abc(b+1)+ac\,\mathbf1_{b=1}.}
\]
The degree of each \(AB\)-type vertex, \(BC\)-type vertex, and \(AC\)-type vertex, respectively, is
\[
\boxed{a+b-2+bc+c\mathbf1_{b=1},\quad
b+c-2+ab+a\mathbf1_{b=1},\quad
a+c+2b-2.}
\]
The diameter of this polytope's one-skeleton is \(1\) for \((a,b,c)=(1,1,1)\), and \(2\) otherwise.

More sharply, compare the edge graph with that obtained by adjoining the origin. The graph of \(\widetilde P_{a,b,c}\) induced on its nonorigin vertices is obtained from the graph of \(P_{a,b,c}\) by deleting **exactly \(ac\) edges if \(b=1\), and none if \(b\ge2\)**. The deleted edges in the singleton-middle case are precisely the \(ac\) composable pairs \((u,w),(w,v)\), where \(u\in A,w\in B,v\in C\). Thus one intermediate vertex induces arbitrarily many new root-to-root edges on removing the origin, whereas two intermediate vertices prevent this phenomenon completely.

In particular, for \(a,b,c\ge2\), there are no simple vertices. For completeness, when \(b=1\), every \(AC\) vertex is simple, and \(AB\) vertices are simple precisely if \(c=1\), while \(BC\) vertices are simple precisely if \(a=1\). When \(b\ge2\), simple vertices can occur only for \(b=2,c=1\) (all \(AB\) vertices) or \(b=2,a=1\) (all \(BC\) vertices).

## Assumptions and scope
All sets are labeled; the standard coordinate vectors are orthonormal. Here adjacency refers to an exposed one-dimensional face of the polytope, **not** to adjacency in the underlying directed graph. \(\mathbf1_{b=1}\) is one for \(b=1\) and zero otherwise. The distinction between \(P_{a,b,c}\) and its origin-adjoined counterpart is essential. No other orientation or missing cross-layer arc is covered.

All root vectors have squared Euclidean norm two. Strict convexity of that norm implies every displayed root is a distinct vertex: a nontrivial convex combination of distinct roots has squared norm strictly less than two. Every root lies in \(H=\{x:\sum_i x_i=0\}\). The only linear functionals constant on all these roots are multiples of \(\sum_i x_i\): complete cross-layer arcs first force the potential constant within each part, and then equality of the three differences \(h_A-h_B=h_A-h_C=h_B-h_C\) forces each to vanish. Thus the affine hull is all of \(H\), of dimension \(a+b+c-1\). The origin is a vertex of \(\widetilde P\), since a potential strictly increasing from layer \(A\) through \(C\) is strictly negative on all roots and zero at the origin.

## Proof
For a potential \(h\) on \(A\sqcup B\sqcup C\), the root \((u,v)\) has score \(h_u-h_v\). Two roots form a polytope edge precisely when a potential makes these two, and no other roots, attain the same maximum. This criterion is valid even if that maximum is negative.

**Exposing every claimed edge.** Each homogeneous arc block (\(AB\), \(AC\), or \(BC\)) is an exposed face and is the product of the two corresponding simplices. Indeed constant potentials on \((A,B,C)\) of \((2,0,1)\), \((2,1,0)\), and \((1,2,0)\) expose the three respective blocks. In a product of simplices, two vertices are adjacent exactly when they share one product factor, which proves every same-type assertion. More explicitly, multiply these three baseline potentials by ten and alter the designated common tail by \(+2\) and the two heads by \(-2\), or alter the two tails by \(+2\) and the common head by \(-2\). The selected scores then equal \(24\), while every other root scores at most \(22\).

For an \(AB\) root \((u,w)\) and an \(AC\) root \((u,v)\) with the same \(A\)-tail, set potential \(2\) at \(u\), \(0\) at all other \(A\) entries, \(0\) at \(w,v\), and \(1\) at every remaining \(B,C\) entry. Exactly the selected two roots score \(2\), all others scoring at most \(1\). Similarly, for \(AC\) \((u,v)\) and \(BC\) \((w,v)\) sharing the \(C\)-head, set potential \(2\) at \(u,w\), \(0\) at \(v\) and all other \(A\) entries, and \(1\) at every remaining \(B,C\) entry. Again exactly the selected scores are \(2\), all others at most \(1\).

For \(AB\) \((u,w)\) and \(BC\) \((w',v)\) with \(w\ne w'\), assign potential \(1\) to \(u\), \(-1\) to all other \(A\) entries, \(0\) to \(w\), \(2\) to \(w'\), \(1\) to all remaining \(B\) entries, \(1\) to \(v\), and \(3\) to all other \(C\) entries. Exactly those two roots score \(1\); all others score at most zero.

Finally, if \(b=1\) and \(w\) is its unique middle vertex, expose the composable pair \((u,w),(w,v)\) by assigning \(0\) to \(u\), \(-2\) to all other \(A\) entries, \(1\) to \(w\), \(2\) to \(v\), and \(4\) to all other \(C\) entries. The selected pair scores \(-1\); all other roots score at most \(-2\). This proves every asserted edge for every positive \(a,b,c\).

**Excluding every other pair.** Suppose two distinct candidate roots share no allowed adjacency pattern. In each case their vector sum has another decomposition as a sum of two *different* root vertices: disjoint tails and heads within one arc block admit the swapped-head decomposition; \(AB,AC\) roots with different \(A\)-tails admit swapped tails; \(AC,BC\) roots with different \(C\)-heads admit swapped heads; and \(AB\) \((u,w)\) plus \(BC\) \((w,v)\) with \(b\ge2\) has, for any \(w'\ne w\), the alternative decomposition
\[
(e_u-e_w)+(e_w-e_v)=(e_u-e_{w'})+(e_{w'}-e_v).
\]
An exposing functional strictly maximized at the chosen two roots would give their sum a strictly larger score than the alternative pair, contradicting equality. These are all possible types of unordered root pairs, completing the edge classification.

**Origin deletion.** All displayed edge witnesses have positive maximum, except the composable pairs in the singleton-middle case, whose witness has maximum \(-1\). Therefore every positive-witness edge remains an edge of \(\widetilde P\). Conversely, for the composable pair \((u,w),(w,v)\), the third root \((u,v)\) is present and satisfies \(r_{uw}+r_{wv}=r_{uv}\). If both selected roots have common exposing maximum \(T\), the long root scores \(2T\); for a strict two-vertex maximum we must have \(T<0\). The origin scores \(0>T\), so no such pair is an edge of \(\widetilde P\). Adding a vertex cannot create a previously nonexistent edge among the old vertices, because any exposing functional for a pair in the larger polytope also exposes that pair in the smaller one. The exact origin-deletion statement follows.

**Counts, degrees, diameter, simplicity.** Within the \(XY\) block of sizes \(p,q\) there are \(p\binom q2+q\binom p2=pq(p+q-2)/2\) edges. The \(AB/AC\) and \(AC/BC\) cases each contribute \(abc\); \(AB/BC\) contributes \(acb(b-1)\), plus \(ac\) when \(b=1\). Adding yields the boxed edge formula. Counting incident same-type and cross-type neighbors at each root yields the three displayed degrees. Every nonadjacent pair has a two-edge path: swap one tail or one head in the offending pair, or use \((u,v)\) as the common neighbor for a nonadjacent composable pair. The graph is complete only when all three blocks have one vertex, proving the diameter formula. Subtracting the dimension \(a+b+c-1\) from the three degrees gives, for \(b\ge2\), the excesses \(c(b-1)-1\), \(a(b-1)-1\), and \(b-1\); for \(b=1\) they are \(c-1\), \(a-1\), and \(0\). Their zero sets give precisely the claimed simple vertices.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. The file enumerates all \(125\) triples \(1\le a,b,c\le5\), totaling \(3375\) roots and \(24975\) predicted polytope edges. For every predicted edge, it reconstructs the stated *integer* exposing potential and strictly compares its score with every other root. For every excluded pair, it independently finds a second root-pair decomposition of exactly the same integral sum vector. It also checks the edge-count and local-degree formulas, graph diameter at most two, and that exactly \(ac\) edge witnesses have negative support when \(b=1\), with zero otherwise. The checker printed `VERIFY_OK parameter_profiles= 125 vertices_total= 3375 edges_total= 24975`. Exhaustive finite profiles only corroborate the universally quantified proof above; no infinite conclusion relies on their exhaustion.

## Relationship to prior work
Numata, Takahashi, and Tamaki, *Faces of Directed Edge Polytopes* (arXiv:2203.14521v1, 2022), establish a general facet characterization for directed edge polytopes and their dimensions. Their full paper's statements and examples concern facet criteria and forest/cycle families, not this explicit three-layer graph, its local degrees, or the origin-deletion threshold.

Setiabrata, *Faces of Root Polytopes* (arXiv:2001.05191, first available 2020), gives broad combinatorial characterizations of **faces of origin-adjoined** acyclic root polytopes; these indeed include the surviving nonorigin edges of \(\widetilde P\) here. We do **not** claim a new general origin-adjoined face criterion. The point requiring additional analysis is the exact graph of the non-origin-adjoined \(P\), especially the complete quadratic family of edges that emerge when the origin is removed for \(b=1\), and their disappearance as soon as \(b\ge2\). The general characterizations provide background but do not state this transition or the displayed one-skeleton/degree census. An earlier indexed result on the full transitive-tournament positive-root polytope describes a different graph: it retains within-layer arcs and reports only linearly many edges born upon removing the origin, rather than the arbitrary quadratic \(ac\) here.

## Limitations
The theorem is confined to complete, transitively oriented three-layer digraphs; it does not enumerate higher-dimensional faces or classify arbitrary directed graphs. The one-skeleton could also be recovered by substantial specialization of general face-characterization machinery, so priority for the explicit classification has not been externally adjudicated. Unindexed or differently named equivalent results remain possible. The exact finite checker is corroborative, not a substitute for proof. Independent mathematical audit has not been performed.

## References
- Y. Numata, Y. Takahashi, D. Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521v1, first public 2022-03-28, primary MSC2020 52B05. https://arxiv.org/pdf/2203.14521
- L. Setiabrata, *Faces of Root Polytopes*, arXiv:2001.05191, first public 2020-01-15; revised full text arXiv:2001.05191v2. https://arxiv.org/pdf/2001.05191
