# Exact mean-height calibration and radial activity in the axisymmetric Langford torus model
## Finding
Consider the axisymmetric Langford torus model
\[
\dot x=(z-\beta)x-\omega y,
\qquad
\dot y=\omega x+(z-\beta)y,
\]
\[
\dot z
=
\lambda+\alpha z-\frac{z^3}{3}
-
(x^2+y^2)(1+\rho z),
\]
with
\[
\omega\ne0.
\]
Define
\[
R=x^2+y^2
\]
and
\[
G(z)=\lambda+\alpha z-\frac{z^3}{3}.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure whose support stays off the symmetry axis:
\[
R>0.
\]
Compactness then supplies a positive lower bound for \(R\) on the support.

The angular coordinate has constant speed
\[
\dot\theta=\omega,
\]
so its marginal under \(\mu\) is uniform on the circle.

The radial and height coordinates satisfy two exact conditional laws:
\[
\boxed{
\mathbb E_\mu[z\mid R]=\beta
}
\]
and
\[
\boxed{
\mathbb E_\mu[(1+\rho z)R\mid z]
=
G(z)
}.
\]

The first law implies
\[
\boxed{
\mathbb E_\mu[z]=\beta
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(R,z)=0
}.
\]
More generally, \(z-\beta\) is orthogonal to every square-integrable function of \(R\).

Since
\[
\dot R=2(z-\beta)R,
\]
the stationary height variance is exactly logarithmic radial activity:
\[
\boxed{
\operatorname{Var}_\mu(z)
=
\frac14
\mathbb E_\mu
\left[
\left(
\frac{\dot R}{R}
\right)^2
\right]
}.
\]

For the height equation, write
\[
W=(1+\rho z)R.
\]
Then
\[
W=G(z)-\dot z.
\]
The second conditional law is equivalent to
\[
\mathbb E_\mu[\dot z\mid z]=0,
\]
so the residual \(-\dot z\) is orthogonal to every function of \(z\). Therefore
\[
\boxed{
\operatorname{Var}_\mu(W)
=
\operatorname{Var}_\mu(G(z))
+
\mathbb E_\mu[\dot z^2]
}.
\]

Assume in addition that
\[
1+\rho\beta\ne0
\]
and
\[
R_*=
\frac{G(\beta)}{1+\rho\beta}>0.
\]
Then
\[
\operatorname{Var}_\mu(z)=0
\]
holds exactly for the invariant circular orbit
\[
z=\beta,
\qquad
R=R_*.
\]
Every other compact invariant state off the axis has
\[
\operatorname{Var}_\mu(z)>0.
\]
Because its mean height is exactly \(\beta\), it must assign positive mass to both half-spaces
\[
z<\beta
\quad\text{and}\quad
z>\beta.
\]

For Langford's axisymmetric numerical parameters
\[
\alpha=1,
\qquad
\beta=\frac7{10},
\qquad
\lambda=\frac35,
\qquad
\omega=\frac72,
\qquad
\rho=\frac14,
\]
one has
\[
G(\beta)=\frac{3557}{3000},
\qquad
1+\rho\beta=\frac{47}{40},
\]
and hence
\[
\boxed{
R_*=\frac{3557}{3525}
}.
\]
Thus every noncircular compact stationary torus or periodic state in this axisymmetric model has exact mean height
\[
\boxed{
\mathbb E_\mu[z]=\frac7{10}
}
\]
and its height variance is exactly one quarter of its mean-square logarithmic radial speed.

## Assumptions and scope
The theorem concerns the axisymmetric subfamily of the model used by Langford for numerical studies of torus bifurcations. In the original numerical study the symmetry-breaking coefficient is denoted separately and the first displayed torus is the axisymmetric case where that coefficient is zero.

The support condition
\[
R>0
\]
excludes invariant sets on the symmetry axis and makes logarithmic radial tests regular. No ergodicity assumption is imposed.

Langford's original torus-bifurcation work and later bifurcation-control studies establish the orbit geometry, torus bifurcations, phase locking, period doubling, and transitions toward strange attractors. Those results are prior work.

The 1984 model source is resolved to a month rather than a day in the checked public record. The structured source date therefore uses 30 May 2008, the earliest checked day-resolved public same-model source, rather than inventing a day in 1984.

A later same-system mathematical record classifies the Langford system first under \(34A34\), so that primary code is used here.

## Proof
Differentiate
\[
R=x^2+y^2.
\]
The rotational terms cancel:
\[
\dot R
=
2x\dot x+2y\dot y
=
2(z-\beta)R.
\]

Fix any continuous function \(\phi\) on the compact \(R\)-projection of the support. Because \(R\) is bounded away from zero, choose an antiderivative \(F\) with
\[
F'(R)=\frac{\phi(R)}{2R}.
\]
For the flow generator \(L\),
\[
LF
=
\phi(R)(z-\beta).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(R)(z-\beta)]=0
\]
for every \(\phi\). Therefore
\[
\mathbb E_\mu[z\mid R]=\beta.
\]

Taking \(\phi=1\) gives
\[
\mathbb E[z]=\beta,
\]
and taking the centered test \(R-\mathbb E[R]\) gives
\[
\operatorname{Cov}(R,z)=0.
\]

The pointwise identity
\[
\frac{\dot R}{R}=2(z-\beta)
\]
and the mean-height law give
\[
\operatorname{Var}(z)
=
\mathbb E[(z-\beta)^2]
=
\frac14
\mathbb E
\left[
\left(
\frac{\dot R}{R}
\right)^2
\right].
\]

