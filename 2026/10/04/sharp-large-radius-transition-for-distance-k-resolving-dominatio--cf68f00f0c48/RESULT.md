# Sharp large-radius transition for distance-\(k\) resolving domination of balanced spiders
## Finding
For integers \(q\ge3\) and \(L\ge2\), let \(S_{q,L}\) be the balanced spider with \(q\) arms, each of length \(L\). For every integer \(k\ge\lceil L/2\rceil\), its distance-\(k\) resolving domination number satisfies \[\gamma_k^r(S_{q,L})=\begin{cases}q,&\lceil L/2\rceil\le k\le L,\\q-1,&k\ge L+1.\end{cases}\] Thus the least radius at which distance-\(k\) resolving domination collapses to the metric dimension \(q-1\) is exactly \(L+1\), strictly below the diameter \(2L\). Moreover, for \(k\ge L+1\), every minimum set consists of one noncentral vertex on each of exactly \(q-1\) arms, and if their depths from the center are \(d_1,\ldots,d_{q-1}\), it is distance-\(k\) dominating exactly when \(\min_i d_i\le k-L\). Consequently the number of minimum sets is \[q\left(L^{q-1}-(2L-k)^{q-1}\right)\quad(L+1\le k\le2L-1),\]and \(qL^{q-1}\) for \(k\ge2L\).

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. For integers \(q\ge3\) and \(L\ge2\), let \(S_{q,L}\) be the balanced spider with center \(c\) and arms
\[
c\,v_{i,1}v_{i,2}\cdots v_{i,L},\qquad 1\le i\le q.
\]
The depth of \(v_{i,d}\) is \(d\).

A set \(R\subseteq V(G)\) is resolving if every two vertices have distinct distance vectors to \(R\). It is distance-\(k\) dominating if every vertex of \(G\) is at distance at most \(k\) from \(R\). The distance-\(k\) resolving domination number \(\gamma_k^r(G)\) is the minimum cardinality of a set having both properties.

## Proof
We first record the metric-basis structure of \(S_{q,L}\). Any resolving set must meet at least \(q-1\) arms away from the center. Indeed, if two distinct arms contain no noncentral landmark, then their depth-one vertices have equal distance to every landmark. Conversely, choosing one noncentral vertex on each of \(q-1\) distinct arms resolves the spider: the distances to the selected arms identify both the arm and the depth. Hence
\[
\dim(S_{q,L})=q-1,
\]
and every metric basis has exactly one noncentral vertex on each of \(q-1\) arms.

Suppose
\[
\left\lceil\frac L2\right\rceil\le k\le L.
\]
No resolving set of size \(q-1\) can be distance-\(k\) dominating. Such a set omits one entire arm, and if the nearest selected landmark has depth \(d\ge1\), then the omitted leaf is at distance
\[
L+d\ge L+1>k.
\]
Therefore \(\gamma_k^r(S_{q,L})\ge q\).

For the matching upper bound, if \(k<L\), choose on every arm the vertex of depth
\[
d=L-k.
\]
Because \(L\le2k\), one has \(d\le k\). The selected vertex on an arm is within distance \(k\) of both the center and the leaf, and hence of the whole arm. The set meets every arm and is resolving, so it is distance-\(k\) resolving dominating. When \(k=L\), choosing \(v_{i,1}\) on every arm gives the same conclusion. Thus
\[
\gamma_k^r(S_{q,L})=q
\]
throughout this range.

Now let \(k\ge L+1\). Choose \(v_{i,1}\) on any \(q-1\) arms. This is a metric basis. Every vertex on a selected arm is within distance at most \(L-1\), the center is within distance \(1\), and the leaf on the omitted arm is at distance exactly \(L+1\). Hence the set is distance-\(k\) dominating, so
\[
\gamma_k^r(S_{q,L})=q-1.
\]

It remains to classify the minimum sets in this regime. Every minimum set is a metric basis, hence it has one selected vertex on each of \(q-1\) arms and omits one arm. Let the selected depths be \(d_1,\ldots,d_{q-1}\). Since \(k\ge L+1\), all vertices on the selected arms and the center are automatically within distance \(k\). The farthest vertex on the omitted arm is its leaf, whose distance to the basis is
\[
L+\min_i d_i.
\]
Therefore the basis is distance-\(k\) dominating if and only if
\[
\min_i d_i\le k-L.
\]

Choose the omitted arm in \(q\) ways. For \(L+1\le k\le2L-1\), there are \(L^{q-1}\) possible depth vectors and exactly \((2L-k)^{q-1}\) of them have every depth strictly larger than \(k-L\). Hence the number of minimum sets is
\[
q\left(L^{q-1}-(2L-k)^{q-1}\right).
\]
For \(k\ge2L\), every metric basis is distance-\(k\) dominating, so the count is
\[
qL^{q-1}.
\]

## Verification
The included checker constructs balanced spiders directly, computes all-pairs distances, and tests both resolvability and distance-\(k\) domination from their definitions.

For \(3\le q\le5\) and \(2\le L\le5\), it verifies every theorem value in the stated range, enumerates all resolving sets of size \(q-1\), checks the one-vertex-per-\(q-1\)-arms metric-basis structure, and confirms the exact minimum-set count and depth threshold for every \(k\ge L+1\) tested.

## Relationship to prior work
The 2021 general distance-\(k\) resolving-domination paper establishes
\[
\max\{\gamma_k(G),\dim(G)\}\le\gamma_k^r(G)
\]
and proves the general stabilization statement \(\gamma_k^r(G)=\dim(G)\) whenever \(k\) is at least the graph diameter. It gives exact formulas for paths and cycles but does not treat spiders or subdivided stars in the inspected full text.

An earlier 2021 paper on the distance-\(2\) case gives exact values for paths, stars, complete graphs, and friendship graphs and explicitly leaves distance-\(k\) values for further graph families as an open direction. Its inspected full text contains no spider or subdivided-star treatment.

The theorem above sharpens the general diameter guarantee on balanced spiders: their diameter is \(2L\), but equality with metric dimension begins already at \(L+1\). It also determines the entire minimum-set family after stabilization.

## Limitations
The theorem covers the large-radius regime \(k\ge\lceil L/2\rceil\). Smaller \(k\) require additional landmarks along each arm and are not claimed here. The spider is balanced; unequal arm lengths are not covered. The exhaustive computation is corroborative only and is not used as a proof for arbitrary parameters.

## References
1. D. A. Retnowardani, M. I. Utoyo, Dafik, L. Susilowati, K. Dliou, “A study of a combination of distance domination and resolvability in graphs,” arXiv:2111.09095v1, 17 November 2021.
2. D. A. R. Wardani, M. I. Utoyo, Dafik, K. Dliou, “The distance 2-resolving domination number of graphs,” Journal of Physics: Conference Series 1836 (2021), 012017, DOI 10.1088/1742-6596/1836/1/012017.
