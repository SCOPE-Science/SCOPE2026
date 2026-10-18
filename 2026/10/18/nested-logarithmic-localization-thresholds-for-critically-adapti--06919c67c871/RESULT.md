# Nested logarithmic localization thresholds for critically adaptive Brownian resetting

## Finding

A one-dimensional Brownian particle with generator \(D\partial_x^2\), \(D>0\), is returned instantaneously to the origin at state-dependent hazard \(r(x)\). At the marginal inverse-square intensity \(2D/|x|^2\), the existence of a stationary probability is not determined by the leading term alone: logarithmic corrections resolve the transition.

Fix \(\ell>0\), and write \(t=\log(|x|/\ell)\) on sufficiently large \(|x|\). Suppose \(r\) is bounded, continuous, nonnegative, even, and eventually positive.

**First logarithmic boundary.** If, for some \(a\in\mathbb R\), \(\delta>0\), and finite \(K\),
\[
\left|\frac{x^2r(x)}D-2-\frac a t\right|\leq \frac K{t^{1+\delta}},
\]
then the resetting diffusion has a stationary probability distribution **if and only if** \(a>3\). When it exists, its density \(p_*\) obeys
\[
\lim_{|x|\to\infty}\frac{\log(|x|p_*(x))}{\log\log(|x|/\ell)}=-\frac a3,
\quad
\lim_{R\to\infty}\frac{\log\mathbb P_*(|X|>R)}{\log\log(R/\ell)}=1-\frac a3.
\]

**Second logarithmic boundary.** If, for some \(b\in\mathbb R\), \(\delta>0\), and finite \(K\),
\[
\left|\frac{x^2r(x)}D-2-\frac3t-\frac b{t\log t}\right|
\leq\frac K{t(\log t)^{1+\delta}},
\]
then a stationary probability exists **if and only if** \(b>3\). In that case,
\[
\lim_{|x|\to\infty}\frac{\log\bigl(|x|t\,p_*(x)\bigr)}{\log\log t}=-\frac b3,
\quad
\lim_{R\to\infty}\frac{\log\mathbb P_*(|X|>R)}{\log\log\log(R/\ell)}=1-\frac b3.
\]
Both equality cases, \(a=3\) under the first remainder assumption and \(b=3\) under the second, are nonlocalizing. These statements concern the ordinary continuous-time stationary probability, not the existence of a nonnormalizable stationary solution of the forward equation.

## Assumptions and scope

Brownian motion \(B\) is continuous with variance \(2Dt\) over a time interval of length \(t\); a resetting clock conditioned on a trajectory has survival probability \(\exp(-\int_0^s r(B_u)\,du)\). Independent Brownian paths and clocks are used after each reset. Rates are even for a two-sided conclusion, but no restrictions are placed on their detailed behavior on compact sets beyond boundedness, continuity, and nonnegativity. The stated tail formulas only use \(t>e\) and hold beyond some finite radius. The constants \(K,\delta,\ell\) need not be uniform across different models. The two hypotheses are separate, increasingly resolved critical classes; they do not claim to classify arbitrary \(o(1)\) perturbations.

## Proof

**1. Renewal occupation reduction.** Let \(R_0\) be the first resetting time from the origin. Because Brownian motion is recurrent and \(r\) is positive on some interval, \(R_0<\infty\) almost surely. The cycles between resets are independent and identically distributed. If \(G(x)\,dx=\mathbb E_0\int_0^{R_0}\mathbf1_{\{B_s\in dx\}}\,ds\) denotes the unnormalized killed occupation measure, then its density satisfies
\[
DG''-rG=-\delta_0,\qquad \mathbb E_0R_0=\int_{\mathbb R}G(x)\,dx.
\]
The regenerative stationary law, when normalizable, is \(G/\mathbb E_0R_0\). Conversely, any invariant probability density must be a normalizable solution of the same one-source equation (with a positive source coefficient), so normalization is possible exactly when \(\mathbb E_0R_0<\infty\). In particular, the stationary density is unique when it exists.

