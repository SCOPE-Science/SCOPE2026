# Antipodal Fourier obstruction and exact Laplace spectrum for the supremum-circle torus

## Finding
Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let \(\delta(t)=\min_{j\in\mathbb Z}|t-2\pi j|\), and equip \(\mathbb T^2\) with the translation-invariant product supremum distance
\[
D(x,y)=\max\{\delta(x_1-y_1),\delta(x_2-y_2)\}.
\]
For any real \(f\in C^2([0,\pi])\), form \(F_f(t,s)=f(\max\{\delta(t),\delta(s)\})\). Its axial Fourier coefficients obey
\[
\lim_{k\to\infty}(2k)^2\widehat F_f(2k,0)=\frac{f'(\pi)}{\pi},\qquad
\lim_{k\to\infty}(2k+1)^2\widehat F_f(2k+1,0)=-\frac{f'(\pi)}{\pi}.
\]
Thus \(f'(\pi)\ne0\) forces infinitely many strictly negative Fourier coefficients, and \(F_f\) cannot be a positive-definite function on \(\mathbb T^2\).

For the natural Laplace profile \(f(t)=e^{-at}\), \(a>0\), **all** Fourier coefficients can be signed exactly. Every off-axis coefficient \(\widehat F_a(n,m)\) with \(nm\ne0\), every odd nonzero axial coefficient and the constant coefficient are strictly positive. The even axial coefficient \(\widehat F_a(n,0)\), where \(n\in2\mathbb Z\setminus\{0\}\), is negative exactly if
\[
n^2>Q(a):=\frac{2a(e^{\pi a}-1)}{\pi}-a^2;
\]
it vanishes on equality and is positive below the threshold. Consequently, \(e^{-aD}\) is **not** positive definite on \(\mathbb T^2\) for *any* \(a>0\), although the corresponding two-dimensional Euclidean supremum-norm Laplace kernel and the one-circle intrinsic Laplace kernel are both positive definite. The least even positive axial frequency with a negative coefficient is
\[
n_*(a)=2\biggl(\biggl\lfloor\frac{\sqrt{Q(a)}}2\biggr\rfloor+1\biggr)
\sim \sqrt{\frac{2a}{\pi}}\,e^{\pi a/2}\quad(a\to\infty).
\]

## Assumptions and scope
A translation-invariant function \(F\) on \(\mathbb T^2\) is positive definite if, for all finite point systems \(x_j\in\mathbb T^2\) and coefficients \(c_j\in\mathbb C\), one has \(\sum_{j,k}c_j\overline{c_k}F(x_j-x_k)\ge0\). Fourier coefficients use normalized Haar measure:
\[
\widehat F(n,m)=(2\pi)^{-2}\int_{[-\pi,\pi]^2}F(t,s)e^{-i(nt+ms)}\,dt\,ds.
\]
Fourier variables \(n,m\) are integers. In the general obstruction, \(f\) is real and twice continuously differentiable up to both endpoints; this smoothness assumption concerns the scalar function \(f\), not the nonsmooth maximum map. The explicit Laplace classification holds for every real \(a>0\). Zero-frequency and equality cases are included.

## Proof
**1. Reduction to the first quadrant and the antipodal seam.** The function is even in both variables. Consequently,
\[
\widehat F_f(n,m)=\frac1{\pi^2}\int_0^\pi\!\int_0^\pi
 f(\max\{t,s\})\cos(nt)\cos(ms)\,ds\,dt.
\]
For \(n\ge1\), setting \(m=0\) and integrating over the two triangles \(0\le s\le t\) and \(0\le t\le s\) gives
\[
\widehat F_f(n,0)=\frac1{\pi^2}\int_0^\pi f(t)
\left(t\cos(nt)+\frac{\sin(nt)}n\right)dt.
\]
Integrate by parts twice. The endpoint terms from \(\sin(n\pi)=0\) and the factor \(t\) at zero yield the exact identity
\[
\widehat F_f(n,0)=\frac{(-1)^nf'(\pi)}{\pi n^2}
-\frac1{\pi^2n^2}\int_0^\pi (f'(t)+tf''(t))\cos(nt)\,dt.
\]
The final integrand is continuous. By the Riemann--Lebesgue lemma, its cosine transform tends to zero. The two stated parity limits follow. A continuous positive-definite function on a compact abelian group has nonnegative Fourier coefficients (the compact-group Bochner theorem); the negative subsequence contradicts positivity. This proves the general obstruction without any finite-frequency extrapolation.

**2. Explicit spectrum for the exponential profile.** Put \(E=e^{-\pi a}\) and, for integers \(j\), \(B_j=a^2+j^2\). Direct integration gives
\[
\widehat F_a(0,0)=\frac{2[1-(1+\pi a)E]}{\pi^2a^2}>0.
\]
If \(n\ge1\), then
\[
\widehat F_a(n,0)=\widehat F_a(0,n)
=\frac1{\pi^2}\left[\frac{2a^2(1-(-1)^nE)}{B_n^2}
-\frac{\pi a(-1)^n E}{B_n}\right].
\]
For \(n,m\ge1\), the two triangles instead yield
\[
\widehat F_a(n,m)=\frac1{\pi^2}\int_0^\pi e^{-at}
\left(\frac{\cos(nt)\sin(mt)}m+\frac{\cos(mt)\sin(nt)}n\right)dt.
\]
The identity \(\int_0^\pi e^{-at}\sin(jt)dt=j[1-(-1)^jE]/B_j\) and product-to-sum simplify this to
\[
\widehat F_a(n,m)=\frac{a^2[1-(-1)^{n+m}E]}{2\pi^2nm}
\left(\frac1{B_{n-m}}-\frac1{B_{n+m}}\right)>0.
\]
Evenness covers negative indices, replacing \(n,m\) by their absolute values. For odd \(n\), both terms of the displayed axial coefficient are positive; for positive even \(n\), its sign is the sign of \(2a(1-E)-\pi E(a^2+n^2)\), giving the threshold \(Q(a)\) exactly. Since \(Q(a)>a^2>0\) and grows without bound but is finite for every \(a>0\), infinitely many even axial modes are strictly negative. Equality gives a zero coefficient at that single even magnitude; higher even modes stay negative. The asymptotic for \(n_*(a)\) follows from \(Q(a)\sim(2a/\pi)e^{\pi a}\).

**3. Why the product obstruction is substantive.** In \(\mathbb R^2\),
\[
\max\{|u|,|v|\}=\tfrac12(|u+v|+|u-v|).
\]
Hence \(e^{-a\max\{|u|,|v|\}}\) is a product of two pullbacks of the positive-definite one-dimensional Laplace kernel, so is positive definite for every \(a>0\). On one circle, the kernel \(e^{-a\delta(t)}\) has the strictly positive cosine/Fourier coefficients \(a[1-(-1)^nE]/[\pi(a^2+n^2)]\) for every integer \(n\). The two-fold wrapped supremum construction therefore destroys positivity that exists in both comparison settings. The obstruction arises specifically from the antipodal edges and survives arbitrarily strong damping.

## Verification
Run `python3 verify.py` with Python 3 standard library. It computes the closed Fourier formulas and independently approximates 24 continuous double integrals by composite two-dimensional quadrature (maximum observed discrepancy approximately \(1.3\times10^{-7}\)); it then checks exact-sign implications for 1,497 even axial modes and 432 mixed nonzero modes, for three positive damping parameters. Direct finite-grid Fourier computations give negative real quadratic forms at \(a=1\), frequency \((4,0)\), on both 16-by-16 and 32-by-32 toroidal sampling grids. For the 16-by-16 grid, the negative quadratic form is about \(-7.740924236\), and the corresponding normalized discrete Fourier coefficient about \(-0.00023623426\). These finite computations corroborate but do not replace the all-frequency analytic proof.

## Relationship to prior work
Gneiting (arXiv:1111.7077, 2011) establishes positive-definite classes for geodesic distances on spheres and the circle, including completely monotone Laplace profiles; this does not entail positivity after taking a maximum over two independently wrapped circle distances. Feragen, Lauze and Hauberg (arXiv:1411.0296, 2014) give geodesic exponential-kernel and negative-type criteria, not the explicit two-torus obstruction or the frequency sign classification here. Guella, Menegatto and Peron (arXiv:1503.08174, 2015) characterize isotropic positive-definite kernels on products of spheres through nonnegative double Fourier/Gegenbauer coefficients; their separate arXiv:1505.01169 study treats strict positivity on products of circles through arithmetic support conditions; specializing their general criterion makes our calculations meaningful but does not supply the antipodal-seam asymptotic or the explicit \(Q(a)\) cutoff. Zhou (arXiv:2609.05622, 2026) studies Riemannian flat-torus distances defined using the Euclidean quotient norm, not the present supremum product metric, so its non-positive-definiteness conclusions do not imply the exact statement here.

## Limitations
The general sign theorem requires \(f\in C^2([0,\pi])\) and \(f'(\pi)\ne0\); when the endpoint derivative vanishes, no assertion is made. The exact complete spectral classification applies only to the exponentially damped maximum of two shortest-arc distances; no classification for higher torus dimensions or arbitrary wrapped norms follows. The negative coefficient proves existence of a finite negative Gram witness; the proof need not specify a minimal witness size. The literature comparison is bounded and cannot rule out equivalent formulations outside the inspected sources. All conclusions are mathematical proofs with supplementary numerical consistency tests, not independently validated findings.

## References
- T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077v1 (2011-11-30), https://arxiv.org/abs/1111.7077.
- A. Feragen, F. Lauze and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296v1 (2014-11-02), https://arxiv.org/abs/1411.0296.
- J. C. Guella, V. A. Menegatto and A. P. Peron, *An extension of a theorem of Schoenberg to products of spheres*, arXiv:1503.08174v1 (2015-03-27), https://arxiv.org/abs/1503.08174.
- J. C. Guella, V. A. Menegatto and A. P. Peron, *Strictly positive definite kernels on a product of circles*, arXiv:1505.01169v1 (2015-05-05), https://arxiv.org/abs/1505.01169.
- Y. Zhou, *Distance Energies and Negative Type of Flat Tori*, arXiv:2609.05622v1 (2026), https://arxiv.org/abs/2609.05622 (different Riemannian distance; comparison only).
