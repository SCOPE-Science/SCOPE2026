# Exact second-moment boundary gap for arbitrary Euclidean triangles
## Finding
Let \(T\subset\mathbb{R}^2\) be a nondegenerate Euclidean triangle with side lengths \(a,b,c\), semiperimeter \(s=(a+b+c)/2\), circumradius \(R\), and inradius \(r\). Let \(X,X'\) be independent points uniformly distributed in area on \(T\), and let \(Y,Y'\) be independent points uniformly distributed by arclength on \(\partial T\). Then
\[
\mathbb E\|X-X'\|^2=\frac{s^2-4Rr-r^2}{9},
\qquad
\mathbb E\|Y-Y'\|^2=\frac{s^2-3r^2}{6},
\]
and hence
\[
\mathbb E\|Y-Y'\|^2-\mathbb E\|X-X'\|^2
=\frac{s^2+8Rr-7r^2}{18}>0.
\]
Thus the second-moment Zaporozhets--Tarasov inequality is strict for every nondegenerate triangle.

## Assumptions and scope
The triangle is nondegenerate, so its area is positive and \(s-a,s-b,s-c\) are all positive. Interior points use normalized planar Lebesgue measure and boundary points use normalized arclength measure. The statement concerns the squared Euclidean distance, namely the \(p=2\) moment; it does not assert the full all-moments conjecture for arbitrary triangles or arbitrary planar convex bodies.

## Proof
For any square-integrable random vector \(Z\) and an independent copy \(Z'\),
\[
\mathbb E\|Z-Z'\|^2=2\bigl(\mathbb E\|Z\|^2-\|\mathbb EZ\|^2\bigr).
\]

Write the vertices as \(A,B,C\), opposite side lengths as \(a=\|B-C\|\), \(b=\|C-A\|\), \(c=\|A-B\|\), and \(P=a+b+c\). For the area-uniform point, use barycentric coordinates \(X=\lambda_AA+\lambda_BB+\lambda_CC\). Their joint law is Dirichlet with parameters \(1,1,1\), so
\[
\mathbb E\lambda_i=\frac13,
\qquad
\mathbb E\lambda_i^2=\frac16,
\qquad
\mathbb E\lambda_i\lambda_j=\frac1{12}\quad(i\ne j).
\]
Substitution into the preceding variance identity gives
\[
\mathbb E\|X-X'\|^2=\frac{a^2+b^2+c^2}{18}.
\]
Using the standard triangle identity \(a^2+b^2+c^2=2(s^2-r^2-4Rr)\) yields the stated interior formula.

For a boundary-uniform point, the edge \(BC\), \(CA\), or \(AB\) is selected with probabilities \(a/P\), \(b/P\), or \(c/P\), respectively, and the conditional point is uniform on that segment. If \(U,V\) are the endpoints of a segment and \(W\) is uniform on it, then
\[
\mathbb EW=\frac{U+V}2,
\qquad
\mathbb E\|W\|^2=\frac{\|U\|^2+U\mathbin{\cdot}V+\|V\|^2}3.
\]
Applying these three times and simplifying in any translated coordinate system gives
\[
\mathbb E\|Y-Y'\|^2
=\frac{a^3+b^3+c^3+3abc}{6(a+b+c)}.
\]
Now use \(ab+bc+ca=s^2+r^2+4Rr\), \(abc=4Rrs\), and \(a+b+c=2s\). Expanding \(a^3+b^3+c^3\) in the elementary symmetric polynomials gives
\[
\mathbb E\|Y-Y'\|^2=\frac{s^2-3r^2}6.
\]
Subtracting the two exact expressions gives the claimed gap.

For a self-contained strict-positivity check, put \(x=s-a\), \(y=s-b\), and \(z=s-c\). Then \(x,y,z>0\), \(a=y+z\), \(b=z+x\), and \(c=x+y\). Before the \(R,r\) simplification, the numerator of the gap over the common denominator \(18(a+b+c)\) is
\[
2a^3-a^2b-a^2c-ab^2+9abc-ac^2+2b^3-b^2c-bc^2+2c^3.
\]
After the substitution it becomes
\[
2\bigl(x^3+y^3+z^3+5x^2y+5x^2z+5xy^2+5xz^2+5y^2z+5yz^2+3xyz\bigr),
\]
which is strictly positive. This proves strictness without an auxiliary inequality.

## Verification
The algebraic identities were independently replayed in `verify.py`. The script derives the boundary second moment from a coordinate model \(A=(0,0)\), \(B=(c,0)\), \(C=(u,v)\), verifies the side-length gap, verifies the positive semitangent expansion, and verifies the \(s,R,r\) form. The proof above does not rely on numerical sampling or a finite enumeration.

As checks on normalization, for an equilateral triangle of side length \(q\) the formulas give \(\mathbb E\|X-X'\|^2=q^2/6\) and \(\mathbb E\|Y-Y'\|^2=q^2/3\). The result is invariant under translation, rotation, and common scaling, as both sides scale quadratically.

## Relationship to prior work
Lotnikov's arXiv:2608.14848v1 formulates the all-moments comparison \(\Delta^p(K)\le\theta^p(K)\), proves sufficiently high moments for arbitrary planar convex bodies, and proves the triangle case only for the first moment via a stronger per-projection inequality. Its displayed sufficient condition for arbitrary planar bodies cannot cover \(p=2\): for \(p=2\) it requires \(|T|/|\partial T|^2\ge1/\sqrt{40}\), while the planar isoperimetric inequality gives \(|T|/|\partial T|^2\le1/(4\pi)\).

Tokmachev's arXiv:2607.08869v1 proves all \(p\ge1\) when the interior and boundary centroids coincide, and for a circumscribed polytope under the stronger condition that the incenter coincides with both centroids. For a triangle, the area centroid and perimeter centroid coincide only in the equilateral case: writing the boundary centroid as
\[
\frac{{(b+c)A+(c+a)B+(a+b)C}}{{2(a+b+c)}},
\]
equality with \((A+B+C)/3\) forces \(b+c=2a\), \(c+a=2b\), and \(a+b=2c\), hence \(a=b=c\). Thus that theorem does not imply the present arbitrary-triangle statement.

Earlier distance-distribution work such as Pure--Durrani--Tong--Pan (2022) treats two area-uniform points in arbitrary polygons, while Bäsel's regular-polygon moment formulas concern area-uniform points in regular polygons. These sources can recover or specialize interior moments but do not supply the arbitrary-triangle boundary-vs-interior second-moment comparison above.

## Limitations
The result is specific to Euclidean triangles and the squared-distance moment. It does not establish convex-order domination, does not treat \(p\ne2\), and does not imply the all-moments conjecture for arbitrary planar convex bodies. The literature comparison found no covering statement, but absence from the inspected sources and searches is not a proof that no equivalent formula exists elsewhere.

## References
1. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848v1, submitted 2026-08-14.
2. A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869v1, submitted 2026-07-09.
3. G. Bonnet, A. Gusakova, C. Thäle, D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, Advances in Mathematics 386 (2021), DOI:10.1016/j.aim.2021.107813.
4. R. Pure, S. Durrani, F. Tong, J. Pan, *Distance distribution between two random points in arbitrary polygons*, Mathematical Methods in the Applied Sciences 45 (2022), DOI:10.1002/mma.7951.
5. U. Bäsel, *The moments of the distance between two random points in a regular polygon*, arXiv:2101.03815.
