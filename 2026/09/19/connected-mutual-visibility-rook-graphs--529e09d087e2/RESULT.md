# Connected mutual visibility of rook graphs is exactly the Zarankiewicz number

## Result

Let
\[
R_{m,n}=K_m\square K_n,\qquad m,n\ge 2,
\]
be the rook graph on an \(m\times n\) board. For \(X\subseteq V(R_{m,n})=[m]\times[n]\), form the bipartite graph \(B_X\) with row vertices \(r_1,\dots,r_m\), column vertices \(c_1,\dots,c_n\), and edge \(r_i c_j\) exactly when \((i,j)\in X\).

Then:

1. \(X\) is a mutual-visibility set of \(R_{m,n}\) if and only if \(B_X\) is \(C_4\)-free.
2. \(R_{m,n}[X]\cong L(B_X)\), so \(X\) is connected if and only if all edges of \(B_X\) lie in one connected component.
3. Every inclusion-maximal mutual-visibility set of \(R_{m,n}\) is connected.

Consequently,
\[
\boxed{\mu_c(K_m\square K_n)=\mu(K_m\square K_n)=z(m,n;2,2)},
\]
where \(z(m,n;2,2)\) is the Zarankiewicz number, equivalently the maximum number of edges in a \(C_4\)-free bipartite graph with part sizes \(m,n\).

The conclusion is stronger than equality of the two maxima: **connectivity is automatic for every inclusion-maximal mutual-visibility set** in a rook graph.

## Proof

The first assertion is the standard rook-graph/Zarankiewicz correspondence. Two selected cells in a common row or column are adjacent. If \((i,j),(i',j')\in X\) differ in both coordinates, then they are at distance two and their only two possible internal vertices on a geodesic are the opposite corners \((i,j')\) and \((i',j)\). Thus the selected pair fails to be mutually visible exactly when both opposite corners also belong to \(X\), which is exactly a \(C_4\) in \(B_X\).

For the second assertion, vertices of the line graph \(L(B_X)\) are the edges \(r_i c_j\) of \(B_X\), and two such edges are adjacent exactly when they share a row endpoint or a column endpoint. This is exactly adjacency of the corresponding cells in \(R_{m,n}[X]\).

Now let \(X\) be inclusion-maximal as a mutual-visibility set. By the first assertion, \(B_X\) is an edge-maximal \(C_4\)-free spanning subgraph of \(K_{m,n}\). Suppose its edges lie in two distinct nontrivial components. Choose a row vertex \(r\) incident with an edge of one component and a column vertex \(c\) incident with an edge of another. The edge \(rc\) is absent. Adding \(rc\) cannot create a \(C_4\): any new \(C_4\) would contain \(rc\), and deleting that edge from the cycle would leave an old length-three path from \(r\) to \(c\), impossible because they were in different components. This contradicts edge-maximality. Hence all edges of \(B_X\) lie in a single component, and therefore \(L(B_X)\cong R_{m,n}[X]\) is connected.

Every maximum mutual-visibility set is inclusion-maximal, so it is connected. The classical identity \(\mu(K_m\square K_n)=z(m,n;2,2)\) then gives the displayed formula for \(\mu_c\).

## Explicit exact regimes

Write
\[
p=\min\{m,n\},\qquad q=\max\{m,n\}.
\]
For every \(C_4\)-free bipartite graph with left part of size \(p\), right degrees \(d_1,\dots,d_q\) satisfy
\[
\sum_{j=1}^q \binom{d_j}{2}\le \binom p2,
\]
because each pair of left vertices has at most one common neighbour. Since
\[
d\le 1+\binom d2\qquad(d\ge0),
\]
we obtain
\[
z(p,q;2,2)\le q+\binom p2.
\]
Equality holds if and only if \(q\ge\binom p2\). Indeed, if \(q\ge\binom p2\), use one degree-two right vertex for every pair of left vertices and make all remaining right vertices degree one. Conversely, equality in the two inequalities above forces every right degree to be \(1\) or \(2\), and forces exactly \(\binom p2\) degree-two vertices, hence \(q\ge\binom p2\).

