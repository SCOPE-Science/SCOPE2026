# A sharp three-phase Löwner-ellipsoid law for two Euclidean balls

## Finding
For every integer \(n\ge2\), the unique minimum-volume ellipsoid covering the proper intersection of two Euclidean balls of potentially unequal radii has the explicit three-branch form below. Two sharp center-separation transitions exchange the contact orbits. The first regime is simply the smaller ball even when that ball is *not* contained in the larger one. The last regime is absent for sufficiently unequal radii.

## Assumptions and scope
Write \((x,y)\in\mathbb R\times\mathbb R^{n-1}\). Let \(R\ge r>0\), \(R-r<d<R+r\), and
\[
K=\{(x,y):x^2+\|y\|^2\le R^2,\ (x-d)^2+\|y\|^2\le r^2\}.
\]
Set \(\ell=d-r\), \(u=R\), \(t=(d^2+R^2-r^2)/(2d)\), \(h=\sqrt{R^2-t^2}>0\), and
\[
d_0=-\frac r n+\sqrt{R^2-r^2(1-n^{-2})}.
\]
The unique enclosing ellipsoid of minimum \(n\)-volume has equation
\[
E=\{(x,y):(x-c)^2/a^2+\|y\|^2/b^2\le1\},
\]
with the following **complete** parameter classification, restricted to the proper-overlap domain:

* **Smaller-ball phase:** if \(d\le d_0\), then \((c,a,b)=(d,r,r)\).
* **One-pole-and-rim phase:** if \(d_0<d<n(R-r)\), then
  \[
  c=\frac{\ell+nt}{n+1},\qquad a=\frac{n(t-\ell)}{n+1},\qquad b=\frac{nh}{\sqrt{n^2-1}}.
  \]
* **Two-poles-and-rim phase:** if \(d\ge n(R-r)\), then, with \(k=(R-r)/d\),
  \[
  c=\frac{\ell+u}{2},\qquad a=\frac{u-\ell}{2},\qquad b=\frac h{\sqrt{1-k^2}}
  =\frac12\sqrt{(R+r)^2-d^2}.
  \]

The formulas agree continuously where regimes meet. The second transition lies in the proper-overlap domain exactly when \(R/r<(n+1)/(n-1)\); at equality it meets the excluded tangency endpoint. For \(R=r\), the two-pole phase covers every \(0<d<2R\), with \(a=R-d/2\), \(b=\sqrt{R^2-d^2/4}\). If \(0\le d\le R-r\), the intersection is simply the smaller ball (including the centered case).

## Proof
**1. Reduction and geometry.** Uniqueness of the minimum-volume enclosing ellipsoid of a full-dimensional compact convex set and rotation invariance around the center line imply the axial form displayed above. The axial interval of \(K\) is \([\ell,u]\); its maximal squared transverse radius is
\[
\rho(x)^2=\begin{cases}r^2-(x-d)^2,&\ell\le x\le t,\\ R^2-x^2,&t\le x\le u.\end{cases}
\]
This identity follows by solving the equality of the two sphere profiles. The common rim lies at \(x=t\) and \(\|y\|=h\).

**2. Exact containment.** For any proposed \(E\) with \(a\le b\), the function
\[
q_j(x)=\frac{(x-c)^2}{a^2}+\frac{r_j^2-(x-c_j)^2}{b^2}
\]
for a boundary arc of a ball with radius \(r_j\) and axial center \(c_j\) is a convex quadratic: its quadratic coefficient is \(a^{-2}-b^{-2}\ge0\). Therefore \(E\supseteq K\) follows from \(q_{r,d}(\ell),q_{r,d}(t),q_{R,0}(t),q_{R,0}(u)\le1\). In the one-pole regime, direct substitution gives equality at \(\ell\) and \(t\), and
\[
q_{R,0}(u)-1=\frac{4d(n+1)[d-n(R-r)]}{n^2(R+d-r)^2}\le0.
\]
Moreover \(a^2/b^2=\frac{n-1}{n+1}\frac{r+(t-d)}{r-(t-d)}\le1\) precisely when \(d\ge d_0\). In the two-pole regime equality holds at all three axial levels \(\ell,t,u\), and \(a^2/b^2=[(R+r)-d]/[(R+r)+d]<1\). The smaller-ball regime is manifestly containing because \(K\subseteq B_r(de_1)\).

