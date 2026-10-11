# Dual stationary nullcline calibration and activity defects in the Gray–Scott kinetics
## Finding
Consider the spatially homogeneous Gray–Scott reaction kinetics
\[
\dot u=F(1-u)-uv^2,
\qquad
\dot v=uv^2-(F+k)v,
\]
with
\[
F>0,
\qquad
k>0.
\]
Let \(\mu\) be any compactly supported invariant Borel probability measure whose support lies in
\[
(0,\infty)^2.
\]
Then the two concentration coordinates satisfy the exact conditional laws
\[
\boxed{
\mathbb E_\mu[v^2\mid u]
=
\frac{F(1-u)}{u}
}
\]
and
\[
\boxed{
\mathbb E_\mu[u\mid v]
=
\frac{F+k}{v}
}.
\]
Equivalently,
\[
\mathbb E_\mu[uv^2\mid u]=F(1-u),
\qquad
\mathbb E_\mu[uv\mid v]=F+k.
\]

The first law immediately forces the stationary support bound
\[
\boxed{0<u\le1}
\]
almost surely. It also gives the exact covariance calibration
\[
\boxed{
\operatorname{Cov}_\mu(u,uv^2)
=-F\operatorname{Var}_\mu(u)
},
\]
while the second gives
\[
\boxed{
\operatorname{Cov}_\mu(v,uv)=0
}.
\]

The conditional residuals are the kinetic speeds themselves:
\[
uv^2=F(1-u)-\dot u,
\qquad
uv=(F+k)+\frac{\dot v}{v}.
\]
Consequently
\[
\boxed{
\operatorname{Var}_\mu(uv^2)
=F^2\operatorname{Var}_\mu(u)
+\mathbb E_\mu[\dot u^2]
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(uv)
=
\mathbb E_\mu\!\left[
\left(\frac{\dot v}{v}\right)^2
\right]
}.
\]
More locally,
\[
\mathbb E_\mu[\dot u^2]
=
\mathbb E_\mu\!\left[u^2\operatorname{Var}_\mu(v^2\mid u)\right]
\]
and
\[
\mathbb E_\mu\!\left[
\left(\frac{\dot v}{v}\right)^2
\right]
=
\mathbb E_\mu\!\left[v^2\operatorname{Var}_\mu(u\mid v)\right].
\]
Either activity defect vanishes exactly for invariant measures supported on the positive equilibrium set.

There is also a parameter-exact support consequence. Put
\[
c=F+k,
\qquad
\Delta=1-\frac{4c^2}{F}.
\]
If a compact invariant probability measure supported in the strict positive quadrant exists, then
\[
\boxed{\Delta\ge0}.
\]
When this holds, define
\[
u_+=\frac{1+\sqrt\Delta}{2}.
\]
Every such stationary state satisfies
\[
\boxed{0<u\le u_+}
\]
and
\[
\boxed{v\ge\frac{c}{u_+}}
\]
almost surely.

The discriminant \(\Delta=0\), the corresponding saddle-node curve, and the positive equilibrium branches are classical Gray–Scott bifurcation structure. The new stationary content is the fiberwise nullcline calibration, its exact kinetic-activity defects, and the resulting invariant-support envelope for arbitrary compact stationary states.

## Assumptions and scope
The result concerns the homogeneous ordinary differential equations obtained from the standard Gray–Scott reaction-diffusion model by dropping diffusion.

Compact support inside the open positive quadrant implies that both coordinates are bounded and bounded away from zero. This permits the logarithmic test used in the \(v\)-coordinate. No ergodicity assumption is made.

Pearson's 1993 Gray–Scott paper writes the standard dimensionless reaction-diffusion equations and explicitly identifies the homogeneous kinetics by dropping the diffusion terms. The public preprint appeared on 17 April 1993, which is the structured source date used here.

The saddle-node locus
\[
F=4(F+k)^2
\]
and the positive equilibrium branches are established prior bifurcation facts. A later full same-object bifurcation study gives a global parameter map and proves Takens–Bogdanov and Bautin structure. A still later study gives a complete classification of phase portraits in the Poincaré disk. Those orbit-level facts are treated as prior and not claimed as new.

