# A matching expansion for convex sets in graph subdivisions

## Finding

For a finite simple graph \(G=(V,E)\), replace each edge \(uv\) by a two-edge path \(u-e_{uv}-v\); call the resulting graph \(S(G)\). Let \(Q_G(z)\) be the generating polynomial of all \(P_3\)-convex vertex sets of \(S(G)\), counted by their numbers of vertices. Write \(d_A(v)=|N_G(v)\cap A|\), and let \(\mathcal M(H)\) denote the set of all matchings of a graph \(H\), including the empty matching. Then the **subdivision matching expansion** is

\[
Q_G(z)=\sum_{A\subseteq V}z^{|A|+|E(G[A])|}
\sum_{M\in\mathcal M(G[V\setminus A])}z^{|M|}
\prod_{v\in(V\setminus A)\setminus V(M)}(1+d_A(v)z).
\]

In particular, for every integer \(n\ge2\), the one-subdivision of the complete graph has the explicit **coefficient polynomial**

\[
Q_{K_n}(z)=\sum_{a=0}^{n}\binom na z^{\binom{a+1}{2}}
\sum_{j=0}^{\lfloor(n-a)/2\rfloor}
\frac{(n-a)!}{2^j j!(n-a-2j)!}
 z^j(1+az)^{n-a-2j}.
\]

All exponents \(0\le s\le\binom{n+1}{2}\) that have nonzero coefficients are exactly

\[
\{0\}\ \cup\ \bigcup_{a=1}^{n}
\bigl\{\binom{a+1}{2},\,\binom{a+1}{2}+1,\ldots,\,
 n+\binom a2\bigr\}.
\]

There are consequently **exactly** \(\lfloor(n-1)^2/4\rfloor\) cardinalities in that range for which no convex set exists. For \(n\ge3\), the largest proper convex set has \(\binom{n}{2}+1\) vertices, with exactly \(n(n-1)\) such sets.

More generally, when \(G\) is connected and \(|V|\ge2\), the greatest size of a **proper** \(P_3\)-convex set in \(S(G)\) is \(|V|+|E|-\delta(G)\), where \(\delta(G)\) is the minimum degree of \(G\).

## Assumptions and scope

Graphs are finite, simple, undirected and labelled. A vertex set \(C\) is \(P_3\)-convex precisely when every vertex outside \(C\) has at most one neighbor in \(C\); both the empty and full sets count. Each original edge gives one distinct subdivision vertex. A matching is a set of pairwise vertex-disjoint edges. The matching expansion includes disconnected graphs and isolated vertices; the largest-proper-set statement assumes connectedness and at least two original vertices. Polynomial coefficients count labelled vertex subsets, not isomorphism classes. All integers \(n\ge2\) are included in the complete-graph formula and gap count.

## Proof

**Matching decomposition.** Fix a convex set \(C\subseteq V(S(G))\), and let \(A=C\cap V(G)\), \(B=V(G)\setminus A\). A subdivision vertex \(e_{uv}\) omitted from \(C\) would have both neighbors in \(C\) if \(u,v\in A\); hence **every** edge of \(G[A]\) has its subdivision vertex selected. Conversely, subdivision vertices with at most one endpoint in \(A\) have no such forced inclusion.

An original vertex \(v\in B\) has no selected original neighbors in \(S(G)\), so convexity requires at most one selected incident subdivision vertex. In particular, selected subdivision vertices corresponding to edges entirely within \(B\) form a matching \(M\) in \(G[B]\). Every vertex of \(V(M)\) has already used its one available incidence, and cannot support another selected subdivision vertex. Independently, each vertex \(v\in B\setminus V(M)\) may support either no selected edge to \(A\) or the subdivision vertex of **one** of its \(d_A(v)\) cross edges. This is all: each omitted subdivision vertex has zero, one or two original neighbors selected; the two-neighbor case was forced selected in the first step. Thus the conditions are both necessary and sufficient. The fixed \(A,M\) contribution is exactly the first displayed product; summing proves the expansion without overlaps.

**Complete graph.** For \(G=K_n\), write \(a=|A|\), \(b=n-a\). There are \(\binom na\) choices for \(A\) and \(\binom a2\) forced internal subdivision vertices. Every unmatched vertex of \(B\) has \(d_A(v)=a\). The number of matchings of size \(j\) in \(K_b\) is \(b!/(2^jj!(b-2j)!)\). Substituting proves the second displayed polynomial.

