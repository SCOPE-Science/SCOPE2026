# Sharp age-shape phase boundaries for a two-frailty Gompertz cohort

## Finding
Consider a cohort made of two equally large subpopulations. Each has an exponentially increasing individual hazard, but after survivor selection the *aggregate* mortality hazard need not increase. The complete classification below gives sharp and explicit boundaries for this phenomenon.

**Theorem.** Let \(0<a<b\), \(c>0\) and \(t\ge0\). Suppose the two subcohorts have respective hazards \(h_1(t)=a e^{ct}\) and \(h_2(t)=b e^{ct}\), with initial weights \(1/2\) each. Define \(\Delta=b-a\), \(A=a/\Delta\), \(k=\Delta/c\), and
\[
 k_0=4A+2=\frac{2(a+b)}{b-a},\qquad
 k_c=k_0-\log(b/a).
\]
The aggregate mortality hazard exhibits these **and only these** shapes on positive ages:

1. If \(0<k<k_c\), it is strictly increasing, with no stationary point.
2. If \(k=k_c>0\), it is strictly increasing with one stationary inflection (no strict extremum).
3. If \(\max\{0,k_c\}<k<k_0\), it has exactly two strict positive-age extrema: first a local maximum, then a local minimum, with derivative signs \(+,-,+\).
4. If \(k\ge k_0\), it has exactly one strict positive-age local minimum and decreases before that minimum. At \(k=k_0\), the age-zero derivative vanishes as an endpoint phenomenon, not an additional positive-age extremum.

Equivalently, the two-extrema window is precisely
\[
 2(a+b)-(b-a)\log(b/a)<\frac{(b-a)^2}{c}<2(a+b).
\]
The lower bound may be negative and then imposes no further restriction. The window has exact width \(\log(b/a)\) in the dimensionless coordinate \(k\).

At a positive lower boundary \(k=k_c\), let \(\varepsilon=k-k_c\downarrow0\) while \(A\) is fixed, and set \(u=\frac{b-a}{c}(e^{ct}-1)\). The newly separated stationary coordinates satisfy
\[
 u_\pm=\log(b/a)\pm\sqrt{\frac{2\varepsilon}{2A+1}}+O(\varepsilon).
\]
Approaching the upper boundary from below, \(k=k_0-\varepsilon\), the first stationary coordinate is \(u_-=\varepsilon/2+O(\varepsilon^2)\).

## Assumptions and scope
The two subcohorts are fixed at birth, have exactly equal initial probabilities, and differ only in their positive Gompertz hazard multipliers; they share the same positive exponential aging slope. Survival is independent conditional on subcohort membership. The population hazard is the instantaneous rate of death conditional on still being alive, not the unconditional mean of individual hazards. The classification concerns \(t\ge0\) and counts only **strict interior** extrema. All logarithms are natural. No gamma or other continuous frailty assumption is used.

