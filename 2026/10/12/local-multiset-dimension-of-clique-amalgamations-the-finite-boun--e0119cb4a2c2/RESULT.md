# Local multiset dimension of clique amalgamations: the finite boundary
## Finding
For integers \(r\ge2\) and \(t\ge2\), let
\[
A_{r,t}=\operatorname{Amal}(K_t,v,r)
\]
be formed from \(r\) copies of \(K_t\) by identifying one vertex from every copy to a common center \(c\). Then
\[
\operatorname{lmd}(A_{r,t})=
\begin{cases}
1,&t=2,\\
r,&t=3,\\
\infty,&t\ge4.
\end{cases}
\]

For \(t=2\), the graph is a star and every singleton vertex is a local multiset basis. For \(t=3\), the graph is the friendship graph with \(r\) triangles, and every local multiset basis consists of exactly one noncentral vertex from each triangle. Hence there are exactly
\[
2^r
\]
minimum bases.

This gives the sharp clique-order boundary omitted by the published blanket assertion that complete-graph amalgamations have infinite local multiset dimension: the assertion is correct from \(t=4\) onward, but triangle amalgamations have finite dimension.

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. For a vertex set \(W\subseteq V(G)\), the multiset representation of \(x\in V(G)\) is the multiset
\[
r_m(x\mid W)=\{d(x,w):w\in W\},
\]
with multiplicity. A set \(W\) is local multiset resolving if
\[
r_m(x\mid W)\ne r_m(y\mid W)
\]
for every edge \(xy\). The minimum cardinality of such a set is the local multiset dimension; if no such set exists, the dimension is \(\infty\).

For \(A_{r,t}\), write
\[
B_1,\ldots,B_r
\]
for the disjoint sets of \(t-1\) noncentral vertices in the clique blades. Thus each \(B_i\cup\{c\}\) induces \(K_t\), and there are no edges between distinct \(B_i\).

## Proof
Let \(W\subseteq V(A_{r,t})\). Put
\[
s_i=|W\cap B_i|,
\qquad
S=\sum_{i=1}^r s_i,
\]
and let \(\delta=1\) if \(c\in W\), otherwise \(\delta=0\).

Fix a blade \(B_i\). If \(u\in B_i\cap W\), then its multiset representation contains one \(0\), exactly \(s_i-1+\delta\) copies of \(1\), and exactly \(S-s_i\) copies of \(2\). Therefore every two selected vertices in the same blade have identical representations.

If \(u\in B_i\setminus W\), its representation contains no \(0\), exactly \(s_i+\delta\) copies of \(1\), and exactly \(S-s_i\) copies of \(2\). Therefore every two unselected vertices in the same blade also have identical representations.

All vertices in one blade are pairwise adjacent. Hence a local multiset resolving set can contain at most one selected and at most one unselected vertex in each \(B_i\). Consequently
\[
|B_i|=t-1\le2.
\]
If \(t\ge4\), then \(|B_i|\ge3\), so by the pigeonhole principle two adjacent blade vertices have the same selection status and therefore the same multiset representation. No local multiset resolving set exists, and
\[
\operatorname{lmd}(A_{r,t})=\infty.
\]

Now let \(t=3\). Each blade is a two-vertex set
\[
B_i=\{a_i,b_i\}.
\]
The preceding argument forces every local multiset resolving set to select exactly one vertex from every \(B_i\). Thus
\[
|W|\ge r.
\]
Choose exactly one outer vertex from each triangle and omit the center. Then the center has representation
\[
\{1,\ldots,1\},
\]
with \(r\) copies of \(1\). A selected outer vertex has representation
\[
\{0,2,\ldots,2\},
\]
with one \(0\) and \(r-1\) copies of \(2\), while its unselected mate has representation
\[
\{1,2,\ldots,2\},
\]
with one \(1\) and \(r-1\) copies of \(2\). Since \(r\ge2\), these three multisets are distinct. Every edge lies in one triangle, so the set is local multiset resolving. Therefore
\[
\operatorname{lmd}(A_{r,3})=r.
\]
Equality forces one selected noncentral vertex in every triangle and no center, giving exactly \(2^r\) bases.

Finally, when \(t=2\), \(A_{r,2}\cong K_{1,r}\) is bipartite. The foundational local-multiset theorem gives dimension \(1\). Directly, any singleton distinguishes the endpoints of every star edge: choosing the center yields representations \(\{0\}\) and \(\{1\}\), while choosing a leaf yields \(\{0\}\), \(\{1\}\), or \(\{2\}\) according to the vertex. Hence every singleton is a basis.

## Verification
The included checker constructs the clique amalgamations directly, computes all-pairs shortest-path distances, forms the representation multiset for every vertex and every candidate landmark set, and tests all adjacent pairs.

It exhaustively checks fifteen parameter pairs: \(2\le r\le5\) for \(t=2,3,4\), and \(2\le r\le4\) for \(t=5\). It enumerates every vertex subset in each graph, verifies the complete minimum-basis families in the finite cases, and verifies nonexistence in every checked \(t\ge4\) case.

## Relationship to prior work
The local multiset dimension was introduced in 2019. Its foundational paper defines the invariant used here and proves that dimension one is equivalent to bipartiteness.

A 2023 paper on amalgamation graphs, revised in 2024, reports
\[
\operatorname{lmd}(\operatorname{Amal}(K_n,v,m))=\infty
\]
for complete-graph amalgamations. Under the published definitions, that assertion misses the triangle boundary: \(\operatorname{Amal}(K_3,v,r)\) is a friendship graph and has local multiset dimension \(r\) for every \(r\ge2\). The proof above also identifies why the infinite conclusion becomes valid at \(K_4\): a clique blade then has at least three noncentral vertices, forcing two adjacent vertices with identical selection status and identical multiset representations.

Later work on local and local-outer multiset dimension retains the same definition and assigns the topic MSC \(05C12\). Targeted searches under amalgamation, friendship, windmill, and complete-clique terminology did not locate a published correction or the basis classification above.

## Limitations
The theorem concerns one-vertex amalgamations of complete graphs with at least two copies. It does not address edge amalgamation, amalgamation over larger common subgraphs, or noncomplete blades.

The finite computation is corroborative only. The all-parameter trichotomy follows from the selection-status obstruction within each clique blade and the explicit friendship-graph construction.

A differently phrased or non-indexed correction may exist; no such correction was found in the inspected primary and later literature.

## References
1. R. Alfarisi, Dafik, A. I. Kristiana, I. H. Agustin, “The local multiset dimension of graphs,” International Journal of Engineering and Technology 8(3) (2019), DOI 10.14419/ijet.v8i3.11643. Published 25 August 2019.
2. R. Alfarisi, L. Susilowati, Dafik, S. Prabhu, “Local Multiset Dimension of Amalgamation Graphs,” F1000Research 12:95, version 1 published 24 January 2023, DOI 10.12688/f1000research.128866.1; revised version published 23 April 2024, DOI 10.12688/f1000research.128866.2.
3. R. Simanjuntak, M. A. Hasan, M. Anggarawan, “Local (Outer) Multiset Dimensions of Graphs,” arXiv:2507.15071v1, 20 July 2025.
