# Minimum restrained double Roman functions of half graphs
## Finding
Let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Then
\[
\gamma_{rdR}(H_2)=6,
\qquad
\gamma_{rdR}(H_n)=8\quad(n\ge3).
\]

For \(n=2\), writing a function as
\[
(f(a_1),f(a_2);f(b_1),f(b_2)),
\]
the five minimum functions are
\[
(0,3;3,0),\quad
(1,1;2,2),\quad
(1,2;2,1),\quad
(2,1;1,2),\quad
(2,2;1,1).
\]

For \(n=3\), the nine minimum functions are
\[
(0,0,3;2,3,0),\quad
(0,1,3;2,2,0),\quad
(0,2,2;2,2,0),
\]
\[
(0,2,2;3,1,0),\quad
(0,3,1;2,0,2),\quad
(0,3,2;3,0,0),
\]
\[
(2,0,2;1,3,0),\quad
(2,1,1;1,1,2),\quad
(3,0,1;1,0,3).
\]

For every \(n\ge4\), the minimum function is unique:
\[
f(a_1)=f(b_n)=3,
\qquad
f(b_1)=f(a_n)=1,
\]
and every other vertex receives label \(0\).

Thus the optimizer multiplicity has a sharp stabilization:
\[
5,\ 9,\ 1,\ 1,\ldots
\]
for \(n=2,3,4,5,\ldots\).

## Assumptions and scope
A restrained double Roman dominating function is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
such that every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\), every vertex labeled \(1\) has a neighbor labeled \(2\) or \(3\), and the subgraph induced by the zero-labeled vertices has no isolated vertex.

The weight is
\[
\omega(f)=\sum_{v\in V(G)} f(v),
\]
and \(\gamma_{rdR}(G)\) is the minimum weight.

## Proof
Assume first that \(n\ge4\).

The vertex \(b_1\) is a leaf with sole neighbor \(a_1\). It cannot receive label \(0\): restrainedness would then force its only neighbor \(a_1\) also to be zero, but \(b_1\) would have no positive defender. Hence
\[
f(b_1)\ge1.
\]

Consider the four-vertex left block
\[
L=\{a_1,a_2,b_1,b_2\}.
\]
We claim that
\[
f(L)\ge4.
\tag{1}
\]

If \(f(b_1)=1\), then \(f(a_1)\ge2\). When \(f(a_1)=3\), inequality (1) is immediate. When \(f(a_1)=2\), the simultaneous assignment \(f(a_2)=f(b_2)=0\) is impossible because the zero vertex \(b_2\), whose neighborhood is \(\{a_1,a_2\}\), would see only one label \(2\). Thus at least one further unit is needed, and again \(f(L)\ge4\).

If \(f(b_1)=2\), then either \(f(b_2)\ge2\), already giving four units on \(b_1,b_2\), or \(f(b_2)\le1\). In the latter case, the double Roman condition at \(b_2\) when it is zero, or the support condition when it is one, forces at least two additional units on \(a_1,a_2\). Hence \(f(L)\ge4\).

If \(f(b_1)=3\), then \(f(L)\ge4\) follows because \(b_2\) cannot be a zero with both \(a_1,a_2\) zero, and if \(b_2=1\) then one of \(a_1,a_2\) must have label at least \(2\).

By symmetry, for the right block
\[
R=\{a_{n-1},a_n,b_{n-1},b_n\}
\]
we also have
\[
f(R)\ge4.
\tag{2}
\]

For \(n\ge4\), the blocks \(L\) and \(R\) are disjoint. Therefore
\[
\omega(f)\ge8.
\]

Now define \(f^\star\) by
\[
f^\star(a_1)=f^\star(b_n)=3,
\qquad
f^\star(b_1)=f^\star(a_n)=1,
\]
and assign \(0\) elsewhere. Every internal zero \(a_i\) with \(2\le i\le n-1\) is adjacent to \(b_n\), every internal zero \(b_j\) with \(2\le j\le n-1\) is adjacent to \(a_1\), and the zero-induced subgraph has no isolated vertex because \(a_i b_i\) is an edge for every internal index. The two label-\(1\) leaves are supported by the adjacent label-\(3\) vertices. Thus \(f^\star\) is feasible with weight \(8\), proving
\[
\gamma_{rdR}(H_n)=8
\quad(n\ge4).
\]

