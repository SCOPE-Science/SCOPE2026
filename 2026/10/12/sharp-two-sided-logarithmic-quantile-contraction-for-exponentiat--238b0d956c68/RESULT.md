# Sharp two-sided logarithmic quantile contraction for exponentiated-exponential lifetimes

## Finding

For every pair of real shape parameters \(0<r<s\), let \(X_a\) have the exponentiated-exponential distribution
\[
\Pr(X_a\le x)=(1-e^{-x})^a\qquad (x>0,\ a>0),
\]
let \(Z_a=\log X_a\), and write its quantile as
\[
Q_a(u)=\log\bigl[-\log(1-u^{1/a})\bigr],\qquad 0<u<1.
\]
Then for **every** \(0<u<v<1\), the following strict, simultaneous two-sided comparison holds:
\[
\boxed{\frac rs\,[Q_r(v)-Q_r(u)]<Q_s(v)-Q_s(u)<Q_r(v)-Q_r(u).}
\]
Both multipliers \(r/s\) and \(1\) are the **best possible uniform constants for each fixed pair** \(r<s\): the ratio of the quantile increments approaches \(r/s\) in arbitrarily short intervals near \(u=0\), and approaches \(1\) in arbitrarily short intervals near \(u=1\).

Thus the increasing quantile transport \(Q_s\circ Q_r^{-1}\) is globally Lipschitz with optimal Lipschitz constant \(1\), and its inverse has optimal Lipschitz constant \(s/r\). In the usual stochastic-order notation,
\[
\frac rs Z_r\ \le_{\mathrm{disp}}\ Z_s\ \le_{\mathrm{disp}}\ Z_r,
\]
where the dispersive order compares *quantile increments* and is invariant under location shifts. A further consequence is the centered convex-order sandwich
\[
\frac rs\,(Z_r-\mathbb E Z_r)\ \le_{\mathrm{cx}}\ Z_s-\mathbb E Z_s
\ \le_{\mathrm{cx}}\ Z_r-\mathbb E Z_r.
\]
For integer \(a\), \(X_a\) is precisely the maximum of \(a\) independent unit exponential lifetimes. The real-shape formulation also covers the full proportional-reversed-hazards family with this exponential baseline.

## Assumptions and scope

The parameters \(r,s\) are *arbitrary real numbers* with \(0<r<s<\infty\). The probabilities \(u,v\) satisfy \(0<u<v<1\). The baseline is the unit exponential law; a common positive exponential rate only adds the same constant to every \(Z_a\) and leaves all increments unchanged. There is no restriction to integer sample sizes in the parametric theorem. No independence across the two compared random variables is required, because the claim compares only their laws and is realized by their common-quantile coupling.

Each \(Z_a\) possesses finite absolute moments of every positive order. Indeed, its negative tail is exponential of rate \(a\), while its positive tail is super-exponential: these facts follow directly from \(\Pr(X_a\le x)\sim x^a\) as \(x\downarrow0\) and \(\Pr(X_a>x)\sim a e^{-x}\) as \(x\to\infty\). Therefore the centered convex-order statements are well-defined and imply moment inequalities, without any appeal to formal differences of divergent means.

## Proof

**Step 1: exact derivative ratio.** Put \(t=-\log u>0\) and define
\[
B(w)=(e^w-1)\,[-\log(1-e^{-w})],\qquad w>0.
\]
Differentiating the displayed quantile formula gives
\[
Q_a'(u)=\frac{1}{a u\,B(t/a)}>0.
\]
Consequently, for \(\rho=r/s\in(0,1)\) and \(w=t/r\),
\[
\frac{Q_s'(u)}{Q_r'(u)}=\rho\,\frac{B(w)}{B(\rho w)}.\tag{1}
\]

**Step 2: the structural lemma (including endpoints).** The function \(B\) is strictly increasing and strictly concave on \((0,\infty)\), with \(B(0+)=0\) and \(B(+\infty)=1\). To verify this directly, set \(L(w)=-\log(1-e^{-w})\). Then
\[
B'(w)=e^wL(w)-1>0,
\qquad B''(w)=e^w\left[L(w)-\frac{1}{e^w-1}\right]<0.
\]
Both strict signs follow on writing \(z=e^{-w}\in(0,1)\): the elementary inequalities \(z< -\log(1-z)<z/(1-z)\) give \(L(w)>e^{-w}\) and \(L(w)<1/(e^w-1)\). Moreover,
\[
B(w)\sim w\log(1/w)\quad(w\downarrow0),\qquad B(w)\to1\quad(w\to\infty).
\]
Since \(B(0+)=0\) and \(B\) is strictly concave and increasing, for every \(w>0\),
\[
\rho B(w)<B(\rho w)<B(w).\tag{2}
\]
Combining (1) and (2) proves
\[
\rho<Q_s'(u)/Q_r'(u)<1\qquad(0<u<1).\tag{3}
\]

