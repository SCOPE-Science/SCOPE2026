# Sharp oscillation cutoff and unique negative spectral band for a hyperbolic soliton kernel

## Finding

Let \(\mathbb H^3\) have sectional curvature \(-1\) and let \(d\) denote geodesic distance. Define for each \(\omega\ge0\)
\[
K_\omega(x,y)=\operatorname{sech}^2(d(x,y))\cos(\omega d(x,y)).
\]
There is a **sharp, inclusive** oscillation threshold
\[
\omega_*=\frac{2u_*}{\pi}=0.7637391428751280204\ldots,
\qquad u_*\tanh u_*=1,\quad u_*>0,
\]
such that \(K_\omega\) is positive semidefinite for every finite point configuration in \(\mathbb H^3\) **if and only if** \(0\le\omega\le\omega_*\).

There is also a complete spectral-sign classification. Above the cutoff, the spherical transform has exactly one nontrivial zero \(\lambda_\omega>0\), is negative precisely on \(0<\lambda<\lambda_\omega\), and is positive for \(\lambda>\lambda_\omega\), with
\[
\lambda_\omega\coth\left(\frac{\pi\lambda_\omega}{2}\right)
=\omega\tanh\left(\frac{\pi\omega}{2}\right).
\]
At the cutoff, the transform is zero at \(\lambda=0\) and positive for every \(\lambda>0\). Below the cutoff it is positive at all real frequencies.

## Assumptions and scope

Positive semidefiniteness means that, for every finite set of points \(x_1,\ldots,x_N\in\mathbb H^3\) and all complex coefficients \(c_1,\ldots,c_N\),
\[
\sum_{j,k=1}^N c_j\overline{c_k}K_\omega(x_j,x_k)\ge0.
\]
No restriction is imposed on the configuration or on \(N\). The parameter \(\omega\) is real and nonnegative. The metric normalization is constant curvature \(-1\); no additional length scale is implicit.

For an invariant radial function \(k(r)\), the spherical transform is normalized here by
\[
\widehat k(\lambda)=\frac{4\pi}{\lambda}
\int_0^\infty k(r)\sinh r\,\sin(\lambda r)\,dr
\qquad (\lambda>0),
\]
with the value at \(\lambda=0\) taken by continuity. Its elementary spherical functions are \(\varphi_\lambda(r)=\sin(\lambda r)/(\lambda\sinh r)\). The Plancherel density is proportional to \(\lambda^2d\lambda\), with a positive proportionality constant.

## Proof

**Integrability and the spectral criterion.** The radial profile is continuous, and
\[
\int_{\mathbb H^3}|K_\omega(o,x)|^2\,dx
\le4\pi\int_0^\infty \operatorname{sech}^4r\sinh^2r\,dr
=\frac{4\pi}{3}.
\]
The last identity follows from \(s=\tanh r\). Therefore the \(L^2\)-Godement theorem applies once the spherical transform has been computed and shown integrable against the Plancherel measure.

**Exact transform.** Write \(c=\pi/2\) and \(g(r)=\operatorname{sech}r\). Then
\[
\sinh r\,\operatorname{sech}^2r=-g'(r),
\qquad
\int_0^\infty g(r)\cos(sr)\,dr=\frac{\pi}{2}\operatorname{sech}(cs)
\quad(s\in\mathbb R).
\]
For any real \(s\), integration by parts (the boundary terms vanish) gives
\[
\int_0^\infty -g'(r)\sin(sr)\,dr
=\frac{\pi s}{2}\operatorname{sech}(cs).
\]
Applying the product-to-sum identity yields, for every \(\lambda>0\),
\[
\boxed{\displaystyle
\widehat K_\omega(\lambda)=\frac{\pi^2}{\lambda}
\left[(\lambda+\omega)\operatorname{sech}(c(\lambda+\omega))
+(\lambda-\omega)\operatorname{sech}(c(\lambda-\omega))\right].}
\]
This expression is continuous at zero, where
\[
\widehat K_\omega(0)=2\pi^2\operatorname{sech}(c\omega)
\left[1-c\omega\tanh(c\omega)\right].
\]
It decays exponentially in \(\lambda\) for fixed \(\omega\), so \(\int_0^\infty|\widehat K_\omega(\lambda)|\lambda^2d\lambda<\infty\).

