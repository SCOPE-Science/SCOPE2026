# Exact stationary slice calibrations and variance-speed rigidity in the Brusselator
## Finding
Consider the positive Brusselator
\[
\dot x=A-(B+1)x+x^2y,\qquad
\dot y=Bx-x^2y,
\]
with
\[
A>0,\qquad B>0.
\]

For every compactly supported invariant Borel probability measure \(\mu\) whose support is contained in
\[
(0,\infty)^2,
\]
the activator obeys the exact total-concentration slice law
\[
\boxed{\mathbb E_\mu[x\mid x+y]=A}.
\]

There is also an exact inhibitor-fiber law
\[
\boxed{
B\,\mathbb E_\mu[x\mid y]
=
y\,\mathbb E_\mu[x^2\mid y]
}.
\]
If
\[
m(y)=\mathbb E_\mu[x\mid y],
\]
then
\[
\operatorname{Var}_\mu(x\mid y)
=
m(y)\left(\frac{B}{y}-m(y)\right),
\]
so
\[
0<m(y)\le\frac{B}{y}
\]
for \(\mu\)-almost every inhibitor level.

Because the first slice law gives
\[
\mathbb E_\mu[x]=A,
\]
the activator-size-biased measure
\[
d\nu=\frac{x}{A}\,d\mu
\]
is a probability measure. Its inhibitor fibers are calibrated exactly to the nontrivial \(y\)-nullcline:
\[
\boxed{
\mathbb E_\nu[x\mid y]=\frac{B}{y}
}.
\]

Every bounded complete positive orbit also satisfies the strict recurrent barrier
\[
x+y>A.
\]
Thus the support of every such invariant measure lies entirely above the line
\[
x+y=A.
\]

The total-concentration slice law further yields
\[
\operatorname{Cov}_\mu(x,x+y)=0,
\]
and hence
\[
\boxed{
\operatorname{Cov}_\mu(x,y)
=
-\operatorname{Var}_\mu(x)
}.
\]
Equivalently,
\[
\boxed{
\operatorname{Var}_\mu(y)
-
\operatorname{Var}_\mu(x+y)
=
\operatorname{Var}_\mu(x)
=
\mathbb E_\mu[(\dot x+\dot y)^2]
}.
\]

The common defect vanishes exactly for the equilibrium atom
\[
\delta_{(A,B/A)}.
\]
Therefore every other compact stationary state has positive mass in both half-planes
\[
x<A
\quad\text{and}\quad
x>A.
\]
In particular every nonconstant periodic orbit crosses
\[
x=A
\]
while remaining strictly in
\[
x+y>A.
\]

The global period-average relation
\[
\langle x\rangle=A
\]
was already derived in the classical Brusselator literature and is not claimed as new. The new statement assessed here is the conditional refinement, the inhibitor-fiber size-bias law, the recurrent barrier, and the exact covariance-speed defect with its equality classification.

## Assumptions and scope
The measure \(\mu\) is invariant under the autonomous Brusselator flow and supported on a compact subset of the positive quadrant. Compactness and strict positivity guarantee integrability of all polynomial and antiderivative test functions and keep \(y\) bounded away from zero on the support.

The equations are the standard unit-rate Brusselator normalization. The unique positive equilibrium is
\[
\left(A,\frac BA\right).
\]

The earliest verified public source date for this reaction mechanism is 15 February 1968. A 1971 article then gave the normalized two-dimensional equations, proved existence of sustained oscillations beyond the instability threshold, and explicitly derived the period-average identity
\[
\langle x\rangle=A.
\]

Modern work on the same planar system classifies it primarily under MSC \(34C05\), with additional classifications \(34C23\) and \(34C07\).

## Proof
Set
\[
s=x+y.
\]
Adding the equations gives the exact scalar relation
\[
\dot s=A-x.
\]

Let \(\phi\) be any continuous function on the compact \(s\)-range of the support, and choose a continuously differentiable antiderivative \(H\) satisfying
\[
H'(s)=\phi(s).
\]
For the generator \(L\),
\[
LH
=
\phi(s)(A-x).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(s)(A-x)]=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[x\mid s]=A.
\]

