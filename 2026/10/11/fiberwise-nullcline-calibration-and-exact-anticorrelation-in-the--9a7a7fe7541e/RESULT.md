# Fiberwise nullcline calibration and exact anticorrelation in the Brusselator
## Finding
Consider the classical Brusselator
\[
\dot x=a-(b+1)x+x^2y,
\qquad
\dot y=bx-x^2y,
\]
with
\[
a>0,\qquad b>0.
\]

Let \(\mu\) be a compactly supported invariant Borel probability measure whose support is contained in the strictly positive quadrant, and write
\[
S=x+y.
\]

Then the total-concentration fibers satisfy the exact calibration
\[
\boxed{
\mathbb E_\mu[x\mid S]=a
}.
\]
Equivalently,
\[
\mathbb E_\mu[y\mid S]=S-a.
\]

The activator fibers satisfy a second exact calibration:
\[
\boxed{
\mathbb E_\mu[y\mid x]
=
\frac{(b+1)x-a}{x^2}
}.
\]
The right-hand side is exactly the \(x\)-nullcline viewed as a graph over \(x\).

These two conditional laws imply the universal stationary anticorrelation identities
\[
\boxed{
\operatorname{Cov}_\mu(x,y)
=
-\operatorname{Var}_\mu(x)
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(y)
=
\operatorname{Var}_\mu(S)
+
\operatorname{Var}_\mu(x)
}.
\]

Because
\[
\dot S=a-x,
\]
one also has the exact speed defect
\[
\boxed{
\operatorname{Var}_\mu(x)
=
\mathbb E_\mu[\dot S^2]
}.
\]

The activator-nullcline calibration gives a second fluctuation defect. Define
\[
F(x)=\frac{(b+1)x-a}{x^2}.
\]
Then
\[
y-F(x)=\frac{\dot x}{x^2},
\]
and therefore
\[
\boxed{
\operatorname{Var}_\mu(y)
-
\operatorname{Var}_\mu(F(x))
=
\mathbb E_\mu\!\left[\frac{\dot x^2}{x^4}\right]
}.
\]

Every non-equilibrium compact stationary state satisfies
\[
\operatorname{Var}_\mu(y)
>
\operatorname{Var}_\mu(x)
>
0,
\]
and
\[
\operatorname{Cov}_\mu(x,y)<0.
\]

Moreover, compact positivity gives a positive lower bound on \(y\). Since
\[
F(x)=\mathbb E_\mu[y\mid x]>0
\]
on the stationary \(x\)-support,
\[
\boxed{
x>\frac{a}{b+1}
}
\]
throughout that support.

For the standard oscillatory parameters
\[
a=1,\qquad b=3,
\]
every compact positive stationary state is therefore supported in
\[
x>\frac14,
\]
and every non-equilibrium one has strictly larger \(y\)-variance than \(x\)-variance.

## Assumptions and scope
The invariant measure is compactly supported inside
\[
(0,\infty)^2.
\]
This ensures that \(x\) is bounded away from zero, so the normalized residual
\[
\dot x/x^2
\]
is square-integrable and the nullcline graph \(F(x)\) is bounded on the stationary support.

The equations are the standard nondimensional Brusselator equations introduced in the classical Prigogine–Lefever model. The foundational article was published on 15 February 1968.

The result is classified under primary MSC \(34C35\), matching a same-object mathematical treatment of the Brusselator differential system.

The result does not assert the existence of a non-equilibrium invariant measure for every parameter pair. In the classical phase portrait, the equilibrium loses stability through a Hopf bifurcation at
\[
b=a^2+1,
\]
and the oscillatory regime contains a stable limit cycle.

## Proof
Summing the two equations gives
\[
\dot S=a-x.
\]

Take any continuous function \(\phi\) on the compact \(S\)-range and choose a continuously differentiable antiderivative \(H\) with
\[
H'(S)=\phi(S).
\]
Then
\[
LH=\phi(S)(a-x),
\]
where \(L\) is the generator of the flow. Invariance gives
\[
\mathbb E_\mu[\phi(S)(a-x)]=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[x\mid S]=a.
\]
Since
\[
y=S-x,
\]
it follows that
\[
\mathbb E_\mu[y\mid S]=S-a.
\]

The residual
\[
x-a=-\dot S
\]
has conditional mean zero given \(S\). Therefore it is orthogonal to every square-integrable function of \(S\), and in particular
\[
\operatorname{Cov}(x,S)=0.
\]
Using
\[
y=S-x
\]
gives
\[
\operatorname{Cov}(x,y)
=
\operatorname{Cov}(x,S)-\operatorname{Var}(x)
=
-\operatorname{Var}(x).
\]
Likewise,
\[
\operatorname{Var}(y)
=
\operatorname{Var}(S-x)
=
\operatorname{Var}(S)+\operatorname{Var}(x).
\]
Because
\[
\mathbb E[x]=a,
\]
the identity
\[
\dot S=a-x
\]
also gives
\[
\operatorname{Var}(x)
=
\mathbb E[\dot S^2].
\]

For the second calibration, let \(\psi\) be continuous on the compact \(x\)-range and choose an antiderivative \(K\) with
\[
K'(x)=\psi(x).
\]
Then
\[
LK
=
\psi(x)
\left[
a-(b+1)x+x^2y
\right].
\]
Invariance implies
\[
\mathbb E_\mu
\left[
\psi(x)
\left(
a-(b+1)x+x^2y
\right)
\right]
=
0
\]
for every \(\psi\). Thus
\[
a-(b+1)x+x^2\mathbb E_\mu[y\mid x]=0,
\]
and, since \(x>0\),
\[
\mathbb E_\mu[y\mid x]
=
\frac{(b+1)x-a}{x^2}
=
F(x).
\]

