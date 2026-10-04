# Conditional stationary laws and an exact equilibrium-height defect in the Chen system
## Finding
Consider the Chen system
\[
\dot x=a(y-x),\qquad
\dot y=(c-a)x-xz+cy,\qquad
\dot z=xy-bz,
\]
with
\[
a>0,\qquad b>0,\qquad \rho=2c-a>0.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the conditional stationary laws
\[
\mathbb E_\mu[y\mid x]=x
\]
and
\[
\mathbb E_\mu[xy\mid z]=bz.
\]
In particular,
\[
\mathbb E_\mu[xy]
=
\mathbb E_\mu[x^2]
=
b\,\mathbb E_\mu[z].
\]

The same measure satisfies the exact equilibrium-height defect
\[
\mathbb E_\mu[(z-\rho)x^2]
=
a\,\mathbb E_\mu[(y-x)^2].
\]

Equality holds exactly for convex mixtures of the three equilibrium atoms
\[
O=(0,0,0),
\]
\[
C_\pm=
\left(
\pm\sqrt{b\rho},
\pm\sqrt{b\rho},
\rho
\right).
\]

Every compact invariant probability measure not supported on those three equilibria therefore assigns positive mass to
\[
z>\rho,
\]
and positive mass to each of
\[
y>x
\qquad\text{and}\qquad
y<x.
\]

Consequently every nonconstant periodic orbit reaches a height strictly above \(\rho\) and crosses the plane \(y=x\) at least twice in each least period.

For the classical parameters
\[
a=35,\qquad b=3,\qquad c=28,
\]
one has
\[
\rho=21,\qquad
C_\pm=(\pm3\sqrt7,\pm3\sqrt7,21),
\]
and
\[
\mathbb E_\mu[(z-21)x^2]
=
35\,\mathbb E_\mu[(y-x)^2].
\]
Thus every non-equilibrium compact recurrent statistical state reaches \(z>21\).

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the Chen flow and supported on compact subsets of \(\mathbb R^3\). Compact support guarantees integrability of every test function used below.

The hypotheses \(a>0\), \(b>0\), and \(\rho=2c-a>0\) are exactly the sign conditions needed for the stated three-equilibrium geometry. The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

The level \(z=\rho\) is dynamically natural in the established Chen-system literature: it is the common height of the two nonzero equilibria, and the classical bifurcation analysis uses \(z=2c-a\) as a Poincaré section for the chaotic attractor.

## Proof
Let \(L\) denote the generator of the flow. If \(\mu\) is compactly supported and invariant, then
\[
\int LH\,d\mu=0
\]
for every continuously differentiable \(H\).

Let \(\phi\) be any continuous function on the compact \(x\)-range, and choose \(H\) with \(H'(x)=\phi(x)\). Then
\[
LH=a\phi(x)(y-x).
\]
Therefore
\[
\mathbb E_\mu[y-x\mid x]=0,
\]
which is equivalent to
\[
\mathbb E_\mu[y\mid x]=x.
\]

Likewise, for any continuous \(\psi\) on the compact \(z\)-range, choose \(K'(z)=\psi(z)\). Then
\[
LK=\psi(z)(xy-bz),
\]
and hence
\[
\mathbb E_\mu[xy\mid z]=bz.
\]

The first conditional law gives
\[
\mathbb E_\mu[xy]=\mathbb E_\mu[x^2],
\]
while the second gives
\[
\mathbb E_\mu[xy]=b\,\mathbb E_\mu[z].
\]

Set
\[
d=y-x.
\]
Using the equations,
\[
\dot d=(\rho-z)x+(c-a)d.
\]
Define
\[
F
=
xd-\frac{c-a}{2a}x^2
=
xy-\frac{a+c}{2a}x^2.
\]
A direct calculation gives the exact polynomial coboundary
\[
LF
=
a(y-x)^2+(\rho-z)x^2.
\]
After integration,
\[
\mathbb E_\mu[(z-\rho)x^2]
=
a\,\mathbb E_\mu[(y-x)^2].
\]

Because \(a>0\), equality holds if and only if \(y=x\) almost surely. The support of an invariant probability measure is invariant under the complete flow on that compact support, so the support then lies in the invariant part of the plane \(y=x\).

On \(y=x\),
\[
\frac{d}{dt}(y-x)=(\rho-z)x.
\]
If \(x=0\), then \(y=0\) and
\[
\dot z=-bz.
\]
Any point with \(z\ne0\) has a backward trajectory whose magnitude grows exponentially and therefore cannot belong to a compact invariant support. Thus this branch contributes only \(O\).

If \(x\ne0\), tangency to \(y=x\) forces
\[
z=\rho.
\]
Tangency to \(z=\rho\) then gives
\[
0=\dot z=x^2-b\rho,
\]
so
\[
x=y=\pm\sqrt{b\rho}.
\]
These are exactly \(C_+\) and \(C_-\). Conversely, every convex mixture of the three equilibrium atoms is invariant and realizes equality.

For any other compact invariant measure,
\[
\mathbb E_\mu[(z-\rho)x^2]>0.
\]
The integrand is nonpositive on \(z\le\rho\), so positive expectation forces positive mass on
\[
z>\rho.
\]

Finally, invariance applied to the coordinate \(x\) gives
\[
\mathbb E_\mu[y-x]=0.
\]
Outside the equality class,
\[
\mathbb E_\mu[(y-x)^2]>0,
\]
so the continuous observable \(y-x\) must take both signs on sets of positive measure.

A nonconstant periodic orbit carries its normalized orbit measure and is not an equilibrium mixture. It therefore reaches \(z>\rho\), and its periodic continuous function \(y-x\) takes both signs. On a periodic circle that forces at least two zeros of \(y-x\) per least period.

## Verification
The accompanying standard-library checker uses exact sparse-polynomial arithmetic over rational coefficients.

It verifies
\[
Lx=a(y-x),
\]
\[
Lz=xy-bz,
\]
the difference equation
\[
L(y-x)=(\rho-z)x+(c-a)(y-x),
\]
and the critical certificate
\[
L\left(
xy-\frac{a+c}{2a}x^2
\right)
=
a(y-x)^2+(\rho-z)x^2.
\]

It also verifies the classical parameter reductions
\[
\rho=21,
\qquad
b\rho=63,
\]
and checks the equilibrium equations symbolically through \(x^2=b\rho\), \(y=x\), and \(z=\rho\).

The stored checker output is `VERIFY_OK`. The conditional identities use arbitrary continuous test functions through antiderivatives on compact coordinate ranges; they are not finite-sampling arguments. Equality rigidity additionally uses invariance of the compact support.

## Relationship to prior work
Chen and Ueta introduced the attractor in 1999. Their later full bifurcation analysis records the symmetry, dissipativity, the three equilibria
\[
O,\qquad
C_\pm=
\left(
\pm\sqrt{(2c-a)b},
\pm\sqrt{(2c-a)b},
2c-a
\right),
\]
and a detailed bifurcation picture for equilibria and periodic solutions.

For the classical parameters \((a,b,c)=(35,3,28)\), that same full analysis gives
\[
C_\pm=(\pm3\sqrt7,\pm3\sqrt7,21)
\]
and uses
\[
z=2c-a,\qquad y>x
\]
as one of the Poincaré sections for the chaotic attractor. Thus the height appearing in the defect is already a distinguished dynamical level in the primary same-object literature.

A 2003 paper on complex dynamical behavior derives a precise bound and states in its abstract that every nontrivial trajectory passes alternately through two specified Poincaré projections infinitely often. Only abstract and first-page material were available in the inspected sources, so possible overlap between that trajectory-crossing theorem and the height-crossing corollary here remains a bibliographic risk. The accessible statement does not give the conditional stationary laws or the exact weighted defect above.

Targeted searches for invariant-measure, stationary-moment, conditional-expectation, equilibrium-height, and equivalent weighted-defect formulations found no same-object statement implying the final theorem. The closest indexed exact identities concern different polynomial flows.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not classify unbounded trajectories, prove existence of nontrivial compact recurrence throughout the parameter region, or supply a lower bound on periodic-orbit periods.

The result forces every non-equilibrium compact recurrent state above \(z=\rho\), but it does not by itself force visits below that height.

The foundational 1999 source was checked through bibliographic and abstract material. The 2000 bifurcation analysis was inspected in full through the authors' public HTML version. The complete 2003 trajectory-analysis paper was unavailable in the inspected sources; its abstract indicates a potentially related Poincaré-crossing theorem, and this remains the main residual literature risk.

## References
1. G. Chen and T. Ueta, “Yet Another Chaotic Attractor,” International Journal of Bifurcation and Chaos 9(7), 1465–1466 (1999), DOI 10.1142/S0218127499001024.
2. T. Ueta and G. Chen, “Bifurcation Analysis of Chen's Equation,” International Journal of Bifurcation and Chaos 10(8), 1917–1931 (2000), DOI 10.1142/S0218127400001183.
3. T. Zhou, Y. Tang, and G. Chen, “Complex Dynamical Behaviors of the Chaotic Chen's System,” International Journal of Bifurcation and Chaos 13(9), 2561–2574 (2003), DOI 10.1142/S0218127403008089.
