# Exact stationary equilibrium-cone balance and RMS trapping in the Wang multiscroll flow
## Finding
Consider the Wang multiscroll system
\[
\dot x=a(x-y)-yz,\qquad
\dot y=-by+xz,\qquad
\dot z=-cz+dx+xy,
\]
with
\[
a,b,c,d>0.
\]
Define
\[
\Delta=\sqrt{a^2+4ab},
\qquad
k_+=\frac{a+\Delta}{2a},
\qquad
k_-=\frac{\Delta-a}{2a}.
\]
Then
\[
k_+>0,\qquad k_->0,\qquad
k_+-k_-=1,\qquad
k_+k_-=\frac ba.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the exact coordinatewise stationary laws
\[
\mathbb E_\mu[y(a+z)\mid x]=ax,
\]
\[
\mathbb E_\mu[xz\mid y]=by,
\]
and
\[
\mathbb E_\mu[x(d+y)\mid z]=cz.
\]

It also satisfies the equilibrium-cone balance
\[
\mathbb E_\mu\!\left[(x-k_+y)(x+k_-y)\right]=0.
\]
The two zero lines
\[
x=k_+y,
\qquad
x=-k_-y
\]
are exactly the two \(xy\)-slopes occupied by the four nonzero equilibria.

The balance has a rigid equality set. It vanishes pointwise on the invariant support if and only if the measure is a convex mixture of the five equilibrium atoms: the origin and the four nonzero equilibria.

Consequently, every compact invariant probability measure that is not an equilibrium mixture gives positive mass to both regions
\[
(x-k_+y)(x+k_-y)>0
\]
and
\[
(x-k_+y)(x+k_-y)<0.
\]
Thus genuinely recurrent nonequilibrium stationary dynamics must straddle the equilibrium cone in the \(xy\)-projection.

There is also an exact RMS trapping law. For every non-origin compact invariant probability measure define
\[
R=
\sqrt{
\frac{\mathbb E_\mu[x^2]}
{\mathbb E_\mu[y^2]}
}.
\]
Then
\[
k_-\le R\le k_+.
\]
The upper equality holds exactly for convex mixtures supported on the origin and the two equilibria on
\[
x=k_+y,
\]
while the lower equality holds exactly for convex mixtures supported on the origin and the two equilibria on
\[
x=-k_-y.
\]
Every invariant measure that is not an equilibrium mixture obeys the strict inequalities
\[
k_-<R<k_+.
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the polynomial flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of the polynomial and one-variable antiderivative test functions used below, and every support point lies on a bounded complete trajectory.

The parameters are positive, as in the system introduced in the foundational source. That source gives five equilibria. If
\[
z_\pm=\frac{-a\pm\Delta}{2},
\]
then the four nonzero equilibria occur in two pairs at heights \(z_+\) and \(z_-\), with
\[
y=\frac{xz}{b}.
\]
Therefore their \(xy\)-slopes are
\[
\frac{x}{y}
=
\frac b{z_+}
=
k_+,
\qquad
\frac{x}{y}
=
\frac b{z_-}
=
-k_-.
\]

The earliest verified public date of the foundational source is 8 September 2008, its online-publication date.

## Proof
Let \(L\) be the generator of the flow.

For any continuous function \(\phi\) on the compact \(x\)-range, choose an antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
\phi(x)\bigl(ax-y(a+z)\bigr).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)(ax-y(a+z))]=0
\]
for every such \(\phi\), hence
\[
\mathbb E_\mu[y(a+z)\mid x]=ax.
\]

Applying the same argument to arbitrary antiderivative test functions of \(y\) and \(z\) gives
\[
\mathbb E_\mu[xz\mid y]=by
\]
and
\[
\mathbb E_\mu[x(d+y)\mid z]=cz.
\]

Now
\[
L\left(\frac{x^2+y^2}{2}\right)
=
a x^2-a xy-b y^2.
\]
Therefore every invariant measure satisfies
\[
\mathbb E[x^2-xy-(b/a)y^2]=0.
\]
Since
\[
k_+-k_-=1,
\qquad
k_+k_-=\frac ba,
\]
the quadratic factors:
\[
x^2-xy-\frac ba y^2
=
(x-k_+y)(x+k_-y).
\]
This proves the equilibrium-cone balance.

We next classify the pointwise-zero case. Suppose
\[
(x-k_+y)(x+k_-y)=0
\]
on the invariant support. The zero set is the union of the two planes
\[
x=ky,
\]
where \(k\) is either \(k_+\) or \(-k_-\). Both values satisfy
\[
ak^2-ak-b=0.
\]

A bounded complete support trajectory that reaches the intersection \(x=y=0\) must be the origin trajectory. Indeed, on that intersection
\[
\dot x=\dot y=0,\qquad
\dot z=-cz,
\]
and bounded completeness in both time directions forces \(z=0\).

