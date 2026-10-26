# Strict birthday–coverage anticorrelation in uniform coupon sampling

## Finding

Fix an integer \(m\ge 2\). Draw independent labels uniformly from \(\{1,\ldots,m\}\). Let \(B_m\) be the time index of the **first repeated label** and \(C_m\) the first index by which **all** labels have been observed. Thus \(B_m\in\{2,\ldots,m+1\}\), whereas \(C_m\ge m\); in particular \(B_m>C_m\) is possible when the first \(m\) draws are distinct.

Write \(s_{m,b}=(m)_{\underline b}/m^b\) for \(0\le b\le m\), where \((m)_{\underline b}=m!/(m-b)!\), and \(H_m=\sum_{j=1}^m 1/j\), with \(H_0=0\). The **joint dependence theorem** is
\[
\operatorname{Cov}(B_m,C_m)
=-\sum_{b=2}^{m}s_{m,b}\sum_{r=1}^{b-1}\frac{r}{m-r}<0,
\qquad m\ge2.
\]
The conditional laws \(C_m\mid(B_m=b)\) are strictly decreasing in first-order stochastic order as \(b\) increases from \(2\) to \(m+1\). Quantitatively,
\[
\frac{\operatorname{Cov}(B_m,C_m)}{\sqrt m}
\longrightarrow-\sqrt{\frac{\pi}{8}},
\qquad
m\operatorname{Corr}(B_m,C_m)
\longrightarrow-\sqrt{\frac{3}{2\pi(4-\pi)}}.
\]
There is also a conditional-mean profile: for fixed \(x>0\) and integers \(b_m\in\{2,\ldots,m\}\) with \(b_m/\sqrt m\to x\),
\[
\mathbb E[C_m\mid B_m=b_m]-mH_m\longrightarrow1-\frac{x^2}{2}.
\]
All conclusions concern the classical uniform independent-label model, rather than heterogeneous coupon probabilities or dependent sampling.

## Assumptions and scope

Times count draws starting from one, inclusive of the first repeated draw and final new-label draw respectively. A geometric random variable \(G(p)\) takes values \(1,2,\ldots\), with \(\Pr(G(p)=k)=(1-p)^{k-1}p\). Every random time in the theorem is almost surely finite, and has finite moments for fixed \(m\). The exact identity includes \(m=2\); no unproven uniform extension to unequal label probabilities is asserted.

## Proof

**1. Conditional completion times.** On \(\{B_m=b\}\), for \(2\le b\le m\), the initial \(b-1\) draws are distinct and draw \(b\) repeats one of them. Exactly \(b-1\) labels are present at time \(b\). After that, the waiting times for successive previously unseen labels are independent geometrics with success parameters \((m-b+1)/m,(m-b)/m,\ldots,1/m\). Hence
\[
C_m\mid(B_m=b)\ \stackrel{d}{=}\ b+\sum_{j=1}^{m-b+1}G(j/m),
\qquad 2\le b\le m.
\]
When \(B_m=m+1\), all \(m\) labels appeared by time \(m\), and \(C_m=m\) deterministically. Couple the displays for adjacent \(b,b+1\) using their common geometric summands. For \(2\le b<m\) the difference is \(G((m-b+1)/m)-1\), nonnegative and strictly positive with nonzero probability. For the final pair \(b=m,m+1\), the difference is \(G(1/m)\), strictly positive. Thus the conditional completion-time laws strictly decrease in stochastic order. Taking expectations also gives
\[
\mathbb E[C_m\mid B_m=b]
=b+mH_{m-b+1}
=mH_m+1-\sum_{r=1}^{b-2}\frac{r}{m-r}
\]
for \(2\le b\le m\). A direct expansion of the latter sum when \(b_m/\sqrt m\to x\) yields \(\sum_{r=1}^{b_m-2}r/(m-r)\to x^2/2\), establishing the conditional-mean profile.

**2. Exact covariance.** Let \(s_{m,b}=\Pr(B_m>b)\): all first \(b\) draws must be distinct, so \(s_{m,b}=(m)_{\underline b}/m^b\) for \(0\le b\le m\). Conditional on \(B_m>b\), exactly \(b\) distinct labels have been observed at time \(b\). Hence, by the independent geometric-stage decomposition,
\[
\mathbb E[C_m\mid B_m>b]=b+mH_{m-b},
\qquad 0\le b\le m.
\]
The standard expectation is \(\mathbb E[C_m]=mH_m\). The pathwise tail identity \(B_m=\sum_{b=0}^{m}\mathbf1\{B_m>b\}\), valid even when \(B_m=m+1\), yields
\[
\begin{aligned}
\operatorname{Cov}(B_m,C_m)
&=\sum_{b=0}^{m}s_{m,b}\bigl(b+mH_{m-b}-mH_m\bigr)\\
&=-\sum_{b=2}^{m}s_{m,b}\sum_{r=1}^{b-1}\frac{r}{m-r}.
\end{aligned}
\]
Every summand on the last line is positive for \(b\ge2\). Since \(s_{m,2}>0\) for \(m\ge2\), strict negativity follows for all sizes, without recourse to the stochastic-order step.

