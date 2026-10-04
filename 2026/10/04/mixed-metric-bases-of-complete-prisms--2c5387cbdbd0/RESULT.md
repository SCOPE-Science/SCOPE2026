# Mixed metric bases of complete prisms
## Finding
For every integer \(n\ge5\), let \(G_n=K_n\square K_2\), with clique layers \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_i\) is the matching edge. Then \(\operatorname{mdim}(G_n)=n\). Moreover, the mixed metric bases are exactly the sets that contain one endpoint of every matching edge and contain at least two vertices from each clique layer. Consequently the number of mixed metric bases is \[2^n-2n-2.\]

## Assumptions and scope
All graphs are finite, simple, and connected. For \(n\ge5\), let
\[
G_n=K_n\square K_2,
\]
with clique layers
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and matching edges \(a_i b_i\).

A set \(S\subseteq V(G_n)\) is a mixed metric generator if every two distinct elements of \(V(G_n)\cup E(G_n)\) have different ordered distance vectors to \(S\), where the distance from a vertex to an edge is the minimum distance to its endpoints.

## Proof
We first prove the lower bound. Fix an index \(j\), and choose any \(i\ne j\). Compare the vertex \(a_i\) with the clique edge \(a_i a_j\). A landmark distinguishes these two elements only if it is \(a_j\) or \(b_j\): every other vertex is equally far from \(a_i\) and from the edge \(a_i a_j\). Hence every mixed metric generator meets
\[
\{a_j,b_j\}
\]
for every \(j\). Therefore
\[
|S|\ge n.
\]

Suppose now that \(|S|=n\). The preceding argument forces \(S\) to contain exactly one endpoint of each matching edge. Let
\[
X=\{i:a_i\in S\},\qquad Y=\{i:b_i\in S\},
\]
so \(X\sqcup Y=\{1,\ldots,n\}\).

If \(X=\varnothing\), then for every \(j\), the selected vertex \(b_j\) and the matching edge \(a_jb_j\) have identical distance vectors to \(S\). If \(X=\{r\}\), then for each \(j\in Y\), the matching edge \(a_jb_j\) and the clique edge \(b_rb_j\) have identical distance vectors to \(S\). Thus \(|X|\ge2\). By symmetry, \(|Y|\ge2\).

It remains to prove these conditions are sufficient. For each selected landmark \(s_i\), where \(s_i=a_i\) for \(i\in X\) and \(s_i=b_i\) for \(i\in Y\), every distance from \(s_i\) to a vertex or edge of \(G_n\) belongs to \(\{0,1,2\}\). Hence an element is determined by the pair
\[
(Z_0,Z_2),
\]
where \(Z_t\) is the set of landmark indices at distance \(t\).

The pairs are as follows.

For vertices:
\[
a_j:
\begin{cases}
(\{j\},Y),&j\in X,\\
(\varnothing,Y\setminus\{j\}),&j\in Y,
\end{cases}
\qquad
b_j:
\begin{cases}
(\varnothing,X\setminus\{j\}),&j\in X,\\
(\{j\},X),&j\in Y.
\end{cases}
\]

For a matching edge:
\[
a_jb_j:(\{j\},\varnothing).
\]

For a clique edge \(a_ja_k\):
\[
a_ja_k:\bigl(\{j,k\}\cap X,\;Y\setminus\{j,k\}\bigr),
\]
and for a clique edge \(b_jb_k\):
\[
b_jb_k:\bigl(\{j,k\}\cap Y,\;X\setminus\{j,k\}\bigr).
\]

Within each displayed type, the endpoint indices are recovered from the exceptional coordinates, so no two distinct elements of the same type collide. A selected vertex cannot collide with an incident clique edge because the edge deletes one coordinate from the opposite-layer \(Z_2\)-set. Matching edges are the unique elements with one zero-coordinate and empty \(Z_2\).

The only possible cross-layer ambiguity with no zero-coordinate would be an \(A\)-clique edge whose two endpoints exhaust \(Y\) and a \(B\)-clique edge whose two endpoints exhaust \(X\). This requires
\[
|X|=|Y|=2,
\]
hence \(n=4\), excluded here. Since \(n\ge5\) and \(|X|,|Y|\ge2\), all displayed pairs are distinct. Therefore every such transversal is a mixed metric basis.

Finally, choosing a mixed metric basis is equivalent to choosing the subset \(X\subseteq\{1,\ldots,n\}\) with
\[
2\le|X|\le n-2.
\]
Thus the number of bases is
\[
\sum_{k=2}^{n-2}\binom nk
=
2^n-2n-2.
\]

## Verification
The included checker constructs \(K_n\square K_2\) directly, computes all-pairs vertex distances, and evaluates mixed distance vectors for every vertex and every edge.

For each \(5\le n\le9\), it checks every vertex subset of size below \(n\) and verifies that none is mixed resolving. It then checks every \(n\)-vertex subset and compares the direct mixed-resolving test with the exact matching-transversal characterization above.

## Relationship to prior work
The foundational mixed metric dimension paper introduces the invariant, establishes structural facts, treats trees and grids, and closes with an explicit open problem asking for relationships between the mixed metric dimension of product graphs and the dimensions of their factors. Its inspected full text contains no prism formula.

Later work on prism-related mixed resolvability studies a different planar family \(\mathbb D_n^t\), obtained from the ordinary cycle prism by adding additional vertices and pendant edges. That graph has \(4n\) vertices and \(6n\) edges and is not the complete prism \(K_n\square K_2\). Targeted searches for complete prisms, clique prisms, \(K_n\square K_2\), and mixed metric bases did not locate an equivalent theorem.

## Limitations
The theorem is stated for \(n\ge5\). The exceptional graph \(K_4\square K_2\) has a different minimum size and is not included. No claim is made for \(K_m\square K_n\) with both factors of order at least three, or for other metric-dimension variants. Literature search cannot exclude a differently named or non-indexed complete-prism treatment.

## References
1. A. Kelenc, D. Kuziak, A. Taranenko, I. G. Yero, “Mixed metric dimension of graphs,” arXiv:1611.04292v1, 14 November 2016; Applied Mathematics and Computation 314 (2017), 429–438, DOI 10.1016/j.amc.2017.07.027.
2. S. Kumar Sharma, V. Kumar Bhat, “Unbounded Mixed Resolvability of Web Graph and Prism Related Graph,” arXiv:2108.08588v1, 19 August 2021.
