# Three fiberwise stationary regressions and speed-coherence laws in the Chen flow
## Finding
Consider the classical real Chen system
\[
\dot x=a(y-x),
\qquad
\dot y=(c-a)x-xz+cy,
\qquad
\dot z=xy-bz,
\]
with
\[
a>0,\qquad b>0,\qquad c>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Then the three coordinate equations sharpen from global stationary balances to exact fiberwise regressions:
\[
\boxed{\mathbb E_\mu[y\mid x]=x},
\]
\[
\boxed{\mathbb E_\mu[x(z+a-c)\mid y]=cy},
\]
and
\[
\boxed{\mathbb E_\mu[xy\mid z]=bz}.
\]

The three regression residuals are exactly the coordinate speeds, up to sign and the factor \(a\):
\[
y-x=\frac{\dot x}{a},
\]
\[
x(z+a-c)-cy=-\dot y,
\]
and
\[
xy-bz=\dot z.
\]

Conditional orthogonality therefore gives the exact speed-defect identities
\[
\boxed{
\operatorname{Var}_\mu(y)
=
\operatorname{Var}_\mu(x)
+
\frac{1}{a^2}\mathbb E_\mu[\dot x^2]
},
\]
\[
\boxed{
\operatorname{Var}_\mu(x(z+a-c))
=
c^2\operatorname{Var}_\mu(y)
+
\mathbb E_\mu[\dot y^2]
},
\]
and
\[
\boxed{
\operatorname{Var}_\mu(xy)
=
b^2\operatorname{Var}_\mu(z)
+
\mathbb E_\mu[\dot z^2]
}.
\]

The same regressions fix three directed covariances:
\[
\boxed{
\operatorname{Cov}_\mu(x,y)
=
\operatorname{Var}_\mu(x)
},
\]
\[
\boxed{
\operatorname{Cov}_\mu(x(z+a-c),y)
=
c\operatorname{Var}_\mu(y)
},
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(xy,z)
=
b\operatorname{Var}_\mu(z)
}.
\]

Each speed defect vanishes exactly for invariant measures supported on equilibria. The equilibrium set is
\[
\mathcal E=\{(0,0,0)\}
\]
when
\[
2c\le a,
\]
and when
\[
2c>a
\]
it is
\[
\mathcal E
=
\left\{
(0,0,0),
\left(\sqrt{b(2c-a)},\sqrt{b(2c-a)},2c-a\right),
\left(-\sqrt{b(2c-a)},-\sqrt{b(2c-a)},2c-a\right)
\right\}.
\]

Hence every compact stationary state not supported on \(\mathcal E\) has all three defects strictly positive. In particular,
\[
\operatorname{Var}_\mu(y)>\operatorname{Var}_\mu(x)>0.
\]
Moreover all three predictor-response correlations are strictly between zero and one. They are given exactly by
\[
\boxed{
\operatorname{Corr}_\mu(x,y)
=
\left(
1+
\frac{\mathbb E_\mu[\dot x^2]}
{a^2\operatorname{Var}_\mu(x)}
\right)^{-1/2}
},
\]
\[
\boxed{
\operatorname{Corr}_\mu(x(z+a-c),y)
=
\left(
1+
\frac{\mathbb E_\mu[\dot y^2]}
{c^2\operatorname{Var}_\mu(y)}
\right)^{-1/2}
},
\]
and
\[
\boxed{
\operatorname{Corr}_\mu(xy,z)
=
\left(
1+
\frac{\mathbb E_\mu[\dot z^2]}
{b^2\operatorname{Var}_\mu(z)}
\right)^{-1/2}
}.
\]

Thus mean-square coordinate speeds measure exactly the loss from perfect stationary coherence along the three natural Chen couplings.

For the classical chaotic parameters
\[
(a,b,c)=(35,3,28),
\]
the regressions become
\[
\mathbb E[y\mid x]=x,
\qquad
\mathbb E[x(z+7)\mid y]=28y,
\qquad
\mathbb E[xy\mid z]=3z,
\]
and the nonzero equilibria are
\[
(\pm3\sqrt7,\pm3\sqrt7,21).
\]

## Assumptions and scope
The theorem concerns the autonomous three-dimensional real Chen flow. Compact support guarantees integrability of every polynomial observable and every one-coordinate antiderivative test used below. No ergodicity assumption and no symmetry assumption on the invariant measure are required.