**Exact spectral sign.** Put
\[
A=\cosh(c\lambda)\cosh(c\omega),\qquad
B=\sinh(c\lambda)\sinh(c\omega).
\]
Since \(\cosh(c(\lambda\pm\omega))=A\pm B>0\), the bracket in the transform has the sign of
\[
2(\lambda A-\omega B)
=2A\left[\lambda-\omega\tanh(c\lambda)\tanh(c\omega)\right].
\]
For \(\lambda>0\), this is the sign of
\[
h(\lambda)-q(\omega),\qquad
h(\lambda)=\lambda\coth(c\lambda),\quad
q(\omega)=\omega\tanh(c\omega).
\]
The function \(h\) is strictly increasing because
\[
h'(\lambda)=\frac{\sinh(c\lambda)\cosh(c\lambda)-c\lambda}
{\sinh^2(c\lambda)}>0,
\]
and its range on positive \(\lambda\) is \((1/c,\infty)\). Likewise \(q\) increases continuously from zero to infinity. Consequently, the unique cutoff is characterized by \(q(\omega_*)=1/c\), equivalently \(u_*\tanh u_*=1\) with \(u_*=c\omega_*\).

For \(\omega\le\omega_*\), \(h(\lambda)>q(\omega)\) at every positive frequency. At equality the displayed zero-frequency limit vanishes, but all positive frequencies remain strictly positive. For \(\omega>\omega_*\), strict monotonicity of \(h\) gives one and only one positive solution \(\lambda_\omega\) of \(h(\lambda)=q(\omega)\), and the transform has negative and positive signs on the asserted intervals. The crossing is simple because \(h'(\lambda_\omega)>0\).

**Positive-definiteness equivalence.** The continuous radial function belongs to \(L^2(\mathbb H^3)\), and its spherical transform is integrable against \(\lambda^2d\lambda\). The \(L^2\)-Godement positivity criterion therefore asserts that its induced distance kernel is positive semidefinite exactly when the transform is nonnegative almost everywhere. The sign classification just proved gives the sharp if-and-only-if condition, including the boundary. For \(\omega>\omega_*\), the negative interval has positive Plancherel measure, so no finite-configuration positive-definiteness assertion can hold universally.

## Verification

The embedded `verify_spherical_transform.py` evaluates the original spherical integral and the closed transform at 12 positive-frequency test pairs below, at, and above the critical oscillation threshold, with high-precision quadrature. The largest absolute discrepancy in these cases is less than \(5\times10^{-28}\) at 50-digit working precision. It also checks the relevant hyperbolic addition identity symbolically, computes the unique cutoff, and verifies the unmodulated radial \(L^2\)-integral. The continuum and endpoint conclusions follow from the analytic proof, not from the numerical checks.

To reproduce, run `python verify_spherical_transform.py` with Python, SymPy and mpmath installed. The kernel and transform conventions in the checker agree with those in this document.

## Relationship to prior work

De Marchi and Schaback (2009, Section 8.4) use the squared hyperbolic-secant *translation-invariant kernel on the line*, recognizing its positive Euclidean Fourier transform. Feragen, Lauze and Hauberg (arXiv:1411.0296, public 2014-11-02) study geodesic exponential kernels on curved spaces; their main conclusions concern Gaussian and Laplacian-type kernels, rather than the modulated squared hyperbolic secant. Da Costa, Mostajeran, Ortega and Said (arXiv:2310.19270, Appendix B) treat \((\cosh r)^{-a}\) on \(\mathbb H^3\), proving positivity for integer powers; they supply the applicable \(L^2\)-Godement framework and spherical transform. Their unmodulated positivity is the \(\omega=0\) case but does not imply the sharp nonzero-oscillation cutoff or the unique negative spectral band. The new statement concerns modulation \(\cos(\omega r)\), not a change of the decay exponent \(a\).

## Limitations

The conclusion concerns real hyperbolic dimension three, curvature \(-1\), fixed envelope \(\operatorname{sech}^2r\), and real \(\omega\ge0\). It does not classify other powers, dimensions, geometries, or complex oscillation parameters. The literature comparison is bounded and does not exclude an equivalent result under an unindexed or differently named formulation. No finite numerical check is used as an infinite proof.

## References

1. S. De Marchi and R. Schaback, *Nonstandard Kernels and their Applications*, DRNA 2 (2009), pp. 16–43, Section 8.4. https://drna.padovauniversitypress.it/system/files/papers/Schaback-2009-NKA.pdf
2. A. Feragen, F. Lauze and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, 2014 preprint, arXiv:1411.0296. https://arxiv.org/abs/1411.0296
3. N. Da Costa, C. Mostajeran, J.-P. Ortega and S. Said, *Invariant kernels on Riemannian symmetric spaces: a harmonic-analytic approach*, arXiv:2310.19270, Theorem 3.1, Section 4.2 and Appendix B. https://arxiv.org/abs/2310.19270
