# Two-dimensional inertial resetting cusps, an exact directional dipole, and a cubic mixture crossover

## Finding

Consider an inertial active Brownian particle in two spatial dimensions, returned to the origin at independent Poisson times. Each reset also restores a fixed propulsion heading, while its velocity is either set to zero or sampled from a Maxwell (isotropic Gaussian) distribution. The **joint local stationary-density theorem** below determines the singularity under this experimentally distinct pair of velocity-restoration protocols, the first orientation-dependent term, and the singular crossover when zero-velocity resets become rare.

Let \(f_p\) denote the stationary density of its planar position, let \(e_1=(1,0)\), and put
\[
 c=\frac{2}{3M^2},\quad
 A=\frac{R\Gamma(2/3)}{3\pi(2c)^{1/3}},\quad
 B=\frac{R\mathrm{Pe}\,M}{4\pi},\quad
 C=\frac{R}{2\sqrt{2\pi}\,w}.
\]
**Theorem.** For every fixed \(M,R,w>0\), \(\mathrm{Pe}\ge0\), and \(0\le p\le1\), uniformly over unit vectors \(e\in\mathbb S^1\),
\[
 f_p(se)=pA s^{-4/3}+
 \bigl[pB(e\cdot e_1)+(1-p)C\bigr]s^{-1}
 +pO(s^{-2/3})+(1-p)O(1+|\log s|),\qquad s\downarrow0.
\]
The constants in the error terms may depend on the four fixed physical parameters, but not on \(p\) or \(e\). In particular, the zero-velocity cusp is isotropic at leading order but has an explicit first angular (dipole) correction, whereas Maxwellian velocity restoration changes the leading radial singularity from exponent \(-4/3\) to exponent \(-1\).

There is an **exact cubic crossover scale**: for every fixed \(\kappa>0\), uniformly in \(e\),
\[
 \lim_{p\downarrow0}p^3 f_p(\kappa p^3 e)
 =A\kappa^{-4/3}+C\kappa^{-1},\qquad
 \lim_{p\downarrow0}p^{-3}\Pr_p\{|X|\le\kappa p^3\}
 =3\pi A\kappa^{2/3}+2\pi C\kappa.
\]
At pure zero-velocity resetting \(p=1\), the conditional direction within a small disk satisfies
\[
 \mathbb E_1\left[\frac{X}{|X|}\,\middle|\,0<|X|\le\varepsilon\right]
 =\frac{B}{3A}\varepsilon^{1/3}e_1+o(\varepsilon^{1/3})
 =\frac{\mathrm{Pe}\,M^{1/3}}{48^{1/3}\Gamma(2/3)}
 \varepsilon^{1/3}e_1+o(\varepsilon^{1/3}).
\]
These assertions characterize a planar *density*, not a one-coordinate marginal or the radial probability density (which includes a Jacobian).

## Assumptions and scope

Work in the nondimensional parameters of Patel–Shee (2026). Between resets the stochastic differential equations are
\[
 dX_t=V_t\,dt,\qquad
 M\,dV_t=(-V_t+\mathrm{Pe}\,U_t)\,dt+\sqrt2\,dB_t,\qquad
 d\theta_t=\sqrt2\,dW_t,\quad U_t=(\cos\theta_t,\sin\theta_t),
\]
where \(B_t\) is a planar standard Brownian motion, \(W_t\) is independent scalar Brownian motion, \(M,R,w>0\), and \(\mathrm{Pe}\ge0\). At independent Poisson times with rate \(R\), replace \((X,\theta)\) by \((0,0)\); independently set \(V=0\) with probability \(p\), and otherwise draw \(V\sim N(0,w^2 I_2)\). All reset choices are independent of the noise and of preceding excursions. This includes the all-zero-velocity reset studied by Patel–Shee as \(p=1\), and a Maxwell-restarted velocity variant as \(p=0\). Only the stationary **position** law is asserted, and all asymptotics keep the physical parameters fixed while the spatial radius tends to zero.

The regenerative process possesses a unique invariant probability distribution, because the entire state is refreshed at each Poisson event and the excursion-age distribution at stationarity is exponential. Each age \(t>0\) has a strictly positive translational Gaussian variance, so its stationary position marginal has an absolutely continuous density on \(\mathbb R^2\), smooth away from \(X=0\). The density at the single point \(X=0\) may be assigned any value and is not an atom.

## Proof

