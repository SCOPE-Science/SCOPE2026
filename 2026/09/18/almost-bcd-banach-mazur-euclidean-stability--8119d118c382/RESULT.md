# Banach--Mazur Euclidean stability from almost barycenter curvature--dimension

## Statement

Let \((X,d,\mathfrak m)\) be a complete separable geodesic metric-measure space that is locally doubling, supports a local weak \((1,1)\)-Poincare inequality, and satisfies the additive-error barycenter curvature--dimension condition \(\mathrm{BCD}_{\delta}(K,\infty)\). At almost every point \(x\), let \(T_x^*X\) be the finite-dimensional cotangent norm appearing in the differentiability structure, and put \(m(x)=\dim T_x^*X\).

For each fixed integer \(m\ge 2\), set
\[
\beta_m=18m^2-17m+14.
\]
Then, as \(\delta\downarrow0\), at almost every point with \(m(x)=m\),
\[
\boxed{
 d_{\rm BM}(T_x^*X,\ell_2^m)
 \le 1+8\beta_m\sqrt\delta+O_m(\delta).
}
\]
In particular, if the cotangent dimensions are essentially bounded by \(N\), then the measurable cotangent norms are uniformly \(1+O_N(\sqrt\delta)\) Banach--Mazur close to Euclidean spaces.

For a finite-dimensional normed space \((\mathbb R^n,F)\), if \((\mathbb R^n,F,\mathcal L^n)\) satisfies \(\mathrm{BCD}_{\delta}(0,\infty)\), then
\[
\boxed{
 d_{\rm BM}((\mathbb R^n,F),\ell_2^n)
 \le 1+8(18n^2-17n+14)\sqrt\delta+O_n(\delta).
}
\]
The same statement holds with the optimal BCD error \(\Delta_{\rm BCD}(F)\) in place of \(\delta\).

In dimension two there is a non-asymptotic form. Put \(\eta=8\sqrt\delta\). Whenever
\[
15\eta+\frac{27}{2}\eta^2<1,
\]
one has
\[
\boxed{
 d_{\rm BM}((\mathbb R^2,F),\ell_2^2)
 \le
 \sqrt{\frac{1+15\eta+\frac{27}{2}\eta^2}
 {1-15\eta-\frac{27}{2}\eta^2}}
 =
 \sqrt{\frac{1+120\sqrt\delta+864\delta}
 {1-120\sqrt\delta-864\delta}}.
}
\]

The exponent \(1/2\) is sharp in fixed dimension. For every smooth nonquadratic even perturbation used by Han--Liu,
\[
F_\tau(v)^2=|v|^2+\tau H(v),
\]
with \(H\) two-homogeneous and not a quadratic form, one has
\[
\Delta_{\rm BCD}(F_\tau)\asymp_H \tau^2
\quad\text{and}\quad
 d_{\rm BM}(F_\tau,\ell_2^n)-1\asymp_H |\tau|.
\]
Consequently
\[
\boxed{
 d_{\rm BM}(F_\tau,\ell_2^n)-1
 \asymp_H \sqrt{\Delta_{\rm BCD}(F_\tau)}.
}
\]
Thus no estimate with a uniformly better power of the BCD error can hold, even among smooth strongly convex Minkowski norms near a Euclidean norm.

## Proof

Han and Liu prove that \(\mathrm{BCD}_{\delta}(K,\infty)\), together with local doubling and a local weak Poincare inequality, implies the normalized parallelogram-defect estimate
\[
\mathfrak p_{\rm par}(T_x^*X)\le 8\sqrt\delta
\]
for almost every \(x\). For a finite-dimensional norm \(\|\cdot\|\), write
\[
R(u,v)=
\frac{\|u+v\|^2+\|u-v\|^2}
{2\|u\|^2+2\|v\|^2}.
\]
The denominator is at least every term appearing in the normalizing maximum in \(\mathfrak p_{\rm par}\). Hence
\[
|R(u,v)-1|\le \mathfrak p_{\rm par}.
\]
The change of variables
\[
(u,v)\longmapsto \left(\frac{u+v}{2},\frac{u-v}{2}\right)
\]
replaces \(R\) by \(1/R\). It follows that the symmetric von Neumann--Jordan constant \(C_{\rm NJ}\) satisfies
\[
C_{\rm NJ}(T_x^*X)\le 1+8\sqrt\delta.
\]

Passer's quantitative Jordan--von Neumann theorem says that an \(m\)-dimensional real normed space with \(C_{\rm NJ}=1+\varepsilon\) satisfies
\[
d_{\rm BM}(E,\ell_2^m)
\le 1+\beta_m\varepsilon+O_m(\varepsilon^2),
\qquad
\beta_m=18m^2-17m+14.
\]
Substituting \(\varepsilon\le8\sqrt\delta\) gives the first displayed Banach--Mazur estimate. For a normed space \((\mathbb R^n,F)\), Han--Liu's cotangent norm is the dual norm \(F^*\). Finite-dimensional Banach--Mazur distance is invariant under duality, because an isomorphism and its adjoint have the same operator norm and inverse norm. Therefore
\[
d_{\rm BM}(F,\ell_2^n)=d_{\rm BM}(F^*,\ell_2^n),
\]
which proves the normed-space assertion. If \(\Delta_{\rm BCD}(F)\) is defined as the infimum of admissible errors, apply the estimate to admissible \(\delta\) decreasing to \(\Delta_{\rm BCD}(F)\) and pass to the limit.

