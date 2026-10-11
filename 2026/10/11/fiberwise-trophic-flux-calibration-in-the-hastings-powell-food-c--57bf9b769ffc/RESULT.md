# Fiberwise trophic-flux calibration in the Hastings–Powell food chain
## Finding
Consider the nondimensional Hastings–Powell three-species food chain
\[
\dot x=x(1-x)-f_1(x)y,
\]
\[
\dot y=f_1(x)y-f_2(y)z-d_1y,
\]
\[
\dot z=(f_2(y)-d_2)z,
\]
where
\[
f_i(s)=\frac{a_i s}{1+b_i s},
\qquad
a_i>0,\ b_i>0,\ d_i>0.
\]

Let \(\mu\) be a compactly supported invariant Borel probability measure whose support is contained in the strictly positive orthant
\[
(0,\infty)^3.
\]
Define
\[
g(x)=\frac{(1-x)(1+b_1x)}{a_1}
\]
and
\[
Q(x,y,z)
=
f_1(x)-\frac{a_2z}{1+b_2y}.
\]

Then the three trophic layers obey exact fiberwise stationarity laws:
\[
\boxed{
\mathbb E_\mu[y\mid x]=g(x)
},
\]
\[
\boxed{
\mathbb E_\mu[Q(x,y,z)\mid y]=d_1
},
\]
and
\[
\boxed{
\mathbb E_\mu[f_2(y)\mid z]=d_2
}.
\]

These are stronger than the corresponding integrated time-average balances. Their residuals are precisely the three per-capita coordinate speeds:
\[
y-g(x)
=
-\frac{1+b_1x}{a_1x}\dot x,
\]
\[
Q-d_1
=
\frac{\dot y}{y},
\]
and
\[
f_2(y)-d_2
=
\frac{\dot z}{z}.
\]

Conditional orthogonality therefore gives the exact fluctuation budgets
\[
\boxed{
\operatorname{Var}_\mu(y)
=
\operatorname{Var}_\mu(g(x))
+
\mathbb E_\mu
\left[
\left(
\frac{1+b_1x}{a_1x}\dot x
\right)^2
\right]
},
\]
\[
\boxed{
\operatorname{Var}_\mu(Q)
=
\mathbb E_\mu
\left[
\left(
\frac{\dot y}{y}
\right)^2
\right]
},
\]
and
\[
\boxed{
\operatorname{Var}_\mu(f_2(y))
=
\mathbb E_\mu
\left[
\left(
\frac{\dot z}{z}
\right)^2
\right]
}.
\]

Each displayed defect vanishes exactly for invariant measures supported on equilibria.

The top-predator fiber law also gives a sharp persistence obstruction. Since
\[
0<f_2(y)<\frac{a_2}{b_2}
\]
for every finite positive \(y\), existence of an interior compact stationary state forces
\[
\boxed{
a_2>b_2d_2
}.
\]

Assume this necessary inequality and define the top-predator break-even middle-trophic density
\[
y_*
=
\frac{d_2}{a_2-b_2d_2},
\]
so that
\[
f_2(y_*)=d_2.
\]
Because \(f_2\) is strictly increasing and strictly concave,
\[
d_2
=
\mathbb E_\mu[f_2(y)]
\le
f_2(\mathbb E_\mu[y]).
\]
Hence
\[
\boxed{
\mathbb E_\mu[y]\ge y_*
}.
\]
Equality holds exactly for equilibrium-supported measures. Therefore every compact stationary state that is not supported on equilibria satisfies
\[
\boxed{
\mathbb E_\mu[y]>y_*
}.
\]

For a nonconstant positive periodic orbit, periodicity of \(\log z\) gives
\[
\frac1P\int_0^P f_2(y(t))\,dt=d_2.
\]
Since \(f_2\) is strictly increasing, \(y(t)-y_*\) must take both signs. Thus every nonconstant positive periodic orbit crosses
\[
\boxed{
y=y_*
}
\]
at least twice in each least period.

At the classical chaotic parameters used by Hastings and Powell,
\[
a_1=5,\qquad
b_1=3,\qquad
a_2=\frac1{10},\qquad
b_2=2,\qquad
d_1=\frac25,\qquad
d_2=\frac1{100},
\]
one obtains
\[
y_*=\frac18.
\]
Accordingly, every non-equilibrium compact stationary state in the positive orthant satisfies
\[
\mathbb E_\mu[y]>\frac18,
\]
while the exact fiber laws specialize to
\[
\mathbb E_\mu[y\mid x]
=
\frac{(1-x)(1+3x)}{5},
\]
\[
\mathbb E_\mu
\left[
\frac{5x}{1+3x}
-
\frac{z}{10(1+2y)}
\mathrel{\Big|} y
\right]
=
\frac25,
\]
and
\[
\mathbb E_\mu
\left[
\frac{y}{10(1+2y)}
\mathrel{\Big|}z
\right]
=
\frac1{100}.
\]

