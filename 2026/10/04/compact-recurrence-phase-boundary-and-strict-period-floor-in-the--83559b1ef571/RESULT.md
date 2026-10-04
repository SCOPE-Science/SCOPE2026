# Compact-recurrence phase boundary and strict period floor in the generalized Sprott R flow
## Finding
Consider the generalized Sprott R system
\[
\dot x=a-y,\qquad \dot y=b+z,\qquad \dot z=xy-z,
\]
with real parameters \(a,b\).

For \(a<0\), the only compactly supported invariant probability measure is the Dirac measure at
\[
\left(-\frac ba,a,-b\right).
\]
For \(a=0\) and \(b\ne0\), no compactly supported invariant probability measure exists. For \(a=b=0\), the compactly supported invariant probability measures are exactly the compactly supported probabilities on
\[
\{(x,0,0):x\in\mathbb R\}.
\]

For \(a>0\), every compactly supported invariant probability measure \(\mu\) has barycenter
\[
\left(\mathbb E_\mu[x],\mathbb E_\mu[y],\mathbb E_\mu[z]\right)
=\left(-\frac ba,a,-b\right)
\]
and satisfies
\[
\operatorname{Var}_\mu(y)=a\,\operatorname{Var}_\mu(x).
\]
If \(\mu\) is not the equilibrium atom, then it assigns positive mass to both sides of \(x=-b/a\) and to both sides of \(y=a\). Its centered \(z\)-coordinate \(z+b\) is nonconstant with zero mean, hence both signs occur on its support.

Every nonconstant periodic orbit for \(a>0\), with least period \(P\), obeys
\[
P>\frac{2\pi}{\sqrt a}.
\]
It crosses each of
\[
x=-\frac ba,\qquad y=a,\qquad z=-b
\]
at least twice per least period. For the standard chaotic parameters \(a=0.9\), \(b=0.4\),
\[
P>6.623058843864068\ldots.
\]

## Assumptions and scope
The measure statements concern Borel probability measures invariant under the flow and supported on a compact subset of \(\mathbb R^3\). Compact support makes the polynomial generator identities below integrable. The periodic-orbit statement concerns a nonconstant classical periodic solution and its least positive period.

The system normalization is the two-parameter Case R normalization recorded by J. C. Sprott, whose standard chaotic example is \(a=0.9\), \(b=0.4\). The archive date is the publication date of the original Sprott-flow paper, 1994-08-01.

## Proof
For an invariant probability measure, the integral of the Lie derivative of each polynomial below is zero. The coordinate identities give
\[
\mathbb E[y]=a,\qquad
\mathbb E[z]=-b,\qquad
\mathbb E[xy]=-b.
\]
When \(a\ne0\), stationarity of \(x^2\) gives
\[
0=\mathbb E[2x(a-y)]
=2a\,\mathbb E[x]-2\mathbb E[xy],
\]
hence
\[
\mathbb E[x]=-\frac ba.
\]

For \(a\ne0\), set
\[
X=x+\frac ba,\qquad Y=y-a,\qquad Z=z+b,\qquad c=\frac ba.
\]
Then
\[
\dot X=-Y,\qquad \dot Y=Z,\qquad \dot Z=XY+aX-cY-Z.
\]
Define
\[
H=-XZ-\frac12Y^2-XY+\frac c2X^2-\frac13X^3.
\]
Exact differentiation yields
\[
\dot H=Y^2-aX^2.
\]
Therefore every compact invariant measure satisfies
\[
\mathbb E[Y^2]=a\,\mathbb E[X^2].
\]

If \(a<0\), nonnegativity forces \(X=Y=0\) almost surely. Stationarity of \(YZ\) then gives \(\mathbb E[Z^2]=0\), so only the equilibrium atom remains.

If \(a>0\), the centered means vanish and the displayed identity is exactly
\[
\operatorname{Var}(y)=a\,\operatorname{Var}(x).
\]
If one variance vanishes, both \(X\) and \(Y\) vanish almost surely, and stationarity of \(YZ\) again forces \(Z=0\), giving the equilibrium atom. Thus every other invariant measure has nonzero, zero-mean \(X\) and \(Y\), so each takes both signs with positive measure.

If \(Z=0\) almost surely, invariance of the support forces the vector field to be tangent to the hyperplane \(Z=0\). Along a compact complete trajectory there, \(\dot Y=0\), so \(Y\) is constant; \(\dot X=-Y\) and compactness force \(Y=0\). Tangency then gives \(\dot Z=aX=0\), so \(X=0\) for \(a>0\). Hence a non-equilibrium compact invariant measure has nonconstant, zero-mean \(Z\), which also takes both signs.

