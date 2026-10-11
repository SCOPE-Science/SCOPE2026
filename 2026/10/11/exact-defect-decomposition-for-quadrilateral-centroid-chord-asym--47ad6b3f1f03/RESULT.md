# Exact defect decomposition for quadrilateral centroid-chord asymmetry
## Finding
Let \(Q\) be a strictly convex quadrilateral and \(G\) its area centroid. A centroid-bisecting chord is a chord whose midpoint is \(G\). If such a chord cuts the area of \(Q\) in proportions \(\alpha\) and \(1-\alpha\), use the convention \(0<\alpha\le 1/2\), and define
\[
\rho(Q)=\frac{\alpha_{\min}(Q)}{\alpha_{\max}(Q)}.
\]

Up to an invertible affine map and a dihedral relabeling of the vertices, every strictly convex quadrilateral can be written
\[
A=(-1,0),\qquad B=(0,1),\qquad C=(x,0),\qquad D=(0,-y),
\]
with \(x\ge y\ge1\). Define the affine diagonal-asymmetry coordinates
\[
u=\frac{x-1}{x+1},\qquad v=\frac{y-1}{y+1},\qquad 0\le v\le u<1.
\]
The parallelogram is the removable endpoint \((u,v)=(0,0)\), where \(\rho(Q)=1\). For every non-parallelogram put
\[
\Delta(u,v)=u^2v^2-u^2-uv+9u-v^2+9v.
\]
Then
\[
\rho(Q)=\frac{(u+v)(3+u+v-uv)(3+u-v+uv)}{(1+u)\Delta(u,v)}.
\]
Moreover the deficit from the sharp quadrilateral value has the exact decomposition
\[
\rho(Q)-\frac{24}{25}
=
\frac{(7u-3)^2}{25(9-u)(1+u)}
+
\frac{v^2(1-u)B(u,v)}{(9-u)(1+u)\Delta(u,v)},
\]
where
\[
B(u,v)=17u^2+10uv+6u+9-u^2v-9v.
\]
Thus, at fixed \(u\), moving the second diagonal away from bisection can only increase \(\rho\), and equality in the global bound occurs exactly at \((u,v)=(3/7,0)\). In the one-parameter family \(\operatorname{conv}\{(0,0),(1,0),(0,1),(c,c)\}\) this is \(c=7/4\).

## Assumptions and scope
The statement concerns the area centroid of a planar strictly convex quadrilateral and the smaller area fractions of all chords bisected by that centroid. The quantity \(\rho\) is affine invariant, so diagonal intersection coordinates lose no geometry. Swapping the two endpoints of either diagonal replaces one diagonal ratio by its reciprocal, and swapping the diagonals exchanges the two ratios; hence the normalization \(x\ge y\ge1\) is always possible.

The result does not claim a new value for the global quadrilateral minimum \(24/25\): that value and its equality class were reported by Chevallier, Fruchard, and Vîlcu using Maple. The new claim is the explicit formula on the full two-dimensional affine moduli space, the exact positive defect splitting, and the consequent one-coordinate monotonic reduction.

## Proof
The centroid in the normalized coordinates is
\[
G=\left(\frac{x-1}{3},\frac{1-y}{3}\right).
\]
A chord with endpoints \(P,Q\in\partial Q\) is bisected by \(G\) exactly when \(P+Q=2G\). Solving this equation on pairs of polygon edges shows that two centroid-bisecting chords occur throughout the normalized chamber: one joins \(BC\) to \(CD\), and one joins \(BC\) to \(DA\). The third joins \(AB\) to \(CD\) when
\[
v\le \frac{u}{u+2},
\]
and joins \(CD\) to \(DA\) when the reverse inequality holds. At equality the two descriptions give the same chord through a vertex. Hence there are exactly three distinct centroid-bisecting chords away from the parallelogram endpoint.

A direct shoelace calculation gives the smaller area fraction of the \(BC\)-to-\(CD\) chord as
\[
a_{12}=\frac{(3+u+v-uv)(3+u-v+uv)}{18(1+u)},
\]
and that of the \(BC\)-to-\(DA\) chord as
\[
a_{13}=\frac{\Delta(u,v)}{18(u+v)}.
\]
For \(v\le u/(u+2)\), the third value is
\[
a_{02}=\frac{u^2v^2-u^2+uv+9u-v^2-9v}{18(u-v)},
\]
with the removable boundary values taken by continuity. For \(v\ge u/(u+2)\), it is
\[
a_{23}=\frac{(3+u+v-uv)(3-u+v+uv)}{18(1+v)}.
\]