Now take any continuous function \(\psi\) on the compact \(z\)-projection and choose an antiderivative \(K\) with
\[
K'(z)=\psi(z).
\]
Then
\[
LK
=
\psi(z)
\left[
G(z)-(1+\rho z)R
\right].
\]
Stationarity gives
\[
\mathbb E
\left[
\psi(z)
\left(
G(z)-(1+\rho z)R
\right)
\right]
=
0
\]
for every \(\psi\). Hence
\[
\mathbb E[(1+\rho z)R\mid z]=G(z).
\]

Since
\[
\dot z=G(z)-(1+\rho z)R,
\]
the same identity is
\[
\mathbb E[\dot z\mid z]=0.
\]
Thus \(\dot z\) is orthogonal in \(L^2(\mu)\) to every function of \(z\), including the centered quantity
\[
G(z)-\mathbb E[G(z)].
\]
Writing
\[
W=G(z)-\dot z
\]
gives
\[
\operatorname{Var}(W)
=
\operatorname{Var}(G(z))
+
\mathbb E[\dot z^2].
\]

Suppose
\[
\operatorname{Var}(z)=0.
\]
Then
\[
z=\beta
\]
on invariant support. The radial equation gives
\[
\dot R=0,
\]
so \(R\) is constant on every support trajectory. The height equation must also satisfy
\[
0=\dot z
=
G(\beta)-(1+\rho\beta)R,
\]
hence
\[
R=R_*.
\]
The remaining planar equations reduce to
\[
\dot x=-\omega y,
\qquad
\dot y=\omega x,
\]
so the support lies on the circular periodic orbit of radius
\[
\sqrt{R_*}.
\]
Continuous rotation at nonzero speed has the normalized orbit measure as its invariant probability measure.

Conversely, that circular orbit has
\[
z=\beta
\]
and zero height variance.

Any other compact invariant measure off the axis therefore has positive height variance. Since its mean height is \(\beta\), it cannot be supported in either closed half-space
\[
z\ge\beta
\quad\text{or}\quad
z\le\beta
\]
unless \(z=\beta\) almost surely. Thus it places positive mass on both sides of \(\beta\).

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies
\[
\dot R=2(z-\beta)R
\]
directly from the first two Langford equations.

It checks the two regression-residual identities
\[
z-\beta=\frac{\dot R}{2R}
\]
and
\[
(1+\rho z)R=G(z)-\dot z.
\]

It verifies the orthogonal variance decomposition abstractly and evaluates the standard axisymmetric circular radius exactly:
\[
R_*=\frac{3557}{3525}.
\]

The stored checker output is `VERIFY_OK`.

The conditional-expectation quantifiers, Haar angular marginal, equality classification, and two-sided height statement are analytic proofs and are not inferred from finite numerical trajectories.

## Relationship to prior work
Langford's 1979 work develops the interaction of a steady-state bifurcation and a Hopf bifurcation and proves the appearance of doubly periodic torus solutions in a broad normal-form setting.

The complete 1984 numerical study specializes that program to a three-dimensional model. It writes the model equations, identifies the axisymmetric torus at zero symmetry-breaking coefficient, and then follows phase locking, period doubling, chaotic bands, and thickened tori as symmetry is broken. The complete searchable text contains no `average`, `conditional`, or `moment` formulation and no statistical-variance theorem.

A 2008 same-model study analyzes bifurcation characteristics and control of periodic solutions changing into invariant tori. Its focus is bifurcation structure and nonlinear control rather than invariant-measure calibration.

A later perturbation study treats Langford equations under admissible perturbations and is classified primarily under nonlinear ordinary differential equations. It does not implication-wise determine the two stationary conditional laws here.

A recent published record for a different generalized Hopf–Langford-type system derives an exact amplitude reduction and uses it to obstruct a claimed Neimark–Sacker torus. That system and theorem concern a different parameterized vector field; they do not imply the conditional height and weighted radial-load laws of the 1984 axisymmetric model.

The present theorem supplies a statistical invariant across the entire off-axis compact recurrent family: all such states have the same exact mean height \(\beta\), and noncircular radial breathing is measured exactly by height variance.

## Limitations
The theorem is restricted to the axisymmetric subfamily. The symmetry-breaking term used by Langford to generate phase locking and strange attractors changes the height equation and is outside the claim.

The support must stay off the symmetry axis.

The circular-orbit equality classification additionally assumes
\[
1+\rho\beta\ne0
\]
and
\[
G(\beta)/(1+\rho\beta)>0.
\]

The result determines conditional means and selected variances, not the full invariant distribution or torus rotation number.

Because the logarithmic radial calculation is short, an equivalent mean-height observation could remain in older unindexed torus-bifurcation literature.

## References
1. W. F. Langford, “Periodic and Steady-State Mode Interactions Lead to Tori,” *SIAM Journal on Applied Mathematics* 37, 22–48 (1979), DOI 10.1137/0137003.
2. W. F. Langford, “Numerical Studies of Torus Bifurcations,” in *Numerical Methods for Bifurcation Problems*, International Series of Numerical Mathematics 70, 285–295 (1984), DOI 10.1007/978-3-0348-6256-1_19.
3. S.-H. Liu, J.-S. Tang, J.-Q. Qin, and X.-B. Yin, “Bifurcation analysis and control of periodic solutions changing into invariant tori in Langford system,” *Chinese Physics B* 17, 1691–1697 (2008), DOI 10.1088/1674-1056/17/5/026.
4. E. V. Musafirov, “Perturbations of the Lanford system which do not change the reflecting function,” *International Journal of Bifurcation and Chaos* 27 (2017), DOI 10.1142/S0218127417501541.
