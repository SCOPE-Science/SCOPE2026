# Sharp parameter dependence of the hazard-minimum age in the LR1 lifetime model

## Finding

Consider the one-parameter LR1 lifetime distribution: with probability \(\lambda^2/(1+\lambda^2)\) the lifetime is exponential of rate \(2\lambda\), and otherwise it is Gamma with shape four and rate \(\lambda/2\), where \(\lambda>0\). Write \(h_\lambda(t)\) for the failure hazard. Its minimum-age \(t_\lambda\) is the unique minimizer over \(t\ge0\).

Put
\[
Q(y)=\frac{e^{3y}y^2(y^2+4y+6)}{6(3y^3+15y^2+32y+32)},\qquad y>0.
\]
Then \(Q\) is a strictly increasing bijection from \((0,\infty)\) onto itself, and the exact minimum-age characterization is
\[
\lambda^2=Q(y_\lambda),\qquad t_\lambda=\frac{2y_\lambda}{\lambda}.
\]
**The parameter-to-age map \(\lambda\mapsto t_\lambda\) is strictly decreasing**, and its two sharp endpoint expansions are
\[
t_\lambda=8\sqrt2-\frac{256}{3}\lambda+O(\lambda^2)
\quad(\lambda\downarrow0),
\]
\[
t_\lambda=\frac2\lambda\left(\frac23\log\lambda-\frac13\log\log\lambda+\log3+o(1)\right)
\quad(\lambda\to\infty).
\]
The minimum hazard also has the sharp expansions
\[
h_\lambda(t_\lambda)=2\lambda^3-\frac{64\sqrt2}{3}\lambda^4+O(\lambda^5)
\quad(\lambda\downarrow0),
\]
\[
\frac{2h_\lambda(t_\lambda)}{\lambda}
=1-\frac{9}{2\log\lambda}
+O\!\left(\frac{\log\log\lambda}{(\log\lambda)^2}\right)
\quad(\lambda\to\infty).
\]
If \(\mu_\lambda=\mathbb E X_\lambda=(\lambda^2+16)/(2\lambda(1+\lambda^2))\), the minimum age relative to mean lifetime crosses from
\[
\frac{t_\lambda}{\mu_\lambda}\sim\sqrt2\,\lambda\to0
\quad\text{to}\quad
\frac{t_\lambda}{\mu_\lambda}\sim\frac83\log\lambda\to\infty.
\]
Thus an absolute minimum-age that shrinks monotonically can nevertheless lie an unbounded number of mean lifetimes into the distribution's future.

## Assumptions and scope

The time unit is fixed throughout the LR1 family. The Gamma distribution is parameterized by shape and **rate**. All statements concern fixed numerical \(\lambda>0\), with endpoint limits taken only afterward. The hazard is \(h_\lambda(t)=f_\lambda(t)/\Pr(X_\lambda>t)\), with its continuous right extension at \(t=0\). No assertion concerns sampling, fitted parameter uncertainty, or a cost-optimal replacement schedule.

## Proof