Hence any non-origin support trajectory remains in one plane \(x=ky\). Along that plane tangency requires
\[
0=\frac{d}{dt}(x-ky)
=
y\left[a(k-1)+kb-z(1+k^2)\right].
\]
A non-origin bounded complete trajectory on the plane cannot have \(y=0\). Using
\[
b=ak(k-1)
\]
from the quadratic equation for \(k\), tangency reduces to
\[
z=a(k-1).
\]
Thus \(z\) is constant. Moreover,
\[
\dot y
=
y(-b+kz)
=
0,
\]
so \(y\) and \(x=ky\) are constant. The remaining equation
\[
0=-cz+dx+xy
\]
is exactly the equilibrium equation. Consequently every support point is one of the five equilibria.

Conversely, all five equilibrium atoms lie on the two zero planes, so every convex mixture of them has pointwise zero defect. This proves the equality classification.

If an invariant measure is not an equilibrium mixture, its cone polynomial is not zero almost surely. Since its expectation is zero, it cannot have only one sign. Therefore it gives positive mass to both open sign regions.

For the RMS bound, a non-origin invariant measure has
\[
\mathbb E[y^2]>0.
\]
Indeed, if \(y=0\) almost surely, support invariance gives \(xz=0\); the remaining complete bounded dynamics force the origin.

Set
\[
X=\mathbb E[x^2],\qquad
Y=\mathbb E[y^2],\qquad
C=\mathbb E[xy],
\qquad
R=\sqrt{X/Y}.
\]
The balance gives
\[
\frac CY
=
R^2-\frac ba.
\]
Cauchy–Schwarz gives
\[
-R
\le
R^2-\frac ba
\le
R.
\]
The positive roots of the two boundary quadratics are precisely \(k_-\) and \(k_+\), so
\[
k_-\le R\le k_+.
\]

Equality in Cauchy–Schwarz forces \(x=k_+y\) almost surely at the upper endpoint or \(x=-k_-y\) almost surely at the lower endpoint. The support-rigidity argument above then restricts the measure to the origin and the corresponding equilibrium pair. The converse is immediate. Any invariant measure that is not an equilibrium mixture therefore has strict RMS bounds.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients for the generator identity
\[
L\left(\frac{x^2+y^2}{2}\right)
=
a x^2-a xy-b y^2.
\]

It separately checks the defining algebra
\[
k_+-k_-=1,
\qquad
k_+k_-=\frac ba,
\]
through the equivalent quadratic relation
\[
ak^2-ak-b=0,
\]
and verifies the tangency reduction
\[
a(k-1)+kb=a(k-1)(1+k^2).
\]

For the source's three-scroll parameters
\[
a=0.977,\qquad
b=10,\qquad
c=4,\qquad
d=0.1,
\]
the checker verifies numerically to high precision that the two slope values obtained from the source equilibrium heights agree with \(k_+\) and \(-k_-\), and that the factored quadratic balance vanishes on those equilibrium rays.

The stored checker output is `VERIFY_OK`.

The checker verifies the nonstandard algebraic certificates. The conditional expectations use arbitrary one-variable test functions, while the equality classification uses invariant-support tangency and bounded completeness.

## Relationship to prior work
The foundational article introduces the exact four-parameter quadratic system, derives its five equilibria, analyzes local equilibrium stability and dissipation, and reports periodic, two-scroll, three-scroll, and four-scroll regimes. It explicitly notes that the switching mechanism among the observed multiscroll states remains unexplained. No invariant-probability, stationary-average, RMS, or equilibrium-cone theorem appears in the inspected full text.

A later mathematical study of simple three-dimensional quadratic multiscroll systems treats the number and placement of equilibria as a central organizing feature and cites the Wang system as a principal example. Its analysis develops algebraic equilibrium conditions and numerical multiscroll examples rather than stationary invariant-measure balances.

The present finding uses the same equilibrium geometry but at the level of arbitrary compact invariant probability measures. The two equilibrium slopes become the exact factor lines of a stationary quadratic balance, yielding both sign-straddling of nonequilibrium stationary states and sharp RMS trapping.

## Limitations
The result is a necessary structural law for compact stationary recurrence. It does not prove existence of a chaotic attractor at any parameter value and does not explain the detailed orbit-by-orbit mechanism that creates or destroys individual scrolls.

The equality classification concerns invariant probability measures. It does not classify nonrecurrent bounded connecting sets that may carry only equilibrium invariant measures.

The RMS ratio uses second moments only and does not determine the full invariant distribution.

The originality comparison is strongest for the foundational full text and the later full multiscroll-equilibrium study. A differently phrased stationary balance in unindexed control, synchronization, or circuit literature could remain unlocated.

## References
1. L. Wang, “3-scroll and 4-scroll chaotic attractors generated from a new 3-D quadratic autonomous system,” Nonlinear Dynamics 56, 453–462 (2009), DOI 10.1007/s11071-008-9417-4. Published online 8 September 2008.
2. Z. Elhadj and J. C. Sprott, “Simplest 3D continuous-time quadratic systems as candidates for generating multiscroll chaotic attractors,” International Journal of Bifurcation and Chaos 23, 1350120 (2013), DOI 10.1142/S0218127413501204.
