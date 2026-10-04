# Exact perturbation-angle law and finite-dimensional positive-sign tax for OLS Gaussian mirrors
## Finding
For the low-dimensional OLS Gaussian-mirror construction, the published normalization fixes the residual perturbation norm but leaves a random residual angle. That angle has an exact and monotone effect on the mirror statistic.

Let \(j\) be a feature and define
\[
P=I-X_{-j}(X_{-j}^{\mathsf T}X_{-j})^{-1}X_{-j}^{\mathsf T},\qquad a=Px_j,\qquad r=\lVert a\rVert>0.
\]
For the published choice \(c_j=r/\lVert Pz_j\rVert\), put \(b=c_jPz_j\) and
\[
\rho=\frac{a^{\mathsf T}b}{r^2}.
\]
Then \(\lVert a\rVert=\lVert b\rVert=r\), and the residualized mirror columns \(a+b\) and \(a-b\) are orthogonal. Conditional on \(X\) and \(z_j\),
\[
\hat\beta_j^+\sim N\!\left(\frac{\beta_j}{2},\frac{\sigma^2}{2r^2(1+\rho)}\right),\qquad
\hat\beta_j^-\sim N\!\left(\frac{\beta_j}{2},\frac{\sigma^2}{2r^2(1-\rho)}\right),
\]
and the two coefficients are independent.

For every real \(u,v\),
\[
|u+v|-|u-v|=2\,\operatorname{sgn}(uv)\min(|u|,|v|).
\]
Thus, outside a null event, the sign of the published mirror statistic \(M_j\) is the sign of \(\hat\beta_j^+\hat\beta_j^-\). If \(\beta_j\ne0\) and
\[
\lambda=\frac{|\beta_j|r}{\sqrt2\sigma},
\]
then
\[
\Pr(M_j>0\mid X,z_j)=F_\lambda(\rho),
\]
where
\[
F_\lambda(\rho)=
\Phi(\lambda\sqrt{1+\rho})\Phi(\lambda\sqrt{1-\rho})
+
\Phi(-\lambda\sqrt{1+\rho})\Phi(-\lambda\sqrt{1-\rho}).
\]
The function \(F_\lambda\) is even and strictly decreasing in \(|\rho|\) for \(0<|\rho|<1\). Hence the residual-orthogonal benchmark \(\rho=0\) uniquely maximizes the probability that a true signal has positive mirror sign. Since every selection event \(M_j\ge t\) with \(t>0\) requires \(M_j>0\), this gives an exact featurewise gate on achievable selection probability.

Under the actual Gaussian perturbation, the residual-space dimension is
\[
d=\operatorname{rank}(P)=n-p+1\ge2.
\]
The random direction \(Pz_j/\lVert Pz_j\rVert\) is uniform on the unit sphere of that residual space, so \(\rho\) has density
\[
f_d(u)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}(1-u^2)^{(d-3)/2},\qquad -1<u<1.
\]
Consequently the exact design-conditional positive-sign probability is
\[
\Pi_d(\lambda)=\int_{-1}^{1}F_\lambda(u)f_d(u)\,du,
\]
and \(\Pi_d(\lambda)<F_\lambda(0)\) for every finite \(d\ge2\) and \(\lambda>0\). For fixed \(\lambda\),
\[
\Pi_d(\lambda)=F_\lambda(0)-\frac{A(\lambda)}{d}+O_\lambda(d^{-2}),
\]
with
\[
A(\lambda)=
\frac{[2\Phi(\lambda)-1]\lambda(\lambda^2+1)\phi(\lambda)}{4}
+
\frac{\lambda^2\phi(\lambda)^2}{2}>0.
\]
At \(\lambda=1\), the orthogonal benchmark is \(F_1(0)=0.733032471337196\), while the published Gaussian-direction mixture gives \(\Pi_3(1)=0.683939720585721\) and \(\Pi_{10}(1)=0.720864540388746\). At \(\lambda=2\), \(F_2(0)=0.955534873110961\) but \(\Pi_3(2)=0.877289454861085\). These losses are largest when \(p\) is close to \(n\), precisely where the residual dimension \(d=n-p+1\) is small.

