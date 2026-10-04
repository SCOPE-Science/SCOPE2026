# Near-square stabilization of minimal finite bouquet models
## Finding
Let \(B_n=\bigvee_{i=1}^n S^1\), and let \(M(n)\) denote the number of homeomorphism classes of minimal finite \(T_0\)-models of \(B_n\). For \(e\ge 0\), define \(b_e\) to be the number of isomorphism classes of finite bipartite graphs with an ordered pair of color classes, exactly \(e\) edges, and no isolated vertices, where isomorphisms preserve the two color classes. Put \(b_0=1\), represented by the empty bipartite graph.

For every pair of integers \(d\ge 0\) and \(k\ge d+1\),
\[
M(k^2-d)=b_d+2\sum_{r=1}^{\lfloor\sqrt d\rfloor} b_{d-r^2}.
\]
Hence the number of minimal finite models depends only on the fixed deficit \(d\), not on \(k\), once \(k\ge d+1\). The first values are
\[
M(k^2)=1,\quad M(k^2-1)=3,\quad M(k^2-2)=5,\quad M(k^2-3)=12,
\]
\[
M(k^2-4)=30,\quad M(k^2-5)=68,
\]
with the displayed formulas valid respectively for \(k\ge1,2,3,4,5,6\).

## Assumptions and scope
A minimal finite model means a finite \(T_0\)-space of minimum cardinality in the weak homotopy type of the indicated bouquet. Homeomorphism of finite \(T_0\)-spaces is order isomorphism. The bipartite number \(b_e\) is color-preserving: interchanging the two color classes is not identified unless it can already be achieved by a color-preserving isomorphism after the ambient construction is fixed.

The result concerns bouquets of circles whose rank is \(k^2-d\) with fixed nonnegative deficit \(d\) and \(k\ge d+1\). It does not enumerate arbitrary ranks in a single closed formula, and it does not assert an asymptotic formula for \(b_e\).

## Proof
Barmak and Minian characterize minimal finite models of \(B_n\): if \(X\) is such a model and \(p\) and \(q\) are the numbers of minimal and maximal points, then \(X\) has height one,
\[
p+q=\min\{u+v:(u-1)(v-1)\ge n}\},
\]
and its Hasse diagram has
\[
|E|=|X|+n-1
\]
edges. Conversely, those conditions imply that \(X\) is a minimal finite model.

Fix \(d\ge0\), \(k\ge d+1\), and put \(n=k^2-d\). Since \(d\le k-1\),
\[
k(k-1)<k^2-d\le k^2.
\]
Therefore the minimum of \(u+v\) subject to \((u-1)(v-1)\ge n\) is \(2k+2\). Write
\[
a=p-1,\qquad b=q-1.
\]
Then \(a+b=2k\). After first choosing the orientation with \(a\le b\), there is a unique integer \(r\ge0\) with
\[
a=k-r,\qquad b=k+r.
\]
The feasibility condition is
\[
ab=k^2-r^2\ge k^2-d,
\]
which is equivalent to \(r^2\le d\).

For such \(r\), the complete bipartite Hasse diagram on the two levels has
\[
pq=(k-r+1)(k+r+1)=(k+1)^2-r^2
\]
edges. A minimal model has
\[
|E|=(2k+2)+(k^2-d)-1=(k+1)^2-d,
\]
so exactly
\[
e=d-r^2
\]
relations are missing from the complete bipartite order.

The hypothesis \(k\ge d+1\) makes the ambient levels strictly larger than any support needed by those missing relations. Indeed, with \(p=k-r+1\le q\),
\[
p-e=k-r+1-(d-r^2)\ge r^2-r+2\ge2.
\]
Thus \(p>e\) and \(q>e\), and in fact every vertex of the remaining Hasse graph has degree at least two. Deleting any \(e\) edges also cannot disconnect \(K_{p,q}\), because its edge connectivity is \(\min(p,q)=p>e\). Hence every \(e\)-edge missing-relation pattern gives a connected two-level poset whose order complex is a graph with \(2k+2\) vertices and \(2k+1+n\) edges, so its first Betti number is \(n\). It is therefore weakly homotopy equivalent to \(B_n\), has no beat points, and has the minimum possible number of points.

