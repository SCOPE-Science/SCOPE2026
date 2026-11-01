# Exact seasonal basin ray and universal stable multiplier under time-varying mosquito competition

## Finding
For a two-population seasonal competition system with **arbitrary strictly positive continuous within-season coefficients** and equal instantaneous crowding on both populations, a bistability regime has a unique positive annual saddle. Its entire strictly positive stable basin is a straight ray, independent of initial total population. The annual map has a universal stable Floquet multiplier \(R_2^{-1}\), where \(R_2\) is the second population's boundary reproduction multiplier; neither this multiplier nor the exact global inverse-abundance relaxation rate depends on the mating response, first-population parameters, or crowding function. The unstable multiplier is explicitly a positive sensitivity integral.

## Assumptions and scope
Fix \(T>0\). On each favorable interval \(0\le t\le T\), let \(\beta(t),\mu(t),b(t),\alpha(t),\xi(t)\) be strictly positive continuous functions, repeated in each season. For \(x,y>0\), evolve
\[
\dot x=x\left[\frac{\beta(t)x}{x+\alpha(t)y}-\mu(t)-\xi(t)(x+y)\right],\qquad
\dot y=y\left[b(t)-\xi(t)(x+y)\right].
\]
At the season's end apply the diagonal reset \((x,y)\mapsto(\delta_1 x,\delta_2 y)\), with \(0<\delta_1,\delta_2\le1\). The resulting annual map is \(P\). Let
\[
B=\int_0^T b(t)\,dt,\quad
V=\int_0^T[\beta(t)-\mu(t)-b(t)]\,dt,\quad
\kappa=\delta_1/\delta_2,\quad
R_2=\delta_2e^B.
\]
Assume \(R_2>1\) and \(\kappa e^V>1\). These are the strict two-boundary persistence/bistability conditions; equality cases are excluded. The first population's boundary multiplier is \(R_1=\delta_1\exp(\int_0^T(\beta-\mu))=R_2\kappa e^V>1\).

Set \(r=x/y\), and denote by \(\phi_t(r_0)\) the unique positive solution of
\[
\dot r=r\,h(t,r),\qquad h(t,r)=\frac{\beta(t)r}{r+\alpha(t)}-\mu(t)-b(t),\quad r(0)=r_0.
\]
Define the strictly increasing scalar function
\[
Q(r)=\log\kappa+\int_0^T h(t,\phi_t(r))\,dt.
\]
There exists exactly one \(r_*>0\) with \(Q(r_*)=0\). The entire positive stable set of the annual saddle is \(\{(x,y):x=r_*y,\ y>0\}\). Every strictly positive initial state with \(x/y<r_*\) tends annually to the second-population-only fixed point, and every state with \(x/y>r_*\) tends annually to the first-population-only fixed point. All limits here are for the annual map; within each season the limiting states follow the corresponding time-periodic boundary solutions.

