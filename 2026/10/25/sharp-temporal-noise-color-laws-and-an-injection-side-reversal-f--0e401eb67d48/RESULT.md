# Sharp temporal-noise-color laws and an injection-side reversal for constrained midpoint integration

## Finding

For any finite-dimensional, linearly constrained, symmetric positive definite problem whose constraint kernel is invariant under its stiffness matrix, the implicit midpoint rule has a **strictly convex stationary numerical spread** as a function of the lag-one correlation of stationary Gaussian AR(1) perturbations, except when every midpoint amplification vanishes. This holds when the noise is applied after the midpoint solve and when it is inserted into the midpoint equation's right-hand side. The two conventions can have **opposite uniquely optimal correlation signs**, even though each has the same Gaussian marginal at its own injection point for every correlation choice.

More precisely, let \(K=\ker B\) have dimension \(m\ge1\), with \(B\) of full row rank. Let \(A\) be real symmetric positive definite, let \(AK\subseteq K\), and consider \(\dot u+Au+B^{\mathsf T}\lambda=0\), \(Bu=0\), with \(u(0)\in K\). On an orthonormal eigenbasis of \(A\vert_K\), write \(A e_i=\lambda_i e_i\), where \(\lambda_i>0\). Fix \(h>0\) and set
\[
\mu_i=\frac{1-h\lambda_i/2}{1+h\lambda_i/2}\in(-1,1),\qquad d_i=\frac1{1+h\lambda_i/2}>0.
\]
For each \(-1<\rho<1\), let the stationary perturbation input satisfy
\[
\eta_{n+1}=\rho\eta_n+\sqrt{1-\rho^2}\,z_{n+1},\quad
z_n\stackrel{\mathrm{iid}}\sim\mathcal N(0,h^5Q),\quad
\eta_0\sim\mathcal N(0,h^5Q),
\]
where \(Qe_i=q_i e_i\), \(q_i>0\), and the initial perturbation is independent of subsequent innovations and deterministic \(u(0)\). Thus \(\operatorname{Cov}(\eta_n,\eta_{n+k})=h^5\rho^{|k|}Q\) and every fixed-time perturbation marginal is independent of \(\rho\).

Consider either the **state-increment** integrator \(U_{n+1}=M_hU_n+\eta_n\), or the **equation-residual** integrator \((I+hA/2)U_{n+1}=(I-hA/2)U_n+\eta_n\) on \(K\). Here \(M_h=(I+hA/2)^{-1}(I-hA/2)\vert_K\). For either convention, let \(g_i=1\) (state-increment) or \(g_i=d_i\) (equation-residual). Then
\[
\boxed{
\lim_{n\to\infty}\mathbb E\|U_n\|_2^2
=R_h(\rho)
=h^5\sum_{i=1}^m\frac{q_i g_i^2}{1-\mu_i^2}
\frac{1+\mu_i\rho}{1-\mu_i\rho}.}
\]
If any \(\mu_i\ne0\), this risk is strictly convex on \((-1,1)\) and has at most one minimizer. An interior minimizer exists **exactly** when \(R_h'(-1)<0<R_h'(1)\), interpreting the two derivatives by continuous extension. Otherwise the infimum is reached only in the limit \(\rho\downarrow-1\) if \(R_h'(-1)\ge0\), or \(\rho\uparrow1\) if \(R_h'(1)\le0\). If all \(\mu_i=0\), the risk is constant.

For exactly two modes \(\mu_1=u>0\), \(\mu_2=-v<0\), let
\[
\alpha=\sqrt{\frac{q_1g_1^2u}{1-u^2}},\qquad
\beta=\sqrt{\frac{q_2g_2^2v}{1-v^2}}.
\]
The unconstrained stationary point is
\[
\boxed{\rho_* =\frac{\beta-\alpha}{\alpha v+\beta u}.}
\]
It lies in \((-1,1)\) precisely when
\[
\frac{1-v}{1+u}<\frac\beta\alpha<\frac{1+v}{1-u}.
\]
In that case it is the unique global minimizer; otherwise the appropriate endpoint is the unattained infimum for the nondegenerate AR(1) family.

**Exact injection-side reversal.** Take \(h=1\), \(m=2\), \(\lambda_1=1\), \(\lambda_2=10\), and \(Q=I_K\). Then \((\mu_1,\mu_2)=(1/3,-2/3)\). The state-increment convention has the unique optimum
\[
\boxed{\rho_{\mathrm{state}}=9\sqrt5-\frac{39}{2}>0,\qquad
R_{\mathrm{state}}(\rho_{\mathrm{state}})=\frac{6\sqrt5}{5}-\frac9{40}<\frac{117}{40}=R_{\mathrm{state}}(0).}
\]
For isotropic perturbations inserted in the equation's right-hand side, the midpoint solve filters their mode variances to \((4/9,1/36)\), and the unique optimum instead is
\[
\boxed{\rho_{\mathrm{equation}}=\frac{9\sqrt5-33}{19}<0,\qquad
R_{\mathrm{equation}}(\rho_{\mathrm{equation}})=\frac3{20}+\frac{2\sqrt5}{15}<\frac{11}{20}=R_{\mathrm{equation}}(0).}
\]
The two optimal signs are therefore opposite. These are separate optimization problems with fixed marginals *within each injection convention*; no assertion that the two output marginal covariances match is made.

