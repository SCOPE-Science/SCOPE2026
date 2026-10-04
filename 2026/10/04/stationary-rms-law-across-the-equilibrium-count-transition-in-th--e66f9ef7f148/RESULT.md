# Stationary RMS law across the equilibrium-count transition in the Chen–Wang flow
## Finding
Consider the Chen–Wang system
\[
\dot x=y,\qquad
\dot y=z,\qquad
\dot z=-y-x^2-xz+3y^2+a,
\]
with \(a\in\mathbb R\).

Every compactly supported invariant probability measure \(\mu\) satisfies the conditional stationary laws
\[
\mathbb E_\mu[y\mid x]=0,
\qquad
\mathbb E_\mu[z\mid y]=0,
\]
and the exact RMS identity
\[
\mathbb E_\mu[x^2]
=
a+4\,\mathbb E_\mu[y^2].
\]

This identity changes meaning exactly at the parameter value where the number of finite equilibria changes.

If \(a>0\), the two equilibria are
\[
e_\pm=(\pm\sqrt a,0,0).
\]
Then
\[
\mathbb E_\mu[x^2]\ge a,
\]
with equality exactly for convex mixtures of the two equilibrium atoms. Every other compact invariant probability measure satisfies
\[
\mathbb E_\mu[x^2]>a,
\]
so it gives positive mass to
\[
|x|>\sqrt a.
\]
It also gives positive mass to both \(y>0\) and \(y<0\).

If \(a=0\), every compact invariant probability measure satisfies
\[
\mathbb E_\mu[x^2]=4\,\mathbb E_\mu[y^2].
\]

If \(a<0\), every compact invariant probability measure, if one exists, satisfies the strict no-equilibrium floor
\[
\mathbb E_\mu[y^2]>-\frac a4.
\]
At the published chaotic example \(a=-0.05=-1/20\), this gives
\[
\sqrt{\mathbb E_\mu[y^2]}
>
\frac{1}{4\sqrt5}
\approx 0.1118033989.
\]

Consequently, every nonconstant periodic orbit for \(a>0\) exits the slab
\[
|x|\le\sqrt a
\]
and crosses \(y=0\) at least twice in each least period. Every periodic orbit for \(a<0\), if one exists, obeys the same strict RMS floor for \(y=\dot x\).

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the Chen–Wang flow and supported on compact subsets of \(\mathbb R^3\). Compact support guarantees integrability of the polynomial and one-variable antiderivative test functions used below.

The normalization adopted here is the one used explicitly in the later rigorous Chen–Wang literature:
\[
\dot z=-y-x^2-xz+3y^2+a.
\]
The 2012 preprint is the earliest verified public source for the system and its equilibrium-count transition. Its PDF displays a minus sign before the parameter in the equation while simultaneously stating the equilibrium behavior corresponding to the plus-sign normalization. The later rigorous papers consistently use the plus-sign normalization above; the proof here depends only on that explicitly stated later normalization.

The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

## Proof
Let \(L\) denote the generator of the flow. If \(\mu\) is compactly supported and invariant, then
\[
\int LH\,d\mu=0
\]
for every continuously differentiable \(H\) defined on a neighborhood of the compact support.

Let \(\phi\) be continuous on the compact \(x\)-range and choose an antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH=\phi(x)y,
\]
so
\[
\mathbb E_\mu[\phi(x)y]=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[y\mid x]=0.
\]

Likewise, for a continuous \(\psi\) on the compact \(y\)-range and an antiderivative \(K\) with
\[
K'(y)=\psi(y),
\]
one has
\[
LK=\psi(y)z.
\]
Therefore
\[
\mathbb E_\mu[z\mid y]=0.
\]

Now define the polynomial
\[
F=z+xy+x.
\]
Direct differentiation gives the exact coboundary
\[
LF
=
a-x^2+4y^2.
\]
Integrating against \(\mu\) proves
\[
\mathbb E_\mu[x^2]
=
a+4\,\mathbb E_\mu[y^2].
\]

Assume \(a>0\). The identity immediately gives
\[
\mathbb E_\mu[x^2]\ge a.
\]
Equality is equivalent to
\[
y=0
\]
almost surely. The support of an invariant probability measure is invariant along every complete trajectory contained in that compact support. Hence a support contained in \(y=0\) must also satisfy
\[
\dot y=z=0.
\]
On \(y=z=0\), tangency of \(z=0\) requires
\[
0=\dot z=a-x^2.
\]
Thus the support is contained in
\[
\{e_+,e_-\}.
\]
Conversely every convex mixture of those equilibrium atoms is invariant and realizes equality.

