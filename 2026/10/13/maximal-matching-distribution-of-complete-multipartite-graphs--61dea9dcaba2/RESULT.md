# Maximal-matching distribution of complete multipartite graphs

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite classes \(V_1,\ldots,V_r\), and
\[
N=\sum_{i=1}^r n_i.
\]
Define the maximal-matching enumerator
\[
\mathcal A_G(z)=\sum_{M\text{ maximal matching of }G} z^{|M|}.
\]

For a vector \(\mathbf a=(a_1,\ldots,a_r)\) of nonnegative integers, let \(P(\mathbf a)\) be the number of perfect matchings of \(K_{a_1,\ldots,a_r}\), with \(P(\mathbf 0)=1\). A finite coefficient formula is
\[
P(\mathbf a)=
\Bigl(\prod_i a_i!\Bigr)
\sum_{\substack{e_{ij}\ge0\ (i<j)\\
\sum_{j<i}e_{ji}+\sum_{j>i}e_{ij}=a_i\ \forall i}}
\prod_{i<j}\frac1{e_{ij}!}.
\]
Equivalently, if \(a_i>0\), one may compute it recursively by
\[
P(a_1,\ldots,a_r)
=
\sum_{j\ne i} a_j
P(a_1,\ldots,a_i-1,\ldots,a_j-1,\ldots,a_r),
\]
with impossible vectors assigned value zero.

Then
\[
\boxed{
\mathcal A_G(z)=
\mathbf 1_{2\mid N}P(n_1,\ldots,n_r)z^{N/2}
+
\sum_{i=1}^r
\sum_{\substack{1\le u\le n_i\\u\equiv N\pmod 2}}
\binom{n_i}{u}
P(n_1,\ldots,n_i-u,\ldots,n_r)
z^{(N-u)/2}.
}
\]

