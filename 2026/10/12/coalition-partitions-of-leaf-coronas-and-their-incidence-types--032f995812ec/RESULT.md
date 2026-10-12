# Coalition partitions of leaf coronas and their incidence types
## Finding
Let \(G\) be any finite simple graph of order \(n\ge2\), not necessarily connected. Attach to each core vertex \(v_i\) a private pendant leaf \(u_i\), producing the leaf corona
\[
X=G\circ K_1.
\]
Then the ordinary coalition number satisfies
\[
C(X)=4.
\]
Every maximum coalition partition has four blocks, and the incidence support of its private core-leaf pairs is isomorphic to precisely one of
\[
2K_2,\qquad P_4,\qquad C_4.
\]
The three types occur respectively when \(n\ge2\), \(n\ge3\), and \(n\ge4\), because each support edge needs at least one private pair. The number of distinct **unordered** maximum coalition partitions is
\[
N_n=2^{n-3}(4^n-5\cdot2^n+6).
\]
The formula depends only on the core order \(n\), not on any edge of \(G\).

## Assumptions and scope
A set \(D\subseteq V(X)\) dominates \(X\) when every vertex belongs to \(D\) or has a neighbor in \(D\). Two distinct non-dominating, disjoint sets form a coalition if their union dominates. A coalition partition is a partition of the vertex set into nonempty blocks such that every block either is a **singleton** dominating set or has a coalition partner among the other blocks. The coalition number \(C(X)\) is the maximum number of blocks in such a partition.

The theorem concerns **ordinary**, not connected, coalitions. The core \(G\) can have isolated vertices and disconnected components. The case \(n=1\) is not included: its corona is \(K_2\) and the singleton-dominating-block exception applies.

Given a partition \(\mathcal P=\{B_1,\ldots,B_k\}\), form a multigraph \(H(\mathcal P)\) on its \(k\) block-vertices, with one edge labeled \(i\) connecting the block containing \(v_i\) to the block containing \(u_i\). A loop occurs when a core vertex and its leaf lie in the same block; parallel edges are permitted. Its **support** is the underlying simple graph, with loops retained when present. The support type theorem concerns the four-block maximum partitions and is unaffected by edge multiplicities.

## Proof
### The private-pair lemma
For every set \(D\subseteq V(X)\),
\[
D\text{ dominates }X
\quad\Longleftrightarrow\quad
D\cap\{v_i,u_i\}\ne\varnothing\quad(1\le i\le n).
\tag{1}
\]
Indeed, the leaf \(u_i\) has the unique neighbor \(v_i\), so domination requires at least one endpoint of each private pair. Conversely, meeting every private pair dominates its leaf and its core vertex, independently of the original core edges.

A union of partition blocks therefore dominates exactly when the corresponding block-vertices are a vertex cover of the incidence multigraph \(H(\mathcal P)\): every incidence edge, including a loop, has a chosen endpoint. Moreover, when \(n\ge2\), no vertex of \(X\) is universal. Every leaf has degree one and every core vertex misses the other \(n-1\) pendant leaves. Hence there are no singleton dominating blocks. Thus \(\mathcal P\) is a coalition partition precisely when its incidence multigraph has **no one-vertex cover** and **every vertex belongs to a two-vertex cover**. It also has no isolated vertex, because the partition blocks are nonempty.

### At most four blocks
Suppose the incidence multigraph has \(k\ge5\) vertices and has the above properties. Choose any two-vertex cover \(\{a,b\}\), which exists because every vertex belongs to one. Put
\[
R=V(H)\setminus\{a,b\},\qquad |R|\ge3.
\]
Because \(\{a,b\}\) covers every edge, no edge joins two vertices of \(R\) and no loop occurs at a vertex of \(R\). Every \(r\in R\) has a neighbor in \(\{a,b\}\), since the incidence multigraph has no isolated vertex.

