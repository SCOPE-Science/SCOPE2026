# A sharp survival floor and unique optimal mixing of immediate and delayed dispersal

## Finding
Consider a two-channel, two-generation linear plant-dispersal recurrence on the integer lattice. Immediate propagules move one site per generation; surviving delayed propagules travel two sites and contribute after two generations. For every growth multiplier \(1<R<2\) and delayed-channel survival \(1/R<s\leq1\), the exact linear exponential-envelope speed is uniquely maximized as follows.

Let \(t_R>0\) be the unique solution of
\[
t_R\tanh t_R-\log\cosh t_R=\log R,
\]
and put \(c_0(R)=\tanh t_R\) and
\[
s_c(R)=\frac{R}{1+c_0(R)^2}.
\]
If \(s\leq s_c(R)\), using only the immediate channel is the unique speed-optimal choice. If \(s>s_c(R)\), there is a unique strictly interior allocation \(\theta_{\rm opt}\in(0,1)\); its speed strictly exceeds that of either pure channel, even at \(s=1\), when the two pure-channel speeds coincide. Define
\[
u=\sqrt{R/s-1},\quad \tau=\operatorname{arctanh}u,\quad z=\tanh(2\tau),\quad v=\frac{\log(R\cosh\tau)}{\tau}.
\]
Then
\[
\theta_{\rm opt}=\frac{v-u}{2z-u-v},\qquad c(\theta_{\rm opt})=v.
\]
Moreover, \(s_c(R)\) has a unique global minimum on \(1<R<2\),
\[
s_{\min}=0.878135713950414\ldots,
\]
at \(R_*=1.363120373806496\ldots\). The parameter \(t_*=0.957504024077269\ldots\) is the unique positive root of \(t=\tanh(2t)\), and \(R_*=\exp(t_*\tanh t_*)/\cosh t_*\). The threshold \(s_c\) decreases on \((1,R_*)\), increases on \((R_*,2)\), and tends to \(1\) at both ends. Thus for each fixed \(s\in(s_{\min},1)\) there is exactly one bounded open growth interval on which an interior allocation beats both pure strategies; outside its closure pure immediate dispersal is optimal. For \(s=1\) the interval is all \(1<R<2\).

## Assumptions and scope
Fix \(1<R<2\), \(1/R<s\le1\), and \(0\le\theta\le1\). The scalar population density \(n_k(j)\) at integer time \(k\) and site \(j\in\mathbb Z\) evolves by
\[
n_{k+1}(j)=\frac{R(1-\theta)}2\big[n_k(j-1)+n_k(j+1)\big]
+\frac{Rs\theta}2\big[n_{k-1}(j-2)+n_{k-1}(j+2)\big].
\]
This is a specified positive linear recursion, not an empirical plant model. A fraction \(\theta\) is assigned to delayed, longer-range offspring, whose survival factor is \(s\); the remainder uses one-generation local dispersal. Two initial generations are specified and no density dependence, mortality outside \(s\), or spatial heterogeneity is assumed.

For a spatial exponential mode \(\exp(-tj)\), \(t>0\), its positive temporal growth factor \(\lambda_\theta(t)\) solves
\[
\lambda_\theta(t)^2=R(1-\theta)\cosh(t)\lambda_\theta(t)+Rs\theta\cosh(2t).
\]
Define the *linear exponential-envelope speed functional*
\[
c(\theta)=\inf_{t>0}\frac{\log\lambda_\theta(t)}t.
\]
The theorem concerns this precisely defined quantity. It does not assert nonlinear front selection or measured invasion velocity. Strict inequalities and uniqueness below refer to all admissible real parameters, not a numerical grid.

