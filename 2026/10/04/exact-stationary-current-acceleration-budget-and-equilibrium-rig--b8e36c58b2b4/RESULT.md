# Exact stationary current-acceleration budget and equilibrium rigidity in the Vallis model
## Finding
Consider the autonomous Vallis model
\[
\dot x=B y-C(x+p),\qquad
\dot y=xz-y,\qquad
\dot z=1-z-xy,
\]
with
\[
B>0,\qquad C>0,\qquad p\in\mathbb R.
\]

For every compactly supported invariant probability measure \(\mu\),
\[
\mathbb E_\mu[y\mid x]
=
\frac{C}{B}(x+p).
\]
Thus the wind-driven-current coordinate has an exact stationary linear regression against the east–west temperature contrast.

More strongly,
\[
\operatorname{Var}_\mu(y)
-
\left(\frac{C}{B}\right)^2
\operatorname{Var}_\mu(x)
=
\frac{1}{B^2}\mathbb E_\mu[\dot x^2]
\ge0.
\]
Equality holds exactly when \(\mu\) is supported on the equilibrium set, equivalently when it is a probability mixture of equilibrium atoms.

The temperature coordinates also satisfy
\[
\mathbb E_\mu\!\left[
y^2+
\left(z-\frac12\right)^2
\right]
=
\frac14.
\]
Combining the two identities yields the exact stationary current-acceleration budget
\[
\frac{C^2}{B^2}\mathbb E_\mu[(x+p)^2]
+
\frac{1}{B^2}\mathbb E_\mu[\dot x^2]
+
\mathbb E_\mu\!\left[
\left(z-\frac12\right)^2
\right]
=
\frac14.
\]

Therefore every compact invariant probability measure that is not supported on equilibria satisfies the strict inequality
\[
\operatorname{Var}_\mu(y)
>
\left(\frac{C}{B}\right)^2
\operatorname{Var}_\mu(x),
\]
and uses a strictly positive part of the universal quadratic temperature budget in current acceleration.

