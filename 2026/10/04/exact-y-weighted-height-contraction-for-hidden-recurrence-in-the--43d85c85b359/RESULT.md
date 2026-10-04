# Exact y-weighted height contraction for hidden recurrence in the Wang–Chen flow
## Finding
Consider the Wang–Chen system
\[
\dot x=yz+a,\qquad
\dot y=x^2-y,\qquad
\dot z=1-4x,
\]
in the stable-equilibrium regime
\[
a>0.
\]
Its unique equilibrium is
\[
p_a=\left(\frac14,\frac1{16},-16a\right).
\]

Let \(\mu\) be any compactly supported invariant probability measure. Its support is contained in
\[
y>0.
\]
The forcing term produces the exact coordinatewise stationary law
\[
\mathbb E_\mu[yz\mid x]=-a.
\]

Define the nonnegative stationary defect
\[
D=\mathbb E_\mu[(1-4x)^2]
  =\mathbb E_\mu[\dot z^2],
\]
and define the \(y\)-weighted probability measure
\[
d\nu=\frac{y\,d\mu}{\mathbb E_\mu[y]}.
\]
Then
\[
\boxed{
\mathbb E_\nu[z]
=
-\frac{16a}{1+D}
}.
\]

The defect is rigid:
\[
D=0
\quad\Longleftrightarrow\quad
\mu=\delta_{p_a}.
\]
Therefore every non-equilibrium compact invariant probability measure satisfies
\[
-16a<\mathbb E_\nu[z]<0.
\]
Consequently,
\[
\mu\{z>-16a\}>0
\qquad\text{and}\qquad
\mu\{z<0\}>0.
\]

There is also a fiberwise form of the sign obstruction. For a regular conditional distribution \(\mu_x\) given the \(x\)-coordinate,
\[
\int yz\,d\mu_x(y,z)=-a<0
\]
for almost every \(x\) with respect to the \(x\)-marginal. Since \(y>0\) on the compact invariant support,
\[
\mu_x\{z<0\}>0
\]
for almost every represented \(x\).

At the coexistence value
\[
a=0.01
\]
reported for simultaneous point, periodic, and strange attractors, every compact invariant measure supported on either non-point attractor therefore satisfies
\[
-0.16<\mathbb E_\nu[z]<0
\]
and has positive mass both above the equilibrium height
\[
z=-0.16
\]
and below
\[
z=0.
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the polynomial flow and supported on a compact subset of \(\mathbb R^3\). Compact support makes every support trajectory bounded and complete and guarantees integrability of all test functions below.

The restriction
\[
a>0
\]
is the regime in which the unique equilibrium is asymptotically stable. The characteristic polynomial at \(p_a\) is
\[
\lambda^3+\lambda^2+\left(8a+\frac14\right)\lambda+\frac14,
\]
and the cubic Routh–Hurwitz criterion gives asymptotic stability exactly when
\[
a>0.
\]

The earliest verified public source is the preprint posted on 21 January 2011. The source explicitly identifies the degenerate case
\[
a=0
\]
with Sprott E. Results that depend only on the two unchanged equations
\[
\dot y=x^2-y,\qquad
\dot z=1-4x
\]
are therefore treated here as proof ingredients rather than as the originality-bearing part of the finding.

## Proof
First, let
\[
(x(t),y(t),z(t))
\]
be any bounded complete trajectory in the invariant support. Variation of constants for the \(y\)-equation gives
\[
y(t)
=
e^{-(t-s)}y(s)
+
\int_s^t e^{-(t-u)}x(u)^2\,du.
\]
Letting
\[
s\to-\infty
\]
and using boundedness yields
\[
y(t)
=
\int_{-\infty}^{t} e^{-(t-u)}x(u)^2\,du
\ge0.
\]
If equality held at some time, then
\[
x(u)=0
\]
for every earlier time \(u\). The equation
\[
\dot z=1-4x
\]
would then give
\[
\dot z=1
\]
on an entire backward half-orbit, contradicting bounded completeness. Thus
\[
y(t)>0
\]
on every compact invariant support. Compactness then supplies a positive lower bound for \(y\) on that support.

Let \(L\) be the generator. For an arbitrary continuous function \(\phi\) on the compact \(x\)-range, choose an antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH=\phi(x)(yz+a).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)(yz+a)]=0
\]
for every such \(\phi\). Hence
\[
\mathbb E_\mu[yz\mid x]=-a.
\]
In particular,
\[
\mathbb E_\mu[yz]=-a.
\]

