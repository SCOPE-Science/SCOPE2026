# Exact Hilbert-snowflake thresholds for generalized theta graphs with one three-edge branch

## Finding
For each integer \(m\ge3\), let \(G_m\) consist of two poles joined by \(m\) internally disjoint paths of length two and one internally disjoint path of length three, all with unit edges. Set
\[
 t_m=\frac{3m+2+\sqrt{29m^2+92m+4}}{2(m+4)},\qquad
 p_m=\log_2\frac{t_m}{t_m-1}.
\]
The supremal negative-type exponent of the shortest-path metric of \(G_m\) is exactly \(p_m\): the metric has strict \(p\)-negative type for \(0\le p<p_m\), nonstrict \(p_m\)-negative type, and fails \(p\)-negative type for all \(p>p_m\). The zero-sum equality space at the endpoint is one-dimensional. Consequently, the minimum affine dimension of a real Hilbert-space isometric realization of \(d^{p/2}\) is \(m+3\) for \(0<p<p_m\), and \(m+2\) at \(p=p_m\).

The exponents decrease strictly with \(m\), and
\[
 p_m=p_\infty+\frac{4T-2}{\sqrt{29}\,(T-1)\log2}\,\frac1m+O(m^{-2}),\qquad
 T=\frac{3+\sqrt{29}}2,\quad
 p_\infty=\log_2\frac{3+\sqrt{29}}{1+\sqrt{29}}=0.3931152819448\ldots.
\]
In particular, all \(G_m\) with \(m\ge3\) fail ordinary \(1\)-negative type, although they admit the precise nonzero range of smaller exponents stated above. For comparison, the same closed formula extends algebraically to the boundary cases \(m=1\) (the known five-cycle) and \(m=2\) (the known three-path theta graph); these boundary cases are not asserted to be new.

## Assumptions and scope
The vertex set is \(\{u,v,a,b,x_1,\ldots,x_m\}\), with exactly the edges \(ux_j\), \(vx_j\) for \(1\le j\le m\), and \(ua\), \(ab\), \(bv\). There are \(m+4\) vertices. For every pair of distinct vertices the path distance is either one (for adjacent vertices) or two (for nonadjacent vertices): this follows from the explicit common-neighbor paths, including \(d(u,v)=2\), \(d(u,b)=d(v,a)=2\), and \(d(a,x_j)=d(b,x_j)=2\). In particular the diameter is exactly two.

For \(p\ge0\), write \(D_p=(d(i,j)^p)_{i,j}\) with diagonal entries zero. The metric has \(p\)-negative type exactly when \(z^{\mathsf T}D_pz\le0\) for every real vector \(z\) satisfying \(\sum_i z_i=0\); it has strict negative type when equality is possible only for \(z=0\). At \(p=0\), all off-diagonal entries are defined to be one. All embedding dimensions refer to the affine dimension of a real Euclidean or Hilbert isometric embedding of the metric \(d^{p/2}\).

## Proof
Let \(A\) be the \((m+4)\)-by-\((m+4)\) adjacency matrix, \(J\) the all-ones matrix, and \(q=2^p\). Because every off-diagonal distance is either one or two, the **complete** powered-distance matrix is
\[
 D_p=q(J-I)+(1-q)A.
\]
Thus on the zero-sum subspace \(H=\{z:\sum_i z_i=0\}\),
\[
 z^{\mathsf T}D_pz=-q\|z\|_2^2-(q-1)z^{\mathsf T}Az.
\]
It remains to find the least Rayleigh quotient of \(A\) on \(H\). The following mutually orthogonal decomposition exhausts \(H\).

First, the \((m-1)\)-dimensional middle-vertex contrast space, supported on \(x_1,\ldots,x_m\) with coefficient sum zero, has adjacency eigenvalue zero. Second, on the two-dimensional antisymmetric space \((z_u,z_v,z_a,z_b)=(U,-U,V,-V)\), with all middle coefficients zero, adjacency acts as \(\begin{pmatrix}0&1\\1&-1\end{pmatrix}\); its eigenvalues are \((-1\pm\sqrt5)/2\). Its least eigenvalue is \(-\varphi\), where \(\varphi=(1+\sqrt5)/2\).

Finally, the remaining two-dimensional zero-sum space consists of vectors with common pole coefficient \(U\), common three-edge-path interior coefficient \(V\), and common middle coefficient \(X\). The zero-sum condition gives \(X=-2(U+V)/m\). Directly summing all graph-edge contributions yields
\[
 z^{\mathsf T}Az=-8U^2-4UV+2V^2,
 \qquad \|z\|_2^2=2U^2+2V^2+\frac4m(U+V)^2.
\]
Accordingly, the two generalized adjacency eigenvalues in this sector are the roots of
\[
 \det\left(
 \begin{pmatrix}-8&-2\\-2&2\end{pmatrix}
 -\lambda\begin{pmatrix}2+4/m&4/m\\4/m&2+4/m\end{pmatrix}
 \right)=0,
\]
which reduces without omitted factors to
\[
 (m+4)\lambda^2+(3m+2)\lambda-5m=0.
\]
The smaller root is \(-t_m\). Let \(T=(3+\sqrt{29})/2\), the positive root of \(t^2-3t-5=0\). The polynomial \(F_m(t)=(m+4)t^2-(3m+2)t-5m\) satisfies \(F_m(0)<0\) and \(F_m(T)=4T^2-2T>0\), so \(0<t_m<T\). Differentiating \(F_m(t_m)=0\) with respect to real \(m>0\) gives
\[
 \frac{dt_m}{dm}=
 \frac{5+3t_m-t_m^2}{2(m+4)t_m-(3m+2)}>0,
\]
since \(t_m<T\) and the denominator is the positive derivative of \(F_m\) at its positive root. At \(m=1\) one has \(t_1=\varphi\). Hence \(t_m>\varphi>1\) for all \(m\ge2\). Moreover, \(F_m(2)=12-7m<0\) for \(m\ge2\), so \(t_m>2\) and \(p_m<1\) in that regime. Thus the least Rayleigh quotient on all of \(H\) is uniquely \(-t_m\) for every \(m\ge3\). Its equality space is one-dimensional.

