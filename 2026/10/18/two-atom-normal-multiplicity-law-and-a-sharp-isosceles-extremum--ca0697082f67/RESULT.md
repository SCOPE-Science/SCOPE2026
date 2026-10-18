# Two-atom normal-multiplicity law and a sharp isosceles extremum for obtuse triangles

## Finding

Let \(T=\operatorname{conv}\{A,B,C\}\) be a nondegenerate Euclidean triangle and \(Y\) uniform with respect to area on \(T\). Count normals through \(Y\) that have a base on the boundary: a normal is a line segment from its boundary base point to \(Y\) perpendicular to at least one supporting line at that base. The exceptional finite union of lines where a normal changes face is ignored; it has area zero. Write \(N_T(Y)\) for the number of distinct boundary bases of such normals.

**Complete law.** If the triangle is nonobtuse, \(\Pr(N_T=6)=1\). Otherwise, label its unique obtuse vertex \(A\), set \(u=B-A\), \(v=C-A\), \(U=u\cdot u\), \(V=v\cdot v\), \(g=u\cdot v<0\), and \(\Delta=UV-g^2>0\). Then

\[
\Pr(N_T=6)=\frac{\Delta}{(U-g)(V-g)},\qquad
\Pr(N_T=4)=1-\frac{\Delta}{(U-g)(V-g)}.
\]

Both atoms are strictly positive in an obtuse triangle; all other values have probability zero. In particular,

\[
\mathbb E N_T=4+\frac{2\Delta}{(U-g)(V-g)},\qquad
\operatorname{Var}(N_T)=4p(1-p),\quad p=\Pr(N_T=6).
\]

**Sharp shape comparison.** Fix an obtuse angle \(\theta=\angle BAC\in(\pi/2,\pi)\), put \(t=-\cos\theta\in(0,1)\) and \(r=|AC|/|AB|>0\). Then

\[
p=\frac{r(1-t^2)}{(r+t)(1+rt)},\qquad
\frac{1-t}{1+t}-p
=\frac{t(1-t)(r-1)^2}{(1+t)(r+t)(1+rt)}.
\]

Thus the unique (up to similarity and reflection) maximizer of the six-normal probability and mean count at fixed obtuse angle is the isosceles triangle \(r=1\). The sharp upper probability is \((1-t)/(1+t)\) and the sharp upper mean is \(4+2(1-t)/(1+t)\). The infimum of the six-normal probability is zero and the infimum of the mean is four, neither attained by a nondegenerate triangle at that fixed angle.

## Assumptions and scope

The plane is Euclidean, the triangle has positive area, and the sample point is area-uniform on its interior. A normal based at an edge interior is perpendicular to that edge, while at a vertex its inward direction lies in the vertex's inward normal cone, permitting any supporting line. Distinct normals are counted by distinct boundary bases. All asserted pointwise counts apply outside the measure-zero normal-bifurcation set; the law and its moments are unaffected by these exceptional points. No assertion is made for a point sampled on the boundary or outside the triangle.

## Proof

**1. Active boundary bases.** For a point \(x\) in the interior and an edge with endpoints \(P,Q\), the orthogonal foot is in its relative interior exactly when

\[
0<(x-P)\cdot(Q-P)<|Q-P|^2.
\]

A vertex \(P\) is the base of an inward normal exactly when \((x-P)\cdot(Q-P)>0\) for both other vertices \(Q\). Away from the finitely many equality lines these conditions count distinct normals, one per active side or vertex.

**2. Nonobtuse case.** Every angle has nonnegative cosine. An interior point is a strict positive combination of the two incident edge vectors at every vertex, so all three vertices are active. Its orthogonal projection onto every side lies strictly between that side's endpoints because the two base angles are nonobtuse. Therefore all six bases are active. Right angles cause no exception for an interior sample point.

