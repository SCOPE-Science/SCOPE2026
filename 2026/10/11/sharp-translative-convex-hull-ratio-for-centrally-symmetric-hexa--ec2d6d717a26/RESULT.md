# Sharp translative convex-hull ratio for centrally symmetric hexagons
## Finding
Let \(K\subset\mathbb R^2\) be a nondegenerate centrally symmetric convex hexagon. Define
\[
c^{\mathrm{tr}}(K)=\max_{t:\,K\cap(K+t)\ne\varnothing}\frac{\operatorname{area}(\operatorname{conv}(K\cup(K+t)))}{\operatorname{area}(K)}.
\]
Then
\[
c^{\mathrm{tr}}(K)\ge \frac73.
\]
Equality holds if and only if \(K\) is an affine image of a regular hexagon.

This settles the complete centrally symmetric six-vertex branch of the translative polygon problem posed by Horváth and Lángi: within that branch, the regular-hexagon value is sharp and the equality class is exactly the affine-regular hexagons.

## Assumptions and scope
The hexagon is assumed nondegenerate, with six distinct extreme vertices. After translating its center of symmetry to the origin, label the vertices counterclockwise as
\[
v_1,v_2,v_3,-v_1,-v_2,-v_3.
\]
Put
\[
a=\det(v_1,v_2),\qquad b=\det(v_2,v_3),\qquad c=\det(v_1,v_3).
\]
Convex cyclic order gives \(a,b,c>0\). The shoelace formula gives
\[
\operatorname{area}(K)=a+b+c.
\]

For \(x\in\partial K\), let \(A_K(x)\) be the area of the triangle with vertices \(0,x,y\), where \(y\) lies on a supporting line of \(K\) parallel to \(x\). Horváth and Lángi prove in the planar centrally symmetric setting that
\[
d_K(x)w_K(x^\perp)=8A_K(x),
\]
and their translative hull formula therefore yields
\[
c^{\mathrm{tr}}(K)=1+\frac{8\max_{x\in\partial K}A_K(x)}{\operatorname{area}(K)}.
\]

## Proof
For a boundary vector \(x\), the supporting line parallel to \(x\) maximizes \(\det(x,y)\) over \(y\in K\). Hence at the first three vertices,
\[
A_K(v_1)=\frac12\max\{a,c\},\qquad
A_K(v_2)=\frac12\max\{a,b\},\qquad
A_K(v_3)=\frac12\max\{b,c\}.
\]
Consequently,
\[
\max_{x\in\partial K}A_K(x)\ge\frac12\max\{a,b,c\}
\ge\frac{a+b+c}{6}.
\]
Substituting this into the translative formula gives
\[
c^{\mathrm{tr}}(K)\ge1+8\frac{(a+b+c)/6}{a+b+c}=\frac73.
\]

Suppose equality holds. Then both inequalities in the preceding chain are equalities. In particular,
\[
\max\{a,b,c\}=\frac{a+b+c}{3},
\]
so \(a=b=c\).

Choose the unique invertible linear map sending \(v_1\) to \((1,0)\) and \(v_3\) to \((0,1)\). If the image of \(v_2\) is \((\alpha,\beta)\), determinant ratios give
\[
\beta=\frac ac=1,\qquad \alpha=\frac bc=1.
\]
Thus the image of \(K\) is
\[
H=\operatorname{conv}\{(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)\},
\]
which is an affine image of a Euclidean regular hexagon. Hence equality can occur only for an affine-regular hexagon.

Conversely, \(c^{\mathrm{tr}}\) is affine invariant, so it suffices to evaluate it on \(H\). Its area is \(3\). On the edge from \((1,0)\) to \((1,1)\), write \(x=(1,t)\) with \(0\le t\le1\). Directly from the six vertices,
\[
\max_{y\in H}\det(x,y)=1,
\]
so \(A_H(x)=1/2\). The determinant-one linear automorphism sending \((1,0)\) to \((1,1)\), \((1,1)\) to \((0,1)\), and \((0,1)\) to \((-1,0)\) cyclically carries every edge to the next. Thus \(\max_{x\in\partial H}A_H(x)=1/2\), and
\[
c^{\mathrm{tr}}(H)=1+\frac{8(1/2)}3=\frac73.
\]
This proves both sharpness and the equality characterization.

## Verification
The proof is exact and analytic. The only non-elementary input is the published planar formula connecting the translative hull ratio with the support-triangle quantity \(A_K\). All remaining steps are determinant identities and affine normalization.

The boundary cases are explicit: six genuine extreme vertices imply \(a,b,c>0\); no smoothness or strict convexity beyond polygonal nondegeneracy is used. Equality is checked in both directions, and the canonical equality model is evaluated on every boundary edge through its determinant-preserving cyclic linear symmetry.

## Relationship to prior work
Horváth and Lángi introduced the discrete minima \(t_m\) of \(c^{\mathrm{tr}}\) over convex \(m\)-gons, proved the cases \(m\le5\), and asked whether \(t_m=c^{\mathrm{tr}}(P_m)\) for every \(m\ge3\), with affine-regular polygons as the unique equality class. Their first public version appeared on 2013-02-25. The present theorem does not solve the full \(m=6\) problem because a minimizing hexagon could be nonsymmetric; it proves the entire centrally symmetric branch.

A later normed Rogers--Shephard paper gives, for an origin-symmetric planar body, a formula for \(c^{\mathrm{tr}}\) through a largest inscribed parallelogram. That formula is compatible with the determinant proof but does not state the six-vertex extremum above. A 2026 paper on normed Macbeath problems studies different functionals involving normed volumes of maximal inscribed polytopes; despite its use of maximum-area parallelograms and affine-regular hexagons, its statements do not imply this translative area-ratio theorem.

Targeted searches using the translative ratio, largest-inscribed-parallelogram ratio, central symmetry, the exact value \(7/3\), and affine-regular-hexagon formulations located no statement covering this theorem. This negative search evidence is not itself treated as a proof of novelty.

## Limitations
The theorem is restricted to centrally symmetric convex hexagons. It does not determine \(t_6\) over all convex hexagons, and it does not give a quantitative stability estimate away from affine regularity.

The principal originality risk is an unindexed elementary observation in the classical literature on maximum-area parallelograms or affine-regular polygons. No such covering statement was located in the inspected primary and later sources.

## References
1. Á. G. Horváth and Z. Lángi, *On the volume of the convex hull of two convex bodies*, arXiv:1302.6164v1; later Monatshefte für Mathematik 174 (2014), 219–229, DOI 10.1007/s00605-013-0526-x.
2. Z. Lángi, *On a normed version of a Rogers--Shephard type problem*, arXiv:1308.2500v1; later Israel Journal of Mathematics 212 (2016), 203–217, DOI 10.1007/s11856-016-1284-y.
3. P. Gronchi and M. Longinetti, *Affinely regular polygons as extremals of area functionals*, Discrete & Computational Geometry 39 (2008), 273–297, DOI 10.1007/s00454-007-9010-5.
4. Z. Lángi and S. Wang, *Variants of a theorem of Macbeath in finite-dimensional normed spaces*, Mathematika 72 (2026), e70078, DOI 10.1112/mtk.70078.
