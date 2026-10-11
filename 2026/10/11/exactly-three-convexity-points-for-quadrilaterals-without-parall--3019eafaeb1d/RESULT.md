# Exactly three convexity points for quadrilaterals without parallel sides
## Finding
Let \(Q=ABCD\subset\mathbb R^2\) be a nondegenerate convex quadrilateral with no pair of parallel sides. A **convexity point** is a point \(z\) for which \(Q\cup(2z-Q)\) is convex. Then \(Q\) has exactly three convexity points.

After an invertible affine normalization
\[
A=(0,0),\qquad B=(1,0),\qquad D=(0,1),\qquad C=(p,q),
\]
convexity is equivalent to \(p>0\), \(q>0\), \(p+q>1\), and the absence of parallel sides is equivalent to \(p\ne1\), \(q\ne1\). Put \(m_{XY}=(X+Y)/2\). The complete list is
\[
\begin{array}{c|c}
\text{parameter region}&\text{convexity points}\\ \hline
p>1,\ q>1& m_{BC},m_{BD},m_{CD}\\
p>1,\ q<1& m_{AC},m_{AD},m_{CD}\\
p<1,\ q>1& m_{AB},m_{AC},m_{BC}\\
p<1,\ q<1& m_{AB},m_{AD},m_{BD}.
\end{array}
\]
In each case these are exactly the three vertices of the convex hull of the middle hedgehog.

## Assumptions and scope
The quadrilateral is assumed nondegenerate, convex, and cyclically labelled \(A,B,C,D\). No two sides are parallel. This excludes trapezoids and parallelograms; no claim is made here about those boundary strata. The statement is affine invariant, so the normalization above loses no cases in the stated class.

For a planar convex body \(K\) and unit vector \(u\), let \(M_K(u)\) be the line midway between the two support lines with normals \(u\) and \(-u\), and let
\[
Z_K(u)=\frac12\bigl(F(K,u)+F(K,-u)\bigr)
\]
be the corresponding middle set. The middle hedgehog is \(\mathcal M_K=\bigcup_u Z_K(u)\).

## Proof
Schneider's reflection criterion for bodies with no pair of parallel edges states that \(z\) is a convexity point exactly when
\[
z\in M_Q(u)\ \Longrightarrow\ z\in Z_Q(u)\qquad\text{for every unit }u.
\tag{1}
\]
For a polygon with no parallel edges, every edge contributes one middle segment and the middle hedgehog is their closed polygonal union.

First observe that every convexity point lies on \(\mathcal M_Q\). Indeed, with support function \(h_Q\), define
\[
g_z(u)=\frac12\bigl(h_Q(u)-h_Q(-u)\bigr)-\langle z,u\rangle.
\]
Then \(g_z(-u)=-g_z(u)\), so continuity gives a direction \(u\) with \(g_z(u)=0\), equivalently \(z\in M_Q(u)\). Criterion (1) then gives \(z\in Z_Q(u)\subset\mathcal M_Q\).

Normalize affinely as above. The four edge normals partition the unoriented normal circle into four open cones. On any such cone the two support faces are singleton vertices, say \(X\) and \(Y\), so the middle set is the single midpoint \(m_{XY}\) and the middle-line equation is
\[
\langle x-m_{XY},u\rangle=0.
\tag{2}
\]
At an edge-normal boundary the middle set is the segment joining the two adjacent midpoint values. Thus criterion (1) becomes a finite four-cone test: a point on one of the four middle segments is allowed only if every further solution of (2) occurs at the corresponding midpoint.

Carrying out this test gives the following middle-hedgehog corner sets and the unique corner excluded by (1):
\[
\begin{array}{c|c|c}
\text{region}&\text{hedgehog corners}&\text{corner failing (1)}\\ \hline
p>1,q>1& m_{AC},m_{BC},m_{BD},m_{CD}&m_{AC}\\
p>1,q<1& m_{AC},m_{AD},m_{BD},m_{CD}&m_{BD}\\
p<1,q>1& m_{AB},m_{AC},m_{BC},m_{BD}&m_{BD}\\
p<1,q<1& m_{AB},m_{AC},m_{AD},m_{BD}&m_{AC}.
\end{array}
\tag{3}
\]
For completeness, the same four-cone calculation also shows that every relative-interior point of every middle segment has a second middle line through it whose middle set is a different singleton midpoint, so no segment-interior point satisfies (1). Hence the only possible convexity points are the three nonexcluded corners in each row of (3).

It remains to check that those three points really are convexity points. Their status can be seen directly from (1), and it also follows from Schneider's exposed-point lemma once we identify the convex hull. In the four regions, the excluded corner is a strict convex combination of the other three. Using doubled midpoints to remove the factor \(1/2\), the coefficients are respectively
\[
\begin{aligned}
AC&=\frac{p-1}{p+q-1}BC+\frac1{p+q-1}BD+\frac{q-1}{p+q-1}CD,\\
BD&=\frac{p-1}p AD+\frac qp AC+\frac{1-q}p CD,\\
BD&=\frac{q-1}q AB+\frac pq AC+\frac{1-p}q BC,\\
AC&=(1-q)AB+(1-p)AD+(p+q-1)BD.
\end{aligned}
\]
All displayed coefficients are strictly positive in their indicated regions and sum to one. Therefore \(\operatorname{conv}\mathcal M_Q\) is exactly the triangle spanned by the three surviving corners. Each of those corners is exposed, hence is a convexity point. Together with the exclusion above, this proves exactness.

## Verification
The proof uses an exact support-function criterion, not a finite sampling argument. The only case split is by the signs of \(p-1\) and \(q-1\), which exhaust the no-parallel-sides domain. The convexity inequalities \(p>0\), \(q>0\), \(p+q>1\) follow from the four oriented edge cross-products of the normalized quadrilateral. The barycentric coefficients above are positive precisely in the stated regions.

The critical external lemma was checked in the full text of Rolf Schneider, *Reflections of planar convex bodies*: for a body with no pair of parallel edges, condition (1) is necessary and sufficient. The middle-hedgehog polygonal description and the exposed-point implication were checked in the full text of Schneider, *The middle hedgehog of a planar convex body*.

## Relationship to prior work
Schneider introduced convexity points and proved that every non-centrally symmetric planar convex body has three affinely independent ones. He later observed that triangles and Reuleaux triangles have precisely three, asked whether having only three is typical, and proved instead that a Baire-typical planar convex body has infinitely many. The later paper also develops the middle hedgehog of polygons with no parallel edges and proves that exposed points of its convex hull are convexity points.

The present statement is a low-complexity exact classification: every convex quadrilateral in the open dense no-parallel-sides class has precisely three convexity points, with an explicit affine formula. Neither inspected Schneider paper states a quadrilateral classification, and a full-text search of both inspected papers found no occurrence of “quadrilateral”.

## Limitations
No statement is made for quadrilaterals with a pair of parallel sides. Those cases fall outside the hypothesis of the reflection criterion used here and can have different middle-set degeneracies. The result concerns point reflections in the Euclidean affine plane; it does not address higher-dimensional polytopes or other reflection notions.

## References
1. R. Schneider, *Reflections of planar convex bodies*, arXiv:1504.00541v1, first submitted 2015-04-02. Primary MSC 52A10.
2. R. Schneider, *The middle hedgehog of a planar convex body*, arXiv:1607.03014v1, first submitted 2016-07-11. MSC 52A10.
