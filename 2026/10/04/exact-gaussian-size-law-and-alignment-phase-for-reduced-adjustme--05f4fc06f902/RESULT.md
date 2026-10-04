# Exact Gaussian size law and alignment phase for reduced-adjustment Maxway CRT
## Finding
Let \((X_i,Y_i,Z_i)\), \(i=1,\ldots,n\), be independent copies of a jointly Gaussian vector satisfying the full conditional-independence null through
\[
X=\beta^\top Z+\varepsilon_x,\qquad Y=\theta^\top Z+\varepsilon_y,
\]
where \(Z\sim N(0,\Sigma)\), \(\varepsilon_x\sim N(0,\tau_x^2)\), \(\varepsilon_y\sim N(0,\tau_y^2)\), \(\tau_x,\tau_y>0\), and the noises and \(Z\) are mutually independent. Let \(S=A^\top Z\), with \(A^\top\Sigma A\) nonsingular, and define
\[
R_x=X-\mathbb E[X\mid S],\qquad R_y=Y-\mathbb E[Y\mid S].
\]
Write their variances as \(\sigma_x^2,\sigma_y^2\) and their correlation as \(\rho\in(-1,1)\).

Run the ideal Maxway randomization from the exact reduced law \(X\mid S\) and use
\[
T=\left|\sum_{i=1}^nR_{x,i}R_{y,i}\right|.
\]
Then
\[
p_\infty=2\{1-\Phi(|W_n|)\},\qquad
W_n=\frac{\sum_iR_{x,i}R_{y,i}}{\sigma_x\sqrt{\sum_iR_{y,i}^2}},
\]
and exactly
\[
W_n\overset d=\rho Q_n+\sqrt{1-\rho^2}\,G,
\qquad Q_n\sim\chi_n,\quad G\sim N(0,1),\quad Q_n\perp G.
\]
Thus, with \(z=z_{1-\alpha/2}\), the exact rejection probability is
\[
\alpha_n(\rho)=\mathbb E\!\left[
\bar\Phi\!\left(\frac{z-\rho Q_n}{\sqrt{1-\rho^2}}\right)+
\bar\Phi\!\left(\frac{z+\rho Q_n}{\sqrt{1-\rho^2}}\right)
\right].
\]
For \(\sqrt n\,\rho_n\to\kappa\in\mathbb R\),
\[
\alpha_n(\rho_n)\to\bar\Phi(z-\kappa)+\bar\Phi(z+\kappa).
\]
Hence \(\sqrt n|\rho_n|\to0\) gives asymptotically nominal size, any finite nonzero local limit gives strict inflation, and \(\sqrt n|\rho_n|\to\infty\) gives rejection probability tending to one.

Let
\[
\Sigma_\perp=\operatorname{Cov}(Z\mid S)=\Sigma-\Sigma A(A^\top\Sigma A)^{-1}A^\top\Sigma,
\]
\[
\Delta_x^2=\beta^\top\Sigma_\perp\beta,\qquad
\Delta_y^2=\theta^\top\Sigma_\perp\theta.
\]
Then
\[
\rho=\frac{\beta^\top\Sigma_\perp\theta}{\sigma_x\sigma_y}
=\frac{\gamma\Delta_x\Delta_y}{\sigma_x\sigma_y},\qquad |\gamma|\le1.
\]
Thus orthogonal omitted directions give \(\rho=0\) and exact nominal ideal-CRT size even if both omissions are nonzero, while collinear omitted directions attain the product-error order.

At \(\alpha=0.05\), \(n=100\), and \(\rho=0.1\), the exact size is \(0.168815564178\); the \(\kappa=1\) limit is \(0.170075045753\).

## Assumptions and scope
The result concerns scalar \(X\) and \(Y\), iid jointly Gaussian data, positive noise variances, a fixed linear reduction, exact reduced conditional means, the exact reduced conditional law \(X\mid S\), and the ideal infinite-randomization p-value. The scientific null is \(X\perp Y\mid Z\); the reduction \(S\) need not preserve that null. The theorem quantifies the resulting type-I distortion.

The statistic is the Maxway \(d_0\) form with residualizing functions chosen as the exact reduced means \(\mathbb E[X\mid S]\) and \(\mathbb E[Y\mid S]\).