**1. Exact renewal kernel.** Set
\[
 K(t)=M(1-e^{-t/M}),\qquad
 v(t)=2\int_0^t(1-e^{-u/M})^2\,du,
\]
\[
 H_t=\mathrm{Pe}\int_0^t(1-e^{-(t-u)/M})U_u\,du,
 \qquad\phi_v(y)=\frac{1}{2\pi v}\exp\left(-\frac{|y|^2}{2v}\right).
\]
Solving the linear inertial equation and integrating its velocity yields \(X_t=K(t)V_0+H_t+G_t\), with \(G_t\sim N(0,v(t)I_2)\), independent of \(V_0\) and the angular path. Thus, writing \(v_w(t)=v(t)+w^2K(t)^2\), the renewal representation is exact:
\[
 f_p(x)=p f_0(x)+(1-p)f_w(x),\quad
 f_0(x)=R\int_0^\infty e^{-Rt}\mathbb E[\phi_{v(t)}(x-H_t)]\,dt,
\]
\[
 f_w(x)=R\int_0^\infty e^{-Rt}\mathbb E[\phi_{v_w(t)}(x-H_t)]\,dt.
\]
For each \(x\ne0\), these integrals converge. The large-age portions are bounded by Gaussian normalization, positive finite variance on \(t\ge\delta>0\), and the exponential renewal weight. Exponential regeneration establishes uniqueness of the invariant distribution.

**2. Precise short-age information.** Taylor expansion, with constants uniform on a small fixed age interval, gives
\[
 v(t)=c t^3(1+O(t)),\qquad
 K(t)=t(1+O(t)),\qquad
 v_w(t)=w^2t^2(1+O(t)),\qquad
 c=\frac{2}{3M^2}.
\]
Since \(\mathbb E|e^{i\theta_u}-1|\le C\sqrt u\) and \(|U_u|=1\),
\[
 H_t=\frac{\mathrm{Pe}}{2M}t^2 e_1+E_t,\qquad
 \mathbb E|E_t|\le C t^{5/2},\quad |H_t|\le C t^2.
\]
The deterministic error from the exponential inertial kernel is \(O(t^3)\), which is bounded by the displayed \(O(t^{5/2})\) for small \(t\). These bounds hold at nonzero angular diffusivity, not merely when heading is frozen.

**3. Zero-velocity branch.** Fix \(x=se\). The elementary planar Gaussian integral gives
\[
 R\int_0^\infty\phi_{ct^3}(se)\,dt
 =\frac{R s^{-4/3}}{2\pi c}\int_0^\infty u^{-3}
 \exp\!\left(-\frac{1}{2cu^3}\right)du
 =A s^{-4/3};
\]
we used \(t=s^{2/3}u\) and \(\int_0^\infty u^{-3}e^{-1/(2cu^3)}du=(2c)^{2/3}\Gamma(2/3)/3\).

For the first positional drift correction, the identity
\[
 \phi_v(se-H_t)=\phi_v(se)
 \exp\!\left(\frac{s e\cdot H_t}{v}-\frac{|H_t|^2}{2v}\right)
\]
shows that the first nonconstant term is \(s e\cdot\mathbb E H_t/v\). Replacing the leading quantities by their short-age expressions gives exactly
\[
 \frac{R}{2\pi c}\frac{\mathrm{Pe}}{2Mc}
 (e\cdot e_1)s\int_0^\infty t^{-4}
 \exp\!\left(-\frac{s^2}{2ct^3}\right)dt
 =\frac{R\mathrm{Pe}M}{4\pi}(e\cdot e_1)s^{-1},
\]
using \(\int_0^\infty u^{-4}e^{-1/(2cu^3)}du=2c/3\).

Here are explicit error controls, needed for a genuine two-term asymptotic. For \(t\le s^{3/4}\), the Gaussian cutoff is exponentially small in \(s^{-1/4}\): the bound \(|H_t|\le Ct^2\) ensures \(|se-H_t|\ge s/2\) for small \(s\). For \(s^{3/4}\le t\le\delta\), the first-order exponential expansion has a remainder bounded by a constant times \((s/t)^2+t\) after multiplication by a Gaussian cutoff \(\exp[-c_0s^2/t^3]\). The leading-variance correction and the reset-age weight contribute a relative \(O(t)\). The orientation error contributes at most \(Cs t^{-1/2}\) relative to the Gaussian prefactor, by \(\mathbb E|E_t|=O(t^{5/2})\). Consequently the integrated absolute remainders are bounded by
\[
 C\int_0^\delta t^{-3}e^{-c_0s^2/t^3}
 \left(t+\frac{s^2}{t^2}+\frac{s}{\sqrt t}\right)dt
 =O(s^{-2/3}).
\]
The tails \(t\ge\delta\) of the actual and comparison integrals contribute \(O(1)\), uniformly in direction. Thus
\[
 f_0(se)=A s^{-4/3}+B(e\cdot e_1)s^{-1}+O(s^{-2/3}).
\]

**4. Maxwell-velocity branch.** The dominant small-age positional variance is \(w^2t^2\), and the active drift is still \(O(t^2)\). The same argument, now using \(t=su\), gives
\[
 R\int_0^\infty\phi_{w^2t^2}(se)\,dt
 =\frac{R s^{-1}}{2\pi w^2}\int_0^\infty u^{-2}
 e^{-1/(2w^2u^2)}du
 =C s^{-1}.
\]
On \(t\le\delta\), the variance and exponential reset-weight errors are relative \(O(t)\), the linear drift contribution is relative \(O(s)\), and the quadratic drift contribution is relative \(O(t^2)\). Integrating \(t^{-2}\exp(-c_0s^2/t^2)\) against these errors gives at most \(O(1+|\log s|)\). The contribution from \(t\ge\delta\) is \(O(1)\), proving
\[
 f_w(se)=C s^{-1}+O(1+|\log s|).
\]
Exact convex mixing completes the asserted planar-density expansion, including its uniformity in \(p\) and \(e\).