A Gray–Scott homoclinic/heteroclinic study lists \(34C20\) first among its Mathematics Subject Classification codes; that primary code is used here.

## Proof
Let \(L\) denote the generator of the homogeneous flow.

Fix a continuous function \(\phi\) on the compact \(u\)-projection of the support and choose an antiderivative \(H\) with
\[
H'(u)=\phi(u).
\]
Then
\[
LH
=
\phi(u)\left[F(1-u)-uv^2\right].
\]
Invariance gives
\[
\mathbb E_\mu\!\left[
\phi(u)\left(F(1-u)-uv^2\right)
\right]=0
\]
for every \(\phi\). Hence
\[
\mathbb E_\mu[uv^2\mid u]=F(1-u),
\]
and because \(u>0\),
\[
\mathbb E_\mu[v^2\mid u]=\frac{F(1-u)}u.
\]
The left side is nonnegative, so \(u\le1\) almost surely.

For the second coordinate, compact support in the positive quadrant gives a positive lower bound for \(v\). For any continuous \(\psi\) of \(v\), choose \(K\) with
\[
K'(v)=\frac{\psi(v)}v.
\]
Then
\[
LK
=
\psi(v)\left[uv-(F+k)\right].
\]
Stationarity yields
\[
\mathbb E_\mu[uv\mid v]=F+k,
\]
hence
\[
\mathbb E_\mu[u\mid v]=\frac{F+k}{v}.
\]

The covariance identities follow by conditioning. If
\[
Q=uv^2,
\]
then
\[
\operatorname{Cov}(u,Q)
=
\operatorname{Cov}(u,F(1-u))
=-F\operatorname{Var}(u).
\]
If
\[
P=uv,
\]
then its conditional mean given \(v\) is constant, so
\[
\operatorname{Cov}(v,P)=0.
\]

The first equation is
\[
Q=F(1-u)-\dot u.
\]
The same generator identity says
\[
\mathbb E[\dot u\mid u]=0.
\]
Therefore \(\dot u\) is orthogonal in \(L^2(\mu)\) to every function of \(u\), and
\[
\operatorname{Var}(Q)
=F^2\operatorname{Var}(u)+\mathbb E[\dot u^2].
\]
Conditioning the square of the residual also gives
\[
\mathbb E[\dot u^2]
=
\mathbb E\!\left[u^2\operatorname{Var}(v^2\mid u)\right].
\]

Likewise
\[
P=(F+k)+\frac{\dot v}{v}
\]
and
\[
\mathbb E\!\left[\frac{\dot v}{v}\middle|v\right]=0.
\]
Since the conditional mean of \(P\) is the constant \(F+k\),
\[
\operatorname{Var}(P)
=
\mathbb E\!\left[
\left(\frac{\dot v}{v}\right)^2
\right]
=
\mathbb E\!\left[v^2\operatorname{Var}(u\mid v)\right].
\]

If \(\mathbb E[\dot u^2]=0\), then \(u\) is constant on every complete support trajectory. The first equation then fixes \(v^2\), and positivity fixes \(v\), so the trajectory is an equilibrium. Conversely equilibrium-supported measures have zero defect. The same argument applies if the logarithmic \(v\)-speed defect vanishes: then \(v\) is constant, \(uv=F+k\), and positivity forces \(u\) constant. Thus either defect vanishes exactly on equilibrium-supported measures.

For the support envelope, let
\[
U=\operatorname*{ess\,sup}_\mu u.
\]
Then \(0<U\le1\). From
\[
\mathbb E[u\mid v]=\frac{F+k}{v}
\]
and \(u\le U\),
\[
v\ge\frac{F+k}{U}
\]
almost surely. Hence
\[
\mathbb E[v^2\mid u]
\ge
\frac{(F+k)^2}{U^2}.
\]
Combining this with the first conditional law gives, almost surely,
\[
\frac{F(1-u)}u
\ge
\frac{(F+k)^2}{U^2},
\]
so
\[
u
\le
\frac{FU^2}{FU^2+(F+k)^2}.
\]
Taking essential suprema yields
\[
U
\le
\frac{FU^2}{FU^2+(F+k)^2}.
\]
Because \(U>0\), this is equivalent to
\[
FU^2-FU+(F+k)^2\le0.
\]
Therefore the quadratic must have real roots, so
\[
\Delta=1-\frac{4(F+k)^2}{F}\ge0.
\]
Moreover \(U\) lies between those roots, hence in particular
\[
U\le u_+.
\]
Finally
\[
v\ge\frac{F+k}{U}\ge\frac{F+k}{u_+}.
\]
This proves the support envelope.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the two residual identities, the covariance formulas, both variance decompositions, and the algebra converting the essential-supremum inequality into the classical Gray–Scott discriminant.

