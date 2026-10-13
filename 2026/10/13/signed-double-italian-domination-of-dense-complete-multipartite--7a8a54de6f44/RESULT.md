# Signed double Italian domination of dense complete multipartite graphs
## Finding
Let
\[
G=K_{n_1,\ldots,n_r}
\]
be a complete multipartite graph with
\[
r\ge3
\qquad\text{and}\qquad
n_i\ge2
\]
for every part. Then
\[
\gamma_{sdI}(G)=
\begin{cases}
2,&\min_i n_i=2,\\
3,&\min_i n_i\ge3.
\end{cases}
\]

Thus, throughout this dense multipartite class, the signed double Italian domination number has only two possible values, with a sharp threshold exactly at the presence of a two-vertex part.

## Assumptions and scope
All graphs are finite, simple, and undirected. A signed double Italian dominating function is a function
\[
f:V(G)\longrightarrow\{-1,1,2,3\}
\]
such that:

1. for every vertex \(v\),
\[
\sum_{u\in N[v]}f(u)\ge1;
\]
2. if \(f(v)=-1\), some subset \(A\subseteq N(v)\) satisfies
\[
\sum_{u\in A}f(u)\ge3;
\]
3. if \(f(v)=1\), some subset \(A\subseteq N(v)\) satisfies
\[
\sum_{u\in A}f(u)\ge2.
\]

The weight is
\[
w(f)=\sum_{v\in V(G)}f(v),
\]
and \(\gamma_{sdI}(G)\) is the minimum possible weight.

The theorem assumes at least three partite classes and no singleton part. Complete bipartite graphs and complete multipartite graphs containing singleton parts are not included.

## Proof
Let the partite classes be \(V_1,\ldots,V_r\). Put
\[
s_i=\sum_{v\in V_i}f(v),
\qquad
W=w(f).
\]
For a vertex \(v\in V_i\),
\[
\sum_{u\in N[v]}f(u)=f(v)+W-s_i.
\tag{1}
\]

Because the defender set in conditions 2 and 3 may be chosen arbitrarily inside \(N(v)\), those conditions are equivalent to requiring positive-label weight at least \(3\), respectively \(2\), outside the part containing \(v\).

We first prove \(W\ge2\) whenever every part has at least two vertices. Suppose \(W\le1\). If some part \(V_i\) has \(s_i>0\) and contains a vertex labeled \(-1\), then (1) gives
\[
-1+W-s_i\ge1,
\]
hence
\[
s_i\le W-2<0,
\]
a contradiction.

So a positive-sum part contains only positive labels. If such a part contains a vertex labeled \(1\), then \(s_i\ge2\), while (1) gives \(s_i\le W\le1\). If its smallest label is \(2\), then \(s_i\ge4\), while (1) gives \(s_i\le W+1\le2\). If every label is \(3\), then \(s_i\ge6\), while (1) gives \(s_i\le W+2\le3\). Thus no part can have positive sum.

If \(W=1\), this contradicts \(W=\sum_i s_i\). If \(W\le0\), every part has nonpositive sum and therefore contains a vertex labeled \(-1\). Applying (1) to one such vertex in each part gives
\[
s_i\le W-2
\]
for every \(i\). Summing,
\[
W=\sum_i s_i\le r(W-2),
\]
which is impossible for \(W\le0\). Therefore
\[
W\ge2.
\tag{2}
\]

Now assume every \(n_i\ge3\). We rule out \(W=2\). Since the part sums total \(2\), some part has positive sum. Such a part cannot contain a vertex labeled \(-1\), because (1) would give \(s_i\le0\). Hence all of its labels are positive. If it contains a \(1\), then \(s_i\ge3\), while (1) gives \(s_i\le2\). If its smallest label is \(2\), then \(s_i\ge6\), while (1) gives \(s_i\le3\). If every label is \(3\), then \(s_i\ge9\), while (1) gives \(s_i\le4\). All cases are impossible, so
\[
W\ge3
\tag{3}
\]
when every part has size at least three.

