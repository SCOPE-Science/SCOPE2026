# Twin-pair locality for adjacency-Dirac spectral distances

## Finding

Let \(V\) be any finite set with two distinct points \(x,y\), and let \(D=(D_{uv})_{u,v\in V}\) be a real symmetric matrix. Suppose that the off-pair entries of its two distinguished rows coincide:
\[
D_{xz}=D_{yz}=w_z\quad (z\in V\setminus\{x,y\}), \qquad D_{xy}=\gamma.
\]
Define
\[
C=\gamma^2+\frac12\sum_{z\ne x,y}w_z^2.
\]
The Connes distance for the diagonal representation on \(\ell^2(V)\) is exactly
\[
d_D(x,y)=\begin{cases}C^{-1/2},&C>0,\\+\infty,&C=0.\end{cases}
\]
No entries of \(D\) between vertices outside \(\{x,y\}\) appear in the answer, nor do the diagonal entries. Moreover, the supremum is attained when \(C>0\) by the explicitly normalized antisymmetric two-point potential. This is a weighted twin-pair locality principle rather than a metric classification for arbitrary vertex pairs.

For an unweighted simple graph, write \(k\) for the number of common neighbors *outside* the pair. Two nonadjacent vertices with identical external neighborhoods (false twins) have \(d_D(x,y)=\sqrt{2/k}\) for \(k>0\). Two adjacent vertices with identical external neighborhoods (true twins) have \(d_D(x,y)=\sqrt{2/(k+2)}\). For \(k=0\), the false-twin distance is infinite. Holding the external neighborhood fixed while deleting the edge joining true twins changes their mutual distance by the exact factor \(\sqrt{(k+2)/k}\) when \(k>0\).

## Assumptions and scope

The ambient Hilbert space is finite-dimensional \(\ell^2(V)\), with the standard orthonormal basis \(e_u\). The Dirac operator is the *specified* real symmetric matrix \(D\), not a graph-incidence Dirac operator or a Laplacian. Real potentials \(f:V\to\mathbb R\) act as diagonal multiplication operators \(F=\operatorname{diag}(f(u))\). The distance is the extended value
\[
d_D(x,y)=\sup\{|f(x)-f(y)|:\ f:V\to\mathbb R,\ \|[D,F]\|_{2\to2}\le1\}.
\]
The equal-row condition is only on columns \(z\notin\{x,y\}\); \(D_{xx}\) and \(D_{yy}\) are arbitrary. The graph corollaries additionally require zero diagonal and edge entries in \(\{0,1\}\). All assertions quantify over every finite \(V\), every permitted real symmetric \(D\), and every designated pair satisfying the displayed row condition.

## Proof

Put \(q=(e_x-e_y)/\sqrt2\), which has Euclidean norm one, and write \(\delta=f(x)-f(y)\). The commutator satisfies \([D,F]_{uv}=D_{uv}(f(v)-f(u))\). Direct multiplication using the equal-row condition gives
\[
[D,F]q=\delta v,\qquad
v=\frac{\gamma}{\sqrt2}(e_x+e_y)
 +\frac1{\sqrt2}\sum_{z\ne x,y}w_z e_z.
\]
Consequently \(v\perp q\), and \(\|v\|_2^2=\gamma^2+(1/2)\sum_z w_z^2=C\). For *every* potential,
\[
\|[D,F]\|_{2\to2}\ge\|[D,F]q\|_2
 =|\delta|\sqrt C.
\]
This is the exact universal upper bound \(|\delta|\le C^{-1/2}\) for admissible \(F\) whenever \(C>0\); note that unspecified outside-to-outside edges cannot invalidate this inequality.

For the reverse inequality, choose \(f_*(x)=1/2\), \(f_*(y)=-1/2\), and \(f_*(z)=0\) elsewhere. A direct entrywise calculation gives
\[
[D,\operatorname{diag}f_*]=vq^{\mathsf T}-qv^{\mathsf T}.
\]
The last matrix is skew-symmetric, acts as \(\begin{pmatrix}0&-\sqrt C\\\sqrt C&0\end{pmatrix}\) on the plane spanned by \(q\) and \(v/\sqrt C\), and vanishes on its orthogonal complement. Hence it has operator norm exactly \(\sqrt C\). Scaling \(f_*\) by \(C^{-1/2}\) is admissible and gives difference \(C^{-1/2}\), proving sharpness and attainment. If \(C=0\), then \(\gamma=0\) and all \(w_z=0\); the same \(f_*\) has zero commutator, and its arbitrary positive scalar multiples prove that the distance is infinite.

