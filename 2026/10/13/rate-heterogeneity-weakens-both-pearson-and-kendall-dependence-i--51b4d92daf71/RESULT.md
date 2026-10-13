# Rate heterogeneity weakens both Pearson and Kendall dependence in exponential load sharing
## Finding
Consider a two-component load-sharing parallel system whose full-load component lifetimes satisfy \(X_i\sim\operatorname{Exp}(\lambda_i)\) independently, with \(\lambda_i>0\). While both components are alive, component \(i\) has hazard \(c\lambda_i\), where the common decelerating factor satisfies \(0<c<1\); after the other component fails, its hazard becomes \(\lambda_i\). Let \(T_i\) denote the ultimate lifetime of component \(i\), and put \(r=\lambda_2/\lambda_1\).

Then the Pearson correlation is
\[
\rho_P(r,c)=\frac{1-c^2}{\sqrt{[1+c^2(r^2+2r)][1+c^2(r^{-2}+2r^{-1})]}}.
\]
The covariance itself is
\[
\operatorname{Cov}(T_1,T_2)=\frac{1-c^2}{c^2(\lambda_1+\lambda_2)^2}.
\]
For each fixed \(c\), the Pearson correlation is a strictly decreasing function of the heterogeneity index \(r+r^{-1}\). Consequently
\[
0<\rho_P(r,c)\le \frac{1-c^2}{1+3c^2},
\]
with equality exactly when \(\lambda_1=\lambda_2\), and \(\rho_P(r,c)\to0\) as \(r\to0\) or \(r\to\infty\).

Li and Li give the heterogeneous-rate Kendall coefficient
\[
\tau(\lambda_1,\lambda_2,c)=
\frac{\lambda_1\lambda_2(1-c)(1+2c)}{[(c+1)\lambda_1+c\lambda_2][c\lambda_1+(c+1)\lambda_2]}.
\]
After division by \(\lambda_1\lambda_2\), its denominator is
\[
c(c+1)(r+r^{-1})+2c^2+2c+1.
\]
Thus Kendall dependence has the same heterogeneity monotonicity:
\[
0<\tau(\lambda_1,\lambda_2,c)\le\frac{1-c}{1+2c},
\]
again with equality exactly at equal rates and convergence to zero under extreme rate imbalance. Hence the source sentence identifying equal rates as the *minimum* Kendall dependence reverses the extremum: equal rates give the unique maximum.

## Assumptions and scope
The claim is restricted to the two-component exponential model with a common decelerating factor \(c\in(0,1)\). This is exactly the heterogeneous exponential setting of Li and Li's Theorem 4.4 and equation (A.14). Exponential lack of memory removes the virtual-age function from the calculation. The statement concerns Pearson correlation and the source's explicit Kendall coefficient; it does not claim an analogous extremum for every dependence functional or for unequal decelerating factors.

## Proof
Let \(S\) be the time to the first component failure. While both components are alive, the competing hazards are \(c\lambda_1\) and \(c\lambda_2\), so
\[
S\sim\operatorname{Exp}(c(\lambda_1+\lambda_2)).
\]
Let \(I\in\{1,2\}\) denote the component that fails first. Standard competing-exponential factorization gives
\[
\Pr(I=1)=\frac{\lambda_1}{\lambda_1+\lambda_2},\qquad
\Pr(I=2)=\frac{\lambda_2}{\lambda_1+\lambda_2},
\]
and \(S\) is independent of \(I\). By lack of memory, if component \(j\) survives the first failure, its additional full-load lifetime \(E_j\) is independent exponential with rate \(\lambda_j\). Therefore
\[
T_1=S+\mathbf 1_{\{I=2\}}E_1,\qquad
T_2=S+\mathbf 1_{\{I=1\}}E_2.
\]
The two add-on terms never occur simultaneously. Put \(L=\lambda_1+\lambda_2\). Since \(\operatorname{Var}S=1/(c^2L^2)\),
\[
\operatorname{Cov}(T_1,T_2)
=\frac1{c^2L^2}-
\left(\frac{\lambda_2}{L\lambda_1}\right)
\left(\frac{\lambda_1}{L\lambda_2}\right)
=\frac{1-c^2}{c^2L^2}.
\]
Using \(\mathbb E[E_j]=1/\lambda_j\) and \(\mathbb E[E_j^2]=2/\lambda_j^2\) gives
\[
\operatorname{Var}(T_1)=
\frac{1+c^2(r^2+2r)}{c^2L^2},\qquad
\operatorname{Var}(T_2)=
\frac{1+c^2(r^{-2}+2r^{-1})}{c^2L^2}.
\]
Dividing the covariance by the geometric mean of these variances proves the Pearson formula.

