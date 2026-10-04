# Exact speed-weighted fold balance in the Koper mixed-mode oscillator
## Finding
Consider the symmetric Koper system
\[
\varepsilon\dot x=y-c(x),\qquad
\dot y=kx-2(y+\lambda)+z,\qquad
\dot z=\delta(\lambda+y-z),
\]
where
\[
c(x)=x^3-3x,
\qquad
\varepsilon>0,\qquad
\delta>0,\qquad
k<0.
\]

Every compactly supported invariant Borel probability measure \(\mu\) satisfies the two exact regressions
\[
\boxed{\mathbb E_\mu[y\mid x]=c(x)}
\]
and
\[
\boxed{\mathbb E_\mu[y\mid z]=z-\lambda}.
\]

The corresponding regression residuals are exactly coordinate speeds:
\[
y-c(x)=\varepsilon\dot x,
\qquad
y-(z-\lambda)=\frac{\dot z}{\delta}.
\]
Therefore
\[
\boxed{
\operatorname{Var}_\mu(y)
-
\operatorname{Var}_\mu(c(x))
=
\varepsilon^2\mathbb E_\mu[\dot x^2]
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(y)
-
\operatorname{Var}_\mu(z)
=
\frac1{\delta^2}\mathbb E_\mu[\dot z^2]
}.
\]

