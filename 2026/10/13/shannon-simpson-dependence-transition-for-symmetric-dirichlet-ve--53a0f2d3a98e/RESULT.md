# Shannon–Simpson dependence transition for symmetric Dirichlet vectors

## Finding

Let \(m\ge 2\) be an integer and \(a>0\). Let \(P=(P_1,\ldots,P_m)\) have the symmetric Dirichlet law \(\operatorname{Dirichlet}(a,\ldots,a)\). Write \(A=ma\), let \(H=-\sum_{i=1}^m P_i\log P_i\) be Shannon entropy (natural logarithms), and let \(Q=\sum_{i=1}^mP_i^2\) be Simpson concentration, not its complementary diversity index. Then

\[
\operatorname{Cov}(H,Q)=-\frac{a(m-1)}{(A+1)^2(A+2)}<0,
\]

\[
\operatorname{Var}(H)=\frac{a+1}{A+1}\psi_1(a+1)-\psi_1(A+1),\qquad
\operatorname{Var}(Q)=\frac{2a(a+1)(m-1)}{(A+1)^2(A+2)(A+3)},
\]

where \(\psi_1\) is the trigamma function. All displayed variances are strictly positive.

For every fixed \(a>0\), the correlation has the nonzero limiting value

\[
\rho(a):=\lim_{m\to\infty}\operatorname{Corr}(H,Q)
=-\frac{1}{\sqrt{2(a+1)\big[(a+1)\psi_1(a+1)-1\big]}}.
\]

**The limiting correlation \(\rho(a)\) is strictly decreasing on \((0,\infty)\).** More precisely,

\[
\lim_{a\downarrow0}\rho(a)
=-\frac{1}{\sqrt{2(\pi^2/6-1)}}
=-0.8804959104\ldots,\qquad
\lim_{a\to\infty}\rho(a)=-1.
\]

An additional singular-limit distinction holds. For **every fixed** \(m\ge2\),

\[
\lim_{a\downarrow0}\operatorname{Corr}(H,Q)
=-\frac{\sqrt3}{2\sqrt{2\zeta(3)-\pi^2/6}}
=-0.9939357851\ldots.
\]

Consequently the two iterated limits of the correlation with respect to \(m\to\infty\) and \(a\downarrow0\) **do not commute**. Explicitly,

\[
\lim_{m\to\infty}\lim_{a\downarrow0}\operatorname{Corr}(H,Q)
=-0.9939357851\ldots
\ne
\lim_{a\downarrow0}\lim_{m\to\infty}\operatorname{Corr}(H,Q)
=-0.8804959104\ldots.
\]

For fixed \(a>0\), there is also a joint central limit theorem. With \(\psi\) denoting digamma,

\[
\begin{pmatrix}
\sqrt m\,[H-\mathbb EH]\\
m^{3/2}[Q-\mathbb EQ]
\end{pmatrix}
\ \xrightarrow{\,d\,}\
N_2\!\left(0,
\begin{pmatrix}
\dfrac{(a+1)\psi_1(a+1)-1}{a}&-\dfrac1{a^2}\\
-\dfrac1{a^2}&\dfrac{2(a+1)}{a^3}
\end{pmatrix}\right).
\]

For the uniform-spacing specialization \(a=1\), the first covariance identity reduces to \(-(m-1)/[(m+1)^2(m+2)]\), while the general \(a\)-dependent correlation transition and its two distinct singular limits concern the full concentration family.

## Assumptions and scope

All assertions concern an **unconditional** symmetric finite-dimensional Dirichlet random vector. The integer \(m\) is a number of components; \(a>0\) is the shape parameter of **each** component, not total concentration. There are no independent ecological observations or estimated parameters. The logarithm is natural, and the probability vector lies in the open simplex almost surely. The endpoints \(a=0\) and \(a=\infty\) are limiting regimes, not Dirichlet distributions admitted in the theorem. For \(m=1\) both statistics are constant, so the correlation would be undefined and is not asserted.

For \(a=1\) the model is also the complete spacing vector of \(m-1\) independent uniform observations on \((0,1)\); then \(Q\) is Greenwood's statistic. This is a concrete probability/statistics motivation for studying the paired observables. The same observables are Shannon entropy and Simpson concentration in finite-category diversity measurement. No assertion of universal finite-\(m\) correlation monotonicity in \(a\) is made.

## Proof

**1. Dirichlet moment differentiation.** For real exponents satisfying \(s_i>-a\),

\[
\mathbb E\!\left[\prod_{i=1}^{m}P_i^{s_i}\right]
=\frac{\Gamma(A)}{\Gamma(A+\sum_i s_i)}
\prod_{i=1}^{m}\frac{\Gamma(a+s_i)}{\Gamma(a)}.
\tag{1}
\]

All derivatives below are justified by dominated convergence in a neighborhood of the indicated positive exponents. In particular,