**3. Sharp covariance asymptotic.** For each fixed \(x\ge0\),
\[
s_{m,\lfloor x\sqrt m\rfloor}\to e^{-x^2/2},
\qquad
\sum_{r=1}^{\lfloor x\sqrt m\rfloor-1}\frac{r}{m-r}\to\frac{x^2}{2}.
\]
To justify passage through the whole sum, for \(b\le m/2\) use the uniform bounds
\[
s_{m,b}\le\exp\bigl(-b(b-1)/(2m)\bigr),
\qquad
\sum_{r=1}^{b-1}\frac r{m-r}\le\frac{b(b-1)}m.
\]
These imply an integrable Gaussian-times-quadratic envelope after scaling \(b=x\sqrt m\). For \(b>m/2\), monotonicity of \(s_{m,b}\) gives \(s_{m,b}\le\exp(-(m-2)/8)\), while the inner sum is at most \(mH_{m-1}\). Thus this portion contributes \(o(\sqrt m)\). The Riemann sum therefore satisfies
\[
-\frac{\operatorname{Cov}(B_m,C_m)}{\sqrt m}
\longrightarrow\int_0^\infty\frac{x^2}{2}e^{-x^2/2}\,dx
=\sqrt{\frac\pi8}.
\]

**4. Correlation normalization.** The same Gaussian tail estimates and tail-sum moment formulas yield the Rayleigh moment limits
\[
\frac{\mathbb E[B_m]}{\sqrt m}\to\sqrt{\frac\pi2},
\quad \frac{\mathbb E[B_m^2]}m\to2,
\quad\frac{\operatorname{Var}(B_m)}m\to\frac{4-\pi}{2}.
\]
Since the coupon-collection stages are independent geometrics with parameters \(j/m\), their variance sum gives exactly
\[
\operatorname{Var}(C_m)
=m^2\sum_{j=1}^{m}\frac1{j^2}-mH_m,
\qquad
\frac{\operatorname{Var}(C_m)}{m^2}\to\frac{\pi^2}{6}.
\]
Combining the variance limits with step 3 yields the asserted correlation constant. This argument establishes a sharp decay rate and does not claim that the two stopping times are independent for finite \(m\).

## Verification

A standalone pure-Python program `verify_coupon_cov.py` computes the displayed covariance with exact rational arithmetic and, **independently**, computes the mixed moment from a Markov recursion tracking the count of distinct observed labels until the first collision. Equality is checked for every integer \(2\le m\le60\). The same script tests the conditional-mean expression against its geometric-stage formula and displays numerical convergence of the normalized covariance for selected larger sizes. Its finite calculations are corroboration; the proof above covers every \(m\ge2\).

## Relationship to prior work

The classic birthday problem determines the first-collision marginal, and the classical coupon collector decomposes completion time into independent geometric stages. The 1987 INRIA report of Flajolet, Gardy and Thimonier treats the birthday and coupon questions separately in its corresponding sections. Pósfai's 2010 treatment details the coupon-collector waiting-time decomposition and marginal approximations. O'Neill (2022) gives a broader framework for occupancy-threshold waiting times. Holst (1986) develops a unified Poisson-embedding treatment of birthday, collector and other urn stopping problems; its accessible abstract addresses exact and asymptotic **single-threshold** waiting times, but full text was inaccessible for comparison with the present mixed-stopping-time statistic. These established facts provide the building blocks here but do not, in the **material inspected**, state the strict joint covariance identity, the first-collision-conditioned stochastic order, or the sharp \(m^{-1}\) correlation scale. Neither distinct titles nor unsuccessful searches establish historical uniqueness; an equivalent formulation in uninspected sections or earlier occupancy literature remains possible.

## Limitations

The theorem applies only to independent **uniform** coupon labels, with the precise time-index convention specified above. No statement is made about arbitrary categorical probabilities, higher mixed moments, or a full bivariate limit theorem. The novelty comparison is constrained by accessible historical material and is subject to independent expert priority checking. Verification by finite computation does not replace the analytic proof.

## References

1. Philippe Flajolet, Danièle Gardy, Loÿs Thimonier, *Birthday paradox, coupon collectors, caching algorithms and self-organizing search*, INRIA research report RR-0720 (1987); later *Discrete Applied Mathematics* 39 (1992). HAL identifier `inria-00075832` (digital submission dated 2006-05-24); open scan: https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/PDF/pdf/RR-0720-ocr.pdf .
2. Anna Pósfai, *Approximation Theorems Related to the Coupon Collector's Problem*, arXiv:1006.3531v1 (2010-06-17), https://arxiv.org/pdf/1006.3531 .
3. Danièle Gardy, *Occupancy urn models in analysis of algorithms*, survey, https://danielegardy.github.io/SourcesPubli/survey_alloc_aleatoires.pdf .
4. Ben O'Neill, *An Examination of the Negative Occupancy Distribution and the Coupon-Collector Distribution*, *Methodology and Computing in Applied Probability* (2022), https://doi.org/10.1007/s11009-022-09966-x .
5. Lars Holst, *On Birthday, Collectors', Occupancy and Other Classical Urn Problems*, *International Statistical Review* 54(1), 15–27 (1986), https://doi.org/10.2307/1403255 (publisher abstract accessible; original full text not inspected).