More strongly, the three coordinate speeds obey the exact slope balance
\[
\boxed{
k\,
\mathbb E_\mu[
(c'(x)-\delta\varepsilon)\dot x^2
]
=
(2+\delta)
\mathbb E_\mu[\dot y^2]
}.
\]

Each of
\[
\mathbb E_\mu[\dot x^2],\qquad
\mathbb E_\mu[\dot y^2],\qquad
\mathbb E_\mu[\dot z^2]
\]
vanishes exactly for probability measures supported on equilibria.

Hence every compact stationary state that is not equilibrium-supported satisfies
\[
\mathbb E_\mu[\dot x^2]>0,\qquad
\mathbb E_\mu[\dot y^2]>0,\qquad
\mathbb E_\mu[\dot z^2]>0.
\]
Because \(k<0\), the slope balance then gives
\[
\mathbb E_\mu[
(c'(x)-\delta\varepsilon)\dot x^2
]<0.
\]
Since
\[
c'(x)=3x^2-3,
\]
the measure must assign positive mass to
\[
\boxed{
|x|<
\sqrt{1+\frac{\delta\varepsilon}{3}}
}.
\]

The critical manifold
\[
y=c(x)
\]
has folds at
\[
x=\pm1.
\]
Thus every genuinely recurrent compact stationary state penetrates an explicit enlargement of the central fold strip.

For the classical parameter
\[
k=-10
\]
with
\[
\delta=1,
\]
the strip is
\[
|x|<\sqrt{\frac{31}{30}}
\approx1.016530
\]
when
\[
\varepsilon=0.1,
\]
and
\[
|x|<\sqrt{\frac{301}{300}}
\approx1.001665
\]
when
\[
\varepsilon=0.01.
\]

In particular, every nonconstant periodic orbit enters the corresponding strip.

## Assumptions and scope
The measure \(\mu\) is invariant under the autonomous Koper flow and supported on a compact subset of \(\mathbb R^3\). Compact support makes all polynomial observables and their derivatives integrable.

The symmetric formulation used here is affinely equivalent to the standard Koper model
\[
\varepsilon_1\dot x=ky-x^3+3x-\lambda,\qquad
\dot y=x-2y+z,\qquad
\dot z=\varepsilon_2(y-z).
\]
The symmetric coordinates expose the cubic critical manifold
\[
y=x^3-3x
\]
with folds at
\[
x=\pm1.
\]

The earliest verified public source for this three-variable autonomous Van der Pol–Duffing Koper model is 1 January 1995. Later mathematical treatments describe it as a prototype for mixed-mode oscillations, folded-node dynamics, singular Hopf bifurcation, and Shilnikov homoclinic behavior.

The result is stated for the mixed-mode regime
\[
k<0,
\]
which is the regime emphasized in the mathematical literature. The two regression identities and their variance defects remain valid for nonzero \(k\) of either sign; the direction of the fold-strip conclusion reverses when \(k>0\).

## Proof
Let \(L\) denote the generator of the flow.

For any continuous function \(\phi\) on the compact \(x\)-range, choose a continuously differentiable antiderivative \(H\) satisfying
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
\frac{\phi(x)}{\varepsilon}
(y-c(x)).
\]
Invariance gives
\[
\mathbb E_\mu[
\phi(x)(y-c(x))
]=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[y\mid x]=c(x).
\]

Likewise, for any continuous function \(\psi\) on the compact \(z\)-range and an antiderivative \(K\),
\[
LK
=
\delta\psi(z)(\lambda+y-z).
\]
Thus
\[
\mathbb E_\mu[y\mid z]=z-\lambda.
\]

Conditional orthogonality now gives
\[
\operatorname{Var}(y)
=
\operatorname{Var}(c(x))
+
\mathbb E[(y-c(x))^2],
\]
which is the first variance defect. The second follows identically from
\[
y-(z-\lambda)=\frac{\dot z}{\delta}.
\]

We next derive the slope balance.

Differentiate the \(y\)-equation along trajectories:
\[
\ddot y
=
k\dot x-2\dot y+\dot z.
\]
Using
\[
z=\dot y-kx+2y+2\lambda
\]
in the \(z\)-equation gives
\[
\dot z
=
\delta(kx-y-\dot y-\lambda).
\]
Therefore
\[
\ddot y
+
(2+\delta)\dot y
+
\delta y
=
k\dot x+\delta kx-\delta\lambda.
\]

Multiply by \(\dot y\) and average under \(\mu\). Stationarity gives
\[
\mathbb E[\ddot y\,\dot y]=0,
\qquad
\mathbb E[y\dot y]=0,
\qquad
\mathbb E[\dot y]=0.
\]
Hence
\[
(2+\delta)\mathbb E[\dot y^2]
=
k\mathbb E[\dot x\,\dot y]
+
\delta k\mathbb E[x\dot y].
\]

From
\[
y=c(x)+\varepsilon\dot x
\]
we obtain
\[
\dot y=c'(x)\dot x+\varepsilon\ddot x.
\]
Stationarity of
\[
\frac12\dot x^2
\]
gives
\[
\mathbb E[\dot x\,\ddot x]=0,
\]
so
\[
\mathbb E[\dot x\,\dot y]
=
\mathbb E[c'(x)\dot x^2].
\]

Stationarity of \(xy\) gives
\[
\mathbb E[x\dot y]
=
-\mathbb E[\dot x\,y].
\]
Using the first regression,
\[
\mathbb E[\dot x\,c(x)]=0,
\]
because it is the stationary average of an antiderivative derivative. Thus
\[
\mathbb E[\dot x\,y]
=
\varepsilon\mathbb E[\dot x^2].
\]
Substitution yields
\[
(2+\delta)\mathbb E[\dot y^2]
=
k\mathbb E[
(c'(x)-\delta\varepsilon)\dot x^2
].
\]

We now classify the zero cases.

If
\[
\mathbb E[\dot x^2]=0,
\]
then \(x\) is constant on every support trajectory. The first equation makes \(y=c(x)\) constant, the second then makes \(z\) constant, and the third forces the equilibrium relation.

If
\[
\mathbb E[\dot z^2]=0,
\]
then \(z\) is constant and the third equation gives
\[
y=z-\lambda,
\]
so \(y\) is constant. The second equation then gives
\[
kx=z,
\]
so \(x\) is constant because \(k\ne0\). Hence the trajectory is an equilibrium.

If
\[
\mathbb E[\dot y^2]=0,
\]
then \(y\) is constant and
\[
z=-kx+2(y+\lambda).
\]
Differentiating gives
\[
\dot z=-k\dot x.
\]
The third equation then yields the scalar linear relation
\[
\dot x
=
-\delta x
+
\frac{\delta(y+\lambda)}{k}.
\]
Every nonconstant solution of this equation is unbounded in backward time. A trajectory in compact invariant support is bounded and complete, so \(x\), and hence \(z\), must be constant. Thus the trajectory is an equilibrium.

Conversely every equilibrium-supported probability measure makes all three speeds vanish.

For a non-equilibrium stationary state the right-hand side of the slope balance is strictly positive. Since \(k<0\),
\[
\mathbb E[
(c'(x)-\delta\varepsilon)\dot x^2
]<0.
\]
The integrand can be negative only where
\[
3x^2-3-\delta\varepsilon<0.
\]
Therefore the set
\[
|x|<
\sqrt{1+\frac{\delta\varepsilon}{3}}
\]
has positive \(\mu\)-measure.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic for the differential identities and exact rational arithmetic for the classical strip bounds.

It verifies
\[
\ddot y
+
(2+\delta)\dot y
+
\delta y
=
k\dot x+\delta kx-\delta\lambda
\]
directly from the vector field.

It verifies the algebraic substitutions used in the two regression residuals and the abstract identity
\[
\operatorname{Var}(A)-\operatorname{Var}(B)
=
\mathbb E[(A-B)^2]
\]
under the conditional-regression moment relations.

For
\[
\delta=1
\]
it confirms
\[
1+\frac{\delta\varepsilon}{3}
=
\frac{31}{30}
\]
at
\[
\varepsilon=\frac1{10},
\]
and
\[
1+\frac{\delta\varepsilon}{3}
=
\frac{301}{300}
\]
at
\[
\varepsilon=\frac1{100}.
\]

The stored checker output is `VERIFY_OK`.

The conditional expectations and equality-rigidity statements are analytic invariant-measure arguments, not finite numerical experiments.

## Relationship to prior work
Koper's 1995 paper introduces the three-variable autonomous Van der Pol–Duffing model and studies its cross-shaped bifurcation diagram and mixed-mode solutions.

A complete 2012 mathematical survey writes both the standard and symmetric Koper equations, identifies the cubic critical manifold and its folds, and develops folded-node and singular-Hopf mechanisms for mixed-mode oscillations. It reports the classical choice
\[
k=-10
\]
and the values
\[
\varepsilon=0.1
\quad\text{and}\quad
\varepsilon=0.01
\]
used in detailed bifurcation diagrams. Targeted document-wide searches found no conditional-expectation or variance formulation matching the accepted result.

Guckenheimer and Lizarraga establish Shilnikov homoclinic bifurcations in the Koper model and analyze the invariant-manifold geometry producing complicated mixed-mode behavior.

A later three-timescale treatment revisits the Koper system, classifies single- and double-epoch mixed-mode dynamics, and again centers the analysis on critical manifolds, folds, and singular geometry. Targeted full-text searches found no invariant-measure, variance, average, or conditional statement matching the present balance.

The accepted result complements that geometric literature. Instead of locating a particular periodic or homoclinic orbit, it constrains every compact stationary state. The speed-weighted slope identity forces any non-equilibrium recurrent state to penetrate a quantitative neighborhood of the two critical-manifold folds.

## Limitations
The fold-strip theorem is stated for
\[
k<0.
\]
For
\[
k>0,
\]
the same exact balance forces speed-weighted mass into the complementary slope-supercritical region instead.

The strip
\[
|x|<
\sqrt{1+\delta\varepsilon/3}
\]
is a necessary recurrence condition, not a sufficient condition for a mixed-mode oscillation or a Shilnikov orbit.

The theorem does not determine an MMO signature, period, return map, canard count, or bifurcation threshold.

The complete 1995 primary article was not available through the inspected open route, so it is used for model provenance, abstract-level comparison, and the verified publication date rather than blanket whole-document noncoverage.

Because the invariant-measure calculations are short, an equivalent observation could remain in unindexed slow–fast literature.

## References
1. M. T. M. Koper, “Bifurcations of mixed-mode oscillations in a three-variable autonomous Van der Pol-Duffing model with a cross-shaped phase diagram,” Physica D 80, 72–94 (1995), DOI 10.1016/0167-2789(95)90061-6.
2. M. Desroches, J. Guckenheimer, B. Krauskopf, C. Kuehn, H. M. Osinga, and M. Wechselberger, “Mixed-Mode Oscillations with Multiple Time Scales,” SIAM Review 54, 211–288 (2012), DOI 10.1137/100791233.
3. J. Guckenheimer and I. Lizarraga, “Shilnikov Homoclinic Bifurcation of Mixed-Mode Oscillations,” SIAM Journal on Applied Dynamical Systems 14, 764–786 (2015), DOI 10.1137/140972007, arXiv:1406.1813.
4. P. Kaklamanos, N. Popović, and K. U. Kristiansen, “Bifurcations of mixed-mode oscillations in three-timescale systems: An extended prototypical example,” Chaos 32 (2022), DOI 10.1063/5.0073353.
