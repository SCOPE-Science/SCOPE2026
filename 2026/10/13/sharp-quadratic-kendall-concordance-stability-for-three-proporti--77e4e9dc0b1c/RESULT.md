# Sharp quadratic Kendall concordance stability for three proportional-hazards failures

## Finding
For three independent continuous proportional-hazards lifetimes, let \(T_1\) and \(T_2\) be the first and second failure times. If the positive hazard multipliers are \(\lambda_1,\lambda_2,\lambda_3\), set \(p_i=\lambda_i/(\lambda_1+\lambda_2+\lambda_3)\) and \(V=\sum_{i=1}^3(p_i-1/3)^2\). Their population Kendall concordance obeys
\[
\tau(T_1,T_2)\le \frac25(1-V).
\]
Equality for positive multipliers occurs precisely at \(p_1=p_2=p_3=1/3\). The coefficient \(2/5\) of the quadratic heterogeneity penalty is optimal: for multipliers tending, after normalization, to \((0,1/2,1/2)\), the ratio \((2/5-\tau)/V\) tends to \(2/5\). Thus the inequality is strictly stronger than the homogeneous concordance ceiling whenever the multipliers are unequal.

## Assumptions and scope
Let \(H:[0,\infty)\to[0,\infty)\) be continuous and strictly increasing, with \(H(0)=0\) and \(H(t)\to\infty\). Independently for \(i=1,2,3\), assume \(\Pr\{X_i>t\}=\exp[-\lambda_iH(t)]\) for all \(t\ge0\), where every \(\lambda_i>0\). Let \(T_1=X_{1:3}\), \(T_2=X_{2:3}\). Kendall's population tau is \(\Pr\{(T_1-T'_1)(T_2-T'_2)>0\}-\Pr\{(T_1-T'_1)(T_2-T'_2)<0\}\) for an independent copy. No censoring or ties arise under these conditions.

## Proof
**1. Transform and decompose the first two failures.** The order-preserving transformation \(Y_i=H(X_i)\) makes independent exponentials with rates \(\lambda_i\); Kendall's tau is unchanged under this common increasing transformation. Rescale time to make \(\sum_i\lambda_i=1\). For the first exponential arrival \(L=Y_{1:3}\), the exponential-race identity gives \(L\sim\mathrm{Exp}(1)\) independent of the winning index \(I\), with \(\Pr\{I=i\}=p_i\). The next gap \(R=Y_{2:3}-Y_{1:3}\) is therefore independent of \(L\), and, conditional on \(I=i\), has distribution \(\mathrm{Exp}(q_i)\), where \(q_i=1-p_i>0\).

**2. An exact concordance formula.** For independent copies \((L,R)\), \((L',R')\), their first-arrival difference \(W=L-L'\) has symmetric double-exponential density \(\frac12e^{-|d|}\). Conditioning on \(A=R-R'\) and integrating this density shows
\[
\mathbb E[\operatorname{sgn}(W)\operatorname{sgn}(W+A)\mid A]=e^{-|A|}.
\]
Thus \(\tau(T_1,T_2)=\mathbb E[e^{-|R-R'|}]\). If \(E_u,E_v\) are independent exponentials of positive rates \(u,v\), direct integration of their difference density gives
\[
\mathbb E[e^{-|E_u-E_v|}]
=\frac{uv}{u+v}\left(\frac1{1+u}+\frac1{1+v}\right).
\]
Consequently the exact finite formula is
\[
\tau(T_1,T_2)=\sum_{i,j=1}^3
\frac{p_i p_jq_iq_j}{q_i+q_j}
\left(\frac1{1+q_i}+\frac1{1+q_j}\right).
\]

**3. Exact nonnegative-polynomial certificate.** Because the formula and penalty are permutation-invariant, sort the probabilities increasingly and write
\[
(p_1,p_2,p_3)=\frac{(a,a+b,a+b+c)}{S},\qquad S=3a+2b+c,
\]
with \(a>0\), \(b,c\ge0\). Put \(G=\frac25(1-V)-\tau(T_1,T_2)\). Straight rational simplification yields \(D G=P(a,b,c)\), with
\[
\begin{aligned}
D={}&15S^2(4a+2b+c)(4a+3b+c)(4a+3b+2c)\\
&\quad\cdot(5a+3b+c)(5a+3b+2c)(5a+4b+2c).
\end{aligned}
\]
The numerator \(P\) is a homogeneous degree-eight polynomial with exactly 40 nonzero monomials, *all with positive integer coefficients*. The least coefficient is \(16\), the greatest is \(183048\), their sum is \(1743120\), and in particular \(P\) contains \(9760a^6b^2+9760a^6c^2\). The attached `verify_tau.py` reconstructs \(G\), multiplies by the displayed \(D\), symbolically confirms polynomiality, and checks every one of the 40 exact integer coefficients. This is a finite exact algebraic positivity certificate valid for all real parameters, not a grid test. Since \(D>0\), one has \(G\ge0\), strictly if \(b>0\) or \(c>0\). Conversely \(b=c=0\) is the equal-hazard case and has \(G=0\).

**4. Optimality of the penalty coefficient.** By the exact concordance formula, at the closed-simplex limit \((p_1,p_2,p_3)=(0,1/2,1/2)\), tau equals \(1/3\) and \(V=1/6\). Therefore \((2/5-\tau)/V=(2/5-1/3)/(1/6)=2/5\). Approaching this boundary with strictly positive multipliers proves that replacing \(2/5\) in front of \(V\) by any larger constant makes the asserted inequality false for some admissible model. The boundary itself is a limiting configuration, not an additional admissible equality case.

## Verification
Execute `python verify_tau.py` from the extracted package directory with Python 3.10+ and SymPy 1.12+. It verifies the rational identity, homogeneous polynomial degree, all 40 strictly positive coefficients, zero and positive equality cases, and exact homogeneous and boundary values. The reported coefficient sum is \(1743120\). All proof statements concern an uncountable continuous parameter domain and rest on the displayed rational identity and positivity, not numerical sampling.

## Relationship to prior work
Kochar, *Dependence comparisons of order statistics in the proportional hazards model*, arXiv:2202.07874 (first public version 2022-02-16), Theorems 3.2–3.3, compares the dependence of heterogeneous and homogeneous order statistics by stronger stochastic-increasing order and consequently implies the **unpenalized** concordance bound \(\tau(T_1,T_2)\le2/5\). That result does not provide a rate-dispersion penalty or its best coefficient. Avérous, Genest and Kochar (2005) obtain explicit homogeneous-sample Kendall tau values; their formula supplies the equal-hazard endpoint but no heterogeneous stability constant. Kochar and Spizzichino (2023) study dependence from time-transformed exponential models with exchangeable parental dependence, not this independent three-rate comparison. The published heterogeneous **minimum–maximum** comparison of Genest, Kochar and Xu (2009) concerns a different pair of order statistics and does not yield the adjacent first–second inequality.

## Limitations
The sharp penalty is established for precisely three independent lifetimes with a **common** proportional-hazards baseline. It does not automatically extend to four or more components, different nonproportional baselines, censoring, or dependent lifetimes. It bounds population tau rather than providing a sampling distribution or a confidence procedure. The coefficient is optimal in the limiting sense; no strictly positive unequal hazard triple attains equality. An independent audit and exhaustive bibliographic priority confirmation have not been performed.

## References
1. S. Kochar (2022), *Dependence comparisons of order statistics in the proportional hazards model*, arXiv:2202.07874; *Probability in the Engineering and Informational Sciences*, doi:10.1017/S0269964822000146. First public manuscript dated 2022-02-16.
2. J. Avérous, C. Genest and S. C. Kochar (2005), *On the dependence structure of order statistics*, *Journal of Multivariate Analysis* 94, 159–171, doi:10.1016/j.jmva.2004.03.004.
3. S. Kochar and F. Spizzichino (2023), *Dependence among order statistics for time-transformed exponential models*, doi:10.1017/S0269964823000190.
4. C. Genest, S. Kochar and M. Xu (2009), *On the range of heterogeneous samples*, *Journal of Multivariate Analysis* 100, 1587–1592.
5. J.-A. Espín-Sánchez and T. Wu (2022), *Order Statistics from Independent Non-Identical Exponentiated and Proportional Hazard Rate Random Variables*, Cowles Foundation Discussion Paper 2346 (order-statistic marginal formulas).
