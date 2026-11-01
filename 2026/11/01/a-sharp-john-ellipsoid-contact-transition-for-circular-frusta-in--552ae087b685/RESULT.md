# A sharp John-ellipsoid contact transition for circular frusta in all dimensions

## Finding
For every integer \(d\ge2\) and every positive pair of end radii \(R\ge r>0\), the maximum-volume inscribed ellipsoid of a right circular frustum has an explicit unique form. In axial coordinates \(-1\le z\le1\), put \(A=(R+r)/2\), \(s=(R-r)/(R+r)\), and
\[
K=\{(x,z)\in\mathbb R^{d-1}\times\mathbb R:-1\le z\le1,\ \|x\|_2\le A(1-sz)\}.
\]
The unique John ellipsoid is
\[
J=\left\{(x,z):\frac{\|x\|_2^2}{q}+\frac{(z-m)^2}{p}\le1\right\}
\]
with
\[
(m,p,q)=\begin{cases}
(0,1,Rr),&0\le s\le 1/d,\\
\left(\dfrac{1-ds}{s(d+1)},\left(1+\dfrac{1-ds}{s(d+1)}\right)^2,\dfrac{d-1}{d+1}R^2\right),&1/d<s<1.
\end{cases}
\]
The transition is exactly \(r/R=(d-1)/(d+1)\). Above this radius ratio, both end planes touch the ellipsoid; below it, only the larger-radius end plane touches. In the second regime its transverse squared semiaxis \(q=(d-1)R^2/(d+1)\) is independent of the smaller radius. The asserted novelty concerns this *inscribed* ellipsoid, not the enclosing ellipsoid of the frustum.

## Assumptions and scope
The axis length is arbitrary and positive. The given coordinate is obtained by an invertible affine change of the physical axial coordinate, taking the larger-radius base to \(z=-1\) and the smaller to \(z=1\). The physical axial center and semiaxis are obtained by rescaling \(m\) and \(\sqrt p\) by half the physical height. \(d=2\) is included; the transverse contact sphere then consists of two points. No claim is made for a zero smaller radius in the displayed parameter domain. The enclosing ellipsoid was already determined in the cited earlier work.

## Proof
**Containment.** For a rotationally symmetric ellipsoid \(E(m,p,q)\), containment between both end planes is equivalent to \(-1\le m-\sqrt p\) and \(m+\sqrt p\le1\). Its maximum of \(\|x\|_2+Asz\) equals
\[
As m+\sqrt{q+A^2s^2p}.
\]
Indeed, \(\|x\|_2\) is the maximum transverse scalar projection and the support function of an ellipsoid gives the displayed radical. Consequently the complete conical-side containment condition is
\[
As m+\sqrt{q+A^2s^2p}\le A.
\]
In the first regime, \(m=0\), \(p=1\), \(q=Rr=A^2(1-s^2)\), so the last left side equals \(A\) and both end constraints are equalities. In the second regime, the stated parameters satisfy \(m\in(-1,0)\), \(p=(1+m)^2\), and
\[
q=A^2(1-sm)^2-A^2s^2(1+m)^2=\frac{d-1}{d+1}R^2.
\]
Thus the conical-side inequality is an equality, the lower-end constraint is an equality, and the upper end constraint is strict. In both regimes the candidate lies inside \(K\).

**Contact certificate for the first regime.** Map the candidate to the Euclidean unit ball by \((x,z)\mapsto(x/\sqrt q,(z-m)/\sqrt p)\). The contact with the conical side is the uniform measure on the latitude sphere whose axial coordinate is \(s\), while the two end-plane poles have axial coordinates \(+1\) and \(-1\). Assign total mass
\[
w=\frac{d-1}{d(1-s^2)}
\]
to the latitude sphere, and masses
\[
w_+=\frac{1-w-ws}{2},\qquad w_-=\frac{1-w+ws}{2}
\]
to its upper and lower poles. The three masses are nonnegative precisely when \(s\le1/d\), and sum to one. Rotational symmetry makes every off-diagonal second moment vanish. The axial mean is \(ws+w_+-w_-=0\), axial second moment is \(ws^2+w_++w_-=1/d\), and each transverse diagonal second moment is \(w(1-s^2)/(d-1)=1/d\). Hence this measure has mean zero and covariance \(I_d/d\).

**Contact certificate for the second regime.** The side-touching latitude has standardized axial coordinate
\[
\xi=\frac{s\sqrt p}{1-sm}=\frac1d.
\]
The large-radius lower end gives the contact pole with coordinate \(-1\). Give the latitude sphere total mass \(d/(d+1)\) and the lower pole mass \(1/(d+1)\). The axial mean is zero, the axial second moment is \(1/d\), and each transverse second moment is
\[
\frac{d}{d+1}\frac{1-1/d^2}{d-1}=\frac1d.
\]
Thus this contact measure also has mean zero and covariance \(I_d/d\). Both candidates have actual boundary contacts: the latitude is the support maximizer for the conical side, and the asserted poles belong to the appropriate end planes. John's contact characterization proves maximal inscribed volume. Its uniqueness theorem proves that these are the unique John ellipsoids, not merely optimal among rotationally symmetric ellipsoids. At \(s=1/d\) the two formulae and their certificates agree.

## Verification
The accompanying standalone Python program `verify_john.py` checks the defining identities, end-plane and conical containment, contact-measure positivity, barycenter equations, and normalized second moments for 464 deterministic and pseudorandom dimension–radius configurations with \(2\le d\le30\). It outputs `PASS: 464 configurations for normalized containment and all contact moments`. This computation is a check, not a proof of the all-dimensional theorem; the contact argument above is the proof.

## Relationship to prior work
Güler and Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases* (public preprint September 5, 2007, arXiv:0709.0707), explicitly determine the **minimum-volume enclosing** ellipsoid of the same truncated second-order cones in Section 8 (Theorem 8.1). Their introduction explicitly says that they **do not solve the inscribed ellipsoid problem for this second class of convex bodies** (Section 1, discussion of Section 8). The present result supplies precisely that unaddressed complementary extremal ellipsoid, and does not assert novelty for their enclosing formula. Gruber and Schuster, *An arithmetic proof of John's ellipsoid theorem* (arXiv:1207.7246, initially public July 31, 2012), supply general contact-theoretic foundations. Related work on a retained half-cone and on homothetic frusta concerns different bodies or different geometric invariants and does not, as checked, give this all-ratio inscribed classification.

## Limitations
Only right circular frusta of strictly positive smaller radius and their affine images are covered, not oblique or nonlinear-sided frusta. The contact decomposition is a continuous rotationally invariant probability measure and can be replaced by finite contact sets; no independent audit or exhaustive historical-priority verification is claimed. A 2007 predecessor explicitly leaves this particular inscribed problem open, but discovery of later equivalent work remains possible. Nothing here revises its previously established outer-ellipsoid theorem.

## References
1. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707 (first posted 2007-09-05), especially introduction and Section 8, https://arxiv.org/abs/0709.0707 . Accessible complete text: https://studylib.net/doc/14946779/the-extremal-volume-ellipsoids-of-convex-bodies--their .
2. P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246 (first posted 2012-07-31), https://arxiv.org/abs/1207.7246 .
3. F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948, foundational contact-ellipsoid characterization.
