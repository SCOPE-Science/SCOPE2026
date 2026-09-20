# Area-balanced Schwarz lanterns and cubic integer area accuracy

## Result

Consider a right circular cylinder of radius \(R>0\) and height \(H>0\).
For integers \(n\ge 3\) and \(m\ge 1\), form the standard Schwarz lantern
with \(n\) equally spaced vertices on each horizontal ring, \(m\) axial
bands, and a half-step angular offset between adjacent rings. Its
\(2mn\) congruent triangular faces have total lateral area
\[
A_{m,n}
=
2mnR\sin\!\frac{\pi}{n}\,
\sqrt{\left(\frac{H}{m}\right)^2+
R^2\left(1-\cos\!\frac{\pi}{n}\right)^2}.
\tag{1}
\]
The cylinder has lateral area \(A_0=2\pi RH\).

Write
\[
x=\frac{\pi}{n},\qquad \rho=\frac RH,\qquad
Q_{m,n}=\frac{A_{m,n}}{A_0}.
\]
Then
\[
Q_{m,n}
=
\frac{\sin x}{x}
\sqrt{1+\rho^2m^2(1-\cos x)^2}.
\tag{2}
\]

### 1. Exact finite-\(n\) area-balance threshold

For each fixed \(n\ge3\), the continuous relaxation \(m>0\mapsto Q_{m,n}\)
is strictly increasing. There is a unique positive real band count
\[
\boxed{
m_*(n)=
\frac{H}{R(1-\cos(\pi/n))}
\sqrt{
\left(\frac{\pi/n}{\sin(\pi/n)}\right)^2-1
}
}
\tag{3}
\]
for which \(A_{m_*(n),n}=A_0\). Consequently,
\[
m<m_*(n)\Longrightarrow A_{m,n}<A_0,\qquad
m>m_*(n)\Longrightarrow A_{m,n}>A_0.
\tag{4}
\]
Thus the same classical lantern family contains a unique finite-resolution
transition from area underestimation to area overestimation.

The exact threshold has the expansion
\[
\boxed{
m_*(n)=
\frac{2H}{\sqrt3\,\pi R}\,n
+
\frac{11\sqrt3\,\pi H}{90R}\,\frac1n
+
\frac{589\sqrt3\,\pi^3H}{37800R}\,\frac1{n^3}
+
O(n^{-5}).
}
\tag{5}
\]

### 2. Unique balanced linear aspect ratio

Suppose \(m_n/n\to c\in(0,\infty)\). Then
\[
\boxed{
Q_{m_n,n}
=
1+
\left(
\frac{\pi^4R^2c^2}{8H^2}
-\frac{\pi^2}{6}
\right)n^{-2}
+o(n^{-2}).
}
\tag{6}
\]
Hence there is a unique positive linear aspect ratio that cancels the
generic \(n^{-2}\) area bias:
\[
\boxed{
c_*=\frac{2H}{\sqrt3\,\pi R}.
}
\tag{7}
\]
For every fixed \(c<c_*\), the linear family \(m_n\sim cn\) eventually
underestimates the cylinder area; for every fixed \(c>c_*\), it eventually
overestimates it.

If the real relaxation is taken exactly at \(m=c_*n\), the cancellation is
two orders stronger:
\[
\boxed{
Q_{c_*n,n}
=
1-\frac{11\pi^4}{180}\,n^{-4}
+O(n^{-6}).
}
\tag{8}
\]
Thus the distinguished linear shape parameter is not merely one of the
many regimes satisfying the classical convergence condition
\(m/n^2\to0\); it is the unique linear regime with vanishing quadratic
area bias.

### 3. Integer balancing gives cubic relative area error

Let \(\widehat m_n\) be a nearest integer to \(m_*(n)\), and put
\(\delta_n=\widehat m_n-m_*(n)\), so \(|\delta_n|\le1/2\). Then, uniformly
for this bounded rounding error,
\[
\boxed{
Q_{\widehat m_n,n}-1
=
\frac{\pi^3R}{2\sqrt3\,H}\,
\delta_n\,n^{-3}
+
\frac{\pi^4R^2}{8H^2}\,
\delta_n^2\,n^{-4}
+
O(n^{-5}).
}
\tag{9}
\]
In particular,
\[
\boxed{
\left|Q_{\widehat m_n,n}-1\right|
\le
\frac{\pi^3R}{4\sqrt3\,H}\,n^{-3}
+O(n^{-4}).
}
\tag{10}
\]
Since the number of triangular faces is \(F_n=2n\widehat m_n=\Theta(n^2)\),
this gives relative area error \(O(F_n^{-3/2})\). By contrast, a fixed
linear aspect ratio \(c\ne c_*\) has relative area error
\(\Theta(n^{-2})=\Theta(F_n^{-1})\).

## Proof

Equation (1) is the standard exact area formula for the Schwarz lantern.
Dividing by \(2\pi RH\) gives (2). For fixed \(x\in(0,\pi/2)\), every
factor in (2) is positive and
\[
\frac{\partial Q}{\partial m}
=
\frac{\sin x}{x}\,
\frac{\rho^2m(1-\cos x)^2}
{\sqrt{1+\rho^2m^2(1-\cos x)^2}}>0.
\]
Moreover,
\[
\lim_{m\downarrow0}Q_{m,n}=\frac{\sin x}{x}<1,\qquad
\lim_{m\to\infty}Q_{m,n}=\infty.
\]
There is therefore exactly one real \(m\) at which \(Q=1\). Solving
(2) algebraically gives (3), and monotonicity gives (4).