\[
\mathbb EH=\psi(A+1)-\psi(a+1),\qquad
\mathbb EQ=\frac{a+1}{A+1}.
\tag{2}
\]

Write \(d=\psi(A+1)-\psi(a+1)\). Differentiating the terms \(\mathbb E[P_i^3]\) and \(\mathbb E[P_i^2P_j]\) in their logarithmic exponents, separately for \(i=j\) and \(i\ne j\), gives

\[
\begin{aligned}
\mathbb E[HQ]
={a+1\over(A+1)(A+2)}\Big[ &(a+2)\{\psi(A+3)-\psi(a+3)\}\\
&+(m-1)a\{\psi(A+3)-\psi(a+1)\}\Big].
\end{aligned}
\tag{3}
\]

Using \(\psi(z+1)-\psi(z)=1/z\) twice in (3) and subtracting \(\mathbb EH\,\mathbb EQ\) from (2), all digamma terms cancel and the exact covariance becomes

\[
\operatorname{Cov}(H,Q)=-\frac{a(m-1)}{(A+1)^2(A+2)}.
\tag{4}
\]

This calculation is valid for every real \(a>0\), not just integral shape.

**2. Second moments.** The same moment identity differentiated twice at the powers \(P_i^2\) and \(P_iP_j\), with \(\psi_1(z+1)=\psi_1(z)-1/z^2\), yields

\[
\operatorname{Var}(H)
=\frac{a+1}{A+1}\psi_1(a+1)-\psi_1(A+1).
\tag{5}
\]

For \(Q\), expanding \(Q^2\) and applying (1) directly yields

\[
\mathbb E Q^2
=\frac{(a+1)\big[(a+2)(a+3)+(m-1)a(a+1)\big]}
{(A+1)(A+2)(A+3)}.
\]

Subtracting \((\mathbb EQ)^2\) gives the stated formula for \(\operatorname{Var}(Q)\). Both observables are nonconstant continuous functions on the positive-dimensional simplex for \(m\ge2\), so each variance is strictly positive. The correlation therefore exists and is negative.

**3. Gaussian scaling and the limiting correlation.** Let \(Y_1,\ldots,Y_m\) be independent \(\operatorname{Gamma}(a,1)\) variables. Normalize \(P_i=Y_i/\sum_jY_j\). Put \(B_m=m^{-1}\sum_iY_i\), \(C_m=m^{-1}\sum_iY_i\log Y_i\), and \(D_m=m^{-1}\sum_iY_i^2\). Then

\[
H=\log m+\log B_m-\frac{C_m}{B_m},\qquad
mQ=\frac{D_m}{B_m^2}.
\]

All polynomial-logarithmic gamma moments are finite; hence the multivariate iid central limit theorem applies to \((B_m,C_m,D_m)\). Its mean is \((a,a\psi(a+1),a(a+1))\). The delta method, using the gradients

\[
\nabla\!\left(\log B-C/B\right)
=\left(\frac{1+\psi(a+1)}a,-\frac1a,0\right),\qquad
\nabla\!\left(D/B^2\right)
=\left(-\frac{2(a+1)}{a^2},0,\frac1{a^2}\right),
\]

produces the stated centered bivariate Gaussian limit. To identify its covariance, one may use the exact moments (4)--(5) and the variance formula for \(Q\): multiplication by \(m\), \(m^2\), and \(m^3\), respectively, gives the limits

\[
\frac{(a+1)\psi_1(a+1)-1}{a},\quad
-\frac1{a^2},\quad
\frac{2(a+1)}{a^3}.
\]

Centering by the exact finite means changes neither gradients nor asymptotic covariance: Taylor remainders are of smaller order because the gamma sample means have all necessary finite moments. Division by the limiting standard deviations gives \(\rho(a)\) as claimed.

**4. Strict monotonicity.** Set \(x=a+1>1\), and write

\[
g(x):=x[x\psi_1(x)-1]=x^2\psi_1(x)-x.
\]

The trigamma integral, after changing variables \(u=xt\), gives the identity

\[
g(x)=\int_0^\infty u e^{-u}
\left(\frac1{1-e^{-u/x}}-\frac{x}{u}\right)\,du
=\int_0^\infty u e^{-u}f(u/x)\,du,
\]

where \(f(t)=(1-e^{-t})^{-1}-t^{-1}\) for \(t>0\). This function is **strictly increasing** because

\[
f'(t)=\frac1{t^2}-\frac{e^{-t}}{(1-e^{-t})^2}>0,
\]

by \(2\sinh(t/2)>t\) for all \(t>0\). Thus \(g(x)\) is strictly decreasing in \(x\). Moreover \(f(0+)=1/2\), \(0<f(t)<1\) for \(t>0\), so dominated convergence gives \(g(x)\to1/2\) as \(x\to\infty\). At \(x=1\), \(g(1)=\psi_1(1)-1=\pi^2/6-1\). Since \(\rho(a)=-[2g(a+1)]^{-1/2}\), it is strictly decreasing from its stated lower-concentration endpoint value to \(-1\).

