# Fiberwise flux calibration and exact anticorrelation in the Schnakenberg oscillator
## Finding
Consider the positive Schnakenberg kinetic system
\[
\dot u=a-u+u^2v,
\qquad
\dot v=b-u^2v,
\qquad
a>0,\quad b>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure on the nonnegative quadrant. Then the autocatalytic reaction flux is calibrated exactly on both concentration fibers:
\[
\boxed{
\mathbb E_\mu[u^2v\mid u]=u-a
}
\]
and
\[
\boxed{
\mathbb E_\mu[u^2v\mid v]=b
}.
\]

There is also an exact total-concentration calibration. With
\[
S=u+v,
\qquad
\beta=a+b,
\]
one has
\[
\boxed{
\mathbb E_\mu[u\mid S]=\beta
}.
\]

Consequently,
\[
\boxed{
\mathbb E_\mu[u]=\beta
},
\]
so every compact stationary state has mean autocatalyst concentration equal to the autocatalyst coordinate of the unique positive equilibrium
\[
p_*=
\left(
\beta,\frac{b}{\beta^2}
\right).
\]

Because \(0\le u\le S\), the conditional law implies
\[
S\ge\beta
\]
almost surely. In fact,
\[
\boxed{S>\beta\quad\mu\text{-almost surely}},
\]
because equality would force \(u=\beta\) and \(v=0\), while the \(v\)-fiber flux law excludes positive invariant mass at \(v=0\).

The centered autocatalyst is exactly the negative total-concentration speed:
\[
u-\beta=-\dot S.
\]
Since
\[
\mathbb E_\mu[u-\beta\mid S]=0,
\]
we obtain
\[
\boxed{
\operatorname{Var}_\mu(u)
=
\mathbb E_\mu[\dot S^2]
}
\]
and
\[
\boxed{
\operatorname{Cov}_\mu(S,u)=0
}.
\]

Since
\[
v=S-u,
\]
the covariance structure closes exactly:
\[
\boxed{
\operatorname{Cov}_\mu(u,v)
=
-\operatorname{Var}_\mu(u)
}
\]
and
\[
\boxed{
\operatorname{Var}_\mu(v)
=
\operatorname{Var}_\mu(S)
+
\operatorname{Var}_\mu(u)
}.
\]

The equality case is rigid:
\[
\operatorname{Var}_\mu(u)=0
\]
if and only if
\[
\mu=\delta_{p_*}.
\]
Therefore every other compact stationary state satisfies
\[
\boxed{
-1<
\operatorname{Corr}_\mu(u,v)
<
0
}
\]
with the exact formula
\[
\boxed{
\operatorname{Corr}_\mu(u,v)
=
-
\left(
1+
\frac{\operatorname{Var}_\mu(S)}
{\operatorname{Var}_\mu(u)}
\right)^{-1/2}
}.
\]

Finally, any nonconstant periodic orbit has time average
\[
\langle u\rangle=\beta.
\]
A continuous nonconstant periodic function with this average must take values on both sides of \(\beta\). Hence every nonconstant Schnakenberg cycle crosses
\[
\boxed{u=a+b}
\]
at least twice per least period.

## Assumptions and scope
The theorem concerns the classical nondimensional Schnakenberg kinetic equations
\[
\dot u=a-u+u^2v,
\qquad
\dot v=b-u^2v
\]
with positive feed parameters \(a,b\). These are the spatially homogeneous kinetics underlying the standard Schnakenberg reaction-diffusion model.

Compact support guarantees all generator tests and second moments used below. No ergodicity is assumed.

The foundational chemical-oscillator article was published on 7 December 1979. A same-object mathematical limit-cycle paper classifies its analysis primarily under MSC \(34C05\) together with \(34A36\). The present result is assigned primary MSC \(34C05\).

The theorem is measure-by-measure. It applies to the equilibrium atom, invariant measures on periodic orbits, and convex mixtures of compact invariant states.

## Proof
Let \(L\) be the generator.

For any continuous \(\phi\) on the compact \(u\)-projection of the support, choose an antiderivative \(H\) with
\[
H'(u)=\phi(u).
\]
Invariance gives
\[
0
=
\int LH\,d\mu
=
\mathbb E_\mu[
\phi(u)(a-u+u^2v)
].
\]
Therefore
\[
\mathbb E_\mu[u^2v\mid u]=u-a.
\]

Likewise, arbitrary antiderivative tests in \(v\) give
\[
0
=
\mathbb E_\mu[
\psi(v)(b-u^2v)
]
\]
for every continuous \(\psi\), hence
\[
\mathbb E_\mu[u^2v\mid v]=b.
\]

Now put
\[
S=u+v.
\]
The nonlinear reaction terms cancel:
\[
\dot S
=
a+b-u
=
\beta-u.
\]
Testing arbitrary antiderivatives of \(S\) gives
\[
\mathbb E_\mu[\beta-u\mid S]=0,
\]
so
\[
\mathbb E_\mu[u\mid S]=\beta.
\]

Taking expectations yields
\[
\mathbb E[u]=\beta.
\]

Since \(u\le S\),
\[
\mathbb E[u\mid S]\le S
\]
almost surely. Hence
\[
S\ge\beta
\]
almost surely. On the event \(S=\beta\), the equality
\[
\mathbb E[u\mid S]=S
\]
together with \(u\le S\) forces \(u=S=\beta\) almost surely on that event, so \(v=0\). But on \(v=0\),
\[
u^2v=0,
\]
whereas
\[
\mathbb E[u^2v\mid v]=b>0.
\]
Thus
\[
\mu(S=\beta)=0.
\]

The total-concentration identity gives
\[
u-\beta=-\dot S.
\]
Therefore
\[
\operatorname{Var}(u)
=
\mathbb E[(u-\beta)^2]
=
\mathbb E[\dot S^2].
\]

Also,
\[
\mathbb E[u-\beta\mid S]=0,
\]
so \(u-\beta\) is orthogonal to every square-integrable function of \(S\), in particular to \(S-\mathbb E[S]\). Thus
\[
\operatorname{Cov}(S,u)=0.
\]

Because
\[
v=S-u,
\]
we obtain
\[
\operatorname{Cov}(u,v)
=
\operatorname{Cov}(u,S)-\operatorname{Var}(u)
=
-\operatorname{Var}(u),
\]
and
\[
\operatorname{Var}(v)
=
\operatorname{Var}(S-u)
=
\operatorname{Var}(S)+\operatorname{Var}(u).
\]

If
\[
\operatorname{Var}(u)=0,
\]
then \(u=\beta\) on the support. The support of an invariant measure is invariant under the flow, so the vector field must be tangent to the line \(u=\beta\) there. Hence
\[
0=\dot u
=
a-\beta+\beta^2v
=
-b+\beta^2v,
\]
which forces
\[
v=\frac{b}{\beta^2}.
\]
Thus the support is the unique positive equilibrium \(p_*\). The converse is immediate.

If the measure is not the equilibrium atom, then
\[
\operatorname{Var}(u)>0.
\]
If
\[
\operatorname{Var}(S)=0,
\]
then \(S\) is constant on invariant support and
\[
\dot S=0,
\]
forcing \(u=\beta\) and again the equilibrium atom. Thus non-equilibrium stationary states also have
\[
\operatorname{Var}(S)>0.
\]
The covariance identities now give
\[
\operatorname{Corr}(u,v)
=
-\frac{\operatorname{Var}(u)}
{\sqrt{\operatorname{Var}(u)
[\operatorname{Var}(u)+\operatorname{Var}(S)]}},
\]
which is the displayed strict formula.

For a nonconstant periodic orbit, the invariant orbit measure has
\[
\langle u\rangle=\beta.
\]
If \(u(t)\ge\beta\) for all \(t\), or \(u(t)\le\beta\) for all \(t\), equality of the average would force \(u(t)\equiv\beta\), hence the equilibrium. Therefore the periodic function \(u(t)-\beta\) takes both signs and, by continuity and periodicity, has at least two zeros in each least period.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the algebraic cancellation
\[
\dot S=\dot u+\dot v=a+b-u,
\]
the residual relation
\[
u-(a+b)=-\dot S,
\]
and the covariance consequences
\[
\operatorname{Cov}(u,v)=-\operatorname{Var}(u),
\]
\[
\operatorname{Var}(v)=\operatorname{Var}(S)+\operatorname{Var}(u)
\]
under the exact orthogonality condition
\[
\operatorname{Cov}(S,u)=0.
\]

It also verifies the unique positive equilibrium
\[
\left(
a+b,\frac{b}{(a+b)^2}
\right)
\]
by exact substitution.

The stored checker output is `VERIFY_OK`.

The conditional-expectation statements and periodic crossing theorem are analytic consequences of invariance; they are not inferred from numerical trajectories.

## Relationship to prior work
Schnakenberg's foundational 1979 paper introduced very small autocatalytic chemical systems with limit-cycle behavior.

A complete 2013 mathematical article writes the standard nondimensional Schnakenberg kinetics
\[
\dot u=a-u+u^2v,
\qquad
\dot v=b-u^2v,
\]
identifies the unique positive equilibrium, analyzes the Hopf bifurcation of the kinetic system, and develops reaction-diffusion bifurcation theory. Full-document searches found no `moment`, `average`, `invariant measure`, or `covariance` formulation.

A complete open 2014 article studies transient growth in the Schnakenberg reaction-advection-diffusion system. It explicitly notes the importance of the sum of the two equations when discussing a modified model, but its analysis is linear transient amplification around homogeneous equilibrium. Full-page searches found no `moment`, `covariance`, or `average` theorem matching the accepted stationary statement.

A 2016 limit-cycle paper applies planar Liénard methods to a Schnakenberg model and classifies the work primarily under MSC \(34C05\) and \(34A36\). Its stated results concern existence, uniqueness, and stability of crossing limit cycles, not invariant-measure fiber calibrations.

The accepted statement is implication-wise different from local Hopf or uniqueness results. It applies to every compact invariant probability measure and gives exact conditional reaction-flux laws, a universal mean autocatalyst level, and the full second-order anticorrelation structure.

## Limitations
The theorem is conditional on compact invariant probability measures in the nonnegative quadrant. It does not prove that a nonconstant limit cycle exists for a chosen parameter pair.

It does not determine the full stationary distribution or the variance of \(S=u+v\).

The inequalities and covariance identities are necessary stationary constraints, not a classification of all periodic orbits.

The foundational 1979 article was used for historical provenance and date; the strongest complete searchable same-object comparison was the 2013 mathematical paper.

Because the fiberwise proof is short once invariant-measure testing is introduced, an equivalent identity could remain in unindexed chemical-oscillator literature.

## References
1. J. Schnakenberg, “Simple chemical reaction systems with limit cycle behaviour,” Journal of Theoretical Biology 81, 389–400 (1979), DOI 10.1016/0022-5193(79)90042-0.
2. P. Liu, J. Shi, Y. Wang, and X. Feng, “Bifurcation analysis of reaction–diffusion Schnakenberg model,” Journal of Mathematical Chemistry 51, 2001–2019 (2013), DOI 10.1007/s10910-013-0196-x.
3. A. Al-Zarka, A. Alagha, and S. Timoshin, “Transient behaviour in RDA systems of the Schnakenberg type,” Journal of Mathematical Chemistry 53, 111–127 (2015), DOI 10.1007/s10910-014-0413-2.
4. F. Jiang, J. Shi, Q.-G. Wang, and J. Sun, “On the existence and uniqueness of a limit cycle for a Liénard system with a discontinuity line,” Communications on Pure and Applied Analysis 15, 2509–2526 (2016), DOI 10.3934/cpaa.2016047.
