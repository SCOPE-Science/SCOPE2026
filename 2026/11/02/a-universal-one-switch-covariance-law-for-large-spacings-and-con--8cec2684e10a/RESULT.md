# A universal one-switch covariance law for large spacings and convex spacing tests

## Finding
Let \(m\ge2\) and let \(X=(X_1,\ldots,X_m)\) be uniform on the \((m-1)\)-dimensional probability simplex, equivalently the \(m\) gaps cut out by \(m-1\) independent uniform observations on \([0,1]\). For \(0<t<1\), define the count of unusually large gaps and an additive statistic by
\[
K_t=\sum_{i=1}^{m}{\bf1}_{\{X_i>t\}},\qquad F_f=\sum_{i=1}^{m}f(X_i).
\]
For **every** continuously differentiable, strictly convex real function \(f\) on \([0,1]\), there exists exactly one \(t_*=t_*(m,f)\) in \((0,1)\) such that
\[
\operatorname{Cov}(K_t,F_f)\begin{cases}<0,&0<t<t_*,\\=0,&t=t_*,\\>0,&t_*<t<1.\end{cases}
\]
For Greenwood's quadratic spacing statistic \(Q=\sum_iX_i^2\), this location is **exactly** \(t_*=2/(m+2)\), and
\[
\boxed{\operatorname{Cov}(K_t,Q)=\frac{m-1}{m+1}\,t(1-t)^{m-1}\big((m+2)t-2\big).}
\]
At the natural large-spacing scale \(t=c/m\), for every fixed \(c>0\),
\[
\boxed{\lim_{m\to\infty}\operatorname{Corr}(K_{c/m},Q)
=\frac{c(c-2)}{2\sqrt{e^c-1-c^2}}.}
\]
Thus the asymptotic correlation is strictly negative for \(0<c<2\), vanishes at \(c=2\), and is strictly positive for \(c>2\). This is a covariance statement, not independence at the zero-covariance threshold.

## Assumptions and scope
The dimension is any integer \(m\ge2\). The simplex distribution has constant density, i.e. Dirichlet parameters all equal to one. Every assertion about the universal sign switch assumes \(f\in C^1([0,1])\) and strict convexity, with no monotonicity requirement. The threshold \(t\) is strictly between zero and one. The asymptotic formula takes fixed \(c>0\), then \(m\to\infty\) along integers satisfying \(c/m<1\). No claim is made for nonsymmetric simplex distributions or arbitrary Schur-convex functions outside the separable class.