There is also an exact null magnitude law. If \(\beta_j=0\), then for \(t\ge0\), writing \(x=tr/(\sqrt2\sigma)\),
\[
\Pr(M_j\ge t\mid X,z_j)
=2\,\bar\Phi(x\sqrt{1+\rho})\bar\Phi(x\sqrt{1-\rho}).
\]
Thus null sign symmetry alone does not make the finite-sample magnitude law independent of the perturbation angle.

## Assumptions and scope
The response follows the fixed-design Gaussian linear model
\[
y=X\beta+\varepsilon,\qquad \varepsilon\sim N(0,\sigma^2I_n),
\]
with \(p<n\), \(X_{-j}\) full column rank, and \(r=\lVert Px_j\rVert>0\). The perturbation is exactly the OLS Gaussian-mirror perturbation of Xing, Zhao and Liu: \(z_j\sim N(0,I_n)\) independently and \(c_j\) is their equation (7). The distributional formulas are conditional on the fixed design \(X\); formulas involving \(\rho\) are additionally conditional on \(z_j\), while \(\Pi_d\) integrates only over the Gaussian perturbation direction.

The result does not analyze the high-dimensional Lasso/post-selection version, non-Gaussian regression errors, or the joint dependence among mirror statistics for different features. The residual-orthogonal case is a geometric benchmark. No claim is made that replacing the published random perturbation by an orthogonal one preserves the paper's global FDR result.

## Proof
By Frisch--Waugh--Lovell, regressing on the mirror pair together with \(X_{-j}\) is equivalent, for the two mirror coefficients, to regressing the residualized response on
\[
u=a+b,\qquad v=a-b.
\]
The source normalization gives \(\lVert b\rVert=r\), hence
\[
u^{\mathsf T}v=\lVert a\rVert^2-\lVert b\rVert^2=0.
\]
Also \(a=(u+v)/2\), so the signal component \(\beta_j a\) has coefficient \(\beta_j/2\) on each of the orthogonal columns \(u,v\). Their squared norms are
\[
\lVert u\rVert^2=2r^2(1+\rho),\qquad
\lVert v\rVert^2=2r^2(1-\rho).
\]
Gaussian OLS on orthogonal columns therefore gives the displayed independent normal laws.

The identity
\[
|u+v|-|u-v|=2\,\operatorname{sgn}(uv)\min(|u|,|v|)
\]
follows by separating the cases in which \(u\) and \(v\) have equal or opposite signs. Standardizing the two independent coefficients then gives the displayed expression for \(F_\lambda(\rho)\).