For \(a=0\), stationarity yields
\[
\mathbb E[y]=0,\qquad \mathbb E[z]=-b,\qquad \mathbb E[xy]=-b.
\]
But stationarity of \(x^2\) gives
\[
0=-2\mathbb E[xy]=2b.
\]
Thus \(b\ne0\) excludes compact invariant probability measures. If \(a=b=0\), the polynomial
\[
H=-xz-\frac12y^2-xy-\frac13x^3
\]
satisfies
\[
\dot H=y^2.
\]
Hence an invariant measure has \(y=0\) almost surely; stationarity of \(yz\) then gives \(z=0\) almost surely. Conversely, every compactly supported probability on \(y=z=0\) is invariant because that line consists entirely of equilibria.

For a nonconstant periodic orbit with \(a>0\), its orbit measure gives
\[
\int_0^P X(t)\,dt=0,\qquad
\int_0^P \dot X(t)^2\,dt
=a\int_0^P X(t)^2\,dt.
\]
Wirtinger's inequality yields \(P\ge2\pi/\sqrt a\). Equality would make \(X\) a nonzero first harmonic satisfying
\[
X''=-aX,\qquad X'''=-aX'.
\]
Eliminating \(Y,Z\) gives
\[
X'''+X''+cX'+aX-XX'=0.
\]
Under equality this reduces to
\[
(c-a-X)X'=0.
\]
A nonconstant first harmonic has \(X'\ne0\) on open intervals, which would force \(X\) to be constant there, a contradiction. Thus the period inequality is strict.

Each centered coordinate \(X,Y,Z\) is then a continuous, nonconstant periodic function of zero mean, so it assumes both signs. Periodicity forces at least two zeros per least period for each coordinate.

## Verification
The accompanying checker uses exact rational-coefficient sparse-polynomial arithmetic. It verifies
\[
L H=Y^2-aX^2
\]
for the centered vector field and verifies
\[
X'''+X''+cX'+aX-XX'=0.
\]
It also checks the coordinate and \(x^2\) generator identities used for the barycenter. The stored checker output is `VERIFY_OK`.

The remaining deductions use the standard invariant-measure identity \(\int Lf\,d\mu=0\), support invariance for a continuous flow, and the classical equality case of Wirtinger's inequality.

## Relationship to prior work
Sprott's two-parameter Case R page gives exactly
\[
\dot x=a-y,\qquad \dot y=b+z,\qquad \dot z=xy-z,
\]
and maps parameter regions numerically as stable equilibria, periodic cycles, chaotic attractors, or unbounded behavior. The present theorem gives an analytic parameter boundary: compact non-equilibrium recurrence is impossible for \(a<0\), no compact invariant probability measure exists for \(a=0,b\ne0\), while for \(a>0\) recurrent statistics obey an exact variance law and periodic cycles obey a strict universal period floor.

Erjaee and Alnasr explicitly treat Sprott R at \(a=0.9\), \(b=0.4\) in a study of coupled integer- and fractional-order phase synchronization. That problem does not imply the uncoupled invariant-measure identities or the least-period lower bound proved here.

Targeted searches for same-object compact invariant measures, stationary variance identities, recurrence obstructions, and period lower bounds returned no statement implying the theorem above. The closest indexed statements concerned analogous balance laws for different vector fields.

## Limitations
The theorem concerns compact invariant measures and periodic orbits; it does not classify unbounded trajectories or prove existence of chaotic attractors for \(a>0\). The period floor is strict but is not asserted to be approached. Targeted searches cannot exclude a differently phrased or unindexed older theorem. The publisher page for the 1994 source supplied its abstract and exact publication date, but no whole-document noncoverage claim is made from that abstract.

## References
1. J. C. Sprott, “Some simple chaotic flows,” Physical Review E 50, R647–R650 (1994), DOI 10.1103/PhysRevE.50.R647. Published 1994-08-01.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note, 2013, https://sprott.physics.wisc.edu/technote/regions.htm.
3. G. H. Erjaee and M. Alnasr, “Phase Synchronization in Coupled Sprott Chaotic Systems Presented by Fractional Differential Equations,” Discrete Dynamics in Nature and Society, Article 753746, DOI 10.1155/2009/753746.
