# A sharp loss-peak resolution wedge and cusp law for two Debye relaxations

## Finding
For two strictly positive Debye dielectric relaxation strengths with distinct positive relaxation times, the frequency loss spectrum has at most two strict local maxima. The **exact condition** for two maxima (a resolved double peak) is the following phase wedge.

Let \(0<\tau_1<\tau_2\) and \(\Delta_1,\Delta_2>0\). Define
\[
\rho=\frac{\tau_2}{\tau_1},\quad q=\rho^2,\quad \lambda=\frac{\Delta_2}{\Delta_1},\quad q_c=17+12\sqrt2,\quad \rho_c=3+2\sqrt2.
\]
For \(q>q_c\), put
\[
x_\pm(q)=\frac{q+1\pm\sqrt{q^2-34q+1}}{6q},\qquad
J_q(x)=\frac{(1-x)(1+qx)^2}{\sqrt q\,(qx-1)(1+x)^2},\qquad
\lambda_-=J_q(x_-),\quad \lambda_+=J_q(x_+).
\]
Then there are **exactly two strict local maxima separated by one strict local minimum** if and only if
\[
\boxed{\rho>3+2\sqrt2\quad\text{and}\quad\lambda_-(q)<\lambda<\lambda_+(q).}
\]
Otherwise there is exactly one strict local maximum (possibly accompanied by a stationary shoulder). The wedge is symmetric under strength exchange:
\[
0<\lambda_-<1<\lambda_+,\qquad \lambda_-\lambda_+=1.
\]
At either strength boundary, the second potential peak has collapsed into a horizontal stationary shoulder, not a second local maximum. At \(\rho=\rho_c,\lambda=1\), the unique peak at \(\omega=(\tau_1\tau_2)^{-1/2}\) is quartically flat.

The wedge opens with an **exact three-halves cusp**. As \(q=q_c+\varepsilon\) decreases to \(q_c\) from above,
\[
\log\lambda_+(q)=C\varepsilon^{3/2}+O(\varepsilon^{5/2}),\qquad
\log\lambda_-(q)=-C\varepsilon^{3/2}+O(\varepsilon^{5/2}),
\]
where
\[
\boxed{C=\frac{(24\sqrt2)^{3/2}}{108(17+12\sqrt2)(16+12\sqrt2)}=0.001634694128180648\ldots.}
\]
Thus two mathematically distinct peaks require both a sufficiently large time-scale separation and a sufficiently balanced pair of strengths. At equal strengths and \(\rho>\rho_c\), the two peak frequencies are explicit:
\[
\omega_\pm=\frac{\exp\big(\pm\operatorname{arcosh}(\sinh(\tfrac12\log\rho))\big)}{\sqrt{\tau_1\tau_2}}.
\]

## Assumptions and scope
The complex susceptibility is the additive **two-Debye** response
\[
\chi(\omega)=\chi_\infty+\frac{\Delta_1}{1-i\omega\tau_1}+\frac{\Delta_2}{1-i\omega\tau_2},\qquad\omega>0,
\]
with real \(\chi_\infty\), strictly positive \(\Delta_i\) and \(\tau_i\), and no conductivity term or additional relaxation/band contribution. With the stated phase convention the dissipative imaginary part is
\[
\mathcal L(\omega)=\Delta_1\frac{\omega\tau_1}{1+(\omega\tau_1)^2}
+\Delta_2\frac{\omega\tau_2}{1+(\omega\tau_2)^2}>0.
\]
By a **resolved double peak** we mean precisely two strict local maxima of \(\mathcal L\) as a function of positive frequency, separated by a strict local minimum. The same definition applies on logarithmic frequency, because logarithm is a smooth increasing change of variable. This is a mathematical peak-count criterion, not a statistical assertion about noisy spectral fitting.

