# Two distinct optimal-tumbling transitions for mean and variance of confined active escape

## Finding

For a persistent particle escaping from a one-dimensional interval with a sticky left wall whose direction-reversal rate is enhanced relative to the bulk, **mean and variance of the first-passage time undergo different sharp optimization transitions**. Denote the dimensionless bulk tumbling rate by \(a\) and the wall enhancement by \(g\). The previously known mean-optimality threshold is
\[
 g_{\rm mean}=\frac{\sqrt7-1}{3}=0.548583770354\ldots,
\]
whereas the variance-optimality threshold is
\[
 g_{\rm var}=\frac{\sqrt[3]{10}-1}{2}=0.577217345015\ldots>g_{\rm mean}.
\]
At every \(g\) in the *nonempty half-open interval* \([g_{\rm mean},g_{\rm var})\), the **mean** escape time is uniquely minimized at zero bulk tumbles, while the **variance** is uniquely minimized at a strictly positive bulk rate. More generally, whenever the two minimizers are defined, the variance-optimal rate is strictly larger than the mean-optimal rate for \(0\le g<g_{\rm var}\). This is a classification of optimality, not a claim that the model, its mean exit time, or its complete exit-time transform were previously unknown.

Write \(Y=vT/R\) for dimensionless first-passage time. Its variance is
\[
 V(a,g)=\frac{15a^4+30a^3g+60a^3+15a^2g^2+92a^2g+72a^2+32ag^2+60ag+48a+6g^2+12g+18}{6(a+g)^2}.
\]
Define
\[
\begin{aligned}
 P_g(a)={}&15a^4+(45g+30)a^3+(45g^2+90g)a^2\\
 &+(15g^3+76g^2+42g-24)a\\
 &+16g^3+24g^2+12g-18.
\end{aligned}
\]
Then \(\partial_a V=P_g(a)/[3(a+g)^3]\). For \(0\le g<g_{\rm var}\), \(P_g\) has exactly one strictly positive root \(a_{\rm var}(g)\), which is the unique global variance minimizer among admissible \(a\). For \(g\ge g_{\rm var}\), the variance is strictly increasing for \(a>0\) and has its unique minimum at \(a=0\), which is admissible because \(g>0\). At the critical point the interior minimizer collapses linearly:
\[
 a_{\rm var}(g)=\frac{12\,10^{2/3}}{15g_{\rm var}^3+76g_{\rm var}^2+42g_{\rm var}-24}(g_{\rm var}-g)+O((g_{\rm var}-g)^2)
\quad(g\uparrow g_{\rm var}).
\]

## Assumptions and scope

Let \(R,v>0\). The particle starts at \(x=0\) with velocity \(+v\) or \(-v\), each with probability \(1/2\). In the interior \((-R,R)\), it moves ballistically and reverses its direction at Poisson rate \(\alpha/2\). The right boundary \(R\) absorbs immediately upon first arrival. On reaching \(-R\) while moving left, the particle waits at that wall until an independent exponential waiting time with rate \((\alpha+\gamma)/2\) expires, then leaves to the right. Here \(\alpha,\gamma\ge0\), \(\alpha+\gamma>0\), with no translational diffusion and no additional wall absorption. All clocks are memoryless and independent of subsequent motion.

Set \(a=\alpha R/v\), \(g=\gamma R/v\), \(Y=vT/R\). The domain of the formulas is \(a,g\ge0\), \(a+g>0\). For \(g=0\), optimization runs over \(a>0\) because \(a=0\) could trap a left-moving particle forever; for \(g>0\), optimization runs over \(a\ge0\). The unique-optimizer statements hold for every such \(g\), with no limit on other parameters.

## Proof