For a simple graph, \(w_z\) is one precisely at common neighbors and zero otherwise. The cases \(\gamma=0\) and \(\gamma=1\) give the displayed formulas. Deleting a twin-pair edge replaces \(\gamma=1\) by \(\gamma=0\) without changing the external row profiles, so the exact edge-deletion factor follows. These are consequences of the same universal statement, not separate discoveries.

## Verification

The attached standalone `check_twin.py` uses Python's exact rational arithmetic to check the crucial rank-two certificate for 539 finite real-symmetric matrices with arbitrary rational common external weights, arbitrary rational edges among the other vertices, and varying potentials. Specifically, for \(K=[D,\operatorname{diag}f_*]\), it checks \((K^{\mathsf T}K)^2=C(K^{\mathsf T}K)\) and \(\operatorname{tr}(K^{\mathsf T}K)=2C\). For a randomly selected general potential \(F\), it separately checks \(\|[D,F](e_x-e_y)\|_2^2=2C|f(x)-f(y)|^2\). The exact-rational test output is `EXACT_RATIONAL_OK cases=539`.

Execute `python3 check_twin.py` from a folder containing that file. The displayed proof proves the infinite family of finite-dimensional claims; 539 finite examples alone would not do so.

## Relationship to prior work

Iochum, Krajewski, and Martinetti (1999), Proposition 5, compute the spectral distance between vertices of a uniformly weighted complete graph and between endpoints of its single deleted edge. These are **already known special cases** of the present formula, and are not claimed new. Their three-point formulas also include the triangle case. Besnard (2021) develops graph-pruning, lower bounds, and quantitative comparisons under edge addition and deletion, without the general weighted equal-row identity; the edge-deletion question is not asserted solved in general. Clare, Li, Poon, and Swartz (2024) provide an explicit graph-distance operator framework and solve the path case, without identifying this twin-pair locality identity.

The contribution assessed here is the exact ambient-independent formula under arbitrary equal external row profiles, including arbitrary other-to-other edges, as well as its sharp twin-edge deletion specialization. For instance, let \(H\) be *any* graph on \(k>0\) vertices. The two nonadjacent universal apices in the double cone over \(H\) have spectral distance \(\sqrt{2/k}\), independently of all edges of \(H\); adding the edge between the apices changes it to \(\sqrt{2/(k+2)}\). Prior complete-graph calculations cover only a highly symmetric choice of \(H\).

## Limitations

The theorem concerns **only equal-external-profile vertex pairs** and the adjacency-type real symmetric Dirac operator. Without that row condition the antisymmetric vector is not a universal lower-bound witness and the formula is not asserted. The result does not classify all distances of the ambient graph, characterize arbitrary edge deletion, or extend as stated to incidence-operator-based graph triples. Equivalently phrased results in older finite spectral geometry or matrix-norm literature remain a genuine residual priority risk; no search can establish uniqueness conclusively. No independent mathematical validation has been performed.

## References

1. P. Clare, C.-K. Li, E. Poon, E. Swartz, *Noncommutative Distances on Graphs: An Explicit Approach via Birkhoff-James Orthogonality*, arXiv:2409.04146v1 (first publicly posted 2024-09-06), https://arxiv.org/html/2409.04146v1.
2. F. Besnard, *Estimating noncommutative distances on graphs*, arXiv:2105.09056 (first publicly posted 2021-05-19), https://arxiv.org/abs/2105.09056.
3. B. Iochum, T. Krajewski, P. Martinetti, *Distances in finite spaces from noncommutative geometry*, arXiv:hep-th/9912217v1 (first publicly posted 1999-12-22), https://arxiv.org/html/hep-th/9912217v1.
