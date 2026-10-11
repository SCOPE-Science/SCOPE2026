# Stationary temperature circle and heightwise convection calibration in the Glukhovsky–Dolzhansky flow
## Finding
Consider the Glukhovsky–Dolzhansky system
\[
\dot x=-\sigma x+\zeta z+\alpha yz,
\qquad
\dot y=\rho-y-xz,
\qquad
\dot z=-z+xy,
\]
with
\[
\sigma>0,\qquad
\zeta>0,\qquad
\alpha>0,\qquad
\rho>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Then the three coordinate layers obey the exact stationary regressions
\[
\boxed{
\mathbb E_\mu[\zeta z+\alpha yz\mid x]=\sigma x
},
\]
\[
\boxed{
\mathbb E_\mu[xz\mid y]=\rho-y
},
\]
and
\[
\boxed{
\mathbb E_\mu[xy\mid z]=z
}.
\]

Writing
\[
m=\mathbb E_\mu[y],
\]
the last two equations of the flow also force the exact parameter-only second-moment shell
\[
\boxed{
\mathbb E_\mu\!\left[
\left(y-\frac{\rho}{2}\right)^2+z^2
\right]
=
\frac{\rho^2}{4}
}.
\]
Equivalently,
\[
\boxed{
\operatorname{Var}_\mu(y)+\mathbb E_\mu[z^2]
=
m(\rho-m)
}.
\]

Consequently,
\[
0<m\le\rho.
\]
Moreover,
\[
m=\rho
\]
holds exactly for the equilibrium atom
\[
\delta_{(0,\rho,0)}.
\]
Thus every other compact stationary state satisfies
\[
\boxed{
0<m<\rho
}.
\]

The heightwise law
\[
\mathbb E_\mu[xy\mid z]=z
\]
has an exact dynamical residual because
\[
xy-z=\dot z.
\]
Conditional orthogonality therefore yields
\[
\boxed{
\operatorname{Var}_\mu(xy)
=
\operatorname{Var}_\mu(z)
+
\mathbb E_\mu[\dot z^2]
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(z,xy)
=
\operatorname{Var}_\mu(z)
}.
\]

The speed defect
\[
\mathbb E_\mu[\dot z^2]
\]
vanishes exactly for invariant measures supported on equilibria.

Hence every compact stationary state that is not supported on equilibria has
\[
\operatorname{Var}_\mu(z)>0,
\qquad
\mathbb E_\mu[\dot z^2]>0,
\]
and its height–convection correlation obeys
\[
\boxed{
0<
\operatorname{Corr}_\mu(z,xy)
<
1
}.
\]
More precisely,
\[
\boxed{
\operatorname{Corr}_\mu(z,xy)
=
\left(
1+
\frac{\mathbb E_\mu[\dot z^2]}
{\operatorname{Var}_\mu(z)}
\right)^{-1/2}
}.
\]

For example, at
\[
\rho=15,
\]
a parameter value used in modern studies of hidden and transient dynamics, every compact stationary state lies on
\[
\mathbb E\!\left[(y-7.5)^2+z^2\right]=56.25.
\]
This identity applies separately to coexisting invariant states; no ergodicity or uniqueness assumption is required.

## Assumptions and scope
The result concerns the classical integer-order Glukhovsky–Dolzhansky model with strictly positive parameters. Compact support guarantees integrability of the polynomial observables and one-coordinate antiderivative tests used below.

The model was introduced in 1980 for convection in a rotating ellipsoidal cavity. The checked 1980 bibliographic evidence did not resolve a day-level public date. The structured date therefore uses 18 May 2015, the earliest checked day-resolved public preprint that contains the Glukhovsky–Dolzhansky model explicitly, rather than inventing a day for the older source.

A mathematical bibliographic record for a same-object Lyapunov-dimension paper lists MSC \(34D45\), \(37C45\), and \(37C70\), with \(34D45\) first. The present result is assigned primary MSC \(34D45\).

No ergodicity assumption is imposed. The formulas apply to equilibrium atoms, periodic-orbit measures, compact chaotic invariant measures, and convex mixtures.

## Proof
Let \(L\) denote the generator of the flow.

Take a continuous function \(\phi\) on the compact \(x\)-range of the support and choose a continuously differentiable antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
\phi(x)
\left(
-\sigma x+\zeta z+\alpha yz
\right).
\]
Invariance gives
\[
\mathbb E_\mu
\left[
\phi(x)
\left(
-\sigma x+\zeta z+\alpha yz
\right)
\right]
=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[\zeta z+\alpha yz\mid x]=\sigma x.
\]