The Chen system was introduced in 1999. The earliest checked source with a day-resolved public publication date is the original Chen–Ueta article, dated 1 July 1999.

A mathematical treatment of stability and bifurcation of the same system is classified under MSC \(34C23\) and \(34D20\). The present result uses primary MSC \(34C23\).

A previously published stationary-balance result for a complex extension of the Chen system specializes on the real subspace to integrated identities such as
\[
\mathbb E[xy]=\mathbb E[x^2]
\]
and an amplitude-weighted height relation. Those integrated statements are treated as prior coverage. The finding assessed here is the stronger three-fiber conditional structure and its exact speed-coherence consequences.

## Proof
Let \(L\) denote the generator of the flow.

Take any continuous function \(\phi\) on the compact \(x\)-range and choose an antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
a\phi(x)(y-x).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)(y-x)]=0
\]
for every \(\phi\). Hence
\[
\mathbb E_\mu[y\mid x]=x.
\]

For the second equation, rewrite
\[
\dot y
=
cy-x(z+a-c).
\]
Testing against arbitrary antiderivatives of \(y\) gives
\[
\mathbb E_\mu[x(z+a-c)-cy\mid y]=0,
\]
so
\[
\mathbb E_\mu[x(z+a-c)\mid y]=cy.
\]

Testing the third equation against arbitrary antiderivatives of \(z\) gives
\[
\mathbb E_\mu[xy-bz\mid z]=0,
\]
and therefore
\[
\mathbb E_\mu[xy\mid z]=bz.
\]

For the first defect define
\[
R_x=y-x=\frac{\dot x}{a}.
\]
The first conditional law says
\[
\mathbb E[R_x\mid x]=0.
\]
Hence \(R_x\) is orthogonal to every square-integrable function of \(x\), in particular to \(x-\mathbb E[x]\). Since
\[
y=x+R_x,
\]
we get
\[
\operatorname{Var}(y)
=
\operatorname{Var}(x)
+
\mathbb E[R_x^2]
\]
and
\[
\operatorname{Cov}(x,y)=\operatorname{Var}(x).
\]
Substitution of \(R_x=\dot x/a\) gives the first speed defect.

For the second defect put
\[
Q=x(z+a-c)
\]
and
\[
R_y=Q-cy=-\dot y.
\]
Because
\[
\mathbb E[R_y\mid y]=0,
\]
we have
\[
Q=cy+R_y
\]
with an orthogonal residual. Thus
\[
\operatorname{Var}(Q)
=
c^2\operatorname{Var}(y)+\mathbb E[\dot y^2]
\]
and
\[
\operatorname{Cov}(Q,y)=c\operatorname{Var}(y).
\]

For the third defect let
\[
R_z=xy-bz=\dot z.
\]
The conditional law gives
\[
\mathbb E[R_z\mid z]=0.
\]
Hence
\[
xy=bz+R_z
\]
with an orthogonal residual, so
\[
\operatorname{Var}(xy)
=
b^2\operatorname{Var}(z)+\mathbb E[\dot z^2]
\]
and
\[
\operatorname{Cov}(xy,z)=b\operatorname{Var}(z).
\]

We next classify all three equality cases.

If the first defect vanishes, then \(\dot x=0\) on the invariant support. Thus \(x\) is constant along each support trajectory and the first equation gives \(y=x\). The second equation becomes
\[
0=x(2c-a-z).
\]
If \(x=0\), then \(y=0\), and the remaining scalar equation
\[
\dot z=-bz
\]
has no nonzero bounded complete orbit, so \(z=0\). If \(x\ne0\), then
\[
z=2c-a,
\]
and the third equation forces
\[
x^2=b(2c-a).
\]
Thus the trajectory is an equilibrium.

If the second defect vanishes, then \(\dot y=0\), so \(y\) is constant along every support trajectory. The first equation is the stable linear filter
\[
\dot x=a(y-x).
\]
A bounded complete solution with constant \(y\) must have \(x=y\) identically. The previous equilibrium argument then applies.

If the third defect vanishes, then \(z\) is constant and
\[
xy=bz=:K.
\]
For
\[
u=x^2
\]
we have
\[
\dot u
=
2a(xy-x^2)
=
2a(K-u).
\]
A bounded complete solution of this scalar stable equation must satisfy
\[
u=K.
\]
If \(K=0\), invariance forces the origin. If \(K>0\), continuity makes \(x\) constant on the trajectory, the first equation gives \(y=x\), and the second gives \(z=2c-a\); hence again the trajectory is one of the nonzero equilibria. The case \(K<0\) is impossible because \(u=x^2\ge0\).

