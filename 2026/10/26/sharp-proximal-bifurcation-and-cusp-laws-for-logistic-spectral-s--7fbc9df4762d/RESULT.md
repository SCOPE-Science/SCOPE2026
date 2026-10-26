# Sharp proximal bifurcation and cusp laws for logistic spectral shrinkage

## Finding
Consider the logistic shrinkage profile
\[
h_a(t)=\frac{t}{1+\exp[-a(t-1)]},\qquad t\ge0,\quad a>0,
\]
and its inverse-designed penalty \(\phi_a\), defined by \(\phi_a(0)=0\) and
\[
\phi_a'(u)=h_a^{-1}(u)-u\quad(u\ge0).
\]
For \(\beta>0\) and input \(s\ge0\), let
\[
\mathcal P_{\beta}(s)=\operatorname*{argmin}_{u\ge0}
 \left\{\frac12(u-s)^2+\beta\phi_a(u)\right\}.
\]
Let \(t_0>1\) be the unique solution of
\[
a t_0\tanh\left(\frac{a(t_0-1)}2\right)=2,
\]
and define \(L=h_a'(t_0)>1\), \(H=-h_a'''(t_0)>0\), and
\[
\beta_c=\frac{L}{L-1}.
\]
The following conclusions hold for **every** \(a>0\).

1. **Exact uniqueness threshold.** The set \(\mathcal P_\beta(s)\) consists of exactly one point for every \(s\ge0\) if and only if \(0<\beta\le\beta_c\). At \(\beta=\beta_c\) the minimizing selection is continuous, but is not locally Lipschitz at a unique positive input \(s_c=2h_a(t_0)\). With \(u_c=h_a(t_0)\),
\[
 u_\beta(s)-u_c\sim L\left(\frac{6(L-1)}H\right)^{1/3}
 \operatorname{sgn}(s-s_c)|s-s_c|^{1/3},
 \qquad s\to s_c,\quad\beta=\beta_c.
\]
2. **Exactly one coexistence datum above threshold.** For every \(\beta>\beta_c\), there exists exactly one \(s_*(\beta)>0\) such that \(\mathcal P_\beta(s_*)\) consists of two distinct positive points \(u_-(\beta)<u_+(\beta)\). For all other nonnegative inputs it is a singleton. The maximizing and minimizing stationary branches have exactly two folds, and the global proximal selection jumps from the smaller branch to the larger one as \(s\) crosses \(s_*\).
3. **Sharp onset exponents and leading constants.** Put \(\varepsilon=\beta-\beta_c\downarrow0\), \(q=(L-1)\sqrt{2/H}\), and \(S_\beta(t)=\beta t+(1-\beta)h_a(t)\). Write \(s_{\max}\) and \(s_{\min}\) for the two fold inputs, in decreasing order. Then
\[
 \frac{s_{\max}-s_{\min}}{\varepsilon^{3/2}}
 \longrightarrow\frac43(L-1)q,
 \qquad
 \frac{u_+(\beta)-u_-(\beta)}{\sqrt\varepsilon}
 \longrightarrow 2\sqrt3\,Lq,
\]
and the unique equal-depth datum satisfies
\[
 s_*(\beta)=S_\beta(t_0)+o(\varepsilon^{3/2})
 =s_c+\varepsilon\bigl(t_0-h_a(t_0)\bigr)+o(\varepsilon^{3/2}).
\]

These are statements about the *global* proximal minimizers, not merely the stationary roots. In particular, the strict condition \(\beta(1-1/L)<1\), known to make the proximal subproblem strongly convex, is sufficient but not necessary for uniqueness at its equality endpoint; above the endpoint, multivaluedness occurs for a unique datum.

## Assumptions and scope
The scalar variable, datum, hardness parameter and proximal scale are real with \(u,s\ge0\), \(a,\beta>0\). All assertions concern the exact global optimization problem, with no numerical or statistical assumptions. The normalized threshold parameter is one. For a general threshold \(\lambda>0\), replace \(u,s\) with \(u/\lambda,s/\lambda\) and the penalty by \(\phi_{a,\lambda}(u)=\lambda^2\phi_a(u/\lambda)\); all conclusions rescale, and \(\beta_c\) remains unchanged. The matrix spectral penalty is the sum of this scalar penalty applied to singular values. A one-by-one positive matrix already establishes the claimed failure of universal single-valuedness above \(\beta_c\).

