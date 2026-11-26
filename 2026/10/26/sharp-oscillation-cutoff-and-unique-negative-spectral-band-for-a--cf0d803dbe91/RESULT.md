# Sharp oscillation cutoff and unique negative spectral band for a hyperbolic soliton kernel

## Finding

On real hyperbolic space \(\mathbb H^3\) of curvature \(-1\), put
\[
K_\omega(x,y)=\operatorname{sech}^2(d(x,y))\cos(\omega d(x,y)),\qquad \omega\ge0.
\]
This kernel is positive semidefinite on every finite point configuration if and only if \(0\le\omega\le\omega_*\), where
\[
\omega_* = \frac{2u_*}{\pi}=0.7637391428751280204\ldots,
\qquad u_*>0,\quad u_*\tanh u_*=1.
\]
The spherical transform is even in the real spectral parameter. Below the cutoff it is strictly positive at every real frequency. At the cutoff it vanishes only at zero. Above the cutoff there is exactly one positive zero \(\lambda_\omega\), determined by
\[
\lambda_\omega\coth(\pi\lambda_\omega/2)=\omega\tanh(\pi\omega/2).
\]
In that case the transform is negative for \(0\le|\lambda|<\lambda_\omega\), zero at \(|\lambda|=\lambda_\omega\), and positive for \(|\lambda|>\lambda_\omega\). In particular the supercritical transform is strictly negative at \(\lambda=0\), not just at sufficiently small positive frequencies.

## Assumptions and scope

Positive semidefiniteness means \(\sum_{j,k}c_j\overline{c_k}K_\omega(x_j,x_k)\ge0\) for arbitrary finite configurations and complex coefficients. Use the curvature \(-1\) spherical functions \(\varphi_\lambda(r)=\sin(\lambda r)/(\lambda\sinh r)\) and the radial transform
\[
\widehat k(\lambda)=\frac{4\pi}{\lambda}\int_0^\infty k(r)\sinh r\sin(\lambda r)\,dr.
\]
This is extended by continuity at zero; the Plancherel measure on the nonnegative spectrum is a positive constant times \(\lambda^2d\lambda\). No other dimension, curvature, or envelope is classified here.

## Proof

Let \(k_\omega(r)=\operatorname{sech}^2r\cos(\omega r)\), \(c=\pi/2\), and \(g(r)=\operatorname{sech}r\). The profile is continuous and radial \(L^2\), since
\[
4\pi\int_0^\infty |k_\omega(r)|^2\sinh^2r\,dr
\le 4\pi\int_0^\infty\operatorname{sech}^4r\sinh^2r\,dr=4\pi/3;
\]
the last integral reduces to \(\int_0^1 s^2\,ds\) by \(s=\tanh r\).

The cosine transform of \(g\) on the positive half-line is \((\pi/2)\operatorname{sech}(cs)\) at frequency \(s\in\mathbb R\). Indeed, substitute \(v=e^{2r}\) in the whole-line Fourier integral to obtain the beta integral \(\int_0^\infty v^{(1+is)/2-1}/(1+v)\,dv=\pi/\cosh(cs)\), and use evenness. Since \(-g'(r)=\sinh r\operatorname{sech}^2r\), integration by parts gives
\[
\int_0^\infty -g'(r)\sin(sr)\,dr=(\pi s/2)\operatorname{sech}(cs).
\]
The boundary terms vanish since \(\sin(0)=0\) and \(g(r)\to0\). Applying the sine–cosine product identity in the radial transform gives, for \(\lambda\ne0\),
\[
\widehat k_\omega(\lambda)=\frac{\pi^2}{\lambda}
\big[(\lambda+\omega)\operatorname{sech}(c(\lambda+\omega))
+(\lambda-\omega)\operatorname{sech}(c(\lambda-\omega))\big].
\]
Writing \(F(s)=s\operatorname{sech}(cs)\), the bracket is \(F(\omega+\lambda)-F(\omega-\lambda)\) by oddness. Thus the transform is even and its value at zero is
\[
\widehat k_\omega(0)=2\pi^2 F'(\omega)=2\pi^2\operatorname{sech}(c\omega)[1-c\omega\tanh(c\omega)].
\]
It decays exponentially for large \(|\lambda|\) at fixed \(\omega\), so it is integrable against the Plancherel measure.

For \(\lambda>0\), put \(A=\cosh(c\lambda)\cosh(c\omega)\) and \(B=\sinh(c\lambda)\sinh(c\omega)\). Combining the positive denominators \(A+B\) and \(A-B\) makes the numerator \(2(\lambda A-\omega B)\). After dividing by positive factors its sign is that of
\[
h(\lambda)-q(\omega),\qquad h(\lambda)=\lambda\coth(c\lambda),\quad q(\omega)=\omega\tanh(c\omega).
\]
The function \(h\) is strictly increasing since its derivative has positive numerator \(\sinh(c\lambda)\cosh(c\lambda)-c\lambda\) and denominator \(\sinh^2(c\lambda)\). Its range for positive \(\lambda\) is \((1/c,\infty)\). The function \(q\) increases continuously from zero to infinity. Hence the unique cutoff satisfies \(q(\omega_*)=1/c\), giving the stated equation for \(u_*\). For \(\omega\le\omega_*\) all positive frequencies have strictly positive transform. For \(\omega>\omega_*\), the positive root of \(h(\lambda)=q(\omega)\) exists, is unique, and is simple because \(h'(\lambda)>0\) and the prefactors in the sign comparison are positive and smooth there. The zero-frequency formula shows separately that the sign at zero is the sign of \(1-cq(\omega)\). This proves the stated classification, with the negative frequencies following by evenness.

The \(L^2\)-Godement criterion for continuous radial profiles applies: the distance kernel is positive semidefinite exactly when the transform is nonnegative almost everywhere for the Plancherel measure. Above the cutoff the negative interval has positive Plancherel measure; at the cutoff all positive frequencies still have positive transform. This proves the inclusive sharp threshold.

## Verification

The transform and monotonicity arguments above establish the continuum claim. The accompanying `verify_spherical_transform.py` evaluates the original spherical integral and closed form at 12 positive-frequency pairs, checks a hyperbolic addition identity and illustrates the cutoff and the \(L^2\) calculation. Run `python verify_spherical_transform.py` with SymPy and mpmath. These finite diagnostics do not establish the spectral sign at zero or on a continuum; the displayed formulas and proof handle those points.

## Relationship to prior work and limitations

Da Costa, Mostajeran, Ortega and Said give the \(L^2\)-Godement criterion and the unmodulated hyperbolic-secant kernels on \(\mathbb H^3\) ([arXiv:2310.19270](https://arxiv.org/abs/2310.19270), Theorem 3.1 and Appendix B). Their power-two case is the \(\omega=0\) member, with transform \(2\pi^2\operatorname{sech}(\pi\lambda/2)\). The Euclidean line kernel \(\operatorname{sech}^2(x-y)\) is discussed by De Marchi and Schaback, *Nonstandard Kernels and their Applications*, DRNA 2 (2009), §8.4. Neither antecedent classifies the sign of the shifted odd transform appearing here. A [related Resultary result](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-sharp-oscillation-threshold-for-exponentially-damped-geodesic-co--99a263d091a0/RESULT.md) studies the same geodesic modulation with the envelope \(e^{-ar}\), yielding a different threshold. The hyperbolic-secant envelope does not follow by a positive mixture of exponential envelopes: such mixtures are convex, while \((\operatorname{sech}^2 r)''<0\) near zero. This comparison identifies distinct claims within the inspected literature, not absolute priority.
