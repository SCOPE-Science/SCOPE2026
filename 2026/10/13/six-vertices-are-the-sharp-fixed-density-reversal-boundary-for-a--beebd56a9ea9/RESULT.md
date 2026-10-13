# Six vertices are the sharp fixed-density reversal boundary for algebraic and edge connectivity
## Finding
For a connected finite simple undirected graph \(G\), let
\[
a(G)=\lambda_2(L_G)
\]
be its algebraic connectivity, the second-smallest eigenvalue of the combinatorial Laplacian, and let
\[
e(G)
\]
be its edge connectivity, the minimum number of edges whose deletion disconnects the graph.

Compare graphs only when they have the same order
\[
n
\]
and the same size
\[
m.
\]

No pair with
\[
n\le5
\]
receives opposite strict rankings from \(a\) and \(e\).

Order
\[
n=6
\]
is sharp. A reversal already occurs with
\[
m=7.
\]

Let \(A\) have edge set
\[
\{04,13,14,23,24,34,45\}.
\]
Equivalently, \(A\) is the cone over
\[
P_3\cup2K_1.
\]
It contains two pendant edges, hence
\[
e(A)=1.
\]

Let \(B\) have edge set
\[
\{02,05,13,14,23,34,35\}.
\]
Equivalently, \(B\) is a triangle and a \(4\)-cycle sharing exactly one vertex. Every edge lies on a cycle, and deleting any one edge leaves the graph connected, so
\[
e(B)=2.
\]

Nevertheless,
\[
a(A)=1
\]
while
\[
a(B)=3-\sqrt5.
\]
Since
\[
1>3-\sqrt5,
\]
algebraic connectivity ranks \(A\) as more connected, whereas edge connectivity ranks \(B\) as more robust to link deletion.

Thus a bridge-containing network can have a strictly larger Fiedler value than a same-order, same-size network with no bridge.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected.

The comparison fixes both vertex count and edge count, so the reversal is not an artifact of giving one network more links.

Edge connectivity is the link-failure notion: it counts the fewest edges whose deletion disconnects the network.

Algebraic connectivity uses the ordinary combinatorial Laplacian
\[
L=D-A,
\]
not the normalized Laplacian.

The theorem concerns ordinal comparison between two robustness summaries. It does not say that algebraic connectivity is generally unsuitable for diffusion, consensus, partitioning, or spectral optimization.

## Proof
The Laplacian characteristic polynomial of \(A\) is
\[
\chi_A(x)
=
x(x-6)(x-4)(x-2)(x-1)^2.
\]
Hence the second-smallest Laplacian eigenvalue is
\[
a(A)=1.
\]

The two pendant edges of \(A\) are bridges, so
\[
e(A)=1.
\]

For \(B\),
\[
\chi_B(x)
=
x(x-3)^2(x-2)(x^2-6x+4).
\]
The smaller root of the quadratic factor is
\[
3-\sqrt5,
\]
and it is the smallest positive Laplacian eigenvalue. Therefore
\[
a(B)=3-\sqrt5.
\]

The graph \(B\) is the one-vertex union of a triangle and a \(4\)-cycle. Every edge belongs to a cycle, so there is no bridge. Deleting the two edges incident with any degree-\(2\) vertex disconnects that vertex, hence
\[
e(B)=2.
\]

Therefore
\[
a(A)=1>3-\sqrt5=a(B)
\]
but
\[
e(A)=1<2=e(B).
\]

For sharpness, every connected simple graph on at most five vertices was generated and quotient-reduced by all vertex relabelings. The connected unlabeled counts obtained were
\[
1,\ 2,\ 6,\ 21
\]
for orders
\[
2,\ 3,\ 4,\ 5.
\]

Within each common \((n,m)\) layer, every pair with different edge connectivity was compared using exact Laplacian characteristic polynomials and exact real algebraic roots. No opposite strict ordering occurs.

Hence six vertices are necessary and sufficient.

## Verification
The embedded `verify_algebraic_edge_connectivity_boundary.py` independently regenerates all connected simple graphs through five vertices from labeled edge subsets and quotients them by vertex permutations.

It checks edge connectivity by exhaustive cuts.

It computes Laplacian characteristic polynomials exactly and uses exact real algebraic roots, not floating-point eigenvalues.

The verifier reproduces connected-unlabeled graph counts
\[
1,\ 2,\ 6,\ 21,
\]
proves the absence of a same-\((n,m)\) reversal through five vertices, and checks the two six-vertex witness polynomials and connectivities.

Run:

`python3 verify_algebraic_edge_connectivity_boundary.py`

The first output line must be `VERIFY_OK`.

The verifier requires SymPy for exact algebraic-root arithmetic.

## Relationship to prior work
Fiedler introduced algebraic connectivity specifically to study its relation to the usual vertex and edge connectivities. His foundational paper proves structural inequalities connecting the Laplacian eigenvalue with combinatorial connectivity, but those inequalities do not imply that the corresponding graph rankings agree.

Later network-robustness work made the distinction operational. Feddema, Byrne, and Abdallah discuss algebraic connectivity together with node and edge connectivity as robustness measures and explicitly warn that increasing algebraic connectivity need not increase combinatorial robustness in the network families they study.

The present result isolates a sharper finite comparison: after fixing both the number of vertices and the number of links, it identifies the exact smallest network order at which algebraic connectivity can prefer a graph containing a bridge over a graph with no bridge.

Targeted searches using algebraic connectivity, Fiedler value, edge connectivity, link connectivity, robustness reversal, fixed edge count, bridge, and the exact witness descriptions did not locate this six-vertex sharp boundary.

## Limitations
The theorem is a finite sharp boundary, not a classification of all larger reversals.

The robustness notions measure different phenomena. Edge connectivity is a worst-case discrete link-deletion threshold, while algebraic connectivity is a global spectral quantity with important dynamical interpretations.

The most directly relevant network-robustness report by Feddema, Byrne, and Abdallah was available through a detailed official abstract and metadata page, but its full report could not be retrieved through the checked open route. No whole-document noncoverage claim is made for that report.

An unindexed small-graph example or software test could contain the same witness without identifying the fixed-density minimality result.

## References
1. M. Fiedler, “Algebraic connectivity of graphs,” *Czechoslovak Mathematical Journal* 23(2), 298–305, 1973. DOI: 10.21136/CMJ.1973.101168.
2. J. T. Feddema, R. H. Byrne, and C. T. Abdallah, “Algebraic connectivity and graph robustness,” Sandia National Laboratories report SAND2009-4494, published 1 July 2009. DOI: 10.2172/973665.
3. A. Jamakovic and P. Van Mieghem, “On the Robustness of Complex Networks by Using the Algebraic Connectivity,” *NETWORKING 2008*, LNCS 4982, 183–194, 2008. DOI: 10.1007/978-3-540-79549-0_16.
