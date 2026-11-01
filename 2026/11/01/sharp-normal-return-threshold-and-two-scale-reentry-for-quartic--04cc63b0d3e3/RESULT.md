# Sharp normal-return threshold and two-scale reentry for quartic polynomial lemniscates

## Finding
Let \(A>0\), and let
\[
\Omega_A=\{z\in\mathbb C:|z^4+iA|<\sqrt{1+A^2}\},\qquad
\gamma_A(t)=1+t(1+iA),\quad t\ge0.
\]
The point \(1\) lies on the real-analytic Jordan boundary of \(\Omega_A\), and \(\gamma_A\) is its outward normal ray (with a non-unit-speed parameter). Define the integer polynomial
\[
\begin{aligned}
P(X)={}&800000X^{12}-109124375X^{11}+171058713X^{10}-81950155X^9\\
&+21890925X^8-3445758X^7+64450X^6+91970X^5\\
&-7342X^4-107X^3+101X^2+9X+1.
\end{aligned}
\]
There is precisely one root \(X_*\) of \(P\) in \((7,\infty)\), lying in \((134,135)\). Put \(A_*=\sqrt{X_*}=11.6114237715954\ldots\). Then:

1. For \(0<A<A_*\), the ray meets \(\overline{\Omega_A}\) only at its starting point \(t=0\). For \(A=A_*\), it additionally touches the boundary at exactly one parameter \(t_*=0.12875861876179\ldots>0\), without entering \(\Omega_A\).
2. For every \(A>A_*\), there are exactly two parameters \(0<t_-(A)<t_+(A)\) at which the ray meets the boundary again. Both crossings are transverse, and \(\gamma_A(t)\in\Omega_A\) holds exactly for \(t_-<t<t_+\).
3. As \(A\to\infty\), the two crossings have different scales:
\[
\begin{split}
t_-(A)&=A^{-1}+\frac{31}{16}A^{-2}+O(A^{-3}),\\
t_+(A)&=8^{1/5}A^{-4/5}-8^{-1/5}A^{-6/5}+O(A^{-8/5}).
\end{split}
\]
The outward signed curvature at \(1\) is \(\kappa_A(1)=(1+A^2)^{-1/2}>0\). Thus every \(A>A_*\) meets the positive-curvature normal-return hypothesis used for constructing polynomial mean-value counterexamples. This theorem classifies this particular ray and quartic family; it does not assert a global minimal parameter among all boundary points or all polynomial families.

## Assumptions and scope
The parameter \(A\) is any positive real number. An **interior normal return** means that there exists \(t>0\) with \(\gamma_A(t)\in\Omega_A\); mere tangency to the boundary does not count. The powers and absolute values use the ordinary complex modulus. The asymptotic bounds hold as \(A\to+\infty\) with absolute implicit constants sufficiently far out.

The boundary is a real-analytic Jordan curve: along a ray \(z=re^{i\theta}\), the boundary equation is \(s^2+2A\sin(4\theta)s-1=0\), where \(s=r^4\). Its unique positive solution \(s=\sqrt{1+A^2\sin^2(4\theta)}-A\sin(4\theta)\) is positive and real analytic in \(\theta\). The defining function \(\varphi_A(z)=|z^4+iA|^2-(1+A^2)\) has gradient \((8,8A)\) at \(z=1\), proving that \(1+iA\) is outward normal. Its Hessian there is \(\bigl(\begin{smallmatrix}56&24A\\24A&8\end{smallmatrix}\bigr)\); the level-curve curvature formula yields \(\kappa_A(1)=1/\sqrt{1+A^2}\).

## Proof
**1. Polynomial reduction.** Put \(X=A^2\). Directly expand \(\varphi_A(\gamma_A(t))\) to obtain the exact factorization
\[
\varphi_A(\gamma_A(t))=t(1+X)H(t,X),
\]
where
\[
\begin{aligned}
H(t,X)={}&(X+1)^3t^7+8(X+1)^2t^6+(4X^2+32X+28)t^5\\
&+(24X+56)t^4+(70-2X)t^3+(56-8X)t^2+28t+8.
\end{aligned}
\]
Thus \(\gamma_A(t)\in\Omega_A\) for \(t>0\) if and only if \(H(t,A^2)<0\). For \(0<X\le7\), every displayed coefficient is nonnegative and the constant term is positive, so there is no return. For \(X>7\), the nonzero coefficients of \(H\), in descending degree order, exhibit at most two sign changes. Descartes' rule of signs therefore permits at most two positive zeros, counted with multiplicity.

**2. A single monotone transition.** Set \(v=At\), so \(t=v/A\). With \(X=v^2/t^2\), the same polynomial becomes
\[
\begin{aligned}
H(t,v^2/t^2)={}&t^7+8t^6+(3v^2+28)t^5+(16v^2+56)t^4\\
&+(3v^4+32v^2+70)t^3+(8v^4+24v^2+56)t^2\\
&+(v^6+4v^4-2v^2+28)t+8(1-v^2).
\end{aligned}
\]
All coefficients of positive powers of \(t\) are strictly positive for \(v\ge0\): the only potentially problematic coefficient satisfies \(v^6+4v^4-2v^2+28\ge 4(v^2-1/4)^2+111/4>0\). Consequently for each fixed \(v>0\), the quantity \(H(v/A,A^2)\) strictly decreases as \(A\) increases. If it is negative at one \(A\), it remains negative at every larger \(A\). An interior return occurs for sufficiently large \(A\), since for fixed \(v=2\), \(H(2/A,A^2)\to8(1-4)<0\). No return occurs for \(A\le\sqrt7\).

