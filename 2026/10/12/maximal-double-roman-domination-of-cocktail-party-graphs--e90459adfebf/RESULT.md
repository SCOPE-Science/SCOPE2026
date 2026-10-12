# Maximal double Roman domination of cocktail party graphs
## Finding
For every integer
\[
n\ge2,
\]
let
\[
CP_n=K_{2,2,\ldots,2}
\]
be the cocktail party graph on \(2n\) vertices. Equivalently, \(CP_n\) is obtained from \(K_{2n}\) by deleting a perfect matching. Write the deleted matching pairs as
\[
P_i=\{x_i,y_i\},\qquad 1\le i\le n.
\]

Then
\[
\gamma_{dR}^{m}(CP_n)=2n+1.
\]

More strongly, every minimum maximal double Roman dominating function is obtained as follows. Choose one vertex \(z\). Assign
\[
f(z)=0.
\]
Its unique nonneighbor, namely the other vertex of the partner pair containing \(z\), has label \(1\). Choose any two vertices outside that partner pair and assign both label \(2\). Assign label \(1\) to every remaining vertex.

No minimum function uses label \(3\). Consequently the exact number of minimum functions is
\[
2n\binom{2n-2}{2}=2n(n-1)(2n-3).
\]

## Assumptions and scope
A double Roman dominating function on a graph \(G\) is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
such that every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\), and every vertex labeled \(1\) has a neighbor labeled \(2\) or \(3\).

It is maximal double Roman when its zero set
\[
V_0=\{v:f(v)=0\}
\]
is not a dominating set. The minimum weight of such a function is \(\gamma_{dR}^{m}(G)\).

The cocktail party graph \(CP_n\) has order \(2n\); every vertex is adjacent to all vertices except its unique partner. The theorem assumes \(n\ge2\), so the graph is nontrivial and connected.

## Proof
We first determine how large the zero set of a maximal double Roman function can be.

Every vertex of \(CP_n\) has exactly one nonneighbor. Therefore every vertex set of cardinality at least two is a dominating set: vertices inside the set dominate themselves, while a vertex outside the set can be nonadjacent to at most one selected vertex and hence is adjacent to another selected vertex. Thus, for every maximal double Roman dominating function,
\[
|V_0|\le1.
\tag{1}
\]

Suppose first that
\[
V_0=\varnothing.
\]
Every vertex then contributes at least \(1\), so the baseline weight is \(2n\). If the total weight were at most \(2n+1\), there could be at most one vertex labeled \(2\) and no vertex labeled \(3\). The partner of that unique label-\(2\) vertex would be labeled \(1\), but would not be adjacent to any vertex labeled \(2\) or \(3\), contradicting the double Roman condition. Hence every zero-free feasible function has weight at least
\[
2n+2.
\tag{2}
\]

Now suppose
\[
V_0=\{z\}.
\]
The other \(2n-1\) vertices contribute a baseline weight \(2n-1\). To defend \(z\), either one adjacent vertex must have label \(3\), contributing two units above the positive baseline, or two adjacent vertices must have label \(2\), again contributing two units above the baseline. Consequently
\[
\omega(f)\ge2n+1.
\tag{3}
\]

This lower bound is attained. Choose any vertex \(z\), choose any two vertices \(p,q\) outside the partner pair of \(z\), and set
\[
f(z)=0,\qquad f(p)=f(q)=2,
\]
with every other vertex labeled \(1\). The zero vertex is adjacent to both \(p\) and \(q\). Every label-\(1\) vertex is adjacent to at least one of \(p,q\): a vertex can fail to be adjacent to at most its unique partner, and both \(p,q\) cannot simultaneously be that partner. The singleton zero set is not dominating because it does not dominate the partner of \(z\). Therefore the function is maximal double Roman and has weight \(2n+1\). Combining this with (2)--(3) gives
\[
\gamma_{dR}^{m}(CP_n)=2n+1.
\]

It remains to classify equality. Let \(f\) have weight \(2n+1\). By (2), its zero set cannot be empty, and by (1) it must be
\[
V_0=\{z\}.
\]
Relative to the all-\(1\) labeling on the other \(2n-1\) vertices, exactly two excess weight units are available.

If these two units form one label \(3\), that label-\(3\) vertex must be adjacent to \(z\) in order to defend it. Hence its unique partner is a different vertex labeled \(1\). That partner is not adjacent to the only label \(3\), and there is no label \(2\), contradicting the condition on label-\(1\) vertices.

Therefore equality uses exactly two vertices labeled \(2\). Both must be adjacent to \(z\), so neither may be the partner of \(z\). All remaining positive vertices have label \(1\). Conversely, the construction above shows that every such choice is feasible.

There are \(2n\) choices for \(z\), and after its partner is excluded there are
\[
\binom{2n-2}{2}
\]
choices for the unordered pair of label-\(2\) vertices. Thus the number of minimum functions is
\[
2n\binom{2n-2}{2}=2n(n-1)(2n-3).
\]

## Verification
The included checker constructs \(CP_n\) directly and tests the defining conditions without using the theorem.

For every labeling it verifies the double Roman conditions at labels \(0\) and \(1\), computes the closed-neighborhood domination of the zero set, and requires that zero set not to dominate the graph.

For
\[
2\le n\le5,
\]
it exhausts all \(4^{2n}\) labelings, computes the true minimum, and compares the entire minimum-function family with the theorem's singleton-zero/two-label-\(2\) classification.

## Relationship to prior work
The foundational paper on maximal double Roman domination introduces the invariant, proves complexity results, establishes general relations and bounds, treats trees, and gives exact values for paths and cycles. Its searchable full text contains no occurrence of “cocktail party” or “complete multipartite,” and its special-graphs section is explicitly devoted to paths, cycles, and trees.

The same paper proves general bounds in terms of maximal Roman domination, maximal domination, ordinary double Roman domination, and minimum degree. These inequalities do not determine the cocktail-party value or its equality functions.

A 2023 survey of double Roman domination summarizes the maximal variant with the same scope: complexity, general relations, trees, paths, and cycles. Targeted searches under the aliases “cocktail party graph,” “complete graph minus a perfect matching,” and “complete multipartite graph with all parts of size two” did not locate an exact maximal-double-Roman theorem for this family.

The classification proved here is stronger than a scalar evaluation: the maximality condition collapses every feasible optimum to a singleton zero set, and the unique-nonneighbor structure then determines exactly how two label-\(2\) defenders may be placed.

## Limitations
The theorem is restricted to cocktail party graphs, equivalently complete multipartite graphs with every part of size two. It does not give the maximal double Roman domination number of arbitrary complete multipartite graphs.

The exhaustive computation covers \(2\le n\le5\) and is corroborative only. The arbitrary-order theorem follows from the proof.

Targeted literature searches cannot exclude a differently phrased or non-indexed treatment of the same family.

## References
1. H. Abdollahzadeh Ahangar, M. Chellali, S. M. Sheikholeslami, J. C. Valenzuela-Tripodoro, “Maximal double Roman domination in graphs,” Applied Mathematics and Computation 414 (2022), 126662, DOI 10.1016/j.amc.2021.126662; repository record dated 1 February 2022.
2. D. Rupnik Poklukar, J. Žerovnik, “Double Roman Domination: A Survey,” Mathematics 11(2) (2023), 351, DOI 10.3390/math11020351; published 9 January 2023.
