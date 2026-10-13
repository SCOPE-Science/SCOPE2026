# Average clustering and transitivity first reverse network rankings at five vertices
## Finding
Let \(G\) be a connected simple undirected graph.

For a vertex \(v\) of degree at least \(2\), write
\[
c(v)
=
\frac{\text{edges among neighbors of }v}{\binom{d(v)}2}.
\]
Following the convention used by Schank and Wagner, define the graph clustering coefficient by averaging over
\[
V'=\{v:d(v)\ge2\}:
\]
\[
C(G)=\frac1{|V'|}\sum_{v\in V'}c(v).
\]

Write
\[
\Delta(G)
\]
for the number of triangles and
\[
\tau(G)=\sum_v\binom{d(v)}2
\]
for the number of centered connected triples. Transitivity is
\[
T(G)=\frac{3\Delta(G)}{\tau(G)}.
\]

Among connected simple graphs of each fixed order
\[
n\le4,
\]
the two statistics never rank a pair of graphs in opposite strict orders.

The distinction between the statistics appears earlier than ranking reversal. At order \(4\), the possible \((T,C)\) pairs are
\[
(0,0),\quad
\left(\frac35,\frac79\right),\quad
\left(\frac34,\frac56\right),\quad
(1,1).
\]
Thus \(T\) and \(C\) can differ numerically while their graph ordering is still compatible.

Order
\[
n=5
\]
is the sharp first order for strict ranking reversal. Among the \(21\) connected unlabeled five-vertex graph types, exactly \(13\) unordered graph pairs satisfy
\[
(T(G)-T(H))(C(G)-C(H))<0.
\]

A particularly transparent witness uses two graphs with exactly the same order, edge count, and triangle count.

Graph \(A\) is a triangle with two leaves attached to the same triangle vertex. Its degree sequence is
\[
(4,2,2,1,1).
\]

Graph \(B\) is a triangle with one leaf attached to each of two distinct triangle vertices. Its degree sequence is
\[
(3,3,2,1,1).
\]

Both have five edges and one triangle, but
\[
T(A)=\frac38
<
\frac37
=
T(B),
\]
whereas
\[
C(A)=\frac{13}{18}
>
\frac59
=
C(B).
\]

Hence transitivity ranks \(B\) as more clustered, while average local clustering ranks \(A\) as more clustered.

The sharp order and this same witness are robust to the other common convention in which vertices of degree below \(2\) receive local clustering \(0\) and are included in the graph average. Under that convention,
\[
C_0(A)=\frac{13}{30}
>
\frac13
=
C_0(B),
\]
while the transitivity values are unchanged. Exhaustive enumeration still gives no strict reversal through order \(4\).

## Assumptions and scope
Graphs are finite, simple, undirected, and connected.

Rankings compare graphs of the same order. This is the natural finite-size question: at what smallest network size can two standard graph-level clustering summaries disagree about which of two networks is more clustered?

The main convention averages local clustering only over vertices of degree at least \(2\), matching Schank and Wagner's displayed definition. The alternative zero-for-low-degree convention is checked separately rather than silently conflated with it.

Only strict ranking reversal is counted. A numerical difference \(C(G)\ne T(G)\), or a tie under one statistic that is split by the other, is not by itself a strict reversal.