If the measure is not such a mixture, then
\[
\mathbb E_\mu[x^2]>a.
\]
If it were supported in \(|x|\le\sqrt a\), its second moment could not exceed \(a\), so positive mass must lie in \(|x|>\sqrt a\).

Also
\[
\mathbb E_\mu[y]=0
\]
because \(Lx=y\). Outside the equality class,
\[
\mathbb E_\mu[y^2]>0.
\]
Therefore \(y\) has positive mass on both signs.

Now assume \(a<0\). From
\[
\mathbb E_\mu[x^2]
=
a+4\,\mathbb E_\mu[y^2]
\]
and nonnegativity of the left side,
\[
\mathbb E_\mu[y^2]\ge-\frac a4.
\]
Equality would force \(x=0\) almost surely. Support invariance would then force successively
\[
y=0,\qquad z=0.
\]
But at the origin
\[
\dot z=a\ne0,
\]
contradicting invariance. The lower bound is therefore strict.

Finally, a nonconstant periodic orbit carries its normalized orbit measure. For \(a>0\) it cannot be an equilibrium mixture, so it reaches \(|x|>\sqrt a\). The continuous periodic function \(y=\dot x\) has zero mean and is not identically zero; therefore it takes both signs and has at least two zeros on the periodic circle.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients and only the Python standard library.

It verifies
\[
Lx=y,\qquad Ly=z,
\]
and the critical certificate
\[
L(z+xy+x)=a-x^2+4y^2.
\]

It also checks the equilibrium substitution \(y=z=0\), \(x^2=a\), and the exact no-equilibrium benchmark
\[
a=-\frac1{20}
\quad\Longrightarrow\quad
-\frac a4=\frac1{80}.
\]

The stored checker output is `VERIFY_OK`.

The checker certifies the nonstandard algebraic step. The conditional identities use arbitrary one-variable test functions through antiderivatives on compact coordinate ranges, and the equality classifications use invariance of the compact support; neither step is a finite experiment.

## Relationship to prior work
Wang and Chen introduced the system to show that chaotic dynamics can persist while the number of equilibria is varied. Their publicly posted 2012 preprint gives the two-equilibrium, merged-equilibrium, and no-equilibrium parameter regimes and reports a chaotic no-equilibrium example.

Llibre, Oliveira, and Valls subsequently fixed the plus-sign normalization used here and studied Darboux integrability and the zero–Hopf bifurcation. Their full text proves nonexistence of invariant algebraic surfaces and Darboux first integrals and establishes two small periodic solutions for sufficiently small positive \(a\). It does not state an invariant-probability RMS law or the sharp equality classification above.

Oliveira and Valls later introduced a two-parameter generalization and analyzed Hopf and zero–Hopf bifurcations, periodic solutions, the flow at infinity, invariant algebraic surfaces, and analytic/Darboux integrability. Their full text again identifies the original Chen–Wang system as the one-parameter case and emphasizes the transition between zero and two finite equilibria.

Targeted semantic searches using the system name, the exact stationary identity, equilibrium-amplitude language, no-equilibrium RMS language, and periodic-orbit consequences returned no same-object statement implying the theorem above. The closest indexed results are structurally analogous stationary balances for different polynomial flows.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not prove that such a measure exists for every parameter value, classify unbounded trajectories, or give a period lower bound.

For \(a>0\), the theorem forces non-equilibrium compact recurrence outside the equilibrium-amplitude slab but does not force it to enter the interior of that slab.

For \(a<0\), the strict RMS bound is conditional on the existence of compact recurrence. The published chaotic examples motivate that regime numerically but are not used as a proof of existence here.

The earliest preprint contains a sign inconsistency between its displayed parameter term and its stated equilibrium locations. The normalization used in this result is independently fixed by the later rigorous full-text analyses.

## References
1. X. Wang and G. Chen, “Constructing a chaotic system with any number of equilibria,” arXiv:1201.5751, first posted 2012-01-27; later published in Nonlinear Dynamics 71, 429–436.
2. J. Llibre, R. D. S. Oliveira, and C. Valls, “On the integrability and the zero–Hopf bifurcation of a Chen–Wang differential system,” Nonlinear Dynamics 80, 353–361 (2015), DOI 10.1007/s11071-014-1873-4.
3. R. D. S. Oliveira and C. Valls, “Global dynamical aspects of a generalized Chen–Wang differential system,” Nonlinear Dynamics 84, 1497–1516 (2016), DOI 10.1007/s11071-015-2584-1.