For \(R>0\) and \(x\ge R\), put
\[
u_r(x)=\mathbb E_x\exp\left(-\int_0^{\tau_R}r(B_s)\,ds\right),
\qquad\tau_R=\inf\{s:B_s=R\}.
\]
Then \(Du_r''=ru_r\) on \((R,\infty)\), \(u_r(R)=1\), and \(u_r\) is the bounded minimal solution. The occupation density is a positive constant times \(u_r\) on this half-line. For nonnegative rates \(r_1\le r_2\) on \([R,\infty)\), direct coupling of the same Brownian paths gives the crucial comparison
\[
u_{r_1}(x)\ge u_{r_2}(x),\qquad x\ge R.
\]
This is a pointwise inequality, not an empirical approximation.

**2. Exact comparison family.** For real \(\beta\), take
\[
v_\beta(x)=\frac1{x\,t^\beta},\qquad t=\log(x/\ell),\qquad x>\ell e^e.
\]
Direct differentiation gives the exact identity
\[
\frac{x^2v_\beta''(x)}{v_\beta(x)}
=2+\frac{3\beta}{t}+\frac{\beta(\beta+1)}{t^2}.
\]
On a sufficiently distant half-line, \(v_\beta\) decreases to zero and \(Dv_\beta''/v_\beta\ge0\). Thus its normalized version is exactly the comparison function \(u_{r_\beta}\), where \(r_\beta=Dv_\beta''/v_\beta\).

For the first hypothesis, choose \(\beta_-<a/3<\beta_+\). At all sufficiently large \(x\),
\[
r_{\beta_-}(x)\le r(x)\le r_{\beta_+}(x),
\quad
C_-v_{\beta_+}(x)\le G(x)\le C_+v_{\beta_-}(x),
\]
with positive constants after normalization at a fixed large \(R\). Since \(\int_R^\infty v_\beta(x)\,dx=\int_{\log(R/\ell)}^\infty t^{-\beta}\,dt\), its convergence threshold is \(\beta>1\). Taking \(\beta\)'s strictly between \(1\) and \(a/3\) proves localization for \(a>3\); taking them strictly between \(a/3\) and \(1\) proves nonlocalization for \(a<3\). Letting both comparison exponents approach \(a/3\) gives the stated logarithmic density exponent.

**3. Both equality cases.** The first equality \(a=3\) requires finer comparison. For any real \(\gamma\) put
\[
w_\gamma(x)=\frac1{x\,t\,(\log t)^\gamma}.
\]
Its curvature is exactly
\[
\frac{x^2w_\gamma''}{w_\gamma}
=2+\frac3t+\frac{3\gamma}{t\log t}
+\frac2{t^2}+\frac{3\gamma}{t^2\log t}
+\frac{\gamma(\gamma+1)}{t^2(\log t)^2}.
\]
When \(a=3\) with the first error bound, choose \(0<\gamma<1\). The positive \(3\gamma/(t\log t)\) dominates the allowed error \(O(t^{-1-\delta})\), so eventually \(r(x)\le Dw_\gamma''/w_\gamma\). Comparison gives \(G(x)\ge Cw_\gamma(x)\). But \(\int w_\gamma\,dx=\int (\log t)^{-\gamma}\,dt/t\) diverges for \(\gamma\le1\). Therefore \(a=3\) does not localize.

**4. Second boundary and its equality.** For the second hypothesis, \(w_\gamma\) supplies the same upper/lower comparison as \(v_\beta\), because its leading adjustable term is \(3\gamma/(t\log t)\); the remainder \(O(t^{-2})\) is smaller than the allowed error separation. Since \(\int w_\gamma\,dx\) converges exactly for \(\gamma>1\), there is localization for \(b>3\) and nonlocalization for \(b<3\). Letting comparison exponents approach \(b/3\) proves the stated second logarithmic density exponent.