## Proof
Write \(y=\omega\tau_1>0\), \(x=y^2\) and \(\rho=\sqrt q\). Apart from an irrelevant positive factor \(\Delta_1\),
\[
F(y)=\frac{y}{1+y^2}+\lambda\frac{\rho y}{1+\rho^2y^2}.
\]
Differentiate directly:
\[
F'(y)=\frac{1-x}{(1+x)^2}+\lambda\sqrt q\frac{1-qx}{(1+qx)^2}.
\]
Both terms are positive when \(x<1/q\); both are negative when \(x>1\). Hence every stationary point lies in the open interval \((1/q,1)\). On that interval the derivative has the same sign as \(J_q(x)-\lambda\), where the displayed \(J_q\) is positive, tends to \(+\infty\) at the left endpoint, and tends to \(0\) at the right endpoint.

An exact logarithmic derivative identity is
\[
\frac{J_q'(x)}{J_q(x)}=-\frac{(q-1)P_q(x)}{(1-x^2)(q^2x^2-1)},\qquad
P_q(x)=3qx^2-(q+1)x+3.
\]
The denominator is strictly positive throughout \((1/q,1)\). The discriminant of \(P_q\) is \(q^2-34q+1\). Its two zeros in \(q\) are \(17\pm12\sqrt2\), of which only \(q_c=17+12\sqrt2\) is greater than one. Thus, for \(1<q<q_c\), \(P_q>0\) and \(J_q\) strictly decreases. At \(q=q_c\), its derivative vanishes only at one interior point but \(J_q\) remains strictly decreasing. In both cases each positive \(\lambda\) intersects \(J_q\) exactly once, so \(F\) has one strict maximum.

When \(q>q_c\), the two zeros \(x_-<x_+\) of \(P_q\) are both in \((1/q,1)\). Indeed its vertex \((q+1)/(6q)\) is interior, its minimum is negative, and \(P_q(1/q)=2+2/q>0\), \(P_q(1)=2q+2>0\). Therefore \(J_q\) decreases on \((1/q,x_-)\), increases on \((x_-,x_+)\), and decreases on \((x_+,1)\). A horizontal line at height \(\lambda\) meets all three branches exactly when \(\lambda_-<\lambda<\lambda_+\), yielding the sign sequence \(+,-,+,-\) of \(F'\), and precisely two strict maxima and one strict minimum. Else the line crosses once, except at an endpoint height when a tangency produces a double stationary root plus a simple maximum. Such a tangency has no sign reversal and is a stationary shoulder. There cannot be more than three stationary points because the derivative numerator is cubic in \(x\).

The identity
\[
J_q(x)J_q\!\left(\frac{1}{qx}\right)=1
\]
holds algebraically. Since \(x_-x_+=1/q\), it gives \(\lambda_-\lambda_+=1\), and strict increase between the extrema gives \(\lambda_-<1<\lambda_+\).

For the cusp coefficient, complete the square in the critical quadratic. With
\[
m=\frac{q+1}{6q},\quad h=\frac{\sqrt{q^2-34q+1}}{6q},\quad D(x,q)=(1-x^2)(q^2x^2-1),
\]
one has \(P_q(x)=3q((x-m)^2-h^2)\). Hence
\[
\log\frac{\lambda_+}{\lambda_-}=
\int_{m-h}^{m+h}\frac{3q(q-1)(h^2-(x-m)^2)}{D(x,q)}\,dx.
\]
At \(q=q_c\), \(m=1/\sqrt{q_c}\) and \(D(m,q_c)=(q_c-1)^2/q_c>0\). Uniformly on the shrinking integration interval, Taylor expansion of the smooth reciprocal denominator, with odd terms integrating to zero, gives
\[
\log\frac{\lambda_+}{\lambda_-}
=\frac{[q^2-34q+1]^{3/2}}{54q_c(q_c-1)}+O((q-q_c)^{5/2}).
\]
Since \(\lambda_-\lambda_+=1\) and \(q^2-34q+1=(q-q_c)(q-(17-12\sqrt2))\), the displayed three-halves law follows with coefficient \(C\).

Finally suppose \(\Delta_1=\Delta_2=A\). Set \(s=\log(\omega\sqrt{\tau_1\tau_2})\), \(a=\tfrac12\log\rho\). Using \(u/(1+u^2)=1/(2\cosh(\log u))\),
\[
\mathcal L(s)=\frac A2[\operatorname{sech}(s-a)+\operatorname{sech}(s+a)]
=A\frac{\cosh a\cosh s}{\cosh^2s+\sinh^2a}.
\]
As a function of \(v=\cosh s\ge1\), the last factor is proportional to \(v/(v^2+\sinh^2a)\). Its maximum occurs at \(v=1\) for \(\sinh a\le1\), and at \(v=\sinh a>1\) otherwise, proving the explicit frequency formula and exactly the same critical ratio \(\rho_c=(1+\sqrt2)^2\). At equality the expansion is
\[
\mathcal L(s)=A\sqrt2\left(\frac12-\frac{s^4}{16}+O(s^6)\right),
\]
so the merged peak is quartically flat.

## Verification
The standalone \(\texttt{check_resolution.py}\) implements symbolic differentiation, the exact discriminant and reciprocal identities, the symmetric hyperbolic representation, the quartic-critical Taylor coefficient, rational stationary-root counts in contrasting regimes, and high-precision checks of the cusp coefficient. Invoke with \(\texttt{python check_resolution.py}\) using Python, SymPy and mpmath. The symbolic identities and proof above establish the infinite-parameter result; finite root-count checks and asymptotic samples are corroboration, not substitutes for proof.

## Relationship to prior work
Jakobsen, Maggi, Christensen and Dyre (2008, arXiv:0805.4519) experimentally distinguish a dominant Debye-type relaxation from another, generally non-Debye relaxation and discuss overlap and potential merger. Julrat, Chongcheawchamnan and Robertson (2014) use an extended Debye model with two mechanisms. Elton (2017, arXiv:1704.01667), especially its discussion of overlapping modes and Table I, surveys multiple-Debye fits and the difficulty of interpreting excess dielectric response. These works motivate but do not provide the phase wedge or its cusp coefficient.

Došlá (2009) proves general modality criteria for mixtures of two unimodal densities and explicitly studies logistic and Cauchy components. In logarithmic frequency, a Debye loss line is a translated hyperbolic-secant kernel, not a logistic \(\operatorname{sech}^2\) density. Her general derivative-ratio criterion is relevant broader methodology, and could be specialized to this kernel, but the exact algebraic time-scale threshold, reciprocal strength wedge and three-halves opening derived here are not stated in the inspected text. The quantitative threshold is therefore the delimited contribution; neither the Debye response itself nor the general derivative-ratio principle is claimed as new.

## Limitations
The theorem counts mathematically exact peaks in a noiseless, additive, two-Debye spectrum only. Conductive background, non-Debye relaxation, distributed relaxation times, and oscillator resonances can change the count. A single observed peak **does not imply** a single physical relaxation; conversely, two mathematical maxima may not be experimentally resolvable in finite bandwidth or noise. The formula gives no statistical estimator error bounds or uniqueness of fitting parameters from finite samples. The generic mixture theorem is a significant related predecessor; specialized prior closed-form results outside the inspected literature remain a priority risk.

## References
1. B. Jakobsen, C. Maggi, T. Christensen, J. C. Dyre, *Investigation of the shear-mechanical and dielectric relaxation processes in two mono-alcohols close to the glass transition*, arXiv:0805.4519, first submitted 2008-05-29. https://arxiv.org/abs/0805.4519
2. Š. Došlá, *Conditions for bimodality and multimodality of a mixture of two unimodal densities*, Kybernetika **45** (2009), 279–292. https://dml.cz/handle/10338.dmlcz/140075
3. S. Julrat, M. Chongcheawchamnan, I. D. Robertson, *Characterisation of the dielectric properties of rubber latex from 0.5 to 33 GHz*, Biosystems Engineering **125** (2014), 1–8, doi:10.1016/j.biosystemseng.2014.06.013. https://eprints.whiterose.ac.uk/id/eprint/82386/
4. D. C. Elton, *The origin of the Debye relaxation in liquid water and fitting the high frequency excess response*, arXiv:1704.01667, 2017. https://arxiv.org/abs/1704.01667
