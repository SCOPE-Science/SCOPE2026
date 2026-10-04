# Compact-recurrence phase boundary and strict period floor in the generalized Sprott Q flow

## Finding
Consider the generalized Sprott Q flow
\[
\dot x=-z,\qquad \dot y=x-y,\qquad \dot z=ax+y^2+bz,
\]
with \(a>0\) and \(b\in\mathbb R\). Every compactly supported invariant probability measure \(\mu\) satisfies the two exact stationary identities
\[
\int y(y+a)\,d\mu=0,
\]
and
\[
\int (y-x-z)^2\,d\mu=(a-b)\int (x-y)^2\,d\mu.
\]
Consequently, if \(a\le b\), every compactly supported invariant probability measure is a convex combination of the two equilibrium atoms at \((0,0,0)\) and \((-a,-a,0)\). Thus there is no non-equilibrium compact recurrent statistical state in that parameter half-space.

If \(a>b\), every compact invariant probability measure not supported on the two equilibria assigns positive mass both to the open slab \(-a<y<0\) and to its strict exterior \(y<-a\) or \(y>0\). In particular, every nonconstant periodic orbit enters the open slab and leaves the closed slab \(-a\le y\le0\). Its least period \(P\) obeys the strict universal bound
\[
P>\frac{2\pi}{\sqrt{a-b}}.
\]
For the canonical Sprott Q parameters \(a=3.1\) and \(b=0.5\), this gives
\[
P>\frac{2\pi}{\sqrt{2.6}}\approx 3.8966661098.
\]

## Assumptions and scope
The claim concerns compactly supported invariant Borel probability measures of the smooth polynomial flow. Compact support guarantees that the generator identity \(\int L\phi\,d\mu=0\) is legitimate for every polynomial \(\phi\) used below. The periodic-orbit statement refers to a nonconstant classical periodic solution and its least positive period.

The source normalization is the two-parameter Sprott Q family recorded by Sprott: \(\dot x=-z\), \(\dot y=x-y\), \(\dot z=ax+y^2+bz\), with the canonical chaotic example \(a=3.1\), \(b=0.5\). The result does not assert existence of non-equilibrium compact recurrence for every \(a>b\); it gives necessary structure whenever such recurrence exists.

## Proof
Let \(L\) denote the Lie derivative along the vector field and set
\[
w=x-y=\dot y,\qquad v=Lw=y-x-z=\ddot y.
\]
First define
\[
K=z+bx-ay.
\]
A direct calculation gives
\[
LK=y(y+a).
\]
Invariant averaging therefore yields
\[
\int y(y+a)\,d\mu=0.
\]
If \(m=\int y\,d\mu\), then
\[
\operatorname{Var}_\mu(y)=-m(a+m),
\]
so \(-a\le m\le0\). Equivalently,
\[
\int\left(y+\frac a2\right)^2d\mu=\frac{a^2}{4}.
\]
The endpoint cases are rigid: \(m=0\) or \(m=-a\) forces zero variance, and invariance of the support then forces the corresponding equilibrium \((0,0,0)\) or \((-a,-a,0)\).

For the second identity define
\[
H=wv+\frac{1-b}{2}w^2+\frac a2y^2+\frac13y^3.
\]
Exact differentiation gives
\[
LH=v^2-(a-b)w^2.
\]
Hence every compact invariant probability measure satisfies
\[
\int v^2\,d\mu=(a-b)\int w^2\,d\mu,
\]
which is the stated derivative-energy balance.

If \(a<b\), the left side is nonnegative while the right side is nonpositive, so both integrals vanish. Thus \(w=v=0\) on the support. If \(a=b\), the identity gives \(v=0\) on the support; applying invariance to \(yw\), for which \(L(yw)=w^2+yv\), gives \(w=0\) as well. In either case \(w=v=0\) implies \(x=y\) and \(z=0\) on the support. Invariance of that support requires \(\dot z=y(y+a)=0\), leaving only the two equilibria. This proves the compact-recurrence obstruction for \(a\le b\).

