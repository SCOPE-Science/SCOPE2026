# Right truncation can destroy decreasing generalized mean residual life

## Finding
There exists a nonnegative random variable with an absolutely continuous distribution, positive density on the entire positive half-line, finite moments of all orders, and **strictly decreasing generalized mean residual life** (DGMRL), whose ordinary right-truncated law fails the DGMRL property. An explicit example has survival function
\[
S(x)=\begin{cases}
 e^{-x},&0\le x\le1,\\
 e^{-1-(x-1)/3},&x\ge1.
\end{cases}
\]
Truncating by conditioning on \(X\le T\), where
\[
T=1+3\log(5/4),
\]
produces a law \(Y\) whose generalized mean residual life has strictly **positive** left derivative at \(x=1\):
\[
\lim_{x\uparrow1}\frac{d}{dx}\ell_Y(x)
=11-48\log(5/4)>\frac14.
\]
In particular, the DGMRL class is **not closed under right truncation**. The same positive-threshold counterexample applies if truncation is represented as \(X\mathbf1_{\{X\le T\}}\), which adds an atom at zero: the two constructions have identical residual-life functions at strictly positive thresholds.

## Assumptions and scope
For any nonnegative lifetime \(Z\) with survival function \(S_Z(x)=\Pr(Z>x)>0\), define its mean residual life and generalized mean residual life by
\[
m_Z(x)=\mathbb E[Z-x\mid Z>x]
=\frac{\int_x^\infty S_Z(u)\,du}{S_Z(x)},\qquad
\ell_Z(x)=\frac{m_Z(x)}x,\quad x>0.
\]
The **DGMRL** property means that \(\ell_Z\) is nonincreasing throughout the positive part of the support. A local strictly positive derivative is therefore sufficient to refute DGMRL. All integrals below converge, since \(X\) has an exponential tail. A right-truncated law here means \(Y\overset{d}{=}X\mid\{X\le T\}\), not right censoring at \(T\). The displayed survival is continuous and strictly decreasing, so its distribution function is absolutely continuous; no differentiability at the hazard switch \(x=1\) is assumed or needed.

## Proof
**The original distribution is strictly DGMRL.** On \(0<x<1\), the numerator of the mean residual life is
\[
\int_x^\infty S(u)\,du
=\int_x^1 e^{-u}\,du
+\int_1^\infty e^{-1-(u-1)/3}\,du
=e^{-x}+2e^{-1}.
\]
Consequently,
\[
m_X(x)=1+2e^{x-1}\quad(0<x\le1),
\qquad m_X(x)=3\quad(x\ge1).
\]
These expressions agree at \(x=1\). Differentiating their quotients by \(x\) gives
\[
\ell_X'(x)=\frac{2(x-1)e^{x-1}-1}{x^2}<0
\quad(0<x<1),
\qquad
\ell_X'(x)=-\frac3{x^2}<0\quad(x>1).
\]
Continuity at the switch therefore proves strict decrease over the whole positive axis.

**Right truncation reverses local monotonicity.** Let \(T=1+3\log(5/4)>1\). Then
\[
S(T)=\tfrac45e^{-1},\qquad
S_Y(x)=\frac{S(x)-S(T)}{1-S(T)}\quad(0\le x<T).
\]
For \(x<T\), write \(h_Y(x)=f_X(x)/(S(x)-S(T))\) at density-continuity points. From the left at the hazard switch,
\[
 h_Y(1^-)=\frac{e^{-1}}{e^{-1}-\frac45e^{-1}}=5.
\]
The truncated mean residual life at the switch is exactly
\[
\begin{aligned}
m_Y(1)
&=\frac{\int_1^T[S(u)-S(T)]\,du}{S(1)-S(T)}\\
&=\frac{3e^{-1}(1-\tfrac45)-(T-1)\tfrac45e^{-1}}{\tfrac15e^{-1}}\\
&=3-4(T-1)=3-12\log(5/4).
\end{aligned}
\]
On every open interval of density continuity the standard identity \(m_Y'(x)=h_Y(x)m_Y(x)-1\) follows by differentiation of the survival integral. Hence
\[
\ell_Y'(x)=\frac{x(h_Y(x)m_Y(x)-1)-m_Y(x)}{x^2}.
\]
Taking the left limit at \(x=1\), using continuity of \(m_Y\), yields
\[
\lim_{x\uparrow1}\ell_Y'(x)
=(5-1)[3-12\log(5/4)]-1
=11-48\log(5/4).
\]
The alternating Taylor series at \(z=1/4\) gives the **rigorous strict upper bound**
\[
\log(5/4)<\frac14-\frac1{32}+\frac1{192}
=\frac{43}{192},
\]
and therefore
\[
11-48\log(5/4)>
11-48\left(\frac{43}{192}\right)=\frac14>0.
\]
The derivative is continuous on a sufficiently short interval immediately to the left of \(1\), and has a positive limit there. Thus \(\ell_Y\) increases on that interval, contradicting DGMRL. This proves the assertion. \(\square\)

## Verification
The accompanying dependency-free `verify.py` checks the exact rational Taylor bound using `fractions.Fraction`; it separately computes the cutoff, mean residual life, and one-sided derivatives with high-precision `decimal.Decimal`, and checks several nearby generalized mean residual life values. Running `python3 verify.py` prints the strict exact certificate \(11-48\log(5/4)>1/4\) and confirms the finite diagnostics. The global DGMRL assertion and the local failure are justified by the analytic identities above, not by finite sampling.

## Relationship to prior work
Leonardos and Melolidakis's arXiv preprint *A Class of Distributions for Linear Demand Markets* (arXiv:1805.06327, first submitted 15 May 2018; section 4.3 of the 2021 revision) explicitly leaves preservation of DGMRD/DGMRL under right truncation unresolved. Leonardos, Koki, and Melolidakis's later *A generalization of the increasing generalized failure rate unimodality condition* (published online 7 June 2023, DOI 10.1007/s10479-023-05425-z; section 4) repeats the open question. The present example gives a negative answer under the usual conditional-truncation convention.

Banciu and Mirchandani, *Technical Note—New Results Concerning Probability Distributions with Increasing Generalized Failure Rates* (Operations Research, 2013, DOI 10.1287/opre.2013.1198, Proposition 1), establish preservation under right truncation for the **smaller IGFR class**. This does not contradict the example: the generalized failure rate \(x h_X(x)\) jumps down from \(1\) to \(1/3\) at the switch, so the original law is not IGFR. Thus that existing preservation theorem cannot apply.

## Limitations
The result supplies an explicit counterexample to **closure**, not a characterization of which DGMRL laws or cutoff values retain the property. The original hazard is piecewise constant with a downward jump; smooth hazards, or right censoring rather than right truncation, are not addressed. The exact violation is local, at a specific positive threshold, and does not imply multiple fixed points or failure of every related pricing model. Independently establishing priority relative to all earlier literature remains outstanding.

## References
1. S. Leonardos and C. Melolidakis, *A Class of Distributions for Linear Demand Markets*, arXiv:1805.06327 (submitted 15 May 2018; revised 16 July 2021), https://arxiv.org/abs/1805.06327 .
2. S. Leonardos, C. Koki, and C. Melolidakis, *A generalization of the increasing generalized failure rate unimodality condition*, Annals of Operations Research (first online 7 June 2023), https://doi.org/10.1007/s10479-023-05425-z .
3. M. Banciu and P. Mirchandani, *Technical Note—New Results Concerning Probability Distributions with Increasing Generalized Failure Rates*, Operations Research 61 (2013), 925–931, https://doi.org/10.1287/opre.2013.1198 .