**Moment boundary-value problem.** Scale space by \(R\), time by \(R/v\). Write \(u_n^\pm(x)=\mathbb E_{x,\pm}[Y^n]\) for \(n=0,1,2\), with \(u_0^\pm\equiv1\). In the interior the backward generator is
\[
 {\cal L}f_+=f_+'+\frac a2(f_--f_+),\qquad
 {\cal L}f_-=-f_-'+\frac a2(f_+-f_-).
\]
Thus \({\cal L}u_n^\pm=-n u_{n-1}^\pm\). Set \(s_n=u_n^++u_n^-\), \(d_n=u_n^+-u_n^-\), obtaining
\[
 d_n'=-n s_{n-1},\qquad s_n'=-n d_{n-1}+a d_n.
\]
The exit boundary gives \(u_n^+(1)=0\) for \(n\ge1\), and therefore \(s_n(1)+d_n(1)=0\). From \(-1\), the left-moving state waits an independent \({\rm Exp}((a+g)/2)\) time \(W\), then restarts as right-moving from \(-1\). The binomial formula and \(\mathbb EW^j=j![2/(a+g)]^j\) imply, for the first two moments,
\[
 u_1^-(-1)=u_1^+(-1)+\frac{2}{a+g},\qquad
 u_2^-(-1)=u_2^+(-1)+\frac{4u_1^+(-1)}{a+g}+\frac{8}{(a+g)^2}.
\]
Equivalently the recurrence boundary condition is \(d_n(-1)=-n[s_{n-1}(-1)-d_{n-1}(-1)]/(a+g)\) for \(n=1,2\). (For \(n=2\), the first-order boundary relation eliminates the explicit waiting-time second-moment term.) These two first-order linear equations, the exit condition, and the wall condition uniquely determine \(s_n,d_n\) at each order. Integration yields at the center
\[
 M(a,g)=\frac{s_1(0)}2=2+\frac{3a}{2}+\frac{1+a}{a+g},
\]
and
\[
\mathbb E[Y^2]=\frac{57a^4+114a^3g+228a^3+57a^2g^2+364a^2g+288a^2+136ag^2+300ag+168a+60g^2+72g+48}{12(a+g)^2}.
\]
Subtracting \(M^2\) produces \(V\) above. A symbolic reproduction of the recurrence, and an independent numerical differentiation of a boundary-value Laplace transform, are supplied in `verify_escape_variance.py`.

**Existence and finiteness.** For each \(a+g>0\), start from any admissible interior or wall state. With probability at least \(p=e^{-5a/2}(1-e^{-(a+g)/2})>0\), there is no bulk direction reversal before exit, and (if the path reaches the left wall) a wall release occurs within one dimensionless time unit. Such a path is absorbed within five dimensionless time units: at most two units to reach the left wall and at most two more to cross from it to the right. The strong Markov property gives \(\mathbb P(Y>5n)\le(1-p)^n\), proving an exponential moment near the origin and justifying the moment equations. The displayed moments and their differentiation are therefore legitimate. At \(a=0,g>0\), the direct mixture of a one-unit rightward flight and a three-unit left-wall route with an additional \({\rm Exp}(g/2)\) wait also gives the continuous endpoint formula.

**Variance optimizer.** Direct differentiation gives \(\partial_aV=P_g(a)/[3(a+g)^3]\). The constant term is
\[
 P_g(0)=2[(2g+1)^3-10].
\]
It is negative exactly when \(g<g_{\rm var}\). For such \(g\), the coefficients of \(a^4,a^3\) are strictly positive and that of \(a^2\) is nonnegative (zero only at \(g=0\)); the coefficient of \(a\) may have either sign; and the constant coefficient is negative. The descending coefficient sequence therefore has exactly one sign change. Descartes' rule, together with \(P_g(0)<0\) and \(P_g(a)\to+\infty\), proves one simple positive root and a decrease-then-increase variance profile. For \(g\ge g_{\rm var}>1/2\), the coefficient \(15g^3+76g^2+42g-24\) is positive because it increases with \(g\) and equals \(143/8>0\) at \(g=1/2\); every other coefficient is nonnegative, so \(P_g(a)>0\) whenever \(a>0\). The variance increases quadratically at large \(a\), and the stated minimizers are global.

