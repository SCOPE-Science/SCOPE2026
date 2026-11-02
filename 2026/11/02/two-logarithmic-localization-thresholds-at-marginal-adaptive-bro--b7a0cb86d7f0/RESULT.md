# Two logarithmic localization thresholds at marginal adaptive Brownian resetting

## Finding

**Theorem (sharp logarithmic and iterated-logarithmic stationary boundaries).** Fix an integer \(d\ge1\) and diffusivity \(D>0\). Let \(X_t\) be Brownian motion on \(\mathbb R^d\) with generator \(D\Delta\), returned instantaneously to the origin at a state-dependent exponential hazard \(\kappa(|X_t|)\). Suppose \(\kappa:[0,\infty)\to(0,\infty)\) is continuous and locally bounded, and, for some constants \(b,c\in\mathbb R\),
\[
\kappa(\rho)=\frac{D}{\rho^2}\left(2d+\frac{b}{\log \rho}+\frac{c}{\log\rho\,\log\log\rho}+O((\log\rho)^{-2})\right),\qquad \rho\longrightarrow\infty.
\]
The big-O is a uniform real-valued radial bound, not an assumption of differentiability of the error. Let \(G(x)\) be the occupation-density Green function for diffusion started at the origin and killed at hazard \(\kappa\), up to its first killing time. Then there is a constant \(C\in(0,\infty)\), dependent on the complete hazard, such that
\[
G(x)\sim C|x|^{-d}(\log|x|)^{-b/(d+2)}(\log\log|x|)^{-c/(d+2)}\qquad (|x|\to\infty).
\]
The reset diffusion admits a stationary **probability** distribution precisely when
\[
\boxed{\quad b>d+2\quad\text{or}\quad [b=d+2\ \text{and}\ c>d+2].\quad}
\]
In that case the stationary density is \(G/\int_{\mathbb R^d}G\), and the stationary law is unique. Otherwise its regenerative occupation measure has infinite total mass, so there is no stationary probability law. In particular, the leading marginal rate \(2dD/\rho^2\) alone does **not** determine localization: the first and second logarithmic corrections settle its boundary.

## Assumptions and scope

Brownian trajectories are continuous, resetting is instantaneous to a fixed origin, and conditional survival along an unreset trajectory of length \(t\) equals \(\exp(-\int_0^t\kappa(|X_s|)\,ds)\). Diffusive noise, hazard clocks, and successive excursions are independent in the usual killed-process construction. The rate is radial and continuous and may take arbitrary strictly positive values on compact sets. The asymptotic statement is required only outside some radius \(\rho_0>e^e\). All limits concern fixed \(d,D,b,c\) and one fixed hazard function, not a uniform parameter family. The result addresses existence of an invariant probability, not the precise mixing rate or correlations of the stationary process.

## Proof

