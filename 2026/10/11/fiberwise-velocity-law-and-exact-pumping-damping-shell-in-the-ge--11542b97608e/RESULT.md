# Fiberwise velocity law and exact pumping–damping shell in the generalized Rayleigh oscillator
## Finding
Consider the generalized Rayleigh system
\[
\dot x=y,
\qquad
\dot y=-x+a(1-y^{2n})y,
\]
where
\[
n\ge1
\]
is an integer and
\[
a\ne0.
\]

Let \(\mu\) be any compactly supported invariant Borel probability measure. Then the two coordinate fibers satisfy
\[
\boxed{
\mathbb E_\mu[y\mid x]=0
}
\]
and
\[
\boxed{
\mathbb E_\mu[x\mid y]
=
a(1-y^{2n})y
}.
\]

Thus the position–velocity covariance vanishes exactly:
\[
\boxed{
\operatorname{Cov}_\mu(x,y)=0
}.
\]

The quadratic energy
\[
H(x,y)=\frac12(x^2+y^2)
\]
has derivative
\[
\dot H
=
a y^2(1-y^{2n}).
\]
Stationarity therefore gives the exact moment shell
\[
\boxed{
\mathbb E_\mu[y^{2n+2}]
=
\mathbb E_\mu[y^2]
}.
\]

Writing
\[
G(y)=a(1-y^{2n})y,
\]
the second fiber law says that \(G(y)\) is the exact regression of \(x\) on \(y\). Since
\[
x=G(y)-\dot y
\]
and
\[
\mathbb E_\mu[\dot y\mid y]=0,
\]
the orthogonal residual decomposition is
\[
\boxed{
\operatorname{Var}_\mu(x)
=
\operatorname{Var}_\mu(G(y))
+
\mathbb E_\mu[\dot y^2]
}.
\]
Equivalently,
\[
\boxed{
\operatorname{Var}_\mu(x)
=
a^2\operatorname{Var}_\mu((1-y^{2n})y)
+
\mathbb E_\mu[\dot y^2]
}.
\]

The origin atom is the unique compact stationary state with
\[
\mathbb E_\mu[y^2]=0,
\]
and it is also the unique compact stationary state with
\[
\mathbb E_\mu[\dot y^2]=0.
\]

Every other compact stationary state obeys the strict universal root-mean-square velocity bound
\[
\boxed{
0<
\mathbb E_\mu[y^2]
<
1
}.
\]
Indeed, if
\[
m=\mathbb E_\mu[y^2],
\]
then Jensen's inequality and the moment shell give
\[
m^{n+1}
\le
\mathbb E_\mu[(y^2)^{n+1}]
=
m.
\]
Thus
\[
0\le m\le1.
\]
The endpoint \(m=0\) is the origin. The endpoint \(m=1\) would force \(y^2=1\) almost surely, which is incompatible with an invariant complete trajectory because \(y\) would have to remain constant while
\[
\dot x=y\ne0.
\]

The energy balance also resolves the nonlinear damping threshold. The quantity
\[
y^2(1-y^{2n})
\]
is positive on
\[
0<|y|<1
\]
and negative on
\[
|y|>1.
\]
For every non-origin stationary state, its mean is zero but it is not almost surely zero. Therefore
\[
\boxed{
\mu\{0<|y|<1\}>0
}
\]
and
\[
\boxed{
\mu\{|y|>1\}>0
}.
\]
Every genuinely recurrent state must therefore sample both the energy-pumping and energy-dissipating velocity regimes.

Finally, every non-origin compact stationary state has
\[
\operatorname{Var}_\mu(x)>0,
\qquad
\operatorname{Var}_\mu(y)>0,
\]
while
\[
\operatorname{Cov}_\mu(x,y)=0.
\]
Hence
\[
\boxed{
\operatorname{Corr}_\mu(x,y)=0
}.
\]

For a nonconstant periodic orbit, the normalized time measure is a non-origin invariant measure. Since the periodic velocity \(y(t)\) spends positive time both below and above the threshold in absolute value, continuity forces at least two crossings of
\[
\boxed{|y|=1}
\]
during every least period.

## Assumptions and scope
The theorem concerns the generalized Rayleigh family
\[
\ddot x+x=a(1-\dot x^{2n})\dot x,
\qquad
n\in\mathbb N,
\qquad
a\ne0.
\]
Compact support is used to justify the invariant-generator tests and the second moments.

No ergodicity assumption is made. The statement applies to the equilibrium atom, the invariant probability on the unique limit cycle, and any compact invariant mixture.