**Strict separation from the mean optimum.** From the known exact mean,
\[
 \partial_aM=\frac32+\frac{g-1}{(a+g)^2},
\]
so the mean-optimal rate is \(a_{\rm mean}(g)=\sqrt{2(1-g)/3}-g\) for \(0\le g<g_{\rm mean}=(\sqrt7-1)/3\), and \(0\) for \(g\ge g_{\rm mean}\). For \(0\le g<g_{\rm mean}\), put \(t=a_{\rm mean}+g=\sqrt{2(1-g)/3}>1/2\). Substitution into the *variance* derivative gives
\[
 \left.\partial_aV\right|_{a=a_{\rm mean}}=-\frac{18t^4+51t^3+12t^2-8}{6t^2}<0.
\]
The numerator increases strictly for positive \(t\) and equals \(5/2\) at \(t=1/2\), so the variance minimizer lies strictly to the right of the mean minimizer. When \(g_{\rm mean}\le g<g_{\rm var}\), the mean minimizer is zero while the variance minimizer is positive. The interval is nonempty since \(g_{\rm mean}<11/20<57/100<g_{\rm var}\). Finally \(\partial_aP_g(0)|_{g=g_{\rm var}}=15g_{\rm var}^3+76g_{\rm var}^2+42g_{\rm var}-24>0\), whereas \(\partial_gP_g(0)|_{g=g_{\rm var}}=12\,10^{2/3}\); the implicit-function theorem yields the stated linear collapse.

## Verification

Execute `python verify_escape_variance.py` with SymPy and mpmath installed. The script reconstructs the first two backward moments and boundary conditions symbolically, verifies both closed-form formulas and their derivative, and independently computes the Laplace transform from a transfer matrix, differentiating it numerically at six parameter pairs. It also checks qualitative root counts at ten sample enhancement rates. Its observed output was `PASS 42 exact symbolic, independent Laplace, and parameter-sample checks`. Those finitely many numerical samples do **not** establish uniqueness for all \(a,g\); the coefficient-sign argument above does. The provided file contains the full algorithm and dependencies.

## Relationship to prior work

Angelani's *One-dimensional run-and-tumble motions with generic boundary conditions* (published 16 October 2023) gives the general boundary formalism, exact first-passage Laplace transform (equation 45), and mean formula (equation 47). Thus the model and full first-passage transform are **prior results**, from which the displayed variance is in principle obtainable by differentiation; the variance expression alone is not a novel distributional solution. Angelani's *Optimal escapes in active matter* (public preprint 20 November 2023, section 2, equations 7–11) states the same enhanced-wall mean and its threshold \(g_{\rm mean}\). The contribution assessed here is the **second and strictly higher variance-optimality threshold, global uniqueness and strict comparison of both optimal rates**. Jeon, Go, and Kim (preprint 6 October 2023) analyze a partially absorbing interior target and obtain exit-time fluctuation quantities, but their target/wall geometry and tuned parameter are not the present enhanced-left-wall setup. The general transform remains a meaningful implicit-priority risk; independent literature assessment is still needed.

## Limitations

The sharp thresholds apply only to symmetric initial velocity, homogeneous Poisson bulk tumbles, independent exponential wall release with the stated enhanced rate, and absorption at the opposite endpoint. They do not describe translational Brownian noise, non-Poisson waiting times, bulk drift, partial right-wall absorption, or random initial position. A second moment is not a guarantee of an improved tail at every probability level. The first-passage law itself was known from previous general methods.

## References

1. L. Angelani, *One-dimensional run-and-tumble motions with generic boundary conditions*, J. Phys. A: Math. Theor. **56** (2023), 455003, DOI: 10.1088/1751-8121/ad009e, public 16 October 2023. Open-access article: https://iris.cnr.it/retrieve/e1d78abe-8685-4eff-936b-9bcad8ad4c0f/prod_489129-doc_203607.pdf .
2. L. Angelani, *Optimal escapes in active matter*, Eur. Phys. J. E **47** (2024), article 9, DOI: 10.1140/epje/s10189-023-00402-7, preprint arXiv:2311.11873 first public 20 November 2023. Full open article: https://link.springer.com/article/10.1140/epje/s10189-023-00402-7 .
3. E. Jeon, B. G. Go, and Y. W. Kim, *Searching for a partially absorbing target by a run-and-tumble particle in a confined space*, Phys. Rev. E **109** (2024), 014103, DOI: 10.1103/PhysRevE.109.014103; preprint arXiv:2310.04016, first public 6 October 2023. https://arxiv.org/pdf/2310.04016 .
