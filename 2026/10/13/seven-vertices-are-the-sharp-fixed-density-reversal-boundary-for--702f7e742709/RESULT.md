# Seven vertices are the sharp fixed-density reversal boundary for path length and global efficiency
## Finding
For a connected finite simple undirected graph with
\[
n
\]
vertices, write \(d(i,j)\) for graph distance.

The characteristic path length is
\[
L(G)=\frac{1}{\binom{n}{2}}\sum_{i<j} d(i,j),
\]
so smaller values indicate shorter average communication routes.

The global efficiency is
\[
E(G)=\frac{1}{\binom{n}{2}}\sum_{i<j}\frac{1}{d(i,j)},
\]
so larger values indicate more efficient communication.

When two connected simple graphs have the same order \(n\) and the same number of edges \(m\), opposite strict rankings are impossible for every
\[
n\le6.
\]

Seven vertices are sharp. A reversal already occurs with
\[
n=m=7,
\]
and the two witness graphs even have the same degree multiset
\[
(1,1,2,2,2,3,3).
\]

Graph \(A\) has edge set
\[
\{04,12,13,14,25,26,56\}.
\]
Equivalently, begin with a triangle on vertices \(2,5,6\), attach vertex \(1\) to vertex \(2\), attach a leaf \(3\) to vertex \(1\), and attach the two-edge arm \(1-4-0\).

Its unordered pair-distance histogram is
\[
1^7,\ 2^6,\ 3^6,\ 4^2.
\]
Therefore
\[
L(A)=\frac{15}{7},
\qquad
E(A)=\frac{25}{42}.
\]

Graph \(B\) has edge set
\[
\{01,02,05,14,23,35,36\}.
\]
Equivalently, begin with the four-cycle \(0-2-3-5-0\), attach the two-edge arm \(0-1-4\), and attach leaf \(6\) to the opposite cycle vertex \(3\).

Its unordered pair-distance histogram is
\[
1^7,\ 2^7,\ 3^4,\ 4^2,\ 5.
\]
Therefore
\[
L(B)=\frac{46}{21},
\qquad
E(B)=\frac{188}{315}.
\]

Hence
\[
L(A)<L(B)
\]
by exactly
\[
\frac{1}{21},
\]
while simultaneously
\[
E(A)<E(B)
\]
by exactly
\[
\frac{1}{630}.
\]

Characteristic path length therefore ranks \(A\) as the better-connected network, whereas global efficiency ranks \(B\) as the better-connected network.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected.

Only graph pairs with the same order and the same number of edges are compared. This controls network density.

The seven-vertex witness pair also has the same degree multiset, so the reversal cannot be attributed to a change in degree distribution.

Characteristic path length is the arithmetic mean of all unordered-pair shortest-path distances. Global efficiency is the arithmetic mean of their reciprocals. For connected undirected graphs, these are equivalent to the usual ordered-pair normalizations because every unordered pair occurs twice in the ordered sum.

The result concerns strict ranking reversal. A tie under one measure can already be split by the other at six vertices; the theorem does not claim equality of the two weak orderings through six vertices.

## Proof
For any connected graph, let
\[
h_r(G)=\#\{\{i,j\}:i<j,\ d(i,j)=r\}.
\]
Then
\[
\sum_r h_r(G)=\binom{n}{2},
\]
and
\[
L(G)=\frac{\sum_r r h_r(G)}{\binom{n}{2}},
\qquad
E(G)=\frac{\sum_r h_r(G)/r}{\binom{n}{2}}.
\]

Thus a fixed-order comparison is an exact comparison of two linear functionals of the integer distance histogram, one weighting distance \(r\) by \(r\) and the other by \(1/r\).

For \(A\), the distance histogram is
\[
h_1=7,\quad h_2=6,\quad h_3=6,\quad h_4=2.
\]
Hence
\[
\sum_{i<j}d_A(i,j)
=7+12+18+8
=45,
\]
and
\[
\sum_{i<j}\frac1{d_A(i,j)}
=7+3+2+\frac12
=\frac{25}{2}.
\]
Dividing by
\[
\binom72=21
\]
gives
\[
L(A)=\frac{45}{21}=\frac{15}{7},
\qquad
E(A)=\frac{25}{42}.
\]

