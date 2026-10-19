# Counter-moving extreme excursions in renewal-reset random acceleration

## Finding

For a one-dimensional random-acceleration particle with *complete renewal resetting* of both position and velocity and Lomax reset durations, a stationary particle conditioned to be arbitrarily far to the right has a strictly positive probability of **moving left**. This limiting probability depends only on the renewal-tail exponent, not on diffusivity or the reset-duration scale. For each \(\alpha>0\), set \(s=2\alpha/3\), and write \(\varphi\) and \(\Phi\) for the standard normal density and distribution function. Then
\[
\boxed{\lim_{x\to\infty}\Pr(V<0\mid X>x)=Q(\alpha)
=\frac{\int_0^\infty z^s\varphi(z)\Phi(-\sqrt3z)\,dz}{\int_0^\infty z^s\varphi(z)\,dz}.}
\]
The function \(Q\) is strictly decreasing on \((0,\infty)\), with limits \(Q(0+)=1/6\) and \(Q(\infty)=0\). At the natural exact-moment parameter \(\alpha=3/2\),
\[
\boxed{Q(3/2)=(2-\sqrt3)/4=0.0669872981\ldots .}
\]
Thus even at arbitrarily large positive positions about \(6.7\%\) of particles are moving towards the reset point for this renewal exponent. The finding also determines the complete joint extreme-tail coefficient and a sharp mixed-moment finiteness frontier, stated below. These belong to the same stationary joint law.

Let \((G,H)\) be centered bivariate Gaussian with covariance \(\bigl(\begin{smallmatrix}1/3&1/2\\1/2&1\end{smallmatrix}\bigr)\). For \(p,q\ge0\) with \(p+q>0\), stationary moments satisfy
\[
\boxed{\mathbb E[|X|^p|V|^q]<\infty\quad\Longleftrightarrow\quad 3p+q<2\alpha.}
\]
If \(s_{p,q}=(3p+q)/2<\alpha\), their exact values are
\[
\mathbb E[|X|^p|V|^q]=(2D)^{(p+q)/2}b^{s_{p,q}}\frac{\Gamma(s_{p,q}+1)\Gamma(\alpha-s_{p,q})}{\Gamma(\alpha)}\,\mathbb E[|G|^p|H|^q].
\]
At equality and beyond, the mixed moment is infinite.

More specifically, define \(m_G=\mathbb E|G|^{2\alpha/3}\), \(m_H=\mathbb E|H|^{2\alpha}\). The stationary marginal absolute-tail constants are \(c_X=b^\alpha(2D)^{\alpha/3}m_G\) and \(c_V=b^\alpha(2D)^\alpha m_H\). If \(u_X(n)\) and \(u_V(n)\) are the upper \(1-1/n\) quantiles of \(|X|\) and \(|V|\), respectively, then their asymptotic co-exceedance coefficient is
\[
\boxed{\lim_{n\to\infty}n\Pr(|X|>u_X(n),\ |V|>u_V(n))
=\chi_\alpha=\mathbb E\!\left[\min\left\{\frac{|G|^{2\alpha/3}}{m_G},\frac{|H|^{2\alpha}}{m_H}\right\}\right]\in(0,1).}
\]
This coefficient is independent of \(D,b\). In particular extreme position and extreme velocity are asymptotically dependent, even though their marginal tail exponents differ by a factor of three.

## Assumptions and scope

Let \(D,b,\alpha>0\). Between independent resetting times, position and velocity evolve as \(dV_t=\sqrt{2D}\,dB_t\), \(dX_t=V_t\,dt\). Both are instantaneously returned to zero at each resetting epoch, after which a fresh independent Brownian noise and a fresh interarrival time are used. The positive iid interarrival times \(T\) obey \(\Pr(T>t)=(1+t/b)^{-(1+\alpha)}\) for all \(t\ge0\), and are independent of the driving noises. The state is sampled in the equilibrium stationary renewal regime, not at a fixed elapsed time after the initial reset. This model permits any \(\alpha>0\), including infinite stationary coordinate moments.

The coefficient \(\chi_\alpha\) concerns *absolute* marginal quantiles, whereas \(Q(\alpha)\) concerns a one-sided large positive position and the sign of velocity. The two different conditionings must not be conflated.

