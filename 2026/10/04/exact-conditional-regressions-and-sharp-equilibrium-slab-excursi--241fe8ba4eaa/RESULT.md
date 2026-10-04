# Exact conditional regressions and sharp equilibrium-slab excursions in the generalized Sprott H flow
## Finding
Consider the generalized Sprott H system
\[
\dot x=-y+z^2,\qquad
\dot y=x+ay,\qquad
\dot z=x-bz,
\]
with \(a,b>0\). Its two equilibria are
\[
E_0=(0,0,0),\qquad
E_1=\left(-\frac{b^2}{a},\frac{b^2}{a^2},-\frac ba\right).
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the three conditional stationary laws
\[
\mathbb E_\mu[x\mid z]=bz,
\qquad
\mathbb E_\mu[x\mid y]=-ay,
\qquad
\mathbb E_\mu[y-z^2\mid x]=0.
\]
It also satisfies the exact height-circle identity
\[
\mathbb E_\mu\!\left[\left(z+\frac{b}{2a}\right)^2\right]
=
\left(\frac{b}{2a}\right)^2
\]
and the exact horizontal defect identity
\[
\mathbb E_\mu\!\left[x\left(x+\frac{b^2}{a}\right)\right]
=
\mathbb E_\mu[(x-bz)^2].
\]

The right-hand side of the horizontal defect vanishes exactly when \(\mu\) is supported on \(\{E_0,E_1\}\). Equivalently, the height product
\[
z\left(z+\frac ba\right)
\]
vanishes \(\mu\)-almost surely exactly for measures supported on those two equilibria.

Consequently every compact invariant probability measure not supported on \(\{E_0,E_1\}\) assigns positive mass both to
\[
-\frac ba<z<0
\]
and to the strict exterior
\[
z<-\frac ba\quad\text{or}\quad z>0.
\]
It also assigns positive mass outside the closed horizontal slab
\[
-\frac{b^2}{a}\le x\le0.
\]
Every nonconstant periodic orbit crosses the boundary of each equilibrium-coordinate slab at least twice per least period.

For the standard chaotic parameters \(a=1/2\), \(b=1\), these identities become
\[
\mathbb E[(z+1)^2]=1,
\qquad
\mathbb E[x(x+2)]=\mathbb E[(x-z)^2],
\]
with equilibria \((0,0,0)\) and \((-2,4,-2)\).

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the flow and supported on compact subsets of \(\mathbb R^3\). Compact support guarantees integrability of the polynomial generator identities and allows arbitrary continuously differentiable test functions on the compact coordinate ranges.

The equations are the two-parameter Case H normalization given in the primary-author parameter survey. The canonical chaotic choice is \(a=1/2\), \(b=1\). The earliest verified public source date used for this flow is 1994-08-01.

## Proof
Let \(L\) be the generator. Invariance gives
\[
\int Lh\,d\mu=0
\]
for every continuously differentiable test function \(h\) used below.

For a test function depending only on \(z\),
\[
Lh(z)=h'(z)(x-bz).
\]
Because every continuous function on the compact \(z\)-range has an antiderivative, invariance yields
\[
\mathbb E_\mu[x-bz\mid z]=0,
\]
which is the first conditional law. Applying the same argument to functions of \(y\) and functions of \(x\) gives
\[
\mathbb E_\mu[x+ay\mid y]=0,
\qquad
\mathbb E_\mu[-y+z^2\mid x]=0,
\]
and therefore the other two conditional laws.

A first exact polynomial coboundary is
\[
L(ax+y-z)=az^2+bz.
\]
After integration,
\[
a\mathbb E[z^2]+b\mathbb E[z]=0,
\]
which is equivalent to
\[
\mathbb E\!\left[\left(z+\frac{b}{2a}\right)^2\right]
=
\left(\frac{b}{2a}\right)^2.
\]
Equivalently,
\[
\mathbb E\!\left[z\left(z+\frac ba\right)\right]=0.
\]

A second exact coboundary is
\[
L\!\left(abz^2+ab^2x+b^2y\right)
=
a x\left(x+\frac{b^2}{a}\right)-a(x-bz)^2.
\]
Since \(a>0\), stationarity gives
\[
\mathbb E\!\left[x\left(x+\frac{b^2}{a}\right)\right]
=
\mathbb E[(x-bz)^2]\ge0.
\]

If the right-hand side is zero, then \(x-bz=0\) on the support. The support of an invariant measure is invariant under the continuous flow, so along every complete trajectory in the support one has \(\dot z=0\), hence \(z\) is constant and \(x=bz\). Then \(\dot x=0\) gives \(y=z^2\), while \(\dot y=0\) gives
\[
z(b+az)=0.
\]
Thus the trajectory is either \(E_0\) or \(E_1\). Conversely, every probability supported on \(\{E_0,E_1\}\) makes the defect vanish.

The same equilibrium rigidity follows if
\[
z\left(z+\frac ba\right)=0
\]
almost surely. The invariant support is then contained in the two planes \(z=0\) and \(z=-b/a\). Continuity keeps each complete support trajectory in one component, and the tangency conditions reduce it to \(E_0\) or \(E_1\).

Now suppose \(\mu\) is not supported on \(\{E_0,E_1\}\). Then the random variable
\[
W=z\left(z+\frac ba\right)
\]
is not almost surely zero but has mean zero. Hence it assumes both signs with positive measure. Its negative set is exactly
\[
-\frac ba<z<0,
\]
and its positive set is exactly the strict exterior of that slab. This proves the sharp height excursion statement.

The horizontal defect is now strict:
\[
\mathbb E\!\left[x\left(x+\frac{b^2}{a}\right)\right]>0.
\]
Since the quadratic on the left is nonpositive on the closed interval \([-b^2/a,0]\), positive expectation forces positive mass in its strict exterior.

For a nonconstant periodic orbit, its normalized orbit measure is not supported on the two equilibria. The height conclusion supplies times both inside and outside the open \(z\)-slab, so continuity on the periodic circle forces at least two crossings of its boundary. Also
\[
\mathbb E[z]\in\left(-\frac ba,0\right),
\qquad
\mathbb E[x]=b\mathbb E[z]\in\left(-\frac{b^2}{a},0\right),
\]
while the horizontal defect supplies a time outside the closed \(x\)-slab. A continuous periodic function with mean strictly inside the slab and with an exterior value must enter the slab and leave it again, hence it crosses the horizontal slab boundary at least twice per least period.

## Verification
The accompanying dependency-free checker uses exact sparse-polynomial arithmetic. It verifies the two critical pointwise identities
\[
L(ax+y-z)=az^2+bz
\]
and
\[
L\!\left(abz^2+ab^2x+b^2y\right)
=
a x\left(x+\frac{b^2}{a}\right)-a(x-bz)^2,
\]
with the latter compared after clearing the displayed division. It also verifies the canonical equilibria at \(a=1/2\), \(b=1\). The stored output is `VERIFY_OK`.

The conditional-expectation statements are analytic consequences of the generator identity with arbitrary one-coordinate test functions; they are not inferred from finite simulation. The excursion conclusions use only sign analysis, support invariance, and continuity.

## Relationship to prior work
The primary-author parameter survey gives exactly this two-parameter Case H normalization and maps numerical parameter regions labeled stable equilibrium, periodic, chaotic, and unbounded. The theorem above supplies parameter-uniform necessary geometry for every compact recurrent statistical state when \(a,b>0\): two conditional regressions, a conditional quadratic balance, two exact stationary defects, and forced excursions relative to the two equilibrium coordinate levels.

A full publicly available author-uploaded paper on Sprott H reproduces the canonical equations and studies their dynamics and electronic circuit implementation. Its inspected text contains no invariant-measure, moment, variance, or conditional-balance theorem. A separate same-object paper studies numerical simulation, circuit implementation, synchronization, and secure communication.

A broader analytical paper on all Sprott flows studies asymptotic reformulations and mentions statistical treatment in its abstract. Only indexed metadata and abstract-level material were available during this comparison, so no whole-document noncoverage claim is made for that source. Targeted semantic searches over Sprott H aliases, invariant measures, stationary moments, conditional regressions, slab recurrence, and exact defects returned no same-object statement implying the result here.

## Limitations
The theorem concerns compactly supported invariant probability measures and periodic orbits. It does not prove existence of chaotic attractors or classify unbounded trajectories. The horizontal slab conclusion for a general invariant measure guarantees positive mass outside the slab but does not assert positive mass in its interior; the stronger two-sided crossing statement is proved for periodic orbits using continuity and the strict interior mean.

The 1994 foundational paper was inspected through its publisher record and abstract, not line by line. The broad 2004 analytical paper was available only through indexed metadata and abstract-level material. These are retained bibliographic risks, together with the possibility of differently phrased or unindexed older stationary identities.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note, 2013, https://sprott.physics.wisc.edu/technote/regions.htm.
3. M. F. Çıtak and Y. Çelik, “Electronic circuit design of Sprott H chaotic system with CCII+,” 22nd Signal Processing and Communications Applications Conference, 2014, DOI 10.1109/SIU.2014.6830654.
4. “Simulation and Circuit Implementation of Sprott Case H Chaotic System and its Synchronization Application for Secure Communication Systems,” International Journal of Bifurcation and Chaos, 2013, DOI 10.1142/S0218126613500229.
5. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21, 1271–1281 (2004), DOI 10.1016/j.chaos.2003.12.054.