## Assumptions and scope
The theorem concerns compact invariant probability measures supported strictly inside the biologically meaningful positive orthant. The interior-support assumption is essential because the proof uses per-capita growth rates and antiderivatives with factors \(1/x\), \(1/y\), and \(1/z\).

The original Hastings–Powell model was published on 1 June 1991. It uses exactly the nondimensional equations above with Holling type-II functional responses and reports chaotic dynamics at the parameter set
\[
(a_1,b_1,a_2,b_2,d_1,d_2)
=
(5,3,0.1,2,0.4,0.01).
\]

A complete mathematical treatment by Klebanoff and Hastings studies this same model through normal-form and bifurcation theory and classifies the work under MSC \(37D45\) among its dynamical-systems classifications. The present theorem is assigned primary MSC \(37D45\).

The theorem does not require ergodicity. It applies separately to compact positive chaotic invariant measures, positive periodic-orbit measures, positive equilibrium atoms, and convex mixtures whose support remains in the positive orthant.

## Proof
Because the support of \(\mu\) is compact and contained in
\[
(0,\infty)^3,
\]
all three coordinates are bounded away from zero on the support.

Let \(\phi\) be a continuous function on the compact \(x\)-projection of the support. Choose an antiderivative \(H\) satisfying
\[
H'(x)=\frac{\phi(x)}{x}.
\]
Then
\[
LH
=
\phi(x)
\left(
1-x-\frac{a_1y}{1+b_1x}
\right).
\]
Invariance gives
\[
\mathbb E_\mu
\left[
\phi(x)
\left(
1-x-\frac{a_1y}{1+b_1x}
\right)
\right]
=
0
\]
for every \(\phi\). Therefore
\[
\mathbb E_\mu[y\mid x]
=
\frac{(1-x)(1+b_1x)}{a_1}
=
g(x).
\]

Similarly, using arbitrary antiderivatives with derivative
\[
\frac{\psi(y)}{y}
\]
gives
\[
\mathbb E_\mu
\left[
f_1(x)-\frac{a_2z}{1+b_2y}-d_1
\mathrel{\Big|}y
\right]
=
0,
\]
which is the second fiber law.

Finally, arbitrary antiderivative tests with derivative
\[
\frac{\chi(z)}{z}
\]
give
\[
\mathbb E_\mu[f_2(y)-d_2\mid z]=0,
\]
proving the third.

The three residual identities follow directly from the ODE:
\[
\frac{\dot x}{x}
=
\frac{a_1}{1+b_1x}(g(x)-y),
\]
\[
\frac{\dot y}{y}
=
Q-d_1,
\]
and
\[
\frac{\dot z}{z}
=
f_2(y)-d_2.
\]
A conditional-expectation residual is orthogonal in \(L^2(\mu)\) to every square-integrable function of the conditioning coordinate. Applying the Pythagorean identity gives all three variance formulas.

For the equality cases, suppose first that the \(x\)-defect vanishes. Then
\[
\dot x=0
\]
on the invariant support, so \(x\) is constant along each support trajectory. The first equation then makes \(y=g(x)\) constant along that trajectory. Since the trajectory is complete and bounded and
\[
\dot z=z(f_2(y)-d_2)
\]
has constant coefficient, boundedness in both time directions forces
\[
f_2(y)=d_2,
\]
hence \(z\) is constant. The middle equation then gives an equilibrium.

If the \(y\)-defect vanishes, then
\[
\dot y=0
\]
on support trajectories, so \(y\) is constant. Again bounded completeness of the scalar \(z\)-equation forces
\[
f_2(y)=d_2,
\]
then \(z\) is constant, and strict monotonicity of \(f_1\) in the middle equation forces \(x\) to be constant. Thus the trajectory is an equilibrium.

If the \(z\)-defect vanishes, then
\[
\dot z=0
\]
and the third equation gives
\[
f_2(y)=d_2.
\]
Strict monotonicity of \(f_2\) makes \(y\) constant. The middle equation then makes \(f_1(x)\) constant, so strict monotonicity of \(f_1\) makes \(x\) constant. Again the support consists of equilibria.

Conversely, every equilibrium-supported invariant measure has all three coordinate speeds zero, so every defect vanishes.

