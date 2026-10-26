# A sharp high-frequency ambiguity-zero dichotomy for three distinct exponential factors

## Finding
Fix \(0<a<b\), \(r>0\). For the three-factor exponential convolution \(f=\eta_a*\eta_b*\check\eta_r\) defined below, a sharp dichotomy governs self-ambiguity zeros at high **angular** frequency and fixed positive delay.

If \(0<r<a\), a unique positive balanced delay \(T_*\) supports two conjugate-frequency strings of genuine isolated transverse zeros. For all sufficiently large positive integers \(n\),
\[
 A_f(T_n,\pm\omega_n)=0,\qquad T_n=T_*+O_{a,b,r}(n^{-1}),\qquad
 \omega_nT_n=(2n+1)\pi+O_{a,b,r}(n^{-1}).
\]
In every compact band \(K\subset(0,\infty)\), and at all sufficiently large absolute angular frequencies, every zero must have delay arbitrarily close to \(T_*\). More precisely, if \(T_*\) is in the interior of \(K\), these two strings exhaust the high-frequency zeros with delay in \(K\); if \(T_*\notin K\), none occur. This exhaustion assertion is restricted to bands whose boundaries do not equal \(T_*\).

If \(r\ge a\), then for every compact \(K\subset(0,\infty)\), there is \(\Omega_K<\infty\) such that \(A_f(T,\omega)\ne0\) whenever \(T\in K\), \(|\omega|>\Omega_K\). Nothing is asserted about delays tending to zero or infinity with frequency, or finite-frequency zeros.

For the fully distinct rational-rate example \((a,b,r)=(2,3,1)\), the balanced delay is exactly \(T_*=\log3\).

## Assumptions and scope
For \(q>0\), define \(\eta_q(t)=e^{-qt}\mathbf1_{[0,\infty)}(t)\), \(\check\eta_q(t)=e^{qt}\mathbf1_{(-\infty,0]}(t)\). Convolution is the ordinary Lebesgue convolution on the real line. The strictly positive real window \(f=\eta_a*\eta_b*\check\eta_r\) is in \(L^1\cap L^2\), is continuously differentiable, and has a jump in its second derivative. We use the angular convention
\[
 A_f(T,\omega)=\int_{\mathbb R} f(u+T/2)f(u-T/2)e^{-i\omega u}\,du,
\]
where \(T,\omega\in\mathbb R\). For a real window, \(A_f(T,-\omega)=\overline{A_f(T,\omega)}\), and interchange of the factors gives \(A_f(-T,\omega)=A_f(T,\omega)\). Thus positive delays suffice for the high-frequency analysis.

## Proof
**1. Explicit pulse and jump.** Successive convolution and elementary integration yield
\[
 f(t)=\begin{cases}
 e^{rt}/[(a+r)(b+r)],&t<0,\\
 \bigl(e^{-at}/(a+r)-e^{-bt}/(b+r)\bigr)/(b-a),&t\ge0.
 \end{cases}
\]
Both one-sided values and first derivatives coincide at zero. Direct differentiation gives \(f''(0+)-f''(0-)=-1\). For any fixed \(T>0\) the correlation \(h_T(u)=f(u+T/2)f(u-T/2)\) is \(C^1\); its second derivative has jumps \(-f(-T)\) at \(u=-T/2\), and \(-f(T)\) at \(u=T/2\).

**2. A uniform Fourier-jump law.** In distributions, \(D^3h_T\) equals an integrable, piecewise-exponential regular part plus the two point masses just described. Taking Fourier transforms gives
\[
 (i\omega)^3 A_f(T,\omega)
 =-f(-T)e^{i\omega T/2}-f(T)e^{-i\omega T/2}+R(T,\omega),
 \qquad R(T,\omega)=O_K(|\omega|^{-1})
\]
uniformly for \(T\) in each compact \(K\subset(0,\infty)\). The regular part is a finite sum of exponentials on three intervals, and its Fourier transform is a finite sum of endpoint terms divided by affine functions of \(i\omega\). Hence this asymptotic expansion is also \(C^1\) in \(T\) and in the rescaled phase \(\phi=\omega T-(2n+1)\pi\), with the remainder and its first derivatives \(O_K(n^{-1})\) when \(\omega=((2n+1)\pi+\phi)/T\) for bounded \(\phi\). This derivative estimate follows directly by differentiating the finite exponential integral formulas; a merely pointwise Fourier asymptotic would not be sufficient for the implicit-function step.