For \(a\ge1\), choose the empty matching and select exactly \(t\) cross-edge subdivision vertices, one at each of \(t\) distinct vertices of \(B\), for every integer \(0\le t\le n-a\). Hence every exponent in the displayed interval for \(a\) occurs. No larger exponent can occur for that \(a\): with a matching of size \(j\), one can select at most \(j+(n-a-2j)=n-a-j\) additional subdivision vertices beyond those forced. For \(a=0\), all selected subdivision vertices form a matching and yield just the exponents from \(0\) to \(\lfloor n/2\rfloor\), already included in \(\{0\}\) and the interval for \(a=1\). This proves the exact support.

Let \(L_a=\binom{a+1}{2}\) and \(U_a=n+\binom a2\). The count of integers strictly between the successive intervals \([L_a,U_a]\) and \([L_{a+1},U_{a+1}]\) is \(\max\{0,L_{a+1}-U_a-1\}=\max\{0,2a-n\}\). Summing over \(1\le a\le n-1\) gives \(\lfloor(n-1)^2/4\rfloor\). Note that \(U_n=L_n=\binom{n+1}{2}\), so these account for *every* missing cardinality.

**Largest proper sets.** Suppose \(G\) is connected, \(n=|V|\ge2\), and \(C\ne V(S(G))\). If every original vertex were in \(C\), every subdivision vertex would be forced in, contradicting properness. Thus \(B=V\setminus A\ne\emptyset\). There are exactly \(|E(G[A])|\) selected internal subdivision vertices; every other selected subdivision vertex touches \(B\), and each vertex of \(B\) is incident with at most one of them. Consequently

\[
|C|\le |A|+|E(G[A])|+|B|=n+|E(G[A])|
\le n+|E|-\delta(G),
\]

because an excluded original vertex has at least \(\delta(G)\) incident edges not lying in \(G[A]\). Equality is attained by omitting a minimum-degree original vertex \(v\), including every other original vertex and every subdivision vertex associated with \(G-v\), and also including exactly one subdivision vertex on an edge incident with \(v\). Its convexity follows from the matching decomposition. This yields the claimed maximum. In \(K_n\), \(n\ge3\), the preceding bound is strict whenever at least two original vertices are omitted: for \(|B|\ge2\), the graph \(G[A]\) loses strictly more than \(n-1\) edges. Therefore each largest proper convex set is uniquely specified by one excluded original vertex and one of its \(n-1\) incident subdivision vertices. There are \(n(n-1)\) such sets.

## Verification

The standalone standard-library program `verify.py` checks the formula independently by enumerating all vertex subsets in every one-subdivision of all labelled simple graphs on at most five original vertices (1,099 graph instances); it also checks the connected-case extremal formula on 771 graphs. It checks the full complete-graph coefficient formula by direct enumeration for orders two through five and its support, omitted-cardinality count, and largest-proper coefficient through order 25. All checks passed. Direct finite enumeration supports the statements, but the arguments above establish their validity for all claimed graph orders.

Run: `python3 verify.py`.

## Relationship to prior work

Dourado, Grippo, Lin and Protti (2026) established the general framework for counting \(P_3\)-convex sets, including hardness on split graphs, tractable classes of trees and threshold graphs, and exact general algorithms. Their inspected preprint does not give the subdivision matching expansion, the complete-subdivided-clique polynomial or the quadratic missing-cardinality theorem. Existing work on \(P_3\)-convexity of Hamming graphs studies different graph families and chiefly Carathéodory/hull invariants rather than this all-coefficient count. The present result is a structural specialization and enumerative refinement, not a claim to have introduced \(P_3\)-convexity or the general counting problem.

## Limitations

No claim is made that the general matching expansion yields a polynomial-time counting algorithm for arbitrary \(G\): its outer subset sum can be exponential. The missing-cardinality and extremal coefficient formulas are specific to complete-graph subdivisions. Potential independent equivalent formulas in unindexed subdivision-convexity literature remain an originality risk. Reproducible finite checks are not exhaustive for infinite families.

## References

- M. C. Dourado, L. N. Grippo, M. C. Lin and F. Protti, *Counting \(P_3\)-convex sets in graphs*, arXiv:2603.04706v1 (first public March 5, 2026), https://arxiv.org/html/2603.04706v1.
- *Formulas and Upper Bounds for the Carathéodory Number of Hamming Graphs*, arXiv:2509.01645v1, https://arxiv.org/html/2509.01645v1 (related but distinct graph family and invariant).