Now let \(\psi\) be continuous on the compact \(y\)-range and choose an antiderivative \(K\). Since
\[
\dot y=x(B-xy),
\]
we have
\[
LK
=
\psi(y)x(B-xy).
\]
Stationarity gives
\[
B\,\mathbb E_\mu[x\mid y]
=
y\,\mathbb E_\mu[x^2\mid y].
\]

Writing
\[
m(y)=\mathbb E_\mu[x\mid y],
\]
we obtain
\[
\mathbb E_\mu[x^2\mid y]
=
\frac{B}{y}m(y),
\]
and therefore
\[
\operatorname{Var}_\mu(x\mid y)
=
m(y)\left(\frac{B}{y}-m(y)\right).
\]
Strict positivity of \(x\) on the support gives
\[
m(y)>0.
\]

Taking expectations in the first slice law yields
\[
\mathbb E_\mu[x]=A.
\]
Thus
\[
d\nu=\frac{x}{A}\,d\mu
\]
is a probability measure. Conditional size-biasing gives
\[
\mathbb E_\nu[x\mid y]
=
\frac{\mathbb E_\mu[x^2\mid y]}
{\mathbb E_\mu[x\mid y]}
=
\frac{B}{y}.
\]

We next prove the strict barrier. Suppose a bounded complete positive orbit had
\[
s(t_0)<A.
\]
Set
\[
r=A-s>0
\]
and reverse time by writing
\[
\tau=t_0-t.
\]
While \(s<A\),
\[
\frac{dr}{d\tau}
=
A-x.
\]
Because
\[
x<s=A-r,
\]
we have
\[
\frac{dr}{d\tau}>r.
\]
Thus \(r\) grows at least exponentially backward in time, forcing
\[
s=A-r
\]
to become nonpositive in finite backward time, contradicting positivity of a complete orbit. If instead
\[
s(t_0)=A,
\]
then
\[
\dot s(t_0)=A-x(t_0)=y(t_0)>0,
\]
so the backward orbit immediately enters \(s<A\), giving the same contradiction. Hence every bounded complete positive orbit satisfies
\[
s>A.
\]

For the variance identities, the slice law gives
\[
\mathbb E_\mu[xs]
=
A\,\mathbb E_\mu[s].
\]
Since
\[
\mathbb E_\mu[x]=A,
\]
this is
\[
\operatorname{Cov}_\mu(x,s)=0.
\]
Using
\[
y=s-x,
\]
we obtain
\[
\operatorname{Cov}_\mu(x,y)
=
-\operatorname{Var}_\mu(x)
\]
and
\[
\operatorname{Var}_\mu(y)
=
\operatorname{Var}_\mu(s)+\operatorname{Var}_\mu(x).
\]

Finally,
\[
\dot s=A-x
\]
gives
\[
\mathbb E_\mu[\dot s^2]
=
\mathbb E_\mu[(x-A)^2]
=
\operatorname{Var}_\mu(x).
\]
Since
\[
\dot s=\dot x+\dot y,
\]
the displayed speed defect follows.

If the defect is zero, then
\[
\operatorname{Var}_\mu(x)=0,
\]
so
\[
x=A
\]
on the invariant support. Along every support trajectory \(x\) is constant, hence
\[
0=\dot x=A-(B+1)A+A^2y
=
A(Ay-B).
\]
Therefore
\[
y=\frac BA,
\]
so the support is the unique equilibrium. The converse is immediate.

For every non-equilibrium-supported invariant measure,
\[
\operatorname{Var}_\mu(x)>0
\]
while
\[
\mathbb E_\mu[x]=A.
\]
Therefore both sets
\[
\{x<A\}
\quad\text{and}\quad
\{x>A\}
\]
have positive measure. The periodic-orbit crossing statement follows by continuity.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic.

It verifies the pointwise cancellation
\[
\dot x+\dot y=A-x,
\]
the inhibitor flux identity
\[
\dot y=x(B-xy),
\]
and the equilibrium cancellation at
\[
\left(A,\frac BA\right)
\]
after clearing the denominator \(A\).