## Proof
**1. Unique point of maximal shrinker slope.** Write \(p(t)=\bigl(1+e^{-a(t-1)}\bigr)^{-1}\). Direct differentiation gives
\[
 h_a'(t)=p(t)+atp(t)(1-p(t)),
\]
\[
 h_a''(t)=ap(t)(1-p(t))
 \left[2-at\tanh\left(\frac{a(t-1)}2\right)\right].
\]
The bracket is positive for \(0\le t\le1\); on \(t>1\), the function \(t\tanh(a(t-1)/2)\) is strictly increasing from zero to infinity. Therefore \(h_a''\) has exactly one zero \(t_0>1\), changing from positive to negative. Thus \(h_a'\) is strictly unimodal, has unique maximum \(L>1\), and \(H=-h_a'''(t_0)>0\). The equality \(h_a'(t_0)=L\) and the defining equation imply
\[
 L=\frac{p(t_0)}{2p(t_0)-1},\qquad
 \beta_c=\frac{p(t_0)}{1-p(t_0)}.
\]
In particular \(S_{\beta_c}(t_0)=2h_a(t_0)\).

**2. Reduction to a one-variable S-curve.** Since \(h_a\) is an increasing bijection of \([0,\infty)\), the stationarity condition at \(u=h_a(t)\) is
\[
 \frac{d}{du}\left[\frac12(u-s)^2+\beta\phi_a(u)\right]
 =S_\beta(t)-s=0.
\]
The objective derivative at the boundary \(u=0\) is \(-s\), so no positive input has a boundary minimizer; at \(s=0\), nonnegativity of \(\phi_a\) makes \(u=0\) the unique minimizer. Also
\[
 S_\beta'(t)=\beta+(1-\beta)h_a'(t).
\]
For \(0<\beta\le\beta_c\), this derivative is nonnegative and vanishes only at \(t=t_0\) when \(\beta=\beta_c\). Consequently \(S_\beta\) is strictly increasing from zero to infinity, giving exactly one global minimizer for each input. For \(\beta>\beta_c\), the level \(\beta/(\beta-1)\in(1,L)\) is met by \(h_a'\) exactly twice, at \(0<t_1<t_0<t_2\). The curve \(S_\beta\) increases on \([0,t_1]\), decreases on \([t_1,t_2]\), and increases on \([t_2,\infty)\). Set \(s_{\max}=S_\beta(t_1)>s_{\min}=S_\beta(t_2)>0\). Inputs in \((s_{\min},s_{\max})\) have three interior stationary points, with strict local minima on the two outer branches and a local maximum on the middle branch. Outside the closed interval there is one stationary point, the global minimizer.

**3. One and only one Maxwell datum.** For \(s\) in the open fold interval, denote the outer stationary points by \(u_l(s)<u_r(s)\) and their objective values by \(E_l(s),E_r(s)\). They are differentiable and satisfy
\[
 \frac{d}{ds}\bigl(E_r(s)-E_l(s)\bigr)
 =u_l(s)-u_r(s)<0.
\]
At \(s=s_{\min}\), the upper stationary point is a tangency rather than a minimum and lies at strictly higher objective value than the genuine lower minimum: integrate the derivative \((S_\beta(t)-s)h_a'(t)\), which is nonnegative between them and not identically zero. At \(s=s_{\max}\), the analogous derivative is nonpositive from the lower tangency to the genuine upper minimum; the upper minimum has strictly lower value. Continuity and strict decrease yield exactly one zero of \(E_r-E_l\), hence exactly one datum with two global minimizers. At either fold boundary the tangential stationary point is not an additional global minimizer.

**4. Cubic critical response.** At \(\beta=\beta_c\), put \(B=H/(L-1)>0\). Since \(h_a''(t_0)=0\), Taylor's theorem gives
\[
 S_{\beta_c}(t)=s_c+\frac B6(t-t_0)^3+O((t-t_0)^4),
 \qquad
 h_a(t)=u_c+L(t-t_0)+O((t-t_0)^3).
\]
The strictly increasing inverse therefore has precisely the stated signed cubic-root asymptotic. Its slope diverges at \(s_c\), so it is not locally Lipschitz there.

**5. Fold separation and global jump.** Let \(\varepsilon=\beta-\beta_c>0\). Uniformly for bounded real \(x\), with \(t=t_0+\sqrt\varepsilon\,x\) and \(\overline s_\beta=S_\beta(t_0)\),
\[
 \varepsilon^{-3/2}\bigl[S_\beta(t)-\overline s_\beta\bigr]
 =-(L-1)x+\frac B6x^3+O(\sqrt\varepsilon).
\]
The two fold locations have rescaled limits \(x=\pm q\), where \(q=\sqrt{2(L-1)/B}=(L-1)\sqrt{2/H}\). Evaluating this cubic at the folds gives the displayed \(\varepsilon^{3/2}\) fold-gap constant.

For the coexistence datum, write \(s_*=\overline s_\beta+\sigma_\varepsilon\varepsilon^{3/2}\). Its location between the folds makes \(\sigma_\varepsilon\) bounded. The exact identity
\[
 \frac{d}{dt}J_{\beta,s}(h_a(t))
 =\bigl(S_\beta(t)-s\bigr)h_a'(t),\quad
 J_{\beta,s}(u)=\tfrac12(u-s)^2+\beta\phi_a(u),
\]
shows that the objectives near \(t_0\), after subtracting their value at \(t_0\) and dividing by \(\varepsilon^2\), converge uniformly on bounded \(x\) to
\[
 L\left[-\frac{L-1}{2}x^2+\frac B{24}x^4-\sigma x\right]
\]
when \(\sigma_\varepsilon\to\sigma\). Any limit of equal-depth outer minima must have \(\sigma=0\): in this symmetric quartic family their energy difference is strictly decreasing in \(\sigma\), and equal depths occur only at zero. Hence \(\sigma_\varepsilon\to0\). The two outer minimizers satisfy \((t_\pm-t_0)/\sqrt\varepsilon\to\pm\sqrt3\,q\). Since \(h_a'(t_0)=L\), their separation in \(u\) is \(2\sqrt3\,Lq\sqrt\varepsilon+o(\sqrt\varepsilon)\), as claimed. This also proves the asserted Maxwell location.

## Verification
The included standalone script `prox_bifurcation_check.py` numerically reconstructs the unique slope peak, critical scale and endpoint identity, two folds, the equal-depth input through a signed area integral, and the two asymptotic constants for several hardness values and decreasing supercritical offsets. Numerical tests support the calculations but do not substitute for the global and asymptotic arguments above. The exact proof relies on differentiation, strict monotonicity, one-dimensional energy comparison, and uniform Taylor expansions; no finite search is asserted to prove an infinite-domain claim.

## Relationship to prior work
Yang, Wang and Yang (2026), arXiv:2610.21664, construct the logistic-induced spectral penalty and prove its exact weak-convexity constant \(\rho_a=1-1/L\). Their Theorem 5.2 gives a *sufficient* globally unique scaled proximal map under \(\beta\rho_a<1\). That result is an input to the present analysis, not a newly claimed theorem. The additional assertions here are uniqueness at the critical endpoint, a unique two-minimizer input for *every* supercritical scale, and quantified cubic-root/square-root/fold exponents with their exact family-dependent constants. Lu et al. (2014/2015) prove general monotone-set behavior and singular-value reduction for nonconvex proximal operators; these general statements do not calculate the logistic family's critical diagram or equal-depth bifurcation. Generic cusp normal forms motivate the scaling argument, but the analytic unimodality, global-minimizer classification and constants are specific to this induced penalty.

## Limitations
Only the inverse-designed logistic penalty and the scalar proximal problem are classified. The result does not claim that every nonconvex spectral penalty shares these constants, that an entire proximal-gradient trajectory is unstable above the threshold, or that finite-precision algorithms exhibit the asymptotic laws without resolution limits. The matrix implication is a universal single-valuedness obstruction, not a classification of all matrix-valued minimizer manifolds. Originality may be affected by unindexed specialized proximal-bifurcation analyses; broad nonconvex proximal theory contains related qualitative mechanisms.

## References
1. G. Yang, Z. Wang, and G. Yang, *Data-Driven Smooth-to-Hard Spectral Regularization for General Linear Inverse Problems*, arXiv:2610.21664v1 (first public 2026-10-15), Sections 3–5, especially Theorems 4.2 and 5.2. https://arxiv.org/html/2610.21664
2. C. Lu, C. Zhu, C. Xu, S. Yan, and Z. Lin, *Generalized Singular Value Thresholding*, arXiv:1412.2231 (2014), especially Theorems 1–2. https://arxiv.org/abs/1412.2231
3. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, Springer, third edition (2004), for classical cusp normal-form background; no claim of a new general cusp universality theorem is made.