For a unit vector in \(H\) with adjacency Rayleigh quotient \(\lambda\ge-t_m\), the powered-distance quadratic form is \(-q-(q-1)\lambda\), largest when \(\lambda=-t_m\) for \(q>1\). The maximum is \((t_m-1)q-t_m\). This is negative for \(1\le q<t_m/(t_m-1)\), zero at equality, and positive beyond it. Because \(q=2^p\) increases strictly with \(p\), this proves the complete sharp negative-type classification including all exponents above the endpoint. At \(p=0\), \(D_0=J-I\) is strictly conditionally negative.

For \(0<p\le p_m\), the centered Gram matrix \(-\tfrac12 P D_p P\), \(P=I-J/(m+4)\), is positive semidefinite. By the Euclidean distance-matrix correspondence, its rank equals the minimum affine Hilbert dimension of an isometric embedding of \(d^{p/2}\). The rank is \(m+3\) below the endpoint and \(m+2\) at the endpoint, because the zero-sum kernel has dimension exactly one there.

The strict increase of \(t_m\) implies strict decrease of \(p_m\), since \(t\mapsto\log_2(t/(t-1))\) strictly decreases for \(t>1\). To obtain the asymptotic, rewrite \(F_m(t)=m(t^2-3t-5)+(4t^2-2t)\). The simple root at \(T\) and the implicit-function theorem give
\[
 t_m=T-\frac{4T^2-2T}{\sqrt{29}\,m}+O(m^{-2}).
\]
Taylor-expanding \(\log_2(t/(t-1))\) at \(T\) yields the stated positive coefficient and limit. No numerical extrapolation is used to prove either limit or error term.

## Verification
`check.py` is a self-contained Python 3 standard-library program. It separately constructs the graph adjacency list and recovers all shortest-path distances by breadth-first search. A Jacobi eigenvalue routine applied to the centered adjacency and powered-distance matrices checks the predicted least eigenvalue, endpoint nullity, strict subcritical negativity, and failure beyond the threshold for \(m=1,\ldots,18,22,29,40\). It also compares the analytic large-\(m\) coefficient against \(m=100,1000,10000\). Invoke `python3 check.py` from the directory containing that file; successful output ends with `CHECK_OK`. These are finite floating-point tests only; the infinite-dimensional parameter quantifiers follow from the preceding exact decomposition and inequalities.

Independent boundary checks corroborate the algebra: at \(m=1\), \(G_1=C_5\) and the ordinary quadratic embedding constant is \(-2/(3+\sqrt5)\), exactly \(t_1-2\); at \(m=2\), the known graph \(\Theta(2,2,3)\) has ordinary quadratic embedding constant \((\sqrt{19}-4)/3\), exactly \(t_2-2\). Both values appear in the primary sources cited below.

## Relationship to prior work
Obata and Zakiyyah (2018) determine the ordinary quadratic embedding constant of \(C_5\) and classify graphs of order at most five. Młotkowski, Skrzypczyk and Wojtylak (arXiv:2409.17662, first posted September 26, 2024) investigate **three-path** theta graphs and give the ordinary quadratic embedding constant of \(\Theta(2,2,3)\) in their Example 7.2. Those are the \(m=1\) and \(m=2\) boundary checks here, not novel claims. The present generalized theta family has at least **four** internally disjoint pole-to-pole paths when \(m\ge3\); the cited three-path results and the known single exponent-one constants do not supply the explicit all-\(m\) powered-distance threshold, its endpoint Hilbert dimensions, or its sharp large-\(m\) limit.

The general fact that negative type of a diameter-two metric can be tested by an adjacency quadratic form is an elementary reduction, used openly in the proof. The substantive family-specific calculation is the exact least *zero-sum* adjacency eigenvalue, its strict dominance over the competing mode for all \(m\ge3\), and the resulting complete parameter-dependent Hilbert classification. No general novelty or independent validation beyond the stated comparisons is asserted.

## Limitations
The theorem covers only unweighted finite generalized theta graphs with exactly one length-three path and at least three length-two paths, with no other edges. It does not classify arbitrary generalized theta path-length vectors or weighted variants. Earlier equivalent work could exist under a different graph-family name or spectral formulation. The numerical checker is not an infinite proof and the scientific assessment is not an independent peer review.

## References
1. W. Młotkowski, M. Skrzypczyk and M. Wojtylak, *On quadratic embeddability of bipartite graphs and theta graphs*, arXiv:2409.17662 (initial version September 26, 2024), especially Definition 4.1 and Example 7.2. https://arxiv.org/abs/2409.17662
2. N. Obata and A. Y. Zakiyyah, *Distance matrices and quadratic embedding of graphs*, Electronic Journal of Graph Theory and Applications **6** (2018), 37–60, especially the five-vertex table. https://doi.org/10.5614/ejgta.2018.6.1.4
3. I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society **44** (1938), 522–536. https://doi.org/10.1090/S0002-9947-1938-1501980-0