**3. Obtuse case.** Translate \(A\) to the origin. Since \(g<0\), the two remaining angles at \(B,C\) are acute. For every interior point \(x\), both those vertices and the side \(BC\) contribute normals. Moreover, because \(x\) lies strictly inside the triangle, \(x\cdot u<U\) and \(x\cdot v<V\); thus side \(AB\) contributes exactly if \(x\cdot u>0\), and side \(AC\) contributes exactly if \(x\cdot v>0\). The vertex \(A\) contributes exactly if both inequalities hold. They cannot both fail: writing \(x=s u+t v\), with \(s,t>0\), gives \(|x|^2=s(x\cdot u)+t(x\cdot v)>0\). Consequently exactly one positive dot product gives \(N_T(x)=4\), while two give \(N_T(x)=6\).

**4. Exact chamber area.** Parametrize the opposite side by \(x(z)=(1-z)u+zv\), \(0\le z\le1\). Its two strict inequalities are equivalent to

\[
\frac{-g}{V-g}<z<\frac{U}{U-g}.
\]

The endpoints lie strictly inside \((0,1)\), and the interval length is

\[
\frac{U}{U-g}-\frac{-g}{V-g}=
\frac{UV-g^2}{(U-g)(V-g)}=p.
\]

The six-normal chamber is the triangle with apex \(A\) and the segment of \(BC\) specified by this interval. It has area fraction exactly \(p\), proving the entire distribution. The complement consists of two triangles whose points have exactly four normals. Its boundaries are line segments, hence area zero.

**5. Fixed-angle optimization.** Put \(|AB|=a>0\), \(|AC|=ra\), \(g=-a^2rt\), and \(\Delta=a^4r^2(1-t^2)\). Substitution gives the stated rational expression for \(p\). Direct subtraction from \((1-t)/(1+t)\) yields the displayed nonnegative quadratic square. Because \(t\in(0,1)\), equality occurs precisely at \(r=1\). Sending \(r\) to zero or infinity forces \(p\to0\), but positivity holds for every finite nonzero \(r\). The moment formulas follow from the two-atom law.

## Verification

The included standalone standard-library program `verify_triangle_normals.py` independently counts active edge and vertex bases by rational dot products on interior rational barycentric grids for six distinct rational triangles, including obtuse, right, and acute configurations. It also checks the exact six-normal base-interval identity and the fixed-angle square-gap identity on rational parameters. The program prints `TRIANGLE_NORMALS_EXACT_OK checks=2715` when all assertions pass. These finite exact checks corroborate—but do not replace—the analytical proof, which covers all nondegenerate Euclidean triangles and all admissible real parameters.

## Relationship to prior work

Santaló's average-normal question and its development are surveyed by Domokos and Lángi (first public preprint June 2014). Nasonov, Panina and Siersma (2024), Proposition 9, establish that the mean is six exactly for nonobtuse triangles and lies strictly between four and six for obtuse triangles. The complete two-atom law, its explicit all-triangle area ratio, and the unique fixed-angle isosceles extremum are the specific additional claims here; the earlier qualitative dichotomy is not claimed as new. Published work computing average normal multiplicities of regular odd polygons and of ellipses concerns different shape classes and does not imply the asserted obtuse-triangle shape profile. Classical articles by Hann and Hug are relevant historical-priority sources; the full text of some of them was not accessible for inspection.

## Limitations

All numerical checks are finite, though exact over the rational test cases. Full historical-priority verification against some classical articles remains unresolved. The theorem concerns Euclidean supporting-line normals and area-uniform interior points, not nearest-point projection alone, outward normal rays, or a boundary-weighted sampling law.

## References

1. G. Domokos and Z. Lángi, *On the average number of normals through points of a convex body*, arXiv:1406.0813v1 (first posted 3 June 2014), https://arxiv.org/abs/1406.0813.
2. I. Nasonov, G. Panina and D. Siersma, *Concurrent normals problem for convex polytopes and Euclidean distance degree*, arXiv:2406.01773v2 (2024), especially Section 6, Proposition 9, https://arxiv.org/abs/2406.01773.
3. K. Hann, *The average number of normals through a point in a convex body and a related Euler-type identity*, Geom. Dedicata 48 (1993), 27–55, https://doi.org/10.1007/BF01265675 (full text not inspected).
4. D. Hug, *On the mean number of normals through a point in the interior of a convex body*, Geom. Dedicata 55 (1995), 319–340 (full text not inspected).
