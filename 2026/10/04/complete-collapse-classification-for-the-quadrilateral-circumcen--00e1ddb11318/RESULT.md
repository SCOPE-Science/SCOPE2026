# Complete collapse classification for the quadrilateral circumcenter-of-mass Euler line
## Finding
Let \(ABCD\) be a strictly convex Euclidean quadrilateral and let \(X=AC\cap BD\). Write \(\alpha=XA\), \(\gamma=XC\), \(\beta=XB\), and \(\delta=XD\), and let \(\theta=\angle AXB\in(0,\pi)\). The circumcenter of mass \(CCM(ABCD)\) equals the lamina centroid \(CM(ABCD)\)—equivalently, the generalized Euler line collapses to a point—if and only if either \(\alpha=\gamma\) and \(\beta=\delta\), so \(ABCD\) is a parallelogram, or \(4\cos^2\theta=1\) and \(\beta-\delta=2\cos\theta(\alpha-\gamma)\). Thus every non-parallelogram collapse has diagonal lines meeting at \(60^\circ\), with the two signed diagonal asymmetries matched by the displayed relation; for example \(A=(2,0)\), \(B=(1,\sqrt3)\), \(C=(-1,0)\), \(D=(-1/2,-\sqrt3/2)\) is a non-equilateral, non-parallelogram collapse example.

The classification is complete within the stated domain. In particular, the well-known sufficient condition for equilateral polygons does not exhaust the quadrilateral case: a continuous non-parallelogram family occurs exactly when the diagonal lines make an acute angle of \(60^\circ\) and the signed diagonal asymmetries satisfy the relation above.

## Assumptions and scope
The vertices \(A,B,C,D\) occur in cyclic order and form a strictly convex quadrilateral. Hence the diagonals meet at an interior point \(X\). Let \(u\) and \(v\) be the unit vectors from \(X\) toward \(A\) and \(B\), respectively, and put \(t=u\cdot v=\cos\theta\). Then
\[
A=\alpha u,\qquad C=-\gamma u,\qquad B=\beta v,\qquad D=-\delta v,
\]
with \(\alpha,\beta,\gamma,\delta>0\). The centroid is the centroid of the homogeneous lamina bounded by the quadrilateral. The circumcenter of mass is the polygon center introduced by Tabachnikov and Tsukerman; for a quadrilateral it is the intersection of the perpendicular bisectors of the two diagonals.

## Proof
Set \(p=\alpha-\gamma\) and \(q=\beta-\delta\). The polygon-centroid formula, applied with origin \(X\), gives
\[
CM(ABCD)=\frac{p}{3}u+\frac{q}{3}v.
\]
For completeness, if \(s=\sin\theta>0\), then twice the oriented area is
\[
s(\alpha+\gamma)(\beta+\delta).
\]
In the standard shoelace centroid numerator, the coefficient of \(u\) is
\[
s(\alpha^2-\gamma^2)(\beta+\delta),
\]
and the coefficient of \(v\) is
\[
s(\beta^2-\delta^2)(\alpha+\gamma),
\]
so division by three times the doubled area yields the displayed centroid formula.

Let \(K=CCM(ABCD)\). Since \(K\) lies on the perpendicular bisector of \(AC\) and on that of \(BD\),
\[
K\cdot u=\frac{p}{2},\qquad K\cdot v=\frac{q}{2}.
\]
Therefore \(CM(ABCD)=K\) is equivalent to
\[
\frac{p+qt}{3}=\frac p2,\qquad \frac{pt+q}{3}=\frac q2,
\]
or, after clearing denominators,
\[
p=2qt,\qquad q=2pt.
\]
If either \(p\) or \(q\) is zero, both are zero. This means both diagonals bisect each other, which is equivalent to \(ABCD\) being a parallelogram. Otherwise substitution gives \(4t^2=1\), and the second equation gives \(q=2tp\). Conversely, each of these two alternatives satisfies both equations, proving necessity and sufficiency.

When \(4t^2=1\), the two diagonal lines meet at an acute angle of \(60^\circ\). The sign in \(q=2tp\) records which of the two supplementary labeled angles is \(\theta\).

For the explicit example, \(p=q=1\) and \(t=1/2\), so the criterion holds. Its squared side lengths in cyclic order are \(4,7,1,7\), hence it is not equilateral; its diagonals do not bisect each other, hence it is not a parallelogram.

## Verification
The proof above is algebraic and does not depend on numerical experimentation. The included `verify.py` performs exact rational checks of the polygon-centroid reduction, the perpendicular-bisector equations, the determinant \(1-4t^2\) of the coincidence system, and the explicit non-parallelogram witness. Running

`python3 verify.py`

returns `VERIFY_OK`.

## Relationship to prior work
Myakishev introduced the quadrilateral quasi-Euler line using the lamina centroid and quasicircumcenter and proved its center collinearities. Tabachnikov and Tsukerman identified the quadrilateral circumcenter of mass with the intersection of the perpendicular bisectors of the diagonals and proved the sufficient result \(CCM(P)=CM(P)\) for every equilateral polygon. Their full text does not state a converse or a complete quadrilateral coincidence classification. The present result supplies that missing lowest-dimensional classification and shows that non-parallelogram coincidences form a genuine \(60^\circ\)-diagonal family.

Targeted searches for the phrases “quasicircumcenter equals centroid”, “quadrilateral circumcenter of mass equals center of mass”, “degenerate generalized Euler line quadrilateral”, and combinations with “60 degree” did not locate a source stating or implying the classification. A later uniqueness paper on circumcenter-of-mass constructions characterizes admissible center assignments, not which individual quadrilaterals satisfy \(CCM=CM\). A 2026 paper on averaged triangle centers uses a different polygon-center construction and therefore does not cover this statement.

## Limitations
The theorem is restricted to strictly convex quadrilaterals with the lamina centroid. It does not classify concave, crossed, or zero-signed-area quadrilaterals, and it makes no claim for polygons with more than four sides. The literature search cannot exclude an unindexed or differently phrased prior appearance; this is the principal originality risk.

## References
1. A. Myakishev, “On Two Remarkable Lines Related to a Quadrilateral,” *Forum Geometricorum* 6 (2006), 289–295. Publication date: 2006-11-20.
2. S. Tabachnikov and E. Tsukerman, “Circumcenter of Mass and generalized Euler line,” arXiv:1301.0496v1 (2013-01-03); *Discrete & Computational Geometry* 51 (2014), 815–836, DOI 10.1007/s00454-014-9597-2, MR3216665, Zbl 1301.51023.
3. S. Tabachnikov and E. Tsukerman, “Remarks on the the circumcenter of mass,” arXiv:1410.5115v1 (2014-10-19).
