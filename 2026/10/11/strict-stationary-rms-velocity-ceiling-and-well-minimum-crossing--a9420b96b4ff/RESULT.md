# Strict stationary RMS velocity ceiling and well-minimum crossing in the forced Duffing oscillator
## Finding
Consider the periodically forced double-well Duffing oscillator written as the autonomous flow
\[
\dot x=y,
\qquad
\dot y=-\delta y+\beta x-\alpha x^3+f\cos\theta,
\qquad
\dot\theta=\omega
\]
on
\[
\mathbb R^2\times\mathbb S^1,
\]
with
\[
\alpha>0,\qquad
\beta>0,\qquad
\delta>0,\qquad
f>0,\qquad
\omega>0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Its phase marginal is the uniform measure on \(\mathbb S^1\). In particular,
\[
\mathbb E_\mu[\cos\theta]=0,
\qquad
\mathbb E_\mu[\sin\theta]=0,
\qquad
\mathbb E_\mu[\cos^2\theta]=\frac12.
\]

The state coordinates satisfy two exact conditional laws:
\[
\boxed{
\mathbb E_\mu[y\mid x]=0
}
\]
and, with
\[
L=\beta x-\alpha x^3+f\cos\theta,
\]
\[
\boxed{
\mathbb E_\mu[L\mid y]=\delta y
}.
\]

Thus
\[
\boxed{
\operatorname{Cov}_\mu(x,y)=0
}
\]
and the nonlinear load has the exact orthogonal decomposition
\[
\boxed{
\operatorname{Var}_\mu(L)
=
\delta^2\operatorname{Var}_\mu(y)
+
\mathbb E_\mu[\dot y^2]
}.
\]
Also,
\[
\boxed{
\operatorname{Cov}_\mu(y,L)
=
\delta\operatorname{Var}_\mu(y)
}.
\]

Averaging the second conditional law gives the cubic barycenter identity
\[
\boxed{
\alpha\mathbb E_\mu[x^3]
=
\beta\mathbb E_\mu[x]
}.
\]

The standard mechanical energy
\[
H(x,y)
=
\frac12y^2-\frac{\beta}{2}x^2+\frac{\alpha}{4}x^4
\]
obeys
\[
\dot H
=
-\delta y^2+fy\cos\theta.
\]
Stationarity therefore gives the exact input-dissipation balance
\[
\boxed{
\delta\mathbb E_\mu[y^2]
=
f\mathbb E_\mu[y\cos\theta]
}.
\]
A second phase test gives
\[
\boxed{
\mathbb E_\mu[y\cos\theta]
=
\omega\mathbb E_\mu[x\sin\theta]
},
\]
so
\[
\boxed{
\delta\mathbb E_\mu[y^2]
=
f\omega\mathbb E_\mu[x\sin\theta]
}.
\]

These identities yield a strict parameter-only ceiling for stationary velocity activity:
\[
\boxed{
0
<
\mathbb E_\mu[y^2]
<
\frac{f^2}{2\delta^2}
}.
\]
The upper bound depends only on forcing amplitude and damping; it is independent of the cubic stiffness, linear stiffness, and forcing frequency.

The load correlation is also rigidly nondegenerate:
\[
\boxed{
0
<
\operatorname{Corr}_\mu(y,L)
<
1
}
\]
with
\[
\boxed{
\operatorname{Corr}_\mu(y,L)
=
\left(
1+
\frac{\mathbb E_\mu[\dot y^2]}
{\delta^2\mathbb E_\mu[y^2]}
\right)^{-1/2}
}.
\]

Finally, define the two unforced potential-minimum levels
\[
r=\sqrt{\frac{\beta}{\alpha}}.
\]
If an invariant state is supported entirely in the positive well,
\[
x>0,
\]
then
\[
\boxed{
\mu\{0<x<r\}>0,
\qquad
\mu\{x>r\}>0
}.
\]
If it is supported entirely in the negative well,
\[
x<0,
\]
then
\[
\boxed{
\mu\{x<-r\}>0,
\qquad
\mu\{-r<x<0\}>0
}.
\]
Hence every nonconstant periodic orbit confined to one well crosses that well's unforced minimum level
\[
x=r
\quad\text{or}\quad
x=-r
\]
at least twice per least period.

## Assumptions and scope
The result concerns the classical harmonically forced double-well Duffing equation
\[
\ddot x+\delta\dot x-\beta x+\alpha x^3
=
f\cos(\omega t)
\]
with positive coefficients, represented autonomously by adjoining the forcing phase.

Compact support guarantees the moments and generator tests used below. No ergodicity, symmetry, or uniqueness assumption is imposed.

The strict velocity ceiling is not a claim that the bound is attained. In fact, the cubic restoring term makes equality impossible for every compact invariant probability measure under the stated positive-parameter assumptions.

The mechanical input-dissipation identity is elementary and is treated as prior structure, not as the new contribution. The finding is the combination of exact fiberwise regressions, the strict universal RMS ceiling with equality obstruction, the phase-quadrature identity, the nonlinear-load variance defect, and the one-well minimum-crossing theorem.

The Duffing equation itself is older than the day-resolved source used here. The structured date is 23 October 1979, the earliest checked day-resolved source that explicitly writes this forced double-well equation and studies its strange-attractor dynamics.

A mathematical treatment of forced oscillations using the Duffing equation lists \(37D45\) first in its Mathematics Subject Classification. That primary code is used here.

## Proof
Because
\[
\dot\theta=\omega
\]
with
\[
\omega\ne0,
\]
the phase marginal of any invariant probability measure is invariant under every circle rotation. The unique such probability measure is normalized Lebesgue measure. Hence
\[
\mathbb E[\cos\theta]
=
\mathbb E[\sin\theta]
=
0
\]
and
\[
\mathbb E[\cos^2\theta]
=
\frac12.
\]

Let \(L_{\mathrm{flow}}\) denote the flow generator.

For any continuous function \(\phi\) on the compact \(x\)-projection of the support, choose an antiderivative \(F\) with
\[
F'(x)=\phi(x).
\]
Then
\[
L_{\mathrm{flow}}F
=
\phi(x)y.
\]
Invariance gives
\[
\mathbb E[\phi(x)y]=0
\]
for every \(\phi\), hence
\[
\mathbb E[y\mid x]=0.
\]

Likewise, for any continuous function \(\psi\) on the compact \(y\)-projection, choose an antiderivative \(G\) with
\[
G'(y)=\psi(y).
\]
Then
\[
L_{\mathrm{flow}}G
=
\psi(y)
\left(
L-\delta y
\right).
\]
Stationarity for every \(\psi\) gives
\[
\mathbb E[L\mid y]=\delta y.
\]

The first conditional law gives
\[
\mathbb E[y]=0
\]
and
\[
\mathbb E[xy]=0,
\]
so
\[
\operatorname{Cov}(x,y)=0.
\]

The second law says
\[
L=\delta y+\dot y
\]
with
\[
\mathbb E[\dot y\mid y]=0.
\]
Therefore \(\dot y\) is orthogonal in \(L^2(\mu)\) to every square-integrable function of \(y\). Since
\[
\mathbb E[L]
=
\delta\mathbb E[y]
=
0,
\]
the law of total variance gives
\[
\operatorname{Var}(L)
=
\delta^2\operatorname{Var}(y)
+
\mathbb E[\dot y^2]
\]
and
\[
\operatorname{Cov}(y,L)
=
\delta\operatorname{Var}(y).
\]

Averaging
\[
L=\beta x-\alpha x^3+f\cos\theta
\]
and using
\[
\mathbb E[L]=0,
\qquad
\mathbb E[\cos\theta]=0
\]
gives
\[
\alpha\mathbb E[x^3]
=
\beta\mathbb E[x].
\]

Now differentiate the mechanical energy:
\[
\dot H
=
y\dot y-\beta xy+\alpha x^3y
=
-\delta y^2+fy\cos\theta.
\]
Invariance yields
\[
\delta\mathbb E[y^2]
=
f\mathbb E[y\cos\theta].
\]

For the quadrature relation, use the bounded smooth test
\[
x\cos\theta.
\]
Its derivative is
\[
\frac{d}{dt}(x\cos\theta)
=
y\cos\theta-\omega x\sin\theta.
\]
Stationarity gives
\[
\mathbb E[y\cos\theta]
=
\omega\mathbb E[x\sin\theta].
\]

Set
\[
q=\mathbb E[y^2].
\]
The power balance and Cauchy–Schwarz give
\[
\delta q
=
f\mathbb E[y\cos\theta]
\le
f
\sqrt{
q\mathbb E[\cos^2\theta]
}
=
f\sqrt{\frac q2}.
\]
If
\[
q>0,
\]
division and squaring yield
\[
q
\le
\frac{f^2}{2\delta^2}.
\]

The zero endpoint is impossible. If
\[
q=0,
\]
then
\[
y=0
\]
on invariant support. Thus
\[
x
\]
is constant along every support trajectory. But the support phase rotates through the entire circle, while invariance would require
\[
0
=
\dot y
=
\beta x-\alpha x^3+f\cos\theta
\]
for all phases on that trajectory, impossible because
\[
f>0.
\]
Hence
\[
q>0.
\]

Equality at the upper endpoint is also impossible. Equality in Cauchy–Schwarz together with the positive power balance forces
\[
y
=
\frac f\delta\cos\theta
\]
almost surely.

Set
\[
A
=
\frac{f}{\delta\omega}.
\]
Since
\[
\dot x=y,
\qquad
\dot\theta=\omega,
\]
the quantity
\[
C=x-A\sin\theta
\]
is constant along every support trajectory. Along such a trajectory,
\[
x=C+A\sin\theta.
\]
The equality form of \(y\) gives
\[
\dot y
=
-\frac{f\omega}{\delta}\sin\theta
=
-A\omega^2\sin\theta.
\]
Meanwhile the damping and forcing terms cancel:
\[
-\delta y+f\cos\theta=0,
\]
so the equation for \(\dot y\) becomes
\[
-A\omega^2\sin\theta
=
\beta(C+A\sin\theta)
-
\alpha(C+A\sin\theta)^3.
\]
Because the phase runs through all values, this is a polynomial identity in
\[
s=\sin\theta.
\]
Its cubic coefficient is
\[
-\alpha A^3,
\]
which is nonzero. Contradiction. Therefore
\[
q
<
\frac{f^2}{2\delta^2}.
\]

The same compactness argument shows
\[
\mathbb E[\dot y^2]>0.
\]
If \(\dot y=0\) on invariant support, then \(y\) is constant along every complete support trajectory. Compactness and
\[
\dot x=y
\]
force
\[
y=0,
\]
which has already been shown impossible under nonzero periodic forcing.

Since
\[
\operatorname{Var}(y)=q>0,
\]
the load covariance and variance formulas give the strict correlation formula.

Finally, let
\[
r^2=\frac{\beta}{\alpha}.
\]
The cubic barycenter identity is
\[
\mathbb E[
x(x^2-r^2)
]
=
0.
\]

Suppose the support lies in
\[
x>0.
\]
The integrand is negative on
\[
0<x<r
\]
and positive on
\[
x>r.
\]
If either region had zero mass, zero expectation would force
\[
x=r
\]
almost surely. But a constant \(x=r\) would force
\[
y=0
\]
and is incompatible with the rotating nonzero forcing. Hence both regions have positive mass.

The negative-well statement is identical after reversing signs.

For a periodic orbit confined to one well, its normalized time measure is invariant and therefore visits both sides of the corresponding minimum with positive time. By continuity and periodicity, it crosses the minimum level at least twice per least period.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the abstract orthogonal-regression identities generated by
\[
L=\delta y+\dot y,
\qquad
\mathbb E[\dot y\mid y]=0.
\]

It checks the power-balance conversion from
\[
\delta q=f\mathbb E[y\cos\theta]
\]
and
\[
\mathbb E[\cos^2\theta]=\frac12
\]
to
\[
q\le\frac{f^2}{2\delta^2}.
\]

It verifies the exact phase-quadrature identity and confirms that the equality ansatz produces the nonzero cubic coefficient
\[
-\alpha
\left(
\frac{f}{\delta\omega}
\right)^3,
\]
so the Cauchy equality case cannot solve the Duffing equation when
\[
\alpha f\ne0.
\]

It also checks the sign structure of
\[
x
\left(
x^2-\frac{\beta}{\alpha}
\right)
\]
around the two potential minima.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation quantifiers, invariant-support endpoint exclusions, and periodic crossing count are analytic arguments; no finite orbit simulation is used.

## Relationship to prior work
Holmes's 1979 paper writes
\[
\ddot x+\delta\dot x-\beta x+\alpha x^3
=
f\cos(\omega t)
\]
with positive coefficients and analyzes strange-attractor dynamics in this forced nonlinear oscillator.

Holmes's 1980 averaging paper develops chaotic motions in forced oscillations and uses Duffing-type examples. Its mathematical classification places \(37D45\) first.

Early 1980s Duffing studies analyze transitions to chaos and statistical properties of chaotic states. One such study explicitly discusses the relation between time averages and ensemble averages. That makes stationary statistical questions natural prior territory, but the checked abstract does not state the conditional regression or the strict RMS theorem proved here.

A complete open 2017 forced-Duffing study analyzes the same oscillator family through Melnikov thresholds, Lyapunov exponents, and bifurcation diagrams. Full-document searches found no occurrence of `mean square`, `average`, `variance`, or `conditional`.

The mechanical identity
\[
\dot H=-\delta y^2+fy\cos\theta
\]
is elementary and is not claimed as new. The accepted result uses it together with invariant phase uniformity and an equality-rigidity argument to obtain a strict all-invariant-measures RMS ceiling. The two conditional laws and the one-well minimum-crossing theorem are separate stationary consequences not supplied by the standard power balance.

## Limitations
The theorem concerns harmonic forcing with a constant nonzero frequency and the double-well sign convention
\[
\alpha>0,
\qquad
\beta>0.
\]

It assumes compactly supported invariant probability measures.

The upper RMS velocity bound is strict but is not asserted to be the best unattained supremum over all parameters or invariant measures.

The theorem constrains selected conditional means, moments, and one-well crossings; it does not determine the full invariant distribution, Lyapunov spectrum, or chaotic parameter thresholds.

The 1982 statistical Duffing source was compared from its published abstract rather than a complete local full-text copy.

Because the core generator identities are short, equivalent weighted formulations may remain in older unindexed literature.

## References
1. P. Holmes, “A nonlinear oscillator with a strange attractor,” Philosophical Transactions of the Royal Society of London. Series A 292, 419–448 (1979), DOI 10.1098/rsta.1979.0068.
2. P. Holmes, “Averaging and Chaotic Motions in Forced Oscillations,” SIAM Journal on Applied Mathematics 38, 65–80 (1980), DOI 10.1137/0138005.
3. S. T. Chui and K. W. Ma, “Nature of some chaotic states for Duffing's equation,” Physical Review A 26, 2262–2268 (1982), DOI 10.1103/PhysRevA.26.2262.
4. M. S. Siewe and H. Cao, “Chaotic Motion in Forced Duffing System Subject to Linear and Nonlinear Damping,” International Journal of Bifurcation and Chaos 27 (2017), DOI 10.1155/2017/3769870.
