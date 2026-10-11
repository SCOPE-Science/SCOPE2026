# Sharp equilibrium-root RMS ceiling and stationary defect shell in the Ehrhard–Müller system
## Finding
Consider the Ehrhard–Müller system
\[
\dot x=\sigma(y-x),
\qquad
\dot y=rx-xz-y+c,
\qquad
\dot z=xy-z,
\]
with
\[
\sigma>0,
\qquad
c>0,
\qquad
r\in\mathbb R.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Then the three coordinate layers satisfy the exact stationary regressions
\[
\boxed{\mathbb E_\mu[y\mid x]=x},
\]
\[
\boxed{\mathbb E_\mu[xy\mid z]=z},
\]
and
\[
\boxed{\mathbb E_\mu[x(r-z)+c\mid y]=y}.
\]

Write
\[
m=\mathbb E_\mu[x]=\mathbb E_\mu[y]
\]
and
\[
h=\mathbb E_\mu[z].
\]
Stationarity forces the exact chain
\[
\boxed{
\mathbb E_\mu[z]
=
\mathbb E_\mu[x^2]
=
\mathbb E_\mu[xy]
=h
}.
\]
Because \(c>0\), every compact stationary state has
\[
\boxed{h>0}.
\]

The first regression has residual
\[
y-x=\frac{\dot x}{\sigma}.
\]
Consequently
\[
\boxed{
\operatorname{Var}_\mu(y)
=
\operatorname{Var}_\mu(x)
+
\mathbb E_\mu\!\left[\left(\frac{\dot x}{\sigma}\right)^2\right]
}.
\]
Define the nonnegative speed defect
\[
s=
\mathbb E_\mu\!\left[\left(\frac{\dot x}{\sigma}\right)^2\right].
\]
Then the quadratic energy
\[
V=\frac{x^2}{\sigma}+y^2+z^2
\]
gives the exact stationary shell
\[
\boxed{
\operatorname{Var}_\mu(z)+s
=
h(r-1-h)+cm
}.
\]

The height regression has its own exact dynamical residual:
\[
xy-z=\dot z.
\]
Hence
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

The defect shell yields a sharp parameter-only recurrence ceiling. Let \(\xi_+\) be the unique positive root of
\[
\xi^3-(r-1)\xi-c=0.
\]
Then every compact stationary state satisfies
\[
\boxed{
0<
\mathbb E_\mu[z]
=
\mathbb E_\mu[x^2]
\le
\xi_+^2
}.
\]
Equality is rigid:
\[
\mathbb E_\mu[z]=\xi_+^2
\]
holds if and only if
\[
\boxed{
\mu=\delta_{(\xi_+,\xi_+,\xi_+^2)}
}.
\]
Thus every other compact stationary state has
\[
\boxed{
\mathbb E_\mu[z]
=
\mathbb E_\mu[x^2]
<
\xi_+^2
}.
\]

The speed defect \(s\) vanishes exactly for invariant measures supported on equilibria. Therefore any stationary state carrying genuinely time-dependent recurrent dynamics has
\[
\operatorname{Var}(y)>
\operatorname{Var}(x).
\]

For the chaotic example displayed in the classical modern study,
\[
(\sigma,r,c)=(15,2000,1500),
\]
the positive equilibrium amplitude is the unique positive root of
\[
\xi^3-1999\xi-1500=0,
\]
namely
\[
\xi_+\approx45.0807456556.
\]
Thus every compact invariant state at these parameters obeys
\[
\boxed{
\mathbb E[z]
=
\mathbb E[x^2]
\le
2032.2736288672
},
\]
with strict inequality unless the invariant state is the positive-equilibrium atom.

## Assumptions and scope
The theorem concerns the standard Ehrhard–Müller equations with \(\sigma>0\) and nonsymmetric heating parameter \(c>0\). The heating parameter \(r\) is arbitrary real. Compact support guarantees all polynomial moments and generator tests used below.

No ergodicity assumption is required. The statements apply separately to equilibrium atoms, periodic-orbit measures, compact chaotic invariant measures, and convex mixtures.

The foundational natural-convection paper appeared in print in 1990. The checked bibliographic source resolves that print publication only to August 1990, so no day is invented. The structured source date uses the earliest checked day-resolved public release, 26 April 2006, when the foundational article was published online by Cambridge University Press.

A day-resolved 2016 mathematical treatment writes the exact system above and studies periodic and chaotic regimes. Its mathematical bibliography lists \(34A34\) first; that MSC2020 classification is used here.

## Proof
Let \(L\) denote the generator of the flow.

For any continuous function \(\phi\) on the compact \(x\)-projection of the support, choose an antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
\sigma\phi(x)(y-x).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)(y-x)]=0
\]
for every \(\phi\), hence
\[
\mathbb E_\mu[y\mid x]=x.
\]