It remains to prove uniqueness at equality. Equality in (1) leaves exactly three possible left-block patterns, written as
\[
(f(a_1),f(a_2);f(b_1),f(b_2)):
\]
\[
(0,0;2,2),\qquad
(2,0;1,1),\qquad
(3,0;1,0).
\tag{3}
\]
The symmetric equality patterns on the right are
\[
(f(a_{n-1}),f(a_n);f(b_{n-1}),f(b_n)):
\]
\[
(2,2;0,0),\qquad
(1,1;0,2),\qquad
(0,1;0,3).
\tag{4}
\]

Because the total weight is exactly \(8\), every vertex outside the two end blocks has label \(0\).

The first pattern in (3) is impossible: \(b_3\) is zero, and its neighborhood
\[
\{a_1,a_2,a_3\}
\]
contains neither a label \(3\) nor two labels \(2\). This remains true for \(n=4\), because the right equality patterns in (4) give \(f(a_3)\le2\).

The second pattern in (3) is also impossible. If \(n\ge5\), then \(a_3=0\), so the zero vertex \(b_3\) sees only the single label \(2\) at \(a_1\). If \(n=4\), the only right equality pattern that could supply a second label \(2\) at \(a_3\) is \((2,2;0,0)\); but then the zero vertex \(a_2\) has neighborhood \(\{b_2,b_3,b_4\}\) containing no label \(2\) or \(3\). Hence only the third left pattern in (3) survives.

By symmetry, only the third right pattern in (4) survives. This is exactly \(f^\star\), proving uniqueness for all \(n\ge4\).

For \(n=2\) and \(n=3\), the displayed finite lists are proved by exhaustive inspection of all
\[
4^{2n}
\]
labelings using the defining conditions directly. The included verifier performs this exhaustive check and confirms that no other labeling attains the stated minimum.

## Verification
The included checker constructs \(H_n\) directly for
\[
2\le n\le5
\]
and enumerates every map
\[
f:V(H_n)\to\{0,1,2,3\}.
\]
It tests the double Roman conditions and independently checks that the zero-induced subgraph has no isolated vertex.

For \(n=2\) and \(n=3\), the complete minimum-function lists are compared exactly. For \(n=4\) and \(n=5\), the checker confirms that the unique minimum is the four-corner function proved above.

## Relationship to prior work
Restrained double Roman domination was introduced in 2021. The introducing paper gives the definition, proves NP-hardness, establishes general bounds, and determines several standard families including paths, cycles, complete graphs, and complete multipartite graphs. Its searchable full text contains no half-graph or chain-graph occurrence.

A later primary paper continues the subject with planar hardness, bounded-clique-width algorithms, general bounds, tree results, and small-value characterizations. Its scope is algorithmic and extremal rather than an exact half-graph computation; no half-graph formula appears in the inspected material.

The half graph is the canonical twin-free chain graph. The new content here is the exact minimum on the whole family together with the full optimizer classification, including the sharp uniqueness threshold at \(n=4\).

## Limitations
The theorem concerns minimum restrained double Roman functions, not the complete weight distribution of all feasible functions.

The boundary cases \(H_2\) and \(H_3\) are exceptional and are certified by finite exhaustive verification; the arbitrary-\(n\) argument begins at \(n=4\).

The finite checker through \(n=5\) is corroborative for the infinite family. The proof of the \(n\ge4\) theorem is independent of finite enumeration.

A differently phrased or non-indexed half-graph treatment may exist despite the targeted searches.

## References
1. D. A. Mojdeh, I. Masoumi, L. Volkmann, “Restrained double Roman domination of a graph,” arXiv:2106.08501v1, 16 June 2021; RAIRO-Operations Research 56 (2022), 2293–2304, DOI 10.1051/ro/2022089.
2. B. Samadi, N. Soltankhah, H. Abdollahzadeh Ahangar, M. Chellali, D. A. Mojdeh, S. M. Sheikholeslami, J. C. Valenzuela-Tripodoro, “Restrained condition on double Roman dominating functions,” arXiv:2109.06666v1, 11 September 2021; Applied Mathematics and Computation 438 (2023), 127554, DOI 10.1016/j.amc.2022.127554.