**3. Exact balanced-delay classification.** The ratio of the two jump amplitudes is
\[
 \rho(T)=\frac{f(T)}{f(-T)}
 =\frac{(b+r)e^{(r-a)T}-(a+r)e^{(r-b)T}}{b-a},\quad T\ge0.
\]
It obeys \(\rho(0)=1\), \(\rho'(0)=2r>0\). If \(r<a\), write \(u=a-r>0\), \(v=b-r>u\). Then
\[
 (b-a)\rho'(T)=-(b+r)u e^{-uT}+(a+r)v e^{-vT}.
\]
The ratio between its positive and negative terms is strictly decreasing, starting above one, so \(\rho\) increases to one strict maximum and then decreases to zero. Consequently it crosses one at exactly one positive \(T_*\), transversely with \(\rho'(T_*)<0\). If \(r\ge a\), then
\[
 (b-a)\rho'(T)=(b+r)(r-a)e^{(r-a)T}-(a+r)(r-b)e^{(r-b)T}>0\quad(T>0).
\]
Indeed the second term is nonnegative when \(r\le b\); for \(r>b\), the first dominates from \(T=0\) onward, since its initial coefficient exceeds the other by \(2r(b-a)\) and its exponential growth is faster. Thus \(\rho(T)>1\) for all \(T>0\).

**4. True zeros rather than approximate phase cancellation.** For each nonnegative integer \(n\), substitute \(\omega=((2n+1)\pi+\phi)/T\) and multiply the jump law by \(i(-1)^n\). This produces a complex-valued map, whose zero set is unchanged,
\[
 F_n(T,\phi)=f(-T)e^{i\phi/2}-f(T)e^{-i\phi/2}+O_{C^1(K)}(n^{-1}).
\]
The limit \(F_\infty\) has a zero precisely where \(f(T)=f(-T)\) and \(\phi\in2\pi\mathbb Z\). At \((T_*,0)\), the derivative of its real part with respect to \(T\) is nonzero by \(\rho'(T_*)<0\), whereas the derivative of its imaginary part with respect to \(\phi\) equals \(f(T_*)>0\). The cross-derivatives vanish. The real two-dimensional implicit-function theorem, or stable persistence of regular zeros under uniform \(C^1\) perturbations, therefore gives one unique transverse zero \((T_n,\phi_n)\) near \((T_*,0)\) for every sufficiently large \(n\), with errors \(O(n^{-1})\). The \(T,\phi\) to \(T,\omega\) coordinate transformation has nonzero Jacobian \(1/T\), so the zeros remain transverse in the original variables. Conjugation supplies the negative-frequency partners.

For the exhaustion statement, the modulus of the dominant expression is bounded below by \(|f(-T)-f(T)|\), uniformly in the phase. It has a positive lower bound away from the balanced delay on each compact band. Near that delay, \(F_\infty\) vanishes only at odd-multiple-\(\pi\) phases; periodicity, compactness, and uniform \(C^1\) convergence ensure precisely one zero per high-frequency phase cell. When \(r\ge a\), the positive lower bound holds on the entire band, proving the stated high-frequency exclusion.

**5. Explicit example.** For \((a,b,r)=(2,3,1)\), one has \(f(t)=e^t/12\) for \(t<0\), and \(f(t)=e^{-2t}/3-e^{-3t}/4\) for \(t\ge0\). The balance condition is \(4e^{-T}-3e^{-2T}=1\), equivalent to \((e^T-1)(e^T-3)=0\). Its unique positive solution is \(\log3\).

## Verification
An independent algebraic differentiation verifies continuity of \(f,f'\) and the exact second-derivative jump \(-1\). `CHECK.py` evaluates the piecewise-exponential correlation by three exact elementary Fourier integrals, then uses two-real-variable root finding. The recorded checks find genuine small-residual zeros at several frequencies for \((a,b,r)=(2,3,1)\), converging to \(\log3\) as predicted, and check the analytical ratio crossing. These finite checks are supplementary; the infinite-branch theorem follows from the uniform Fourier expansion and implicit-function argument, not from numerical enumeration.

## Relationship to prior work
Gröchenig–Stöckler, arXiv:1104.4894v1, develops the underlying finite-type totally-positive class and Gabor frame properties. Gröchenig–Jaming–Malinnikova, arXiv:1811.03937v1, especially its Section 3, proves nonvanishing for individual exponential factors and their two-factor positive/reflected convolutions. Neither inspected primary statement establishes this all-distinct-rate three-factor high-frequency phase diagram. A separate earlier calculation for the **repeated-rate** subfamily \(\eta_a*\eta_a*\check\eta_r\) supplies a related but lower-dimensional special case; the present claim instead permits three distinct positive rates and identifies the sharp transition at \(r=a\). No assertion of absolute publication novelty is made: an equivalent general exponential-spline asymptotic theorem could subsume this result and merits independent bibliographic checking.

## Limitations
This is a fixed-positive-delay, high-angular-frequency result, not a global classification of all finite-frequency ambiguity zeros. It does not exclude zeros along delays that tend to zero or infinity as frequency grows. The exhaustion statement only applies to compact bands with boundary disjoint from the balanced delay. The derivation uses three exponential factors with exactly two positive and one reflected time direction, distinct positive rates \(a<b\), and no Gaussian factor. A publication-priority risk remains from the broader exponential-spline and time-frequency analysis literature. Independent mathematical audit has not been performed.

## References
1. K. Gröchenig and J. Stöckler, *Gabor Frames and Totally Positive Functions*, arXiv:1104.4894v1, publicly posted April 26, 2011, https://arxiv.org/abs/1104.4894.
2. K. Gröchenig, P. Jaming and E. Malinnikova, *Zeros of the Wigner Distribution and the Short-Time Fourier Transform*, arXiv:1811.03937v1, posted November 9, 2018, especially Section 3, https://arxiv.org/abs/1811.03937.
