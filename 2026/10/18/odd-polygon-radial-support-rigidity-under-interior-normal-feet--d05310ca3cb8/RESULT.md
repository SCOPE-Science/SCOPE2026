# Odd-polygon radial–support rigidity under interior normal feet

## Finding
Let \(n\ge3\) and let \(P\) be a strictly convex Euclidean \(n\)-gon whose interior contains the origin. Suppose that for each side the perpendicular projection of the origin onto its supporting line belongs to the **relative interior of the side**. Then, when \(n\) is odd, the ordered directions of the vertices as seen from the origin, together with the ordered perpendicular distances from the origin to all side-supporting lines, determine \(P\) uniquely. This remains true for arbitrary unequal positive side distances.

More precisely, if \(h_i>0\) is the support distance of side \([v_i,v_{i+1}]\), \(d_i=\|v_i\|\), and \(\delta_i\in(0,\pi)\) is the counterclockwise angle from \(v_i\) to \(v_{i+1}\), all cyclically indexed, then every such polygon obeys
\[
\arccos\frac{h_i}{d_i}+\arccos\frac{h_i}{d_{i+1}}=\delta_i.\tag{1}
\]
For odd \(n\), system (1) has at most one solution corresponding to a polygon with all perpendicular feet strictly internal. At every such solution, its Jacobian in the log-radii is nonsingular, so reconstruction from these data is locally real-analytic.

The odd-parity restriction is sharp: when \(n\) is even, any two such realizations with identical data have alternating strictly opposite inequalities among their radii (unless identical), and their radii are determined by any one radius. In particular, an explicit continuum of nonidentical quadrilaterals has the same four ordered vertex rays and the same four support distances.

## Assumptions and scope
The polygon has exactly \(n\ge3\) vertices \(v_0,\ldots,v_{n-1}\), in counterclockwise order, no flat interior angle, and contains \(0\) strictly in its interior. Each outward support line of \([v_i,v_{i+1}]\) has positive distance \(h_i\) from \(0\). The orthogonal foot from \(0\) to this line lies strictly between the endpoints, not merely on the line extension. The prescribed vertex rays are *labelled* and ordered, and their gaps \(\delta_i\) lie in \((0,\pi)\) with sum \(2\pi\). No assertion is made about polygon realizations in which even one orthogonal foot is outside its side. The result is a uniqueness theorem conditional on existence, not an all-instance existence theorem.

## Proof
Let \(q_i\) be the perpendicular foot from \(0\) to the segment \([v_i,v_{i+1}]\). The two right triangles \((0,q_i,v_i)\) and \((0,q_i,v_{i+1})\) have common short leg \(\|q_i\|=h_i\), with hypotenuses \(d_i\) and \(d_{i+1}\). Since the foot is strictly between the endpoints, its radial direction lies strictly between the successive vertex rays. Consequently \(d_i>h_i\), \(d_{i+1}>h_i\), and their two strictly positive acute angles add to \(\delta_i\), proving (1).

For fixed \(h>0\), the function \(f_h(d)=\arccos(h/d)\) is strictly increasing for \(d>h\), with derivative \(h/(d\sqrt{d^2-h^2})>0\). Suppose two admissible polygons have the same vertex rays and support distances, and radii \(d_i\) and \(\widetilde d_i\). If \(d_i=\widetilde d_i\) at any index, (1) and strict monotonicity force equality at the next index; cyclic propagation gives equality at every index. Otherwise, if \(d_i>\widetilde d_i\), equation (1) forces \(d_{i+1}<\widetilde d_{i+1}\). Thus strict inequalities alternate around the cycle. An odd cycle cannot support this alternation, proving uniqueness when \(n\) is odd. For even \(n\), it proves the claimed alternating comparison and that a fixed initial radius determines at most one ordered radius list.

