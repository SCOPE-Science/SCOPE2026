# Exact stationary nullcline calibration and coupled speed defects in the Oregonator
## Finding
Consider the irreversible three-intermediate Oregonator
\[
\dot X=k_1AY-k_2XY+k_3BX-2k_4X^2,
\]
\[
\dot Y=-k_1AY-k_2XY+fk_5Z,
\]
\[
\dot Z=k_3BX-k_5Z,
\]
with
\[
A,B,k_1,k_2,k_3,k_4,k_5,f>0.
\]

Every compactly supported invariant Borel probability measure \(\mu\) satisfies the exact conditional nullcline law
\[
(k_1A-k_2X)\mathbb E_\mu[Y\mid X]
+k_3BX-2k_4X^2
=0.
\]
Thus, away from the vertical degeneracy \(k_1A=k_2X\), the stationary conditional mean of \(Y\) lies exactly on the deterministic \(X\)-nullcline:
\[
\mathbb E_\mu[Y\mid X]
=
\frac{X(2k_4X-k_3B)}{k_1A-k_2X}.
\]
The undivided identity remains valid at the degenerate slice.

The catalyst coordinate has an even simpler exact regression:
\[
\boxed{
\mathbb E_\mu[X\mid Z]
=
\frac{k_5}{k_3B}Z
}.
\]

Both laws have exact dynamical defects. The first coordinate satisfies
\[
\boxed{
\mathbb E_\mu[\dot X^2]
=
\mathbb E_\mu\!\left[
(k_1A-k_2X)^2
\operatorname{Var}_\mu(Y\mid X)
\right]
}.
\]
The catalyst coordinate satisfies
\[
\boxed{
\operatorname{Var}_\mu(X)
-
\left(\frac{k_5}{k_3B}\right)^2
\operatorname{Var}_\mu(Z)
=
\frac{1}{(k_3B)^2}
\mathbb E_\mu[\dot Z^2]
\ge0
}.
\]

Either defect vanishes exactly for probability measures supported on the equilibrium set. Therefore every compact invariant probability measure that is not equilibrium-supported satisfies both strict inequalities
\[
\mathbb E_\mu[\dot X^2]>0
\]
and
\[
\operatorname{Var}_\mu(X)
>
\left(\frac{k_5}{k_3B}\right)^2
\operatorname{Var}_\mu(Z).
\]

