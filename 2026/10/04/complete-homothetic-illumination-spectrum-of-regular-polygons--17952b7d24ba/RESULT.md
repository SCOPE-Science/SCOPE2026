# Complete homothetic illumination spectrum of regular polygons

## Finding

Let \(P_m(R)\) be a regular Euclidean \(m\)-gon, \(m\ge3\), centered at the origin and having circumradius \(R>0\). For \(\delta>0\), define the illumination body
\[
P_m(R)^\delta
=
\left\{
x\in\mathbb R^2:
A\!\left(\operatorname{conv}(P_m(R)\cup\{x\})\right)
\le
A(P_m(R))+\delta
\right\}.
\]
Put
\[
\alpha=\frac{\pi}{m}.
\]

Then \(P_m(R)^\delta\) is a positive homothetic copy of \(P_m(R)\) if and only if there is an odd integer \(q\) satisfying
\[
3\le q<\frac m2
\]
such that
\[
\mu_{m,q}
=
\frac{\cos\alpha}{\cos(q\alpha)}
\]
and
\[
\delta_{m,q}
=
R^2
\left(
\cos^2\alpha\,\tan(q\alpha)
-
q\sin\alpha\cos\alpha
\right).
\]
For this parameter,
\[
P_m(R)^{\delta_{m,q}}
=
\mu_{m,q}P_m(R).
\]

Consequently the complete number of positive illumination parameters producing a homothetic illumination body is
\[
\left\lfloor\frac{m-3}{4}\right\rfloor.
\]
There are no such parameters for \(m\le6\). For \(7\le m\le10\), the unique one corresponds to \(q=3\); new homothetic levels appear exactly when another odd \(q\) enters the range \(q<m/2\).

The statement is affine-covariant. If \(T\) is an invertible affine map with linear part \(A\), then the corresponding affinely regular polygon has the same homothety ratios, while every illumination-area parameter is multiplied by \(|\det A|\).

## Assumptions and scope

The illumination body is the area sublevel set associated with the convex hull of the polygon and one exterior point. The homothety in the theorem is positive. The regular polygon is centered at its rotational center.

Horváth and Lángi characterize, for an arbitrary convex polygon, when an illumination body can be homothetic to the polygon. Their Theorem 8 expresses the condition through a \((k,l)\)-extension built from intersections of polygon sidelines and requires
\[
k,l\ge1,\qquad
2\mid(k+l),\qquad
k+l+1<\frac m2.
\]
It also states that any extension satisfying the homothety condition is a level curve of the illumination function. The result here specializes that structural theorem to regular polygons, computes every allowable extension exactly, and then computes the corresponding area level.

## Proof

Let the vertices of \(P_m(R)\) be
\[
v_j
=
R\left(
\cos(2j\alpha),
\sin(2j\alpha)
\right),
\qquad
j\in\mathbb Z/m\mathbb Z.
\]
Its inradius is
\[
\rho=R\cos\alpha.
\]
The sideline through \(v_j\) and \(v_{j+1}\) has outward unit normal at angle \((2j+1)\alpha\) and equation
\[
\langle x,u_j\rangle=\rho.
\]

Suppose first that an illumination body is homothetic to \(P_m(R)\). Because the illumination body inherits every rotation of \(P_m(R)\), the center of the homothety must be the origin. By Theorem 8 of Horváth and Lángi, its boundary is a \((k,l)\)-extension for integers \(k,l\ge1\) with even
\[
r=k+l
\]
and
\[
r+1<\frac m2.
\]
The same theorem forces the relevant extension sides to use pairs of sidelines whose indices differ by
\[
q=r+1.
\]
Thus \(q\) is odd and
\[
3\le q<\frac m2.
\]

Conversely, fix any odd \(q\) in that range and set
\[
s=\frac{q-1}{2}.
\]
Choose \(k=l=s\). The vertices of the corresponding extension are intersections of pairs of sidelines whose outward normals differ by angle
\[
2q\alpha.
\]
By regularity, each such intersection lies on the angular bisector of its two normals. Its distance from the origin is
\[
\frac{\rho}{\cos(q\alpha)}
=
R\frac{\cos\alpha}{\cos(q\alpha)}
=
\mu_{m,q}R.
\]
As the sideline pair advances cyclically, these intersection points are precisely the vertices of the regular polygon
\[
\mu_{m,q}P_m(R).
\]
Since \(q\alpha<\pi/2\), one has \(\mu_{m,q}>1\), so this extension contains \(P_m(R)\) in its interior. The converse direction of Theorem 8 now shows that this extension is an illumination level curve. Hence every admissible \(q\) produces a homothetic illumination body, and the structural theorem shows that there are no others.

