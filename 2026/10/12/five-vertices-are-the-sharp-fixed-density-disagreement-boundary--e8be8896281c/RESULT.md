# Five vertices are the sharp fixed-density disagreement boundary for degree centralization and degree Gini
## Finding
Consider connected finite simple undirected graphs with the same number of vertices
\[
n
\]
and the same number of edges
\[
m.
\]

Let Freeman degree centralization be
\[
C_F(G)
=
\frac{\sum_{v\in V(G)}\left(d_{\max}-d(v)\right)}
{(n-1)(n-2)},
\]
where
\[
d_{\max}=\max_{v\in V(G)}d(v).
\]

Let the degree Gini coefficient be
\[
G_d(G)
=
\frac{\sum_{i=1}^n\sum_{j=1}^n|d_i-d_j|}
{2n\sum_{i=1}^n d_i}.
\]

When order and size are fixed, these two standard summaries can rank network heterogeneity in opposite directions, but not before five vertices.

For every connected simple graph pair with
\[
n\le4
\]
and common
\[
m,
\]
opposite strict rankings are impossible.

At
\[
n=5,\qquad m=6,
\]
a strict reversal appears for the first time. Up to graph isomorphism the reversing pair is unique.

The first graph is the friendship graph consisting of two triangles sharing one vertex. Its degree multiset is
\[
(2,2,2,2,4).
\]

The second graph is obtained from
\[
K_4
\]
with one edge removed by attaching one leaf to one of the two degree-\(2\) vertices. Its degree multiset is
\[
(1,2,3,3,3).
\]

For the friendship graph,
\[
C_F=\frac23,
\qquad
G_d=\frac2{15}.
\]

For the second graph,
\[
C_F=\frac14,
\qquad
G_d=\frac16.
\]

Therefore
\[
\frac23>\frac14
\]
but
\[
\frac2{15}<\frac16.
\]

Freeman degree centralization calls the friendship graph more heterogeneous, while degree Gini calls the second graph more heterogeneous.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected.

Only graph pairs with equal order and equal size are compared. Fixing both quantities also fixes mean degree,
\[
\bar d=\frac{2m}{n},
\]
so the reversal is not caused by comparing networks at different density.

Freeman degree centralization uses the classical star-normalized denominator
\[
(n-1)(n-2).
\]

The Gini coefficient is applied directly to the degree sequence. It measures degree-distribution inequality and depends only on the multiset of vertex degrees, not on how vertices with those degrees are interconnected.

The theorem is a finite structural statement about these two graph-level summaries. It does not claim that either measure is preferable for every empirical social-network question.

## Proof
For a graph with order
\[
n
\]
and size
\[
m,
\]
the sum of the degrees is
\[
\sum_i d_i=2m.
\]

Hence Freeman degree centralization simplifies to
\[
C_F
=
\frac{n d_{\max}-2m}
{(n-1)(n-2)}.
\]

At fixed
\[
n
\]
and
\[
m,
\]
its ranking therefore depends only on
\[
d_{\max}.
\]

For degree Gini,
\[
G_d
=
\frac{\sum_i\sum_j|d_i-d_j|}
{2n\sum_i d_i}
=
\frac{\sum_{i<j}|d_i-d_j|}
{2nm}.
\]

At fixed
\[
n
\]
and
\[
m,
\]
its ranking depends on the complete pairwise degree spread
\[
L(d)=\sum_{i<j}|d_i-d_j|.
\]

Thus a reversal requires one degree sequence to have a larger maximum degree but a smaller value of
\[
L(d).
\]

A complete connected-graph census through five vertices gives connected unlabeled counts
\[
1,\ 2,\ 6,\ 21
\]
for orders
\[
2,\ 3,\ 4,\ 5.
\]

For every common-size pair through four vertices, maximum degree and pairwise degree spread never move in opposite strict directions.

At
\[
n=5,\qquad m=6,
\]
the realizable connected degree multisets are exactly
\[
(1,2,2,3,4),
\]
\[
(1,2,3,3,3),
\]
\[
(2,2,2,2,4),
\]
and
\[
(2,2,2,3,3).
\]