## Proof
Let \(Y\) be an independent uniform simplex vector, and write
\[
\Phi_f(t)=\mathbb E\left[f\big(t+(1-t)Y_1\big)+\sum_{j=2}^mf\big((1-t)Y_j\big)\right].
\]
The simplex-slice identity is \(\Pr(X_1>t)=(1-t)^{m-1}\). The conditional law of \(X\) given \(X_1>t\) is exactly \(t e_1+(1-t)Y\). Exchangeability therefore proves the **exact identity**
\[
\operatorname{Cov}(K_t,F_f)=m(1-t)^{m-1}\big(\Phi_f(t)-\Phi_f(0)\big).\tag{1}
\]
For almost every interior simplex vector \(Y\), each coordinate of \(t e_1+(1-t)Y\) is affine and at least one has nonzero slope. Strict convexity of \(f\) makes the sum strictly convex along this line; averaging proves strict convexity of \(\Phi_f\) on \([0,1]\). Differentiating under the expectation is justified by the bounded derivative of \(f\), and exchangeability gives
\[
\Phi_f'(0)=\mathbb E[f'(Y_1)]-m\mathbb E[Y_1f'(Y_1)]
=-m\operatorname{Cov}(Y_1,f'(Y_1))<0.\tag{2}
\]
The strict inequality holds because \(Y_1\sim\operatorname{Beta}(1,m-1)\) is nondegenerate and \(f'\) is strictly increasing; the independent-copy identity \(2\operatorname{Cov}(U,g(U))=\mathbb E[(U-U')(g(U)-g(U'))]\) makes strict positivity immediate. On the other hand, the strict chord inequality \(f(u)<(1-u)f(0)+uf(1)\) for \(0<u<1\) yields
\[
\Phi_f(1)=f(1)+(m-1)f(0)>\mathbb E\sum_i f(Y_i)=\Phi_f(0).\tag{3}
\]
A strictly convex function starting with negative right derivative and ending above its initial value crosses its initial level at precisely one positive interior point. Combining this with (1) proves the universal sign law, including strictness in both open regimes.

For \(f(u)=u^2\), the elementary moments \(\mathbb EY_i=1/m\) and \(\mathbb EY_i^2=2/[m(m+1)]\) give
\[
\Phi_f(t)=t^2+\frac{2t(1-t)}m+\frac{2(1-t)^2}{m+1},
\qquad
\Phi_f(t)-\Phi_f(0)=\frac{m-1}{m(m+1)}t\big((m+2)t-2\big).
\]
Substitution into (1) establishes the stated quadratic identity and its sharp threshold.

For the limit, denote \(p_t=(1-t)^{m-1}\) and \(q_t=(1-2t)_+^{m-1}\). Direct two-coordinate simplex volumes give
\[
\operatorname{Var}(K_t)=m p_t(1-p_t)+m(m-1)(q_t-p_t^2),\tag{4}
\]
while fourth-order Dirichlet moments give
\[
\operatorname{Var}(Q)=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)}.\tag{5}
\]
For fixed \(c>0\), put \(t=c/m\). Expanding logarithms through order \(1/m\) gives
\[
\frac1m\operatorname{Var}(K_{c/m})\to e^{-c}-(1+c^2)e^{-2c},\qquad
m^3\operatorname{Var}(Q)\to4,\qquad
m\operatorname{Cov}(K_{c/m},Q)\to c(c-2)e^{-c}.
\]
The limiting variance coefficient is positive: \(e^c>1+c^2\) for \(c>0\), e.g. by its Taylor series and the positive quadratic \(1-c/2+c^2/6\). Taking ratios completes the correlation formula.

## Verification
The accompanying standalone `verify_spacing.py` uses exact rational arithmetic to compare (1) with an **independent beta-density integration** of \(\mathbb E[{\bf1}_{\{X_1>t\}}X_1^r]\) and \(\mathbb E[{\bf1}_{\{X_1>t\}}X_2^r]\), for dimensions \(2\) through \(13\), rational thresholds \(j/16\) with \(1\le j\le15\), and monomials of degrees \(2\) through \(6\). It checks the exact quadratic covariance, the sign switch, both variance formulas and large-dimension asymptotic correlations; it passes 1,459 assertions. The sole zero variance of \(K_t\) on that grid occurs at \(m=2,t=1/2\), where \(K_t\) is constant; the covariance theorem nevertheless applies. These finite checks do not replace the proof for all dimensions and all strictly convex functions.

## Relationship to prior work
Jammalamadaka and Wells (1988) establish the null distribution and asymptotic efficiency of counts of small and large spacings, and give a limiting Gaussian covariance kernel for the spacing empirical process. Their Theorems 2.1 and 3.1–3.2 and Section 4 do not give the exact **mixed finite-sample covariance** between a threshold count and a convex additive spacing functional, nor its unique sign crossing. Ghosh and Jammalamadaka (1998) study marginal Greenwood/Rao/log spacing statistics and their approximations, not this mixed finite-sample law. Holst (1980) studies stick-breaking and extreme spacings; L'Ecuyer (1997) studies marginal sum-function tests. Nagaraja, Bharath and Zhang (2014 first public release) analyze spacings neighboring an order statistic, rather than a global exceedance count combined with an additive convex cost. A limiting covariance can sometimes be obtained by combining older empirical-process theory with additional work; the claim of novelty rests principally on the exact all-dimension, all-\(f\) one-switch theorem, not on an independently new central-limit theorem.

## Limitations
No independence at the zero covariance point is asserted. The root for general \(f\) is implicitly characterized and generally not explicit. The theorem requires uniform Dirichlet spacings and strictly convex differentiable additive costs. The correlation limit alone is not asserted to supply a joint central limit theorem or test-power guarantee. Despite the primary sources inspected, an equivalent theorem may exist elsewhere in older spacings/majorization literature; historical priority is not certified. One cited 2014 item was available only as its first published page. The stronger 1988 primary paper was read in its complete 10-page scientific text.

## References
1. S. R. Jammalamadaka and M. T. Wells, *A Test of Goodness-of-Fit Based on Extreme Spacings with Some Efficiency Comparisons*, Metrika 35 (1988), 223–232, https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/1988_ExtremeSpacings-Metrika.pdf; doi:10.1007/BF02613309.
2. K. Ghosh and S. R. Jammalamadaka, *Small Sample Approximations for Spacing Statistics*, Journal of Statistical Planning and Inference 69 (1998), 245–261, https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/1998_SmallSample%20AppoxSpacings_JSPI.pdf; doi:10.1016/S0378-3758(97)00164-X.
3. L. Holst, *On the Lengths of the Pieces of a Stick Broken at Random*, Journal of Applied Probability 17 (1980), 623–634, https://imprs-lectures.aei.mpg.de/wp-content/uploads/2023/12/Holst_StickBreakingDistributions.pdf.
4. H. N. Nagaraja, K. Bharath, and F. Zhang, *Spacings around an Order Statistic*, Annals of the Institute of Statistical Mathematics 67 (2015), 515–540, first publicly online 26 April 2014, https://www.ism.ac.jp/editsec/aism/67/0515.pdf; doi:10.1007/s10463-014-0466-9.
5. P. L'Ecuyer, *Tests Based on Sum-Functions of Spacings for Uniform Random Numbers*, Communications in Statistics—Simulation and Computation 26 (1997), 773–796; doi:10.1080/00949659708811859.
