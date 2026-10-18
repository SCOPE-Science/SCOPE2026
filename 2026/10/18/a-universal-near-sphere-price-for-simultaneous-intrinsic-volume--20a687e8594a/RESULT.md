# A universal near-sphere price for simultaneous intrinsic-volume sampling

## Finding

Let \(d\geq3\), and let \(K\subset\mathbb R^d\) be a compact, strictly convex body with \(C^2\) boundary and positive principal curvatures. The \(j\)-th intrinsic-volume deficiency of an inscribed random polytope has a known leading curvature-weighted functional; normalize this leading coefficient by the least coefficient achievable by any sampling density for that particular \(j\). Define \(\mathcal Q_d(K)\) as the least possible maximum of these \(d\) normalized leading coefficients when all intrinsic volumes must share **one** boundary sampling density.

The exact minimax value is the maximum of a finite-dimensional concave function on the standard \(d\)-simplex, explicitly given below. It equals \(1\) precisely for Euclidean balls. More quantitatively, if \(K_t\) is a smooth family of positive-curvature bodies with \(K_0=B_d\), and the Gauss curvature in outer-normal coordinates obeys \(\log\kappa_t(u)=t h(u)+O(t^2)\), uniformly in \(u\in S^{d-1}\), with sufficiently smooth dependence on \(t\), then

\[
\boxed{\mathcal Q_d(K_t)=1+\frac{t^2}{4(d+1)}\operatorname{Var}_{S^{d-1}}(h)+o(t^2).}
\]

Thus, to second order, the entire hierarchy of intrinsic-volume objectives has the same minimax price as the two extremal objectives, volume and mean width. If \(h\) is nonconstant, every maximizing weight vector converges to one half on each of these two objectives and zero on the intermediate ones. Relative to uniform boundary area measure, the optimal common sampling density is \(1+\frac{t}{2}(h-\overline h)+o(t)\) to first order.

In particular, for the axially stretched spheroids \(E_{d,t}=\operatorname{diag}(1+t,1,\ldots,1)B_d\),

\[
\boxed{\mathcal Q_d(E_{d,t})=1+\frac{d^2-1}{2d^2(d+2)}t^2+O(t^3)\qquad (t\to0).}
\]

## Assumptions and scope

The dimension \(d\) is an integer at least \(3\). For each \(j=1,\ldots,d\), let \(\kappa\) be Gauss curvature and let \(H_k\) be the normalized elementary symmetric polynomial of degree \(k\) in the \(d-1\) positive principal curvatures, with \(H_0=1\) and \(H_{d-1}=\kappa\). Put

\[
\alpha=\frac{2}{d-1},\qquad \beta=\frac1{1+\alpha}=\frac{d-1}{d+1},\qquad
w_j=\kappa^{1/(d-1)}H_{d-j}.
\]

For a continuous positive density \(\rho\) on \(\partial K\) with \(\int\rho\,dS=1\), define

\[
I_j(\rho)=\int_{\partial K}w_j\rho^{-\alpha}\,dS,
\quad M_j=\left(\int_{\partial K}w_j^{\beta}\,dS\right)^{1/\beta},
\quad\mathcal Q_d(K)=\inf_\rho\max_{1\le j\le d}\frac{I_j(\rho)}{M_j}.
\]

These ratios are the ratios of the *leading* asymptotic expected intrinsic-volume errors, not an assertion about optimizers at every finite sample size. The positive constants multiplying each leading asymptotic coefficient cancel in each ratio. In particular, all \(M_j\) are positive and finite.

For the local expansion, assume \(t\mapsto K_t\) is \(C^3\) in a normal/support parametrization and the principal curvatures have sufficiently uniform Taylor expansions through second order; the displayed \(O(t^2)\) for logarithmic Gauss curvature is understood under this stronger regularity. The angular variance is with respect to normalized Haar measure on the *unit sphere*. In the density expansion, write \(q_t=\operatorname{area}(\partial K_t)\rho_t\), so that \(\int q_t\,dS_t/\operatorname{area}(\partial K_t)=1\).

## Proof

**Step 1: Exact global minimax dual and uniqueness.** Write \(v_j=w_j/M_j\), and for \(\lambda\) in the probability simplex \(\Delta_{d-1}\) define

\[
G_\lambda=\sum_{j=1}^d\lambda_jv_j,\qquad
F(\lambda)=\left(\int_{\partial K}G_\lambda^{\beta}\,dS\right)^{1/\beta}.
\]