For the persistence obstruction,
\[
d_2
=
\mathbb E_\mu[f_2(y)]
<
\frac{a_2}{b_2},
\]
which is equivalent to
\[
a_2>b_2d_2.
\]

Under that inequality,
\[
f_2(y_*)=d_2
\]
for
\[
y_*=\frac{d_2}{a_2-b_2d_2}.
\]
The function \(f_2\) is strictly increasing and strictly concave on the positive axis. Jensen's inequality gives
\[
d_2
=
\mathbb E[f_2(y)]
\le
f_2(\mathbb E[y]),
\]
hence
\[
\mathbb E[y]\ge y_*.
\]
Equality in strict Jensen forces \(y\) to be constant on the support. The invariant-support argument above then forces equilibrium support. This proves the strict inequality away from equilibrium-supported measures.

For a nonconstant periodic orbit, integrating
\[
\dot z/z=f_2(y)-d_2
\]
over one period gives zero. If \(y(t)\) stayed on only one side of \(y_*\), strict monotonicity of \(f_2\) would make the integral strictly positive or strictly negative unless \(y\equiv y_*\), which would force an equilibrium. Hence \(y-y_*\) takes both signs and, by continuity and periodicity, has at least two zeros in every least period.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the three residual identities from the vector field, the exact standard-parameter value
\[
y_*=\frac18,
\]
and the abstract conditional-regression variance decomposition.

It also verifies strict concavity of the Holling type-II response through the exact formula
\[
f_2''(y)
=
-\frac{2a_2b_2}{(1+b_2y)^3}.
\]

The stored checker output is `VERIFY_OK`.

The conditional-expectation statements, equality classifications, and periodic crossing theorem are analytic consequences of invariant-support geometry; they are not inferred from finite numerical trajectories.

## Relationship to prior work
Hastings and Powell introduced the nondimensional three-species food chain with Holling type-II responses and demonstrated stable, periodic, and chaotic regimes numerically. Their classical chaotic example uses
\[
a_1=5,\quad
b_1=3,\quad
a_2=0.1,\quad
b_2=2,\quad
d_1=0.4,\quad
d_2=0.01.
\]
The complete article formulates the ODE, reports period-doubling and chaotic attractors, and discusses trophic crashes and sensitive dependence; it does not formulate invariant probability measures or fiberwise conditional trophic-flux laws.

Klebanoff and Hastings give a complete mathematical bifurcation treatment of the same model and a broader class of three-species food chains. Their article derives equilibria, invariant feasible geometry, normal forms, Hopf, homoclinic and heteroclinic bifurcations, and horseshoe mechanisms. Its complete argument is organized around local/global bifurcation geometry rather than invariant-measure conditional moments.

Coria studies global bounds for the Hastings–Powell system, obtaining a compact region containing all compact invariant sets, together with nonexistence and predator-survival conditions. The open article's stated results concern localization of invariant sets, not the fiberwise stationarity theorem proved here.

The integrated identity
\[
\mathbb E[f_2(y)]=d_2
\]
is a direct global consequence of zero mean per-capita top-predator growth and is not, by itself, the originality claim. The accepted result strengthens it to
\[
\mathbb E[f_2(y)\mid z]=d_2
\]
and supplies the two companion fiber laws, exact speed-defect decompositions, equality rigidity, and the finite-amplitude break-even crossing theorem.

## Limitations
The theorem assumes compact invariant support strictly inside the positive orthant. It does not cover boundary invariant measures with one or more extinct species.

It does not prove existence of a positive chaotic invariant measure for arbitrary parameters.

The conditional laws determine selected conditional means, not complete conditional distributions.

The top-predator break-even inequality is necessary for an interior compact stationary state, not sufficient for persistence or chaos.

General ecological persistence theory contains integrated per-capita growth balances; the novelty assessment here is restricted to the stronger coordinate-fiber disintegrations and their exact speed-defect consequences.

Because the generator calculation is short, an equivalent conditional statement could remain in unindexed ecological-dynamics literature.

## References
1. A. Hastings and T. Powell, “Chaos in a Three-Species Food Chain,” *Ecology* 72, 896–903 (1991), DOI 10.2307/1940591.
2. A. Klebanoff and A. Hastings, “Chaos in three species food chains,” *Journal of Mathematical Biology* 32, 427–451 (1994), DOI 10.1007/BF00160167.
3. L. N. Coria, “Global Dynamics of the Hastings-Powell System,” *Mathematical Problems in Engineering* 2013, 469072 (2013), DOI 10.1155/2013/469072.
