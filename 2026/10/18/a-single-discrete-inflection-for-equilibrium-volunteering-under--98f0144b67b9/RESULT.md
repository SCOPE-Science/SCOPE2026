# A single discrete inflection for equilibrium volunteering under group-size variation

## Finding
In a symmetric one-volunteer public-good game, let the group size be any integer \(n\ge 2\), the common public benefit be \(b>c>0\), and the individual cost of volunteering be \(c\). Conditional on the realized group size, every participant plays the symmetric, interior mixed Nash equilibrium independently. Put \(\lambda=\log(b/c)>0\), and write \(V_n\) for the expected number of volunteers. Then
\[
 V_n=n\left(1-e^{-\lambda/(n-1)}\right).
\]
For every integer \(n\ge3\), the discrete curvature
\[
 D_n(\lambda)=V_{n+1}-2V_n+V_{n-1}
\]
has a **unique positive crossover** \(\theta_n\): it is positive for \(0<\lambda<\theta_n\), zero at \(\lambda=\theta_n\), and negative for \(\lambda>\theta_n\). The thresholds form a strictly increasing ladder
\[
 0<\theta_3<\theta_4<\cdots<2,\qquad \lim_{n\to\infty}\theta_n=2,
\]
and satisfy the sharp expansion
\[
 \theta_n=2-\frac2n-\frac{4}{3n^3}+O(n^{-4}).
\]
Equivalently, at every fixed benefit-to-cost ratio, the expected-volunteer sequence has **at most one discrete inflection**, with negative curvature at smaller group sizes and positive curvature at larger sizes whenever both regimes occur.

The exact defining equation is the unique root \(z_n\in(0,1)\), other than the boundary root \(1\), of
\[
 -(n+1)+2nz_n^{n-2}-(n-1)z_n^{2n-2}=0,
 \qquad \theta_n=-n(n-1)(n-2)\log z_n.
\]
The crossover obeys the explicit brackets
\[
 \frac{2(n-2)}{n-1}<\theta_n<\frac{2n}{n+1}.
\]

**Group-size diversification.** Suppose separate groups independently draw their sizes from a distribution supported on integers at least two; each group learns its size and independently uses that size's symmetric mixed equilibrium. The expectation of volunteers *per group* equals \(\mathbb E[V_N]\). When \(0<\lambda\le\theta_3\), all discrete curvatures are nonnegative, so a mean-preserving spread of group sizes cannot decrease this expectation. When \(\lambda\ge2\), all curvatures are strictly negative, so such a spread cannot increase it. For \(\theta_3<\lambda<2\), there is one change from negative to positive curvature as \(n\) grows; the effect of local size diversification depends on the sizes involved.

For example, replace a deterministic three-person group by an equal-probability choice of two- and four-person groups (the same mean size). With \(b/c=(6/5)^6\), the resulting change in expected volunteers per group is exactly \(575/46656>0\). With \(b/c=(5/4)^6\), the change is exactly \(-96/15625<0\). These are exact rational comparisons, not decimal estimates.

## Assumptions and scope
There is one simultaneous, one-shot public good available to every member if at least one volunteers. Volunteering always incurs cost \(c\), whether or not others volunteer; successful provision yields benefit \(b\) to every member. Failure yields zero before any personal cost. Every player has identical payoffs and independently follows the interior symmetric mixed Nash equilibrium *after learning the realized group size*. The assertion is not about asymmetric pure Nash equilibria, a common ex-ante strategy used across multiple sizes, evolutionary equilibrium in an infinite population, or optimal provision probability. The group-size spread comparison concerns expected volunteers per independent group encounter, not volunteer counts under a fixed number of total participants divided into an endogenous number of groups.