For every strictly positive weight \(G\), Hölder's inequality, with equality characterized by strict convexity, gives

\[
\inf_{\rho>0,\,\int\rho=1}\int G\rho^{-\alpha}\,dS
=\left(\int G^{\beta}\,dS\right)^{1/\beta},\quad
\rho_G=\frac{G^{\beta}}{\int G^{\beta}\,dS}.
\]

The function \(F\), as an infimum of linear functions of \(\lambda\), is concave and continuous on the compact simplex. Fix any maximizer \(\lambda_*\), and let \(\rho_*:=\rho_{G_{\lambda_*}}\). Differentiating the minimizing value by the envelope theorem (or directly differentiating the displayed integral) gives \(\partial_jF(\lambda_*)=I_j(\rho_*)/M_j\). The first-order maximum condition along every feasible vector \(e_j-\lambda_*\) therefore yields

\[
\frac{I_j(\rho_*)}{M_j}\le\sum_k\lambda_{*,k}\frac{I_k(\rho_*)}{M_k}=F(\lambda_*)\qquad(1\le j\le d).
\]

Conversely, every density satisfies \(\max_j I_j(\rho)/M_j\ge\sum_j\lambda_{*,j}I_j(\rho)/M_j\ge F(\lambda_*)\). Together these prove the exact formula

\[
\boxed{\mathcal Q_d(K)=\max_{\lambda\in\Delta_{d-1}}F(\lambda),\quad
\rho_*=\frac{G_{\lambda_*}^{\beta}}{\int G_{\lambda_*}^{\beta}\,dS}.}
\]

Every \(I_j\) is strictly convex as a functional of \(\rho>0\). Since any minimizer of the maximum also minimizes the strictly convex weighted sum at \(\lambda_*\), the minimax density \(\rho_*\) is unique, whether or not maximizing simplex weights are unique.

**Step 2: Exact equality case.** Each ratio \(I_j/M_j\) is at least one. Equality \(\mathcal Q_d(K)=1\) forces a single density to minimize both endpoints \(j=1,d\). Their unique Hölder-optimal densities are respectively proportional to \(\kappa^{d/(d+1)}\) and \(\kappa^{1/(d+1)}\); equality forces constant Gauss curvature. A closed, strictly convex, positive-curvature hypersurface of constant Gauss curvature is a sphere. Conversely, a sphere has all \(w_j\) constant and its uniform density minimizes every objective.

**Step 3: A uniform small-perturbation lemma.** Let \(\mu_t=dS_t/\operatorname{area}(\partial K_t)\) be normalized surface area; Gauss parametrization identifies all these measures with measures on \(S^{d-1}\). Set \(A_j(t)=(\int w_j(t)^\beta\,d\mu_t)^{1/\beta}\) and \(v_j(t)=w_j(t)/A_j(t)\). Thus \(\int v_j(t)^\beta\,d\mu_t=1\). Suppose \(v_j(t)=1+t r_j(h-\overline h)+O(t^2)\) uniformly. The exact identity obtained by expanding the power \(\beta\) around one, using the individual normalizations, is

\[
\int\Big(\sum_j\lambda_jv_j(t)\Big)^\beta d\mu_t
=1+\frac{\beta(1-\beta)}2t^2
\operatorname{Var}_{\lambda}(r_j)\operatorname{Var}_{S^{d-1}}(h)+o(t^2),
\]

uniformly over \(\lambda\in\Delta_{d-1}\). Raising to power \(1/\beta\) gives

\[
F_t(\lambda)=1+\frac{1-\beta}2t^2
\operatorname{Var}_{\lambda}(r_j)\operatorname{Var}_{S^{d-1}}(h)+o(t^2).
\]

For completeness, the second-order identity uses no unknown second-order curvature terms: subtract \(\sum_j\lambda_j\int v_j(t)^\beta d\mu_t=1\) before Taylor expansion. The linear and all individual second-order terms then cancel, leaving \(\frac{\beta(\beta-1)}2\big[(\sum\lambda_j\delta_j)^2-\sum\lambda_j\delta_j^2\big]\) with \(\delta_j=t r_j(h-\overline h)+O(t^2)\).

**Step 4: Curvature weights and the universal coefficient.** At a sphere, differentiating normalized elementary symmetric curvature functions gives \(\left.\partial_t\log H_k\right|_0=\frac{k}{d-1}h\). Consequently