The primary generalized-Rayleigh source gives the same family with a positive integer exponent and studies existence and stability of its limit cycles by averaging. Its mathematical classification lists \(34C05\) first, so that code is used here.

A later complete global-dynamics study proves that the same generalized Rayleigh system has a unique limit cycle for every nonzero parameter \(a\), with stability determined by the sign of \(a\). The present result does not depend on that global classification.

## Proof
Let \(L\) be the flow generator.

For any continuous function \(\phi\) on the compact \(x\)-projection of the support, choose an antiderivative \(F\) with
\[
F'(x)=\phi(x).
\]
Then
\[
LF
=
\phi(x)y.
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)y]=0
\]
for every \(\phi\). Hence
\[
\mathbb E_\mu[y\mid x]=0.
\]

Similarly, for any continuous \(\psi\) on the compact \(y\)-projection, choose \(K\) with
\[
K'(y)=\psi(y).
\]
Then
\[
LK
=
\psi(y)
\left(
-x+a(1-y^{2n})y
\right).
\]
Stationarity for every \(\psi\) gives
\[
\mathbb E_\mu[x\mid y]
=
a(1-y^{2n})y.
\]

The first fiber law implies
\[
\mathbb E[y]=0
\]
and, taking the test function \(x\),
\[
\mathbb E[xy]=0.
\]
Therefore
\[
\operatorname{Cov}(x,y)=0.
\]

Now differentiate
\[
H=\frac12(x^2+y^2).
\]
Using the equations,
\[
\dot H
=
xy+y[-x+a(1-y^{2n})y]
=
a y^2(1-y^{2n}).
\]
Since \(a\ne0\),
\[
0
=
\mathbb E[\dot H]
=
a\left(
\mathbb E[y^2]
-
\mathbb E[y^{2n+2}]
\right),
\]
which proves the moment shell.

For the variance decomposition, set
\[
G(y)=a(1-y^{2n})y.
\]
The second conditional law is
\[
\mathbb E[x\mid y]=G(y).
\]
Thus
\[
x-G(y)=-\dot y
\]
has conditional mean zero given \(y\). It is therefore orthogonal in \(L^2(\mu)\) to every square-integrable function of \(y\), including \(G(y)-\mathbb E[G(y)]\). The law of total variance gives
\[
\operatorname{Var}(x)
=
\operatorname{Var}(G(y))
+
\mathbb E[\dot y^2].
\]

Suppose
\[
\mathbb E[y^2]=0.
\]
Then
\[
y=0
\]
on the support. Invariance requires support trajectories to remain on that line, but there
\[
\dot y=-x.
\]
Hence
\[
x=0,
\]
so the measure is the origin atom.

Conversely, the origin atom clearly has zero \(y\)-variance.

Suppose
\[
\mathbb E[\dot y^2]=0.
\]
Then
\[
\dot y=0
\]
on the invariant support. Along each complete support trajectory, \(y\) is constant and
\[
\dot x=y.
\]
Compactness of the complete trajectory forces
\[
y=0,
\]
and then
\[
\dot y=-x=0.
\]
Again the measure is the origin atom.

For the root-mean-square bound, let
\[
Z=y^2
\]
and
\[
m=\mathbb E[Z].
\]
The moment shell is
\[
\mathbb E[Z^{n+1}]=m.
\]
Since \(s\mapsto s^{n+1}\) is strictly convex on the nonnegative axis,
\[
m^{n+1}
\le
\mathbb E[Z^{n+1}]
=
m.
\]
Thus
\[
0\le m\le1.
\]
If
\[
m=1,
\]
equality in Jensen forces
\[
Z=1
\]
almost surely. Along every support trajectory this would give
\[
y^2\equiv1.
\]
Differentiating forces
\[
\dot y\equiv0,
\]
so the second equation gives
\[
x\equiv0.
\]
But then
\[
\dot x=y
\]
is equal to \(1\) or \(-1\), a contradiction. Hence \(m<1\). For a non-origin measure, the zero case was already excluded.

The threshold-excursion result follows from
\[
0
=
\mathbb E[y^2(1-y^{2n})].
\]
If the measure assigned no positive mass to
\[
0<|y|<1,
\]
the integrand would be nonpositive almost surely, so zero expectation would force it to vanish almost surely. The support would then lie in
\[
y\in\{0,\pm1\},
\]
which cannot carry a non-origin invariant measure by the preceding rigidity arguments. Thus the pumping region has positive mass. The same argument with signs reversed proves positive mass in
\[
|y|>1.
\]

