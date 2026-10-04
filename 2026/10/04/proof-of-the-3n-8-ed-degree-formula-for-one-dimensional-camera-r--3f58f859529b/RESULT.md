# Proof of the \(3n-8\) ED-degree formula for one-dimensional camera resectioning
## Finding
For every \(n\ge 4\), let \(X_1,\ldots,X_n\in\mathbb P^1\) be generic distinct world points. Then the affine one-dimensional resectioning variety of Duff--Rydell satisfies
\[
\operatorname{EDD}(\mathcal R_n^{1,1})=3n-8.
\]
This proves item 1 of their Conjecture 7.5. Equivalently, a generic Möbius-alignment problem on \(n\) point pairs has exactly \(3n-8\) complex critical points whose image tuples lie in the smooth resectioning stratum.

## Assumptions and scope
Work over \(\mathbb C\) and use the conventional affine output chart in each \(\mathbb P^1\) factor. The world points and the Euclidean data point are generic. Choose an affine coordinate in the world line avoiding all \(X_i\), and write the distinct coordinates as \(z_i\). A camera in the chart \(d=1\) acts by
\[
g_i=\frac{a z_i+b}{c z_i+1}.
\]
The point \(c=\infty\) supplies the complementary camera chart, so the final one-variable count is projective. All exclusions below (vanishing denominators, a singular normal-equation matrix, degree drops, multiple roots, or coincidences between exceptional sets) are proper algebraic conditions and therefore absent for generic inputs.

## Proof
Put \(s_i=1+c z_i\), \(t_i=a z_i+b\), and \(r_i=t_i-u_i s_i\), where \(u_i\) is the affine data coordinate. The squared objective is
\[
\Phi(a,b,c)=\sum_{i=1}^n\frac{r_i^2}{s_i^2}.
\]
For fixed \(c\), its first two critical equations are the weighted least-squares normal equations
\[
F_0=\sum_i\frac{r_i}{s_i^2}=0,\qquad
F_1=\sum_i\frac{z_i r_i}{s_i^2}=0.
\]
For generic \(c\) they determine a unique pair \(a(c),b(c)\). Let \(\phi(c)=\Phi(a(c),b(c),c)\).