For (5), expand the dimensionless factor in (3):
\[
\frac{1}{1-\cos x}
\sqrt{\left(\frac{x}{\sin x}\right)^2-1}
=
\frac{2}{\sqrt3\,x}
+\frac{11\sqrt3}{90}x
+\frac{589\sqrt3}{37800}x^3
+O(x^5).
\]
Substitution \(x=\pi/n\) proves (5).

For \(m_n/n\to c\), use
\[
\frac{\sin x}{x}=1-\frac{x^2}{6}+O(x^4),
\qquad
(1-\cos x)^2=\frac{x^4}{4}+O(x^6),
\]
in (2). Since \(m_n^2x^4=c^2\pi^4n^{-2}+o(n^{-2})\),
\[
\sqrt{1+\rho^2m_n^2(1-\cos x)^2}
=
1+\frac{\rho^2c^2\pi^4}{8}n^{-2}+o(n^{-2}),
\]
which yields (6). Its quadratic coefficient vanishes at exactly (7).
Expanding (2) with \(m=c_*n\) two orders further gives
\[
Q_{c_*n,n}
=
1-\frac{11\pi^4}{180}n^{-4}
+\frac{173\pi^6}{10080}n^{-6}
+O(n^{-8}),
\]
and hence (8).

Finally write \(m=m_*(n)+\delta\), with \(\delta\) bounded. Substituting
the expansion (5) into (2) and expanding at \(n=\infty\) gives, uniformly
for bounded \(\delta\),
\[
Q_{m_*(n)+\delta,n}-1
=
\frac{\pi^3R}{2\sqrt3\,H}\delta n^{-3}
+\frac{\pi^4R^2}{8H^2}\delta^2n^{-4}
-\frac{19\sqrt3\,\pi^5R}{360H}\delta n^{-5}
+O(n^{-6}).
\]
Taking \(\delta=\delta_n\) proves (9) and (10). The face-count statement
follows from \(\widehat m_n\sim c_*n\). \(\square\)

## Context and originality boundary

The Schwarz lantern is the classical counterexample showing that inscribed
polyhedral surfaces can converge geometrically to a smooth surface while
their areas fail to converge. Kobayashi and Tsuchiya (2017) use the
lantern in their study of surface-area approximation by triangulations,
record the exact formula (1), and recover the classical criterion
\(m/n^2\to0\) for convergence of the lantern area to \(2\pi RH\).
Modern work continues to use the lantern as a stress test. Brewin (2015)
derived error bounds for the ordinary lantern and then obtained a fourth-order
estimate after replacing Euclidean edge lengths by curvature-corrected ones;
that changes the area estimator rather than tuning the ordinary lantern.
Lachaud--Romon--Thibert--Coeurjolly (2020) likewise use difficult polygonal
meshes to motivate corrected curvature measures.

The contribution asserted here is narrower: the exact finite-\(n\)
area-balance threshold (3), its sign separation (4), the unique linear
bias-cancelling aspect ratio (7), the quartic real-relaxation cancellation
(8), and the cubic integer-rounding law (9). Searches under *Schwarz
lantern*, *Schwarz polyhedron*, *surface-area approximation*, *area
error*, *convergence rate*, *optimal aspect ratio*, *balanced
triangulation*, and the equivalent exact-area equation did not locate
these statements or an equivalent asymptotic optimization. Originality is
therefore asserted only **to the best of our knowledge**. Because the
claims follow from an elementary expansion of a classical exact formula,
an equivalent observation may exist in older approximation or finite
element literature under different terminology.

## Limitations

- The result concerns the standard staggered Schwarz-lantern triangulation
  of a circular cylinder; it is not a general theorem for arbitrary
  triangulations or smooth surfaces.
- The optimized quantity is total lateral area only. No corresponding
  optimality is claimed for normals, curvature measures, Hausdorff error,
  interpolation error, or element quality.
- The exact threshold \(m_*(n)\) is a real relaxation. Physical lanterns
  require integer \(m\); (9) quantifies the resulting rounding loss.
- The originality assessment is to the best of our knowledge, with
  residual folklore risk because the proof is elementary.

## References

1. K. Kobayashi and T. Tsuchiya, *Approximating surface areas by
   interpolations on triangulations*, Japan Journal of Industrial and
   Applied Mathematics 34 (2017), 509--530.
   https://doi.org/10.1007/s13160-017-0253-0
   Preprint: https://arxiv.org/abs/1610.06054

2. L. Brewin, *Curvature corrected estimates for geodesic arc-length*,
   arXiv:1512.03461 (2015).
   https://arxiv.org/abs/1512.03461

3. J.-O. Lachaud, P. Romon, B. Thibert, and D. Coeurjolly,
   *Interpolated corrected curvature measures for polygonal surfaces*,
   Computer Graphics Forum 39 (2020), 41--54.
   https://doi.org/10.1111/cgf.14067

## Review status

**Same-model review: passed. Independent audit: not yet performed.**