The extreme values are always \(a_{12}\) and \(a_{13}\). In the first chamber,
\[
a_{13}-a_{02}=\frac{v^3(1-u)(1+u)}{9(u-v)(u+v)}\ge0.
\]
Also
\[
a_{02}-a_{12}=\frac{(u-1)(v+1)E(u,v)}{18(u+1)(u-v)},
\]
where \(E(u,v)=2u^2v-2u^2-uv^2+2uv+v^2\). For fixed \(u\), the polynomial \(E\) is increasing in \(v\), and at \(v=u/(u+2)\) it equals
\[
-\frac{3u^2(u+1)}{(u+2)^2}<0,
\]
so \(a_{02}\ge a_{12}\). In the second chamber,
\[
a_{23}-a_{12}=
-\frac{(u-1)(u-v)(v-1)(uv-u-v-3)}{18(u+1)(v+1)}\ge0.
\]
Finally,
\[
a_{13}-a_{23}=
\frac{(u-1)(v-1)F(u,v)}{18(u+v)(v+1)},
\]
where \(F(u,v)=u^2v-u^2+2uv^2+2uv+2v^2\). The function \(F\) is increasing in \(v\), and at the chamber boundary it equals
\[
\frac{2u^2(u+1)}{(u+2)^2}>0.
\]
Therefore \(\alpha_{\min}=a_{12}\) and \(\alpha_{\max}=a_{13}\) throughout the normalized moduli chamber. Dividing these two expressions gives the formula for \(\rho\).

The defect identity follows by exact rational simplification. Its denominators are positive: for \(0\le v\le u<1\),
\[
\Delta(u,v)=9u+9v-u^2-uv-v^2+u^2v^2>0
\]
whenever \(u>0\). Also
\[
B(u,v)\ge 9-3u+17u^2-u^3>0.
\]
Hence both defect terms are nonnegative. The second vanishes exactly when \(v=0\), and the first then vanishes exactly when \(u=3/7\). This proves the stated rigidity and monotonic reduction.

## Verification
The accompanying `verify.py` reconstructs the normalized quadrilateral from its vertices, solves the midpoint equations for the four relevant edge pairs, recomputes the directed subpolygon areas by the shoelace formula, and checks every displayed rational identity symbolically. Its run on the packaged file returns `VERIFY_OK`.

The proof itself is algebraic and does not depend on numerical sampling. The symbolic replay verifies identities only; the sign arguments establishing the valid moduli chambers and positivity are given above.

## Relationship to prior work
Chevallier, Fruchard, and Vîlcu introduced the centroid-chord quotient \(\alpha_{\min}(K)/\alpha_{\max}(K)\) as an affine asymmetry measure and reported that, among quadrilaterals, its minimum is \(24/25\), attained precisely in their family at \(c=7/4\). Their text explicitly attributes the quadrilateral minimization to Maple and displays only the one-parameter formulas needed for their example. It does not state a two-parameter affine-moduli formula, a monotonicity principle in diagonal imbalance, or an exact defect decomposition.

The formula above recovers their scalar extremum analytically and strengthens it by resolving the full affine moduli into two nonnegative defect contributions. Exact-form and alias searches did not locate a published statement implying this decomposition.

## Limitations
The theorem is specific to quadrilaterals. It does not address the source paper's broader problem of minimizing the centroid-chord quotient over all planar convex bodies. The diagonal coordinates are affine invariants only after the stated endpoint and diagonal relabelings; they should not be interpreted as Euclidean shape parameters.

The public literature search cannot exclude an unindexed note or an unpublished symbolic worksheet containing the same two-parameter simplification. The closest primary source establishes the scalar extremum but not the stronger formula claimed here.

## References
1. Nicolas Chevallier, Augustin Fruchard, Costin Vîlcu, *Envelopes of \(\alpha\)-sections*, arXiv:1509.02084v1, first posted 2015-09-07; later published in *Convexity and Discrete Geometry Including Graph Theory*, Springer Proceedings in Mathematics & Statistics 148.
2. U. Viet, *Umkehrung eines Satzes von H. Brunn über Mittelpunktseibereiche*, Math.-Phys. Semesterber. 5 (1956), 141--142, cited by [1] for existence of at least three centroid-bisecting chords.
