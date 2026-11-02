# Strict geodesic unimodality of single-grounding second-order coherence on weighted trees

## Finding

**Theorem (global tree-leader unimodality and exact linear-time optimization).** Let \(T=(V,E)\) be any finite undirected tree with \(n=|V|\ge 2\), each edge \(e\) assigned an arbitrary strictly positive conductance \(c_e\), and resistance \(r_e=1/c_e\). For every potential noise-free leader \(v\in V\), let \(L^{(v)}\) be the positive-definite matrix obtained by deleting the row and column of \(v\) from the weighted combinatorial Laplacian. Set

\[
J(v)=\operatorname{tr}\!\left((L^{(v)})^{-2}\right).
\]

For any ordered sequence of consecutive vertices \(v_0,v_1,\ldots,v_\ell\) on a simple path, there are real numbers \(B_0<B_1<\cdots<B_{\ell-1}\) such that

\[
J(v_{i+1})-J(v_i)=r_{v_iv_{i+1}}B_i.
\]

In particular, the signs of consecutive changes can switch only from negative to positive, with at most one zero. Every graph-neighbor local minimizer of \(J\) is global. **There is either one global minimizer or exactly two adjacent global minimizers**, and no others. The full minimizer set and the minimum objective value are computable with \(O(n)\) arithmetic operations and comparisons for arbitrary positive edge resistances, without matrix inversion.

## Assumptions and scope

The statement applies to a tree with at least two vertices, positive finite undirected edge conductances, and exactly **one perfectly grounded** vertex. There are no bounds or uniformity requirements on edge weights. The objective is the inverse-square grounded trace itself; in a stable second-order consensus model whose damping and stiffness are proportional to the grounded Laplacian, a fixed positive scalar multiple is the stationary position-variance measure. These conclusions do not assert anything about higher leader budgets, general cyclic graphs, finite-strength pinning, or objectives other than the displayed inverse-square trace.

For a connected tree \(X\) with distinguished root \(x\in X\), put \(S(X,x)=\mathbf 1^\mathsf{T}(L_X^{(x)})^{-1}\mathbf 1\), with the value zero when \(X\) has one vertex. Equivalently, orient every edge away from \(x\) and let \(s_e\) be the number of vertices downstream of \(e\); then

\[
S(X,x)=\sum_{e\in E(X)}r_e s_e^2.
\]

For an oriented edge \(u\to v\) of \(T\), remove that edge, obtaining the component \(A\) containing \(u\) and the component \(B\) containing \(v\). Set \(p=|A|\), \(q=|B|\), \(r=r_{uv}\), and define its directional comparison bracket by

\[
\mathcal B(u,v)=2\big(S(A,u)-S(B,v)\big)+r(p^2-q^2).
\]

## Proof

**1. Green kernels on a rooted tree.** For a tree rooted at \(x\), let \(P(x,i)\) be the set of edges on the unique path from \(x\) to \(i\). Direct verification of Kirchhoff's current law yields

\[
(L_X^{(x)})^{-1}_{ij}=\sum_{e\in P(x,i)\cap P(x,j)}r_e
\]

for follower vertices \(i,j\ne x\). Summing all entries proves the formula for \(S(X,x)\) above, because an edge contributes to exactly \(s_e^2\) ordered follower pairs.

**2. Exact edge comparison.** In the decomposition \(T\setminus uv=A\sqcup B\), grounding \(u\) makes the follower Green matrix block diagonal across \(A\setminus\{u\}\) and \(B\). On the \(B\)-block the Green matrix is the Green matrix of \(B\) rooted at \(v\), extended by a zero row/column for \(v\), plus \(r\mathbf1\mathbf1^\mathsf T\). Therefore its squared trace equals \(J_B(v)+2rS(B,v)+r^2q^2\). Grounding \(v\) interchanges the sides, giving exactly

\[
J(v)-J(u)=r\left[2(S(A,u)-S(B,v))+r(p^2-q^2)\right]=r\mathcal B(u,v).
\]

**3. Strict increase on every path.** Let \(u,v,w\) be three consecutive vertices. Delete both path edges to get components \(A,C,D\) containing \(u,v,w\), of sizes \(a,c,d\), respectively, and let \(r=r_{uv}\), \(s=r_{vw}\). The all-entries Green sum of a rooted component splits at the adjoining edge. In particular,

\[
S(C\cup D,v)=S(C,v)+S(D,w)+sd^2,
\]
\[
S(A\cup C,v)=S(A,u)+S(C,v)+ra^2.
\]

Substituting into the preceding edge-bracket definition gives the exact identity

\[
\boxed{\mathcal B(v,w)-\mathcal B(u,v)
=4S(C,v)+r\big(a^2+(c+d)^2\big)+s\big((a+c)^2+d^2\big)>0.}
\]

Every term after the Green sum is strictly positive. Repeating over an arbitrary simple path gives the displayed strictly increasing brackets. Because edge resistances are positive, their strictly increasing signs determine consecutive objective differences. Thus along every path the objective strictly decreases until (at most) one flat edge, then strictly increases; its numerical first differences need not themselves increase.

