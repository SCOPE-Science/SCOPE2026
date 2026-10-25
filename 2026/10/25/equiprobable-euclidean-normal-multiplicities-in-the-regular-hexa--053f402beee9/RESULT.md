# Equiprobable Euclidean normal multiplicities in the regular hexagon

## Finding

Let \(H\subset\mathbb R^2\) be a regular hexagon of circumradius \(1\), and let \(P\) be drawn from its interior with the normalized area measure. A **boundary normal foot** is a point \(q\in\partial H\) such that the line \(Pq\) is perpendicular to a supporting line of \(H\) at \(q\). Almost everywhere, the finite number \(N(P)\) of distinct feet satisfies
\[
\Pr(N(P)=4)=\Pr(N(P)=8)=\Pr(N(P)=12)=\frac13.
\]
The joint counts of feet in relative interiors of sides and at vertices are respectively \((2,2)\), \((4,4)\), and \((6,6)\), likewise equiprobable. Consequently
\[
\mathbb E[N(P)]=8,\qquad \operatorname{Var}(N(P))=\frac{32}{3}.
\]

## Assumptions and scope

The normal is an ordinary Euclidean supporting-line normal, **including normals at vertices**. A vertex can have many supporting lines, but is counted as one boundary foot. The statement is almost-everywhere: the twelve endpoint projection equalities lie on six lines. On those exceptional lines, boundary feet may coincide or transition; the law asserts nothing about their counting conventions. Uniformity means normalized two-dimensional Lebesgue area, not arclength or an isotropic random direction.

## Proof

Use rational coordinates \((u,v)\) for the Euclidean position \((u,\sqrt3v)\). The six vertices in counterclockwise order are
\[
(1,0),\ (1/2,1/2),\ (-1/2,1/2),\ (-1,0),\ (-1/2,-1/2),\ (1/2,-1/2).
\]
For vectors in these coordinates the Euclidean inner product is \(\langle(a,b),(c,d)\rangle=ac+3bd\). For each oriented vertex–edge incidence \((a,b)\), define \(s_{a,b}(P)=\langle P-a,b-a\rangle\). Assume all twelve incidence products are nonzero.

A side with endpoints \(a,b\) has exactly one interior normal foot if and only if both \(s_{a,b}(P)>0\) and \(s_{b,a}(P)>0\). The foot is the orthogonal projection of \(P\) onto its supporting line, and these inequalities mean the projection lies strictly between the endpoints. A vertex \(a\), with neighbors \(b,c\), is a normal foot if and only if \(s_{a,b}(P)>0\) and \(s_{a,c}(P)>0\). Indeed, \(P-a\) then belongs to the interior of the cone of inward supporting normals at \(a\), equivalently it makes an acute angle with both incident outgoing edge directions. Both criteria follow directly from the characterization of an orthogonal projection and the supporting normal cone.

For a point inside \(H\), two signs for the same edge cannot both be negative, because the projection parameter along that edge cannot be simultaneously smaller than \(0\) and larger than \(1\). Two signs at the same vertex cannot both be negative: their negative half-planes intersect only outside the two incident supporting half-planes containing \(H\) (equivalently this follows by taking the nonnegative cone of vectors from the vertex into the polygon). Each negative incidence therefore removes **one side foot and one vertex foot** from the all-positive baseline of six side feet and six vertex feet. If \(M(P)\) is the number of negative incidences, their joint count is \((6-M(P),6-M(P))\).

A direct dot-product calculation shows that the twelve incidence inequalities consist of **two copies each** of the following six strict inequalities:
\[
\frac12-u>0,\quad \frac12+u>0,\quad
1-u-3v>0,\quad 1+u+3v>0,\quad
1-u+3v>0,\quad 1+u-3v>0.
\]
Write \(K(P)\) for the number of these six inequalities violated. Then \(M(P)=2K(P)\) and
\[
N(P)=12-4K(P),\qquad (N_{\rm side}(P),N_{\rm vertex}(P))=(6-2K(P),6-2K(P)).
\]

Each failed inequality cuts out a triangle (a cap) of exact area \(|H|/6\). For instance, the cap \(u>1/2\) is the triangle with vertices \((1,0),(1/2,1/2),(1/2,-1/2)\). Rotating gives the other five congruent caps. Exactly six unordered pairs of caps have positive-area overlap: the cyclically adjacent pairs. Each overlap is a triangle of area \(|H|/18\); one example has vertices \((1,0),(1/2,1/2),(1/2,1/6)\). All remaining pairs, and all triple intersections, have area zero. These assertions follow by intersecting the six displayed linear half-planes with the displayed six-vertex hexagon; the rational-coordinate verification also enumerates every intersection exactly.

Consequently \(K\le2\) almost everywhere. The event \(K=2\) consists of the six disjoint-in-area overlaps, so it has probability \(6/18=1/3\). By linearity of expectation, \(\mathbb E K=6(1/6)=1\). Thus \(\Pr(K=1)=1-2(1/3)=1/3\), and the remaining mass \(\Pr(K=0)=1/3\). Substituting into the count formulas proves the joint distribution and the moments, including \(\operatorname{Var}(N)=(16+0+16)/3=32/3\).

## Verification

The accompanying `verify_hexagon.py` uses Python's exact rational arithmetic for the transformed coordinates and explicit convex half-plane clipping. It enumerates all thirteen positive-area sign chambers, checks the six congruent cap areas and six pairwise overlap areas, excludes triple overlaps, independently computes side and vertex feet in every chamber, and reproduces both the joint law and the variance. The program terminates successfully with rational fractions; no sampling or floating-point tolerance is used. The proof of the law is the analytic cap inclusion calculation above, not an extrapolation from finitely many sampled points.

## Relationship to prior work

Domokos and Lángi's 2014 preprint studies the **mean** number of Euclidean normals through points of a convex body, and discusses the known constant mean \(8\) for centrally symmetric cyclic polygons. That mean is recovered here, but does not determine a probability distribution. Nasonov, Panina, and Siersma study distance critical points and normals of convex polytopes generally; their normal-cone and bifurcation framework does not by itself specify these three equal hexagonal area classes. Earlier mean-normal work of Hug was checked at the abstract level, not claimed absent from its inaccessible full text. The claimed contribution is solely the complete almost-everywhere distribution and its exact variance for the regular Euclidean hexagon.

## Limitations

Exceptional incidence lines are omitted; they carry zero planar area. No analogous distribution is claimed for other polygons, and no independence or external mathematical certification is asserted. Bibliographic uncertainty remains around inaccessible older full texts or unindexed equivalent formulations.

## References

1. G. Domokos and Z. Lángi, *On the average number of normals through points of a convex body*, arXiv:1406.0813, first public 2014-06-03. Author-hosted full text: https://real.mtak.hu/16578/1/DomokosLangi_revised.pdf .
2. A. Nasonov, G. Panina, and D. Siersma, *Concurrent normals problem for convex polytopes and Euclidean distance degree*, arXiv:2406.01773, 2024; full HTML available through arXiv.
3. D. Hug, *On the mean number of normals through a point in the interior of a convex body*, Geometriae Dedicata, 1995. DOI:10.1007/BF01266322 (abstract/metadata compared; full text not inspected).