For local rigidity, put \(s_i=\log d_i\) and define
\[
F_i(s;h,\delta)=\arccos(h_i e^{-s_i})+\arccos(h_i e^{-s_{i+1}})-\delta_i.
\]
The Jacobian \(J=\partial F/\partial s\) has only the entries
\[
a_i=J_{i,i}=\frac{h_i}{\sqrt{d_i^2-h_i^2}}>0,\qquad
b_i=J_{i,i+1}=\frac{h_i}{\sqrt{d_{i+1}^2-h_i^2}}>0,
\]
where the second index is cyclic. Exactly two permutations contribute to its determinant: the identity and the full cyclic shift. Therefore
\[
\det J=\prod_{i=0}^{n-1}a_i+(-1)^{n-1}\prod_{i=0}^{n-1}b_i.
\]
For odd \(n\) both terms are positive. The real-analytic implicit function theorem gives a locally unique analytic radial inverse for nearby admissible data. Strict convexity and the interior-foot inequalities persist locally.

To demonstrate sharp parity, take the four fixed rays of angles \(\pi/4,3\pi/4,5\pi/4,7\pi/4\), and choose any \(t\in(0,\pi/2)\). Set \(d_0=d_2=\sec t\) and \(d_1=d_3=\csc t\). On every side the two acute angles are \(t\) and \(\pi/2-t\), so the support distance is exactly \(h_i=1\); all feet lie in their side interiors. These are nonidentical rhombi with identical labelled rays and support distances. Their distinctness follows from the strictly increasing function \(\sec t\).

## Verification
The identity (1), strict increase of \(f_h\), odd-cycle contradiction, and the two-permutation determinant expansion are analytic arguments for all admissible dimensions \(n\), not numerical extrapolations. The accompanying standard-library Python program tests 2,500 perturbed regular odd polygons of orders \(3,5,7,9,11\), verifies the side-foot condition, angle identity, and positive determinant, and checks four members of the even quadrilateral family. It also checks the unequal-support-distance integer-coordinate triangle with vertices \((2,0),(-1,2),(-1,-1)\), for which \((h_0,h_1,h_2)=(4/\sqrt{13},1,2/\sqrt{10})\). The tests are finite consistency checks only.

## Relationship to prior work
Baumann, Biedl, Elashmawi, Fink, Saumell and Schulz (2026), Section D.4.2, identify reconstruction of convex polygons from labelled corner directions and edge distances as an unresolved general scenario, in part because a vertex can admit alternative tangent-line choices. The strict interior-foot condition used here excludes that ambiguity, and the odd cycle then enforces global rigidity. Their paper does not state this odd-order uniqueness or the exact Jacobian determinant. Older parity rigidity for *tangential* polygons with prescribed side lengths concerns a different data set and has all support distances equal; the present statement allows arbitrary unequal support distances and fixes vertex rays instead of side lengths. The classical fixed-parallel-sides result for cyclic polygons likewise does not specify these nonuniform radial and support measurements.

## Limitations
No general polygon-reconstruction algorithm or uniqueness is asserted without the strict interior-foot hypothesis. The theorem does not assert that arbitrary positive distances and arbitrary ray gaps admit a realization. The Jacobian result yields local conditioning qualitatively, not a dimension-independent numerical condition bound. Prior-priority assessment is based on the primary sources and indexed literature actually inspected; unindexed sources may contain overlapping observations. No independent external mathematical audit has been performed.

## References
1. A. Baumann, T. Biedl, M. Elashmawi, S. D. Fink, M. Saumell, A. Schulz, *On Reconstructing a Convex Polygon from Partial Information*, arXiv:2607.01423, first version 2026-07-01, especially Section D.4.2. https://arxiv.org/abs/2607.01423
2. A. Leung and F. Lopez-Real, *Properties of tangential and cyclic polygons: an application of circulant matrices*, International Journal of Mathematical Education in Science and Technology 34 (2003), 859–870. https://doi.org/10.1080/00207390310001595456
3. *Poncelet Theorem*, exposition of the parallel-side parity theorem for polygons inscribed in a circle. https://www.cut-the-knot.org/Curriculum/Geometry/PonceletTheorem.shtml