In particular,
\[
\boxed{
\operatorname{avm}(G)
=
\frac{\mathcal A_G'(1)}{\mathcal A_G(1)}.
}
\]

There is also an exact size-spectrum criterion. An integer \(m\) occurs as the size of a maximal matching if and only if either
\[
2m=N
\quad\text{and}\quad
\max_i n_i\le m,
\]
or, with \(u=N-2m\ge1\), there is an index \(i\) satisfying
\[
u\le n_i
\quad\text{and}\quad
\max\!\left\{n_i-u,\max_{j\ne i}n_j\right\}\le m.
\]

## Assumptions and scope

Graphs are finite, simple, and labeled for counting purposes. The part sizes are positive and \(r\ge2\), so \(G\) is connected. A matching is maximal by inclusion, not necessarily maximum. The quantity \(\operatorname{avm}(G)\) is the arithmetic mean of the sizes of all maximal matchings.

The formula counts each labeled maximal matching exactly once. It does not claim that the same distribution is determined by the ordinary matching polynomial for arbitrary graph classes.

## Proof

A matching \(M\) is maximal exactly when no edge has both endpoints unmatched. Equivalently, the set \(U\) of unmatched vertices is independent. In a complete multipartite graph, every independent set lies inside a single partite class. Therefore
\[
M\text{ is maximal}
\quad\Longleftrightarrow\quad
U\subseteq V_i\text{ for some }i,
\]
with the empty set allowed.

First consider \(U=\varnothing\). This is possible only when \(N\) is even, and the maximal matchings are exactly the perfect matchings of \(G\), contributing
\[
P(n_1,\ldots,n_r)z^{N/2}.
\]

Now suppose \(U\ne\varnothing\). Then \(U\) lies in a unique part \(V_i\). Put \(u=|U|\). Choosing \(U\) gives the factor
\[
\binom{n_i}{u}.
\]
The remaining \(N-u\) vertices must be perfectly matched, and their part sizes are
\[
(n_1,\ldots,n_i-u,\ldots,n_r).
\]
Thus they contribute
\[
P(n_1,\ldots,n_i-u,\ldots,n_r)
\]
matchings, each of size \((N-u)/2\). Necessarily \(u\equiv N\pmod2\). Summing over all \(i\) and all positive feasible \(u\) proves the displayed formula for \(\mathcal A_G(z)\).

For the formula for \(P(\mathbf a)\), record for each pair of distinct parts the number \(e_{ij}\) of matching edges between them. The row-sum equations force every vertex to be matched. For fixed edge-type counts, partitioning the labeled vertices of each part among their partner parts and then pairing them gives
\[
\frac{\prod_i a_i!}{\prod_{i<j}e_{ij}!}
\]
perfect matchings. Summing over all feasible edge-type arrays proves the finite formula. The recurrence follows by fixing one labeled vertex in a nonempty part and choosing the part and then the vertex of its partner.

A complete multipartite graph \(K_{a_1,\ldots,a_r}\) with even total order \(2m\) has a perfect matching exactly when
\[
\max_i a_i\le m.
\]
Necessity is immediate because every vertex in the largest part must be paired outside that part. Sufficiency follows greedily by repeatedly pairing vertices from two currently largest nonempty parts; the inequality is preserved until no vertices remain, or equivalently from Hall's theorem applied to the natural multipartite pairing condition.

Applying this criterion to the residual graph after leaving \(u=N-2m\) vertices unmatched in \(V_i\) gives exactly
\[
\max\!\left\{n_i-u,\max_{j\ne i}n_j\right\}\le m.
\]
The perfect case \(u=0\) gives the first branch of the size-spectrum criterion.

Finally, differentiating the enumerator gives
\[
\mathcal A_G'(1)=\sum_M |M|,
\qquad
\mathcal A_G(1)=|\mathcal M(G)|,
\]
so their quotient is \(\operatorname{avm}(G)\).

## Verification

The accompanying script `artifacts/verify.py` independently enumerates every matching in every nondecreasing complete-multipartite part profile of total order \(2\) through \(8\). It checks maximality directly from the graph: a matching is maximal precisely when no unused edge can be added. It then compares the resulting coefficient distribution with the formula above, using an independent recurrence for residual perfect matchings.

The replay covers \(58\) distinct part profiles, examines \(9543\) matchings, and identifies \(2448\) maximal matchings. Every coefficient agrees. It also checks the size-spectrum criterion and the average obtained as the first moment of the coefficient distribution.

The finite calculation is corroborative only. The all-orders statement is proved by the unmatched-independent-set argument.

## Relationship to prior work

Zhang's 2026 paper studies the same statistic \(\operatorname{avm}(G)\) and determines the minimum over connected bicyclic graphs. Its first public version is dated April 30, 2026, and lists primary MSC \(05C70\). The paper formulates the parameter through the counts of maximal matchings of each size, but its classes are bicyclic core families; the full text contains no occurrence of “multipartite”, “complete graph”, or “bipartite”.

Engbers and Erey introduced the extremal study of the average size of maximal matchings and treated trees, connected unicyclic graphs, and related bounded-diameter classes. The accessible bibliographic material does not state a complete-multipartite distribution theorem.

Chen and Lian study ordinary matching counts, matching energy, and matching roots for complete multipartite graphs. Those counts include nonmaximal matchings. Their theorems compare matching energy under balancing operations; they do not identify which matchings are maximal or give the maximal-matching size distribution. The theorem here uses the complete-multipartite structure to pass from maximality to a residual perfect-matching problem.

A nearby database result gives a sharp lower bound for \(\operatorname{avm}(G)\) in connected graphs of prescribed cyclomatic number. That statement is extremal over a very different class and does not determine the exact maximal-matching distribution of a specified complete multipartite graph.

## Limitations

The result is restricted to complete multipartite graphs. The perfect-matching term \(P(\mathbf a)\) is given by a finite sum or recurrence rather than a single product in general.

The originality assessment is based on targeted searches, direct inspection of the recent full-text source, and comparison with complete-multipartite ordinary matching literature. The 2023 Engbers--Erey article was not available in lawful full text during this run, so an unindexed special-family formula there remains a residual bibliographic risk; its accessible descriptions emphasize trees and unicyclic graphs rather than complete multipartite graphs.

## References

1. K. Zhang, “Extremal graphs for average size of maximal matchings in bicyclic graphs,” arXiv:2604.28033v1, first public April 30, 2026.
2. J. Engbers and A. Erey, “Extremal graphs for average sizes of maximal matchings,” Discrete Applied Mathematics 341 (2023), 308–321, DOI:10.1016/j.dam.2023.08.022.
3. X. Chen and H. Lian, “Extremal Matching Energy and the Largest Matching Root of Complete Multipartite Graphs,” Complexity (2019), Article 9728976, DOI:10.1155/2019/9728976.