## Proof
**1. Equilibrium and curvature identity.** If each of the other \(n-1\) participants volunteers with probability \(p\), the payoff from volunteering is \(b-c\), while abstaining yields \(b[1-(1-p)^{n-1}]\). Indifference therefore requires \((1-p)^{n-1}=c/b=e^{-\lambda}\). This has the unique interior symmetric solution \(p=1-e^{-\lambda/(n-1)}\), giving the formula for \(V_n\). Cancelling linear terms yields
\[
 D_n=-(n+1)e^{-\lambda/n}+2ne^{-\lambda/(n-1)}-(n-1)e^{-\lambda/(n-2)}.
\]
Set \(z=e^{-\lambda/[n(n-1)(n-2)]}\in(0,1)\). Factoring the strictly positive term \(z^{(n-1)(n-2)}\) gives
\[
 D_n=z^{(n-1)(n-2)}R_n(z),\qquad
 R_n(z)=-(n+1)+2nz^{n-2}-(n-1)z^{2n-2}.
\]

**2. One positive crossover.** We have \(R_n(0)=-(n+1)<0\), \(R_n(1)=0\), and
\[
 R_n'(z)=2z^{n-3}\bigl[n(n-2)-(n-1)^2z^n\bigr].
\]
The derivative changes sign exactly once within \((0,1)\), because \(n(n-2)=(n-1)^2-1\). Thus \(R_n\) increases to one strict maximum and then decreases to zero at \(z=1\). As \(R_n'(1)=-2\), that maximum is positive. Consequently exactly one further zero \(z_n\) lies in \((0,1)\). Since \(z\) decreases as \(\lambda\) increases, \(D_n\) has the stated sign orientation and unique positive crossover.

**3. Monotone threshold ladder.** Extend the formula to \(f_\lambda(x)=(x+1)(1-e^{-\lambda/x})\) for every real \(x>0\). Direct differentiation gives
\[
 f_\lambda''(x)=\frac{\lambda e^{-\lambda/x}}{x^4}\left[2x-\lambda(x+1)\right].
\]
Its sign is positive when \(\lambda<2x/(x+1)\), and negative when the inequality reverses. The second difference is the exact weighted integral
\[
 D_n=\int_{n-2}^{n}(1-|x-(n-1)|)f_\lambda''(x)\,dx.
\]
At a zero \(\lambda=\theta_n\), the factor \(f_\lambda''\) must change sign inside this interval; the unique change is from negative to positive, at \(x_*=\lambda/(2-\lambda)\). In particular \(\theta_n<2\).

To compare adjacent second differences, write \(w_n(x)=(1-|x-(n-1)|)_+\) and \(w_{n+1}(x)=(1-|x-n|)_+\). Where \(w_n>0\), the ratio \(w_{n+1}/w_n\) increases from zero on the left to infinity on the right; explicitly on their common support \((n-1,n)\), it is \((x-n+1)/(n-x)\). If \(x_*\le n-1\), then the entire support of \(w_{n+1}\) lies weakly to the right of the sign change, and \(D_{n+1}(\theta_n)>0\). Otherwise \(n-1<x_*<n\); take \(k=w_{n+1}(x_*)/w_n(x_*)\). The function \(w_{n+1}-kw_n\) is negative left of \(x_*\) and positive right of \(x_*\), in the union of their supports. The same is true of \(f_{\theta_n}''\). Therefore
\[
 D_{n+1}(\theta_n)-kD_n(\theta_n)
 =\int (w_{n+1}-kw_n)f_{\theta_n}''\,dx>0.
\]
Since \(D_n(\theta_n)=0\), this proves \(D_{n+1}(\theta_n)>0\). By the unique-crossover property, \(\theta_{n+1}>\theta_n\). Since \(2x/(x+1)\) increases strictly with \(x\), the integral also establishes the displayed brackets. These brackets give \(\theta_n\to2\).

**4. Sharp asymptotics.** Put \(h=1/n\), \(\lambda=2-2h+uh^3\), with \(u\) in a fixed compact interval. Expanding the three exponential terms in the exact formula for \(D_n\) yields, uniformly for bounded \(u\),
\[
 D_n(2-2h+uh^3)=h^6\left(-2u-\frac83\right)+O(h^7).
\]
At \(u=-2\) the leading sign is positive and at \(u=0\) negative. Consequently the unique \(\theta_n\) lies between \(2-2/n-2/n^3\) and \(2-2/n\) for all sufficiently large \(n\). Write \(u_n=n^3(\theta_n-2+2/n)\), which is bounded. Substituting \(u_n\) in the uniform expansion and using \(D_n(\theta_n)=0\) gives \(u_n=-4/3+O(n^{-1})\), proving the announced expansion.

**5. Diversification consequences.** For \(\lambda\le\theta_3\), monotonicity of \(\theta_n\) makes all \(D_n\ge0\), and for \(\lambda\ge2\) all are negative. Piecewise-linear interpolation of \(V_n\) on integer sizes is therefore convex in the first range and concave in the second. The defining inequality for convex order proves the mean-preserving-spread comparisons. In the intermediate regime \(\theta_3<\lambda<2\), strictly increasing thresholds imply that \(D_n\) switches from negative to positive at most once as \(n\) increases. Finally, direct substitution for \(n=2,3,4\) with \(e^{\lambda/6}=6/5\) and \(5/4\), respectively, gives the exact two rational examples.

## Verification
The accompanying executable `verify.py` independently checks 352 equilibrium indifference comparisons at high precision, 158 successive positive curvature thresholds and their analytic bounds, 948 signed exponential-polynomial identities, two rational group-size-spread certificates, and the symbolic order-six asymptotic expansion. It successfully reports `PASS`. These numerical tests are corroboration, not substitutes for the unrestricted derivative, integral, root-count, and convex-order proofs. The symbolic expansion is independently recomputed from the explicit formula in the package.

## Relationship to prior work
Archetti's 2009 volunteer-dilemma models establish the conditional symmetric equilibrium and analyze group-size effects on the probability that a public good is provided. Peña's 2011/2012 analysis studies Jensen effects of group-size diversity on **evolutionary selection gradients**, with a common evolving strategy across groups. Hillenbrand and Winter (2017/2018) establish a complementary mean-preserving-spread effect on individual volunteering probabilities when participants **do not observe realized group size before choosing** and play a common ex-ante symmetric strategy. Their Proposition 1 therefore does not control expected aggregate volunteering after each realized group re-equilibrates. The present object is different: it is the expected *number of volunteers* in independent groups whose participants condition and re-equilibrate on the realized size. The contribution claimed here is the exact one-inflection classification of that sequence, the strictly ordered discrete-curvature thresholds, and their sharp asymptotic. The classical equilibrium formula is background rather than claimed new. A prior result on the first differences of this same equilibrium sequence establishes where expected counts peak; it does not provide the second-difference sign classification or the Jensen-type effect under mean-preserving spreads.

## Limitations
The conclusions apply only to homogeneous one-shot, one-volunteer, interior symmetric Nash play and ex-post knowledge of group size. They do not cover correlated mixed actions, heterogeneous costs, multi-volunteer thresholds, evolutionary dynamics, experimental behavior, or fixed-population regrouping costs. Literature searches and accessible primary full-text comparisons did not identify a covering theorem, but an equivalent characterization elsewhere remains possible. The full text of one relevant 2009 group-size paper could not be inspected through available authorized routes; that is an outstanding bibliographic uncertainty.

## References
1. M. Archetti, “The volunteer's dilemma and the optimal size of a social group,” *Journal of Theoretical Biology* 261 (2009), 475–480. DOI: 10.1016/j.jtbi.2009.08.018. First public online: 2009-08-22 (PubMed publication record).
2. M. Archetti, “Cooperation as a volunteer's dilemma and the strategy of conflict in public goods games,” *Journal of Evolutionary Biology* 22 (2009), 2192–2200. DOI: 10.1111/j.1420-9101.2009.01835.x.
3. J. Peña, “Group-size diversity in public goods games,” *Evolution* 66 (2012), 623–636. DOI: 10.1111/j.1558-5646.2011.01504.x. First online: 2011-11-04.
4. A. Hillenbrand and F. Winter, “Volunteering under Population Uncertainty,” *Games and Economic Behavior* (2018), DOI: 10.1016/j.geb.2017.12.009. Accessible author-hosted 2017 preprint: https://homepage.coll.mpg.de/pdf_dat/2017_12online.pdf; Proposition 1 and its appendix proof concern unobserved realized group size.
