# A sharp global recurrence threshold and stationary defect law for the Qi chaotic system
## Finding
Consider the Qi system
\[
\dot x=a(y-x)+yz,\qquad
\dot y=cx-y-xz,\qquad
\dot z=xy-bz,
\]
with
\[
0<a<1,\qquad b>0,\qquad c>0.
\]
Set
\[
c_*=2\sqrt a-a.
\]

Every compactly supported invariant probability measure \(\mu\) satisfies the conditional stationary law
\[
\mathbb E_\mu[xy\mid z]=bz
\]
and the exact stationary defect
\[
\mathbb E_\mu[(\sqrt a\,x-y)^2]
=
b(c-c_*)\,\mathbb E_\mu[z].
\]

This identity makes the equilibrium saddle-node boundary into an exact global recurrence threshold.

If
\[
c<c_*,
\]
then every trajectory converges to the origin. Consequently \(\delta_0\) is the only compactly supported invariant probability measure.

If
\[
c=c_*,
\]
then every compactly supported invariant probability measure is a convex mixture of the three equilibrium atoms
\[
O=(0,0,0)
\]
and
\[
E_\pm=
\left(
\pm\sqrt{b(1-\sqrt a)},
\pm\sqrt{ab(1-\sqrt a)},
\sqrt a(1-\sqrt a)
\right).
\]

If
\[
c>c_*,
\]
then nonzero equilibria exist. Moreover, every compactly supported invariant probability measure other than \(\delta_0\) satisfies
\[
\mathbb E_\mu[z]>0
\]
and
\[
\mathbb E_\mu[(\sqrt a\,x-y)^2]>0.
\]
Thus \(c_*\) is the exact threshold for existence of a non-origin compact stationary state.

## Assumptions and scope
The theorem concerns Borel probability measures invariant under the Qi flow and supported on compact subsets of \(\mathbb R^3\). The restriction \(0<a<1\) is essential for the sharp threshold statement because it makes
\[
c_*=2\sqrt a-a>0
\]
and ensures that the double nonzero equilibrium at threshold is real.

The source literature studies the Qi system for broad positive parameter ranges, including the classical strongly chaotic regime. The theorem isolates a different, analytically tractable low-\(a\) transition where the nonzero-equilibrium discriminant vanishes.

The first public source date is taken as 2005-07-15, the verified issue date of Physica A volume 352, issues 2–4, which contains the original Qi paper. No earlier public posting date for that paper was verified in the inspected sources.

## Proof
Let \(L\) denote the generator of the flow. For any compactly supported invariant probability measure \(\mu\),
\[
\int L H\,d\mu=0
\]
for every continuously differentiable test function \(H\).