It follows that a unique transition parameter \(A_*\in(\sqrt7,\infty)\) separates absence and presence of an interior return. This transition is attained at a positive finite parameter \(t_*\): on a compact interval of \(A\)-values around it, \(H(0,A^2)=8\) uniformly, while \(H(t,A^2)\to+\infty\) uniformly as \(t\to\infty\). Hence \(H(t_*,A_*^2)=\partial_tH(t_*,A_*^2)=0\).

**3. Exact elimination and uniqueness.** The Sylvester determinant gives the finite polynomial identity
\[
\operatorname{Res}_t(H,\partial_tH)
=-262144(X-1)(X+1)^9P(X).
\]
The shifted polynomial \(P(7+Y)\) has positive leading coefficient \(800000\), and all of its twelve lower coefficients are strictly negative. For reproducibility, those lower coefficients in descending degree order are
\[
\begin{split}
-41924375,&\ -5644318162,\ -221830030870,\ -4853054509800,\\
-68916161844048,&\ -676448285041472,\ -4709410955464960,\\
-23317462112719872,&\ -80580670228697088,\\
-185264572138700800,&\ -255174029696630784,\\
&-159565278833016832.
\end{split}
\]
Descartes' rule gives at most one root \(X>7\). Exact substitution gives \(P(134)<0<P(135)\), so there is exactly one such root; it must equal \(A_*^2\). The earlier factor \(X-1\) is irrelevant because \(A_*^2>7\).

At the threshold \(H\ge0\) for \(t>0\), with a double root at \(t_*\). It is exactly double, since Descartes' rule allows at most two positive roots including multiplicities. For \(A>A_*\), strict negativity somewhere and positivity at \(t=0\) and for large \(t\) force exactly two distinct simple positive roots, with negativity precisely between them. This also proves the claimed absence and tangency statements at and below the threshold.

**4. Two asymptotic crossing scales.** For bounded positive \(v\), the rescaled identity in Step 2 gives
\[
H(v/A,A^2)=8(1-v^2)+A^{-1}v(v^6+4v^4-2v^2+28)+O(A^{-2}).
\]
The first crossing has \(v=At_-\to1\); the implicit-function theorem at the simple zero \(v=1\) yields \(v=1+31/(16A)+O(A^{-2})\). For the second crossing put \(t=A^{-4/5}w\). Uniformly for \(w\) near \(\rho=8^{1/5}\),
\[
A^{-2/5}H(A^{-4/5}w,A^2)
=w^7-8w^2+A^{-2/5}(4w^5+8)+O(A^{-4/5}).
\]
The leading polynomial has a simple positive zero at \(w=\rho\), with derivative \(40\rho\). The implicit-function theorem yields \(w=\rho-\rho^{-1}A^{-2/5}+O(A^{-4/5})\). The existence of exactly two crossings and sign tests on either side of these roots identify them with \(t_-\) and \(t_+\), completing the proof.

## Verification
The standalone `CHECK.py` uses exact symbolic algebra to rederive the boundary factorization and Sylvester resultant, check all twelve coefficient signs for the shifted polynomial, and verify the rescaling formula. It also checks the original parameter \(A=64\) with the exact rational interior point \(t=1/32\), numerically isolates \(A_*\) and \(t_*\), and performs supplementary root checks for four parameter values above threshold. Running `python CHECK.py` requires Python 3, SymPy and mpmath. Numerical tests do not establish the universal root count or asymptotics; Steps 1–4 above do.

## Relationship to prior work
The September 2026 public polynomial counterexample to Smale's mean-value bound uses the quartic lemniscate \(|z^4+64i|<\sqrt{4097}\) and an interior outward-normal point. A later October 2026 analysis of its geometric mechanism studies the wider binomial lemniscate family \(|z^m+iA|<\sqrt{1+A^2}\) and proves a sufficient normal-return criterion, but its examined Section 4.3 does not classify the sharp quartic parameter or the two crossing scales. The present theorem settles exactly when that **specific normal ray at \(z=1\)** returns in the quartic family; it does not improve the universal mean-value constant, classify all normal rays, or claim a new counterexample independent of the existing construction.

## Limitations
The threshold is for the specified quartic polynomial family and the ray from \(z=1\) only. It is not a threshold for nonconvexity, for returns from other boundary points, or for the existence of alternative counterexample constructions. The connection to mean-value counterexamples uses the already published sufficient geometric criterion; our original contribution is the exact phase diagram and asymptotic ray geometry. Independent verification of scientific originality has not been performed; equivalence with unindexed classical lemniscate-discriminant calculations remains a residual risk.

## References
1. T. Adamczewski, *Smale's Mean Value Conjecture (K=1): disproof*, public repository first reported September 3, 2026, https://github.com/tadamcz/mean-value-problem (mathematical proof account, quartic seed).
2. T. Adamczewski and M. J. Colbrook, *From boundary geometry to counterexamples in Smale's mean value problem*, arXiv:2610.36158v1, October 26, 2026, https://arxiv.org/html/2610.36158v1 (Sections 3 and 4, especially Proposition 4.4).
3. A. Jatar and T. W. Ng, *Smale's Mean Value Conjecture and its Dual Conjecture for Complex Polynomials*, arXiv:2608.27047v1, August 27, 2026, https://arxiv.org/abs/2608.27047 (related global mean-value extremal problem, not a quartic ray classification).
