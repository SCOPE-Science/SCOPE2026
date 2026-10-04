# Compact-recurrence trichotomy and strict period floor in the generalized Sprott J flow
## Finding
Consider
\[
\dot x=az,\qquad
\dot y=-by+z,\qquad
\dot z=-x+y+y^2,
\]
with \(b>0\) and \(a\in\mathbb R\).

If \(a<0\), the only compactly supported invariant probability measure is the origin atom.

If \(a=0\), the compactly supported invariant probability measures are exactly the compactly supported probabilities on
\[
\mathcal E_0=
\left\{
\left(s+s^2,s,bs\right):s\in\mathbb R
\right\}.
\]

If \(a>0\), every compactly supported invariant probability measure \(\mu\) satisfies
\[
\mathbb E_\mu[(z-by)^2]
=
a\,\mathbb E_\mu[y^2],
\]
equivalently
\[
\mathbb E_\mu[(\dot y)^2]
=
a\,\mathbb E_\mu[y^2],
\]
and
\[
\mathbb E_\mu[y^2(y+1)]=0.
\]
Every non-origin such measure assigns positive mass to both
\[
y>0
\qquad\text{and}\qquad
y<-1.
\]

Every nonconstant periodic orbit for \(a>0\), with least period \(P\), obeys
\[
P>\frac{2\pi}{\sqrt a}.
\]
It crosses each of \(y=0\) and \(y=-1\) at least twice per least period. At the canonical parameters \(a=b=2\),
\[
P>\sqrt2\,\pi
=4.442882938158366\ldots.
\]

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the flow and supported on compact subsets of \(\mathbb R^3\). Compact support makes all polynomial generator identities below integrable.

The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

The normalization is Sprott's generalized Case J normalization. The primary-author parameter survey displays chaos at \(a=2\), \(b=2\).

## Proof
Let \(L\) be the flow generator and put
\[
q=z-by=\dot y.
\]
A direct calculation gives
\[
L F=q^2-a y^2,
\]
where
\[
F
=
yz-\frac{z^2+2xy}{2b}
+\frac{a-b^2+1}{2b}y^2
+\frac{1}{3b}y^3.
\]
Thus every compact invariant measure obeys
\[
\mathbb E[q^2]=a\,\mathbb E[y^2].
\]

If \(a<0\), both sides must vanish. Hence \(y=q=z=0\) almost surely. Since
\[
L(xz)=az^2-x^2+xy+xy^2,
\]
stationarity then gives \(\mathbb E[x^2]=0\), so the measure is the origin atom.

If \(a=0\), the energy identity gives \(q=0\) almost surely. The support of an invariant measure for a continuous flow is invariant, so every support trajectory remains in \(q=0\). There
\[
Lq=-x+y+y^2-bq=-x+y+y^2,
\]
hence invariance forces
\[
x=y+y^2,\qquad z=by.
\]
All three derivatives then vanish, so the support lies in \(\mathcal E_0\). Conversely every compactly supported probability on \(\mathcal E_0\) is invariant.

Now assume \(a>0\). A non-origin invariant measure has \(\mathbb E[y^2]>0\), because otherwise the energy identity and \(L(xz)\) again force the origin. From
\[
Lx=az,\qquad Ly=z-by
\]
we get
\[
\mathbb E[z]=\mathbb E[y]=0.
\]
Therefore both signs of \(y\) have positive mass.

For \(a>0\), another exact coboundary is
\[
L G=y^2(y+1),
\]
where
\[
G
=
\frac{z^2-y^2}{2b}
-\frac{y^3}{3b}
+\frac{x^2}{2ab}.
\]
Hence
\[
\mathbb E[y^2(y+1)]=0.
\]
The contribution on \(y>0\) is strictly positive, while the integrand is negative only for \(y<-1\). Therefore every non-origin compact invariant measure has positive mass in \(y<-1\).

For a nonconstant periodic orbit, normalized orbit measure gives
\[
\int_0^P y(t)\,dt=0,\qquad
\int_0^P \dot y(t)^2\,dt
=
a\int_0^P y(t)^2\,dt.
\]
Wirtinger's inequality yields
\[
P\ge\frac{2\pi}{\sqrt a}.
\]
Equality would make \(y\) a nonzero first harmonic:
\[
y''=-ay,\qquad y'''=-ay'.
\]
Eliminating \(x,z\) from the system gives
\[
y'''+by''+(a-1)y'+ab\,y-2yy'=0.
\]
The equality conditions reduce this to
\[
(1+2y)y'=0,
\]
which is impossible for a nonconstant first harmonic. Thus
\[
P>\frac{2\pi}{\sqrt a}.
\]
Since the orbit takes values above \(0\) and below \(-1\), continuity forces at least two crossings of each boundary in a least period.

## Verification
The accompanying checker verifies exactly
\[
L F=(z-by)^2-a y^2,
\]
\[
L G=y^2(y+1),
\]
\[
L(xz)=az^2-x^2+xy+xy^2,
\]
the eliminated jerk equation
\[
y'''+by''+(a-1)y'+ab\,y-2yy'=0,
\]
and the equality-case reduction. Its stored output is `VERIFY_OK`.

The classification and period proofs are analytic deductions from these identities and standard invariance and Wirtinger facts, not finite experiments.

## Relationship to prior work
Sprott's primary-author parameter survey gives exactly the displayed Case J equations and the canonical chaotic point \(a=b=2\).

The full text of Islam, Islam, and Nikolov studies exactly this generalized Sprott J system with positive parameters. It proves instability of the origin and develops adaptive control, parameter estimation, and synchronization. Its conclusion explicitly identifies control and synchronization as the focus. The inspected text does not state the compact-invariant-measure trichotomy, the exact derivative-energy and cubic balances, the forced \(y<-1\) excursion, or the strict least-period floor.

The 2004 analytical Sprott-flow paper is a plausible broader same-family source. Its complete text was not inspected, so it remains an explicit bibliographic risk rather than being treated as noncovering.

Targeted searches using the system name, parameter aliases, invariant-measure language, exact energy and cubic-moment formulations, amplitude language, and the proposed period bound returned no statement implying this theorem. The closest indexed results concern analogous balance laws for distinct polynomial flows.

## Limitations
The theorem concerns compactly supported invariant probability measures and periodic orbits. It does not classify unbounded trajectories or prove that nontrivial recurrence exists for every \(a>0\).

The period floor is strict whenever a nonconstant periodic orbit exists; no claim is made that it is approached.

The 1994 foundational paper was used through its publisher record and primary-author Case J listing. The complete 2004 analytical Sprott-flow paper was not inspected. A differently phrased or unindexed older theorem could therefore escape the targeted comparison.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note, 2013, https://sprott.physics.wisc.edu/technote/regions.htm.
3. M. Islam, N. Islam, and S. Nikolov, “Adaptive Control and Synchronization of Sprott J System With Estimation Of Fully Unknown Parameters,” Journal of Theoretical and Applied Mechanics 45(2), 45–58 (2015), DOI 10.1515/jtam-2015-0010.
4. S. Panchev, “Analytical properties of the Sprott's chaotic flows,” Chaos, Solitons & Fractals 21 (2004), DOI 10.1016/j.chaos.2003.12.054.