First take an arbitrary continuous function \(\psi\) on the compact \(z\)-range and choose an antiderivative \(K\) with \(K'(z)=\psi(z)\). Then
\[
LK=\psi(z)(xy-bz).
\]
Hence
\[
\mathbb E_\mu[xy-bz\mid z]=0,
\]
which gives
\[
\mathbb E_\mu[xy\mid z]=bz.
\]
In particular,
\[
\mathbb E_\mu[xy]=b\mathbb E_\mu[z].
\]

Now put
\[
H=\frac12(x^2+y^2).
\]
Direct differentiation gives
\[
LH=(a+c)xy-a x^2-y^2.
\]
Stationarity therefore yields
\[
a\mathbb E_\mu[x^2]+\mathbb E_\mu[y^2]
=(a+c)\mathbb E_\mu[xy].
\]
Subtracting \(2\sqrt a\,\mathbb E_\mu[xy]\) from both sides gives
\[
\mathbb E_\mu[(\sqrt a\,x-y)^2]
=(a+c-2\sqrt a)\mathbb E_\mu[xy].
\]
Since
\[
a+c-2\sqrt a=c-c_*
\]
and \(\mathbb E_\mu[xy]=b\mathbb E_\mu[z]\), this is exactly
\[
\mathbb E_\mu[(\sqrt a\,x-y)^2]
=b(c-c_*)\mathbb E_\mu[z].
\]

For the subthreshold dynamics, write
\[
Q(x,y)=a x^2+y^2-(a+c)xy.
\]
If \(c<c_*\), then
\[
(a+c)^2<4a,
\]
so \(Q\) is positive definite and
\[
\dot H=-Q(x,y)\le-\kappa(x^2+y^2)
\]
for some \(\kappa>0\). Hence \(x\) and \(y\) remain bounded and tend to zero. The scalar equation
\[
\dot z+bz=xy
\]
then shows that \(z\) remains bounded and tends to zero. Thus every trajectory converges to the origin. The only compactly supported invariant probability measure is therefore \(\delta_0\).

At threshold, write
\[
s=\sqrt a,
\qquad
c_*=2s-s^2.
\]
The defect identity becomes
\[
\mathbb E_\mu[(sx-y)^2]=0,
\]
so the compact invariant support lies in the plane
\[
y=sx.
\]
Let
\[
d=y-sx.
\]
On that plane, direct substitution gives
\[
\dot d=(1+s^2)x\bigl(s(1-s)-z\bigr).
\]
A point of a compact invariant support with \(x=0\) also has \(y=0\); its complete orbit on the \(z\)-axis is bounded in both time directions only when \(z=0\). If \(x\ne0\), tangency to the plane forces
\[
z=s(1-s).
\]
Along the complete support trajectory this remains true locally, so \(\dot z=0\). Therefore
\[
sx^2-bs(1-s)=0,
\]
which gives
\[
x^2=b(1-s).
\]
These are exactly \(E_+\) and \(E_-\). Thus every compact invariant probability measure at threshold is a convex mixture of the three equilibrium atoms.

For sharpness above threshold, a nonzero equilibrium must satisfy
\[
y=(c-z)x
\]
and
\[
(c-z)(a+z)=a.
\]
Hence its height solves
\[
z^2-(c-a)z-a(c-1)=0,
\]
whose discriminant is
\[
\Delta=(a+c)^2-4a.
\]
At \(c=c_*\), \(\Delta=0\). For every \(c>c_*\), the positive root exists and obeys \(c-z>0\), so
\[
x^2=\frac{bz}{c-z}>0.
\]
Thus nonzero equilibrium atoms exist for every \(c>c_*\).

Finally, for \(c>c_*\), the defect coefficient is positive. If the defect vanished for an invariant measure, its support would again lie in \(y=\sqrt a\,x\). The tangency calculation above, together with compact two-sided invariance of the support, forces either the origin or \(c=c_*\). Since here \(c>c_*\), a non-origin invariant measure has strictly positive defect, and consequently
\[
\mathbb E_\mu[z]>0.
\]

## Verification
The accompanying exact-arithmetic checker verifies the critical generator cancellation, the threshold tangency identity, the equilibrium discriminant, and a rational threshold instance.

In particular, it checks the cancellation of the two cubic terms in
\[
L\left(\frac12(x^2+y^2)\right)
=(a+c)xy-a x^2-y^2,
\]
and, after substituting \(a=s^2\) and \(c=2s-s^2\), verifies
\[
\left.\frac{d}{dt}(y-sx)\right|_{y=sx}
=(1+s^2)x\bigl(s(1-s)-z\bigr).
\]

It also checks the threshold example
\[
a=\frac14,\qquad b=2,\qquad c_*=\frac34,
\]
for which
\[
E_\pm=(\pm1,\pm\tfrac12,\tfrac14).
\]
The stored checker output is `VERIFY_OK`.

## Relationship to prior work
The original 2005 paper introduced the three-dimensional Qi system and analyzed its dynamics through Lyapunov spectra and bifurcation diagrams.

The 2009 full same-object bifurcation analysis writes exactly the system used here, gives the equilibrium formulas, and develops pitchfork and Hopf bifurcations with center-manifold methods. In particular, it studies the local pitchfork at \(c=1\) under a different parameter regime. Those local bifurcation results do not imply the present global threshold at
\[
c=2\sqrt a-a
\]
for \(0<a<1\), nor the invariant-measure defect law.

The later energy-cycle analysis gives a full mechanical decomposition of the Qi system, classifies three-versus-five equilibrium regimes, derives a Casimir-energy derivative, and proves global stability for a particular modified torque balance. It therefore supplies important adjacent energy and equilibrium information. The result here uses a different quadratic observable, produces a conditional stationary law and an exact defect, and identifies the equilibrium discriminant as a sharp global convergence and compact-stationary-recurrence boundary in the low-\(a\) family.

Targeted semantic searches for the Qi system together with invariant-measure, stationary-moment, equilibrium-discriminant, RMS-defect, and compact-recurrence formulations found no same-object statement implying this theorem. The closest indexed result with the same logical shape concerns the distinct Rössler flow.

## Limitations
The sharp global threshold theorem is restricted to \(0<a<1\). It does not claim the same threshold in the classical Qi parameter regime with large \(a\).

For \(c>c_*\), the theorem guarantees non-origin compact stationary states because nonzero equilibria exist, but it does not assert existence of a chaotic attractor or non-equilibrium recurrent measure for every parameter value.

The original 2005 paper was inspected through bibliographic and abstract material rather than full text; complete text was unavailable in the inspected public sources. The 2009 same-object paper and the 2017 energy-cycle paper were inspected in substantially fuller form. A differently phrased or unindexed older stationary identity could remain undiscovered.

## References
1. G. Qi, G. Chen, S. Du, Z. Chen, and Z. Yuan, “Analysis of a new chaotic system,” Physica A 352(2–4), 295–308 (2005), DOI 10.1016/j.physa.2004.12.040.
2. Y. Sun, G. Qi, B. J. Van Wyk, and Z. Wang, “Analysis of the Qi three dimensional chaotic system,” Far East Journal of Dynamical Systems 11(1), 77–94 (2009), DOI 10.17654/0972111809007.
3. G. Qi and J. Zhang, “Energy cycle and bound of Qi chaotic system,” open repository full text, 2017.