The same antiderivative argument in \(z\) gives
\[
\mathbb E_\mu[xy-z\mid z]=0,
\]
so
\[
\mathbb E_\mu[xy\mid z]=z.
\]

Likewise, testing arbitrary antiderivatives of \(y\) gives
\[
\mathbb E_\mu[rx-xz-y+c\mid y]=0,
\]
which is
\[
\mathbb E_\mu[x(r-z)+c\mid y]=y.
\]

Averaging the \(x\)-equation gives
\[
\mathbb E[y]=\mathbb E[x]=m.
\]
Stationarity of \(x^2\) gives
\[
0
=
2\sigma\mathbb E[x(y-x)],
\]
so
\[
\mathbb E[xy]=\mathbb E[x^2].
\]
Averaging the \(z\)-equation gives
\[
\mathbb E[xy]=\mathbb E[z].
\]
Thus
\[
\mathbb E[z]
=
\mathbb E[x^2]
=
\mathbb E[xy]
=h.
\]

If \(h=0\), then
\[
\mathbb E[x^2]=0,
\]
so \(x=0\) on the support and \(m=0\). Averaging the \(y\)-equation would then give
\[
0=c,
\]
contrary to \(c>0\). Hence
\[
h>0.
\]

Write
\[
R=y-x=\frac{\dot x}{\sigma}.
\]
The first conditional regression gives
\[
\mathbb E[R\mid x]=0.
\]
Therefore \(R\) is orthogonal to every square-integrable function of \(x\), and
\[
\operatorname{Var}(y)
=
\operatorname{Var}(x)
+
\mathbb E[R^2].
\]
This is the first speed-defect identity.

Next differentiate
\[
V=\frac{x^2}{\sigma}+y^2+z^2.
\]
A direct substitution gives
\[
\dot V
=
2(1+r)xy
-2x^2
-2y^2
-2z^2
+2cy.
\]
Stationarity and the identities already proved yield
\[
0
=
2rh
-2\mathbb E[y^2]
-2\mathbb E[z^2]
+2cm.
\]
Since
\[
\mathbb E[y^2]=h+s,
\]
we obtain
\[
\mathbb E[z^2]
=
(r-1)h+cm-s.
\]
Subtracting \(h^2\) proves
\[
\operatorname{Var}(z)+s
=
h(r-1-h)+cm.
\]

For the second defect, write
\[
Q=xy-z=\dot z.
\]
The height regression gives
\[
\mathbb E[Q\mid z]=0.
\]
Since
\[
xy=z+Q,
\]
orthogonality gives
\[
\operatorname{Var}(xy)
=
\operatorname{Var}(z)+\mathbb E[Q^2]
\]
and
\[
\operatorname{Cov}(z,xy)=\operatorname{Var}(z).
\]

Now set
\[
q=\sqrt h>0.
\]
Cauchy–Schwarz gives
\[
m\le |m|\le q.
\]
Because the left side of the defect shell is nonnegative and \(c>0\),
\[
0
\le
h(r-1-h)+cm
\le
q^2(r-1-q^2)+cq.
\]
Hence
\[
q^3-(r-1)q-c\le0.
\]
The cubic
\[
f(q)=q^3-(r-1)q-c
\]
has exactly one positive zero. Indeed, \(f(0)=-c<0\); if \(r\le1\), then \(f\) is strictly increasing on the positive axis, while if \(r>1\), it first decreases from an already negative value and then increases to infinity. Denote its unique positive zero by \(\xi_+\). The preceding inequality therefore yields
\[
0<q\le\xi_+,
\]
which proves
\[
0<h\le\xi_+^2.
\]

Suppose equality holds. Then \(q=\xi_+\), so the upper comparison above is zero. Thus the shell itself and both inequalities used in the comparison are equalities. Therefore
\[
m=q,
\qquad
s=0,
\qquad
\operatorname{Var}(z)=0.
\]
Since
\[
\mathbb E[x^2]=q^2
\]
and
\[
\mathbb E[x]=q,
\]
we also have
\[
\operatorname{Var}(x)=0.
\]
The state is therefore concentrated at
\[
x=q,
\qquad
y=q,
\qquad z=q^2.
\]
The cubic equation for \(q\) is exactly the remaining equilibrium condition, so the measure is
\[
\delta_{(\xi_+,\xi_+,\xi_+^2)}.
\]
The converse is immediate.