Finally, if
\[
\operatorname{Var}(x)=0,
\]
then \(x\) is constant on invariant support. Since
\[
\dot x=y,
\]
one has \(y=0\), and the second equation forces \(x=0\). Thus every non-origin invariant state has positive variance in both coordinates. Together with exact zero covariance, this proves zero Pearson correlation.

The periodic crossing assertion follows because a continuous periodic function that spends positive time in both open sets
\[
|y|<1
\quad\text{and}\quad
|y|>1
\]
must cross the boundary
\[
|y|=1
\]
at least twice per least period.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the vector-field identities
\[
\dot x=y,
\qquad
\dot y=-x+a(1-y^{2n})y,
\]
the energy derivative
\[
\frac{d}{dt}\frac{x^2+y^2}{2}
=
a y^2(1-y^{2n}),
\]
and the exact regression residual
\[
x-a(1-y^{2n})y=-\dot y.
\]

It checks the covariance consequence of
\[
\mathbb E[y\mid x]=0,
\]
the moment-shell algebra
\[
\mathbb E[y^{2n+2}]
=
\mathbb E[y^2],
\]
and the orthogonal variance decomposition.

The stored checker output is `VERIFY_OK`.

The conditional-expectation theorem, endpoint rigidity, and threshold-excursion statement are analytic proofs and are not inferred from finite trajectory sampling.

## Relationship to prior work
The 2013 generalized-Rayleigh paper studies
\[
\ddot x+x
=
a(1-\dot x^{2n})\dot x
\]
with positive integer \(n\), proving limit-cycle existence and stability by averaging. Its stated focus is the orbit itself rather than invariant-measure statistics.

A complete later global-dynamics paper studies exactly
\[
\dot x=y,
\qquad
\dot y=-x+a(1-y^{2n})y
\]
and proves uniqueness of the limit cycle for every
\[
a\ne0.
\]
Full-document searches found no `moment`, `average`, `invariant`, or `covariance` formulation.

A complete public study of the classical case
\[
n=1
\]
derives the fixed point, applies a Poincaré–Bendixson/Melnikov argument, and studies limit-cycle stability. Its full searchable text contains no `moment`, `average`, `invariant measure`, or `covariance` statement.

A separate Rayleigh/van der Pol approximation paper derives amplitude and phase approximations for the classical oscillator. Its principal results concern perturbative and homotopy approximations to the limit cycle, not exact stationary conditional laws.

The accepted theorem therefore concerns a different layer of structure. It holds for every compact invariant probability measure, gives the exact nonlinear regression
\[
\mathbb E[x\mid y]=a(1-y^{2n})y,
\]
and converts the sign-changing damping law into a universal power-moment shell and a strict recurrent excursion across the physical threshold
\[
|y|=1.
\]

## Limitations
The theorem assumes
\[
a\ne0.
\]
At
\[
a=0,
\]
the system is the linear harmonic center and the power-moment shell no longer follows.

The result constrains conditional means, second moments, and one higher even moment; it does not determine the full invariant distribution or the period of the limit cycle.

The root-mean-square ceiling
\[
\sqrt{\mathbb E[y^2]}<1
\]
is dimensionless in the normalization used by the generalized Rayleigh equation.

The 2013 primary generalized-family article was available through its bibliographic record and abstract rather than a complete local full-text copy. The strongest complete same-family comparison was the later global-dynamics preprint.

Because the energy-balance calculation is short, the scalar moment identity alone may have been observed implicitly in oscillator literature. The originality assessment concerns the combined fiberwise regression, orthogonal variance defect, strict root-mean-square ceiling, and pumping–damping excursion theorem.

## References
1. M. A. López and R. Martínez, “A note on the generalized Rayleigh equation: limit cycles and stability,” *Journal of Mathematical Chemistry* 51, 1164–1169 (2013), DOI 10.1007/s10910-012-0096-5.
2. M. D. Baldissera, J. Llibre, and R. Oliveira, “Dynamics of a generalized Rayleigh system,” arXiv:2106.06100 (2021).
3. C. H. Miwadinou, A. V. Monwanou, and J. B. Chabi Orou, “Recherche et étude de la stabilité du cycle limite pour l'oscillateur de Rayleigh,” arXiv:1303.0537 (2013).
4. A. Palit and D. P. Datta, “Comparative Study of Homotopy Analysis and Renormalization Group Methods on Rayleigh and Van der Pol Equations,” arXiv:1405.6615 (2014).