For \(B\), the distance histogram is
\[
h_1=7,\quad h_2=7,\quad h_3=4,\quad h_4=2,\quad h_5=1.
\]
Hence
\[
\sum_{i<j}d_B(i,j)
=7+14+12+8+5
=46,
\]
and
\[
\sum_{i<j}\frac1{d_B(i,j)}
=7+\frac72+\frac43+\frac12+\frac15
=\frac{188}{15}.
\]
Therefore
\[
L(B)=\frac{46}{21},
\qquad
E(B)=\frac{188}{315}.
\]
The differences are
\[
L(B)-L(A)=\frac1{21}
\]
and
\[
E(B)-E(A)=\frac1{630}.
\]
This proves the seven-vertex reversal.

For sharpness, the verifier enumerates every labeled simple graph on
\[
2\le n\le6,
\]
filters for connectivity, groups graphs by common \((n,m)\), computes every exact pair \((L,E)\), and checks every distinct metric pair for a strict reversal. The connected labeled graph counts recovered are
\[
1,\ 4,\ 38,\ 728,\ 26704
\]
for orders
\[
2,\ 3,\ 4,\ 5,\ 6,
\]
respectively. No strict reversal occurs in any fixed-size group.

## Verification
The embedded `verify_efficiency_path_boundary.py` uses only the Python standard library and exact rational arithmetic.

It independently enumerates all labeled simple graphs through six vertices, performs a breadth-first search from every vertex of every connected graph, and computes exact characteristic path length and global efficiency.

It verifies the connected labeled graph counts
\[
1,\ 4,\ 38,\ 728,\ 26704
\]
and confirms zero strict fixed-\((n,m)\) ranking reversals through six vertices.

It then reconstructs both seven-vertex witness graphs from their edge sets, checks the complete distance histograms, verifies the common degree multiset, and verifies
\[
L(A)=\frac{15}{7},\quad E(A)=\frac{25}{42},
\]
\[
L(B)=\frac{46}{21},\quad E(B)=\frac{188}{315},
\]
with exact gaps
\[
\frac1{21}
\]
and
\[
\frac1{630}.
\]

Run:

`python3 verify_efficiency_path_boundary.py`

The first output line must be `VERIFY_OK`.

The lower-bound census is exhaustive; the seven-vertex existence statement is proved by direct exact computation of all pairwise distances in the displayed graphs.

## Relationship to prior work
Watts and Strogatz use characteristic path length as the average shortest-path distance in their small-world framework. Their full article explicitly defines the network quantity \(L\) as the average number of edges in shortest paths between vertex pairs.

Latora and Marchiori introduce global efficiency as the average reciprocal shortest-path distance. They explicitly compare the two constructions, describing \(1/L\) as an approximation to global efficiency and noting that the two can differ substantially when pairwise distances are heterogeneous.

That general non-equivalence is established prior work. The present result does not claim otherwise. It isolates the first strict ordinal disagreement under two controls that are common in network comparison: the graphs have the same number of vertices and the same number of edges. The witness further has the same degree multiset, so only the shape of the distance distribution causes the reversal.

Targeted searches using the metric names, ranking-reversal language, fixed edge count, equal degree sequence, seven-vertex graphs, and the exact rational values did not locate this sharp boundary or the displayed witness.

## Limitations
The theorem treats connected unweighted simple graphs. Global efficiency is also defined for disconnected and weighted networks, where different sharp boundaries may occur.

The result is about strict rank reversal. At six vertices there are fixed-size graph pairs tied in characteristic path length but separated by global efficiency, so weak-order equivalence ends one order earlier.

The exhaustive lower bound covers every graph through six vertices, but the result does not classify all reversing pairs on seven or more vertices.

An unindexed worked example, teaching note, or software test could contain the same seven-vertex pair even though the sharp fixed-density boundary was not located in the checked literature.

## References
1. D. J. Watts and S. H. Strogatz, “Collective dynamics of ‘small-world’ networks,” *Nature* 393, 440–442, published 4 June 1998. DOI: 10.1038/30918.
2. V. Latora and M. Marchiori, “Efficient Behavior of Small-World Networks,” arXiv:cond-mat/0101396, first submitted 25 January 2001; later *Physical Review Letters* 87, 198701. DOI: 10.1103/PhysRevLett.87.198701.