For the standard asymmetric parameter triple
\[
(B,C,p)=(102,3,0.83),
\]
the budget becomes
\[
\frac1{1156}\mathbb E[(x+0.83)^2]
+
\frac1{10404}\mathbb E[\dot x^2]
+
\mathbb E\!\left[
\left(z-\frac12\right)^2
\right]
=
\frac14.
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the autonomous Vallis flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of all polynomial test functions and makes each support trajectory bounded and complete.

The theorem covers arbitrary constant asymmetry \(p\). It includes the symmetric case \(p=0\), which is affinely equivalent to a Lorenz system, and the standard asymmetric case \(p=0.83\) considered in rigorous chaos work.

The earliest verified public source date for the Vallis El Niño model is 11 April 1986.

The temperature-circle balance is used as a published-prior ingredient rather than claimed as new. A 2008 localization paper computes the same quadratic Lie derivative in shifted coordinates, which directly implies the integrated stationary circle identity. The new statement assessed here is the coordinatewise current disintegration, its exact acceleration defect, the equilibrium-only equality classification, and the resulting three-term stationary budget.

## Proof
Let
\[
k=\frac{C}{B}.
\]
For any continuous function \(\phi\) on the compact \(x\)-range of the support, choose a continuously differentiable antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
For the generator \(L\),
\[
LH
=
\phi(x)\bigl(By-C(x+p)\bigr).
\]
Invariance gives
\[
0
=
\int LH\,d\mu
=
B\,\mathbb E_\mu\!\left[
\phi(x)\bigl(y-k(x+p)\bigr)
\right].
\]
Since this holds for every continuous \(\phi\),
\[
\mathbb E_\mu[y\mid x]=k(x+p).
\]

Because
\[
\frac{\dot x}{B}
=
y-k(x+p),
\]
the conditional residual is exactly the normalized current speed. The conditional-expectation orthogonality gives
\[
\mathbb E_\mu\!\left[
\left(y-k(x+p)\right)^2
\right]
=
\operatorname{Var}_\mu(y)-k^2\operatorname{Var}_\mu(x).
\]
Hence
\[
\operatorname{Var}_\mu(y)-k^2\operatorname{Var}_\mu(x)
=
\frac1{B^2}\mathbb E_\mu[\dot x^2].
\]

We now classify equality. If
\[
\mathbb E_\mu[\dot x^2]=0,
\]
then \(\dot x=0\) on the invariant support. Along each support trajectory, \(x\) is constant, and the equation \(\dot x=0\) makes
\[
y=k(x+p)
\]
constant as well. Therefore \(\dot y=0\), so
\[
xz=y.
\]
If \(x\ne0\), this fixes \(z\), and then \(\dot z=0\); the trajectory is an equilibrium.

If \(x=0\), constancy of \(y\) together with
\[
\dot y=-y
\]
forces \(y=0\), hence \(p=0\). The remaining equation is
\[
\dot z=1-z.
\]
Its only bounded complete trajectory is \(z=1\). Thus this case is also an equilibrium. Consequently equality forces the support to be contained in the equilibrium set. Conversely every equilibrium atom, and every probability mixture of equilibrium atoms, has \(\dot x=0\) and realizes equality.

For completeness, the quadratic temperature balance follows directly from
\[
L\!\left(\frac{y^2+z^2}{2}\right)
=
-y^2+z-z^2.
\]
Stationarity gives
\[
\mathbb E_\mu[y^2+z^2-z]=0,
\]
equivalently
\[
\mathbb E_\mu\!\left[
y^2+
\left(z-\frac12\right)^2
\right]
=
\frac14.
\]

Finally, from
\[
y=k(x+p)+\frac{\dot x}{B}
\]
and stationarity of
\[
\frac12(x+p)^2,
\]
we have
\[
\mathbb E_\mu[(x+p)\dot x]=0.
\]
Therefore
\[
\mathbb E_\mu[y^2]
=
k^2\mathbb E_\mu[(x+p)^2]
+
\frac1{B^2}\mathbb E_\mu[\dot x^2].
\]
Substitution into the temperature-circle balance gives
\[
\frac{C^2}{B^2}\mathbb E_\mu[(x+p)^2]
+
\frac1{B^2}\mathbb E_\mu[\dot x^2]
+
\mathbb E_\mu\!\left[
\left(z-\frac12\right)^2
\right]
=
\frac14.
\]
The strict variance inequality for every non-equilibrium-supported measure follows from the equality classification.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic.

It verifies
\[
L\!\left(\frac{y^2+z^2}{2}\right)
=
-y^2+z-z^2
\]
and
\[
L\!\left(\frac{(x+p)^2}{2}\right)
=
(x+p)\bigl(By-C(x+p)\bigr).
\]

It also verifies the pointwise identity
\[
\frac{\dot x}{B}
=
y-\frac{C}{B}(x+p)
\]
after clearing denominators, and checks the standard asymmetric coefficients
\[
\frac{C^2}{B^2}=\frac1{1156},
\qquad
\frac1{B^2}=\frac1{10404}
\]
for
\[
(B,C)=(102,3).
\]

The stored checker output is `VERIFY_OK`.

The checker confirms the algebraic certificates. The conditional expectation step uses arbitrary one-variable test functions, while equality rigidity uses invariant support and bounded complete trajectories. Neither is inferred from finite numerical sampling.

## Relationship to prior work
Vallis introduced the three-variable El Niño model in 1986 as a physically motivated mechanism for irregular ENSO-like events. Later work writes the autonomous normalized system in the form used here.

A 2008 localization paper is the strongest implication-level prior comparison. In the shifted height coordinate it uses a quadratic localizing function whose Lie derivative is exactly the temperature-circle defect. Translating back gives
\[
L(y^2+z^2)
=
-2(y^2+z^2-z).
\]
Thus the integrated stationary identity
\[
\mathbb E[y^2+z^2-z]=0
\]
is already implied by that published computation and is not claimed as new.

The same 2008 paper derives pointwise localizing regions for all compact invariant sets, including an ellipsoidal region in the temperature variables. It does not state the conditional law
\[
\mathbb E[y\mid x]=\frac{C}{B}(x+p),
\]
the exact variance defect by current acceleration, the equilibrium-only equality classification, or the three-term stationary budget involving \(\mathbb E[\dot x^2]\).

A 2014 mathematical treatment studies periodic solutions of the seasonally forced Vallis system through averaging theory. A 2015 full rigorous-numerics study proves horseshoes for the autonomous system at both \(p=0\) and \(p=0.83\), and explicitly records the affine equivalence to Lorenz when \(p=0\). This equivalence was included in the prior-work comparison: no novelty is claimed merely for a symmetric Lorenz-type integrated quadratic balance.

Later work studies bifurcation, multistability, fractional variants, and invariant algebraic surfaces. Those topics do not implication-wise supply the stationary current-acceleration decomposition accepted here.

## Limitations
The theorem concerns compactly supported invariant probability measures for the autonomous constant-\(p\) model. It does not treat the periodically forced seasonal-cycle equation as a stationary autonomous measure problem.

The result supplies exact second-order and conditional-mean constraints but does not determine the full invariant density, Lyapunov spectrum, or existence of a chaotic attractor for every parameter triple.

The temperature-circle balance is prior-implied and is included only as an input to the current-acceleration budget. The originality claim does not extend to that integrated balance or to the known affine Lorenz equivalence at \(p=0\).

A differently phrased current-regression or acceleration-budget identity could remain in unindexed climate-dynamics literature. The inspected localization, periodic-orbit, rigorous-chaos, bifurcation, and invariant-algebraic-surface sources did not expose such a statement.

## References
1. G. K. Vallis, “El Niño: a chaotic dynamical system?”, Science 232, 243–245 (1986), DOI 10.1126/science.232.4747.243.
2. G. K. Vallis, “Conceptual models of El Niño and the Southern Oscillation”, Journal of Geophysical Research 93, 13979–13991 (1988), DOI 10.1029/JC093iC11p13979.
3. A. P. Krishchenko and K. E. Starkov, “Localization of Compact Invariant Sets of Nonlinear Time-Varying Systems”, International Journal of Bifurcation and Chaos 18, 1599–1604 (2008), DOI 10.1142/S021812740802121X.
4. R. D. Euzébio and J. Llibre, “Periodic solutions of El Niño model through the Vallis differential system”, Discrete and Continuous Dynamical Systems 34, 3455–3469 (2014), DOI 10.3934/dcds.2014.34.3455.
5. B. M. Garay and B. Indig, “Chaos in Vallis’ asymmetric Lorenz model for El Niño”, Chaos, Solitons & Fractals 75, 253–262 (2015), DOI 10.1016/j.chaos.2015.02.015.
6. K. Rajagopal, S. Jafari, V.-T. Pham, Z. Wei, D. Premraj, K. Thamilmaran, and A. Karthikeyan, “Antimonotonicity, Bifurcation and Multistability in the Vallis Model for El Niño”, International Journal of Bifurcation and Chaos 29, 1950032 (2019), DOI 10.1142/S0218127419500329.
7. J. Yang, W. Tan, and Z. Wei, “Invariant Algebraic Surfaces of the Vallis System”, Applied Mathematics and Mechanics 43, 84–93 (2022), DOI 10.21656/1000-0887.420112.