Their relevant statistics show a single reversal. For
\[
A=(2,2,2,2,4),
\]
\[
d_{\max}(A)=4,
\qquad
L(A)=8.
\]

For
\[
B=(1,2,3,3,3),
\]
\[
d_{\max}(B)=3,
\qquad
L(B)=10.
\]

Therefore
\[
d_{\max}(A)>d_{\max}(B)
\]
while
\[
L(A)<L(B).
\]

Substituting into the normalized indices gives
\[
C_F(A)
=
\frac{5\cdot4-12}{12}
=
\frac23,
\]
\[
C_F(B)
=
\frac{5\cdot3-12}{12}
=
\frac14,
\]
and
\[
G_d(A)
=
\frac8{60}
=
\frac2{15},
\]
\[
G_d(B)
=
\frac{10}{60}
=
\frac16.
\]

The exhaustive census also verifies that each of these two degree multisets has exactly one connected unlabeled realization at this order and size. Hence the first reversing graph pair is unique up to isomorphism.

## Verification
The embedded `verify_freeman_gini_boundary.py` uses only the Python standard library and exact integer arithmetic.

It enumerates every labeled simple graph through five vertices, filters for connectivity, canonically quotients by all vertex relabelings, and reproduces the connected unlabeled counts
\[
1,\ 2,\ 6,\ 21.
\]

It checks every pair of connected graph isomorphism classes with common order and common size and finds exactly one reversal through five vertices.

That reversal occurs at
\[
n=5,\qquad m=6
\]
between degree multisets
\[
(2,2,2,2,4)
\]
and
\[
(1,2,3,3,3).
\]

It also verifies that each degree multiset has exactly one connected unlabeled realization at the sharp layer.

Run:

`python3 verify_freeman_gini_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Freeman introduced graph centralization as a normalized comparison between the most central vertex and all other vertices. For degree centrality this yields the familiar star-normalized network centralization used here.

Hu and Wang introduced the Gini coefficient into complex-network analysis as a measure of structural heterogeneity.

Badham directly compares Freeman centralization with the Gini coefficient as shape measures for degree distributions. The paper emphasizes two points that motivate the present fixed-density question: the feasible range of Freeman centralization depends on mean degree, and the measure is driven by the highest degree relative to the average, whereas degree Gini responds to the full degree distribution.

The accepted result controls both of those confounds by fixing order and size. It then identifies the exact first connected simple graphs on which the two measures make opposite strict judgments, together with uniqueness of the first isomorphism-class pair.

Targeted searches using both metric names, fixed mean degree, fixed edge count, ranking reversal, exact degree multisets, the five-vertex boundary, and the friendship-graph witness did not locate this finite sharp boundary.

## Limitations
The theorem fixes both graph order and edge count. If either is allowed to vary, disagreement can occur for different reasons and the sharp boundary is a different problem.

Both indices depend only on the degree multiset in this comparison. They cannot distinguish nonisomorphic graphs sharing the same degree sequence.

The result is about Freeman degree centralization, not Freeman centralization based on betweenness, closeness, eigenvector scores, or another vertex centrality.

The complete lower-bound argument is a finite exhaustive census through five vertices. It does not claim a classification of every larger reversing pair.

An unindexed exercise, software test, or specialist note could contain the same small witness even though the fixed-density sharp boundary was not located in the checked literature.

## References
1. L. C. Freeman, “Centrality in social networks conceptual clarification,” *Social Networks* 1(3), 215–239, 1978. DOI: 10.1016/0378-8733(78)90021-7.
2. H.-B. Hu and L. Wang, “The Gini Coefficient's Application to General Complex Networks,” *Advances in Complex Systems* 8(1), 159–167, 2005. DOI: 10.1142/S0219525905000385.
3. J. Badham, “Commentary: Measuring the Shape of Degree Distributions,” *Network Science* 1(2), 213–225, published online 28 August 2013. DOI: 10.1017/nws.2013.10.