## Proof
**1. Unique finite minimizing spatial tilt.** Write \(g_\theta(t)=\log\lambda_\theta(t)\). Set
\[
p=R(1-\theta)\cosh(t)e^{-g_\theta(t)},\qquad
q=Rs\theta\cosh(2t)e^{-2g_\theta(t)}.
\]
Then \(p,q\ge0\) and \(p+q=1\). Twice differentiating the defining exponential equation gives the exact identity
\[
g_\theta''(t)=\frac{p[(\tanh t-g_\theta')^2+\operatorname{sech}^2t]
+q[(2\tanh 2t-2g_\theta')^2+4\operatorname{sech}^2(2t)]}{p+2q}>0.
\]
The strict inequality persists at \(\theta=0\) and \(\theta=1\). Since \(R[(1-\theta)+s\theta]>1\), \(g_\theta(0)>0\), so \(g_\theta(t)/t\to+\infty\) as \(t\downarrow0\). As \(t\to\infty\),
\[
\lambda_\theta(t)\sim L_\theta e^t,\quad
L_\theta^2=\tfrac{R(1-\theta)}2L_\theta+\tfrac{Rs\theta}2.
\]
The positive \(L_\theta<1\), because the polynomial on the right evaluated at \(L=1\) is smaller than one for \(R<2\). Thus \(g_\theta(t)=t+\log L_\theta+o(1)\), with \(\log L_\theta<0\). The function \(t g_\theta'(t)-g_\theta(t)\) is strictly increasing, since its derivative is \(tg_\theta''(t)>0\); its endpoint limits are \(-g_\theta(0)<0\) and \(-\log L_\theta>0\). It has a unique zero. Hence \(c(\theta)\) has a unique finite minimizing tilt \(t_\theta\) for every \(\theta\in[0,1]\). Implicit differentiation and the strictly positive curvature give continuous, differentiable dependence on \(\theta\), including one-sided derivatives at endpoints.

**2. Pure strategies and the survival threshold.** At \(\theta=0\), \(\lambda_0(t)=R\cosh t\). At \(\theta=1\), \(\lambda_1(t)=\sqrt{Rs\cosh(2t)}\), whence \(c(0)=c_0(R)\) and \(c(1)=c_0(Rs)\le c_0(R)\). The unique defining equation for \(t_R\) follows from the stationary condition; its left side increases strictly from zero to \(\log2\). The sign of the right derivative of \(c\) at zero is the sign of
\[
\frac{s}{R}\big[1+\tanh^2(t_R)\big]-1.
\]
Indeed the envelope derivative is
\[
c'_+(0)=\frac{1}{t_R}\left(\frac{s}{R}[1+\tanh^2 t_R]-1\right).
\]
Consequently this derivative is strictly positive exactly when \(s>s_c(R)\).

For \(s<s_c(R)\), at the fixed test tilt \(t_R\) the quadratic growth-root is strictly smaller than \(R\cosh t_R\) whenever \(\theta>0\), because \(Rs\cosh 2t_R<(R\cosh t_R)^2\). Hence \(c(\theta)<c(0)\). At equality \(s=s_c(R)\), this growth-root equals \(R\cosh t_R\) for every \(\theta\), but for \(\theta>0\) its logarithmic tilt derivative is
\[
\frac{(1-\theta)\tanh t_R+2\theta\tanh(2t_R)}{1+\theta}>\tanh t_R=c(0).
\]
Thus \(t_R\) is not the minimizing tilt for these allocations; strict convexity gives \(c(\theta)<c(0)\). This proves uniqueness of \(\theta=0\) throughout the nonenhancing regime, including equality.

**3. Existence and uniqueness of an enhancing interior optimum.** For \(s>s_c(R)\), the preceding right derivative is positive, whereas \(c(1)\le c(0)\); compactness gives a global maximum at some interior \(\theta\), necessarily strictly exceeding both endpoint speeds. To prove uniqueness, fix a tilt \(t\). Implicit differentiation of the positive quadratic root shows that the sign of \(\partial_\theta\lambda_\theta(t)\) agrees with the sign of
\[
Rs\cosh(2t)-R^2\cosh^2t.
\]
For an interior extremum of \(c\), the envelope theorem forces this difference to vanish at its minimizing tilt, i.e.
\[
\tanh^2t=R/s-1.
\]
Because \(s>s_c(R)>R/2\), it has precisely one positive solution \(t=\tau\). There, the positive root is identically \(R\cosh\tau\), so its log-derivative in tilt becomes
\[
\frac{(1-\theta)u+2\theta z}{1+\theta}.
\]
This expression is strictly increasing in \(\theta\), since \(z=\tanh2\tau>u\). Equality to \(v=\log(R\cosh\tau)/\tau\) therefore has at most one solution. Solving gives the displayed \(\theta_{\rm opt}\). The previously proved interior existence guarantees \(0<\theta_{\rm opt}<1\), positivity of its denominator, and global uniqueness. Its value follows because \(\lambda_\theta(\tau)=R\cosh\tau\).

**4. Universal floor and bounded growth band.** Parametrize \(R=\exp(t\tanh t)/\cosh t\), a strictly increasing bijection from \((0,\infty)\) to \((1,2)\). Then
\[
\frac{d}{dt}\log s_c(R(t))=\operatorname{sech}^2(t)\,[t-\tanh(2t)].
\]
The function \(\tanh(2t)-t\) is strictly concave on \(t>0\), positive for sufficiently small positive \(t\), and negative for \(t\ge1\), hence has exactly one positive zero \(t_*\). This proves the unique minimum and the strict decreasing–increasing shape of \(s_c\). Its limits are \(1\) as \(R\downarrow1\) and \(R\uparrow2\). Thus each \(s\in(s_{\min},1)\) cuts the threshold at exactly two distinct growth multipliers, giving the claimed unique growth band. Finally, \(s_c(R)>1/R\) because \(2\log R(t)-\log(1+\tanh^2t)\) has derivative \(2\operatorname{sech}^2t\,[t-\tanh t/(1+\tanh^2t)]>0\) and tends to zero at \(t\downarrow0\); the admissible domain is nonempty.

## Verification
The supplied `verification.py` uses only the Python standard library and reproducible random seeds. Execute `python3 verification.py`. It tests the quadratic spectral identity, derivatives, equality of pure-channel speeds with \(c_0\), 90 randomly selected models across each enhancing/nonenhancing regime with numerical speed minimization, the explicit interior-optimum expression, the unique universal-minimum root, and a worked example.

For \(R=1.5\), \(s=0.95\), the calculated quantities are \(s_c=0.885861131610134\ldots\), \(\theta_{\rm opt}=0.239805157409638\ldots\), and \(c(\theta_{\rm opt})=0.839377540710766\ldots\). The two pure speeds are \(0.832626959836046\ldots\) and \(0.787149686619521\ldots\). Symbolic inequalities and strict convexity above, not finite tests, certify the universal statement.

## Relationship to prior work
General stage-structured invasion-speed formulas and sensitivity analysis were developed by Neubert and Caswell (2000). Meyer and Li (2013) treated age-structured seed banks and spreading speeds with considerably broader life-history structure. Lutscher (2019) discussed enhanced or anomalous spreading in coupled or mixed-morph systems. These established frameworks motivate the spectral formulation and already imply that mixed strategies *can* affect speed; neither that general observation nor the spectral-root method is presented as new.

The specific claim here is the all-parameter optimal allocation and its *exact global bifurcation diagram* for a competing one-season/one-step and two-season/two-step channel, including the unique universal survival floor and reentrant growth band. The inspected accessible sources did not state those combined results. The full Meyer–Li article could not be inspected; this leaves historical-priority uncertainty, as does possible subsumption by a general spectral-envelope optimization theorem. A 1980 paper by Venable and Lawlor addressed dispersal/dormancy tradeoffs for a different fitness objective, based on its available abstract; its complete text was not taken as checked.

## Limitations
Only the specified linear recurrence and its exponential-envelope speed are established. No nonlinearly selected front, finite-population stochastic invasion, environmental heterogeneity, genetic evolution of dormancy fraction, or empirical speed enhancement is proved. The assumed delayed pathway has both greater travel distance and a fixed one-generation delay, rather than representing every physiological seed-bank mechanism. Parameter bounds \(1<R<2\) and \(1/R<s\le1\) are essential to finite speed minimizers and strict supercriticality; no claim is made outside them. Search and historical-text limitations prevent independent certification of priority.

## References
- M. G. Neubert and H. Caswell, *Demography and dispersal: calculation and sensitivity analysis of invasion speed for structured populations*, Ecology 81 (2000), 1613–1628; DOI: `10.1890/0012-9658(2000)081[1613:DADCAS]2.0.CO;2`. First online 2000-06-01.
- K. I. Meyer and B. Li, *A Spatial Model of Plants with an Age-Structured Seed Bank and Juvenile Stage*, SIAM Journal on Applied Mathematics 73 (2013), 1676–1702; DOI: `10.1137/120880501`. First online 2013-08-06; primary MSC 92D40.
- F. Lutscher, *Integrodifference Equations in Spatial Ecology*, Springer (2019); DOI: `10.1007/978-3-030-29294-2`.
- D. L. Venable and L. Lawlor, *Delayed germination and dispersal in desert annuals: escape in space and time*, Oecologia 46 (1980), 272–282; DOI: `10.1007/BF00540137`.
