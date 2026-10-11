# Sharp width-variance extremizers among tree graphical zonotopes

## Finding

Let \(G=([n],E)\) be a connected simple graph on \(n\ge 3\) labeled vertices, let \(m=|E|\), and put \(d=n-1\). In the Euclidean hyperplane
\[
H=\left\{x\in\mathbb R^n:\sum_{i=1}^{n}x_i=0\right\},
\]
consider the centered graphical zonotope
\[
Z_G=\sum_{\{i,j\}\in E}
\left[-\frac{e_i-e_j}{2},\frac{e_i-e_j}{2}\right].
\]
Let \(U\) be uniform on the unit sphere of \(H\). Its directional width is \(W_G(U)=\max_{x\in Z_G}\langle x,U\rangle-\min_{x\in Z_G}\langle x,U\rangle\). Write
\[
q(G)=\sum_{v\in[n]}\binom{\deg_G(v)}2,
\quad
\delta=\frac13+\frac{2\sqrt3-4}{\pi}>0,
\quad
c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d+1)/2)}.
\]
Then the exact first two width moments are
\[
\mathbb E W_G=m\sqrt2\,c_d,
\qquad
\mathbb E W_G^2=\frac1d\left(2m+\frac8\pi\binom m2+2\delta q(G)\right).
\tag{1}
\]
Thus at fixed order and edge count, the directional width variance is a strictly increasing affine function of the number of pairs of incident edges.

For every tree \(T\) on \(n\ge4\) vertices, the path \(P_n\) is the unique variance minimizer and the star \(K_{1,n-1}\) is the unique maximizer, up to graph isomorphism:
\[
\operatorname{Var}(W_{P_n})\le\operatorname{Var}(W_T)
\le\operatorname{Var}(W_{K_{1,n-1}}),
\]
with equality in the respective bound exactly for that tree. The exact extremal gap is
\[
\operatorname{Var}(W_{K_{1,n-1}})-\operatorname{Var}(W_{P_n})
=\delta\frac{(n-2)(n-3)}{n-1}.
\tag{2}
\]
Although every such tree zonotope has the same face vector, Euclidean volume \(\sqrt n\), and mean directional width, its width variance distinguishes branching. The asymptotic contrast is sharp:
\[
\lim_{n\to\infty}\operatorname{Var}(W_{P_n})
=2+2\delta-\frac6\pi\approx0.415643841780765,
\qquad
\lim_{n\to\infty}\frac{\operatorname{Var}(W_{K_{1,n-1}})}n
=\delta\approx0.162751579441755.
\tag{3}
\]

## Assumptions and scope

Graphs are finite, undirected, simple, connected and unweighted; the Euclidean metric on \(H\) is inherited from \(\mathbb R^n\). The segment convention fixes generator length \(\sqrt2\); it is a translate of the standard graphical zonotope \(\sum_{\{i,j\}\in E}[e_i,e_j]\), so translations do not affect widths. Uniform orientation means normalized rotation-invariant surface measure on the \((n-2)\)-sphere of \(H\); the boundary cases \(n=3\) are covered by (1), while the strict, distinct tree extremizers require \(n\ge4\).

## Proof

**Zonotope width and spherical reduction.** Support functions add under Minkowski addition, so for every \(u\in H\) of unit norm,
\[
W_G(u)=\sum_{\{i,j\}\in E}|u_i-u_j|.
\tag{4}
\]
Take a standard centered Gaussian \(g\) in the \(d\)-dimensional space \(H\), and write \(g=RU\), where \(U\) is independent of \(R\), is uniform on the unit sphere of \(H\), and \(\mathbb E R^2=d\). For any homogeneous quadratic function of the absolute linear coordinates, its Gaussian expectation is \(d\) times its spherical expectation. Also
\[
\mathbb E|\langle e_i-e_j,U\rangle|=\sqrt2\,c_d
\tag{5}
\]
by the beta integral for a coordinate of a uniform sphere point. Summing (5) yields the first identity of (1).

**Exact pair kernel.** For two standard normal variables \(X,Y\) with correlation \(\rho\in[-1,1]\), polar integration in the plane of the generating independent Gaussians gives
\[
\mathbb E|XY|=\frac2\pi\left(\sqrt{1-\rho^2}+\rho\arcsin\rho\right).
\tag{6}
\]
For example, with \(\theta=\arccos\rho\), write \((X,Y)=(R_2\cos t,R_2\cos(t-\theta))\), where \(t\) is uniform and \(\mathbb E R_2^2=2\); then the integral of \(|\cos t\cos(t-\theta)|\) gives (6). For distinct edges \(e,f\), their root vectors \(e_i-e_j\) and \(e_k-e_\ell\) have norm \(\sqrt2\) each and inner product \(0\) if the edges are disjoint and \(\pm1\) if they share one endpoint. Hence the Gaussian correlations are respectively \(0\) and \(\pm1/2\). Applying (6) and dividing the homogeneous second moment by \(d\) gives
\[
\begin{array}{c|c}
\text{edge relation}&\mathbb E\bigl(|\langle e_i-e_j,U\rangle|\,|\langle e_k-e_\ell,U\rangle|\bigr)\\ \hline
 e=f&2/d\\
 e\ne f,\ e\cap f=\varnothing&4/(\pi d)\\
 e\ne f,\ |e\cap f|=1&(2\sqrt3/\pi+1/3)/d.
\end{array}
\tag{7}
\]
There are exactly \(q(G)=\sum_v\binom{\deg_G(v)}2\) unordered distinct edge pairs sharing a vertex and \(\binom m2-q(G)\) disjoint pairs. Expanding the square of (4), using (7), and collecting the pair correction \(\delta=(2\sqrt3/\pi+1/3)-4/\pi\) proves the second identity of (1). Positivity follows from \(\pi>3\) and \(4-2\sqrt3<1\).

