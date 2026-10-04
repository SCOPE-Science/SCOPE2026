# Sharp stationary sign criterion and exact coordinatewise flux laws for the Chen–Lee flow
## Finding
Consider the normalized Chen–Lee system
\[
\dot x=-yz+ax,\qquad
\dot y=xz+by,\qquad
\dot z=\frac13xy+cz,
\]
with
\[
abc\ne0.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the three exact conditional laws
\[
\mathbb E_\mu[yz\mid x]=ax,
\]
\[
\mathbb E_\mu[xz\mid y]=-by,
\]
and
\[
\mathbb E_\mu[xy\mid z]=-3cz.
\]

Let
\[
Q=\mathbb E_\mu[xyz].
\]
Then
\[
Q
=
a\,\mathbb E_\mu[x^2]
=
-b\,\mathbb E_\mu[y^2]
=
-3c\,\mathbb E_\mu[z^2].
\]

If
\[
\mu\ne\delta_{(0,0,0)},
\]
all three second moments are strictly positive. Therefore a non-origin compact invariant probability measure can exist only when
\[
\operatorname{sgn}(a)
=
-\operatorname{sgn}(b)
=
-\operatorname{sgn}(c).
\]

This sign condition is also sufficient. Whenever it holds, the four nonzero equilibria exist and are characterized by
\[
x^2=3bc,\qquad
y^2=-3ac,\qquad
z^2=-ab,\qquad
xyz=3abc.
\]
Their equilibrium atoms are compact invariant probability measures distinct from the origin atom.

Hence, for nonzero parameters,
\[
\boxed{
\text{a non-origin compact invariant probability measure exists}
\iff
\operatorname{sgn}(a)
=
-\operatorname{sgn}(b)
=
-\operatorname{sgn}(c)
}.
\]

At the classical Chen–Lee parameters
\[
a=5,\qquad
b=-10,\qquad
c=-\frac{19}{5},
\]
every non-origin compact invariant probability measure satisfies the universal RMS ratio
\[
5\,\mathbb E[x^2]
=
10\,\mathbb E[y^2]
=
\frac{57}{5}\,\mathbb E[z^2]
>0.
\]

## Assumptions and scope
The measure \(\mu\) is a Borel probability measure invariant under the Chen–Lee flow and supported on a compact subset of \(\mathbb R^3\). Compact support guarantees integrability of all test functions used below and ensures that every point in the support lies on a bounded complete trajectory.

The normalization is the one obtained in the foundational rigid-body construction after taking the inertia ratio
\[
I_3:I_1:I_2=3:2:1.
\]
In this normalization the original paper writes
\[
\dot x=-yz+ax,\qquad
\dot y=xz+by,\qquad
\dot z=\frac13xy+cz.
\]

The theorem assumes
\[
abc\ne0.
\]
The zero-parameter coordinate planes have additional degeneracies and are not part of the accepted claim.

The earliest verified public source date for the system is 1 August 2004.

## Proof
Let \(L\) denote the generator of the flow.

For any continuous function \(\phi\) on the compact \(x\)-range, choose an antiderivative \(H\) with
\[
H'(x)=\phi(x).
\]
Then
\[
LH
=
\phi(x)(-yz+ax).
\]
Invariance gives
\[
\mathbb E_\mu[\phi(x)(-yz+ax)]=0
\]
for every such \(\phi\). Therefore
\[
\mathbb E_\mu[yz\mid x]=ax.
\]

The same argument in the other two coordinates gives
\[
\mathbb E_\mu[xz\mid y]=-by
\]
and
\[
\mathbb E_\mu[xy\mid z]=-3cz.
\]

Next,
\[
L\left(\frac{x^2}{2}\right)
=
-xyz+ax^2,
\]
so
\[
\mathbb E[xyz]
=
a\,\mathbb E[x^2].
\]

Likewise,
\[
L\left(\frac{y^2}{2}\right)
=
xyz+by^2
\]
gives
\[
\mathbb E[xyz]
=
-b\,\mathbb E[y^2],
\]
and
\[
L\left(\frac{z^2}{2}\right)
=
\frac13xyz+cz^2
\]
gives
\[
\mathbb E[xyz]
=
-3c\,\mathbb E[z^2].
\]

Thus, with
\[
Q=\mathbb E[xyz],
\]
we have
\[
Q
=
a\,\mathbb E[x^2]
=
-b\,\mathbb E[y^2]
=
-3c\,\mathbb E[z^2].
\]

It remains to rule out a non-origin invariant measure with a vanishing second moment. Suppose, for example, that
\[
\mathbb E[x^2]=0.
\]
Then \(x=0\) almost surely, so the invariant support lies in the plane \(x=0\). Tangency to that plane requires
\[
yz=0.
\]
Along such a support trajectory the remaining equations reduce to
\[
\dot y=by,\qquad
\dot z=cz.
\]
Because \(b\) and \(c\) are nonzero, the only solution bounded for all positive and negative time is
\[
y=z=0.
\]
Hence the support is the origin.

The same argument, after cyclicly choosing a zero second moment, shows that any invariant measure with one of
\[
\mathbb E[x^2],\qquad
\mathbb E[y^2],\qquad
\mathbb E[z^2]
\]
equal to zero is the origin atom.

Therefore every non-origin compact invariant measure has all three second moments strictly positive. The common quantity \(Q\) then has simultaneously the signs
\[
\operatorname{sgn}(a),\qquad
-\operatorname{sgn}(b),\qquad
-\operatorname{sgn}(c),
\]
which proves the necessary sign condition.

For sufficiency, assume
\[
\operatorname{sgn}(a)
=
-\operatorname{sgn}(b)
=
-\operatorname{sgn}(c).
\]
Then
\[
3bc>0,\qquad
-3ac>0,\qquad
-ab>0.
\]
Choose signs of \(x,y,z\) so that
\[
x^2=3bc,\qquad
y^2=-3ac,\qquad
z^2=-ab,\qquad
xyz=3abc.
\]
There are four such sign choices. The identities
\[
yz=ax,\qquad
xz=-by,\qquad
xy=-3cz
\]
then hold, so all three right-hand sides of the vector field vanish. These are four nonzero equilibria, and their atoms prove sufficiency.

At
\[
(a,b,c)=\left(5,-10,-\frac{19}{5}\right),
\]
the common-moment identity becomes
\[
5\,\mathbb E[x^2]
=
10\,\mathbb E[y^2]
=
\frac{57}{5}\,\mathbb E[z^2].
\]
Strict positivity follows for every non-origin compact invariant measure.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients.

It verifies
\[
L\left(\frac{x^2}{2}\right)
=
-xyz+ax^2,
\]
\[
L\left(\frac{y^2}{2}\right)
=
xyz+by^2,
\]
and
\[
L\left(\frac{z^2}{2}\right)
=
\frac13xyz+cz^2.
\]

For the classical parameters
\[
\left(5,-10,-\frac{19}{5}\right),
\]
it verifies the exact coefficient chain
\[
5,\qquad
10,\qquad
\frac{57}{5},
\]
and the nonzero-equilibrium square relations
\[
x^2=114,\qquad
y^2=57,\qquad
z^2=50.
\]

The stored output is `VERIFY_OK`.

The checker validates the algebraic certificates. The conditional laws use arbitrary one-variable test functions, and the zero-second-moment rigidity uses bounded completeness of the compact invariant support.

## Relationship to prior work
Chen and Lee introduced the system from Euler rigid-body equations with linear feedback. In the normalized system they identify the sign regime
\[
a>0,\qquad b<0,\qquad c<0
\]
together with the additional dissipativity inequality
\[
0<a<-(b+c)
\]
as a necessary regime for their chaotic construction, and note symmetry-related alternatives. They then report strange attractors and limit cycles numerically.

A later full equilibrium analysis solves the same normalized equations and exhibits the origin plus four nonzero equilibria for the classical sign regime. It studies their linear stability and circuit realization. Targeted full-text searches of that source did not locate invariant-measure, stationary-average, or mean-square formulations.

A Hamilton–Poisson treatment studies special parameter choices of the Chen–Lee system from Poisson geometry and analyzes stability, periodic solutions, and numerical integrators. Its scope is a special Hamiltonian subfamily rather than an all-parameter compact-stationary sign theorem.

The accepted result turns the sign pattern from a local/equilibrium and chaos-construction feature into an exact criterion for existence of any non-origin compact invariant probability measure, and sharpens the global quadratic balance to three coordinatewise conditional laws.

## Limitations
The theorem is stated only for
\[
abc\ne0.
\]
Degenerate zero-parameter cases can carry invariant coordinate subspaces and require separate classification.

The existence criterion is for non-origin compact invariant probability measures. It does not exclude nonrecurrent bounded connecting orbits whose only invariant time-average is the origin atom.

The theorem does not prove a strange attractor or a nonconstant periodic orbit for every admissible sign triple. Sufficiency is supplied by the four nonzero equilibrium atoms.

The Hamilton–Poisson literature contains special integrable parameter cases, and a differently phrased stationary balance could remain unlocated. The originality claim is restricted to the all-parameter invariant-measure sign criterion, the conditional laws, and the resulting universal second-moment ratios.

## References
1. H.-K. Chen and C.-I. Lee, “Anti-control of chaos in rigid body motion,” Chaos, Solitons & Fractals 21, 957–965 (2004), DOI 10.1016/j.chaos.2003.12.034.
2. L.-J. Sheu, L.-M. Tam, H.-K. Chen, and S.-K. Lao, “Alternative implementation of the chaotic Chen-Lee system,” Chaos, Solitons & Fractals 41, 1923–1929 (2009), DOI 10.1016/j.chaos.2008.07.053.
3. C. Pop Arieşanu, “A Hamilton-Poisson Model of the Chen-Lee System,” Journal of Applied Mathematics 2012, Article 484028, DOI 10.1155/2012/484028.
4. J.-H. Chen, H.-K. Chen, and Y.-K. Lin, “Synchronization and anti-synchronization coexist in Chen-Lee chaotic systems,” Chaos, Solitons & Fractals 39, 707–716, DOI 10.1016/j.chaos.2007.01.104.