It also checks an exact rational parameter choice in the positive-equilibrium region and verifies that the support-envelope boundary coincides with the upper positive equilibrium branch.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation quantifiers and the essential-supremum argument are analytic proofs and are not inferred from numerical trajectories.

## Relationship to prior work
Pearson's foundational Gray–Scott study gives the standard dimensionless reaction-diffusion equations and explicitly discusses the homogeneous ordinary differential equations obtained by dropping diffusion. It identifies the trivial equilibrium, the positive-equilibrium region, saddle-node loss, Hopf bifurcation, and periodic-orbit behavior.

Delgado, Hernández-Martínez, and Pérez-López give a full same-object bifurcation study of the homogeneous kinetics. Their complete public author text derives the positive equilibria and the saddle-node discriminant, proves a Takens–Bogdanov point and a Bautin point, and gives a global bifurcation map. Full-document searches found no `conditional`, `average`, `moment`, or `variance` formulation matching the present invariant-measure theorem.

Chen, Li, and Llibre later give a complete classification of phase portraits in the Poincaré disk for the rescaled cubic system
\[
\dot x=1-x-a x y^2,
\qquad
\dot y=-b y+a x y^2.
\]
The checked repository record and abstract concern global phase portraits and the bifurcation diagram. The complete postprint was listed as openly available but was not retrievable through the checked route, so it remains a residual comparison risk rather than being used for a blanket noncoverage statement.

The saddle-node condition and equilibrium branches are therefore explicitly treated as prior. The accepted contribution is the distribution-level statement that every compact positive stationary measure obeys two exact fiberwise nullcline calibrations, with the mismatch from deterministic nullclines measured exactly by kinetic activity.

## Limitations
The theorem is for compact invariant probability measures supported strictly inside the positive quadrant. It excludes the trivial boundary equilibrium \((1,0)\) and invariant measures touching \(v=0\), because the logarithmic \(v\)-test is then singular.

The parameter discriminant and equilibrium branches are classical prior structure, not originality claims.

The theorem concerns the homogeneous kinetics, not spatially varying reaction-diffusion invariant measures.

The complete 2021 phase-portrait postprint was not retrievable in the checked route. Its abstract states a complete orbit classification, so an equivalent support inequality could appear there even though no invariant-measure or conditional-moment statement is exposed in the checked material.

Because the generator proof is short, an equivalent weighted stationary identity could also remain in older unindexed chemical-kinetics literature.

## References
1. J. E. Pearson, “Complex Patterns in a Simple System,” *Science* 261, 189–192 (1993), arXiv:patt-sol/9304003, DOI 10.1126/science.261.5118.189.
2. J. Delgado, L. I. Hernández-Martínez, and J. Pérez-López, “Global Bifurcation Map of the Homogeneous States in the Gray–Scott Model,” *International Journal of Bifurcation and Chaos* 27 (2017), arXiv:1702.03353, DOI 10.1142/S0218127417300245.
3. T. Chen, S. Li, and J. Llibre, “Phase portraits and bifurcation diagram of the Gray-Scott model,” *Journal of Mathematical Analysis and Applications* 496, 124840 (2021), DOI 10.1016/j.jmaa.2020.124840.
4. J. K. Hale, L. A. Peletier, and W. C. Troy, “Exact Homoclinic and Heteroclinic Solutions of the Gray–Scott Model for Autocatalysis,” *SIAM Journal on Applied Mathematics*, DOI 10.1137/S0036139998334913.
