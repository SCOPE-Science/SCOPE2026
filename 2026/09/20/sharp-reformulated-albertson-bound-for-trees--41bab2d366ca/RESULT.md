# Sharp maximum reformulated Albertson index of trees

## Statement

For a graph \(G\), let
\[
\operatorname{RAlb}(G)=\sum_{e\sim f}|d_G(e)-d_G(f)|,
\qquad d_G(xy)=d_G(x)+d_G(y)-2,
\]
where the sum is over unordered adjacent edge pairs. Equivalently,
\(\operatorname{RAlb}(G)=\operatorname{Alb}(L(G))\).

For every tree \(T\) on \(n\ge 2\) vertices,
\[
\boxed{\operatorname{RAlb}(T)\le
2\left\lfloor\frac{(n-2)^2}{4}\right\rfloor
=\left\lfloor\frac{(n-2)^2}{2}\right\rfloor.}
\]
For \(n\ge4\), equality holds if and only if \(T\) is the balanced double star: two adjacent non-leaf vertices with \(p\) and \(q\) pendant neighbors, where
\(p+q=n-2\) and \(|p-q|\le1\). For \(n=2,3\), the unique tree has reformulated Albertson index zero, agreeing with the formula.

Thus, equivalently, among line graphs of \(n\)-vertex trees, the maximum Albertson index is \(\lfloor (n-2)^2/2\rfloor\), uniquely attained for \(n\ge4\) by the line graph of the balanced double star.

## Context

Albertson's irregularity index sums degree differences across adjacent vertices. Work on graph operations has studied how this irregularity behaves under derived constructions, including line-graph-related operations. Cutinha, D'Souza and Nayak introduced the reformulated Albertson index as the adjacent-edge analogue and observed the exact identity \(\operatorname{RAlb}(G)=\operatorname{Alb}(L(G))\). Their 2025 paper proves sharp lower bounds for fixed-order trees and unicyclic graphs with prescribed maximum degree and gives general upper bounds in terms of order, size, minimum degree, maximum degree, the Platt number and Zagreb-type quantities. In particular, their general bound
\[
\operatorname{RAlb}(G)\le m(\Delta-1)(\Delta-\delta)
\]
is not an exact order-only extremal theorem for trees. The result above supplies such a sharp theorem and a complete equality characterization.

## Proof

Write
\[
x_v=d_T(v)-1\ge0.
\]
If \(v\) has neighbors \(u_1,\dots,u_k\), then the adjacent edge pairs whose common endpoint is \(v\) contribute
\[
F_v=\sum_{1\le i<j\le k}|d_T(u_i)-d_T(u_j)|
=\sum_{1\le i<j\le k}|x_{u_i}-x_{u_j}|.
\]

We use the elementary inequality
\[
\sum_{i<j}|a_i-a_j|\le (k-1)\sum_{i=1}^k a_i
\tag{1}
\]
for nonnegative \(a_1,\dots,a_k\). To see this, order them as
\(a_1\le\cdots\le a_k\). Then
\[
\sum_{i<j}(a_j-a_i)
=\sum_{i=1}^k(2i-k-1)a_i
\le (k-1)\sum_{i=1}^k a_i.
\]
If \(k\ge2\) and the right-hand sum is positive, equality in (1) holds exactly when at most one of the \(a_i\) is positive.

Applying (1) at each vertex gives
\[
F_v\le (d_T(v)-1)\sum_{u\sim v}(d_T(u)-1)
=x_v\sum_{u\sim v}x_u.
\]
Hence
\[
\operatorname{RAlb}(T)
=\sum_v F_v
\le \sum_v x_v\sum_{u\sim v}x_u
=2\sum_{uv\in E(T)}x_ux_v.
\tag{2}
\]

Let \((A,B)\) be the bipartition of the tree and put
\(X_A=\sum_{u\in A}x_u\), \(X_B=\sum_{v\in B}x_v\). Since all \(x_v\) are nonnegative,
\[
\sum_{uv\in E(T)}x_ux_v\le X_AX_B.
\tag{3}
\]
Also, using \(\sum_v d_T(v)=2(n-1)\),
\[
X_A+X_B=\sum_v(d_T(v)-1)=n-2.
\]
Therefore
\[
X_AX_B\le \left\lfloor\frac{(n-2)^2}{4}\right\rfloor.
\tag{4}
\]
Combining (2)--(4) proves the claimed upper bound.

It remains to characterize equality for \(n\ge4\). Equality in the final bound is positive. Equality in the local inequality (1) at every vertex implies that every vertex has at most one non-leaf neighbor, because \(x_u>0\) exactly when \(u\) is non-leaf. The subgraph induced by the non-leaf vertices of a tree is connected: the unique path between any two non-leaves has only non-leaf internal vertices. Thus this induced subgraph has at most two vertices. It cannot have only one, because then \(T\) is a star and \(\operatorname{RAlb}(T)=0\). Consequently it has exactly two adjacent vertices, so \(T\) is a double star.

Let its two centers have \(p\) and \(q\) pendant neighbors. Then \(p+q=n-2\), and a direct evaluation gives
\[
\operatorname{RAlb}(T)=2pq.
\]
This is maximal exactly when \(|p-q|\le1\), yielding
\(2\lfloor(n-2)^2/4\rfloor\). Conversely, every balanced double star attains the bound. This proves uniqueness up to isomorphism.

## Verification

A definition-level enumeration with NetworkX 3.6.1 checked every non-isomorphic tree through order 17. At every order the computed maximum equals \(\lfloor(n-2)^2/2\rfloor\); for every \(n\ge4\) there is exactly one maximizing isomorphism class, with the balanced-double-star degree sequence. The script and recorded output are included in `artifacts/`.

The finite check is corroborative only; the theorem is established by the proof above.

## Originality and limitations

To the best of our knowledge, searches for the exact formula, "maximum reformulated Albertson index", "Albertson index of line graphs of trees", "irregularity of line graphs of trees", and balanced/double-star variants did not locate this sharp order-only theorem or its equality characterization. The directly relevant 2025 reformulated-Albertson paper was inspected through its definition, tree results, and upper-bound section; it gives general parameter bounds rather than this extremal formula. Recent work on extremal ordinary Albertson indices for trees with prescribed degree sequences concerns \(\operatorname{Alb}(T)\), not \(\operatorname{Alb}(L(T))\).

Residual originality risk remains from unindexed literature, terminology that does not use "reformulated Albertson", or a result stated purely as irregularity of a restricted block/line-graph class. No independent audit has yet been performed.

## References

1. M. O. Albertson, *The Irregularity of a Graph*, Ars Combinatoria 46 (1997), 219--225. https://combinatorialpress.com/ars-articles/volume-046-ars-articles/the-irregularity-of-a-graph/
2. N. De, A. Pal, S. M. A. Nayeem, *The Irregularity of Some Composite Graphs*, International Journal of Applied and Computational Mathematics 2 (2016), 411--420. https://doi.org/10.1007/s40819-015-0069-z
3. J. S. Cutinha, S. D'Souza, S. Nayak, *On the minimum reformulated Albertson Index of fixed-order trees and unicyclic graphs with a given maximum degree*, AKCE International Journal of Graphs and Combinatorics 22(2) (2025), 217--223. https://doi.org/10.1080/09728600.2025.2458263
4. J. Hamoud, A. Ya. Belov, *Extremal Topological Indices with Prescribed Degree Sequences*, Vestnik KRAUNC. Fiz.-Mat. Nauki 53(4) (2025), 9--28. https://doi.org/10.26117/2079-6641-2025-53-4-9-28