It remains to attain the bounds.

Suppose first that some part \(V_1\) has size \(2\). Label both vertices of \(V_1\) by \(1\), so \(s_1=2\). Give every other part sum \(0\) as follows. If its size \(n\) is even, use \(n/2\) labels \(1\) and \(n/2\) labels \(-1\). If \(n\) is odd, use one label \(2\), \((n-3)/2\) labels \(1\), and \((n+1)/2\) labels \(-1\).

The total weight is \(2\). A vertex outside \(V_1\) sees ordinary outside-part sum \(2\), while a vertex of \(V_1\) sees ordinary outside-part sum \(0\). Hence all closed-neighborhood inequalities hold. Every zero-sum part has positive-label weight at least \(1\), and because \(r\ge3\), each vertex labeled \(-1\) sees the positive weight \(2\) of \(V_1\) plus positive weight from at least one additional part. Thus it has at least \(3\) positive weight in its neighborhood. Vertices labeled \(1\) have at least \(2\) positive weight outside their own part. This is an SDIDF of weight \(2\), proving equality in (2).

Finally suppose every \(n_i\ge3\). Choose three parts and give each part sum \(1\). For an odd part of size \(n\), use \((n+1)/2\) labels \(1\) and \((n-1)/2\) labels \(-1\). For an even part, use one label \(2\), \((n-2)/2\) labels \(1\), and \(n/2\) labels \(-1\). Give every remaining part sum \(0\): for even \(n\), split equally between \(1\) and \(-1\); for odd \(n\), use one \(2\), \((n-3)/2\) labels \(1\), and \((n+1)/2\) labels \(-1\).

The total weight is \(3\). A sum-\(1\) part sees outside-part sum \(2\), and a sum-\(0\) part sees outside-part sum \(3\), so all closed-neighborhood inequalities hold. Every part has positive-label weight at least \(2\), and there are at least three parts; hence every vertex sees at least \(4\) positive weight outside its own part. Conditions 2 and 3 follow. This attains (3).

## Verification
The included checker exhaustively scans every labeling by \(\{-1,1,2,3\}\) for every complete multipartite isomorphism type of orders \(6\) through \(9\) having at least three parts and all part sizes at least \(2\). It independently evaluates the three defining conditions and verifies the explicit constructions used above.

## Relationship to prior work
Signed double Italian domination was introduced in 2023. The defining paper proves complexity results, tree bounds and extremal tree characterizations, and exact values for cycles and the Petersen graph. Its searchable full text contains no complete-bipartite or complete-multipartite treatment.

A later survey of Roman-domination variants summarizes the known signed double Italian results as paths, stars, cycles, the Petersen graph, tree bounds, and complexity results. Targeted searches using complete multipartite, complete \(r\)-partite, complete bipartite, and Turán terminology did not locate the threshold above.

The theorem is not implied by signed Roman, total Roman, strong Roman, or other Roman-type formulas on complete multipartite graphs because signed double Italian domination uses a different label set and simultaneous closed-neighborhood and defender-subset constraints.

## Limitations
The theorem excludes complete bipartite graphs and multipartite graphs with singleton parts; those regimes have additional boundary behavior and are not claimed here.

The exhaustive computation is corroborative only. The all-parameter theorem follows from the part-sum lower bounds and explicit constructions.

A differently named or non-indexed treatment of this family could exist despite targeted searches.

## References
1. A. Almulhim, “Signed double Italian domination,” AIMS Mathematics 8(12) (2023), 30895–30909, DOI 10.3934/math.20231580. Published 17 November 2023.
2. A. Almulhim, B. Al Subaiei, S. R. Mondal, “Survey on Roman \(\{2\}\)-Domination,” Mathematics 12(17) (2024), 2771, DOI 10.3390/math12172771.