It also verifies the algebraic variance decomposition
\[
\operatorname{Var}(s-x)
=
\operatorname{Var}(s)+\operatorname{Var}(x)
\]
under the proved orthogonality condition
\[
\operatorname{Cov}(x,s)=0.
\]

The stored checker output is `VERIFY_OK`.

The checker validates the polynomial certificates. The conditional expectations, support barrier, and equality classification are analytic consequences of stationarity and bounded complete positive dynamics; they are not inferred from finite simulation.

## Relationship to prior work
Prigogine and Lefever introduced the reaction scheme in 1968 while studying dissipative instabilities. Their article gives the autocatalytic two-intermediate mechanism and the associated kinetic equations.

Lefever and Nicolis studied the spatially homogeneous model in detail in 1971. They wrote
\[
\dot X=A+X^2Y-BX-X,\qquad
\dot Y=BX-X^2Y,
\]
proved sustained oscillation beyond the instability threshold, and observed that
\[
\frac{d}{dt}(X+Y)=A-X.
\]
Averaging this identity over the limit cycle, they explicitly obtained
\[
\langle X\rangle=A.
\]
That global periodic-orbit average is prior coverage and is excluded from the originality claim. Their thermodynamic section then used it to compare average entropy production and tabulated average \(Y\)-values; it did not state a conditional law on total-concentration slices or inhibitor fibers.

Tyson's 1973 complete treatment develops the Brusselator through isoclines, Poincaré–Bendixson domains, relaxation oscillations, coupled oscillators, synchronization, and biochemical modifications. It does not state the slice calibrations or covariance-speed law above.

Llibre and Valls later studied Liouvillian and analytic first integrals for the same planar polynomial system, focusing on Darboux polynomials and integrability rather than invariant-measure moment disintegrations.

A modern global phase-portrait classification gives the same equations, the equilibrium and Hopf threshold, and the stable-limit-cycle regime. Document-wide searches of the inspected article did not locate invariant-measure, average, or moment statements.

The accepted result strictly refines the known global relation
\[
\langle x\rangle=A
\]
to
\[
\mathbb E[x\mid x+y]=A
\]
on every compact stationary component. The inhibitor-fiber identity and size-biased nullcline calibration are independent additional constraints, while the barrier and covariance-speed law turn those disintegrations into recurrent geometry and an equality-rigid fluctuation identity.

## Limitations
The theorem concerns compactly supported invariant probability measures whose support lies in the positive quadrant. It does not classify invariant measures on nonphysical extensions of the polynomial vector field outside that quadrant.

The identities constrain conditional first and second moments but do not determine the full invariant density or the period of the stable cycle.

The support barrier
\[
x+y>A
\]
is a statement about bounded complete positive trajectories and invariant supports, not about arbitrary transient initial states.

The global average
\[
\langle x\rangle=A
\]
is prior literature and is not part of the originality claim.

Because the conditional identities follow from short generator calculations, an equivalent formulation could remain in unindexed chemical-oscillation literature.

## References
1. I. Prigogine and R. Lefever, “Symmetry Breaking Instabilities in Dissipative Systems. II,” Journal of Chemical Physics 48, 1695–1700 (1968), DOI 10.1063/1.1668896.
2. R. Lefever and G. Nicolis, “Chemical Instabilities and Sustained Oscillations,” Journal of Theoretical Biology 30, 267–284 (1971), DOI 10.1016/0022-5193(71)90054-3.
3. J. J. Tyson, “Some further studies of nonlinear oscillations in chemical systems,” Journal of Chemical Physics 58, 3919–3930 (1973), DOI 10.1063/1.1679748.
4. J. Llibre and C. Valls, “Liouvillian and Analytic First Integrals for the Brusselator System,” Journal of Nonlinear Mathematical Physics 19, 1250016 (2012), DOI 10.1142/S1402925112500167.
5. F. M. de Abreu and J. Llibre, “Classification of Global Phase Portraits for the Brusselator System,” Journal of Dynamics and Differential Equations (2026), DOI 10.1007/s10883-026-09780-5.
