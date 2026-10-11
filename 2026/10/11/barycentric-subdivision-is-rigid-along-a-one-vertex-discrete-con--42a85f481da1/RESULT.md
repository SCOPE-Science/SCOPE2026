# Barycentric subdivision is rigid along a one-vertex discrete-conformal ray
## Finding
Let \(T\) be an equilateral Euclidean triangle with unit side lengths. Apply the vertex-scaling rule of discrete conformal geometry with factors \((t,0,0)\). The resulting triangle \(\widetilde T_t\) has side lengths
\[
e^{t/2},\qquad e^{t/2},\qquad 1,
\]
and is nondegenerate exactly when \(t>-\log 4\).

For each triangle, take its standard Euclidean barycentric subdivision: add the three edge midpoints and the face centroid, and give every subdivided edge its induced Euclidean length. Then the barycentrically subdivided metrics of \(T\) and \(\widetilde T_t\) are discretely conformally equivalent if and only if
\[
t=0.
\]
Consequently, the standard Euclidean barycentric subdivision does not preserve discrete conformal equivalence, even for one triangle and even along this simplest one-parameter vertex-scaling family.

## Assumptions and scope
Discrete conformal equivalence means that corresponding edge lengths \(\ell_{xy}\) and \(\widetilde\ell_{xy}\) satisfy
\[
\widetilde\ell_{xy}=e^{(U_x+U_y)/2}\ell_{xy}
\]
for real scale factors \(U_x\) attached to vertices of the common triangulation.

The subdivision considered here is specifically the standard Euclidean barycentric metric subdivision: edge barycenters are Euclidean midpoints, the face barycenter is the Euclidean centroid, and the new edge lengths are their Euclidean distances. The result does not rule out other metric assignments on the barycentric combinatorics, nor does it resolve whether some different subdivision scheme preserves discrete conformal equivalence.

## Proof
Write \(z=e^t\). Put the base of \(\widetilde T_t\) at the points \((-1/2,0)\) and \((1/2,0)\), and its third vertex at \((0,h)\), where
\[
h^2=z-\frac14.
\]
The condition \(t>-\log4\) is exactly \(h>0\).

Denote the original vertices by \(1,2,3\), the midpoint of edge \(ij\) by \(m_{ij}\), and the centroid by \(g\). Suppose the two barycentric subdivisions are discretely conformally equivalent, with new vertex factors \(U_1,U_2,U_3,U_{m_{12}},U_{m_{13}},U_{m_{23}},U_g\).

Both half-edges of the original edge \(12\) scale by \(e^{t/2}\). Therefore
\[
U_1+U_{m_{12}}=t=U_2+U_{m_{12}},
\]
so \(U_1=U_2\). The same argument on edge \(13\) gives \(U_1=U_3\). Hence
\[
U_1=U_2=U_3=c
\]
for some real \(c\), and the midpoint factors are forced to be
\[
U_{m_{12}}=U_{m_{13}}=t-c,\qquad U_{m_{23}}=-c.
\]

In the unit equilateral triangle, all three centroid-to-midpoint distances equal \(\sqrt3/6\). In \(\widetilde T_t\), direct coordinates give
\[
d(g,m_{23})=\frac h3,
\]
and
\[
d(g,m_{12})^2=\frac1{16}+\frac{h^2}{36}.
\]
Let \(R_{23}\) and \(R_{12}\) be the corresponding length ratios between the subdivided metrics. Subtracting the two vertex-scaling equations for edges \(gm_{12}\) and \(gm_{23}\) yields the necessary condition
\[
t=2\log\frac{R_{12}}{R_{23}}.
\]
Because the reference centroid-to-midpoint lengths are equal, their ratio cancels, and
\[
\left(\frac{R_{12}}{R_{23}}\right)^2
=
\frac{\frac1{16}+\frac{h^2}{36}}{\frac{h^2}{9}}
=
\frac{z+2}{4z-1}.
\]
Thus discrete conformal equivalence requires
\[
\log z=\log\frac{z+2}{4z-1},
\]
or equivalently
\[
2z^2-z-1=0.
\]
The factorization
\[
2z^2-z-1=(2z+1)(z-1)
\]
shows that the only positive solution is \(z=1\), hence \(t=0\). Conversely, when \(t=0\), the two original metrics and therefore their barycentric subdivisions coincide. This proves the equivalence.

## Verification
The proof is an exact algebraic calculation. The only geometric inputs are the Euclidean midpoint and centroid coordinates and the defining vertex-scaling equation. The critical ratio simplifies to
\[
\left(\frac{R_{12}}{R_{23}}\right)^2=\frac{z+2}{4z-1},
\]
and subtracting the required conformal exponent gives
\[
\frac{z+2}{4z-1}-z
=
-\frac{2(z-1)(2z+1)}{4z-1}.
\]
For the admissible range \(z>1/4\), the denominator is positive and \(2z+1>0\), so equality occurs exactly at \(z=1\).

## Relationship to prior work
Bobenko, Pinkall, and Springborn develop the vertex-scaling notion of discrete conformal equivalence for Euclidean triangulations and classify the subject under MSC \(52C26\). Bauer's 2015 Oberwolfach problem asks whether there exists a metric subdivision scheme preserving this equivalence and names barycentric subdivision as a particular example of a metric subdivision scheme. The present result does not solve that existence problem; it gives an exact obstruction for the standard Euclidean barycentric candidate on the smallest possible two-dimensional complex.

Targeted searches for barycentric subdivision, metric subdivision, vertex scaling, and discrete conformal equivalence did not locate a prior statement of this one-triangle rigidity calculation. The foundational full text contains no occurrence of subdivision terminology, and the 2015 problem statement presents preservation under subdivision as open.

## Limitations
This result concerns the standard Euclidean realization of barycentric subdivision. It does not exclude a modified barycentric metric rule, a subdivision with additional choices, or any other subdivision scheme. It also does not address convergence of repeated subdivision or discrete uniformization. The originality search cannot rule out an unindexed elementary observation under different terminology.

## References
1. A. I. Bobenko, U. Pinkall, B. A. Springborn, “Discrete conformal maps and ideal hyperbolic polyhedra,” arXiv:1005.2698; Geometry & Topology 19 (2015), 2155–2215, DOI 10.2140/gt.2015.19.2155.
2. U. Bauer, “Subdivision of discrete conformal structures,” Problem 6 in A. I. Bobenko, R. Kenyon, P. Schröder, *Discrete Differential Geometry*, Oberwolfach Reports 12 (2015), 661–729, DOI 10.4171/OWR/2015/13.