Their survivor functions and the aggregate survivor function are
\[
 S_i(t)=\exp\left[-\frac{a_i}{c}(e^{ct}-1)\right],\quad
 S(t)=\tfrac12(S_1(t)+S_2(t)),\quad H(t)=-\frac{S'(t)}{S(t)}.
\]

## Proof
Write \(\Delta=b-a\), \(u=k(e^{ct}-1)\), \(A=a/\Delta\), \(k=\Delta/c\). For each \(t\ge0\), the survivor weight of the high-frailty subcohort is
\[
 p(u)=\frac{S_2}{S_1+S_2}=\frac{1}{1+e^u},\qquad 0<p\le\tfrac12.
\]
Consequently,
\[
 H(t)=\Delta(1+u/k)(A+p(u)),\qquad
 \frac{du}{dt}=c(u+k)>0.
\]
Differentiation (with \(p'=-p(1-p)\)) gives the exact sign-reduction
\[
 H'(t)=c\Delta(1+u/k)g(u),\qquad
 g(u)=A+p(u)-(u+k)p(u)(1-p(u)).
\]
Every omitted factor is strictly positive for \(t\ge0\), so positive-age critical points are exactly positive zeros of \(g\).

Using \(1-2p(u)=\tanh(u/2)\), another differentiation gives
\[
 g'(u)=p(u)(1-p(u))\big[(u+k)\tanh(u/2)-2\big].
\]
For every \(k>0\), the bracket is strictly increasing from \(-2\) to infinity on \(u\ge0\). Hence \(g\) has exactly one strict minimum at the unique \(u_*(k)>0\) solving
\[
 (u_*+k)\tanh(u_*/2)=2.
\]
The endpoints satisfy
\[
 g(0)=A+\tfrac12-\tfrac{k}{4}=\frac{k_0-k}{4},\qquad
 \lim_{u\to\infty}g(u)=A>0.
\]
At its minimum, put \(r=p(u_*)\). The displayed stationary relation implies \((u_*+k)=2/(1-2r)\), whence
\[
 g(u_*)=A+r-\frac{2r(1-r)}{1-2r}
        =A-\frac{r}{1-2r}
        =A-\frac{1}{e^{u_*}-1}.
\]
This minimum vanishes exactly when \(u_*=\log(1+1/A)=\log(b/a)=:u_c\). At that point, the stationary relation yields
\[
 k=2\coth(u_c/2)-u_c=4A+2-u_c=k_c.
\]
As \(k\) increases, \(u_*(k)\) strictly decreases, so \(g(u_*)\) decreases strictly and changes sign exactly at \(k_c\) when the latter is positive; if \(k_c\le0\), its minimum is negative for every physical \(k>0\). Together with \(g(0)=(k_0-k)/4\) and the positive asymptotic endpoint, this gives the four exhaustive derivative-sign cases above. In particular, for \(k>k_c\) the strict minimum of \(g\) is negative; when \(k<k_0\) its positive value at zero forces *two* distinct positive roots, whereas for \(k\ge k_0\) its nonpositive initial value gives just *one* positive root.

At the fold \((u_c,k_c)\), \(g=g_u=0\), with
\[
 g_k=-p_c(1-p_c)<0,\qquad
 g_{uu}=p_c(1-p_c)(2A+1)>0.
\]
Taylor expansion therefore yields \(0=-p_c(1-p_c)\varepsilon+\tfrac12p_c(1-p_c)(2A+1)(u-u_c)^2+O(\varepsilon^{3/2})\), proving the square-root split. At the upper boundary, \(g(0,k_0-\varepsilon)=\varepsilon/4\) and \(g_u(0,k)=-1/2\), giving \(u_-=\varepsilon/2+O(\varepsilon^2)\). At \(k=k_c>0\), the isolated double zero of \(g\) has no sign change and is only a stationary inflection of \(H\); at \(k=k_0\), \(u=0\) is an endpoint root and is not counted as an interior extremum. This proves all assertions.

**Explicit witness.** For \(a=1/2\), \(b=5/2\), \(c=1\), one has \(A=1/4\), \(k=2\), \(k_c=3-\log 5\) and \(k_0=3\). The two strictly positive zeros of \(g\) occur at \(u\approx0.634307250238139\) and \(u\approx2.418458919210159\). They correspond respectively to ages \(t\approx0.275473063732862\) and \(t\approx0.792643793921167\), with aggregate hazards approximately \(1.571455222795638\) and \(1.465938177929322\). In contrast, \(H(0)=1.5\). Each individual hazard is strictly increasing throughout.

## Verification
Run the accompanying standard-library Python file `verify.py` using Python 3.10 or later. The code reconstructs the survivor-based hazard independently of the derivative reduction and compares finite-difference derivatives with the derived formula in 3,000 reproducible samples. It also checks root signs, exact phase-boundary identities, the witness roots, the fold square-root scaling, and the age-zero endpoint scaling. All checks passed. These computations **do not** establish the infinite-domain classification: its proof rests on the unique-minimum argument and exact endpoint signs above.

## Relationship to prior work
Frailty heterogeneity in cohort mortality was developed by Vaupel, Manton, and Stallard (1979). More general mathematical identities express the cohort hazard as a survivor-weighted mean and its derivative as individual hazard increase minus survivor-weighted hazard variance; those identities are prior knowledge, including Finkelstein (2009, Sections 2–4) and Vaupel and Missov (2014, Section 4). The gamma-Gompertz examples in these works have continuously distributed frailty and yield a monotone or plateauing aggregate hazard in their stated parameter cases. Finkelstein also surveys two-component *other-family* hazards with modified bathtub shapes. The result proved here is instead the **complete, explicit, necessary-and-sufficient two-atom equal-weight Gompertz phase diagram**, including exact boundaries and fold law. The general formulas can be specialized to the present problem but do not, by themselves, supply its root-count theorem without the new analysis.

The earlier foundational Vaupel–Yashin report on heterogeneous mortality is closely related; only its bibliographic summary was accessible during this comparison because the online report PDF returned access denial. The 1997 Gompertz-mixture estimation study was accessible at title/abstract level but not conclusively in full text. Therefore, historical priority for the specialized inequalities remains a residual risk rather than a proven uniqueness claim.

## Limitations
This is an exact ideal-model result, **not** an empirical fit, estimation algorithm, demographic prediction, or a statement about unequal initial mixing proportions, unequal Gompertz slopes, Makeham background hazards, or continuous frailty distributions. Strict monotonicity is meant in the order sense even at isolated stationary inflections. Finite numerical checks cannot replace the universal calculus proof. Published-priority assessment is bounded by accessible literature, and independently conducted validation has not occurred.

## References
1. Vaupel, J. W., Manton, K. G., and Stallard, E. (1979). *The Impact of Heterogeneity in Individual Frailty on the Dynamics of Mortality*. Demography 16, 439–454. DOI: 10.2307/2061224; public date 1979-08-01.
2. Vaupel, J. W. and Yashin, A. I. (1983). *The Deviant Dynamics of Death in Heterogeneous Populations*. IIASA Research Report RR-83-001. https://pure.iiasa.ac.at/id/eprint/2159/
3. Finkelstein, M. (2009). *Understanding the Shape of the Mixture Failure Rate (with Engineering and Demographic Applications)*. MPIDR Working Paper WP-2009-031. https://www.demogr.mpg.de/papers/working/wp-2009-031.pdf
4. Vaupel, J. W. and Missov, T. (2014). *Unobserved population heterogeneity: A review of formal relationships*. Demographic Research 31, 659–686. DOI: 10.4054/DemRes.2014.31.22.
5. McLachlan, G. J., et al. (1997). *An Algorithm for Fitting Mixtures of Gompertz Distributions to Censored Survival Data*. Journal of Statistical Software. DOI: 10.18637/jss.v002.i07.
