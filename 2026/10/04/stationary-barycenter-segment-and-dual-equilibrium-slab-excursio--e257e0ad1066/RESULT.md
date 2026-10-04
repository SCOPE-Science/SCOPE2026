# Stationary barycenter segment and dual equilibrium-slab excursions in the generalized Sprott G flow
## Finding
Consider the generalized Sprott G system
\[
\dot x=ax+bz,\qquad
\dot y=xz-y,\qquad
\dot z=-x+y,
\]
with parameters \(a>0\) and \(b>0\). Put
\[
c=\frac ba.
\]
The two equilibria are
\[
e_0=(0,0,0),\qquad e_1=(-c,-c,1).
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the conditional regression law
\[
\mathbb E_\mu[z\mid x]= -\frac ab x.
\]
Writing
\[
p=\mathbb E_\mu[z],
\]
one has the exact barycenter and variance identities
\[
0\le p\le1,
\]
\[
\mathbb E_\mu[x]=\mathbb E_\mu[y]=-cp,
\qquad
\mathbb E_\mu[z]=p,
\]
and
\[
\mathbb E_\mu[x^2]=c^2p,
\qquad
\operatorname{Var}_\mu(x)=c^2p(1-p).
\]
Thus the barycenter of every compact stationary state lies on the line segment joining \(e_0\) and \(e_1\), while the \(x\)-variance is fixed exactly by its position on that segment.

There is also an exact height defect:
\[
\mathbb E_\mu\!\left[\left(z-\frac12\right)^2\right]
=
\frac14+rac1{b^2}\mathbb E_\mu[(\dot x)^2].
\]
Equality holds exactly for convex mixtures of the two equilibrium atoms \(\delta_{e_0}\) and \(\delta_{e_1}\).

Finally,
\[
\mathbb E_\mu[x(x+c)]=0.
\]
Hence every compact invariant measure that is not supported on \(\{e_0,e_1\}\) gives positive mass both to
\[
-c<x<0
\]
and to the strict exterior
\[
x<-c\quad\text{or}\quad x>0.
\]
Every nonconstant periodic orbit therefore crosses the boundary of the equilibrium \(x\)-slab \([-c,0]\) at least twice per least period. It also crosses the boundary of the equilibrium \(z\)-slab \([0,1]\) at least twice per least period.

For the canonical Sprott G parameters \(a=0.4\), \(b=1\), one has \(c=2.5\), so the equilibrium pair is
\[
(0,0,0),\qquad (-2.5,-2.5,1),
\]
and every compact stationary barycenter lies on the segment joining them.

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the flow and supported on compact subsets of \(\mathbb R^3\). Compact support makes all polynomial generator identities and all conditional-expectation test functions below integrable. The periodic statement concerns a nonconstant classical periodic solution and its least positive period.

Sprott's two-parameter Case G normalization is
\[
\dot x=ax+bz,\qquad \dot y=xz-y,\qquad \dot z=-x+y,
\]
and his parameter survey displays the canonical chaotic choice \(a=0.4\), \(b=1\). The earliest verified public source date used for the system is 1994-08-01.

## Proof
Let \(L\) denote the generator of the flow. For every continuously differentiable test function whose derivative is integrable against \(\mu\), invariance gives
\[
\int Lh\,d\mu=0.
\]

First take \(h\) to depend only on \(x\). Since
\[
Lh(x)=h'(x)(ax+bz),
\]
for every continuous function \(\phi\) on the compact \(x\)-range of the support, choosing an antiderivative with \(h'=\phi\) gives
\[
\mathbb E_\mu[(ax+bz)\phi(x)]=0.
\]
Therefore
\[
\mathbb E_\mu[ax+bz\mid x]=0,
\]
which is the conditional law
\[
\mathbb E_\mu[z\mid x]= -\frac ab x.
\]

The coordinate generators give
\[
0=\mathbb E_\mu[Lz]= -\mathbb E_\mu[x]+\mathbb E_\mu[y],
\]
so if \(m=\mathbb E_\mu[x]\), then \(\mathbb E_\mu[y]=m\). Also
\[
0=\mathbb E_\mu[Ly]=\mathbb E_\mu[xz]-\mathbb E_\mu[y],
\]
hence
\[
\mathbb E_\mu[xz]=m.
\]
Finally
\[
0=\mathbb E_\mu[Lx]=am+b\mathbb E_\mu[z].
\]
Writing \(p=\mathbb E_\mu[z]\) and \(c=b/a\), this gives
\[
m=-cp.
\]

Stationarity of \(x^2\) yields
\[
0=\mathbb E_\mu[L(x^2)]
=2a\mathbb E_\mu[x^2]+2b\mathbb E_\mu[xz],
\]
so
\[
\mathbb E_\mu[x^2]= -\frac ba m=c^2p.
\]
Therefore
\[
\operatorname{Var}_\mu(x)
=c^2p-c^2p^2
=c^2p(1-p).
\]
Nonnegativity of variance implies
\[
0\le p\le1.
\]
This proves the barycenter segment and variance parabola.

The signed slab balance has a direct polynomial certificate. Define
\[
H_1=\frac12x^2-b(y+z).
\]
A direct differentiation gives
\[
LH_1=ax^2+bx=a\,x(x+c).
\]
Hence
\[
\mathbb E_\mu[x(x+c)]=0.
\]
The polynomial \(x(x+c)\) is strictly negative on \((-c,0)\), strictly positive outside \([-c,0]\), and vanishes only at the two boundary values. If a compact invariant measure were supported only on those boundary values of \(x\), invariance of its support and continuity of trajectories would force \(x\) to be constant along each support orbit. Then \(\dot x=0\) gives \(z=-(a/b)x\), \(\dot z=0\) gives \(y=x\), and \(\dot y=0\) gives \(x(z-1)=0\). Thus only \(e_0\) and \(e_1\) occur. Consequently every other invariant measure must put positive mass on both signs of \(x(x+c)\), proving the forced \(x\)-slab excursion.

For the height defect, define
\[
H_2=-\frac a2x^2-bx-ab(y+z).
\]
Exact differentiation gives
\[
LH_2
=b^2z(z-1)-(ax+bz)^2.
\]
Since \(ax+bz=\dot x\), integration yields
\[
b^2\mathbb E_\mu[z(z-1)]
=
\mathbb E_\mu[(\dot x)^2].
\]
Equivalently,
\[
\mathbb E_\mu\!\left[\left(z-\frac12\right)^2\right]
=
\frac14+rac1{b^2}\mathbb E_\mu[(\dot x)^2].
\]

Equality holds exactly when \(\dot x=0\) almost surely. The support of an invariant measure for a continuous flow is invariant, so every complete support trajectory then has constant \(x\). The same three equations used above force that trajectory to be one of the two equilibria. Conversely every convex mixture of their atoms has equality. This proves sharp rigidity.

If a periodic orbit is nonconstant, its normalized orbit measure is not an equilibrium mixture. Hence \(0<p<1\), its \(x\)-coordinate spends positive time both inside and outside \([-c,0]\), and continuity on the periodic circle forces at least two crossings of that slab boundary. The height defect is strict, so the orbit has some point outside \([0,1]\). Its continuous \(z\)-image cannot avoid the open interval \((0,1)\): otherwise the connected image of the periodic circle would lie entirely in either \(( -\infty,0]\) or \([1,\infty)\), contradicting \(0<p<1\). Thus the orbit visits both the interior and exterior of \([0,1]\) and crosses its boundary at least twice.

## Verification
The accompanying dependency-free checker uses exact sparse-polynomial arithmetic over rational coefficients in the symbolic parameters \(a\) and \(b\). It verifies
\[
LH_1=ax^2+bx,
\]
\[
LH_2=b^2z(z-1)-(ax+bz)^2,
\]
the coordinate and \(x^2\) generator identities, and both equilibrium substitutions.

The stored checker output is `VERIFY_OK`. The conditional-expectation statement is proved analytically from arbitrary antiderivative test functions and is not inferred from finite sampling.

## Relationship to prior work
Sprott's primary-author parameter survey gives exactly the generalized Case G normalization above, reports the canonical chaotic parameters \(a=0.4\), \(b=1\), and numerically partitions the parameter plane into stable, periodic, chaotic, and unbounded regions.

A full-text 2021 Sprott G paper reproduces the canonical equations and studies phase portraits, Lyapunov exponents, fractional-order hyperchaos, and multiscroll modifications. Its searchable text contains no occurrence of “invariant” or “variance”; the paper's stated focus is numerical and circuit/application-oriented rather than an invariant-measure theorem.

Dimitrova and Yordanov's 2001 statistics paper studies the Sprott family through approximate second-order two-point functions and power spectra. Its accessible material does not state the exact conditional regression, barycenter segment, variance parabola, or the two slab barriers proved here. Panchev's 2004 paper is a plausible analytical comparison because it treats all nineteen Sprott flows and discusses asymptotic reformulations and statistical treatment; only metadata and abstract-level material were accessible in this run, so no whole-document noncoverage claim is made for it.

Targeted searches for Sprott G invariant measures, stationary moment laws, conditional expectations, barycenter/variance identities, and slab barriers returned no statement implying the theorem. Published semantic-database matches with similar invariant-measure geometry concern different vector fields.

## Limitations
The theorem concerns compactly supported invariant probability measures. It does not classify unbounded trajectories or prove existence of chaotic attractors in a given parameter region.

The periodic crossing statement gives a universal geometric obstruction but no least-period lower bound. For general invariant measures, the theorem forces both sides of the \(x\)-slab, while the \(z\)-slab interior/exterior crossing conclusion uses connectedness of a periodic orbit and is not asserted for arbitrary disconnected invariant supports.

The 1994 publisher record and Sprott's public technical note were inspected for the foundational source and normalization. The 2021 Sprott G article was inspected in full. The 2001 statistics paper was available through abstract and partial public text, and the 2004 analytical Sprott paper only through metadata/abstract-level material. A differently phrased or unindexed older identity therefore remains a bibliographic risk.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note, 2013, https://sprott.physics.wisc.edu/technote/regions.htm.
3. K. Altun, “Generation of Multi Scroll Attractor with Trigonometric Function in Fractional-Order Hyperchaotic Oscillators,” Journal of the Institute of Science and Technology 11(4), 2673–2681 (2021), DOI 10.21597/jist.969382.
4. E. S. Dimitrova and O. I. Yordanov, “Statistics of Some Low-Dimensional Chaotic Flows,” International Journal of Bifurcation and Chaos 11, 2675–2682 (2001), DOI 10.1142/S0218127401003735.
5. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21, 721–728 (2004), DOI 10.1016/j.chaos.2003.12.054.