**5. Cubic mixture and angular observables.** Substitute \(s=\kappa p^3\) into the uniform expansion and multiply by \(p^3\). The leading zero-velocity and Maxwell contributions both remain of order one; the dipole and all errors vanish. To obtain the disk probability, integrate over polar area \(s\,ds\,d\vartheta\), noting \(\int_{\mathbb S^1}(e\cdot e_1)\,de=0\); the two leading contributions to a disk of radius \(\varepsilon\) are \(3\pi pA\varepsilon^{2/3}\) and \(2\pi(1-p)C\varepsilon\), and the integrated remainders are of smaller order under \(\varepsilon=\kappa p^3\). Finally, for \(p=1\) the vector angular numerator is \(\pi B\varepsilon e_1+o(\varepsilon)\), because \(\int_{\mathbb S^1}e(e\cdot e_1)\,de=\pi e_1\); divide by \(3\pi A\varepsilon^{2/3}+o(\varepsilon^{2/3})\). Direct simplification yields the stated universal angular coefficient. All convergence is uniform in angular direction. \(\square\)

## Verification

The accompanying `verify.py` uses only the exact finite-time Gaussian variance and the derivative at zero propulsion of the *rotationally diffusing* angular forcing, for which \(\mathbb E[U_t]=e^{-t}e_1\). It independently integrates the finite-age renewal kernels and checks convergence of three rescaled quantities: the zero-velocity passive cusp \(A\), the active first directional-response coefficient \(B/\mathrm{Pe}=RM/(4\pi)\), and the Maxwell cusp \(C\). For \(M=1.3\), \(R=1.4\), \(w=0.8\), and radii \(0.01,0.003,0.001,0.0003,0.0001\), all three relative errors decrease monotonically; at the smallest radius they are less than \(1.2\%\). These finite numerical calculations are corroboration only: the proof above establishes the limit for every permitted parameter value and finite \(\mathrm{Pe}\).

Run `python verify.py` with Python 3, NumPy, and SciPy. The only external dependencies are standard numerical packages. In particular, the code does not approximate angular Brownian sample paths to establish the theorem.

## Relationship to prior work

Patel and Shee (arXiv:2602.21134v1, publicly posted 24 February 2026) study exactly the two-dimensional inertial active-particle stochastic differential equation and complete zero-velocity/orientation resetting. Their analysis supplies steady-state second- and fourth-order moments and kurtosis phase diagrams, but not the local planar-density asymptotics or the first angular coefficient. The derivation here uses their model, not their moment formulas.

Franke and Sokolov (2026) analyze two distinct velocity-restoration protocols for a **one-dimensional** underdamped passive Brownian particle and prove different singularities of its one-coordinate positional distribution: a power singularity for zero velocity and a logarithmic singularity for Maxwell resetting. The two-dimensional planar-density exponents, exact angular dipole for persistent propulsion, and cubic crossover between protocols do not follow by simply renaming their one-dimensional density. However, their Gaussian age-mixture technique is a direct methodological antecedent.

Kumar, Sadekar and Basu (2020) investigate **overdamped** planar active Brownian motion under resetting and its one-coordinate marginal distributions. Shankari and Sahoo (arXiv:2509.18515, 2025) study an inertial **one-dimensional active Ornstein–Uhlenbeck** model, including renewal position distributions. These are relevant broader contexts with different dynamical kernels and/or dimension, not direct instances of the stated theorem. The standard renewal identity is not claimed as new.

## Limitations

The result is local to the reset origin and is for finite fixed inertia and positive translational thermal noise. It does not characterize large-distance tails, finite-time approach to stationarity, the entire position density, or non-Poisson reset schedules. The mixture reset is an explicit new protocol, not a claim that the source papers used that mixture. A known general small-time heat-kernel or Gaussian-mixture theorem might implicitly imply some power exponents, and wider literature may contain overlapping anisotropic terms; this is a residual originality risk. No independent external audit has been performed. Numerical checks are not substitutes for the asymptotic estimates.

## References

1. M. Patel and A. Shee, *Controlling inertial active Brownian motion via stochastic resetting*, arXiv:2602.21134v1 (24 February 2026), https://arxiv.org/abs/2602.21134.
2. H. Franke and I. M. Sokolov, *Resetting of underdamped Brownian motion*, Physical Review E 113, 064125 (11 June 2026), https://doi.org/10.1103/qyl8-6q9h.
3. V. Kumar, O. Sadekar and U. Basu, *Active Brownian motion in two dimensions under stochastic resetting*, Physical Review E 102, 052129 (2020), https://doi.org/10.1103/PhysRevE.102.052129.
4. U. Shankari and M. Sahoo, *Active Ornstein–Uhlenbeck particle under stochastic resetting*, arXiv:2509.18515v1 (23 September 2025), https://arxiv.org/abs/2509.18515.
