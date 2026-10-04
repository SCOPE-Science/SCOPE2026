# Exact area and perimeter of regular hyperbolic Reuleaux polygons

## Finding

Let \(n=2m+1\ge3\) be odd and \(d>0\). Start from a regular hyperbolic \(n\)-gon whose largest vertex distance is \(d\), and replace each side by the circular arc of hyperbolic radius \(d\) centered at the unique opposite vertex. Denote the resulting body by \(\mathcal R_{n,d}\). Put
\[
t=\frac{\pi}{n},\qquad u=\sinh^2(d/2),\qquad
\alpha_{n,d}=\arccos\!\left(\frac{u+\cos t}{1+u}\right).
\]
Then
\[
L(\mathcal R_{n,d})=n\alpha_{n,d}\sinh d
\]
and
\[
A(\mathcal R_{n,d})=n\alpha_{n,d}(1+\cosh d)-2\pi.
\]
Equivalently,
\[
A(\mathcal R_{n,d})+2\pi=L(\mathcal R_{n,d})\coth(d/2).
\]
For fixed \(d>0\), as odd \(n\to\infty\),
\[
L(\mathcal R_{n,d})\to2\pi\sinh(d/2),\qquad
A(\mathcal R_{n,d})\to2\pi(\cosh(d/2)-1),
\]
which are the perimeter and area of the hyperbolic disk of radius \(d/2\). The \(n=3\) case is established hyperbolic Reuleaux-triangle theory; the new content is the uniform odd-\(n\) profile and its disk limit.

## Assumptions and scope

The ambient plane has constant curvature \(-1\). Distances, areas and circular arcs are hyperbolic. For odd \(n\), every side of a regular \(n\)-gon has a unique opposite vertex at the common maximal vertex distance \(d\). Horváth proves that hyperbolic Reuleaux polygons are convex bodies of constant width equal to their diameter, independently of their size.

## Proof

Let \(\rho\) be the circumradius of the generating regular polygon. A longest diagonal subtends central angle \(\pi-\pi/n\), so the hyperbolic cosine law gives
\[
\cosh d=1+(1+\cos t)\sinh^2\rho,
\qquad
\sinh^2\rho=\frac{\cosh d-1}{1+\cos t}.
\]
If \(s\) is the side length, adjacent vertices subtend \(2t\), hence
\[
\cosh s=1+\sinh^2\rho(1-\cos 2t).
\]
One Reuleaux arc has center at the opposite vertex and endpoints at two adjacent vertices. The corresponding isosceles hyperbolic triangle has sides \(d,d,s\) and apex angle \(\alpha\), so
\[
\cosh s=\cosh^2d-\sinh^2d\cos\alpha.
\]
Using \(u=\sinh^2(d/2)\), \(\cosh d=1+2u\), and \(\sinh^2d=4u(1+u)\), elimination of \(\rho\) and \(s\) yields
\[
\cos\alpha=\frac{u+\cos t}{1+u}.
\]
Thus \(\alpha=\alpha_{n,d}\).

In hyperbolic polar coordinates, \(ds^2=dr^2+\sinh^2r\,d\theta^2\), so one radius-\(d\) arc has length \(\alpha\sinh d\), proving the perimeter formula.

A radius-\(d\) circle has geodesic curvature \(\coth d\), so one arc contributes \(\alpha\cosh d\) to the curvature integral. At each vertex, the centers of the two incident arcs and the vertex again form the same \(d,d,s\) triangle; hence the exterior turning angle is \(\alpha\). Gauss–Bonnet for a disk in curvature \(-1\) gives
\[
n\alpha\cosh d+n\alpha-A=2\pi,
\]
which proves the area formula. The displayed perimeter-area identity follows from \(\sinh d\,\coth(d/2)=1+\cosh d\).

For fixed \(d\) and \(t=\pi/n\to0\),
\[
\frac{u+\cos t}{1+u}=1-\frac{t^2}{2(1+u)}+O(t^4),
\]
with \(1+u=\cosh^2(d/2)\). Therefore
\[
\alpha_{n,d}=\frac{t}{\cosh(d/2)}+O(t^3),
\]
and the disk limits follow.

## Verification

The accompanying `verify.py` reconstructs the circumradius and side-length relations and recomputes the arc angle from the unsimplified hyperbolic cosine laws for odd \(3\le n<80\) and several positive widths. It also checks the exact perimeter-area identity, the Euclidean small-width limit, and the fixed-width large-\(n\) disk limit.

The checker prints:

`VERIFY_OK regular hyperbolic Reuleaux profile`

The finite replay is a consistency check only; the proof above establishes the all-\(n\), all-\(d\) result.

## Relationship to prior work

Santaló's 1945 paper is cited by later authors for the hyperbolic Reuleaux-polygon definition, while Fillmore and Araújo developed hyperbolic Barbier and constant-width theory. Horváth explicitly proves that hyperbolic Reuleaux polygons have constant width at every diameter. His accessible full text contains no occurrence of “perimeter,” and its occurrence of “area” is unrelated to a Reuleaux metric profile.

Böröczky and Sagmeister treat hyperbolic Reuleaux triangles in the Blaschke–Lebesgue problem, so the \(n=3\) specialization is prior-covered and is not claimed independently. Targeted searches for regular odd hyperbolic Reuleaux polygons, arc angles, exact perimeter or area, equivalent Barbier forms, and the disk limit did not locate the uniform formulas above.

## Limitations

The theorem treats the regular odd-sided construction in curvature \(-1\). It does not classify irregular hyperbolic Reuleaux polygons, solve fixed-arc-count extremal problems, or give a spherical analogue.

Historical-source access is incomplete. Santaló's 1945 paper was identified and bibliographically inspected, but its AMS PDF was inaccessible in this run. Leichtweiss's 2005 paper was also identified through later primary literature but not inspected in full. An equivalent older calculation under different terminology therefore remains a residual originality risk.

## References

Á. G. Horváth, “Diameter, width and thickness in the hyperbolic plane,” arXiv:2011.14739, first submitted 2020-11-30; Journal of Geometry 112 (2021), article 47, DOI 10.1007/s00022-021-00613-3.

K. J. Böröczky and Á. Sagmeister, “Convex bodies of constant width in spaces of constant curvature and the extremal area of Reuleaux triangles,” arXiv:2203.16636, first submitted 2022-03-30; Studia Scientiarum Mathematicarum Hungarica 59 (2022), 244–273.

L. A. Santaló, “Note on convex curves on the hyperbolic plane,” Bulletin of the American Mathematical Society 51 (1945), 405–412, DOI 10.1090/S0002-9904-1945-08366-9.

K. Leichtweiss, “Curves of constant width in the non-Euclidean geometry,” Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg 75 (2005), 257–284, DOI 10.1007/BF02942046.