## Proof

**1. Stationary-age representation.** The mean interarrival is \(\mathbb ET=b/\alpha\). The stationary backward recurrence age \(A\) has density \(\Pr(T>a)/(\mathbb ET)=(\alpha/b)(1+a/b)^{-1-\alpha}\) and survival \(\Pr(A>a)=(1+a/b)^{-\alpha}\). The Brownian scaling identities on one renewal interval give the exact *joint*, not merely marginal, equality in distribution
\[
(X,V)\ \overset d=\ \sqrt{2D}\,(A^{3/2}G,\ A^{1/2}H),\qquad
G=\int_0^1B_s\,ds,\quad H=B_1,\quad A\perp(G,H).
\]
Brownian covariance integration gives \(\mathbb EG^2=1/3\), \(\mathbb EGH=1/2\), \(\mathbb EH^2=1\), and Gaussian determinant \(1/12>0\). In particular the joint law is not supported on a line.

**2. Mixed moments.** For every real \(s>0\), integrating the displayed age density with \(a=by\) yields \(\mathbb EA^s=b^s\Gamma(s+1)\Gamma(\alpha-s)/\Gamma(\alpha)\) exactly when \(s<\alpha\), and divergence when \(s\ge\alpha\). Independently, \(\mathbb E|G|^p|H|^q\in(0,\infty)\) for all finite \(p,q\ge0\). Since the age exponent is \(s_{p,q}=(3p+q)/2\), the finiteness criterion and exact value follow, including its boundary.

**3. Conditional counter-moving limit.** By symmetry only \(G>0\) contributes to \(X>x\). For every fixed \(g>0\),
\[
\lim_{x\to\infty}x^{2\alpha/3}
\Pr\!\left(A>\left[\frac{x}{\sqrt{2D}\,g}\right]^{2/3}\right)
=b^\alpha(\sqrt{2D}\,g)^{2\alpha/3}.
\]
For every \(x,g>0\), the scaled probability is bounded above by the same integrable right-hand side because \((1+y/b)^{-\alpha}\le(b/y)^\alpha\). Dominated convergence therefore gives the one-sided tail and the signed tail with indicator \(H<0\); their ratio is \(\mathbb E[G_+^s\mathbf1_{\{H<0\}}]/\mathbb E[G_+^s]\). Put \(Z=\sqrt3G\). The conditional normal law is \(H\mid Z=z\sim N((\sqrt3/2)z,1/4)\), hence \(\Pr(H<0\mid Z=z)=\Phi(-\sqrt3z)\). This proves the integral for \(Q(\alpha)\).

**4. Strict monotonicity and sharp values.** Under the tilted probability density proportional to \(z^s\varphi(z)\mathbf1_{z>0}\), \(Q\) is the expectation of the strictly decreasing function \(\Phi(-\sqrt3z)\). Increasing \(s\) gives a strict monotone-likelihood-ratio tilt; equivalently, its derivative has negative covariance \(\operatorname{Cov}_s(\log Z,\Phi(-\sqrt3Z))<0\). As \(s\downarrow0\), the fraction tends to \(\Pr(GH<0\mid G>0)=\arccos(\sqrt3/2)/\pi=1/6\), using the standard Gaussian quadrant-angle identity (or a two-dimensional polar integral). As \(s\to\infty\), the tilted positive normal variable escapes to infinity in probability, so \(Q\to0\). At \(\alpha=3/2\), \(s=1\); integration by parts yields \(\int_0^\infty z\varphi(z)\Phi(-az)dz=(1-a/\sqrt{1+a^2})/(2\sqrt{2\pi})\). Divide by \(\int_0^\infty z\varphi(z)dz=1/\sqrt{2\pi}\) and set \(a=\sqrt3\) to obtain \((2-\sqrt3)/4\).

