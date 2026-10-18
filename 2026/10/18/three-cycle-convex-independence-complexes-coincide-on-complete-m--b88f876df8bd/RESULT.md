# Three cycle-convex independence complexes coincide on complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite simple graph, with \(r\ge2\), \(n_i\ge1\), and \(N=\sum_i n_i\). Three families of independent sets in cycle convexity—Helly, Radon and convex independence—are **the same family**, denoted \(\Delta(G)\). It is a simplicial complex, with empty face included and face polynomial \(F_G(z)=\sum_{S\in\Delta(G)}z^{|S|}\).

There are exactly three cases.

1. If \(r=2\) and \(\min(n_1,n_2)=1\), \(G\) is a star and \(\Delta(G)\) is the full simplex on \(N\) vertices; thus \(F_G(z)=(1+z)^N\) and its realization is contractible.
2. If \(G=K_{a,b}\) with \(a,b\ge2\), the faces are precisely all subsets contained in a single part and every mixed subset of cardinality at most three. Here
\[
F_G(z)=(1+z)^a+(1+z)^b-1+abz^2+\left(a\binom b2+b\binom a2\right)z^3,
\qquad
\Delta(G)\simeq\bigvee^{1+ab(a+b-4)/2}S^2.
\]
3. If \(r\ge3\), the faces are precisely all subsets contained in one part and every mixed pair. Writing \(E=\sum_{1\le i<j\le r}n_i n_j\),
\[
F_G(z)=\sum_{i=1}^r(1+z)^{n_i}-r+1+Ez^2,
\qquad
\Delta(G)\simeq\bigvee^{E-r+1}S^1.
\]

All three maximum-cardinality parameters equal \(N\) for stars, \(\max\{a,b,3\}\) for cyclic complete bipartite graphs, and \(\max\{2,\max_i n_i\}\) for graphs with at least three parts. The wedge multiplicities count spheres; empty wedges do not occur in the last two cases.

## Assumptions and scope
For a finite simple graph and vertex subset \(S\), the **cycle interval** \(I(S)\) adds a vertex \(w\notin S\) exactly when the induced graph \(G[S\cup\{w\}]\) contains a simple cycle through \(w\). Iterating until stable gives \(\operatorname{hull}(S)\). Equivalently, \(w\) enters \(I(S)\) exactly when it has two neighbours in the same connected component of \(G[S]\): the connecting path together with the two edges through \(w\) forms the requisite cycle.

A nonempty set \(S\) is **convexly independent** when \(v\notin\operatorname{hull}(S\setminus\{v\})\) for every \(v\in S\). It is **Helly independent** when \(\bigcap_{v\in S}\operatorname{hull}(S\setminus\{v\})=\varnothing\). It is **Radon independent** when every partition \(S=A\sqcup B\) into two nonempty blocks satisfies \(\operatorname{hull}(A)\cap\operatorname{hull}(B)=\varnothing\). Empty sets are independent by convention. These independence notions are hereditary, so each defines a simplicial complex before the equivalence is proved. The term *independence complex* here refers to these cycle-convexity families, **not** the ordinary stable-set complex of the graph.

## Proof
**1. Determine all hulls.** A set entirely within one part has no edges, so its hull is itself. If \(G\) is a star, it has no cycles at all and every set has itself as hull.

Suppose \(G=K_{a,b}\) with \(a,b\ge2\). Every mixed pair is convex: a simple cycle in a bipartite graph requires at least four vertices. Every mixed triple contains two vertices from one part and one from the other. Each as-yet-unselected vertex in the singleton-represented part is on a four-cycle with those three chosen vertices; once one is generated (such a vertex exists because both part sizes are at least two), the remaining vertices in the other part likewise enter through four-cycles. Consequently every mixed set with at least three vertices generates all of \(V(G)\). The argument is symmetric in the parts.

Now suppose \(r\ge3\). Every mixed pair \(\{x,y\}\), with vertices in different parts, generates any vertex in a third part through a triangle. The resulting third-part vertex forms triangles with every other vertex in either of the original two parts; once these are included, any further part is also generated through a triangle. Thus \(\operatorname{hull}(\{x,y\})=V(G)\). Hence the hulls in these three cases have been completely classified.

**2. Translate hulls into independent faces.** Every pure-part subset is independent under all three notions, as each of its subsets has its own set as hull. In a star every subset is independent. In the bipartite cyclic case every mixed set of size two or three is independent: all of its proper subsets occurring in independence tests have at most two vertices, hence have themselves as hulls. For a mixed set with at least four vertices, some proper triple is mixed. Choose \(v\in S\) so that \(S\setminus\{v\}\) contains that triple; thus its hull is all of \(V(G)\). This violates convex independence. For Helly independence, choose any mixed triple \(T\subset S\); the hull of \(S\setminus\{v\}\) is all of \(V(G)\) whenever \(v\notin T\), and for \(v\in T\) it always contains \(S\setminus\{v\}\). Because \(|S|\ge4\), a direct count of each possible part composition (at least three in one part, or at least two in both parts) gives a nonempty common intersection. More explicitly, if a part has at least three chosen vertices then any vertex of that part lies in every deletion hull except possibly its own, in which case the other part's selected vertex and two remaining same-part vertices generate the full graph. In the remaining case both parts contain at least two chosen vertices, and all deletion hulls equal \(V(G)\). For Radon independence partition \(S\) into a mixed triple and its nonempty complement: the triple's hull is all vertices, so the hulls intersect. Therefore all three families equal the stated bipartite collection.