Applying the same argument to arbitrary antiderivatives of \(y\) gives
\[
\mathbb E_\mu[\rho-y-xz\mid y]=0,
\]
so
\[
\mathbb E_\mu[xz\mid y]=\rho-y.
\]

Applying it to arbitrary antiderivatives of \(z\) gives
\[
\mathbb E_\mu[-z+xy\mid z]=0,
\]
hence
\[
\mathbb E_\mu[xy\mid z]=z.
\]

For the stationary circle, differentiate
\[
y^2+z^2
\]
along the vector field:
\[
\frac{d}{dt}(y^2+z^2)
=
2y(\rho-y-xz)+2z(-z+xy).
\]
The mixed terms cancel, giving
\[
\frac{d}{dt}(y^2+z^2)
=
2\rho y-2y^2-2z^2.
\]
Invariance therefore gives
\[
\mathbb E[y^2+z^2]=\rho m.
\]
Since
\[
\mathbb E[y^2]
=
\operatorname{Var}(y)+m^2,
\]
we obtain
\[
\operatorname{Var}(y)+\mathbb E[z^2]
=
m(\rho-m).
\]
Equivalently,
\[
\mathbb E
\left[
\left(y-\frac{\rho}{2}\right)^2+z^2
\right]
=
\frac{\rho^2}{4}.
\]

The left side of
\[
\operatorname{Var}(y)+\mathbb E[z^2]
=
m(\rho-m)
\]
is nonnegative, so
\[
0\le m\le\rho.
\]

The case
\[
m=0
\]
would force
\[
y=0,
\qquad
z=0
\]
on the support. But then
\[
\dot y=\rho>0,
\]
which is incompatible with invariance of that support. Hence
\[
m>0.
\]

If
\[
m=\rho,
\]
then
\[
y=\rho,
\qquad
z=0
\]
on the support. The equation
\[
\dot z=xy
\]
then forces
\[
x=0.
\]
Thus the measure is
\[
\delta_{(0,\rho,0)}.
\]
The converse is immediate.

For the speed defect, define
\[
R=xy-z=\dot z.
\]
The heightwise regression gives
\[
\mathbb E[R\mid z]=0.
\]
Hence \(R\) is orthogonal in \(L^2(\mu)\) to every square-integrable function of \(z\). Since
\[
xy=z+R,
\]
we get
\[
\operatorname{Var}(xy)
=
\operatorname{Var}(z)
+
\mathbb E[R^2]
\]
and
\[
\operatorname{Cov}(z,xy)
=
\operatorname{Var}(z).
\]

It remains to classify zero speed defect. Suppose
\[
\mathbb E[\dot z^2]=0.
\]
Continuity implies
\[
\dot z=0
\]
on the invariant support. Thus every support trajectory has
\[
z(t)=c
\]
and
\[
x(t)y(t)=c.
\]

By Poincaré recurrence, almost every point for \(\mu\) is recurrent.

If
\[
c=0,
\]
then a recurrent support trajectory satisfying
\[
xy=0
\]
cannot have \(y=0\) with \(x\ne0\), because then
\[
\dot y=\rho>0.
\]
If \(x=0\), then
\[
\dot y=\rho-y.
\]
The only bounded complete recurrent solution of this scalar equation is
\[
y=\rho.
\]
Thus the recurrent point is the equilibrium
\[
(0,\rho,0).
\]

If
\[
c\ne0,
\]
then neither \(x\) nor \(y\) vanishes and
\[
y=\frac{c}{x}.
\]
The \(x\)-equation reduces along the support trajectory to the scalar autonomous equation
\[
\dot x
=
-\sigma x+\zeta c+\frac{\alpha c^2}{x}.
\]
A nonconstant solution of a scalar autonomous differential equation is monotone between equilibria and cannot be recurrent. Therefore every recurrent point has
\[
\dot x=0.
\]
Then \(x\), \(y=c/x\), and \(z=c\) are all constant, and the point is an equilibrium.

Thus \(\mu\)-almost every point is an equilibrium. Since the equilibrium set is closed,
\[
\operatorname{supp}\mu
\]
is contained in it. The converse is immediate.

Finally, if
\[
\operatorname{Var}(z)=0,
\]
then \(z\) is constant on the invariant support, so
\[
\dot z=0
\]
there and the same argument gives equilibrium support. Hence a non-equilibrium-supported invariant measure has both
\[
\operatorname{Var}(z)>0
\]
and
\[
\mathbb E[\dot z^2]>0.
\]
Substitution into the covariance and variance formulas yields the displayed strict correlation law.

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies symbolically, as polynomial identities, the cancellation
\[
L(y^2+z^2)
=
2\rho y-2y^2-2z^2
\]
and the residual identities
\[
xy-z=\dot z,
\qquad
xz-(\rho-y)=-\dot y,
\qquad
\zeta z+\alpha yz-\sigma x=\dot x.
\]