Two stationary identities from the unchanged \(y\)- and \(z\)-equations will now be used. Applying the same antiderivative argument in \(z\) gives
\[
\mathbb E_\mu[x\mid z]=\frac14,
\]
hence
\[
\mathbb E_\mu[x]=\frac14.
\]
Applying it in \(y\) gives
\[
\mathbb E_\mu[x^2\mid y]=y,
\]
hence
\[
\mathbb E_\mu[y]=\mathbb E_\mu[x^2].
\]

Therefore
\[
\mathbb E_\mu[y]
=
\frac1{16}
+
\operatorname{Var}_\mu(x).
\]
Because
\[
\dot z=1-4x=-4\left(x-\frac14\right),
\]
we have
\[
D
=
\mathbb E_\mu[\dot z^2]
=
16\,\operatorname{Var}_\mu(x),
\]
and consequently
\[
\mathbb E_\mu[y]
=
\frac{1+D}{16}.
\]

Since \(y>0\), the measure
\[
d\nu=\frac{y\,d\mu}{\mathbb E_\mu[y]}
\]
is a probability measure equivalent to \(\mu\). Using
\[
\mathbb E_\mu[yz]=-a
\]
gives
\[
\mathbb E_\nu[z]
=
\frac{\mathbb E_\mu[yz]}{\mathbb E_\mu[y]}
=
-\frac{16a}{1+D}.
\]

If
\[
D=0,
\]
then
\[
x=\frac14
\]
on the invariant support. A bounded complete support trajectory in this plane must satisfy
\[
\dot y=\frac1{16}-y.
\]
The only solution of this scalar equation bounded for all positive and negative time is
\[
y=\frac1{16}.
\]
Tangency to the plane \(x=1/4\) then gives
\[
0=\dot x=yz+a,
\]
hence
\[
z=-16a.
\]
Thus the support is the single equilibrium \(p_a\). The converse is immediate.

For a non-equilibrium invariant measure,
\[
D>0.
\]
Since \(a>0\),
\[
-16a
<
-\frac{16a}{1+D}
<
0.
\]
If \(\mu\{z>-16a\}=0\), equivalence of \(\mu\) and \(\nu\) would force
\[
\mathbb E_\nu[z]\le-16a,
\]
a contradiction. If \(\mu\{z<0\}=0\), it would force
\[
\mathbb E_\nu[z]\ge0,
\]
also a contradiction. This proves the two excursion statements.

Finally, disintegrate \(\mu\) with respect to its \(x\)-marginal. The conditional identity gives
\[
\int yz\,d\mu_x=-a<0
\]
for almost every represented \(x\). Since \(y>0\) on the support, the conditional law cannot be supported in
\[
z\ge0.
\]
Thus it gives positive mass to
\[
z<0.
\]

## Verification
The accompanying checker uses exact rational sparse-polynomial arithmetic.

It verifies
\[
Lz=1-4x,
\]
\[
L\left(\frac{y^2}{2}\right)=x^2y-y^2,
\]
and the equilibrium equations at
\[
\left(\frac14,\frac1{16},-16a\right).
\]
It also verifies the characteristic polynomial
\[
\lambda^3+\lambda^2+\left(8a+\frac14\right)\lambda+\frac14,
\]
the identity
\[
D=16\,\operatorname{Var}(x),
\]
and the weighted-height algebra
\[
\frac{-a}{(1+D)/16}
=
-\frac{16a}{1+D}.
\]

