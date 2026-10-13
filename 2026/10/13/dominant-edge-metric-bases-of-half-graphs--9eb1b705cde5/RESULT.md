# Dominant edge metric bases of half graphs
## Finding
Let \(H_n\) be the half graph with \(n\ge2\), bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and adjacency rule
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Then
\[
\operatorname{Ddim}_e(H_n)=n.
\]

More strongly, the dominant edge metric bases are exactly
\[
C_t=
\{a_1,\ldots,a_t\}
\cup
\{b_{t+1},\ldots,b_n\},
\qquad 0\le t\le n.
\]
Hence every minimum vertex cover of \(H_n\) is edge-resolving, and \(H_n\) has exactly
\[
n+1
\]
dominant edge metric bases.

## Assumptions and scope
For a vertex \(v\) and edge \(e=xy\), write
\[
d(v,e)=\min\{d(v,x),d(v,y)\}.
\]
A set \(S\subseteq V(G)\) is an edge metric generator if distinct edges have distinct ordered vectors
\[
(d(s,e):s\in S).
\]
A dominant edge metric generator is an edge metric generator that is also a vertex cover. Its minimum cardinality is the dominant edge metric dimension
\[
\operatorname{Ddim}_e(G).
\]

## Proof
The edges
\[
a_i b_i,\qquad 1\le i\le n,
\]
form a matching. Every vertex cover therefore has size at least \(n\). Since either bipartition class itself is a vertex cover,
\[
\tau(H_n)=n.
\tag{1}
\]
Consequently every dominant edge metric generator has at least \(n\) vertices.

We first classify all vertex covers of size \(n\). Their complements are independent sets of size \(n\). Let \(I\) be such an independent set, and let
\[
t=\max\{j:b_j\in I\},
\]
with \(t=0\) when \(I\cap B=\varnothing\).

If \(b_t\in I\), independence forbids every \(a_i\) with \(i\le t\). Thus \(I\) contains at most \(t\) vertices from \(B\) and at most \(n-t\) vertices from \(A\). Since \(|I|=n\), equality must hold on both sides. Therefore
\[
I=\{b_1,\ldots,b_t\}\cup\{a_{t+1},\ldots,a_n\}.
\]
The endpoint \(t=0\) gives \(I=A\), and \(t=n\) gives \(I=B\). Hence the minimum vertex covers are exactly the sets \(C_t\) displayed above.

It remains to prove that every \(C_t\) edge-resolves \(H_n\). Write
\[
e_{ij}=a_i b_j,\qquad i\le j.
\]

If
\[
i\le t<j,
\]
then both endpoints of \(e_{ij}\) belong to \(C_t\). Its edge-distance vector therefore has zeros exactly in the coordinates corresponding to \(a_i\) and \(b_j\), so the edge is uniquely identified.

Suppose
\[
j\le t.
\]
Then only \(a_i\) is an endpoint of \(e_{ij}\) lying in \(C_t\). The zero coordinate identifies \(i\). For every selected \(a_k\),
\[
d(a_k,e_{ij})\le1
\quad\Longleftrightarrow\quad
k\le j.
\]
Indeed, for \(k\ne i\), the distance is \(1\) when \(a_kb_j\) is an edge and \(2\) otherwise. Thus the largest selected \(A\)-index having edge distance at most \(1\) is exactly \(j\). Hence \(j\) is recovered.

Finally suppose
\[
i>t.
\]
Then \(j>t\), and only \(b_j\) is an endpoint of \(e_{ij}\) lying in \(C_t\). The zero coordinate identifies \(j\). For every selected \(b_\ell\),
\[
d(b_\ell,e_{ij})\le1
\quad\Longleftrightarrow\quad
\ell\ge i.
\]
Thus the smallest selected \(B\)-index having edge distance at most \(1\) is exactly \(i\).

These three cases cover every edge and show that each \(C_t\) is an edge metric generator. By (1), each is a minimum dominant edge metric generator. Conversely, every minimum dominant edge metric generator has size \(n\), hence is a minimum vertex cover and therefore equals one \(C_t\). This proves the theorem.

## Verification
The included checker constructs \(H_n\) for
\[
2\le n\le9,
\]
computes all-pairs shortest-path distances, and tests the dominant edge metric definition directly.

It exhausts every subset of size \(n-1\) and \(n\). The size-\(n-1\) sets all fail the vertex-cover condition. Among size-\(n\) sets, the checker independently enumerates the minimum vertex covers and verifies that every one edge-resolves the graph. The resulting complete basis family is compared with the \(n+1\) canonical cuts \(C_t\).

## Relationship to prior work
Dominant edge metric dimension was introduced in 2023 as the minimum size of a vertex cover that is simultaneously an edge metric generator. The introducing paper proves the general lower bound
\[
\max\{\tau(G),\operatorname{edim}(G)\}
\le
\operatorname{Ddim}_e(G)
\]
and gives exact values for complete graphs, complete bipartite graphs, paths, cycles, and wheels. Its searchable full text contains no half-graph or chain-graph occurrence.

For half graphs, ordinary edge metric dimension can be strictly smaller: a published edge-metric classification gives minimum edge-resolving sets of size \(n-1\). The theorem here identifies the exact effect of imposing the vertex-cover requirement: the value rises to \(n\), and the optimum sets become precisely all \(n+1\) minimum vertex covers.

The new content is therefore not a restatement of either the vertex-cover number or the ordinary edge metric dimension. It is the structural fact that every minimum vertex cover of the half graph already resolves all edges, together with the complete classification of dominant edge metric bases.

## Limitations
The theorem concerns canonical half graphs. It does not state a dominant edge metric formula for arbitrary chain graphs with repeated twin classes.

The finite exhaustive verification through \(n=9\) is corroborative only. The arbitrary-\(n\) statement follows from the matching lower bound, the maximum-independent-set classification, and the explicit edge-signature argument.

A differently phrased or non-indexed half-graph treatment may exist despite the targeted searches.

## References
1. M. Tavakoli, M. Korivand, A. Erfanian, G. Abrishami, E. T. Baskoro, “The dominant edge metric dimension of graphs,” Electronic Journal of Graph Theory and Applications 11(1) (2023), 197–208, DOI 10.5614/ejgta.2023.11.1.16.