It remains to compute its illumination parameter. Consider the extension vertex
\[
x=(\mu_{m,q}R,0).
\]
The two supporting sidelines through \(x\) are the ones with normals at angles \(-q\alpha\) and \(q\alpha\). Put
\[
\theta=(q-1)\alpha.
\]
The tangent vertices of the original polygon are
\[
v_{-s}
=
R(\cos\theta,-\sin\theta),
\qquad
v_s
=
R(\cos\theta,\sin\theta).
\]
The triangle with vertices \(x,v_{-s},v_s\) has area
\[
R^2(\mu_{m,q}-\cos\theta)\sin\theta.
\]

The portion of \(P_m(R)\) cut off by the chord \([v_{-s},v_s]\) consists of \(2s=q-1\) consecutive fan triangles from the origin, minus the triangle with vertices \(0,v_{-s},v_s\). Its area is
\[
R^2
\left(
s\sin(2\alpha)
-
\frac12\sin(2\theta)
\right).
\]
Therefore the area added by \(x\) is
\[
\delta_{m,q}
=
R^2
\left(
\mu_{m,q}\sin\theta
-
s\sin(2\alpha)
\right).
\]
Substituting
\[
\mu_{m,q}=\frac{\cos\alpha}{\cos(q\alpha)},
\qquad
\theta=(q-1)\alpha,
\qquad
s=\frac{q-1}{2},
\]
and expanding \(\sin(q\alpha-\alpha)\) gives
\[
\delta_{m,q}
=
R^2
\left(
\cos^2\alpha\,\tan(q\alpha)
-
q\sin\alpha\cos\alpha
\right).
\]

The admissible odd integers are
\[
q=3,5,7,\ldots<\frac m2.
\]
Their number is
\[
\left\lfloor\frac{m-3}{4}\right\rfloor.
\]
The ratios \(\mu_{m,q}\) strictly increase with \(q\), so the resulting homothetic bodies and their illumination parameters are distinct.

Finally, if an invertible affine map has linear part \(A\), area is multiplied by \(|\det A|\) and convex hull commutes with the affine map. This proves the affine-covariance statement.

## Verification

The proof uses the published polygon-extension characterization only as a structural reduction. The regular-polygon geometry and the illumination-area formula are derived explicitly above.

The accompanying `verify.py` independently constructs regular polygons, computes convex hulls by a monotone-chain algorithm, and checks every admissible \(q\) for all
\[
3\le m\le60.
\]
For each pair it verifies the closed formula for the added area at an extension vertex and verifies at five points along one predicted extension side that the convex-hull area stays at the same level. It also checks the exact count
\[
\left\lfloor\frac{m-3}{4}\right\rfloor.
\]
The replay prints:

`VERIFY_OK regular polygon illumination spectrum m=3..60`

These finite computations are consistency checks only. Completeness for all \(m\) comes from Theorem 8 plus the sideline-intersection calculation, and the area formula is proved symbolically.

## Relationship to prior work

Horváth and Lángi define illumination bodies, pose the problem of whether a polygon admitting a homothetic illumination body must be affinely regular, and prove the \((k,l)\)-extension characterization used here. Their theorem is structural: it gives the admissible extension pattern for an arbitrary polygon and proves that such an extension is a level curve. The inspected full text does not state the regular-polygon homothety ratios, the corresponding area parameters, or the number of homothetic illumination levels.

The distinction is substantive. For a regular polygon, the theorem above solves the entire discrete spectrum of homothetic illumination bodies, not only the existence of one extension. The area level
\[
\delta_{m,q}
=
R^2
\left(
\cos^2\!\left(\frac{\pi}{m}\right)
\tan\!\left(\frac{q\pi}{m}\right)
-
q\sin\!\left(\frac{\pi}{m}\right)
\cos\!\left(\frac{\pi}{m}\right)
\right)
\]
does not appear in the inspected source.

Targeted searches for regular-polygon illumination bodies, homothetic illumination levels, \((k,l)\)-extensions of regular polygons, and the trigonometric ratio above did not locate an equivalent formula. A 2026 paper extending illumination bodies to projective geometries was also checked for regular-polygon or polygon specializations and contained no such treatment in the accessible text.

## Limitations

The complete spectrum is proved for regular polygons and, by affine covariance, transfers to affinely regular polygons after scaling the area parameter by the affine determinant. It does not settle the converse open problem for arbitrary polygons: the existence of one homothetic illumination body is still not shown here to force affine regularity beyond the cases covered by the prior structural theorem.

The originality search was targeted rather than exhaustive. Because the final trigonometric computation is elementary once the extension characterization is available, an equivalent regular-polygon calculation could occur in weakly indexed notes or follow-up work under different terminology.

## References

Á. G. Horváth and Z. Lángi, “On the convex hull and homothetic convex hull functions of a convex body,” arXiv:2012.08955, first submitted 2020-12-16; Geometriae Dedicata 216 (2022), article 10, DOI 10.1007/s10711-022-00673-y.

R. Assouline, F. Besau, and E. M. Werner, “Illumination Bodies in Projective Geometries,” arXiv:2605.25122, first submitted 2026-05-24.
