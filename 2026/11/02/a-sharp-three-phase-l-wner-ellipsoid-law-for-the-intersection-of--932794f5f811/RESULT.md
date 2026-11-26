# A sharp three-phase Löwner-ellipsoid law for two Euclidean balls

## Finding
For every integer \(n\ge2\), the minimum-volume ellipsoid covering the proper intersection of two Euclidean balls is unique and given by the three-branch law below. The active contact orbits change at sharp center separations. The first regime is the smaller ball itself despite the proper intersection, and the number of regimes present depends on the radius ratio.

## Assumptions and scope
Write \((x,y)\in\mathbb R\times\mathbb R^{n-1}\). Let \(R\ge r>0\), \(R-r<d<R+r\), and
\[
K=\{(x,y):x^2+\|y\|^2\le R^2,\ (x-d)^2+\|y\|^2\le r^2\}.
\]
Set \(\ell=d-r\), \(u=R\), \(t=(d^2+R^2-r^2)/(2d)\), \(h=\sqrt{R^2-t^2}>0\), and
\[
d_0=-\frac r n+\sqrt{R^2-r^2(1-n^{-2})}.
\]
The unique minimum-volume enclosing ellipsoid is
\[
E=\{(x,y):(x-c)^2/a^2+\|y\|^2/b^2\le1\},
\]
with the following parameters in the proper-overlap domain:

* **Smaller-ball phase**, \(d\le d_0\): \((c,a,b)=(d,r,r)\).
* **One-pole-and-rim phase**, \(d_0<d<n(R-r)\):
  \[
  c=\frac{\ell+nt}{n+1},\qquad a=\frac{n(t-\ell)}{n+1},\qquad b=\frac{nh}{\sqrt{n^2-1}}.
  \]
* **Two-poles-and-rim phase**, \(d\ge n(R-r)\), with \(k=(R-r)/d\):
  \[
  c=\frac{\ell+u}{2},\qquad a=\frac{u-\ell}{2},\qquad b=\frac h{\sqrt{1-k^2}}
  =\frac12\sqrt{(R+r)^2-d^2}.
  \]

The formulas agree at transitions in the proper-overlap interval. The second transition lies in that interval **exactly when** \(1<R/r<(n+1)/(n-1)\). At the upper equality it is at excluded external tangency, and at \(R=r\) it is at the excluded endpoint \(d=0\). For equal radii the two-pole formula therefore covers every \(0<d<2R\), with \(a=R-d/2\), \(b=\sqrt{R^2-d^2/4}\). If \(0\le d\le R-r\), the intersection is simply the smaller ball.

## Proof
**1. Cross-sections.** The lens is full dimensional. Uniqueness of its minimum-volume enclosing ellipsoid and the orthogonal symmetries fixing the line of centers give the axial form above. The interval of axial coordinates is \([\ell,u]\); its squared transverse profile is
\[
 \rho(x)^2=\begin{cases}r^2-(x-d)^2,&\ell\le x\le t,\\ R^2-x^2,&t\le x\le u.\end{cases}
\]
The two profiles agree at the common rim \(x=t,\ \|y\|=h\).

**2. Containment.** For a candidate with \(a\le b\), the function
\[
q_j(x)=\frac{(x-c)^2}{a^2}+\frac{r_j^2-(x-c_j)^2}{b^2}
\]
on either active sphere arc is convex, since its quadratic coefficient is \(a^{-2}-b^{-2}\). It suffices to check the endpoints of the two subintervals. For the one-pole formula the left tip and the rim give equality, and the right tip gives
\[
q_{R,0}(u)-1=\frac{4d(n+1)[d-n(R-r)]}{n^2(R+d-r)^2}.
\]
Also \(a^2/b^2=\frac{n-1}{n+1}\frac{r+(t-d)}{r-(t-d)}\le1\) exactly when \(t-d\le r/n\), or \(d\ge d_0\). For the two-poles formula both tips and the rim give equality, and \(a^2/b^2=(R+r-d)/(R+r+d)<1\). For the smaller-ball formula containment holds by definition of the intersection.

**3. Optimality.** By the Löwner–John criterion, after mapping \(E\) to the unit ball a contact probability measure with mean zero and covariance \(I_n/n\) certifies optimality. All the measures below are uniform within a latitude orbit, so transverse means and off-diagonal moments vanish.