For \(m=2\), Passer proves the explicit estimate
\[
d_{\rm BM}(E,\ell_2^2)
\le
\sqrt{\frac{1+15\varepsilon+\frac{27}{2}\varepsilon^2}
{1-15\varepsilon-\frac{27}{2}\varepsilon^2}}
\]
when the denominator is positive. The right-hand side is increasing for small nonnegative \(\varepsilon\). Taking \(\varepsilon\le\eta=8\sqrt\delta\) gives the stated two-dimensional formula.

It remains to justify sharpness of the exponent. Two elementary comparisons are useful. For every finite-dimensional normed space \(E\),
\[
C_{\rm NJ}(E)\le d_{\rm BM}(E,\ell_2^{\dim E})^2.
\]
Indeed, if after a linear identification with Euclidean space one has
\(|z|\le\|z\|\le D|z|\), then the numerator in \(R\) is at most \(D^2\) times its Euclidean value, while the denominator is at least its Euclidean value, so \(R\le D^2\); take the supremum and then the infimum over \(D\).

There is also the lower comparison
\[
C_{\rm NJ}(E)-1\ge \frac12\mathfrak p_{\rm par}(E).
\]
To see this, write
\[
A=\|u+v\|^2+\|u-v\|^2,
\qquad
B=2\|u\|^2+2\|v\|^2,
\]
and let \(M\) be the maximum used in the definition of \(\mathfrak p_{\rm par}\). The triangle inequality gives \(M\le B\), while the two entries \(2\|u\|^2\) and \(2\|v\|^2\) give \(M\ge B/2\). Hence
\[
\left|\frac AB-1\right|
\ge \frac12\frac{|A-B|}{M}.
\]
If \(A/B<1\), the above linear change of variables realizes its reciprocal as another parallelogram ratio. Taking suprema proves the claim.

For Han--Liu's perturbations they prove, with a positive quantity \(\mathcal Q(H)\) whenever \(H\) is nonquadratic,
\[
\mathfrak p_{\rm par}(F_\tau^*)
\ge \frac12\mathcal Q(H)|\tau|
\]
for sufficiently small \(|\tau|\), and also
\[
\Delta_{\rm BCD}(F_\tau)\asymp_H\tau^2.
\]
The preceding inequalities and duality therefore give
\[
d_{\rm BM}(F_\tau,\ell_2^n)^2
\ge 1+\frac14\mathcal Q(H)|\tau|,
\]
so
\[
d_{\rm BM}(F_\tau,\ell_2^n)-1
\ge \frac18\mathcal Q(H)|\tau|+O_H(\tau^2).
\]
The reverse bound \(d_{\rm BM}-1=O_H(|\tau|)\) is immediate from
\(F_\tau(v)^2=|v|^2(1+\tau\psi(v/|v|))\) and the identity linear map. This proves the sharp square-root scale.

## Context and originality

Han--Liu introduced the additive-error condition \(\mathrm{BCD}_{\delta}\) and proved the sharp \(8\sqrt\delta\) control of cotangent parallelogram defect, together with the quadratic BCD-error scale for non-Riemannian perturbations. Their paper does not formulate Banach--Mazur estimates or ellipsoidal closeness of tangent unit balls.

Passer proved the independent quantitative Jordan--von Neumann theorem converting a small von Neumann--Jordan constant into Banach--Mazur closeness to Euclidean space. Combining the sharp BCD-to-parallelogram estimate with that theorem gives a global affine-invariant geometric consequence not present in either source: small barycentric entropy error forces almost-everywhere Euclidean cotangent balls in Banach--Mazur distance, with a square-root rate, and that rate is optimal.

## Limitations

The coefficient \(8(18m^2-17m+14)\) is inherited from Han--Liu's parallelogram estimate and Passer's general finite-dimensional stability theorem; it is not claimed optimal, especially in its dependence on dimension. Except in dimension two, the displayed upper bound is asymptotic as \(\delta\to0\). The result controls the Banach--Mazur geometry of finite-dimensional cotangent fibers, not a global Gromov--Hausdorff or bi-Lipschitz distance from the ambient metric-measure space to a Riemannian space. The motivating preprint was submitted on 17 September 2026, so unindexed parallel work remains a residual originality risk.

## References

1. B.-X. Han and D.-Y. Liu, *On the Geometry of Wasserstein Barycenter II: Riemannian Rigidity, Essential Non-Branching, and Finsler Models*, arXiv:2609.19564v1 (2026). https://arxiv.org/abs/2609.19564
2. B. Passer, *An Approximate Version of the Jordan von Neumann Theorem for Finite Dimensional Real Normed Spaces*, Linear and Multilinear Algebra 63 (2015), 68--77; arXiv:1305.3546. https://arxiv.org/abs/1305.3546