By pigeonhole, one of \(a,b\), say \(a\), has at least two **distinct** neighbors in \(R\). No pair consisting of two vertices of \(R\) covers the graph: a third vertex of \(R\) has an edge to \(a\) or \(b\), disjoint from that pair. Nor can \(\{b,r\}\) cover the graph for any \(r\in R\), since another neighbor \(s\ne r\) of \(a\) makes the edge \(as\) uncovered. Therefore, for each \(r\in R\), its required two-vertex cover is \(\{a,r\}\).

An edge not incident to \(a\) would need to contain **each** \(r\in R\), since every \(\{a,r\}\) covers it. An edge has only two endpoints, however, while \(|R|\ge3\). Hence every edge is incident to \(a\), making \(\{a\}\) a one-vertex cover, a contradiction. Consequently
\[
k\le4.
\tag{2}
\]

### Classification of four-block supports
Suppose now that \(k=4\), choose a two-vertex cover \(\{a,b\}\), and denote the remaining vertices by \(c,d\). Then \(cd\) and loops at \(c,d\) are absent. A loop at \(a\) would force every two-vertex cover to contain \(a\). As both \(c\) and \(d\) belong to some two-vertex cover, \(\{a,c\}\) and \(\{a,d\}\) must both be covers. Any edge not touching \(a\) would then have to be \(cd\), which is absent. Hence \(a\) would be a one-vertex cover, impossible. Similarly \(b\) cannot carry a loop. The incidence support is therefore loopless and every edge belongs to
\[
\{ab,ac,ad,bc,bd\}.
\tag{3}
\]

If \(ab\) is absent, the support is a spanning subgraph of \(K_{2,2}\), has no isolated vertices, and its two-side bipartition has two vertices on each side. With exactly two, three, or four distinct edges, respectively, it is \(2K_2\), \(P_4\), or \(C_4\).

If \(ab\) is present, neither \(c\) nor \(d\) can be adjacent to **both** \(a\) and \(b\). For example, edges \(ab,ac,bc\) would leave \(d\) unable to participate in any two-vertex cover: \(\{a,d\}\) misses \(bc\), \(\{b,d\}\) misses \(ac\), and \(\{c,d\}\) misses \(ab\). Each of \(c,d\) must nevertheless have a neighbor, so each attaches to exactly one of \(a,b\). They cannot both attach to the same vertex, because that vertex would meet every edge. Thus they attach to different ends, giving \(P_4\).

Conversely, each of \(2K_2\), \(P_4\), and \(C_4\) has no one-vertex cover and every vertex lies in a two-vertex cover. Any multigraph with that simple support and no loops has the same vertex covers. Thus these and only these are the four-block incidence types.

### Existence of four blocks
For \(n\ge2\), partition the \(n\) labeled private pairs into two nonempty groups. Put the two endpoints of every pair in the first group into blocks \(B_1,B_2\), one endpoint per block, and similarly put endpoints of every pair in the second group into blocks \(B_3,B_4\). Then all four blocks are nonempty, none meets every private pair, and either endpoint-block from the first group coalesces with either endpoint-block from the second group to dominate every private pair. Hence these four blocks form a coalition partition. Together with (2), this proves \(C(X)=4\).

### Enumeration of all maximum partitions
For \(m\ge1\), let
\[
s_m(n)=\sum_{j=0}^{m}(-1)^j\binom mj(m-j)^n,
\tag{4}
\]
the number of surjections from the \(n\) labeled private pairs to an \(m\)-element set. For a **fixed abstract simple support** \(H\) with \(m\) edges, a four-block partition with support isomorphic to \(H\) is constructed by assigning every private pair surjectively to an edge of \(H\), then choosing which endpoint of that graph edge receives the core vertex (two choices per private pair). There are \(2^n s_m(n)\) assignments with oriented pairs.