Therefore
\[
\boxed{\mu_c(K_p\square K_q)=q+\binom p2\quad\text{whenever }q\ge\binom p2.}
\]
In particular,
\[
\mu_c(K_2\square K_q)=q+1,
\qquad
\mu_c(K_3\square K_q)=q+3\quad(q\ge3).
\]
For \(p=4\), the same pair-budget argument gives the full thin-side formula
\[
\mu_c(K_4\square K_q)=
\begin{cases}
9,&q=4,\\
10,&q=5,\\
q+6,&q\ge6.
\end{cases}
\]
For example, at \(q=4\) one degree-three column together with three degree-two columns can use the six available left-pairs without repetition, giving \(9\) edges; at \(q=5\), five degree-two columns give \(10\) edges; and the pair-count upper bound proves optimality.

For square rook graphs, the result transfers the classical Zarankiewicz problem without loss:
\[
\mu_c(K_n\square K_n)=z(n,n;2,2).
\]
Hence the known bounds, for sufficiently large \(n\),
\[
n^{3/2}-n^{4/3}\le \mu_c(K_n\square K_n)
\le \frac n4\bigl(1+\sqrt{4n-3}\bigr)
\]
apply verbatim, and determining the exact connected mutual-visibility number of square rook graphs is exactly the classical \(C_4\)-free Zarankiewicz problem.

## Context and originality

Connected mutual visibility was introduced by Tonny K B and Shikhi M in September 2026. Their current preprint develops general bounds, the diameter-two characterization, complete multipartite graphs, defect graphs, joins, block graphs, cycles, cacti, and corona products. The inspected version contains no theorem for rook/Hamming graphs or Cartesian products of complete graphs.

For classical mutual visibility, Cicerone, Di Stefano, and Klavžar proved that a set in \(K_m\square K_n\) is mutual-visible exactly when it occupies at most three vertices of every Cartesian square, and consequently
\(\mu(K_m\square K_n)=z(m,n;2,2)\). The present result adds the connectivity constraint and shows that, at maximality, the constraint is automatically satisfied. A 2026 Builder--Blocker paper also treats Hamming graphs via the same classical \(C_4\)-free correspondence, but predates the connected parameter.

To the best of our knowledge, no source located in exact, synonymous, product-graph, Hamming-graph, rook-graph, or Zarankiewicz searches states that every maximal mutual-visibility set of a rook graph is connected, or the resulting identity \(\mu_c(K_m\square K_n)=z(m,n;2,2)\).

The saturation observation itself is elementary and is not claimed as a new theorem about \(C_4\)-saturated bipartite graphs; older work studies such graphs directly. The claimed contribution is its consequence for the newly introduced connected mutual-visibility invariant, together with the maximal-set strengthening and explicit transferred regimes above.

## Verification

The proof is general and does not rely on computation. The accompanying standalone verifier exhausts all subsets for
\[
(m,n)\in\{(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\},
\]
checks the \(C_4\)-free characterization, computes the ordinary and connected maxima, and checks that every inclusion-maximal \(C_4\)-free set induces a connected rook subgraph. All tested instances pass.

## Limitations

The exact identity reduces the problem to the Zarankiewicz number; it does not solve the still-open general Zarankiewicz problem. The explicit formula \(q+\binom p2\) covers precisely the regime in which that elementary pair-count upper bound can be tight, and the displayed \(p=4\) cases are a small additional thin-side calculation. The result concerns two-factor Hamming/rook graphs only; higher-dimensional Hamming graphs have different visibility geometry.

Originality is asserted only to the best of our knowledge. The central connected-mutual-visibility source and the classical rook-graph mutual-visibility source were inspected in full text. The 2002 paper of Bryant and Fu on \(C_4\)-saturated bipartite graphs was inspected through bibliographic/abstract material rather than full text; it could contain the elementary connectivity observation about saturated bipartite graphs, but it predates mutual visibility and does not by itself cover the connected-mutual-visibility identity. Very recent or unindexed parallel work remains a residual risk.

## References

1. Tonny K B and Shikhi M, *Connected Mutual-Visibility in Graphs*, arXiv:2609.18877v1 (2026). https://arxiv.org/abs/2609.18877
2. S. Cicerone, G. Di Stefano, S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, Applied Mathematics and Computation 438 (2023), 127619; arXiv:2112.13024v2. https://arxiv.org/abs/2112.13024
3. D. E. Bryant and H.-L. Fu, *C4-saturated bipartite graphs*, Discrete Mathematics 259 (2002), 263--268. https://doi.org/10.1016/S0012-365X(02)00371-0
4. V. Iršič Chenoweth, S. Klavžar, G. Rus, E. Tan, J. Tian et al., *Builder-Blocker Mutual-Visibility Game*, Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), article 89. https://doi.org/10.1007/s40840-026-02083-9
