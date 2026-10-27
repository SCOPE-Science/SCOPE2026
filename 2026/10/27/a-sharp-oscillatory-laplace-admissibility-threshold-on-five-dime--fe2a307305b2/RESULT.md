# A sharp oscillatory-Laplace admissibility threshold on five-dimensional hyperbolic space

## Finding

Let \(\mathbb H^5\) be real hyperbolic five-space of sectional curvature \(-1\), and write \(d(x,y)\) for geodesic distance. For every real \(a>4\) and \(\omega\geq0\), consider the continuous real symmetric kernel

\[
K_{a,\omega}(x,y)=e^{-a d(x,y)}\cos\bigl(\omega d(x,y)\bigr).
\]

Define

\[
\Omega_5(a)^2=a^2-\frac{12}{5}-\frac25\sqrt{5a^4-20a^2+16}.
\]

The radicand and the resulting square are positive for all \(a>4\). **The kernel is positive semidefinite on every finite subset of \(\mathbb H^5\) if and only if \(0\leq\omega\leq\Omega_5(a)\).** At equality, its spherical transform vanishes only at spectral frequency \(\lambda=0\) and is strictly positive at every \(\lambda>0\); below equality it is strictly positive at every \(\lambda\geq0\). Above equality there is an explicitly identified negative spherical-transform frequency. In particular, at \(a=6\) the sharp angular frequency is \(\omega=4/\sqrt5\).

The qualification \(a>4\) is part of the theorem. No assertion is made here for smaller decay exponents or for other hyperbolic dimensions.

## Assumptions and scope

For a finite set \(\{x_1,\ldots,x_N\}\subset\mathbb H^5\), positivity means

\[
\sum_{j,k=1}^N c_j\overline{c_k}\,K_{a,\omega}(x_j,x_k)\geq0
\quad\text{for all }N\geq1\text{ and all }c_j\in\mathbb C.
\]

The curvature normalization is exactly \(-1\), and the radial measure is \(\sinh^4r\,dr\,d\sigma_4\), with \(|S^4|=8\pi^2/3\). We use normalized zonal spherical functions \(\varphi_\lambda(0)=1\) with principal spectral parameter \(\lambda\geq0\). As \(a>4\), the radial kernel is integrable on \(\mathbb H^5\); the spherical Fourier multiplier criterion applies: such an integrable continuous radial kernel is positive definite precisely when its spherical transform is nonnegative at all real spectral parameters. This follows by Fourier diagonalization of the associated convolution operator on \(L^2(\mathbb H^5)\) and approximation of point masses.

## Proof

**1. Normalized spherical functions.** Put \(r=d(x,y)\). The normalized spherical function in dimension three is

\[
\varphi^{(3)}_\lambda(r)=\frac{\sin(\lambda r)}{\lambda\sinh r},
\]

with continuous values at \(\lambda=0\) and \(r=0\). The radial dimension-raising identity gives

\[
\varphi^{(5)}_\lambda(r)
=-\frac3{1+\lambda^2}\frac1{\sinh r}
\frac{d}{dr}\varphi^{(3)}_\lambda(r).
\]

It can be verified by applying the five-dimensional radial Laplace--Beltrami operator \(\partial_r^2+4\coth r\,\partial_r\) and checking \(\varphi^{(5)}_\lambda(0)=1\). The eigenvalue is \(-4-\lambda^2\). The same shift-operator construction is established in the cited primary literature.

**2. Exact transform.** For a complex parameter \(z\) with \(\operatorname{Re}z>4\), put

\[
I_z(\lambda)=\int_0^\infty e^{-zr}\varphi^{(5)}_\lambda(r)\sinh^4r\,dr.
\]

Integrating by parts gives

\[
I_z(\lambda)=\frac3{\lambda(1+\lambda^2)}
\int_0^\infty e^{-zr}
\bigl(3\sinh r\cosh r-z\sinh^2r\bigr)
\sin(\lambda r)\,dr.
\]

Using \(\int_0^\infty e^{-ur}\sin(\lambda r)\,dr=\lambda/(u^2+\lambda^2)\) for \(\operatorname{Re}u>0\), elementary expansion yields

\[
\begin{aligned}
I_z(\lambda)
&=\frac3{4(1+\lambda^2)}\left[
\frac{3-z}{(z-2)^2+\lambda^2}
-\frac{3+z}{(z+2)^2+\lambda^2}
+\frac{2z}{z^2+\lambda^2}\right]\\
&=\frac{24z}{(z^2+\lambda^2)((z-2)^2+\lambda^2)((z+2)^2+\lambda^2)}.
\end{aligned}
\]

All denominators are nonzero in the declared half-plane. The formulas at \(\lambda=0\) follow by continuity. For \(z=a-i\omega\) and \(X=\lambda^2\), therefore,

\[
\widehat K_{a,\omega}(\lambda)
=64\pi^2\operatorname{Re}
\frac{z}{(z^2+X)((z-2)^2+X)((z+2)^2+X)}.
\]

The factor \(64\pi^2\) is positive, so only the real part matters.

**3. The sign polynomial.** Put \(W=\omega^2\) and

\[
C_a(W)=5W^2+(24-10a^2)W+(a^2-4)^2.
\]

Multiplying the preceding real part by its positive denominator gives the polynomial

