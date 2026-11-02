# Three simple Zak zeros for every odd two-pole rational window

## Finding
For arbitrary real \(0<a<b\), put
\[
 g_{a,b}(x)=\frac{x}{(x^2+a^2)(x^2+b^2)},\qquad
 Z_{a,b}(t,\xi)=\sum_{m\in\mathbb Z}g_{a,b}(t-m)e^{2\pi i m\xi}.
\]
In the standard half-open Zak fundamental cell \([0,1)\times[0,1)\), the complete zero set of \(Z_{a,b}\) is
\[
 \{(0,0),(1/2,0),(0,1/2)\}.
\]
All three zeros are nondegenerate as real maps from the two-dimensional parameter domain to \(\mathbb C\). With domain coordinates ordered \((t,\xi)\) and the target oriented as \((\operatorname{Re}Z,\operatorname{Im}Z)\), their local winding indices, in the displayed order, are \((-1,+1,+1)\). In particular, the number and signed geometry of Zak zeros do not depend on either pole location, not merely on their common scale.

## Assumptions and scope
The poles are distinct, purely imaginary, and occur in two positive pairs \(\pm ia,\pm ib\); \(a,b\) are arbitrary real numbers satisfying \(0<a<b\). The unit-period Zak transform uses the convention written above. Its defining series and its first derivatives converge locally uniformly: \(g_{a,b}(x)=O(|x|^{-3})\) and \(g'_{a,b}(x)=O(|x|^{-4})\). Quasiperiodic continuation identifies the opposite cell edges. No frame property away from critical lattice density is asserted.

## Proof
**1. Rational Fourier representation.** With Fourier convention \(\widehat g(\omega)=\int_{\mathbb R}g(x)e^{-2\pi i\omega x}\,dx\), partial fractions give
\[
 \widehat g_{a,b}(\omega)=-\frac{i\pi}{b^2-a^2}\operatorname{sgn}(\omega)
 \bigl(e^{-2\pi a|\omega|}-e^{-2\pi b|\omega|}\bigr),
\]
with value zero at \(\omega=0\). Write
\[
 q=e^{-2\pi a},\quad r=e^{-2\pi b},\quad
 u=q^{\xi},\quad v=r^{\xi},\quad z=e^{2\pi it}.
\]
Thus \(0<r<q<1\), and for \(0<\xi<1\), Poisson summation followed by four geometric sums yields
\[
 Z_{a,b}(t,\xi)=-\frac{i\pi}{b^2-a^2}e^{2\pi it\xi}S(z),\quad
 S(z)=\frac{u}{1-qz}-\frac{v}{1-rz}-\frac{q}{u(z-q)}+\frac{r}{v(z-r)}.
\]
The same identity holds continuously at \(\xi=0\) when \(u=v=1\). For \(|z|=1\) all four denominators are nonzero. Hence the Zak zeros equal the unit-circle zeros of the cubic
\[
 N(z)=uv(1-qz)(1-rz)(z-q)(z-r)S(z).
\]

**2. Exclusion of all other interior frequencies.** Set
\[
 \begin{aligned}
 A&=(u-v)(qr-uv)+(qv-ru)(1-uv),\\
 B&=(u-v)(qr-uv)-(qv-ru)(1-uv),\\
 C&=r(1+v^2)(q^2+u^2)-q(1+u^2)(r^2+v^2).
 \end{aligned}
\]
An exact polynomial resultant computation (independently reproducible in `CHECK.py`) establishes
\[
 \begin{split}
 \operatorname{Res}_z\bigl(N(z),z^3N(1/z)\bigr)
 ={}&-u^2v^2(q-1)(q+1)(q-r)^2(r-1)(r+1)\\
 &\quad\cdot(qr-1)^2 A B C^2.
 \end{split}
\]
If a real-coefficient polynomial has a root on the unit circle, it shares that root with its reciprocal polynomial, so this resultant must vanish. For \(0<\xi<1\), \(u>v\), \(uv>qr\), \(qv>ru\), and \(uv<1\), so \(B<0\).

To locate zeros of \(A\) and \(C\), put \(p=-\log q\), \(h=-\log r\), \(\delta=h-p>0\), \(\sigma=h+p>\delta\). The sign of \(A\) is the sign of
\[
 \frac{\sinh(\sigma\xi/2)}{\sinh(\delta\xi/2)}
 -\frac{\sinh(\sigma(1-\xi)/2)}{\sinh(\delta(1-\xi)/2)}.
\]
Indeed, divide its positive and negative summands and simplify using hyperbolic identities. For \(\sigma>\delta>0\), the function \(x\mapsto\sinh(\sigma x/2)/\sinh(\delta x/2)\) increases strictly on \(x>0\); differentiating its logarithm reduces this to the strict increase of \(y\mapsto y\coth y\). Consequently, \(A\) is negative for \(\xi<1/2\), zero exactly at \(1/2\), and positive above \(1/2\).

Likewise, divide \(C\) by the positive factor \(qr(1+u^2)(1+v^2)\). The result is
\[
 \frac{\cosh(p(1-\xi))}{\cosh(p\xi)}
 -\frac{\cosh(h(1-\xi))}{\cosh(h\xi)}.
\]
Its sign is negative below \(1/2\), zero at \(1/2\), positive above \(1/2\): for fixed \(\xi<1/2\), the quotient \(\cosh(x(1-\xi))/\cosh(x\xi)\) strictly increases with \(x>0\), and for \(\xi>1/2\) it strictly decreases. The derivative test uses strict increase of \(y\mapsto y\tanh y\). Therefore the resultant is nonzero throughout \(0<\xi<1\), except possibly \(\xi=1/2\).

**3. The remaining frequencies.** At \(\xi=1/2\), set \(w=\sqrt q\), \(s=\sqrt r\); then \(0<s<w<1\). Exact factorization gives
\[
 \begin{split}
 N(z)={}&sw(s-w)(sw-1)(z-1)\\
 &\cdot\bigl[sw(z^2+1)+((1+w^2)(1+s^2)+2sw)z\bigr].
 \end{split}
\]
The bracket divided by \(z\) is \(2sw\cos(2\pi t)+(1+w^2)(1+s^2)+2sw>0\) on \(|z|=1\). Thus \(z=1\) is the only midpoint zero. At \(\xi=0\), direct factorization gives
\[
 N(z)=-z(q-r)(z-1)(z+1)(qr-1),
\]
so precisely \(z=1,-1\) occur. This establishes the complete zero set.

**4. Simplicity and local indices.** At a zero, multiplication by the nowhere-zero prefactor in Step 1 preserves the Jacobian sign. Put \(S_z=\partial S/\partial z\). At \((z,\xi)=(1,0)\) and \((-1,0)\), direct differentiation yields \(S_z>0\) and
\[
 \partial_\xi S(1,0)=h\coth(h/2)-p\coth(p/2)>0,\qquad
 \partial_\xi S(-1,0)=h\tanh(h/2)-p\tanh(p/2)>0.
\]
At \((z,\xi)=(1,1/2)\), again \(S_z>0\), and
\[
 \partial_\xi S(1,1/2)=\frac{h}{\sinh(h/2)}-\frac{p}{\sinh(p/2)}<0.
\]
Here \(S_z(1,1/2)>0\) follows, for instance, from its explicit factorization
\[
 \frac{(s-w)(sw-1)\bigl((1+s^2)(1+w^2)+4sw\bigr)}{(1-s^2)^2(1-w^2)^2}>0.
\]
The first two inequalities follow from strict increase of \(x\coth(x/2)\) and \(x\tanh(x/2)\); the third follows from strict decrease of \(x/\sinh(x/2)\). Since \(\partial_t S=2\pi izS_z\), the real Jacobian sign is \(-\operatorname{sgn}(zS_z\partial_\xi S)\), yielding \((-1,+1,+1)\), and each Jacobian is nonzero.

## Verification
The standalone `CHECK.py` establishes the exact cubic resultant identity, midpoint and edge factorizations, three spatial derivative identities, and direct numerical agreement between the Zak series and its rational Fourier formula at three asymmetric pole pairs. The analytic inequalities above, not any finite sampling, prove the all-parameter assertion. The checker is run by `python CHECK.py` with SymPy installed. All identities are in terms of independent positive real parameters before the exponential substitutions, avoiding a fixed-ratio specialization.

## Relationship to prior work
Ghosh (2026) developed the cubic rational-polynomial Zak representation and rational-density Gabor frame results for the special pole ratio \(a:b=1:2\); it does not state a complete torus zero divisor for arbitrary unequal pole ratios, nor the three Jacobian indices. The published analysis of Hermite-window Zak zeros by Faulhuber (2025) explains why additional non-parity zeros are a substantive issue, but concerns a different function family. The present theorem concerns arbitrary \(0<a<b\); it is not a consequence of a dilation of a fixed-ratio result because dilation preserves the pole ratio. Classical Zak quasi-periodicity and the forced three zeros for odd windows are background, not claimed as new. The zero exclusion and transversality for all pole ratios are the asserted contribution.

## Limitations
This result applies only to unit-period Zak transforms of two-distinct-pole rational odd windows. It does not determine full Gabor frame sets for general rational lattice densities, nor describe three or more pole pairs. A matching older classification could exist outside the inspected material; this proof has not received independent mathematical review. The indices use the stated convention for the order of domain and target coordinates.

## References
1. R. Ghosh, *Gabor Frames for Rational Windows with Symmetric Poles*, first posted 2026-08-11, arXiv:2608.10568, https://arxiv.org/abs/2608.10568. Sections 2–4 and Appendix; Zak polynomial, reflection, and frame problem.
2. M. Faulhuber, *Gabor systems with Hermite functions of order N and oversampling greater than N+1 which are not frames*, first posted 2025-02-13, arXiv:2502.09510; *Sampling Theory, Signal Processing, and Data Analysis* 23 (2025), article 22. Sections 2–4; parity-forced and further Zak zeros for Hermite windows.
3. T. Kloos, *Zeros of the Zak transform of totally positive functions*, first posted 2014-11-06, arXiv:1411.1539. Different one-zero class for comparison.