\[
\left.\partial_t\log w_j\right|_0=r_j h,
\quad r_j=\frac{d-j+1}{d-1},
\quad r_1-r_d=1.
\]

Normalization by \(A_j(t)\) centers the derivative, as required in Step 3. For any distribution on the numbers \(r_1,\ldots,r_d\), Popoviciu's inequality gives \(\operatorname{Var}_\lambda(r_j)\le (r_1-r_d)^2/4=1/4\), and equality has uniquely the two endpoint masses \(\lambda_1=\lambda_d=1/2\) (all interior \(\lambda_j=0\)). Since \((1-\beta)/2=1/(d+1)\), compact uniform maximization proves the universal local formula. When \(\operatorname{Var}(h)>0\), all maximizing weight vectors converge to this endpoint mixture. The optimal density expands as

\[
q_t=1+\beta\frac{r_1+r_d}2t(h-\overline h)+o(t)
=1+\tfrac12t(h-\overline h)+o(t).
\]

**Step 5: Explicit nonspherical family.** For \(E_{d,t}=\operatorname{diag}(1+t,1,\ldots,1)B_d\), the Gauss curvature at the boundary point \(A_tu\) is

\[
\kappa_t(A_tu)=(1+t)^{-2}
\left(1-u_1^2+\frac{u_1^2}{(1+t)^2}\right)^{-(d+1)/2}.
\]

Thus \(h(u)=(d+1)u_1^2-2\). The classical spherical fourth moment identities \(\mathbb E u_1^2=1/d\) and \(\mathbb E u_1^4=3/[d(d+2)]\) give

\[
\operatorname{Var}(h)=\frac{2(d+1)^2(d-1)}{d^2(d+2)}.
\]

Substitution yields \((d^2-1)/[2d^2(d+2)]\). Analyticity of the finite-dimensional, uniformly compact dual expansion for this analytic ellipsoid family upgrades the stated remainder to \(O(t^3)\), without requiring differentiability of a particular maximizing vector.

## Verification

The accompanying standalone file `verify_minimax.py` computes all curvature weights on axial ellipsoids using the exact principal-curvature formulas and integrates them by deterministic Gauss–Jacobi quadrature. It then solves the simplex dual numerically and compares \((\mathcal Q_d(E_{d,t})-1)/t^2\) against the proved coefficient in dimensions \(3,4,6\). It separately checks the exact rational sphere moments and the endpoint variance extremum. Numerical quadrature only corroborates the theorem: Steps 1–5, not finite experiments, establish the infinite-dimensional optimization and the local asymptotic law.

## Relationship to prior work

Hoehner, *One polytope fits all* (arXiv:2602.18547, first posted February 20, 2026), Theorem 3.1, establishes the individual curvature-weighted asymptotics used as the **input** here, and Theorem 3.4 proves qualitative simultaneous-optimality rigidity. Neither states the exact worst-relative-loss minimax dual, its common optimizer, nor the universal near-sphere second variation across all \(d\) intrinsic volumes. Earlier work on optimal individual densities and their Hellinger separation also differs from the minimax regret studied here. A planar minimax area–perimeter result for ellipses is a known special dimension-two comparison and is expressly excluded from this claimed higher-dimensional contribution.

## Limitations

This is a result for the leading \(N^{-2/(d-1)}\) asymptotic expectation coefficients of random **boundary-sampled** inscribed polytopes. It is not a finite-\(N\) optimizer or a uniform interchange of \(N\to\infty\) and minimax. The quadratic law is for smooth paths through a ball and does not provide a global uniform stability constant on arbitrary bodies. The near-sphere endpoint mixing assertion requires nonconstant first curvature variation; if it vanishes the quadratic regret vanishes and higher order may matter. The quantitative novelty comparison is self-review, not an independent priority certification; records with inaccessible full text leave some residual overlap risk.

## References

1. S. Hoehner, *One polytope fits all: Characterization of the Euclidean ball via simultaneous intrinsic volume approximation*, arXiv:2602.18547v1 (February 20, 2026), Section 3, especially Theorems 3.1 and 3.4; https://arxiv.org/html/2602.18547v1.
2. F. Besau, S. Hoehner, and G. Kur, *Intrinsic and Dual Volume Deviations of Convex Bodies and Polytopes*, International Mathematics Research Notices (first online December 12, 2019), DOI 10.1093/imrn/rnz277; source context for joint intrinsic-volume approximation.