In the smaller-ball phase use the left tip, at normalized axial coordinate \(-1\), with weight \(1/(n+1)\), and the unit-sphere latitude at coordinate \(1/n\) with weight \(n/(n+1)\). The latitude belongs to the lens precisely when \(t-d\ge r/n\), equivalent to \(d\le d_0\). In the one-pole phase the same normalized measure is supported by the left tip and the common rim, now at normalized axial coordinate \(1/n\). In each case the first axial moment is zero, the axial second moment is \(1/n\), and each transverse variance is \(\frac{n}{n+1}(1-1/n^2)/(n-1)=1/n\).

In the two-poles phase the tips are at \(-1,+1\), and the rim is at normalized axial coordinate \(k\in[0,1/n]\) with squared transverse radius \(1-k^2\). Assign the rim mass \(w=(n-1)/(n(1-k^2))\), and the tips masses
\[
p_-=(1-w+wk)/2,\qquad p_+=(1-w-wk)/2.
\]
These weights sum with \(w\) to one, and are nonnegative for \(0\le k\le1/n\): in particular \(p_+=(1-nk)/(2n(1-k))\). The moments are \(-p_-+p_++wk=0\), \(p_-+p_++wk^2=1/n\), and \(w(1-k^2)/(n-1)=1/n\). The supporting points lie in the lens, proving optimality throughout this phase as well.

**4. Sharp transitions.** Put \(\delta=R-r\). The function \(g(d)=d^2+2dr/n+r^2-R^2\) increases for \(d>0\), has its nonnegative zero at \(d_0\), and, for \(\delta>0\), satisfies \(g(\delta)=-2r\delta(1-1/n)<0\) and \(g(n\delta)=(n^2-1)\delta^2>0\). Also \(g(R+r)>0\). Thus the first transition is interior whenever radii are unequal. The second is interior precisely when \(\delta>0\) and \(n\delta<R+r\), yielding the stated strict radius-ratio conditions. At \(d_0\) the relation \(t=d+r/n\) makes the one-pole parameters equal to those of the smaller ball. At an interior \(d=n\delta\) the right tip is also a contact of the one-pole solution, the parameters coincide, and the two-poles contact measure has zero mass on the right tip at equality (positive above). The exact containment and contact conditions distinguish the phases on their strict interiors.

## Verification
The accompanying standard-library Python script `verify_lens.py` checks 1,250 deterministic sampled parameter tuples in dimensions \(2,3,4,5,10\), 60 axial boundary samples per tuple, contact moment residuals, and probes near transition separations. These numerical consistency tests are not the proof; the exact endpoint and moment identities above give the all-parameter result.

## Relationship to prior work
The enclosing-ellipsoid contact criterion is classical. Todd explicitly mentions deriving the minimum-volume ellipsoid of an intersection of two balls via optimal contact measures, without giving the unequal-radius branch or threshold formulas in that passage. Kahan's tight enclosure theorem for intersecting ellipsoids in a common-center setting does not treat the distinct-center ball lenses here. Yousefi and coauthors give outer-approximation algorithms for intersections of general planar ellipses. The specific contribution here is the explicit sharp unequal-radius law for the **outer** minimum-volume ellipsoid, not the maximal-volume inner ellipsoid and not an enclosure of the union of the balls.

## Limitations
Disjoint balls and lower-dimensional tangencies are outside the proper-overlap result. No general characterization for intersections of arbitrary ellipsoids, and no exhaustive historical priority claim, is made.

## References
1. M. J. Todd, *Minimum-Volume Ellipsoids: Applications, Duality, and Algorithms*, ICIAM lecture slides, July 6, 2007, https://people.orie.cornell.edu/~miketodd/ublndetz.pdf, “The Ellipsoid Method, 2.”
2. W. Kahan, *Circumscribing an ellipsoid about the intersection of two ellipsoids*, Canadian Mathematical Bulletin 11(3), 437–441 (1968), https://doi.org/10.4153/CMB-1968-050-2.
3. S. Yousefi, X.-W. Chang, H. Wymeersch, B. Champagne, G. Toussaint, *A Novel Approach for Ellipsoidal Outer-Approximation of the Intersection Region of Ellipses in the Plane*, arXiv:1709.06021 (first posted 2017-09-18).
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948.