Let \(B(t)=\int_0^t b(s)\,ds\), \(r_t=\phi_t(r_*)\), and
\[
H=\int_0^T e^{B(t)}\xi(t)(1+r_t)\,dt>0.
\]
The interior fixed state is precisely \((x_*,y_*)=(r_*y_*,y_*)\), with \(y_*=(R_2-1)/H\). Its two annual Floquet multipliers are
\[
\boxed{\lambda_s=R_2^{-1}\in(0,1),\qquad
\lambda_u=1+r_*Q'(r_*)>1},
\]
where
\[
Q'(r_*)=\int_0^T\frac{\beta(t)\alpha(t)}{(r_t+\alpha(t))^2}\,\partial_{r_0}\phi_t(r_*)\,dt>0.
\]
Moreover, on the invariant ray, writing \(y_n\) for abundance at season starts, the exact identity
\[
\frac1{y_n}-\frac1{y_*}=R_2^{-n}\left(\frac1{y_0}-\frac1{y_*}\right)
\]
holds for every integer \(n\ge0\). Thus the stable contraction rate is exact globally along the separatrix, not only infinitesimally.

## Proof
**1. Projective decoupling and uniqueness.** Direct subtraction of the per-capita equations cancels the common crowding \(\xi(t)(x+y)\), giving the displayed scalar equation for \(r\), independent of abundance. The annual ratio map is \(\mathcal R(r)=\kappa\phi_T(r)=r\exp Q(r)\). The scalar flow is strictly order preserving. Since
\[
\partial_r h(t,r)=\frac{\beta(t)\alpha(t)}{(r+\alpha(t))^2}>0,
\]
differentiation under the integral gives \(Q'(r)>0\) for all \(r>0\). As \(r\downarrow0\), \(\phi_t(r)\to0\) uniformly on \([0,T]\), and as \(r\uparrow\infty\), \(\phi_t(r)\to\infty\) uniformly; hence
\[
\lim_{r\downarrow0}Q(r)=\log\kappa-\int_0^T(\mu+b)<0,\qquad
\lim_{r\uparrow\infty}Q(r)=\log\kappa+V>0.
\]
The first inequality follows from \(\log\delta_1-\int\mu-\log R_2<0\), using \(\delta_1\le1\), \(\mu>0\), and \(R_2>1\). Strict monotonicity gives exactly one root \(r_*\). If \(r_0<r_*\), iterates of \(\mathcal R\) decrease strictly to zero; if \(r_0>r_*\), they increase without bound, since the only interior fixed ratio is \(r_*\). The ray is invariant because the annual ratio returns to itself.

**2. Exact abundance map and positive fixed state.** Given any ratio orbit \(r_t\), the variable \(z=1/y\) obeys the linear differential equation \(\dot z=-b(t)z+\xi(t)(1+r_t)\). Variation of constants and the annual reset give
\[
\frac1{y_{n+1}}=\frac1{R_2}\left[\frac1{y_n}+H(r_n)\right],\quad
H(r)=\int_0^T e^{B(t)}\xi(t)[1+\phi_t(r)]\,dt.
\]
For \(r_n=r_*\), this is one fixed affine contraction with factor \(R_2^{-1}\). Its unique positive fixed point has \(1/y_*=H/(R_2-1)\). Iterating the affine map proves the exact identity in the Finding section, and the formula for \(x_*\) follows from the ratio.

**3. The two full Floquet multipliers.** The differentiable coordinate change \((x,y)\leftrightarrow(r,y)\) is valid at every interior state, and the annual Jacobian is triangular in these coordinates because the ratio map does not depend on abundance. The composition-direction eigenvalue is \(\mathcal R'(r_*)=1+r_*Q'(r_*)>1\); the abundance-direction eigenvalue is the derivative of the reciprocal logistic map at its positive fixed point, namely \(R_2^{-1}\in(0,1)\). Thus the unique positive fixed point is a hyperbolic saddle.

**4. Global basin classification.** Positivity and global forward existence follow from the logistic quadratic damping and bounded coefficients. If \(r_n\downarrow0\), then the within-season ratios tend uniformly to zero. The reciprocal \(y\) recurrence has coefficient \(R_2^{-1}<1\) and forcing \(H(r_n)\to H(0)=\int_0^T e^{B(t)}\xi(t)dt\); hence \(y_n\) tends to the unique positive second-only logistic fixed point, while \(x_n=r_ny_n\to0\). If \(r_n\uparrow\infty\), use instead \(w=1/x\), which satisfies
\[
\dot w=-\left[\frac{\beta(t)r_t}{r_t+\alpha(t)}-\mu(t)\right]w+\xi(t)(1+1/r_t).
\]
Its annual affine recurrence converges in coefficients to that of the first-only logistic system. Since \(R_1>1\), the limiting reciprocal affine map is a contraction and \(x_n\) tends to its unique positive boundary fixed point; \(y_n=x_n/r_n\to0\). Every strictly positive orbit is in one of these three cases, so no further positive periodic orbit exists.

## Verification
A standalone Python program `verify.py` integrates a genuinely time-varying example with \(T=1\), \(\delta_1=0.78\), \(\delta_2=0.75\), \(\beta(t)=2.2+0.3\sin(2\pi t)\), \(\mu(t)=0.4+0.05\sin(2\pi t)\), \(b(t)=0.6+0.1\cos(2\pi t)\), \(\alpha(t)=1.3+0.2\sin(2\pi t)\), and \(\xi(t)=0.8+0.1\cos(2\pi t)\). It confirms the root \(r_*\approx1.031892990204\), stable multiplier \(\lambda_s\approx0.731748848125\), unstable multiplier \(\lambda_u\approx1.715219128729\), and independent full-Jacobian spectra to numerical integration tolerance. The analytic proof, not these finite computations, supplies the all-coefficient quantifiers.

## Relationship to prior work
Niu, Wang, Xie and Zheng (2026, arXiv:2610.29233v1) prove global classification and saddle instability for their constant-rate Aedes seasonal model, but give a qualitative continuous basin separator and qualitative inequalities for Floquet multipliers. Zheng, Chang, Guo and Yu (2025, doi:10.1137/24M1694744) introduce the fixed-rate switched mosquito model and related separation estimates. The constant-rate equal-crowding basin-ray case is an antecedent and is **not** claimed as new here. The contribution is the all-time-dependent coefficient theorem with exact two-multiplier formula and globally exact inverse-abundance relaxation. General time-dependent shared-crowding Lotka–Volterra selection results lack the nonlinear ratio-dependent mating term that creates the interior saddle and bistability.

## Limitations
The classification applies to equal instantaneous crowding functions in both equations, strictly positive continuous within-season coefficients, a single positive diagonal reset per season, and the strict two-boundary bistability regime. It does not claim a straight separator for unequal crowding, nor classify equality-threshold cases or stochastic seasonal variation. The 2025 antecedent's complete text was not accessible for comparison; novelty is a best-knowledge assessment, and an independent mathematical audit remains outstanding.

## References
1. Lei Niu, Yi Wang, Xizhuang Xie and Bo Zheng, *Bistable Dynamics and Complete Classifications of A Seasonal Competition Model Between Aedes aegypti and Aedes albopictus*, arXiv:2610.29233v1, first public 2026-10-21; https://arxiv.org/abs/2610.29233.
2. Bo Zheng, Lijie Chang, Hongpeng Guo and Jianshe Yu, *Global Competitive Dynamics of Aedes aegypti and Aedes albopictus with Favorable-unfavorable Seasonal Shifts*, SIAM Journal on Applied Mathematics **85** (2025), 1189–1211, doi:10.1137/24M1694744.