For the extremum, set \(s=r+r^{-1}\ge2\). The square of the Pearson denominator equals
\[
1+c^2(s^2+2s-2)+c^4(5+2s).
\]
Its derivative with respect to \(s\) is \(2c^2(s+1+c^2)>0\). Hence Pearson correlation decreases strictly with \(s\), so its unique maximum occurs at \(s=2\), equivalently \(r=1\). The endpoint limit follows directly from the formula.

For Kendall's coefficient, Li and Li's displayed formula reduces after division by \(\lambda_1\lambda_2\) to
\[
\tau=\frac{(1-c)(1+2c)}{c(c+1)s+2c^2+2c+1}.
\]
The numerator is positive and the denominator is strictly increasing in \(s\), proving the same unique maximizer. At \(s=2\), the denominator is \((1+2c)^2\), yielding \(\tau=(1-c)/(1+2c)\). This also shows directly why a Schur-convex denominator implies a maximum, not a minimum, for its reciprocal.

## Verification
The derivation uses only competing-exponential factorization, exponential first and second moments, and algebra. Three boundary checks agree with the model: when \(r=1\), the Pearson formula reduces exactly to Li and Li's Proposition 4.2, \(\rho_P=(1-c^2)/(1+3c^2)\); as \(c\uparrow1\), both correlations tend to zero, consistent with disappearance of the load-sharing perturbation; and as \(c\downarrow0\), both tend to one for fixed positive rates because the common first-failure waiting time dominates.

No finite experiment is used as proof. The covariance, variance, and monotonicity calculations were independently re-expanded symbolically during verification.

## Relationship to prior work
Li and Li prove positive dependence and TP2 for the heterogeneous exponential model. Their Proposition 4.2 computes Pearson correlation only for the equal-rate case, while Section 5.1 gives a heterogeneous-rate Kendall formula. The Pearson expression above extends their equal-rate calculation to the full heterogeneous model. Their printed Kendall formula itself implies that equal rates maximize dependence, whereas the accompanying prose says the model achieves its minimum dependence there; the displayed formula and the monotonicity calculation above show that the prose reverses the extremum.

Bassan and Spizzichino's 1999 full text was inspected because Li and Li identify it as the principal predecessor for the common-exponential Ross load-sharing model. Its Example 4.5 treats the equal-rate Ross model and TP2/ageing comparisons, but does not give the heterogeneous Pearson formula or a rate-heterogeneity dependence extremum.

## Limitations
The result does not address more than two components, nonexponential baselines, unequal decelerating factors, or arbitrary virtual-age transformations. Pearson and Kendall correlation summarize different aspects of dependence; their agreement on the rate-heterogeneity maximizer here does not by itself imply monotonicity for every concordance measure. Searches did not reveal an earlier statement of the heterogeneous Pearson formula, but absence from the searched sources is not a proof of global novelty.

## References
1. C. Li and X. Li, “Quantifying stochastic dependence of marginal lifetimes of two-component load-sharing parallel systems,” *Probability in the Engineering and Informational Sciences* (2026). DOI: 10.1017/S0269964825100168. First published online 13 January 2026.
2. B. Bassan and F. Spizzichino, “Stochastic comparisons for residual lifetimes and Bayesian notions of multivariate ageing,” *Advances in Applied Probability* 31 (1999), 1078–1094. DOI: 10.1239/aap/1029955261.
