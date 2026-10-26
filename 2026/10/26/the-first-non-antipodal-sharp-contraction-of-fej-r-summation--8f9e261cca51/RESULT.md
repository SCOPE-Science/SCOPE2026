# The first non-antipodal sharp contraction of Fejér summation

## Finding

Let \(F_n(t)=\sum_{|k|<n}(1-|k|/n)e^{ikt}\) on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with normalized Haar integration. Let \(T_nf=F_n*f\), acting on real continuous functions, and let \(\operatorname{osc}(f)=\max f-\min f\). Set
\[
\delta_n=\sup_{\operatorname{osc}(f)>0}\frac{\operatorname{osc}(T_nf)}{\operatorname{osc}(f)}.
\]
For the first three nonconstant Fejér means,
\[
\delta_2=\frac{2}{\pi},\qquad\delta_3=\frac{8}{3\pi},\qquad
\delta_4=\frac{\sqrt{1-c_*^2}}{\pi}\,\frac{-4(4c_*^4-5c_*^3-12c_*^2-8c_*-2)}{3(1+2c_*)^2},
\]
where \(c_*\) is the unique zero in \((0,2/3)\) of
\[
8c^5-20c^3-14c^2+c+2=0.
\]
Numerically, \(c_*=0.3381071853346558859\ldots\) and \(\delta_4=0.8838823778291968490\ldots\). For \(n=2,3\), precisely antipodal pairs of output evaluations maximize the total-variation distance of the transition kernels. For \(n=4\), the maximizing angular separation is uniquely \(2\arccos(c_*)=2.4517828410692279\ldots<\pi\), up to reversal and simultaneous rotation. The antipodal separation instead gives exactly \(8/(3\pi)\), strictly below \(\delta_4\). Thus order four is the first Fejér order exhibiting a non-antipodal worst pair.

## Assumptions and scope

Functions and oscillations are real-valued; the operator acts on \(C(\mathbb T;\mathbb R)\) modulo constants. The normalization \(F_n\ge0\) and \((2\pi)^{-1}\int F_n=1\) is essential. A maximizing pair of output locations exists, but for the continuous-input operator the sharp seminorm is a supremum, not necessarily achieved by a continuous input. The result is a **one-step** oscillation coefficient for \(n=2,3,4\), not a claim about higher orders, powers, or asymptotic mixing.

## Proof

**Kernel-pair reduction.** Because \(T_n1=1\), normalize \(0\le f\le1\). For any output points \(x,y\), the supremum of \((T_nf)(x)-(T_nf)(y)\) over bounded measurable \(f\) equals the total-variation distance of their kernel probability measures. Continuous approximations to the sign test yield the same supremum on \(C(\mathbb T)\). Rotation invariance therefore gives
\[
\delta_n=\max_{0\le\theta\le\pi}\frac{1}{4\pi}\int_{-\pi}^{\pi}|F_n(z+\theta/2)-F_n(z-\theta/2)|\,dz.
\]
Write \(a=\theta/2\), \(c=\cos a\); then \(\sin a=\sqrt{1-c^2}\), \(0\le c\le1\).

**The first two orders.** Since \(F_2(t)=1+\cos t\), direct integration gives \(\delta_2(\theta)=2\sin a/\pi\), uniquely maximal at \(c=0\). Since \(F_3(t)=1+(4/3)\cos t+(2/3)\cos2t\),
\[
\delta_3(\theta)=\frac{4\sin a}{3\pi}\int_{-1}^{1}|1+2cu|\,du
=\frac{4\sqrt{1-c^2}}{3\pi}\begin{cases}2,&0\le c\le1/2,\\2c+(2c)^{-1},&1/2<c\le1.\end{cases}
\]
On the second branch, \(\sqrt{1-c^2}(2c+(2c)^{-1})<2\): after squaring and multiplying by \(4c^2\), the positive difference factors as \((1+c(2c-1)^2)(4c^3+4c^2+c-1)>0\) for \(c>1/2\). Hence \(\delta_3\) is uniquely maximal at \(c=0\).

**Fourth order and sign geometry.** With \(F_4(t)=1+(3/2)\cos t+\cos2t+(1/2)\cos3t\), elementary trigonometric identities give
\[
F_4(z+a)-F_4(z-a)=-2\sin a\sin z\,p_c(\cos z),
\quad p_c(u)=2((2c-1)u+1-c)((2c+1)u+1+c).
\]
Consequently, defining \(I(c)=\int_{-1}^{1}|p_c(u)|\,du\), we have \(\delta_4(\theta)=\sqrt{1-c^2}\,I(c)/\pi\). The roots of \(p_c\) are \(r=-(1+c)/(1+2c)\) and \(s=(1-c)/(1-2c)\) (the latter interpreted by continuity at \(c=1/2\)). Exactly one root lies in \((-1,1)\) when \(0<c<2/3\); the two roots are inside when \(c>2/3\), exchanging order at \(c=1/\sqrt2\). Integrating the signed polynomial on these intervals yields the exhaustive, continuous, piecewise formula
\[
I(c)=\begin{cases}
-\dfrac{4(4c^4-5c^3-12c^2-8c-2)}{3(2c+1)^2},&0\le c\le2/3,\\[3pt]
-\dfrac{4(16c^6-72c^4+39c^2-6)}{3(2c-1)^2(2c+1)^2},&2/3\le c\le1/\sqrt2,\\[3pt]
\dfrac{4(48c^6-24c^4+9c^2-2)}{3(2c-1)^2(2c+1)^2},&1/\sqrt2\le c\le1.
\end{cases}
\]