Conversely, every invariant measure supported on equilibria makes all coordinate speeds vanish. This proves the equality classification.

If a compact invariant measure is not equilibrium-supported, then all three mean-square speeds are positive. If any of \(\operatorname{Var}(x)\), \(\operatorname{Var}(y)\), or \(\operatorname{Var}(z)\) vanished, the corresponding coordinate would be constant on invariant support and the same bounded-complete-trajectory arguments would force equilibrium support. Thus the correlation denominators are positive. The three displayed correlation formulas follow directly from the covariance and variance identities.

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic.

It verifies the three pointwise residual identities
\[
y-x=\frac{\dot x}{a},
\]
\[
x(z+a-c)-cy=-\dot y,
\]
and
\[
xy-bz=\dot z.
\]

It verifies the abstract orthogonal-regression variance and covariance algebra used in each speed-defect identity.

At the classical parameters
\[
a=35,\qquad b=3,\qquad c=28,
\]
it verifies algebraically that
\[
2c-a=21,
\qquad
b(2c-a)=63,
\]
and that the two nonzero equilibria with
\[
x^2=y^2=63,
\qquad
x=y,
\qquad
z=21
\]
satisfy all three vector-field equations.

The stored checker output is `VERIFY_OK`.

The conditional-expectation and equality-rigidity statements are analytic consequences of invariance and bounded complete trajectories; they are not inferred from finite numerical sampling.

## Relationship to prior work
Chen and Ueta introduced the real three-dimensional system in 1999 with the equations used here and exhibited the now-standard chaotic parameters
\[
(a,b,c)=(35,3,28).
\]

Ueta and Chen then gave a detailed same-object bifurcation analysis. Their complete author-hosted article develops the symmetry, a Lyapunov stability region, divergence and dissipativity, the three equilibria, equilibrium and periodic-orbit bifurcations, coexistence phenomena, stable and unstable manifolds, and the geometric structure of the chaotic attractor. The inspected sections do not state a conditional-expectation, coordinate-variance, or invariant-measure theorem matching the present result.

A later stability-and-bifurcation study provides a mathematical classification under MSC \(34C23\) and \(34D20\). These orbit and local-bifurcation results do not imply the three stationary regressions.

A published result for the complex Chen extension is a particularly close comparison. On the real subspace it supplies integrated balances, including
\[
\mathbb E[xy]=\mathbb E[x^2],
\]
and an amplitude-weighted height identity containing \(\mathbb E[\dot x^2]\). Those formulas are prior. They do not imply
\[
\mathbb E[y\mid x]=x,
\]
which is equivalent to infinitely many orthogonality constraints against functions of \(x\), nor do they imply the independent \(y\)-fiber and \(z\)-fiber regressions. The new statement therefore sharpens integrated stationary balances into a three-coordinate disintegration law.

## Limitations
The theorem assumes compactly supported invariant probability measures. It does not prove existence or uniqueness of a physical measure for any parameter set.

The result does not determine entropy, Lyapunov exponents, fractal dimension, basin geometry, or the full joint invariant density.

The equality classification concerns the three coordinate-speed defects; an equilibrium-supported mixture can have nonzero coordinate variance while all three defects vanish.

Integrated real-subspace balances obtainable from the previously published complex-Chen result are treated as prior coverage and are not claimed as new.

Because the generator argument is short once one tests against arbitrary one-coordinate antiderivatives, a differently phrased equivalent fiberwise observation could remain in unindexed literature.

## References
1. G. Chen and T. Ueta, “Yet Another Chaotic Attractor,” International Journal of Bifurcation and Chaos 9, 1465–1466 (1999), DOI 10.1142/S0218127499001024.
2. T. Ueta and G. Chen, “Bifurcation Analysis of Chen's Equation,” International Journal of Bifurcation and Chaos 10, 1917–1931 (2000), DOI 10.1142/S0218127400001183.
3. Y. Tang, T. Li, and G. Chen, “On stability and bifurcation of Chen's system,” Chaos, Solitons & Fractals 19, 1269–1282 (2004), DOI 10.1016/S0960-0779(03)00334-5.
4. L. Wang and X. Zhang, “Bifurcation and Dynamics of the complex Chen systems,” Discrete and Continuous Dynamical Systems - B 29, 1243–1282 (2024), DOI 10.3934/dcdsb.2023132.