For \(b=3\), introduce the third comparator
\[
z_\eta(x)=\frac1{x\,t\,\log t\,(\log\log t)^\eta},\qquad 0<\eta<1.
\]
Writing \(z_\eta=x^{-1}f(t)\) and using \(x^2z_\eta''/z_\eta=2-3f'/f+f''/f\), one obtains
\[
\frac{x^2z_\eta''}{z_\eta}
=2+\frac3t+\frac3{t\log t}
+\frac{3\eta}{t\log t\log\log t}+O(t^{-2}).
\]
For fixed \(\eta\), the displayed positive correction dominates \(O(1/[t(\log t)^{1+\delta}])\). Hence \(G(x)\ge Cz_\eta(x)\) on a tail; its integral diverges because \(\eta<1\). Thus \(b=3\) is nonlocalizing.

**5. Stationary spatial-tail masses.** For \(a>3\), choose comparison exponents \(\beta_\pm>1\) arbitrarily close to \(a/3\) and integrate the two-sided density bounds. The integrals are multiples of \((\log(R/\ell))^{1-\beta_\pm}\), yielding the first tail-mass limit by squeezing. For \(b>3\), choose \(\gamma_\pm>1\) near \(b/3\), integrate \(w_\gamma\), and obtain powers of \(\log\log(R/\ell)\) in the appropriate transformed coordinate, yielding the second tail-mass limit as displayed. Symmetry doubles one-sided masses and does not affect logarithmic exponents.

## Verification

The included standalone \`checker.py\` uses symbolic differentiation to verify both exact comparator-curvature identities and the third comparator's leading terms. It also evaluates bounded residual expressions at explicit points as a basic implementation check. Running \`python checker.py\` with \`sympy==1.14.0\` reports PASS. The infinite-domain integrability criteria, comparison inequalities, and regenerative equivalence are proved above; no finite calculation is treated as their substitute. An explicitly regularized example is \(r_a(x)=D(1+x^2)^{-1}[2+a/\log(e^e+\sqrt{1+x^2})]\): the choices \(a=2\) and \(a=4\) have identical leading inverse-square tails but, respectively, do not admit and do admit a stationary probability.

## Relationship to prior work

Keidar and Reuveni (2026) establish the power-law localization boundary at inverse-square resetting and show the power-law stationary-tail exponent away from the critical coefficient. Their full main discussion and end matter cover the one- and higher-dimensional leading-order cases, but do not state the nested logarithmic threshold criteria at the exact one-dimensional critical coefficient. The rate-occupation equation and the inverse-square leading exponent are prior results, not claims of novelty here.

Keidar, Blumer, Hirshberg, and Reuveni (2025) establish general adaptive-resetting renewal and stationary-density methods. Pinsky (2018 preprint, 2020 publication) gives substantial general results on spatially dependent resetting and a positive-solution representation for first-passage observables, including comparison inequalities around inverse-square rates. Those general methods underpin the analysis; the new assessed statement is the explicit pair of critical nested correction thresholds, including their equality cases and corresponding stationary-tail mass exponents. The calculation also uses standard Sturm–Liouville/Feynman–Kac ideas; possible implicit derivation from broader critical-operator asymptotics remains a scientific originality risk.

## Limitations

The result is one-dimensional and assumes even bounded continuous hazards with the specified quantitative asymptotic remainders. It does not cover arbitrary oscillatory \(o(1/\log|x|)\) corrections, anisotropic higher-dimensional resets, or moments and mixing times. The logarithmic limits are logarithmic-slope asymptotics, not constant-factor equivalences. Equality for the general second boundary is decided only under its displayed remainder hypothesis. The classification has not received independent validation.

## References

1. T. D. Keidar and S. Reuveni, *Localization–Delocalization Transition in Diffusion with Adaptive Resetting*, arXiv:2608.27090v1 (2026-08-27), https://arxiv.org/abs/2608.27090.
2. T. D. Keidar, O. Blumer, B. Hirshberg, and S. Reuveni, *Adaptive Resetting for Informed Search Strategies and the Design of Non-equilibrium Steady-states*, arXiv:2409.14419v1 (2024-09-22); Nature Communications 16, 7259 (2025), https://www.nature.com/articles/s41467-025-62398-2.
3. R. G. Pinsky, *Diffusive Search with Spatially Dependent Resetting*, arXiv:1805.00320 (2018), Stochastic Processes and their Applications 130 (2020), https://arxiv.org/abs/1805.00320.
4. É. Roldán and S. Gupta, *Path-integral formalism for stochastic resetting: Exactly solved examples and shortcuts to confinement*, Physical Review E 96, 022130 (2017), arXiv:1703.10615, https://arxiv.org/abs/1703.10615.
