# Exact KLX number of balanced complete multipartite graphs
## Finding
For all integers \(r\ge 3\) and \(m\ge 2\), let \(G=K_{m,\ldots,m}\) be the complete \(r\)-partite graph with every part of size \(m\). Then
\[
\operatorname{KLX}(G)=
\begin{cases}
\dfrac{r(r-1)m^2}{4}-1,&m\text{ even},\\[4pt]
\left\lfloor\dfrac{r(r-1)m^2+r}{4}\right\rfloor-1,&m\text{ odd}.
\end{cases}
\]
An optimal ordered DFS tree is the Hamiltonian path obtained by visiting the parts cyclically in the order \(1,2,\ldots,r\), repeated \(m\) times.

## Assumptions and scope
Graphs are finite, connected, and simple. KLX is the kissing-loop-crossing number of Bourotte, Ducloz, Orponen, and Seki: for an ordered DFS tree, one counts the maximum number of back edges open at a tree edge, and then minimizes over ordered DFS trees. The result concerns balanced complete multipartite graphs with at least three parts and at least two vertices in each part.

## Proof
Write \(N=rm\). In an undirected DFS tree every non-tree edge joins comparable vertices in the rooted tree order. Consequently, if a vertex \(x\) has two distinct child subtrees, no graph edge can join those subtrees. In a complete multipartite graph this forces the two child roots to lie in the same part, say \(P\). If one child root \(c\in P\) had a proper descendant \(z\), then the tree edge out of \(c\) forces \(z\notin P\); but \(z\) would then be adjacent to a root in a different child subtree, contradicting the DFS comparability property. Thus every child subtree at a branch vertex is a singleton. Hence every DFS tree is a path (the spine) ending, possibly, in a fan of singleton leaves that all lie in one part.

If the terminal fan has \(p\) leaves, then \(p\le m\), so the spine has at least \(N-m=(r-1)m>N/2\) vertices because \(r\ge3\). Put \(t=\lfloor N/2\rfloor\). The spine therefore contains a tree edge \(e\) immediately after its first \(t\) vertices. Let \(x_i\) be the number of those \(t\) vertices in part \(i\). Every graph edge crossing this prefix cut, except \(e\) itself, is a back edge crossing \(e\), hence is open at \(e\). The cut has
\[
C(x_1,\ldots,x_r)=t(N-t)-\sum_{i=1}^r x_i(m-x_i)
=t(N-m-t)+\sum_{i=1}^r x_i^2
\]
edges. For fixed \(\sum_i x_i=t\), the sum of squares is minimized when the \(x_i\) differ by at most one. Evaluating that balanced minimum at \(t=\lfloor N/2\rfloor\) gives
\[
F(r,m)=
\begin{cases}
\dfrac{r(r-1)m^2}{4},&m\text{ even},\\[4pt]
\left\lfloor\dfrac{r(r-1)m^2+r}{4}\right\rfloor,&m\text{ odd}.
\end{cases}
\]
Therefore every ordered DFS tree has KLX at least \(F(r,m)-1\).

For the reverse inequality, order the vertices by part labels \(1,2,\ldots,r\), repeated \(m\) times, and take the resulting Hamiltonian path as the DFS tree. Consecutive vertices lie in different parts, and every non-tree edge joins two vertices on this single root-to-leaf chain, so this is a valid DFS tree. Because the tree has no branch vertex, no back edge can envelop a tree edge; the number of open back edges at a path edge is exactly the corresponding cut size minus one.

For a prefix of length \(u=qr+s\), where \(0\le s<r\), the cyclic order has \(q+1\) vertices in \(s\) parts and \(q\) in the remaining parts. If \(B(u)\) denotes its cut size, then adding the next vertex gives
\[
B(u+1)-B(u)=(r-1)(m-2q)-2s.
\]
For \(u<N/2\) this difference is nonnegative: if \(m-2q\ge2\) it follows from \(s\le r-1\), while if \(m-2q=1\), the inequality \(u<N/2\) implies \(2s\le r-1\). Also \(B(N-u)=B(u)\). Thus the maximum occurs at the middle cut and equals \(F(r,m)\). The cyclic DFS path therefore has KLX \(F(r,m)-1\), proving the formula.

## Verification
The proof is symbolic and does not rely on finite computation. The accompanying verifier checks the middle-cut formula and cyclic-path maximum for every \(3\le r\le24\) and \(2\le m\le30\). It also exhausts all path/final-fan DFS structural profiles for \((r,m)=(3,2),(3,3),(4,2)\); their minimum DFS-tree congestion agrees with the claimed KLX value. These finite checks are sanity tests, not substitutes for the proof.

## Relationship to prior work
Bourotte, Ducloz, Orponen, and Seki introduced KLX in 2026, defined crossing and enveloping open back edges, proved DFS-tree congestion is a lower bound for KLX, characterized KLX at most two, and established general algorithmic and tree-width results. Direct inspection of their proceedings paper found no treatment of complete multipartite graphs. A separate published database result gives exact KLX values for complete graphs and complete bipartite graphs. Those are the boundary families with one vertex per part or with two parts; the present domain \(r\ge3\), \(m\ge2\) is neither family and is not implied by those formulas. The proof here also identifies why branching cannot improve the DFS congestion on this balanced multipartite class.

## Limitations
The theorem is restricted to equal part sizes and \(r\ge3\). It does not give the KLX number of arbitrary unbalanced complete multipartite graphs, where the middle-cut balancing and the possible terminal fan interact differently. Independent audit has not been performed.

## References
1. C. Bourotte, G. Ducloz, P. Orponen, S. Seki, “A Congestion Parameter for Depth-First Graph Traversals,” arXiv:2606.24675; MFCS 2026, DOI 10.4230/LIPIcs.MFCS.2026.7.
2. “Exact KLX numbers of complete and complete bipartite graphs,” published published-finding corpus record, 19 September 2026, record hash b27f97da8029.