The stored checker output is `VERIFY_OK`.

The conditional law
\[
\mathbb E[yz\mid x]=-a
\]
uses arbitrary one-variable antiderivative test functions. Positivity of \(y\), defect rigidity, and the excursion conclusion use bounded completeness and invariant-support arguments. No finite trajectory experiment is used as an infinite-time proof.

## Relationship to prior work
The foundational Wang–Chen paper introduces the system by adding the constant parameter \(a\) to Sprott E, gives the unique equilibrium
\[
\left(\frac14,\frac1{16},-16a\right),
\]
and numerically exhibits chaotic dynamics while the equilibrium is stable for positive \(a\). Its analysis centers on local stability, Lyapunov exponents, spectra, and period-doubling.

A subsequent full study demonstrates coexistence of point, periodic, and strange attractors at
\[
a=0.01.
\]
That paper gives the same equations and equilibrium and studies Lyapunov exponents, bifurcation diagrams, and basins of attraction. Full-text searches found no invariant-measure, stationary-average, or mean formulation.

Another full mathematical treatment generalizes the first equation to
\[
\dot x=yz+h(x)
\]
with a quadratic \(h\), explicitly identifies the constant-control Wang–Chen system as a special case, and develops equilibrium stability, Hopf bifurcation, and synchronization. Its stated classification places the problem in ordinary-differential-equation dynamics.

Later work studies the same Wang–Chen flow by Poincaré compactification and Jacobi stability. Its accessible description concerns the sphere at infinity, the equilibrium, and periodic-orbit geometry rather than stationary disintegration or weighted-height identities.

The degenerate case \(a=0\) is exactly Sprott E. Previously available stationary identities for that zero-forcing case determine
\[
\mathbb E[x\mid z]
\]
and
\[
\mathbb E[x^2\mid y].
\]
They do not imply the forcing-specific law
\[
\mathbb E[yz\mid x]=-a
\]
for \(a>0\), nor the nontrivial equilibrium-height contraction
\[
\mathbb E_\nu[z]
=
-\frac{16a}{1+D}.
\]
Those forcing-specific statements and their strict excursion consequences are the originality-bearing content here.

## Limitations
The result concerns compactly supported invariant probability measures. It does not prove existence of the periodic or strange attractors for every positive \(a\), nor classify their basins.

The weighted measure \(\nu\) is not itself asserted to be invariant. It is a stationary-state diagnostic obtained by reweighting an invariant measure with the strictly positive coordinate \(y\).

The conclusion forces positive mass above the equilibrium height and below zero, but it does not require positive mass below the equilibrium height.

The complete 2020 global-geometry article was not available in a securely inspectable full-text form. Its accessible abstract and references were compared, so an unindexed stationary identity in that article remains a specific residual literature risk.

## References
1. X. Wang and G. Chen, “A chaotic system with only one stable equilibrium,” arXiv:1101.4067, first posted 21 January 2011; Communications in Nonlinear Science and Numerical Simulation 17, 1264–1272, DOI 10.1016/j.cnsns.2011.07.017.
2. J. C. Sprott, X. Wang, and G. Chen, “Coexistence of Point, Periodic and Strange Attractors,” International Journal of Bifurcation and Chaos 23, 1350093 (2013), DOI 10.1142/S0218127413500934.
3. Z. Wei and Z. Wang, “Chaotic behavior and modified function projective synchronization of a simple system with one stable equilibrium,” Kybernetika 49, 359–374 (2013), DML-CZ record 143372.
4. B. Chen, Y. Liu, Z. Wei, and C. Feng, “New insights into a chaotic system with only a Lyapunov stable equilibrium,” Mathematical Methods in the Applied Sciences 43, 9262–9279 (2020), DOI 10.1002/mma.6619.