**Step 3: all quantile increments and optimality.** Multiply (3) by \(Q_r'(u)>0\) and integrate from arbitrary \(u\) to \(v\); this gives both strict inequalities in the finding. As \(u\downarrow0\), we have \(w=(-\log u)/r\to\infty\), hence \(B(w)/B(\rho w)\to1\) and \(Q_s'(u)/Q_r'(u)\to\rho\). As \(u\uparrow1\), \(w\downarrow0\); the asymptotic \(B(w)\sim w\log(1/w)\) yields \(B(w)/B(\rho w)\to1/\rho\) and the derivative ratio tends \(1\). For fixed \(r,s\), a ratio of quantile increments over intervals of vanishing width tends the local derivative ratio, so these two endpoint limits prove the claimed *global sharpness* of the constants.

**Step 4: centered convex orders.** Inequality (3) says that both \(u\mapsto Q_s(u)-\rho Q_r(u)\) and \(u\mapsto Q_r(u)-Q_s(u)\) are strictly increasing. Subtract their respective expectations under a uniform \(U\) on \((0,1)\). Each centered increasing difference integrates to zero, so its integral over \((0,p)\) is nonpositive for every \(p\in(0,1)\). The integrated-quantile criterion for convex order therefore yields first \(\rho(Z_r-\mathbb E Z_r)\le_{\mathrm{cx}}Z_s-\mathbb E Z_s\) and then \(Z_s-\mathbb E Z_s\le_{\mathrm{cx}}Z_r-\mathbb E Z_r\). The same quantile inequalities directly give the two dispersive orders. Strict convex inequalities follow for nonaffine strictly convex functions with finite expectations, since neither pair differs by a constant in the increasing-quantile coupling.

## Verification

The standalone, dependency-free `verify.py` reproduces the quantiles and derivative ratios, checks the defining calculus identities by finite differences, tests the strict inequalities for deterministic pseudorandom real parameters and quantile intervals, checks the representative \((r,s,u,v)=(1,2,1/5,4/5)\), and numerically illustrates the limiting derivative ratios near the two endpoints. Its output does not certify infinitely many cases; all universal quantifiers are discharged by the analytic proof above. The checker uses numerically stable logarithms for small tail probabilities.

## Relationship to prior work

Datta and Gupta's preprint *Stochastic comparison study of the general family of PHR and PRHR distributions* (publicly submitted February 27, 2020, arXiv:2002.12436v1; published as a REVSTAT article in 2024) studies general PRHR system comparisons and has explicit primary classification 62N05. Its Theorem 4 treats reversed-hazard ordering of parallel lifetimes; its star-order results are in a different, PHR series model. Neither states a sharp two-sided logarithmic quantile-increment bound for the exponentiated-exponential family.

**Crucially, a qualitative part is already known:** Arab, Hadjikyriakou, Oliveira, and Santos, *Star-shaped order for distributions characterized by several parameters and some applications* (2021), Proposition 12 and Remark 14, give a general star-order criterion for PRHR distributions. Applied to the exponential baseline, with the appropriate order direction, that criterion already entails the **unscaled one-sided dispersive comparison** for logarithms. That qualitative assertion is *not claimed as new here*. The additional statement is the **uniform two-sided contraction, with the exact positive lower factor \(r/s\)** and proof of simultaneous optimality of both factors, plus the resulting quantitatively scaled convex-order lower sandwich. No passage from the qualitative star order alone supplies this lower bound: a dispersive comparison has no prescribed positive lower rate without further family-specific structure.

Doumas' logarithm-of-exponential-maximum representation in *An inequality involving alternating binomial sums* (Statistics & Probability Letters 235, 2026, DOI 10.1016/j.spl.2026.110735), and Giam's *Decreasing nature of a sequence related to the Coupon Collector's problem* (2026, DOI 10.1016/j.spl.2026.110790), concern the scalar variance and its monotonicity. They do not, in the material available and inspected, assert this global pair of sharp quantile-increment inequalities; an abstract for Giam, rather than the full paper, was available for this comparison. Earlier order-statistic reviews likewise discuss nonquantitative orders. Other terminology might conceal equivalent earlier coverage, as described below.

## Limitations

The result is specific to the exponentiated-*exponential* (equivalently, exponential-baseline PRHR) family and its logarithm. It does not assert an analogous universal \(r/s\) factor for all baseline laws, heterogeneous parallel systems, or dependent components. Quantile **increment** factors are sharp; this does *not* assert that the induced scalar variance factors are separately optimal. A known qualitative PRHR star-order theorem and a known later scalar variance theorem already cover two easier consequences; they are not independent new discoveries. The literature comparison cannot exclude an older equivalent bound under scaled dispersive, quantile-transport, or relative-aging terminology. 

## References

1. M. Datta and N. Gupta, *Stochastic comparison study of the general family of PHR and PRHR distributions*, arXiv:2002.12436v1, submitted 2020-02-27, https://arxiv.org/abs/2002.12436 (see first-page MSC 62N05, Section 3 Theorem 4, Section 4 Theorem 5). Later journal version: https://doi.org/10.57805/revstat.v22i3.528.
2. I. Arab, M. Hadjikyriakou, P. E. Oliveira, and B. Santos, *Star-shaped order for distributions characterized by several parameters and some applications*, 2021, https://doi.org/10.1017/S0269964821000449 (Proposition 12, Remark 14 and the later exponentiated-Weibull model).
3. A. V. Doumas, *An inequality involving alternating binomial sums*, Statistics & Probability Letters 235 (2026), 110735, https://doi.org/10.1016/j.spl.2026.110735.
4. K. K. Giam, *Decreasing nature of a sequence related to the Coupon Collector's problem*, Statistics & Probability Letters 236 (2026), 110790, https://doi.org/10.1016/j.spl.2026.110790; preprint abstract https://doi.org/10.2139/ssrn.6447308.
5. M. Shaked and J. G. Shanthikumar, *Stochastic Orders*, Springer, 2007, Section 3.A (definitions and integrated-quantile characterization of convex order).