The same family also preserves the original order of accuracy: with \(A,B,Q\) fixed, \(\rho\) fixed in \((-1,1)\), \(T>0\), and the \(h^{5/2}\) perturbation amplitude above, the root-mean-square error relative to the exact constrained flow satisfies
\[
\max_{0\le nh\le T}\bigl(\mathbb E\|U_n-u(nh)\|_2^2\bigr)^{1/2}=O(h^2)
\quad\text{as }h\downarrow0,
\]
with a bound uniform for \(|\rho|\le\rho_0<1\). This finite-horizon statement does not extend uniformly to \(\rho\to\pm1\) without additional assumptions.

## Assumptions and scope

All vector spaces are finite-dimensional and real, and the norm is Euclidean. The noise is additive and constrained to \(K\), with a *stationary* AR(1) input, independent Gaussian innovations, and an eigenbasis-diagonal positive definite input covariance \(Q\). Both integrator variants are completely specified above, with equal step sizes and fixed \(h\). The equation-residual convention is the midpoint saddle-point right-hand-side perturbation specialized to an invariant kernel; the state-increment convention randomizes the completed one-step map. The exact risk concerns the long-time expected squared distance from the zero equilibrium, which is also the asymptotic mean-square error because the exact constrained solution decays to zero.

An explicit nontrivial ambient constraint realizing the example is \(B=(1,1,1)\) on \(\mathbb R^3\), with kernel orthonormal basis \(e_1=(1,-1,0)/\sqrt2\), \(e_2=(1,1,-2)/\sqrt6\). Define \(A=e_1e_1^{\mathsf T}+10e_2e_2^{\mathsf T}+4e_3e_3^{\mathsf T}\), with \(e_3=(1,1,1)/\sqrt3\). This \(A\) is symmetric positive definite and preserves the nontrivial constraint kernel.

## Proof

**Projection and reduction.** The exact constrained flow remains in \(K\), and symmetry plus \(AK\subseteq K\) imply that the orthogonal eigenbasis of \(A\vert_K\) decouples both midpoint solves. For every \(h>0\), \(1+h\lambda_i/2>0\) and \(|\mu_i|<1\). Because every perturbation lies in \(K\), either update satisfies \(BU_n=0\) identically. The equation-residual convention yields an *output* input of \(g_i\eta_{i,n}=d_i\eta_{i,n}\), while the state-increment convention has \(g_i=1\).

**Stationary second moment.** For a single mode with amplifier \(\mu\), injected marginal variance \(w=h^5qg^2\), and correlation \(\rho\), the limiting filter representation is \(X_n=\sum_{j\ge0}\mu^j\epsilon_{n-1-j}\). This series converges in \(L^2\). Its variance is
\[
\sum_{j,k\ge0}\mu^{j+k}w\rho^{|j-k|}
=\frac{w}{1-\mu^2}\left(1+2\sum_{\ell\ge1}(\mu\rho)^\ell\right)
=\frac{w(1+\mu\rho)}{(1-\mu^2)(1-\mu\rho)}.
\]
The first equality uses the complete lag covariance, not a false independence of input and iterate. The geometric sums converge absolutely since \(|\mu|,|\rho|<1\). Finite initial errors vanish as \(n\to\infty\). Summing orthogonal squared components gives the asserted risk, without requiring cross-mode independence beyond the stated construction.

**Optimality.** Direct differentiation yields
\[
R_h'(\rho)=2h^5\sum_i\frac{q_i g_i^2\mu_i}{(1-\mu_i^2)(1-\mu_i\rho)^2},
\quad
R_h''(\rho)=4h^5\sum_i\frac{q_i g_i^2\mu_i^2}{(1-\mu_i^2)(1-\mu_i\rho)^3}.
\]
Every denominator is positive for \(-1\le\rho\le1\). Thus the second derivative is strictly positive whenever at least one \(\mu_i\ne0\), proving unique-interior/boundary cases by monotonicity of \(R_h'\). In the mixed two-mode case, the equation \(R_h'(\rho)=0\) is exactly \(\alpha/(1-u\rho)=\beta/(1+v\rho)\), leading to the closed form and interval criterion.

