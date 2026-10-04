# Exact compact-recurrence phase diagram and strict period floor in the generalized Sprott S flow
## Finding
Consider the generalized Sprott S system
\[
\dot x=-x-ay,\qquad
\dot y=x+z^2,\qquad
\dot z=b+x,
\]
with real parameters \(a,b\).

Its compactly supported invariant probability measures have the following exact phase diagram.

If \(b<0\), no compactly supported invariant probability measure exists.

If \(b=0\) and \(a\ne0\), the only compactly supported invariant probability measure is the origin atom. If \(a=b=0\), the compactly supported invariant probability measures are exactly the compactly supported probabilities on the equilibrium line
\[
\{(0,y,0):y\in\mathbb R\}.
\]

If \(b>0\) and \(a<0\), the compactly supported invariant probability measures are exactly the convex mixtures of the two equilibrium atoms
\[
e_\pm=
\left(-b,\frac ba,\pm\sqrt b\right).
\]
If \(b>0\) and \(a=0\), no compactly supported invariant probability measure exists.

For \(a>0\) and \(b>0\), every compactly supported invariant probability measure \(\mu\) satisfies
\[
\mathbb E_\mu[x]=-b,
\qquad
\mathbb E_\mu[z^2]=b,
\]
and the exact derivative-energy identity
\[
\mathbb E_\mu[(x+ay)^2]
=
a\,\mathbb E_\mu[(x+b)^2].
\]
Equivalently,
\[
z'=x+b,\qquad z''=-x-ay,
\]
so
\[
\mathbb E_\mu[(z'')^2]
=
a\,\mathbb E_\mu[(z')^2].
\]

The equality case \(z^2=b\) almost surely consists exactly of convex mixtures of \(e_+\) and \(e_-\). Hence every other compact invariant probability measure assigns positive mass to both
\[
|z|<\sqrt b
\qquad\text{and}\qquad
|z|>\sqrt b.
\]

Every nonconstant periodic orbit for \(a>0,b>0\), with least period \(P\), satisfies
\[
P>\frac{2\pi}{\sqrt a}.
\]
It crosses
\[
|z|=\sqrt b
\]
at least twice per least period. For the canonical Sprott S parameters \(a=4\), \(b=1\),
\[
P>\pi.
\]

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the flow and supported on compact subsets of \(\mathbb R^3\). Compact support makes the polynomial generator identities below integrable.

The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

The two-parameter normalization is the Case S normalization recorded by J. C. Sprott:
\[
\dot x=-x-ay,\qquad
\dot y=x+z^2,\qquad
\dot z=b+x.
\]
The primary-author parameter survey displays a chaotic example at \(a=4\), \(b=1\).

## Proof
Let \(L\) be the generator of the flow. Invariance gives
\[
\int Lh\,d\mu=0
\]
for every polynomial \(h\).

The coordinate identities are
\[
Lz=b+x,\qquad
Ly=x+z^2.
\]
Therefore
\[
\mathbb E[x]=-b,
\qquad
\mathbb E[z^2]=b.
\]
Since \(z^2\ge0\), \(b<0\) is impossible.

Suppose \(b=0\). Then \(z=0\) almost surely. Invariance of the support forces
\[
z'=x=0
\]
on the support. If \(a\ne0\), tangency of \(x=0\) gives
\[
x'=-ay=0,
\]
so \(y=0\) and only the origin remains. If \(a=0\), every point on \(x=z=0\) is an equilibrium, proving the stated equilibrium-line classification.

Now suppose \(a=0\). The identity
\[
Lx=-x
\]
gives \(\mathbb E[x]=0\). Combined with \(\mathbb E[x]=-b\), this forces \(b=0\). Thus no compact invariant probability measure exists when \(a=0,b>0\).

For the remaining regimes define
\[
v=x+b=z',
\qquad
w=-x-ay=z''.
\]
Set
\[
F
=
vw+\frac12v^2
+a\left(\frac13z^3-bz\right).
\]
A direct differentiation gives
\[
L F=w^2-a v^2.
\]
Hence every compactly supported invariant probability measure satisfies
\[
\mathbb E[w^2]=a\,\mathbb E[v^2].
\]

If \(a<0\), both nonnegative quantities must vanish. Thus \(v=w=0\) almost surely, so
\[
x=-b,\qquad y=\frac ba.
\]
If \(b>0\), support invariance then forces
\[
y'=x+z^2=-b+z^2=0,
\]
hence \(z=\pm\sqrt b\). Therefore the measure is a convex mixture of the two equilibrium atoms \(e_\pm\).

Assume now \(a>0,b>0\). We already know
\[
\mathbb E[z^2]=b.
\]
If \(z^2=b\) almost surely, support tangency gives
\[
L(z^2-b)=2z(b+x)=0.
\]
Since \(z\ne0\), this forces \(x=-b\). Tangency of \(x=-b\) gives
\[
x'=b-ay=0,
\]
so \(y=b/a\). Thus equality consists exactly of convex mixtures of \(e_+\) and \(e_-\).

If the measure is not such a mixture, \(z^2\) is not almost surely equal to its mean \(b\). Since
\[
\mathbb E[z^2-b]=0,
\]
both signs of \(z^2-b\) occur on sets of positive measure. This is exactly the claimed inside/outside excursion.

For a nonconstant periodic orbit, normalized orbit measure gives
\[
\int_0^P z''(t)^2\,dt
=
a\int_0^P z'(t)^2\,dt.
\]
The function \(z'\) is periodic and has zero mean. If it vanished identically, the orbit would be an equilibrium. Thus Wirtinger's inequality gives
\[
P\ge\frac{2\pi}{\sqrt a}.
\]

To exclude equality, eliminate \(x,y\). One obtains
\[
z'''+z''+a z'+a(z^2-b)=0.
\]
Equality in Wirtinger's inequality would make \(z'\) a nonzero first harmonic with
\[
z'''=-a z'.
\]
Substitution gives
\[
z''+a(z^2-b)=0.
\]
Differentiating and using \(z'''=-a z'\) yields
\[
a(2z-1)z'=0.
\]
A nonzero first harmonic \(z'\) is nonzero on open intervals; there the last identity would force \(z=1/2\), contradicting \(z'\ne0\). Hence
\[
P>\frac{2\pi}{\sqrt a}.
\]

A nonconstant periodic orbit is not an equilibrium mixture, so its orbit measure gives both signs of \(z^2-b\). Continuity on the periodic circle forces at least two zeros of \(z^2-b\) in a least period.

## Verification
The accompanying checker uses exact sparse-polynomial arithmetic over rational coefficients.

It verifies
\[
Lz=b+x,\qquad
Ly=x+z^2,
\]
and, with
\[
v=x+b,\qquad
w=-x-ay,
\]
the exact certificate
\[
L\left(
vw+\frac12v^2+a\left(\frac13z^3-bz\right)
\right)
=
w^2-a v^2.
\]
It also verifies
\[
z'''+z''+a z'+a(z^2-b)=0.
\]

The stored checker output is `VERIFY_OK`. The remaining steps are exact analytic deductions using support invariance and the classical equality case of Wirtinger's inequality.

## Relationship to prior work
Sprott's primary-author parameter survey gives exactly the two-parameter Case S equations above and maps stable, periodic, chaotic, and unbounded numerical regions; the canonical chaotic example is \(a=4,b=1\).

Erjaee and Alnasr study coupled Sprott-S systems in integer and fractional order. Their full text focuses on phase synchronization, its dependence on derivative order, and stability of the coupled error dynamics. It does not state the compact-invariant-measure phase diagram, the exact derivative-energy law, the equilibrium-shell excursion theorem, or the least-period lower bound proved here.

Panchev's analytical paper on the Sprott family is a plausible broader comparison and is indexed under MSC \(34C28\), among other dynamical classifications. Its complete text was not inspected here, so no whole-document noncoverage claim is made for that source.

Targeted published searches for Sprott S together with invariant measures, stationary \(z^2\) laws, recurrence phase boundaries, exact derivative-energy identities, equilibrium-shell excursions, and period bounds returned no statement implying the theorem above. The closest indexed results concern analogous balance and period phenomena in different vector fields.

## Limitations
The theorem concerns compactly supported invariant probability measures and periodic orbits. It does not classify unbounded trajectories or prove existence of nontrivial compact recurrence for every \(a>0,b>0\).

The strict period floor is universal when a nonconstant periodic orbit exists, but it is not asserted to be approached.

The 1994 foundational paper was inspected through its publisher record and primary-author Case S listing rather than by a line-by-line full-paper comparison. The full 2009 Sprott-S synchronization article was inspected. The complete 2004 analytical Sprott-flow article was not inspected and remains an explicit bibliographic risk.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note, 2013, https://sprott.physics.wisc.edu/technote/regions.htm.
3. G. H. Erjaee and M. Alnasr, “Phase Synchronization in Coupled Sprott Chaotic Systems Presented by Fractional Differential Equations,” Discrete Dynamics in Nature and Society, 2009, Article 753746, DOI 10.1155/2009/753746.
4. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21 (2004), DOI 10.1016/j.chaos.2003.12.054.