## Proof
Transitivity is a triple-weighted average of local clustering:
\[
T(G)
=
\frac{\sum_v \binom{d(v)}2 c(v)}
     {\sum_v \binom{d(v)}2}.
\]
By contrast, \(C(G)\) gives equal weight to every vertex in \(V'\).

This weighting difference is the only mechanism needed for reversal.

For orders \(2,3,4,5\), complete isomorphism reduction of connected simple graphs gives respectively
\[
1,\ 2,\ 6,\ 21
\]
unlabeled graph types.

At order \(4\), direct evaluation on the six types yields only
\[
(0,0),\quad
\left(\frac35,\frac79\right),\quad
\left(\frac34,\frac56\right),\quad
(1,1).
\]
These pairs are increasing in both coordinates, so no strict reversal is possible. The same conclusion is immediate at orders \(2\) and \(3\).

At order \(5\), complete pairwise comparison of the \(21\) types gives exactly \(13\) reversing unordered pairs.

For the displayed witness, graph \(A\) has one triangle and
\[
\tau(A)
=
\binom42+\binom22+\binom22
=
8.
\]
Therefore
\[
T(A)=\frac{3}{8}.
\]
Its three vertices of degree at least \(2\) have local clustering
\[
\frac16,\ 1,\ 1,
\]
so
\[
C(A)
=
\frac{\frac16+1+1}{3}
=
\frac{13}{18}.
\]

Graph \(B\) also has one triangle, but
\[
\tau(B)
=
\binom32+\binom32+\binom22
=
7,
\]
hence
\[
T(B)=\frac37.
\]
Its three vertices of degree at least \(2\) have local clustering
\[
\frac13,\ \frac13,\ 1,
\]
so
\[
C(B)
=
\frac{\frac13+\frac13+1}{3}
=
\frac59.
\]

Thus
\[
T(A)<T(B)
\quad\text{and}\quad
C(A)>C(B).
\]

## Verification
The embedded `verify_clustering_transitivity_minimal_reversal.py` uses only the Python standard library and exact rational arithmetic.

For each order through \(5\), it:
- enumerates every labeled simple graph;
- discards disconnected graphs;
- canonically quotients the survivors under every vertex permutation;
- reproduces the connected-unlabeled counts \(1,2,6,21\);
- computes triangles, centered triples, local clustering, average clustering, and transitivity from the definitions;
- compares every unordered pair of isomorphism types.

Under the degree-at-least-\(2\) averaging convention, the exact strict-reversal counts at orders \(2,3,4,5\) are
\[
0,\ 0,\ 0,\ 13.
\]

Under the convention assigning low-degree vertices local clustering \(0\), the counts are
\[
0,\ 0,\ 0,\ 12.
\]

The verifier independently checks the hand counts for the displayed five-vertex witness.

Run:

`python3 verify_clustering_transitivity_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Watts and Strogatz introduced the local clustering coefficient in their study of small-world networks, including social networks.

Schank and Wagner give a direct comparison of average clustering and transitivity. They define the average local coefficient and transitivity exactly in the conventions used here, observe that transitivity is the connected-triple-weighted average of local clustering, and explicitly note that the two values differ in general. They also identify the complete graph on four vertices with one edge deleted as the smallest graph on which the two statistics are numerically unequal.

That prior result settles the first pointwise inequality of the statistics, not the first reversal of their ordering of two networks. The present finite boundary separates those questions: values first differ at four vertices, but opposite strict network rankings first become possible at five.

Targeted searches using “average clustering coefficient,” “transitivity,” “global clustering,” “ranking reversal,” “ordering,” and “smallest graph” did not locate the five-vertex ranking threshold or the matched one-triangle witness.

## Limitations
The exact boundary is for connected simple undirected graphs compared at fixed order.

Weighted, directed, temporal, bipartite, and multilayer clustering definitions can behave differently.

The number of five-vertex reversing pairs depends on the convention for vertices of degree below \(2\), although the sharp order and displayed witness do not.

The result is a finite structural benchmark, not a statement that one clustering summary is universally preferable.

A specialized exercise, software test, or unindexed note could contain the same ranking witness even though the sharp order theorem was not located.

## References
1. D. J. Watts and S. H. Strogatz, “Collective dynamics of ‘small-world’ networks,” *Nature* 393, 440–442, published 4 June 1998. DOI: 10.1038/30918.
2. T. Schank and D. Wagner, “Approximating Clustering Coefficient and Transitivity,” *Journal of Graph Algorithms and Applications* 9(2), 265–275, 2005. DOI: 10.7155/jgaa.00108.