**Exact example.** The two midpoint multipliers are \(u=1/3\) and \(-v=-2/3\), with equation-input gains \(d_1=2/3\) and \(d_2=1/6\). For state-increment noise, the derivative simplifies to
\[
R_{\mathrm{state}}'(\rho)=\frac{27(4\rho^2+156\rho-99)}{20(\rho-3)^2(2\rho+3)^2},
\]
whose only root in \((-1,1)\) is \(9\sqrt5-39/2\). For equation-residual noise,
\[
R_{\mathrm{equation}}'(\rho)=\frac{3(19\rho^2+66\rho+36)}{5(\rho-3)^2(2\rho+3)^2},
\]
whose only root in \((-1,1)\) is \((9\sqrt5-33)/19\). Substituting these roots in the stationary formulas gives the displayed optimal and independent-input risks. Strict convexity establishes *global* optimality, beyond numerical checks.

**Finite-horizon order.** For fixed \(T\), deterministic implicit midpoint on the symmetric linear constrained system has uniform global error \(O(h^2)\). The noise-induced part of either integrator at index \(n\) is a sum of at most \(n\) propagated centered Gaussian inputs. The \(n\times n\) Toeplitz lag-correlation matrix \((\rho^{|j-k|})\) has operator norm bounded by \((1+|\rho|)/(1-|\rho|)\). Also \(\|M_h^j\|\le1\) and \(\|H_h\|\le1\) for both injection conventions. Hence the noise-induced expected squared norm is at most
\[
h^5\operatorname{tr}(Q)\,n\,\frac{1+|\rho|}{1-|\rho|}
\le h^4\operatorname{tr}(Q)T\frac{1+|\rho|}{1-|\rho|},
\]
while the deterministic error is \(O(h^2)\). Adding the two terms in \(L^2\) proves the claimed second-order root-mean-square bound.

## Verification

The accompanying `verify.py` uses exact rational arithmetic to compare the stationary filter formula with an independently derived bivariate-moment recursion over multiple signs, lag correlations, and variances. It also checks the two exact derivative identities, exact independent-noise risks, the radical candidate roots numerically, the strict optimization inequalities over a rational grid, and convergence of finite-lag double sums to the closed form. It passed 1,080 checks. Finite tests do not establish convexity or optimality; those are proved above.

## Relationship to prior work

Altmann and Moradi introduced Gaussian perturbations for constrained time integrators, gave a kernel-preserving midpoint formulation, and proved strong convergence under independent perturbations (arXiv:2406.07220, original posting June 11, 2024; specifically their equations (2.5) and (4.3), midpoint noise implementation and Theorem 3.2). Conrad, Girolami, Särkkä, Stuart and Zygalakis previously analyzed independent Gaussian randomizations of deterministic numerical solvers. General spectral input-output theory for linear systems with stationary forcing is classical (Arnold and Wihstutz), while Honeycutt studied stochastic Runge–Kutta methods with colored physical forcing. Such tools explain how one might derive covariance formulas, but the cited material inspected does not provide the strictly convex one-parameter correlation optimization for constrained midpoint perturbations or the opposite optimal signs under the two injection conventions. This is a claim about those *specific* statements, not about universal uniqueness in the literature.

## Limitations

This is an exact-arithmetic, linear, homogeneous, symmetric, invariant-kernel result with an input covariance diagonal in the dynamic eigenbasis; it does not extend unproved to nonlinear DAEs, nonnormal operators, general correlated spatial inputs, or arbitrary temporal noise laws. The optimization objective is **minimizing long-time numerical spread for fixed per-step input marginals**, not proving statistical calibration or superior fidelity of reported uncertainty. The two injection conventions have different output marginal covariances even when their injected inputs are isotropic; the result compares signs of their *separate* optima, not equal output distributions. Endpoints \(\rho=\pm1\) lie outside the nondegenerate AR(1) innovation family. The asymptotic stationary optimization and finite-horizon order analysis are distinct limits. Specialized linear-filtering literature may contain equivalent covariance-based optimizers; publication priority is not independently established.

## References

1. R. Altmann and A. Moradi, *Probabilistic Time Integration for Semi-explicit PDAEs*, arXiv:2406.07220 (first posted June 11, 2024); *Statistics and Computing* **35**, 16 (2025), doi:10.1007/s11222-024-10543-0.
2. P. R. Conrad, M. Girolami, S. Särkkä, A. Stuart and K. Zygalakis, *Statistical analysis of differential equations: introducing probability measures on numerical solutions*, *Statistics and Computing* **27** (2017), 1065–1082, doi:10.1007/s11222-016-9671-0; preprint arXiv:1506.04592.
3. L. Arnold and V. Wihstutz, *Wide Sense Stationary Solutions of Linear Systems with Additive Noise*, *SIAM Journal on Control and Optimization* **21** (1983), 413–426, doi:10.1137/0321024.
4. R. L. Honeycutt, *Stochastic Runge–Kutta algorithms. II. Colored noise*, *Physical Review A* **45** (1992), 604–610, doi:10.1103/PhysRevA.45.604.