Conditional orthogonality now yields
\[
\operatorname{Var}(y)
=
\operatorname{Var}(F(x))
+
\mathbb E[(y-F(x))^2].
\]
The differential equation gives
\[
y-F(x)=\frac{\dot x}{x^2},
\]
so
\[
\operatorname{Var}(y)
-
\operatorname{Var}(F(x))
=
\mathbb E\!\left[\frac{\dot x^2}{x^4}\right].
\]

We classify the equality cases used in the strict statements.

If
\[
\operatorname{Var}(x)=0,
\]
then \(x=a\) almost surely. Invariance makes \(x\) constant along support trajectories, and the \(x\)-equation forces
\[
y=\frac ba.
\]
Thus the measure is supported on the unique equilibrium
\[
\left(a,\frac ba\right).
\]

If
\[
\operatorname{Var}(S)=0,
\]
then \(S\) is constant. Since
\[
\dot S=a-x,
\]
we again obtain \(x=a\), and hence equilibrium support.

Therefore every non-equilibrium compact stationary state satisfies
\[
\operatorname{Var}(x)>0,
\qquad
\operatorname{Var}(S)>0,
\]
which proves
\[
\operatorname{Var}(y)>\operatorname{Var}(x)>0
\]
and strict negative covariance.

Finally, compact support in the positive quadrant gives
\[
y\ge y_{\min}>0
\]
on the support. Hence
\[
F(x)=\mathbb E[y\mid x]\ge y_{\min}>0
\]
for the stationary \(x\)-law, and continuity of \(F\) extends the inequality to its support. Thus
\[
(b+1)x-a>0,
\]
so
\[
x>\frac{a}{b+1}.
\]

## Verification
The accompanying checker verifies the algebraic identities with exact rational arithmetic and sparse polynomials.

It checks directly that
\[
\dot S=a-x
\]
when
\[
S=x+y.
\]

It verifies the cleared-denominator nullcline residual
\[
x^2(y-F(x))
=
a-(b+1)x+x^2y
=
\dot x.
\]

It also verifies the abstract covariance consequences of
\[
\mathbb E[x\mid S]=a:
\]
namely
\[
\operatorname{Cov}(x,S)=0,
\qquad
\operatorname{Cov}(x,y)=-\operatorname{Var}(x),
\]
and
\[
\operatorname{Var}(y)=\operatorname{Var}(S)+\operatorname{Var}(x).
\]

For
\[
a=1,\qquad b=3,
\]
it confirms the exact stationary lower barrier
\[
\frac{a}{b+1}=\frac14.
\]

The stored checker output is `VERIFY_OK`.

The conditional-expectation statements and equality classification are analytic consequences of invariance and compact positivity; they are not inferred from finite trajectory sampling.

## Relationship to prior work
Prigogine and Lefever introduced the Brusselator reaction mechanism in 1968. Their work establishes the autocatalytic model and its symmetry-breaking instability framework.

Llibre and Valls later study exactly the polynomial Brusselator system
\[
\dot x=a-(b+1)x+x^2y,
\qquad
\dot y=bx-x^2y
\]
from the viewpoint of Liouvillian and analytic first integrals. Their open mathematical treatment classifies the system under MSC \(34C35\) and \(34D30\). Its stated results concern integrability rather than invariant-measure conditional moments.

A complete recent global phase-portrait classification studies the same two-parameter system, its unique finite equilibrium, the Hopf curve
\[
b=a^2+1,
\]
and the globally attracting limit cycle in the oscillatory regime. Full-document searches of that article did not locate conditional-expectation, expectation, covariance, variance, moment, or average formulations matching the accepted result.

Ponzo and Wax provide a classical mathematical analysis of the biochemical model and are cited in the modern global classification for the uniqueness argument for the limit cycle.

The accepted statement is different from equilibrium stability, Hopf bifurcation, limit-cycle existence, phase-portrait classification, and integrability. It gives two exact stationary disintegrations and converts them into universal fluctuation and covariance identities that apply to every compact positive invariant probability measure.

## Limitations
The theorem assumes compact support inside the strictly positive quadrant. It does not address invariant measures on extensions of the polynomial flow that leave the chemically meaningful positive region.

The support barrier
\[
x>\frac{a}{b+1}
\]
is a necessary stationary constraint, not a sufficient condition for oscillation.

The result does not determine the limit-cycle period, amplitude, phase distribution, or full invariant density.

The foundational 1968 article is used for provenance, equation family, and the verified publication date rather than for a blanket whole-document noncoverage assertion.

The conditional identities are short consequences of the equations, so an equivalent observation could remain in unindexed chemical-oscillation literature.

## References
1. I. Prigogine and R. Lefever, “Symmetry Breaking Instabilities in Dissipative Systems. II,” The Journal of Chemical Physics 48, 1695–1700 (1968), DOI 10.1063/1.1668896.
2. J. Llibre and C. Valls, “Liouvillian and Analytic First Integrals for the Brusselator System,” Journal of Nonlinear Mathematical Physics 19, 247–254 (2012), DOI 10.1142/S1402925112500167.
3. T. M. P. de Abreu and J. Llibre, “Classification of Global Phase Portraits for the Brusselator System,” Journal of Dynamical and Control Systems 32, article 21 (2026), DOI 10.1007/s10883-026-09780-5.
4. P. J. Ponzo and N. Wax, “Note on a model of a biochemical reaction,” Journal of Mathematical Analysis and Applications 66, 354–357 (1978), DOI 10.1016/0022-247X(78)90238-X.