**1. Radial killed Green equation.** The unnormalized occupation density is the minimal nonnegative Green solution of
\[
D\Delta G-\kappa G=-\delta_0.
\]
Away from the origin, spherical symmetry reduces this to \(D[G''+(d-1)G'/\rho]=\kappa G\). Standard local Green-kernel theory applies because \(\kappa\) is nonnegative and locally bounded; the singularity at the source has the Laplacian type (bounded with a derivative jump in dimension one, logarithmic in dimension two, and a Newtonian pole for larger dimensions). We determine the positive solution with vanishing radial flux at infinity and normalize its source flux to one.

**2. Exact logarithmic transformation.** Put \(z=\log\rho\), \(a=d+2\), and \(G(\rho)=\rho^{-d}h(z)\). Direct differentiation, with no approximation, gives
\[
\rho^{d+2}\left[G''+\frac{d-1}{\rho}G'\right]=h''-a h'+2dh.
\]
Consequently, for sufficiently large \(z\),
\[
h''-a h'-q(z)h=0,\qquad q(z)=\frac b z+\frac c{z\log z}+O(z^{-2}).
\]
Set \(\beta=b/a\), \(\gamma=c/a\), \(g(z)=z^{-\beta}(\log z)^{-\gamma}\), and \(h=gu\). Since
\[
\frac{g'}{g}=-\frac\beta z-\frac\gamma{z\log z},\qquad
f(z):=\frac{g''}{g}-a\frac{g'}{g}-q(z)=O(z^{-2}),
\]
the exact equation for \(u\) is
\[
u''-A(z)u'+f(z)u=0,\qquad A(z)=a-2g'(z)/g(z)=a+O(z^{-1}).
\]

**3. The unique slow positive branch.** For a sufficiently large \(z_0\), let \(A(z)>a/2\) for \(z\ge z_0\). Consider the Volterra integral equation
\[
u(z)=1-\int_z^\infty\int_s^\infty
\exp\left(-\int_s^t A(w)\,dw\right)f(t)u(t)\,dt\,ds.
\]
Its associated operator on bounded continuous functions has norm at most \(\frac2a\int_{z_0}^\infty|f(t)|\,dt=O(z_0^{-1})\). It is therefore a contraction for large \(z_0\), and its unique solution obeys
\[
u(z)=1+O(z^{-1}),\qquad u'(z)=O(z^{-2}).
\]
Differentiation of the integral equation recovers the ODE. Thus the positive slow solution satisfies
\[
G_{\mathrm{slow}}(\rho)=\rho^{-d}(\log\rho)^{-\beta}(\log\log\rho)^{-\gamma}[1+O((\log\rho)^{-1})].
\]
By reduction of order, a second independent solution for \(h\) is \(h_{\mathrm{slow}}(z)\int^z e^{at}h_{\mathrm{slow}}(t)^{-2}\,dt\), which behaves asymptotically as \(a^{-1}e^{az}/h_{\mathrm{slow}}(z)\). The corresponding spatial branch grows like \(\rho^2(\log\rho)^\beta(\log\log\rho)^\gamma\) and cannot be the tail of a positive occupation density with finite source mass.

**4. Positive inward extension and source normalization.** For all sufficiently large \(\rho\), the slow solution is positive and strictly decreasing because its leading logarithmic derivative is \(-d/\rho+O(1/(\rho\log\rho))\). Continue it toward the origin using the nonsingular radial ODE on each compact annulus. For \(F(\rho)=\rho^{d-1}G'(\rho)\),
\[
F'(\rho)=\frac{\kappa(\rho)}{D}\rho^{d-1}G(\rho)>0
\]
wherever \(G>0\). Since \(F<0\) at large radius, inward continuation keeps \(F<0\), \(G'<0\), and \(G>0\); it cannot cross zero or encounter a finite-radius blow-up. Local boundedness of \(\kappa\) gives the classical fundamental-solution singularity near zero and a finite strictly negative limit \(F(0+)\). For \(d=1\), the radial derivative is interpreted on the positive half-line and the source flux includes both sides. Multiplying by a positive constant sets
\[
-D|\mathbb S^{d-1}|F(0+)=1,
\]
which is exactly the Green source strength. The asymptotic slow branch has \(F(\infty)=0\). Integrating the radial equation thus gives \(\int\kappa G\,dx=1\), so the killed trajectory is absorbed with probability one and the Green solution is the physical occupation potential. In particular, \(C>0\).

**5. Exact integrability criterion and stationary equivalence.** The mass in a far radial shell is asymptotic to
\[
|\mathbb S^{d-1}|C\,\rho^{-1}(\log\rho)^{-\beta}(\log\log\rho)^{-\gamma}\,d\rho.
\]
With \(z=\log\rho\), the tail mass is comparable to \(\int^\infty z^{-\beta}(\log z)^{-\gamma}\,dz\). The integral converges if and only if \(\beta>1\), or \(\beta=1\) and \(\gamma>1\). The local Green singularity is integrable at zero in every finite dimension, completing the announced criterion. Each reset begins an independent excursion of duration \(\tau\), with \(\mathbb E\tau=\int G\,dx\). The regenerative stationary-probability theorem gives density \(G/\mathbb E\tau\) exactly when that mean is finite; for infinite mean the recurrent regenerative process has no invariant probability. Uniqueness follows because killing/resetting provides a common regenerative atom accessible almost surely from every starting point. \(\square\)

## Verification

The radial conjugation and residual are exact derivative identities. The Volterra kernel has positive exponential decay for \(a=d+2>0\) and remainder \(f(z)=O(z^{-2})\), providing a convergent analytic fixed-point argument; numerical tail fitting is not used. The two integrability boundaries follow from the classical integral test for \(\int z^{-\beta}(\log z)^{-\gamma}\,dz\). An independent short symbolic identity checker is included as `verify.py`; it tests the radial conjugation formula in representative dimensions, and is **not** a substitute for the infinite-domain Volterra and regenerative arguments.

## Relationship to prior work

Keidar and Reuveni (2026, arXiv:2608.27090v1) derive the leading inverse-square localization boundary at \(\kappa(\rho)\sim 2dD/\rho^2\), as well as the occupation-measure approach; the present theorem does not claim that leading boundary or renewal representation. Instead it resolves the previously undecided leading-critical case under two specified logarithmic correction scales, and it determines the exact dimension-dependent secondary thresholds. Keidar, Blumer, Hirshberg and Reuveni (2024, arXiv:2409.14419) study adaptive resetting and engineered nonequilibrium steady states but do not state these secondary thresholds. Pinsky (2018, arXiv:1805.00320) considers spatially dependent resetting for first-passage search rather than this stationary normalization question. Ishige, Kabeya and Ouhabaz (2016, arXiv:1602.04172) treat radial inverse-square Schrödinger operators; their explicit power-asymptotic hypothesis on the coefficient error does not directly cover \(1/\log\rho\) tails. More general asymptotic-ODE methods remain a possible source of implicit overlap; no broad priority claim is made.

## Limitations

This is a theorem for continuous radial, locally bounded, positive rates and diffusion with a fixed reset point. The asymptotic remainder must be \(O((\log\rho)^{-2})\) in the displayed expansion; an uncontrolled \(o(1/(\log\rho\log\log\rho))\) remainder at the double threshold can produce further iterated-log boundaries. No spectral-gap, mixing-time, finite-time crossover, anisotropic reset-rate, or moving-reset-point conclusion is established. Independent literature-wide priority adjudication has not been performed.

## References

1. O. Keidar and S. Reuveni, *Localization–Delocalization Transition in Diffusion with Adaptive Resetting* (2026), arXiv:2608.27090v1, https://arxiv.org/abs/2608.27090.
2. O. Keidar, D. Blumer, B. Hirshberg, and S. Reuveni, *Adaptive Resetting for Informed Search Strategies and the Design of Non-equilibrium Steady-states* (2024), arXiv:2409.14419, https://arxiv.org/abs/2409.14419.
3. R. G. Pinsky, *Diffusive Search with Spatially Dependent Resetting* (2018), arXiv:1805.00320, https://arxiv.org/abs/1805.00320.
4. K. Ishige, Y. Kabeya, and E. M. Ouhabaz, *Heat kernel of a Schrödinger operator with inverse square potential* (2016), arXiv:1602.04172, https://arxiv.org/abs/1602.04172.