It also verifies the algebraic equivalence between
\[
\mathbb E[y^2+z^2]=\rho m
\]
and
\[
\mathbb E[(y-\rho/2)^2+z^2]=\rho^2/4,
\]
together with the orthogonal-regression variance and covariance decomposition.

The stored checker output is `VERIFY_OK`.

The conditional-expectation identification and the zero-speed recurrence classification are analytic arguments; they are not inferred from finite trajectory sampling.

## Relationship to prior work
The Glukhovsky–Dolzhansky model was introduced in 1980 as a low-order model of convection in a rotating fluid.

A complete open 2015 article writes the model in the equivalent notation
\[
\dot x=-\sigma x+Cz+Ayz,
\qquad
\dot y=R_a-y-xz,
\qquad
\dot z=-z+xy.
\]
It proves dissipativity and completeness, constructs absorbing and positively invariant sets, studies homoclinic orbits, and analyzes self-excited and hidden attractors. The complete searchable PDF contains no occurrences of `variance`, `moment`, `invariant measure`, `conditional`, or `average`. Its quadratic functions are used for absorbing-set and homoclinic arguments rather than an all-invariant-measures stationary disintegration.

A 2015 public preprint devoted specifically to Lyapunov dimension writes the same three equations in the normalization
\[
\dot x=-\sigma x+z+a_0yz,
\qquad
\dot y=R-y-xz,
\qquad
\dot z=-z+xy
\]
and focuses on rigorous Lyapunov-dimension formulas and numerical dimension estimation.

A modern mathematical treatment studies homothetic equivalences, Darboux integrability, existence of a global attractor, local bifurcations, and dynamics at infinity. Its accessible article statement contains no moment, variance, average, or invariant-measure formulation.

A recent full open article analyzes hidden and transient attractors, global-stability boundaries, fractional-order dynamics, finite-time Lyapunov quantities, multifractal spectra, and statistical robustness. Targeted full-text searches found no `variance`, `moment`, or `conditional` theorem matching the present stationary identities.

The accepted result is therefore not a new attractor-existence, boundedness, Lyapunov-dimension, homoclinic, or bifurcation theorem. It is the all-invariant-measures stationary temperature circle, the three coordinate-fiber calibrations, and the exact height–convection speed defect.

## Limitations
The theorem is conditional on compactly supported invariant probability measures. It does not establish the existence or uniqueness of a chaotic attractor for arbitrary positive parameters.

The temperature circle fixes a second-moment shell but not the full joint distribution of \(y\) and \(z\).

The heightwise law determines only the conditional mean of \(xy\) given \(z\), not its full conditional distribution.

The historically earlier 1980 source was verified only at year resolution in the checked material, so no day was invented for it.

The modern 2023 mathematical article was compared through its accessible article statement and searchable page rather than a complete locally extracted PDF.

Because the generator proof is short, a differently phrased equivalent invariant-measure observation could remain in unindexed literature.

## References
1. A. B. Glukhovskii and F. V. Dolzhanskii, “Three-component geostrophic model of convection in a rotating fluid,” Izvestiya, Atmospheric and Oceanic Physics 16, 311–318 (1980).
2. G. A. Leonov, N. V. Kuznetsov, and T. N. Mokaev, “Homoclinic orbits, and self-excited and hidden attractors in a Lorenz-like system describing convective fluid motion,” European Physical Journal Special Topics 224, 1421–1458 (2015), DOI 10.1140/epjst/e2015-02470-3.
3. N. V. Kuznetsov, G. A. Leonov, and T. N. Mokaev, “The Lyapunov dimension and its computation for self-excited and hidden attractors in the Glukhovsky–Dolzhansky fluid convection model,” arXiv:1509.09161 (2015).
4. G. A. Leonov and T. N. Mokaev, “Lyapunov dimension formula for the attractor of the Glukhovsky–Dolzhansky system,” Doklady Mathematics 93, 42–45 (2016), DOI 10.1134/S1064562416010154.
5. J. Jiao, S. Yang, Q. Zhou, and K. Huang, “On a simple model for describing convection of the rotating fluid: Integrability, bifurcations and global dynamics,” Discrete and Continuous Dynamical Systems B 28, 2565–2592 (2023), DOI 10.3934/dcdsb.2022181.
