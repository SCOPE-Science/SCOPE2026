# A sharp doubling threshold for increasing hazard in three exponential lifetimes

## Finding
Let \(X_1,X_2,X_3\) be independent, with \(X_1,X_2\sim\operatorname{Exp}(a)\), \(X_3\sim\operatorname{Exp}(b)\), and \(a,b>0\). Write \(T=\max\{X_1,X_2,X_3\}\), and let \(h_T(t)\) be its hazard rate at \(t>0\).

**Theorem.** The hazard rate is nondecreasing on all of \((0,\infty)\) **if and only if**
\[
 b=a\quad\text{or}\quad b\ge 2a.
\]
In these cases it is in fact **strictly increasing** at every positive time. If \(0<b<2a\) and \(b\ne a\), its derivative is strictly negative for all sufficiently large times, so the distribution is not IFR (increasing failure rate).

This exhibits a sharp, nonmonotone dependence on the third component's exponential rate: modest heterogeneity destroys increasing system hazard, but heterogeneity beyond the factor-of-two threshold restores it. The result is a complete classification for the natural three-component family with two equal component rates, not a classification for arbitrary three distinct rates.

## Assumptions and scope
The \(\operatorname{Exp}(\lambda)\) law has survival function \(\Pr(X>t)=e^{-\lambda t}\) for \(t\ge0\); all three component lifetimes are independent and their rates are strictly positive. The parallel system operates while any component operates, so its lifetime is their maximum. The hazard of a positive-survival, absolutely continuous variable is \(h(t)=-\frac{d}{dt}\log\Pr(T>t)\). Here *IFR* means that this hazard is nondecreasing throughout \((0,\infty)\); no weaker average-aging order is intended.