For \(r\ge3\), every mixed pair is independent, since its one-vertex deletion hulls are singletons and disjoint. Every mixed triple or larger set contains a mixed pair with a nonempty complement. Its hull is all vertices, proving Radon dependence. Some deletion preserves a mixed pair, proving convex dependence. For Helly dependence, choose a mixed pair \(T=\{x,y\}\subset S\) and, if \(|S|\ge3\), let \(z\in S\setminus T\). The hull of \(S\setminus\{z\}\) is all vertices; more generally each deletion hull either is all vertices or contains \(S\setminus\{v\}\). If all chosen vertices except possibly one lie in one part, their common part still contains a vertex surviving every nontrivial deletion hull. If at least three parts are represented, every deletion hull contains a cross pair and is all vertices. This establishes nonempty intersection in every case. The three families therefore coincide for all part sizes.

**3. Enumerate.** Pure-part faces contribute \(\sum_i(1+z)^{n_i}-r+1\), correcting for the empty face counted \(r\) times. Mixed pairs contribute \(ab\) in the bipartite case and \(E\) in the multipartite case. Bipartite mixed triples contribute \(a\binom b2+b\binom a2\); no other mixed faces survive. The stated face polynomials and maximum cardinalities follow.

**4. Determine integral homotopy types.** In the common complex, the vertices of each part span their entire simplex. Collapsing these mutually disjoint contractible subcomplexes one by one to distinct vertices is a homotopy equivalence, by the CW cofibration property. The resulting CW complex has \(r\) zero-cells and one one-cell for each edge joining different parts. In the \(r\ge3\) case it has no higher cells and is connected, so it is a wedge of \(E-r+1\) circles.

In the bipartite cyclic case, the quotient has two zero-cells, \(ab\) one-cells, and \(T=a\binom b2+b\binom a2\) two-cells, with no higher-dimensional cells. The original complex contains the full two-skeleton of the simplex on its \(a+b\) vertices, hence is simply connected; attaching higher-dimensional pure-part simplices cannot introduce fundamental-group elements. The quotient is also simply connected. Its Euler characteristic is \(2-ab+T\), so its free integral second homology has rank \(1-ab+T=1+ab(a+b-4)/2\). A simply connected, two-dimensional CW complex is homotopy equivalent to a wedge of as many two-spheres as its second Betti number (by Hurewicz and the homology Whitehead theorem). This proves the wedge formula. The star case is a full simplex, hence contractible.

## Verification
Run `python3 verify.py` using the standard library. The independent checker constructs all cycle hulls using the connected-component criterion, then tests each of the three independence predicates directly; it does not use the predicted face classification to perform those predicate tests. It independently computes the reduced simplicial Betti numbers over \(\mathbb F_2\) and compares them with the wedge formulas. All 58 unordered multipartite types on two through eight vertices passed, representing 2,414 independent faces. The program tests finite cases only; the unrestricted assertion and integral homotopy conclusion rely on the proof above.

## Relationship to prior work
Nair, Anand, Chandran, Nascimento and Anil introduced complexity and extremal investigations of the Helly, Radon and rank parameters for cycle convexity; their September 2026 paper studies decision hardness and near-maximal \(N-1\) and \(N-2\) structures, not the three complete families and their homotopy types on complete multipartite graphs. The April 2026 paper by Nair and collaborators determines **Carathéodory** numbers for this family, including the value three for \(K_{a,b}\) with \(a,b\ge2\); Carathéodory independence is a different notion and its known numerical statement is not claimed here. An earlier 2026 paper on cycle-convex rank and general-position number is a material bibliographic comparison risk because its complete text was not available for inspection.

The published dissociation-polynomial result for complete multipartite graphs implies the same *face-count formula* in the \(r\ge3\) case for the **different** maximum-induced-degree-one set family; this counting identity by itself is not an originality claim. The contribution is the common identification of three cycle-convex independence families, the exceptional bipartite mixed triples, and their integral wedge homotopy types. A related preprint about ordinary graph independence complexes studies a different simplicial construction.

## Limitations
Only connected complete multipartite simple graphs with at least two nonempty parts are asserted. The theorem does not address disconnected graphs, other convexity rules, Carathéodory-independent families, or external independent verification. A complete published priority determination was not possible for the prior conference work whose open preprint was access-restricted. The computer check is bounded and mod-two; it is not a certificate of the integral infinite-family statement.

## References
1. R. S. Nair, B. S. Anand, U. C. S. V. Chandran, J. R. Nascimento, and A. Anil, *Computing the Helly Number, Radon Number and Rank in Cycle Convexity*, arXiv:2609.34236v1 (first public 2026-09-28).
2. R. S. Nair, B. S. Anand, U. C. S. V. Chandran, and J. R. Nascimento, *Carathéodory Number in Cycle Convexity*, arXiv:2604.20097v1 (first public 2026-04-22), especially the complete multipartite discussion and Corollary 7.
3. *On the Rank and the General Position Number in Cycle Convexity*, IWOCA 2026, DOI:10.1007/978-3-032-27732-9_6. Full text not obtained in this review.
4. *Dissociation polynomials of complete multipartite graphs and their coefficientwise extremizers*, published-finding corpus, published 2026-10-04, exact title as listed; summary inspected, full record unavailable.