Let \(y=\lambda t/2\), \(q=\lambda^2\), and \(P(y)=1+y+y^2/2+y^3/6\). The published mixture formula yields, after cancellation of the common factor in the survival and density,
\[
h_\lambda(t)=\frac\lambda2 H_q(y),\qquad
H_q(y)=\frac{4q e^{-3y}+y^3/6}{q e^{-3y}+P(y)}.
\]
Writing \(A=q e^{-3y}\), direct differentiation (including \(A'=-3A\)) gives the exact sign identity
\[
H_q'(y)=\frac{y^2(y^2+4y+6)-6A(3y^3+15y^2+32y+32)}{12(A+P(y))^2}.
\]
The numerator has the sign of \(Q(y)-q\). Set \(F(y)=y^2+4y+6\) and \(G(y)=3y^3+15y^2+32y+32\), so that \(Q(y)=e^{3y}y^2F(y)/(6G(y))\). The decisive strict positivity identity is
\[
3F(y)G(y)+F'(y)G(y)-F(y)G'(y)
=9y^5+78y^4+306y^3+668y^2+844y+512>0.
\]
It follows that \(Q'(y)/Q(y)>2/y\) for every \(y>0\). Moreover \(Q(y)\sim y^2/32\) at zero and \(Q(y)\sim ye^{3y}/18\) at infinity. Thus \(Q\) maps \((0,\infty)\) bijectively and strictly increasingly onto \((0,\infty)\); the hazard derivative changes strictly from negative to positive at the unique \(y_\lambda\), proving global minimality.

Regarding \(\lambda=\sqrt{Q(y)}\) as an increasing function of \(y\), the minimum-age is \(t(y)=2y/\sqrt{Q(y)}\). Its logarithmic derivative satisfies
\[
\frac{t'(y)}{t(y)}=\frac1y-\frac{Q'(y)}{2Q(y)}<0.
\]
This proves strict decrease in \(\lambda\), not merely an ordering of endpoint limits.

At small \(y\), Taylor expansion gives
\[
Q(y)=\frac{y^2}{32}+\frac{y^3}{12}+O(y^4).
\]
Series inversion therefore gives
\[
y_\lambda=4\sqrt2\,\lambda-\frac{128}{3}\lambda^2+O(\lambda^3),
\]
which implies the small-parameter age formula. Substitution in \(\lambda H_{\lambda^2}(y_\lambda)/2\) gives the small-parameter minimum-hazard formula.

At large \(y\),
\[
Q(y)=\frac{ye^{3y}}{18}(1+O(y^{-1})),
\]
so
\[
2\log\lambda=3y_\lambda+\log y_\lambda-\log18+O(y_\lambda^{-1}).
\]
First \(y_\lambda\sim(2/3)\log\lambda\); one substitution into the logarithm then gives
\[
y_\lambda=\frac23\log\lambda-\frac13\log\log\lambda+\log3+o(1).
\]
At this root \(A=q e^{-3y_\lambda}=y_\lambda/18\,(1+O(y_\lambda^{-1}))\). Consequently the Gamma contribution dominates the rational hazard and
\[
H_{\lambda^2}(y_\lambda)=1-\frac3{y_\lambda}+O(y_\lambda^{-2}).
\]
The large-parameter minimum-hazard formula follows. Finally mixture conditioning gives \(\mu_\lambda=(\lambda^2+16)/(2\lambda(1+\lambda^2))\); dividing the two age asymptotics by this exact mean proves the ratio limits.

## Verification

The bundled `verify_hazard.py` checks the derivative and coefficient-positivity polynomials exactly using symbolic algebra, checks Taylor coefficients, and independently brackets the positive root for a grid spanning \(\lambda=10^{-8}\) through \(10^{40}\). It checks derivative signs around each bracketed minimum, monotonicity across grid values, and the endpoint expansions. The bundled `verification_output.txt` contains the reproduced output. These finite numerical checks are sanity tests; the proofs of monotonicity, uniqueness and asymptotics are the exact arguments above.

## Relationship to prior work

Singh and Patawa (arXiv:2610.24575v1, first publicly posted 2026-10-17) define LR1 and give its explicit hazard, initial decline and eventual increase, but expressly do not classify the number of hazard minima. **The qualitative bathtub-shape conclusion is not asserted as new here**: Block, Langberg, Savits and Wang (2010, Theorem 2.1) already establish such behavior in a broader exponential/IFR-Gamma mixture class containing this case. Block, Langberg and Savits (2012) classify failure-rate shapes for exponential/Gamma mixtures more broadly.

The contribution evaluated here is the **parameter-coupled minimum-age law**, its strict decrease as the LR1 parameter varies, and the quantitative endpoint formulas including the logarithmic correction and the mean-lifetime crossover. These do not follow from the cited qualitative shape statements alone. The 2012 primary paper's abstract was accessible, but its full text could not be retrieved in this investigation; an uninspected quantitative result remains a historical-priority risk.

## Limitations

The formulas apply only to the specific one-parameter LR1 restriction and to the declared fixed time unit; arbitrary time rescaling leaves that one-parameter family. The theorem concerns the age minimizing instantaneous hazard, not the minimizer of a replacement or maintenance cost functional. No uniform error estimate is claimed across the two endpoint regimes or for simultaneous changes in the Gamma shape or component-rate ratio. Broader preexisting formulas for hazard-minimum locations could reduce the historical novelty of the stated quantitative result; independent review is outstanding.

## References

1. L. Singh and R. Patawa, *The LR1 Lifetime Distribution: Properties, Nonmonotone Hazard, and Statistical Inference*, arXiv:2610.24575v1 (2026-10-17), https://arxiv.org/html/2610.24575.
2. H. W. Block, N. A. Langberg, T. H. Savits and J. Wang, *Continuous Mixtures of Exponentials and IFR Gammas Having Bathtub-Shaped Failure Rates*, Journal of Applied Probability 47 (2010), 899–907, https://doi.org/10.1239/jap/1294170507.
3. H. W. Block, N. A. Langberg and T. H. Savits, *A Glaser Twist: Focus on the Mixture Parameters*, Journal of Applied Probability 49 (2012), 1144–1155, https://doi.org/10.1239/jap/1354716663.
