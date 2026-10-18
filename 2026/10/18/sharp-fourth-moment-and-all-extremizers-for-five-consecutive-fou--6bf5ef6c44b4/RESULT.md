# Sharp fourth moment and all extremizers for five consecutive Fourier modes

## Finding
For any complex coefficients \(c_0,\ldots,c_4\), set \(P(z)=\sum_{j=0}^{4}c_jz^j\) and give the unit circle normalized Haar measure. Define \(\eta\) as the unique positive real solution to
\[
2\eta^4+8\eta^3-15\eta-6=0,
\]
and define \(\rho>0\) and \(K>0\) by
\[
\rho^2=\frac{2\eta^4+6\eta^3+12\eta+6}{3(\eta^2+4\eta+2)},
\qquad
K=\frac{3(5\eta^4+24\eta^3+36\eta^2+48\eta+18)}{7\eta^4+24\eta^3+12\eta^2+48\eta+24}.
\]
Then the sharp fourth-power Fourier synthesis inequality is
\[
\boxed{\int_{|z|=1}|P(z)|^4\,dm(z)\le K\left(\sum_{j=0}^{4}|c_j|^2\right)^2.}
\]
Numerically, \(\eta=1.348427469827614\ldots\), \(\rho=1.254664554669290\ldots\), and \(K=3.483450219447046\ldots\). **All** nonzero equality vectors, and no others, are
\[
(c_0,c_1,c_2,c_3,c_4)=\lambda(1,\rho e^{i\theta},\eta e^{2i\theta},\rho e^{3i\theta},e^{4i\theta}),
\qquad \lambda\in\mathbb C\setminus\{0\},\quad\theta\in\mathbb R.
\]
The identical sharp inequality and equality classification hold on every cyclic group \(\mathbb Z/N\mathbb Z\) with \(N\ge9\), with \(z\) running through the \(N\)-th roots of unity and normalized counting measure. The continuous-circle fourth-power norm is \(K^{1/4}\).

## Assumptions and scope
The frequency support is the five-term arithmetic progression \(\{0,1,2,3,4\}\). A frequency translation or injective integer dilation on the circle preserves the coefficient norm and the fourth moment. The cyclic assertion uses the five *distinct* standard characters and requires \(N\ge9\); no assertion is made for cyclic orders below nine. Fourier characters are unnormalized and Haar/counting measure is probability normalized. Coefficients can vanish in the inequality but not in the displayed nonzero equality family.

## Proof
**(1) Autocorrelations and coefficient phases.** Put \(a_j=|c_j|\) and \(E=\sum a_j^2\). Parseval applied to \(|P|^2\) gives
\[
\int|P|^4=E^2+2\sum_{h=1}^{4}\left|\sum_{j=0}^{4-h}c_{j+h}\overline{c_j}\right|^2
\le E^2+2\sum_{h=1}^{4}\left(\sum_{j=0}^{4-h}a_{j+h}a_j\right)^2.
\]
Thus a maximizing coefficient vector can be taken nonnegative. The equation for \(h=1\) forces consecutive nonzero coefficients to have the same phase increment whenever all five magnitudes are positive.

**(2) Palindromic root-mean-square reduction.** For nonnegative magnitudes \((a_0,a_1,a_2,a_3,a_4)\) replace both outer entries by \(\alpha=\sqrt{(a_0^2+a_4^2)/2}\), both inner entries by \(\beta=\sqrt{(a_1^2+a_3^2)/2}\), and leave the middle entry \(\gamma=a_2\). The energy \(E\) is unchanged. Writing \(R_h=\sum_j a_ja_{j+h}\), Cauchy--Schwarz and arithmetic--geometric mean yield
\[
\begin{aligned}
R_1&=a_0a_1+a_1\gamma+\gamma a_3+a_3a_4\le2\alpha\beta+2\beta\gamma,\\
R_2&=\gamma(a_0+a_4)+a_1a_3\le2\alpha\gamma+\beta^2,\\
R_3&=a_0a_3+a_1a_4\le2\alpha\beta,\\
R_4&=a_0a_4\le\alpha^2.
\end{aligned}
\]
The outer products satisfy \(a_0a_1+a_3a_4\le2\alpha\beta\) by Cauchy--Schwarz. Since all correlations are nonnegative, their squared sum cannot decrease. If a maximizer has \(\alpha>0\), equality at \(h=4\) forces \(a_0=a_4\); equality at \(h=2\) then forces \(a_1=a_3\) unless those entries both vanish. In any case an optimum exists among palindromic vectors.

**(3) Boundary is suboptimal.** Compactness on \(E=1\) assures a maximum. For a palindromic vector \((\alpha,\beta,\gamma,\beta,\alpha)\), setting any one parameter to zero reduces the exact fourth moment to a one-variable rational maximization. At \(\alpha=0\) or \(\beta=0\), the maximum is \(15/7\), and at \(\gamma=0\) it is \(9/4\). By contrast, the vector \((1,1,1,1,1)\) has fourth-power ratio \(85/25=17/5\), which is strictly greater than all these boundary values. Consequently every maximizing palindromic vector has positive \(\alpha,\beta,\gamma\).