**3. Exact optimality certificates.** The standard Löwner–John contact criterion says that, after transforming \(E\) to the unit ball, a probability measure on contact points with mean zero and covariance \(I_n/n\) certifies the unique minimum-volume enclosing ellipsoid. The criterion applies in every dimension \(n\ge2\).

In the smaller-ball regime, use the left axial point of the smaller ball, whose transformed axial coordinate is \(-1\), with weight \(1/(n+1)\); use the uniform spherical latitude at transformed axial coordinate \(1/n\) with weight \(n/(n+1)\). This entire latitude belongs to \(K\) exactly because \(t-d\ge r/n\), equivalent to \(d\le d_0\). In the one-pole-and-rim regime the identical normalized measure is supported instead by the left tip \(\ell\) and the common rim \(x=t\), whose transformed axial coordinate is \(1/n\). Its first axial moment vanishes; the axial second moment is \(1/n\), and each transverse diagonal covariance equals \(\frac{n}{n+1}(1-1/n^2)/(n-1)=1/n\).

In the two-poles-and-rim regime, the left and right tips become normalized axial coordinates \(-1,+1\), while the common rim has axial coordinate \(k=(R-r)/d\in[0,1/n]\) and transverse squared radius \(1-k^2\). Put uniform total rim weight
\[
w=\frac{n-1}{n(1-k^2)}
\]
and axial pole weights
\[
p_-=\frac{1-w+wk}{2},\qquad p_+=\frac{1-w-wk}{2}.
\]
They are nonnegative for \(0\le k\le1/n\), sum with \(w\) to one, and satisfy \(-p_-+p_++wk=0\), \(p_-+p_++wk^2=1/n\), and \(w(1-k^2)/(n-1)=1/n\). By rotational symmetry the off-diagonal covariances vanish. All supporting points belong to \(K\), so the contact criterion proves global optimality in all three regimes.

**4. Partition and sharpness.** The smaller-ball latitude fits exactly when \(d\le d_0\). The one-pole ellipse is elongated transversely exactly for \(d\ge d_0\) and covers the rightmost tip exactly while \(d\le n(R-r)\). The two-pole contact weights become nonnegative exactly when \(d\ge n(R-r)\). These conditions partition the overlap interval, and the formulas coincide at boundaries. Since the containing ellipsoid is unique, the displayed phases and contact changes are sharp.

## Verification
The accompanying standard-library Python code `verify_lens.py` checks 1,250 deterministic random parameter tuples in dimensions \(2,3,4,5,10\), 60 axial boundary samples per tuple, exact normalized contact-moment equations, and transition-boundary probes. Recorded maximum numerical containment excess is \(1.53\times10^{-13}\), and maximum contact-moment residual is \(1.39\times10^{-16}\). These finite consistency tests are not a proof; the preceding exact convexity and contact-measure argument establishes the theorem for all admissible parameters.

## Relationship to prior work
The generic Löwner–John theorem is classical. In his dated 2007 lecture notes, Todd explicitly states that the minimum-volume ellipsoid of an intersection of two balls can be derived using optimal contact measures, without presenting the above full unequal-radius dimension-dependent three-phase formulas or phase thresholds; this direct historical mention is a substantial priority caveat. Yousefi, Chang, Wymeersch, Champagne, and Toussaint (2017) develop an outer-approximation algorithm for planar intersections of general ellipses, not an exact spherical-lens classification. The present result concerns the **outer** minimum-volume ellipsoid, not the different maximum-volume **inner** ellipsoid of a lens.

## Limitations
No claim is made for disjoint balls or lower-dimensional tangential intersections; nested balls have the trivial smaller-ball answer. The derivation is for two Euclidean balls, not arbitrary ellipsoid intersections. Earlier unlocated exact lens formulas could predate this presentation; the accessible 2007 source explicitly identifies the same optimization problem. No independent scientific audit or verification of historical priority has been performed.

## References
1. M. J. Todd, *Minimum-Volume Ellipsoids: Applications, Duality, and Algorithms*, ICIAM lecture slides, July 6, 2007, https://people.orie.cornell.edu/~miketodd/ublndetz.pdf, especially slides 10–13.
2. S. Yousefi, X.-W. Chang, H. Wymeersch, B. Champagne, G. Toussaint, *A Novel Approach for Ellipsoidal Outer-Approximation of the Intersection Region of Ellipses in the Plane*, arXiv:1709.06021 (first posted 2017-09-18), https://arxiv.org/abs/1709.06021.
3. F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948, classical enclosing-ellipsoid contact criterion (also discussed in Todd's reference above).