Write \(r=b/a>0\), \(s=at\), \(x=e^{-s}\in(0,1)\), and let a prime denote differentiation with respect to \(s\). Direct multiplication of the three component distribution functions gives the dimensionless survival function
\[
 S_r(s)=\Pr(T>s/a)=2x-x^2+x^r(1-x)^2.
\]
The physical hazard is \(h_T(t)=-aS'_r(s)/S_r(s)\).

## Proof
The hazard derivative has sign equal to
\[
 D_r(s)=(S'_r(s))^2-S_r(s)S''_r(s),\qquad
 h'_T(t)=a^2D_r(s)/S_r(s)^2.
\]
For \(0<x<1\) define
\[
 B_r(x)=-r^2(2-x)(1-x)^2+4r(1-x)-2(2x^2-2x+1).
\]
Expanding \(S_r=2x-x^2+x^r-2x^{r+1}+x^{r+2}\), and differentiating \(e^{-cs}\) as \(-c e^{-cs}\), gives the exact identity
\[
 D_r(s)=x\{2x^2+x^rB_r(x)+2x^{2r}(1-x)^2\}.\tag{1}
\]
The identity holds for every real \(r>0\), without an integer-rate restriction.

**Necessity outside the asserted set.** If \(0<r<2\) and \(r\ne1\), then \(B_r(x)\to-2(r-1)^2\) as \(x\downarrow0\). Dividing (1) by \(x^{r+1}\), and using \(x^{2-r}\to0\) and \(x^r\to0\), proves
\[
 \lim_{s\to\infty}\frac{D_r(s)}{e^{-(r+1)s}}
 =-2(r-1)^2<0.
\]
Consequently \(h'_T(t)<0\) for every sufficiently large \(t\). This covers both a third component slower than the repeated rate (\(r<1\)) and moderately faster than it (\(1<r<2\)).

**The equal-rate case.** If \(r=1\), the same identity factors as
\[
 D_1(s)=3x^3(3-x)(1-x)>0\qquad(0<x<1).
\]

**Sufficiency at and above the sharp threshold.** Suppose \(r=2+u\), \(u\ge0\), and set \(v=-\log x=s>0\). Factor (1) as
\[
 D_r(s)=x^{r+1}\{2e^{uv}+B_r(x)+2x^r(1-x)^2\}.
\]
It suffices to prove \(2e^{uv}+B_r(x)>0\). A quadratic expansion in \(u\) yields
\[
\begin{aligned}
 B_{2+u}(x)={}&B_2(x)-4u(1-x)(x^2-3x+1)\\
 &-u^2(2-x)(1-x)^2,\\
 2+B_2(x)={}&4x(4-x)(1-x)>0.
\end{aligned}
\]
Using \(e^{uv}\ge1+uv+(uv)^2/2\), obtain
\[
\begin{aligned}
 2e^{uv}+B_{2+u}(x)\ \ge{}&4x(4-x)(1-x)\\
 &+u\{2v-4(1-x)(x^2-3x+1)\}\\
 &+u^2\{v^2-(2-x)(1-x)^2\}.\tag{2}
\end{aligned}
\]
Both coefficients involving \(u\) are nonnegative. Indeed,
\[
 v=-\log x\ge\frac{2(1-x)}{1+x}
\]
(following, for example, by differentiating both sides), so
\[
 2v-4(1-x)(x^2-3x+1)
 \ge\frac{4x(1-x)(2+2x-x^2)}{1+x}>0.
\]
Also, on setting \(z=1-x\in(0,1)\), the elementary logarithm inequality \(-\log(1-z)\ge z+z^2/2\) gives
\[
 v^2\ge z^2(1+z+z^2/4)\ge z^2(1+z)=(2-x)(1-x)^2.
\]
Thus the right-hand side of (2) is strictly positive, proving \(D_r(s)>0\) for every \(s>0\) when \(r\ge2\). Together with the other cases, this proves the theorem. \(\square\)

For perspective, (1) also gives exact leading long-time derivatives: if \(0<b<a\), then \(h'_T(t)\sim-2(a-b)^2e^{-(a-b)t}\); if \(a<b<2a\), then \(h'_T(t)\sim-\tfrac12(b-a)^2e^{-(b-a)t}\); at \(b=2a\), \(h'_T(t)\sim4a^2e^{-2at}\); and for \(b>2a\), \(h'_T(t)\sim\tfrac12a^2e^{-at}\). At \(b=a\), the derivative instead behaves as \(a^2e^{-at}\). All asymptotics concern fixed positive rates and \(t\to\infty\).

## Verification
Run `python3 verify.py` using Python 3's standard library. It checks identity (1) against independently differentiated exponential sums using 3,344 exact rational triples in which the power term is treated independently, verifies 2,190 exact integer-rate positivity cases, checks rational counterexamples on both sides of the repeated rate, and checks the coefficient identities in (2). It additionally reports numerical diagnostics for noninteger ratios. These checks exercise the algebra; the proof of positivity for **all** positive times and real rates, and the negative-tail limits, are the analytic arguments above. No finite grid is treated as an exhaustive verification of a continuum.

## Relationship to prior work
The 2021 study by Balakrishnan, Barmalzan and Kosari concerns hazard-rate **ordering between different parallel systems** with proportional reversed-hazard component models and optional starting devices; its two-component comparisons do not state the three-exponential **single-system IFR classification** above. Yaming Yu's 2016 theorem establishes hazard-rate and star ordering between heterogeneous and homogeneous exponential order statistics, but an ordering of two hazards does not imply that each hazard is itself increasing. Kochar and Xu's convex-transform results similarly compare heterogeneous and homogeneous maxima, rather than classify the internal monotonicity of the heterogeneous maximum's hazard. Joo and Mi's two-component exponential comparisons are adjacent background, not a demonstrated three-component doubling criterion. These distinctions concern theorem implications, not only terminology.

## Limitations
The result is restricted to exactly three independent exponential lifetimes with two equal rates. It does not assert IFR for arbitrary heterogeneous three-component systems, nor any failure-rate ordering *between* different systems. The sharp factor-two boundary is a property of this specified parametric family. Related early reliability papers, especially work on two-component hazard functions, may contain alternative arguments or implications not identified in the accessible material; the originality comparison is not an independent literature certification.

## References
1. N. Balakrishnan, G. Barmalzan and S. Kosari, *Comparisons of Parallel Systems with Components Having Proportional Reversed Hazard Rates and Starting Devices*, Mathematics 9 (2021), 856, https://doi.org/10.3390/math9080856 (first publicly dated 2021-04-14).
2. Y. Yu, *On Stochastic Comparisons of Order Statistics from Heterogeneous Exponential Samples*, arXiv:1607.06564v1 (2016), https://arxiv.org/html/1607.06564v1.
3. S. Kochar and M. Xu, *Comparisons of Parallel Systems According to the Convex Transform Order*, Journal of Applied Probability 46 (2009), 342–352, https://doi.org/10.1239/jap/1245676091.
4. S. F. Joo and J. Mi, *Some properties of hazard rate functions of systems with two components*, Journal of Statistical Planning and Inference 140 (2010), 444–453, https://doi.org/10.1016/j.jspi.2009.07.023.