\[
\begin{aligned}
P_a(X,W)=a\big[\,&X^3+(3a^2+3W+8)X^2\\
&+(3a^4-6a^2W-9W^2+16)X\\
&+(a^2+W)C_a(W)\big].
\end{aligned}
\]

More explicitly,

\[
\operatorname{Re}\frac{z}{\prod_{j\in\{-2,0,2\}}((z+j)^2+X)}
=\frac{P_a(X,W)}{\prod_{j\in\{-2,0,2\}}|((z+j)^2+X)|^2}.
\]

The discriminant of \(C_a\) is \(16(5a^4-20a^2+16)>0\), so its two roots are

\[
W_\pm(a)=a^2-\frac{12}{5}\pm\frac25\sqrt{5a^4-20a^2+16}.
\]

The elementary identities

\[
C_a(0)=(a^2-4)^2>0,
\quad C_a(a^2-4)=-4a^2(a^2-4)<0,
\quad C_a(a^2/3)=-\frac{16}{9}(a^4-9)<0
\]

show that \(0<W_-(a)<a^2/3\) and \(W_-(a)<a^2-4<W_+(a)\).

**4. Sufficiency.** For \(0\leq W\leq W_-(a)\), the quadratic \(C_a(W)\) is nonnegative. The coefficient of \(X^2\) in \(P_a/a\) is strictly positive, and the coefficient of \(X\) is positive because \(W<a^2/3\) implies

\[
3a^4-6a^2W-9W^2+16>16>0.
\]

Consequently \(P_a(X,W)\geq0\) for every \(X\geq0\). It is positive for all \(X\geq0\) when \(W<W_-(a)\), while at \(W=W_-(a)\) it vanishes exactly at \(X=0\). The spherical Fourier multiplier is thus nonnegative everywhere, proving positive definiteness.

**5. Necessity and explicit witnesses.** If \(W_-(a)<W<a^2-4\), then \(C_a(W)<0\), whence \(P_a(0,W)<0\): spectral frequency \(\lambda=0\) is a witness. If \(W\geq a^2-4\), select the nonnegative value \(X=W-a^2+4\). Direct substitution yields

\[
P_a(W-a^2+4,W)=-8a(a^2-4)(W+2)(W+4)<0.
\]

The spherical transform is then negative at \(\lambda=\sqrt{W-a^2+4}\). This exhausts all \(W>W_-(a)\) and proves the equivalence.

## Verification

The standalone file `check_h5.py` requires Python 3, SymPy and mpmath. It checks: the exact three-term partial-fraction identity for \(I_z\); the polynomial identity for \(P_a\); the discriminant and two endpoint evaluations of \(C_a\); the explicit high-frequency negative witness; and twelve independent high-precision numerical integrations of the defining radial spherical transform against the rational formula. The observed maximum absolute difference in those twelve comparisons was below \(2.1\times10^{-31}\). The numerical quadrature starts at radius \(10^{-6}\), omitting a rigorously bounded contribution below \(2.1\times10^{-31}\) in each displayed case. These finite numerical comparisons are diagnostics, not the proof of the all-parameter theorem; the universal sign argument appears above.

For a simple exact boundary, \(a=6\) gives \(W_-=16/5\). At \(\omega=4/\sqrt5\), the multiplier is zero only at \(\lambda=0\), whereas for \(\omega=2\) it is negative at \(\lambda=0\).

## Relationship to prior work

Feragen, Lauze, and Hauberg establish positive-definiteness criteria for geodesic exponential kernels, including the unmodulated Laplacian \(e^{-a d}\) on hyperbolic spaces. Their results imply the present claim only at \(\omega=0\), not at positive modulation. Hall and Mitchell give the odd-dimensional hyperbolic spherical shift calculus used here; their subject is Segal--Bargmann transform isometry and inversion, not an exact oscillatory-Laplace covariance admissibility region. Restriction to a totally geodesic \(\mathbb H^3\) can supply necessary conditions but cannot establish the five-dimensional sufficiency or the explicit high-frequency obstruction proved here. The five-dimensional threshold is genuinely dimension-sensitive, approaching \(\Omega_5(a)/a=\sqrt{1-2/\sqrt5}\) as \(a\to\infty\).

The mathematical contribution here is the complete sharp classification of the fast-decay oscillatory family in five dimensions, not the spherical Fourier criterion or the shift operator themselves. A bounded literature and research-record comparison found no statement implying this explicit five-dimensional criterion; absence from inspected sources is not a proof of absolute priority.

## Limitations

The theorem covers \(a>4\), where the kernel is integrable on real hyperbolic five-space. It does not classify \(0<a\leq4\), other dimensions, or nonradial kernels. The Fourier-density zero at the boundary is not a finite-point Gram nullity statement. Independent mathematical verification and exhaustive bibliographic priority review have not been performed.

## References

1. A. Feragen, F. Lauze, and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296, first public 2014-11-02; sections 2--4 discuss CND and geodesic Laplacian kernels. https://arxiv.org/abs/1411.0296
2. B. C. Hall and J. J. Mitchell, *The Segal--Bargmann Transform for Odd-Dimensional Hyperbolic Spaces*, arXiv:1507.03569, first public 2015-07-13; section 4 gives spherical shift operators and section 7 spherical inversion. https://arxiv.org/abs/1507.03569
