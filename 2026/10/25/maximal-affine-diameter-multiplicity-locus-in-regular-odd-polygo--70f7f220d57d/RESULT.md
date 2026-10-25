# Maximal affine-diameter multiplicity locus in regular odd polygons
## Finding
Let \(n=2m+1\ge5\) be odd, and let \(P_n\subset\mathbb R^2\) be a regular \(n\)-gon of circumradius \(R>0\). For \(z\in\operatorname{int}P_n\), let \(N_a(P_n,z)\) be the number of distinct affine-diameter segments of \(P_n\) containing \(z\). Then, for Lebesgue-almost every \(z\in P_n\),
\[
N_a(P_n,z)\in\{1,3,5,\ldots,n\},
\]
and every value in this set occurs on a set of positive area.

The essential maximum-multiplicity locus \(\{z:N_a(P_n,z)=n\}\) is, up to its boundary, a central regular \(n\)-gon \(C_n\) with inradius and circumradius
\[
r(C_n)=R\sin\frac{\pi}{2n},\qquad
R(C_n)=R\frac{\sin(\pi/(2n))}{\cos(\pi/n)}.
\]
Consequently, for a point chosen uniformly from \(P_n\),
\[
\Pr\{N_a(P_n,Z)=n\}
=\frac{\sin^2(\pi/(2n))}{\cos^2(\pi/n)}
=\frac{\pi^2}{4n^2}+O(n^{-4})
\quad(n\to\infty,\ n\text{ odd}).
\]

## Assumptions and scope
An affine diameter is a segment whose endpoints lie on two distinct parallel supporting lines of the same convex body. Multiplicity counts distinct geometric segments, not supporting directions. The claim concerns only regular Euclidean polygons with odd side count \(n\ge5\), under uniform area measure. It makes no claim about exact probabilities for the intermediate levels \(1,3,\ldots,n-2\), irregular polygons, even polygons, or dimensions above two. A finite union of diagonals and arrangement boundaries is ignored in the almost-everywhere statements.

## Proof
Write the vertices as \(v_j=R(\cos(2\pi j/n),\sin(2\pi j/n))\), with indices modulo \(n\), and let \(E_i=[v_i,v_{i+1}]\). Since \(n\) is odd, the support line opposite \(E_i\) touches the vertex \(v_{i+m+1}\). Define
\[
T_i=\operatorname{conv}\{v_i,v_{i+1},v_{i+m+1}\},\qquad i=0,\ldots,n-1.
\]
For a point not on any vertex-to-vertex segment or triangle boundary, an affine diameter through it has one endpoint at a vertex and the other in the relative interior of an edge. Such a segment exists for edge \(E_i\) exactly when the point lies in \(T_i\), and it is unique for that edge. Thus
\[
N_a(P_n,z)=\sum_{i=0}^{n-1}\mathbf 1_{T_i}(z)
\]
away from a finite union of line segments, which has area zero.

Each \(T_i\) contains the center. Its two non-boundary sides are longest diagonals of \(P_n\). Every such diagonal is a side of exactly two of the triangles, on the same side of its supporting line. Along a generic ray from the center, each triangle is exited at most once; crossing a diagonal boundary therefore lowers the triangle count by exactly two. A point sufficiently close to the relative interior of a polygon edge belongs to exactly one triangle, whereas the center belongs to all \(n\) triangles. Choose a ray whose direction avoids the finite set of diagonal-intersection directions and whose endpoint on the polygon boundary is not a vertex. Along this ray the count descends from \(n\) to \(1\) in steps of two. Each intermediate value therefore holds on an open arrangement cell, proving both oddness and occurrence of every value \(1,3,\ldots,n\) on positive-area sets.

The points counted with multiplicity \(n\) are exactly the intersection of all \(T_i\), up to boundary exceptions. This intersection is the intersection of the center-side halfplanes bounded by all longest diagonals; the original polygon-edge constraints are redundant because \(R\sin(\pi/(2n))<R\cos(\pi/n)\) for \(n\ge5\). The longest diagonals have chord endpoints separated by central angle \(\pi-\pi/n\), so each supporting line is at distance
\[
R\cos\frac{\pi-\pi/n}{2}=R\sin\frac{\pi}{2n}
\]
from the center. Their oriented normals are equally spaced by \(2\pi/n\). Their center-side halfplanes therefore intersect in a regular \(n\)-gon with the stated inradius; its circumradius is the inradius divided by \(\cos(\pi/n)\).

A regular polygon's area is proportional to the square of its circumradius when its side count is fixed. Hence \(\operatorname{area}(C_n)/\operatorname{area}(P_n)=R(C_n)^2/R^2\), giving the exact probability. The asymptotic follows from \(\sin x=x+O(x^3)\) and \(\cos x=1+O(x^2)\) as \(x\to0\).

## Verification
The proof uses only the vertex-edge support geometry of a regular odd polygon, convexity of the triangles \(T_i\), the incidence of each longest diagonal with two triangles, and the exact distance from the center to a chord. The exceptional vertex-to-vertex segments and all arrangement boundaries are finite unions of line segments and do not affect area probabilities. The formula gives circumradius ratio \((3-\sqrt5)/2\) and maximum-level probability \((7-3\sqrt5)/2\) when \(n=5\), matching the pentagon specialization. A numerical overlay check for \(n=5,7,9\) was used only as a sanity check; no finite computation is used to infer the all-\(n\) proof. The argument does not provide the intermediate-level probabilities.

## Relationship to prior work
Bárány, Hug, and Schneider give a general formula for the average number of affine diameters in a planar convex body in general relative position and relate it to the area of the difference body. That result controls a mean, not the pointwise multiplicity levels or the area of the maximal-multiplicity locus. A published pentagon calculation gives the exact \(1,3,5\) distribution and the central pentagon at \(n=5\); the present statement extends the parity/support classification and maximal-locus area formula to every odd \(n\ge5\), but does not claim the full intermediate-level distribution. A separate parity result for planar bodies of constant width has different hypotheses and does not cover regular odd polygons with \(n\ge5\). Searches did not locate a prior all-odd-\(n\) maximal-locus formula; this is evidence of a gap, not proof of historical priority.

## Limitations
The theorem is restricted to regular Euclidean odd polygons. It does not establish exact area probabilities for each intermediate multiplicity, nor a corresponding formula for irregular polygons, even polygons, smooth constant-width bodies, or higher-dimensional polytopes. Historical novelty remains subject to unindexed literature risk, and no independent audit has been performed.

## References
1. Imre Bárány, Daniel Hug, and Rolf Schneider, “Affine diameters of convex bodies,” arXiv:1403.7158v1 (first public 2014-03-27), especially Theorem 1.2, equation (1.4), and Section 3's planar triangle decomposition.
2. “Affine-diameter multiplicity law for affine-regular pentagons,” public mathematical record 2026/10/11/SCOPE-affine-diameter-multiplicity-law-for-affine-regular-pentagons--79c71e04b203 (the exact pentagon case).
3. “Odd affine-diameter multiplicity almost everywhere for every planar body of constant width,” public mathematical record 2026/10/4/SCOPE-odd-affine-diameter-multiplicity-almost-everywhere-for-every-pla--bf16ddb3ccce (a related parity theorem under constant-width hypotheses).