Now suppose \(a>b\). The function \(h(y)=y(y+a)\) is strictly negative for \(-a<y<0\), strictly positive for \(y<-a\) or \(y>0\), and vanishes only at \(y=-a,0\). If an invariant measure were supported entirely on the zero set of \(h\), support invariance would again reduce it to the two equilibria. Therefore any other invariant measure has positive mass where \(h\ne0\). Since its mean \(\int h\,d\mu\) is exactly zero, it must assign positive mass to both signs of \(h\), proving the slab-excursion statement.

For a nonconstant periodic orbit of least period \(P\), the derivative \(w=\dot y\) has zero mean and is not identically zero. The balance law becomes
\[
\int_0^P \dot w^2\,dt=(a-b)\int_0^P w^2\,dt.
\]
Wirtinger's inequality for zero-mean \(P\)-periodic functions gives
\[
\int_0^P \dot w^2\,dt\ge \left(\frac{2\pi}{P}\right)^2\int_0^P w^2\,dt,
\]
so \(P\ge2\pi/\sqrt{a-b}\).

The bound is strict. Eliminating \(x\) and \(z\) gives the scalar equation
\[
\dddot y+(1-b)\ddot y+(a-b)\dot y+ay+y^2=0.
\]
Equality in Wirtinger's inequality would make \(w=\dot y\) a pure first harmonic with angular frequency \(\sqrt{a-b}\), so \(\dddot y+(a-b)\dot y=0\). The remaining equation
\[
(1-b)\ddot y+ay+y^2=0
\]
would then contain a nonzero second harmonic coming from \(y^2\), while its other terms contain only a constant and first harmonic. This is impossible unless the harmonic amplitude is zero, contradicting nonconstancy. Hence \(P>2\pi/\sqrt{a-b}\).

## Verification
The accompanying dependency-free checker represents multivariate polynomials with exact rational coefficients and replays the identities
\[
L(z+bx-ay)=y(y+a),
\]
\[
LH=(y-x-z)^2-(a-b)(x-y)^2,
\]
and the eliminated scalar equation. It also checks the two equilibrium substitutions. Its expected and reproduced output is `VERIFY_OK`.

The canonical parameter value gives \(2\pi/\sqrt{3.1-0.5}\approx3.8966661098\).

## Relationship to prior work
Sprott's 1994 paper introduced the nineteen simple quadratic chaotic flows and reported their critical points, Lyapunov exponents, and fractal dimensions. Sprott's later parameter-space note records the exact two-parameter Q normalization used here and numerically maps stable, periodic, chaotic, and unbounded regions. These sources establish the object and its standard parameterization, but the inspected material does not state the stationary coboundaries, the exact threshold \(a=b\) for non-equilibrium compact invariant measures, or the strict period floor proved here.

Later same-object work includes generalized bidirectional synchronization applied to Sprott N and Sprott Q, and a fractional-order Sprott Q study focused on fractional dynamics, synchronization, and secure communication. The accessible statements of those works do not imply the present invariant-measure identities or period theorem. One synchronization paper was not available in full text during the comparison, so no whole-document noncoverage claim is made for it.

## Limitations
The result is a necessary-structure theorem, not a classification of all dynamics for \(a>b\). It does not prove existence, uniqueness, stability, or chaos of any non-equilibrium invariant set. The strict period floor applies only to nonconstant periodic orbits. The originality comparison is bounded by the sources actually inspected; the inaccessible full text of one same-object synchronization paper and potentially unindexed older literature remain bibliographic risks.

## References
1. J. C. Sprott, “Some simple chaotic flows,” *Physical Review E* 50, R647–R650 (1994), DOI: 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” public technical note, exact two-parameter Cases F–S including Case Q, https://sprott.physics.wisc.edu/technote/regions.htm.
3. J. C. Sprott, “Simple Chaotic Flow GIF Animations,” canonical Case Q equations and reference to the 1994 paper, https://sprott.physics.wisc.edu/simplest.htm.
4. M. Jana, M. Islam, and N. Islam, “Dynamics of generalized bidirectional synchronization,” *International Journal of Dynamics and Control* 4, 466–480 (2016), DOI: 10.1007/s40435-015-0162-5.
5. A. Al Themairi, T. M. Abed-Elhameed, A. A. Farghaly, and H. Liu, “Tracking Control Method for Double Compound-Combination Synchronization of Fractional Chaotic Systems and Its Application in Secure Communication,” *Mathematical Problems in Engineering* 2022, 5301689, DOI: 10.1155/2022/5301689.