The block labels are artificial; quotienting by the automorphism group of \(H\) removes their redundancy. This action on surjective assignments is free, because every edge of \(H\) is used and every endpoint of every edge occurs in a partition block: an automorphism preserving all endpoint assignments must fix every vertex. The three support types have automorphism-group orders
\[
|\operatorname{Aut}(2K_2)|=8,\quad
|\operatorname{Aut}(P_4)|=2,\quad
|\operatorname{Aut}(C_4)|=8.
\]
Therefore the exact number of distinct **unordered** maximum coalition partitions is
\[
\begin{aligned}
N_n&=2^n\left(\frac{s_2(n)}8+\frac{s_3(n)}2+\frac{s_4(n)}8\right)\\
&=2^{n-3}\left(4^n-5\cdot2^n+6\right).
\end{aligned}
\tag{5}
\]
For \(n=2,3,4,5\), the counts are respectively \(1,30,364,3480\). This classification and count are independent of the edges of \(G\).

## Verification
The included `verify.py` uses only the Python standard library. It enumerates **all** set partitions of the labeled \(2n\) vertices, represented as restricted-growth strings, for \(n=2,3,4,5\). For each partition it tests the coalition predicate directly through the private-pair lemma, tracks the largest number of blocks, compares the full four-block count with (5), and canonically identifies the incidence support. It examines
\[
15+203+4140+115975=120333
\]
set partitions in total.

It also constructs empty, complete, and path base graphs at each of these four orders, and compares the private-pair dominance test against an independent adjacency-based graph-domination test on all relevant block unions. Finally it validates an explicit four-block construction for every \(2\le n\le50\).

All tested instances agree with the theorem. The infinite result comes from the cover argument, not from finite enumeration.

## Relationship to prior work
The initiating article on ordinary coalition partitions defines exactly the disjoint, non-dominating partnership and coalition-partition predicates used here. It establishes general bounds and studies paths, cycles, and small values, but does not give an exact leaf-corona coalition partition count. Later work on ordinary coalition numbers of trees studies large values and the shape of extremal trees, not the universal leaf-corona classification.

A distinct line studies **connected coalitions**, where the union of two blocks must induce a connected dominating set. For every connected graph \(G\), the known connected coalition number of \(G\circ K_1\) is \(2\). This does **not** determine ordinary coalition number, because an ordinary coalition need not be connected. The present theorem establishes an exact value of \(4\), even for disconnected bases, and a complete three-type classification with an exponential closed count of all optimum partitions. It exhibits a robust, operation-induced two-unit gap between the ordinary and connected variants for every connected base of order at least two.

Searches of the same-invariant foundational and tree papers, indexed results under corona/leaf/private-pair aliases, and comparison against connected-corona results found no stronger theorem implying both the four-block bound and the full enumeration. Distinctly named or unindexed sources remain a risk.

## Limitations
The theorem requires at least two core vertices and exactly **one** private leaf per vertex. It does not address coronas with larger attached graphs or a mixture of different numbers of private leaves.

The result concerns **ordinary** coalitions, and its enumeration counts unordered partitions of a fixed labeled corona graph, not isomorphism classes of partitions under automorphisms of the core graph.

Finite computations check instances only; the unbounded conclusions rest on the cover argument and exact surjection count. Literature indexing may miss a differently phrased result.

## References
1. T. W. Haynes, J. T. Hedetniemi, S. T. Hedetniemi, A. A. McRae, and R. Mohan, “Introduction to coalitions in graphs,” *AKCE International Journal of Graphs and Combinatorics* 17(2) (2020), 653–659, DOI: 10.1080/09728600.2020.1832874; published online 26 October 2020.
2. D. Bakhshesh, M. A. Henning, and D. Pradhan, “On the coalition number of trees,” arXiv:2111.08945v1, first public version 17 November 2021.
3. S. Alikhani, D. Bakhshesh, H. Golmohammadi, and E. V. Konstantinova, “Connected coalitions in graphs,” arXiv:2302.05754v1 (2023); *Discussiones Mathematicae Graph Theory* 44 (2024), 1551–1566.
4. Y. Guan and F. Wang, “On the connected coalition number of graphs,” arXiv:2402.00590v1 (2024).