Two such models with the same ordered pair \((p,q)\) are homeomorphic exactly when their missing-edge bipartite graphs lie in the same orbit under independent permutations of the two levels. Because \(p,q>e\), every \(e\)-edge missing graph uses at most \(e\) vertices on either side, so deleting its isolated vertices gives a finite bipartite graph with ordered color classes, exactly \(e\) edges, and no isolated vertices. Conversely, every such graph embeds by adding isolated vertices to the missing-edge graph. Therefore there are exactly \(b_e\) homeomorphism classes for this ordered pair \((p,q)\).

When \(r=0\), the two levels both have \(k+1\) points and contribute \(b_d\) classes. For each \(1\le r\le\lfloor\sqrt d\rfloor\), the two orientations
\[
(p,q)=(k-r+1,k+r+1)
\]
and
\[
(p,q)=(k+r+1,k-r+1)
\]
have different numbers of minimal points and therefore yield disjoint sets of homeomorphism classes, each of size \(b_{d-r^2}\). Summing gives
\[
M(k^2-d)=b_d+2\sum_{r=1}^{\lfloor\sqrt d\rfloor}b_{d-r^2}.
\]

For the displayed numerical cases, direct color-preserving enumeration gives
\[
(b_0,b_1,b_2,b_3,b_4,b_5)=(1,1,3,6,16,34),
\]
which produces \(1,3,5,12,30,68\).

## Verification
The symbolic argument above proves the theorem for every \(d\ge0\) and \(k\ge d+1\). The included verifier independently enumerates color-preserving bipartite isomorphism classes for \(0\le e\le5\), recovering
\[
1,1,3,6,16,34,
\]
and checks the resulting deficit counts. It also directly enumerates the missing-edge orbits for the concrete ranks \(9,8,7,13\), obtaining respectively \(1,3,5,12\) minimal-model classes, in agreement with the formula.

The finite computation is a check of the first cases and of the orbit interpretation; it is not used as a proof for arbitrary \(d\).

## Relationship to prior work
Barmak and Minian's 2006 preprint and 2007 paper characterize all minimal finite models of bouquets of circles by cardinality and Hasse-edge count. Their example classifies the three models of \(B_3\), and their later book proves that \(B_n\) has a unique minimal finite model exactly when \(n\) is a square. Those results supply the classification criterion used here, but they do not give the square-deficit multiplicity formula or identify the stabilized multiplicities with color-preserving bipartite graph counts.

The later paper by Das and Mawiong discusses minimal finite models for several wedges involving \(S^2\) and recalls the bouquet-of-circles background, but it does not enumerate homeomorphism classes of minimal models in the fixed square-deficit families treated here.

## Limitations
The formula packages the remaining finite enumeration into the numbers \(b_e\). No closed form or asymptotic for \(b_e\) is proved. The stabilization threshold \(k\ge d+1\) is a sufficient uniform threshold arising from the support bound; it is not claimed to be optimal for each fixed \(d\). The literature comparison found no statement implying the multiplicity formula, but older or non-indexed discussions of detailed bouquet-model counts could still exist.

## References
1. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156, first posted 2006-11-06; Journal of Homotopy and Related Structures 2 (2007), 127--140.
2. J. A. Barmak, *Algebraic Topology of Finite Topological Spaces and Applications*, Lecture Notes in Mathematics 2032, Springer, 2011, DOI: 10.1007/978-3-642-22003-6, Section 3.3.
3. P. Das and S. M. Mawiong, *Minimal Finite Model of Wedge Sum of Spheres*, arXiv:2405.13385, 2024.