## Proof
Joint Gaussianity makes \((R_x,R_y)\) jointly Gaussian and independent of \(S\). With \(U=R_y/\sigma_y\), write
\[
R_x/\sigma_x=\rho U+\sqrt{1-\rho^2}\,E,
\]
where \(E\sim N(0,1)\) is independent of \(U\). Across observations,
\[
W_n=\rho\|U\|+\sqrt{1-\rho^2}\frac{E^\top U}{\|U\|}.
\]
Now \(\|U\|\sim\chi_n\), and conditional on \(U\), the normalized projection \(E^\top U/\|U\|\) is standard normal with a conditional law not depending on \(U\), hence is independent of \(\|U\|\). This proves the distributional representation.

For a resample, \(R_x'\mid S\sim N(0,\sigma_x^2)\) independently of observed \(R_y\). Therefore its normalized inner product with \(R_y\) is conditionally standard normal, giving \(p_\infty=2\{1-\Phi(|W_n|)\}\). Conditioning on \(Q_n\) yields the exact size integral.

If \(\sqrt n\rho_n\to\kappa\), then \(Q_n/\sqrt n\to1\) in probability and \(\sqrt{1-\rho_n^2}\to1\), so Slutsky gives \(W_n\Rightarrow N(\kappa,1)\). If \(\sqrt n|\rho_n|\to\infty\), the conditional mean magnitude \(|\rho_n|Q_n\) diverges while the conditional standard deviation is at most one, hence \(|W_n|\to\infty\) in probability. Strict inflation for finite \(\kappa\ne0\) follows because for \(\kappa>0\),
\[
\frac{d}{d\kappa}\{\bar\Phi(z-\kappa)+\bar\Phi(z+\kappa)\}=\phi(z-\kappa)-\phi(z+\kappa)>0.
\]

Finally, Gaussian conditioning gives covariance \(\Sigma_\perp\) for \(Z-\mathbb E[Z\mid S]\). Substituting this residual into the two linear models gives the stated residual variances and covariance; Cauchy--Schwarz gives \(|\gamma|\le1\).

## Verification
`verify.py` evaluates the exact integral, reproduces the two reported constants, checks the \(n=1\) boundary numerically, and verifies the omitted-direction covariance identities on a positive-definite example. Numerical checks support constants and algebra; the infinite-family result is proved above.

## Relationship to prior work
Li and Liu introduce Maxway CRT, define the reduced-function randomization framework and the \(d_0\) statistic, and prove finite-sample upper bounds on type-I inflation. Their Gaussian linear analysis exhibits a \(\sqrt n\) product-of-mean-errors rate, but the inspected theorem statements do not give this chi-normal finite-sample size law, the exact rejection integral, or the alignment-cosine refinement.

Niu, Chakraborty, Dukes, and Katsevich prove asymptotic double robustness of dCRT and asymptotic equivalence with the generalized covariance measure. Their finite-sample section is simulation-based. Generic Wishart/Bartlett theory contains related Gaussian covariance decompositions, so the chi-normal representation itself is not claimed as a new distributional identity. The contribution is its exact implication for reduced-adjustment Maxway validity and the alignment-sensitive sharp boundary.

## Limitations
No claim is made for finite Monte Carlo budgets, learned reduced laws, estimated residual means, non-Gaussian distributions, vector-valued variables, or nonlinear reductions. Older Gaussian sample-covariance literature may encode the same probabilistic decomposition under other notation. Targeted searches found no prior statement applying it to this Maxway validity problem, but search failure is not a uniqueness proof.

## References
1. Shuangning Li and Molei Liu, “Maxway CRT: Improving the Robustness of the Model-X Inference,” arXiv:2203.06496, first public 2022-03-12; Journal of the Royal Statistical Society Series B 85(5), 2023, doi:10.1093/jrsssb/qkad081.
2. Ziang Niu, Abhinav Chakraborty, Oliver Dukes, and Eugene Katsevich, “Reconciling model-X and doubly robust approaches to conditional independence testing,” arXiv:2211.14698, first public 2022-11-27; Annals of Statistics 52(3), 2024, doi:10.1214/24-AOS2372.