**4. All minimizers and local search.** If \(x\) were a graph-neighbor local minimum but not a global minimum, take a path to a strictly better vertex \(y\). The first edge comparison bracket would be nonnegative, hence all later brackets strictly positive, contradicting \(J(y)<J(x)\). Therefore all local minima are global. If two minimizers were nonadjacent, the path joining them would have at least two edges; unimodality with at most one zero precludes equal endpoint minima. If more than two minimizers existed, two would be nonadjacent. Conversely, two adjacent minimizers can occur, for example the two vertices of a single-edge tree. This proves the complete classification.

**5. Exact linear-time algorithm.** Choose any root \(o\). For each nonroot \(v\), let \(p(v)\) be its parent, \(s_v\) its subtree size, \(d_v\) its total resistance depth, and \(r_v=r_{p(v),v}\). Define \(W_v\) by the postorder recurrence

\[
W_v=\sum_{z:\,p(z)=v}\big(W_z+r_zs_z^2\big).
\]

The initial all-entries Green sum and the initial objective are

\[
S(T,o)=W_o,\qquad
J(o)=\sum_{v\ne o}r_v(2d_{p(v)}+r_v)s_v^2.
\]

The second formula follows by expanding the squared Green kernel into pairs of nested rooted edges: every edge \(p(v)v\) contributes \(r_vs_v^2\) multiplied by \(r_v+2d_{p(v)}\). During a preorder traversal, write \(S_u=S(T,u)\) and, for the parent-child edge \(u\to v\), put \(q=s_v\), \(p=n-q\). Then

\[
\begin{aligned}
S_v&=S_u+r_v(p^2-q^2),\\
S(B,v)&=W_v,\\
S(A,u)&=S_u-W_v-r_vq^2,\\
J(v)&=J(u)+r_v\big[2(S_u-2W_v-r_vq^2)+r_v(p^2-q^2)\big].
\end{aligned}
\]

One postorder and one preorder pass calculate all \(J(v)\), from which a minimum and its one or two attaining vertices follow. This takes \(O(n)\) scalar operations and comparisons and \(O(n)\) storage.

## Verification

A standalone Python 3 standard-library program, `verify_tree.py`, independently constructs the grounded matrix and inverts it by exact rational Gauss–Jordan elimination for 635 reproducible weighted trees with 2–10 vertices. Its 3,798 independently calculated grounded inverses agree exactly with the postorder/preorder values. It additionally checks all directed edge comparisons, strict bracket increase along every simple path, downhill-descent implications, and the complete minimizer cardinality. It tests exact adjacent ties and an example of ordinary nonconvexity.

For an illustrative five-vertex path with successive edge **resistances** \(100,1,1,1\), the exact inverse-square objectives at vertices \(0,1,2,3,4\) are \(162826,10026,10211,10422,10663\). The unique optimum is vertex \(1\), whereas the first-order (sum-of-distances) tree median is vertex \(2\). Thus the inverse-square rule is not just the classic first-order median rule. These finite checks support but do not establish the all-tree theorem; the foregoing exact identities are its proof.

## Relationship to prior work

Fitch and Leonard (arXiv:1407.1569, first public July 7, 2014) establish the optimal-single-leader information-centrality characterization for first-order noisy consensus. On a weighted tree this leads to a shortest-path distance sum (weighted 1-median), whereas the present objective is the squared Green kernel and may choose a different vertex. Patterson, McGlohon, and Dyagilev (arXiv:1412.6595) give polynomial-time algorithms on weighted paths and cycles for the **inverse-trace**, rather than inverse-square, criterion. Mackin and Patterson (arXiv:1905.09156, Theorem 5 and Section IV) give the inverse-square second-order coherence formula and general submodularity-based greedy selection, without claiming strict geodesic unimodality or the exact linear-time all-weighted-tree single-leader result here. The main contribution is the strict signed-edge-gradient law for every positively weighted tree, not the already known availability of the inverse-square metric or of general greedy approximations.

## Limitations

Only one perfectly grounded leader, trees, positive edge conductances, and the specified inverse-square trace are covered. General graphs with cycles and multiple leaders can have different behavior. Linear complexity is arithmetic-model complexity; approximate floating-point input may require interval or exact rational arithmetic to resolve near ties. The tests examine finite instances; publication priority against all specialized sources has not been independently certified. The connection with physical second-order variance requires the appropriate stable proportional-Laplacian dynamics and normalization; the theorem itself needs none of these modeling assumptions beyond the mathematical objective.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first posted July 7, 2014). https://arxiv.org/abs/1407.1569
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (first posted December 20, 2014). https://arxiv.org/abs/1412.6595
3. E. D. Mackin and S. Patterson, *Submodularity in Systems with Higher Order Consensus with Absolute Information*, arXiv:1905.09156 (2019), in particular the second-order coherence formula of Theorem 5. https://arxiv.org/abs/1905.09156