Finally, if \(s=0\), continuity gives \(\dot x=0\) on the invariant support, hence \(y=x\) and both are constant along each support trajectory. The \(y\)-equation must also vanish there. The remaining scalar equation is
\[
\dot z=x^2-z.
\]
A nonconstant solution of this scalar equation cannot be a bounded complete recurrent trajectory. Poincaré recurrence therefore places invariant mass only where \(z=x^2\), and the support is contained in the equilibrium set. Conversely every equilibrium-supported measure has \(s=0\).

## Verification
The accompanying checker uses only the Python standard library and exact rational arithmetic, together with a deterministic bisection for the displayed numerical root.

It verifies the pointwise polynomial identity for
\[
\frac{d}{dt}
\left(
\frac{x^2}{\sigma}+y^2+z^2
\right),
\]
the exact stationary reduction to
\[
\operatorname{Var}(z)+s
=
h(r-1-h)+cm,
\]
and both orthogonal-residual variance formulas.

For the published example
\[
(r,c)=(2000,1500),
\]
it brackets and bisects the unique positive zero of
\[
\xi^3-1999\xi-1500
\]
and checks the displayed value of \(\xi_+^2\) to the stated precision.

The stored checker output is `VERIFY_OK`.

The invariant-measure conditional expectations, the uniqueness of the positive root, the equality classification, and the recurrence argument for zero speed defect are analytic proofs; they are not inferred from finite trajectory sampling.

## Relationship to prior work
Ehrhard and Müller derive the natural-convection model for a single-phase loop and show experimentally and analytically that it possesses stable, periodic, and chaotic regimes under symmetric and nonsymmetric heating.

A complete public full-text 2016 study writes exactly
\[
\dot x=\sigma(y-x),
\qquad
\dot y=rx-xz-y+c,
\qquad
\dot z=xy-z,
\]
fixes \(\sigma=15\), analyzes equilibria and neutral-stability curves, builds periodicity diagrams, computes Lyapunov exponents, and performs asymptotic limit-cycle analysis. It explicitly displays a chaotic attractor at
\[
(r,c)=(2000,1500).
\]
Targeted full-text searches found no occurrences of `invariant measure`, `moment`, `variance`, or `average`.

A 2026 same-system mathematical study classifies invariant algebraic surfaces of degree two and the corresponding global phase portraits in the Poincaré ball. Its stated results concern algebraic invariant surfaces and dynamics at infinity rather than invariant-measure moments.

The accepted result is not a new equilibrium, Hopf, Lyapunov-exponent, periodicity-diagram, invariant-surface, or chaos-existence theorem. It is an all-invariant-measures calibration: the height mean equals the fast-amplitude mean square, the coordinate mismatch contributes an exact speed defect, and these quantities combine into a sharp ceiling determined by the positive equilibrium root.

## Limitations
The theorem is conditional on compactly supported invariant probability measures and does not establish existence or uniqueness of a chaotic attractor for arbitrary parameters.

The sharp ceiling assumes \(c>0\). The symmetric-heating case \(c=0\) has additional symmetry and a different equality structure.

The theorem fixes selected first and second moments, not the full invariant distribution.

The foundational 1990 article was inspected through its public abstract and bibliographic record rather than a complete searchable full text in the checked route, so no blanket whole-document noncoverage claim is made for that source.

The 2026 invariant-algebraic-surface paper was compared through its public abstract and stated theorem scope rather than used for whole-document noncoverage.

Because the generator calculations are short, an equivalent stationary-moment identity could remain in unindexed literature.

## References
1. P. Ehrhard and U. Müller, “Dynamical behaviour of natural convection in a single-phase loop,” *Journal of Fluid Mechanics* 217, 487–518 (1990), DOI 10.1017/S0022112090000817.
2. J. Park, H. H. Lee, and J.-J. Baik, “Periodic and Chaotic Dynamics of the Ehrhard–Müller System,” *International Journal of Bifurcation and Chaos* 26, 1630015 (2016), DOI 10.1142/S0218127416300159.
3. J. Llibre and G. Rondón, “The dynamics of the Ehrhard–Müller system with invariant algebraic surfaces,” *Journal of Mathematical Physics* 67, 082701 (2026), DOI 10.1063/5.0281236; preprint arXiv:2505.12047.