**5. Sparse concentration and noncommuting limits.** For fixed \(m\ge2\), use the Taylor expansion

\[
\psi_1(1+t)=\frac{\pi^2}{6}-2\zeta(3)t+O(t^2)\qquad(t\to0).
\]

Equations (4)--(5) and the variance of \(Q\) then give

\[
\begin{aligned}
\operatorname{Cov}(H,Q)&=-\frac{m-1}{2}a+O_m(a^2),\\
\operatorname{Var}(Q)&=\frac{m-1}{3}a+O_m(a^2),\\
\operatorname{Var}(H)&=(m-1)\left(2\zeta(3)-\frac{\pi^2}{6}\right)a+O_m(a^2).
\end{aligned}
\]

Their ratio yields the fixed-\(m\) sparse-correlation constant, independent of \(m\). By contrast, taking \(m\to\infty\) first uses \(\rho(a)\), whose \(a\downarrow0\) endpoint was calculated in Step 4. The two constants differ, proving noncommutation.

## Verification

The standalone script `verify.py` uses SymPy to reduce to zero three independently constructed symbolic differences: the mixed covariance obtained by exponent differentiation, the entropy variance obtained by second derivatives, and the Simpson concentration variance obtained from fourth moments. It also conducts twelve seeded direct-Dirichlet Monte Carlo comparisons, with 300,000 vectors in each case; checks large-dimensional correlation limits for five positive shape parameters; and checks the fixed-dimensional sparse-limit constant for four dimensions. It was run successfully using Python with NumPy, SciPy, and SymPy. The random checks are non-certifying sanity checks; the proof above establishes the all-parameter formulas.

## Relationship to prior work

Royen (2010, arXiv:1008.4059) investigates the marginal distribution of the Dirichlet squared sum and its Greenwood-statistic specialization, including arbitrary gamma shape. Wolpert and Wolf (1994, arXiv:comp-gas/9403001) develop Dirichlet-based Shannon-entropy moments. Cerquetti (2014, arXiv:1404.3441) treats Shannon and Simpson indices as different members of a Tsallis-diversity family and supplies single-index moments for substantially broader random discrete distributions. These marginal theorems do not by themselves supply the cross-moment at **two different index orders**, nor the limiting-correlation monotonicity proved here.

The exact uniform-spacing covariance (the case \(a=1\)) has also been established separately and is **not asserted to be a new special case**. Likewise, analogous entropy–Gini–Simpson correlations for an infinite Poisson–Dirichlet partition are distinct from the fixed-positive-shape, increasing-dimension finite Dirichlet family here. The claim of distinct content is specifically the shape-parametrized dependence law together with the strict limiting-correlation transition and the noncommutation of concentration and dimension limits. The elementary moment-integration machinery is classical, and historical priority for equivalent mixed-moment formulas remains uncertain.

## Limitations

This is an exact finite-dimensional *prior/unconditional law* calculation, not a statement about estimated diversity from a finite ecological sample, posterior uncertainty after data, or arbitrary asymmetric Dirichlet weights. The Gaussian limit assumes \(a\) fixed and positive as \(m\to\infty\); it does not justify any simultaneous regime in which \(ma\) stays bounded. The strict monotonicity statement concerns **only the limiting correlation** \(\rho(a)\); finite-dimensional correlation need not be monotone in \(a\). Neither literature searches nor numerical checks certify absolute historical novelty, and an unindexed two-index covariance calculation might imply part of the theorem.

## References

- T. Royen, *The Distribution of the Square Sum of Dirichlet Random Variables and a Table with Quantiles of Greenwood's Statistic*, arXiv:1008.4059, first preprint 2010-08-24. https://arxiv.org/abs/1008.4059
- D. H. Wolpert and D. R. Wolf, *Estimating Functions of Probability Distributions from a Finite Set of Samples, Part I: Bayes Estimators and the Shannon Entropy*, arXiv:comp-gas/9403001, first preprint 1994-03-08. https://arxiv.org/abs/comp-gas/9403001
- D. R. Wolf and D. H. Wolpert, *Estimating Functions of Probability Distributions from a Finite Set of Samples, Part II: Bayes Estimators for Mutual Information, Chi-Squared, Covariance, and Other Statistics*, arXiv:comp-gas/9403002, first preprint 1994-03-08. https://arxiv.org/abs/comp-gas/9403002
- E. Archer, I. M. Park, and J. W. Pillow, *Bayesian Entropy Estimation for Countable Discrete Distributions*, arXiv:1302.0328, first preprint 2013-02-02. https://arxiv.org/abs/1302.0328
- A. Cerquetti, *Bayesian Nonparametric Estimation of Tsallis Diversity Indices under Gnedin–Pitman Priors*, arXiv:1404.3441, first preprint 2014-04-14. https://arxiv.org/abs/1404.3441