**5. Joint extremes.** For \(x,v>0\), conditional on \((G,H)\) both absolute exceedances require
\[
A>t\max\left\{\left(\frac{x}{\sqrt{2D}|G|}\right)^{2/3},\left(\frac{v}{\sqrt{2D}|H|}\right)^2\right\}
\]
when the thresholds are \(|X|>xt^{3/2}\), \(|V|>vt^{1/2}\). The age-tail formula, followed by dominated convergence bounded by integrable Gaussian powers, gives
\[
\lim_{t\to\infty}t^\alpha\Pr(|X|>xt^{3/2},|V|>vt^{1/2})
=b^\alpha\mathbb E\min\left\{\left(\frac{\sqrt{2D}|G|}{x}\right)^{2\alpha/3},\left(\frac{\sqrt{2D}|H|}{v}\right)^{2\alpha}\right\}.
\]
Taking one marginal at a time supplies \(\Pr(|X|>x)\sim c_Xx^{-2\alpha/3}\) and \(\Pr(|V|>v)\sim c_Vv^{-2\alpha}\). Consequently \(u_X(n)\sim(c_Xn)^{3/(2\alpha)}\) and \(u_V(n)\sim(c_Vn)^{1/(2\alpha)}\); substitution yields \(\chi_\alpha\). Both normalized Gaussian powers are positive a.s. and have mean one. Because the pair has a strictly positive Gaussian density and the normalized powers are not equal a.s., \(\mathbb E\min(A_*,B_*)=1-\mathbb E|A_*-B_*|/2\) is strictly between zero and one.

## Verification

The standalone file `checks.py` verifies the strict covariance determinant, one-dimensional quadrature of \(Q\) and its exact \(\alpha=3/2\) value, the age beta-integral moment identity using independent quadrature, selected analytic covariance identities, convergence of the conditional reverse-sign fraction at three large finite displacement thresholds, and deterministic two-dimensional Gauss–Hermite calculations yielding a co-exceedance coefficient between zero and one. Run `python checks.py` with NumPy and SciPy. Every universal conclusion above is analytical; numerical checks alone are not used to infer positivity, monotonicity, or infinite-size limits.

## Relationship to prior work

Singh, *Random acceleration process under stochastic resetting* (arXiv:2007.05576v1, 2020), establishes the reset-free integrated Brownian position–velocity covariance and the joint stationary law under exponential complete resetting. His reset protocol has memoryless, not Lomax, waiting times. Montero, Palassini and Masoliver, *The effect of stochastic resettings on the counting of level crossings for inertial random processes* (arXiv:2312.13968v1, 2023), develop a Poisson-reset joint-position/velocity framework and crossing intensities, again not the present heavy-tail conditional extremes. Bodrova, Chechkin and Sokolov, *Scaled Brownian motion with renewal resetting* (arXiv:1812.05667, initially 2018; inspected v2), develop power-law-reset stationary **position-marginal** asymptotics for Gaussian transport, including the displacement marginal analogous to the exponent \(2\alpha/3\) here. Consequently the marginal displacement tail is *not* claimed as a standalone discovery. Standard Gaussian conditioning, equilibrium renewal-age theory and product-tail/Breiman-type arguments are also established mathematical ingredients; the present result is their explicit synthesis for the **joint kinematic** reverse-direction extreme probability, its strict exponent dependence and exact value, and the linked joint co-exceedance and mixed-moment laws.

## Limitations

This is a complete-reset, independent-renewal, scalar random-acceleration model with strictly positive \(D,b,\alpha\), observed at stationarity. The conclusion is not proved for position-only resets, history-dependent reset times, damping, correlated noise across renewal intervals, or finite-time sampling. The limit describes conditional frequency rather than a single particle trajectory. The threshold limits may be statistically difficult to estimate and do not establish a finite-sample estimator. Prior general multivariate regular-variation theorems may imply substantial components after specializing to this model; independent priority adjudication is not performed. In particular no novelty is asserted for the individual heavy-tail marginal alone.

## References

1. P. Singh, *Random acceleration process under stochastic resetting*, arXiv:2007.05576v1 (first publicly submitted 10 July 2020), https://arxiv.org/abs/2007.05576.
2. A. S. Bodrova, A. V. Chechkin, and I. M. Sokolov, *Scaled Brownian motion with renewal resetting*, arXiv:1812.05667 (first public version 2018; inspected v2), https://arxiv.org/abs/1812.05667.
3. M. Montero, M. Palassini, and J. Masoliver, *The effect of stochastic resettings on the counting of level crossings for inertial random processes*, arXiv:2312.13968v1 (2023), https://arxiv.org/abs/2312.13968.