To prove strict monotonicity, set
\[
a_\rho=\lambda\sqrt{1+\rho},\qquad b_\rho=\lambda\sqrt{1-\rho},\qquad s(x)=2\Phi(x)-1.
\]
For \(0<\rho<1\), \(a_\rho>b_\rho>0\), and differentiation gives
\[
F_\lambda'(\rho)=\frac{\lambda^2}{2}
\left[
\frac{s(b_\rho)\phi(a_\rho)}{a_\rho}
-
\frac{s(a_\rho)\phi(b_\rho)}{b_\rho}
\right].
\]
Define \(H(x)=x s(x)/\phi(x)\). Since
\[
H'(x)=\frac{(1+x^2)s(x)}{\phi(x)}+2x>0\qquad(x>0),
\]
we have \(H(a_\rho)>H(b_\rho)\), which is exactly \(F_\lambda'(\rho)<0\). Evenness follows by swapping \(a_\rho\) and \(b_\rho\).

Because \(Pz_j\) is an isotropic Gaussian vector on the \(d\)-dimensional residual subspace, its normalized direction is uniform on the sphere. The inner product with the fixed unit vector \(a/r\) therefore has the stated beta-type density. Strict mixture loss follows from strict monotonicity and the fact that \(|\rho|>0\) almost surely.

For the expansion, the sphere coordinate satisfies
\[
\mathbb E[\rho^2]=\frac1d,\qquad
\mathbb E[\rho^4]=\frac{3}{d(d+2)}.
\]
A direct differentiation at zero yields
\[
F_\lambda''(0)=
-\frac{[2\Phi(\lambda)-1]\lambda(\lambda^2+1)\phi(\lambda)}{2}
-\lambda^2\phi(\lambda)^2.
\]
Taylor expansion on \(|\rho|\le1/2\), together with the fourth-moment formula, gives the \(d^{-1}\) term and an \(O_\lambda(d^{-2})\) remainder there. The sphere-density probability of \(|\rho|>1/2\) is exponentially small in \(d\), so it is absorbed in that remainder.

Under the null, the mirror identity shows that \(M_j\ge t\) exactly when the independent coefficients have the same sign and both magnitudes are at least \(t/2\). Standardizing their two variances gives the displayed product of Gaussian survival functions.

## Verification
The included `verify.py` checks the mirror identity on a deterministic grid, the sign of the analytic derivative over a broad parameter grid, the second-derivative coefficient, and deterministic quadrature values of \(\Pi_d(\lambda)\) for the numerical examples. A successful run prints `VERIFY_OK`.

These computations are replay checks rather than a substitute for the proof. The strict monotonicity is established by the analytic \(H'(x)>0\) argument, and the sphere-mixture expansion uses exact sphere-coordinate moments.

## Relationship to prior work
Xing, Zhao and Liu introduce the Gaussian-mirror pair, the statistic \(M_j\), and the scaling \(c_j\) that makes the two OLS mirror coefficients uncorrelated and hence independent under Gaussian errors. Their paper uses the resulting null symmetry for FDR control and reports empirical power, but the inspected OLS construction does not state the residual-angle parameter \(\rho\), the exact alternative positive-sign law \(F_\lambda(\rho)\), its strict orthogonal optimum, the finite-dimensional sphere mixture, or the \(d^{-1}\) loss.

Dai, Lin, Xing and Liu later generalize mirror statistics to generalized linear models and explicitly note the special finite-sample independence available in the original OLS Gaussian-mirror construction. Their analysis does not supply the angle law above. Chen et al. empirically compare Gaussian mirrors and Model-X knockoffs and discuss power sensitivity, including the importance of the mirror construction, but do not derive the finite-sample perturbation-angle distribution or sphere-mixture loss.

Targeted published-finding corpus searches for Gaussian-mirror exact distributions, perturbation-angle power, residualized OLS mirrors, independent mirror estimates, and equivalent sign/minimum formulations returned no result about this OLS Gaussian-mirror law. The closest semantic results concern unrelated Bernoulli mirror products or Gaussian-magnitude dependence.

## Limitations
The quantity \(\Pr(M_j>0)\) is a necessary sign gate for selection at a positive threshold, not the complete power of the data-dependent FDR procedure. Cross-feature dependence and the random global threshold are not analyzed. The orthogonal construction is only a benchmark; global FDR validity after changing the perturbation mechanism is unproved here. The Gaussian error model and low-dimensional OLS assumptions are essential for the exact coefficient laws. Literature search cannot prove absolute novelty, and an equivalent consequence could exist under different perturbation or regression terminology.

## References
1. Xing, X., Zhao, Z., and Liu, J. S. *Controlling False Discovery Rate Using Gaussian Mirrors*. arXiv:1911.09761v1, first public 2019-11-21; later Journal of the American Statistical Association, DOI:10.1080/01621459.2021.1923510.
2. Dai, C., Lin, B., Xing, X., and Liu, J. S. *A Scale-Free Approach for False Discovery Rate Control in Generalized Linear Models*. arXiv:2007.01237; later Journal of the American Statistical Association, DOI:10.1080/01621459.2023.2165930.
3. Chen, S., Li, Z., Liu, L., et al. *The systematic comparison between Gaussian mirror and Model-X knockoff models*. Scientific Reports 13, 5478 (2023), DOI:10.1038/s41598-023-32605-5.