**Global optimization.** On \([0,2/3]\), let \(H(c)=(1-c^2)I(c)^2\). Direct differentiation gives
\[
H'(c)=-\frac{32c(4c^4-5c^3-12c^2-8c-2)(8c^5-20c^3-14c^2+c+2)}{3(2c+1)^5}.
\]
The quartic factor is negative. The quintic \(h(c)=8c^5-20c^3-14c^2+c+2\) is positive on \([0,1/28]\): bound its negative terms by \(20/28^3+14/28^2<2\). On \([1/28,2/3]\), \(h'(c)=40c^4-60c^2-28c+1<0\), since \(40c^4\le(160/9)c^2<60c^2\). Moreover \(h(2/3)=-2048/243\). Thus \(h\) has exactly one zero \(c_*\), and \(H\) strictly increases before it and decreases afterward (apart from the stationary endpoint \(c=0\)).

The remaining two branches also strictly decrease. Indeed their differentiated squared coefficients have respective factors
\[
-\frac{32c A(c)Q(c^2)}{3(2c-1)^5(2c+1)^5},\qquad
-\frac{32c B(c)R(c^2)}{3(2c-1)^5(2c+1)^5},
\]
where
\[
A(c)=16c^6-72c^4+39c^2-6,\quad Q(x)=64x^4-176x^3+100x^2-7x-4,
\]
\[
B(c)=48c^6-24c^4+9c^2-2,\quad R(x)=192x^4-272x^3+124x^2-9x-4.
\]
On \(4/9\le x\le1/2\), the Bernstein coefficients of \(A(\sqrt{x})\) are \((-1082/729,-287/162,-19/9,-5/2)\), and those of \(Q\) are \((-2048/6561,-605/1944,-331/972,-29/72,-1/2)\); hence both factors are strictly negative. On \(1/2\le x\le1\), the Bernstein coefficients of \(B(\sqrt{x})\) are \((5/2,6,27/2,31)\), and those of \(R\) are \((1/2,11/8,29/12,57/8,31)\); hence both are strictly positive. The displayed derivatives are negative throughout their respective open intervals. No global maximum occurs beyond \(c_*\). Since \(c_*>0\) and \(H\) initially increases, antipodal separation \(c=0\) is strictly suboptimal for \(F_4\). The integral at \(c=0\) equals \(8/3\), completing the numerical and equality assertions.

## Verification

Run `python3 CHECK.py` using only the Python standard library. The checker tests the factorized integral formulas over rational points, verifies all four Bernstein-sign certificates exactly as rational arithmetic, isolates the quintic root by bisection, and corroborates the kernel total-variation integral by midpoint quadrature at specified separations. The printed value is `CHECK_OK c=0.338107185334656 angle=2.451782841069228 delta=0.883882377829197`. The infinite-dimensional sharpness and global extremum are proved above, not inferred from quadrature.

## Relationship to prior work

Weisz's survey (first public arXiv version dated June 8, 2012) presents the classical Fejér convolution kernel and convergence results, notably Section 3; it does not evaluate this precise oscillation coefficient. Gaubert and Qu (first public arXiv version dated July 17, 2013) develop the general Doeblin–Dobrushin/Hopf-oscillation contraction principle, from which the kernel-pair variational reduction follows; their Section 5–6 results do not evaluate the Fejér four-term optimization. The present calculation specializes the general principle but adds an explicit algebraic optimum, proof of uniqueness, and the first non-antipodal shift of worst-case kernel separation. Searches of the relevant mathematical database and literature found no equivalent evaluated result; absence from indexed searches does not prove priority.

## Limitations

The claim is restricted to real oscillation on the circle and Fejér orders two, three, and four. No larger-order parity rule, optimal higher-iterate constant, or mixing-time formula is asserted. The sharp constant is an operator-norm supremum on continuous inputs; the formal maximizing sign test may be discontinuous. No independent mathematical audit has been performed. An unindexed equivalent exact calculation remains possible.

## References

1. Ferenc Weisz, *Summability of Multi-Dimensional Trigonometric Fourier Series*, Surveys in Approximation Theory 7 (2012), 1–179; arXiv:1206.1789v1, first submitted June 8, 2012. See especially Section 3, Fejér kernel definition and convolution.
2. Stéphane Gaubert and Zheng Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649v1, submitted July 17, 2013. See especially Theorems 5.1 and 6.2 and the total-variation duality.