For the numerical parameter choices used by Field and Noyes in their 1974 limit-cycle calculation,
\[
k_3=8\times10^3\ \mathrm{M}^{-1}\mathrm{s}^{-1},
\qquad
B=0.06\ \mathrm{M},
\qquad
k_5=1\ \mathrm{s}^{-1}.
\]
Hence
\[
k_3B=480\ \mathrm{s}^{-1}
\]
and the catalyst regression is
\[
\mathbb E[X\mid Z]=\frac{Z}{480}.
\]
The variance-speed defect becomes
\[
\operatorname{Var}(X)
-
\frac{1}{230400}\operatorname{Var}(Z)
=
\frac{1}{230400}\mathbb E[\dot Z^2].
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the autonomous Oregonator flow and supported on a compact subset of \(\mathbb R^3\). The result itself does not require positivity of the support, although the physical Oregonator is used in the positive concentration region.

The equations are the irreversible five-step Field–Noyes Oregonator written in dimensional concentration variables. The 1974 source denotes the intermediates by \(X\), \(Y\), and \(Z\), with feed concentrations \(A\) and \(B\), and obtains the displayed three-dimensional rate equations directly from the five reaction steps.

The earliest verified public source date for this exact Oregonator model is 1 March 1974.

A later mathematical treatment of chemical reaction networks includes the Oregonator among its principal examples and is classified under MSC \(34C15\) and \(37G15\). The primary classification used here is \(34C15\).

The theorem concerns invariant-measure constraints. It does not assert existence or uniqueness of a limit cycle for arbitrary parameters.

## Proof
Let \(L\) denote the generator.

For any continuous function \(\phi\) on the compact \(X\)-range, choose a continuously differentiable antiderivative \(H\) satisfying
\[
H'(X)=\phi(X).
\]
Then
\[
LH
=
\phi(X)
\left[
(k_1A-k_2X)Y+k_3BX-2k_4X^2
\right].
\]
Invariance gives
\[
0
=
\mathbb E_\mu[LH]
\]
for every such \(\phi\). Hence
\[
(k_1A-k_2X)\mathbb E_\mu[Y\mid X]
+k_3BX-2k_4X^2
=0
\]
almost surely.

Define
\[
m(X)=\mathbb E_\mu[Y\mid X].
\]
The preceding relation rewrites the first equation pointwise as
\[
\dot X
=
(k_1A-k_2X)(Y-m(X)).
\]
Conditioning on \(X\) and squaring gives
\[
\mathbb E_\mu[\dot X^2\mid X]
=
(k_1A-k_2X)^2
\operatorname{Var}_\mu(Y\mid X).
\]
Averaging proves the first defect identity.

For the catalyst coordinate, let \(\psi\) be continuous on the compact \(Z\)-range and choose an antiderivative \(K\). Since
\[
LK
=
\psi(Z)(k_3BX-k_5Z),
\]
invariance yields
\[
\mathbb E_\mu[\psi(Z)(k_3BX-k_5Z)]=0
\]
for every \(\psi\). Therefore
\[
\mathbb E_\mu[X\mid Z]
=
\frac{k_5}{k_3B}Z.
\]

Set
\[
c=\frac{k_5}{k_3B}.
\]
Then
\[
\frac{\dot Z}{k_3B}
=
X-cZ
=
X-\mathbb E_\mu[X\mid Z].
\]
Conditional-expectation orthogonality gives
\[
\mathbb E_\mu[(X-cZ)^2]
=
\operatorname{Var}_\mu(X)-c^2\operatorname{Var}_\mu(Z).
\]
Thus
\[
\operatorname{Var}_\mu(X)-c^2\operatorname{Var}_\mu(Z)
=
\frac{1}{(k_3B)^2}\mathbb E_\mu[\dot Z^2].
\]

It remains to classify equality. If either defect vanishes, then respectively \(\dot X=0\) or \(\dot Z=0\) on the invariant support.

Suppose first that \(\dot X=0\) on the support. Then \(X\) is constant along every support trajectory. The \(Z\)-equation is a scalar affine equation with constant forcing,
\[
\dot Z=k_3BX-k_5Z.
\]
Its only bounded complete solution is
\[
Z=\frac{k_3B}{k_5}X.
\]
Thus \(Z\) is constant. The \(Y\)-equation then becomes
\[
\dot Y
=-(k_1A+k_2X)Y+fk_5Z,
\]
a scalar affine equation with strictly negative linear coefficient. Its only bounded complete solution is constant. Hence all three coordinates are constant and the support consists of equilibria.

If instead \(\dot Z=0\) on the support, then \(Z\) is constant and the \(Z\)-equation forces \(X=(k_5/(k_3B))Z\), so \(X\) is constant. The same bounded-complete argument for \(Y\) again gives an equilibrium. Conversely every equilibrium-supported probability measure makes both defects zero.

For the 1974 numerical parameters, the paper uses
\[
k_3=8\times10^3\ \mathrm{M}^{-1}\mathrm{s}^{-1},
\qquad
B=0.06\ \mathrm{M},
\qquad
k_5=1\ \mathrm{s}^{-1},
\]
so
\[
k_3B=480\ \mathrm{s}^{-1}
\]
and the stated specialization follows.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic for the algebraic parts and exact rational arithmetic for the 1974 specialization.

It verifies
\[
\dot X
=
(k_1A-k_2X)Y+k_3BX-2k_4X^2
\]
and
\[
\dot Z=k_3BX-k_5Z.
\]
It checks that the stationary nullcline relation removes the deterministic part of \(\dot X\), leaving the conditional residual multiplied by \(k_1A-k_2X\).

For the 1974 values it verifies exactly
\[
k_3B=480
\]
and
\[
\frac{k_5}{k_3B}=\frac1{480},
\qquad
\frac{1}{(k_3B)^2}=\frac1{230400}.
\]

The stored checker output is `VERIFY_OK`.

The checker validates algebraic certificates only. The conditional-expectation statements and the equilibrium equality classification use stationarity and bounded-complete-trajectory arguments; they are not inferred from finite simulation.

## Relationship to prior work
Field and Noyes introduced the Oregonator in 1974 from a five-step reduction of the Belousov–Zhabotinsky mechanism. Their complete article writes the three-dimensional rate equations, numerically exhibits a stable closed trajectory, studies a stiff two-variable reduction, and performs a normal-mode stability analysis. It does not state invariant-measure conditional regressions or variance-speed defects.

Hastings studied periodic plane waves in the Oregonator reaction–diffusion equations in 1976. That work concerns existence of periodic traveling structures rather than invariant-measure statistics of the homogeneous three-variable flow.

Sexton and Forbes later analyzed oscillatory parameter regions and fold bifurcations in a simplified two-variable Oregonator. Their model reduction and bifurcation question do not implication-wise determine the three-variable stationary conditional laws above.

A modern global-Hopf treatment includes Oregonator chemical reaction networks among its examples and is classified under MSC \(34C15\) and \(37G15\). Its accessible statement concerns structural conditions for global periodic branches, not stationary moment disintegration. The complete text was not available in the inspected source, so no blanket whole-document noncoverage claim is made for that article.

Scholarpedia and a later historical review document the Oregonator normalization, its five-step origin, and its role as the simplest realistic BZ model. They do not expose the conditional-regression or variance-speed statement accepted here.

Targeted searches covered invariant measures, conditional means, nullcline averages, \(X\)-versus-\(Z\) variance defects, derivative-energy formulations, and periodic-orbit averages. No same-object source located supplied the surviving claim.

## Limitations
The theorem gives universal constraints for compactly supported invariant probability measures; it does not prove that a limit cycle exists for every positive parameter set.

The conditional \(X\)-nullcline formula is best kept in undivided form at the slice
\[
k_1A=k_2X,
\]
where the rational nullcline expression has a vanishing denominator.

The result constrains conditional means and second moments but does not determine the full invariant density, oscillation period, or stability multipliers.

The complete modern global-Hopf article was not available in the inspected source, although its abstract, metadata, classification, and reference context were checked.

Because the generator calculations are short, an equivalent observation could remain in unindexed chemical-kinetics literature.

## References
1. R. J. Field and R. M. Noyes, “Oscillations in chemical systems. IV. Limit cycle behavior in a model of a real chemical reaction,” Journal of Chemical Physics 60, 1877–1884 (1974), DOI 10.1063/1.1681288.
2. S. P. Hastings, “Periodic Plane Waves for the Oregonator,” Studies in Applied Mathematics 55, 293–299 (1976), DOI 10.1002/sapm1976554293.
3. M. J. Sexton and L. K. Forbes, “A note on oscillations in a simple model of a chemical reaction,” ANZIAM Journal 37, 451–457 (1996), DOI 10.1017/S0334270000010791.
4. B. Fiedler, “Global Hopf bifurcation in networks with fast feedback cycles,” Discrete and Continuous Dynamical Systems - S 14, 177–203 (2021), DOI 10.3934/dcdss.2020344.
5. R. J. Field, “Oregonator,” Scholarpedia 2, 1386 (2007), DOI 10.4249/scholarpedia.1386.
6. R. J. Field, R. M. Mazo, and N. Manz, “Science, serendipity, coincidence, and the Oregonator at the University of Oregon, 1969–1974,” Chaos 32, 052101 (2022), DOI 10.1063/5.0087455.