**(4) Two-variable exact maximization.** Scale \(\alpha=1\), set \(x=\beta/\alpha>0\) and \(y=\gamma/\alpha>0\). Direct expansion of the four correlations yields
\[
E(x,y)=2+2x^2+y^2,\qquad
F(x,y)=6x^4+12x^2y^2+24x^2y+24x^2+y^4+12y^2+6.
\]
The target ratio is \(Q(x,y)=F(x,y)/E(x,y)^2\). The numerator of its \(x\)-derivative, \(F_xE-2FE_x\), equals
\[
8x\left[2y^4+6y^3+12y+6-3x^2(y^2+4y+2)\right].
\]
Therefore every positive stationary point satisfies
\[
x^2=\frac{2y^4+6y^3+12y+6}{3(y^2+4y+2)}.
\]
The numerator of the \(y\)-derivative, \(F_yE-2FE_y\), divided by eight, is
\[
3x^4y+6x^4-2x^2y^3-9x^2y^2+6x^2-2y^3+3y.
\]
Substituting the expression for \(x^2\) simplifies the latter exactly to
\[
-\frac{(2y^4+8y^3-15y-6)(7y^4+24y^3+12y^2+48y+24)}{3(y^2+4y+2)^2}.
\]
The second quartic factor is positive for \(y>0\). The first factor has precisely one positive root by Descartes' sign rule and the intermediate-value theorem. Hence there is exactly one positive stationary point, and a global maximum must be that point because all boundaries are strictly inferior. Substitution gives the stated \(\rho\) and \(K\).

**(5) Equality and finite grids.** Positivity of all five optimal magnitudes forces equality in the triangle inequality for lag one. Thus the consecutive phase differences are constant, yielding precisely the claimed affine-phase family. Conversely these vectors make every correlation real and nonnegative after modulation and achieve the optimum. On a cyclic group of order \(N\ge9\), the nine differences \(-4,-3,\ldots,4\) are distinct modulo \(N\); Fourier orthogonality therefore gives exactly the same fourth-moment polynomial and equality conditions. This completes the proof for every stated domain.

## Verification
The standalone program `verify.py` verifies the correlation polynomial, the stationary numerators, exact elimination factorization, radical/algebraic substitutions, positive-root numerical values, the boundary rational expressions, and nonaliasing of differences on seven representative finite grids. Execute `python verify.py` with Python 3 and SymPy. These finite computations corroborate identities but the all-\(N\) theorem rests on the analytic proof and the modular distinctness argument. All algebraic identities were checked symbolically with exact rational polynomial arithmetic.

## Relationship to prior work
The classical Hardy--Littlewood majorant principle at even exponents explains coefficient-phase domination, but does not determine the sharp fixed-five-frequency \(\ell^2\)-to-\(L^4\) constant. The published reflection root-mean-square majorization theorem implies palindromic magnitude reduction for any symmetric spectrum; this known reduction is credited and alone does not imply the quartic or the sharp constant. A published exact optimization for four consecutive modes concerns a different spectral size, and a published five-mode Ferrers calculation concerns a non-isomorphic two-dimensional additive-relation pattern. A previously recorded exact eight-point cyclic computation has a different coefficient because the two endpoints of the autocorrelation spectrum alias at order eight; it does not cover the circle or cyclic orders at least nine.

## Limitations
This result is confined to the fixed five-frequency progression and the cyclic no-aliasing range \(N\ge9\), and supplies no universal formula for arbitrary lengths or exponents. The literature comparison does not prove independent publication priority; an old unindexed special-function or low-degree trigonometric-polynomial calculation may encode the same constant. Independent external audit has not been performed.

## References
1. G. Mockenhaupt and W. Schlag, *On the Hardy-Littlewood majorant problem for random sets*, arXiv:math/0207226v1 (first public 25 July 2002), https://arxiv.org/html/math/0207226v1.
2. B. Green and I. Z. Ruzsa, *On the Hardy-Littlewood majorant problem*, arXiv:math/0303244 (first public 19 March 2003), https://arxiv.org/abs/math/0303244.
3. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1 (first public 12 February 2013), https://arxiv.org/html/1302.2766v1.
4. *Reflection root-mean-square majorization of every even Fourier moment*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-reflection-root-mean-square-majorization-of-every-even-fourier-m--ce42dcffc673.
5. *Sharp fourth-moment norm of the four-term arithmetic progression*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-norm-of-the-four-term-arithmetic-progression--813a0369d1a4.
6. *Sharp fourth moments for a five-point Ferrers Fourier spectrum*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moments-for-a-five-point-ferrers-fourier-spectrum--bb5fd3f72396.