**Sharp tree optimization.** For a tree, \(m=n-1\), so its mean in (1) is fixed and minimizing its variance is equivalent to minimizing \(q(T)\). Put \(a_v=\deg_T(v)-1\ge0\). The degree sum identity yields \(\sum_v a_v=n-2\), and
\[
q(T)=\sum_v\binom{a_v+1}2
=\frac12\sum_v(a_v^2+a_v).
\tag{8}
\]
Because the \(a_v\) are nonnegative integers, \(\sum_v a_v^2\ge\sum_v a_v=n-2\), with equality only if every \(a_v\in\{0,1\}\). A connected tree with all degrees at most \(2\) is a path, so \(q(T)\ge n-2\) with equality exactly for \(P_n\). Conversely, \(\sum a_v^2\le(\sum a_v)^2\), with equality exactly when all excess degree lies at one vertex; this gives \(q(T)\le\binom{n-1}{2}\), with equality exactly for the star. Substituting in (1) proves both rigidity claims and (2).

**Equal volume and asymptotics.** For a tree, the \(n\times(n-1)\) incidence matrix \(B\) has columns \(e_i-e_j\). Every maximal square minor obtained by deleting one row has absolute determinant \(1\), by leaf elimination. Cauchy–Binet therefore gives \(\det(B^{\mathsf T}B)=n\). Since the generating parameter cube \([-1/2,1/2]^{n-1}\) has volume \(1\), its image \(Z_T\) has Euclidean \((n-1)\)-volume \(\sqrt n\). Each tree has the face lattice of a cube, as also observed in the cited graphical-zonotope literature. Finally, with \(d=n-1\), the gamma-ratio expansion
\[
\frac{\Gamma(d/2)}{\Gamma((d+1)/2)}
=\sqrt{\frac2d}\left(1+\frac1{4d}+O(d^{-2})\right)
\]
gives \(2d^2c_d^2=4d/\pi+2/\pi+O(d^{-1})\). Inserting \(q(P_n)=d-1\) into (1), then using (2), proves both limits (3).

## Verification

The standalone, standard-library-only program `verify.py` reproduces the exact combinatorial edge-pair counts for all \(18{,}247\) labeled trees of orders \(3\) through \(7\), checks the sharp equality conditions, and independently evaluates the angular integral (6) by deterministic quadrature at correlations \(0,\pm1/2,1\). It also samples uniformly random spherical directions for four specified trees and one cyclic graph and compares empirical first/second width moments with (1). Finally, it checks the asymptotic formulas numerically at \(n=1001\). Invocation: `python3 verify.py`. Observed terminal marker: `VERIFY_OK`. The random samples, quadratures, and finite tree enumeration are diagnostic only; the proof above covers all orders and all connected simple graphs.

## Relationship to prior work

Grujić establishes the face-polynomial formula for graphical zonotopes and notes that every tree graphical zonotope is combinatorially a cube; his proof concerns face enumeration and graph matroids, not the Euclidean distribution of directional widths. Dall and Pfeifle develop graph and regular-matroid zonotope volumes through the matrix-tree theorem; their results account for the equal-volume phenomenon but not the variance gap (2). Padrol, Pilaud and Poullot study deformations and normal fans of graphical zonotopes; their structural results do not give the width-moment extremizers here. The absolute bivariate Gaussian moment (6) and degree-square extremality are standard ingredients; the claim is their precise geometric synthesis, in particular the sharp variance classification among combinatorially and volumetrically identical tree zonotopes.

## Limitations

The theorem concerns unweighted standard root generators, Euclidean spherical directional widths, and simple connected graphs. It does not assert stochastic dominance, a description of the complete width distribution, or the same extremizers under unequal edge weights or alternative norms. Direct overlap with unindexed earlier zonoid support-correlation or Gaussian graph-variation work cannot be excluded from the available literature searches. Numerical diagnostics do not certify the all-dimensional statement, which is proved analytically above.

## References

1. V. Grujić, *Counting faces of graphical zonotopes*, first public arXiv submission 23 April 2016, arXiv:1604.06931, https://arxiv.org/abs/1604.06931. Theorem 1.1, Sections 2 and 5.
2. A. Dall and J. Pfeifle, *A Polyhedral Proof of the Matrix Tree Theorem*, first public arXiv submission 15 April 2014, arXiv:1404.3876, https://arxiv.org/abs/1404.3876. Theorems 3 and 17 and graphical incidence-matrix analysis.
3. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, https://arxiv.org/abs/2111.12422. Graphical zonotope definitions and deformation structure.