Set \(P(c)=\prod_i s_i\). By the Schur-complement formula for a weighted least-squares residual and Cauchy--Binet,
\[
\phi(c)=\frac{N(c)}{D(c)},
\]
where
\[
D(c)=\sum_{i<j}(z_i-z_j)^2\prod_{k\ne i,j}s_k^2
\]
and
\[
N(c)=\sum_{i<j<k}L_{ijk}(c)^2\prod_{\ell\ne i,j,k}s_\ell^2,
\qquad
L_{ijk}(c)=\det\begin{pmatrix}
1&z_i&u_i s_i\\
1&z_j&u_j s_j\\
1&z_k&u_k s_k
\end{pmatrix}.
\]
A useful identity, obtained from \(z_i=(s_i-1)/c\), is
\[
D=(n-1)(P')^2-nPP''.
\]
Both \(N\) and \(D\) have generic degree \(2n-4\). For example, with distinct positive real \(z_i\), the leading coefficient of \(D\) is a positive sum
\[
\sum_{i<j}(z_i-z_j)^2\prod_{k\ne i,j}z_k^2,
\]
and the leading coefficient of \(N\) is nonzero for generic data. The two polynomials are generically coprime: at a root of \(D\), the \(2\times2\) weighted normal matrix has rank one for generic world points, while the bordered \(3\times3\) Gram determinant defining \(N\) is not identically zero as the response vector varies. Hence \(\phi:\mathbb P^1\to\mathbb P^1\) has degree
\[
m=2n-4.
\]
Riemann--Hurwitz therefore gives total ramification degree
\[
2m-2=4n-10.
\]

It remains to remove ramification points whose cameras map to the singular stratum. In the chart \(d=1\), a camera has rank one exactly when \(a=bc\). Then \(t_i=b s_i\), so its image tuple is constant. At such a point the two normal equations become
\[
\sum_i\frac{b-u_i}{s_i}=0,\qquad
\sum_i\frac{z_i(b-u_i)}{s_i}=0.
\]
For \(c\ne0\), the identity \(z_i/s_i=c^{-1}(1-s_i^{-1})\) shows that these equations force
\[
b=\bar u:=\frac1n\sum_i u_i.
\]
Thus the rank-one critical parameters are the zeros, away from the generic exceptional set, of
\[
H(c)=\sum_i(\bar u-u_i)\frac{P(c)}{s_i}.
\]
Since \(\sum_i(\bar u-u_i)=0\), one has \(H(0)=0\), and the relevant polynomial is \(S(c)=H(c)/c\). The polynomials \(P/s_i\) form a Lagrange basis of the polynomials of degree at most \(n-1\). Consequently the map from zero-sum vectors \((v_i)\) to \(c^{-1}\sum_i v_iP/s_i\) is an isomorphism onto the polynomials of degree at most \(n-2\). Therefore, for generic data, \(S\) has degree \(n-2\), has simple roots, and avoids the chart boundaries.

The third critical equation is
\[
F_2=\sum_i\frac{z_i t_i r_i}{s_i^3}=0
\]
(up to the harmless overall sign coming from differentiating with respect to \(c\)). Write \(R=a-bc\). Since \(t_i=b s_i+Rz_i\), the equation \(F_1=0\) gives the exact factorization
\[
F_2=R\sum_i\frac{z_i^2r_i}{s_i^3}.
\]
Hence every zero of \(S\) is a ramification point of the reduced objective. At a rank-one point, the second factor becomes \(\sum_i z_i^2(b-u_i)/s_i^2\). Its vanishing imposes an additional independent linear condition on the data: the vector \((z_i^2/s_i^2)_i\) does not lie in the span of \((1)_i\) and \((1/s_i)_i\) for distinct \(z_i\). Thus these \(n-2\) ramification points are generically simple.

Duff--Rydell prove that the singular locus of \(\mathcal R_n^{1,1}\) is exactly the diagonal rank-one image stratum, while its complementary stratum is isomorphic to \(\operatorname{PGL}_2\). Therefore the \(n-2\) rank-one ramification points are precisely the parameter critical points that must be discarded from the ED count. All remaining ramification points correspond bijectively to smooth ED-critical image tuples. Hence
\[
\operatorname{EDD}(\mathcal R_n^{1,1})=(4n-10)-(n-2)=3n-8.
\]

## Verification
The accompanying `verify.py` reconstructs \(N,D,H,S\) exactly over the rationals for deterministic specializations with \(4\le n\le8\). It checks the Cauchy--Binet denominator identity, \(\deg N=\deg D=2n-4\), coprimality of \(N,D\), \(\deg(N'D-ND')=4n-10\), exact divisibility by the rank-one factor \(S\), and quotient degree \(3n-8\). It also checks squarefreeness and separation in those test cases. These computations are finite consistency checks; the uniform proof above does not infer the theorem from the finite tests.

## Relationship to prior work
Duff and Rydell introduced these resectioning varieties, proved that for \(n\ge4\) the singular locus of \(\mathcal R_n^{1,1}\) is the diagonal rank-one stratum, identified the smooth stratum with \(\operatorname{PGL}_2\), and stated \(\operatorname{EDD}(\mathcal R_n^{1,1})=3n-8\) as Conjecture 7.5(1), supported by computation. Finkel and Rodriguez later proved general ED-degree formulas for rational curves and resolved the one-dimensional line-multiview conjectures from the same catalogue; their stated scope is multiview varieties of rational curves and does not include the three-dimensional resectioning variety treated here.

## Limitations
The statement is for generic distinct world points and a generic Euclidean data point in the conventional affine chart. It does not give ED degrees for nongeneric configurations, other resectioning dimensions, or other choices of metric. The proof uses characteristic zero and the complex critical-point count underlying Euclidean distance degree.

## References
1. Timothy Duff and Felix Rydell, *Metric Multiview Geometry—A Catalogue in Low Dimensions*, arXiv:2402.00648v1, 2024. See Theorem 6.6, Proposition 6.7, and Conjecture 7.5.
2. Bella Finkel and Jose Israel Rodriguez, *The Euclidean distance degree of curves: from rational to line multiview varieties*, arXiv:2512.18521v1, 2025.
