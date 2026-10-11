# Regular odd polygons have exactly as many convexity points as vertices
## Finding
Let \(P_n\) be a regular Euclidean polygon with odd \(n=2m+1\ge3\), circumradius \(R>0\), and cyclic vertices \(v_0,\ldots,v_{n-1}\). Call \(z\in\mathbb R^2\) a convexity point if
\[
P_n\cup(2z-P_n)
\]
is convex. Then the complete set of convexity points is
\[
\left\{c_j=\frac{v_j+v_{j+m+1}}2:0\le j<n\right\}.
\]
Thus \(P_n\) has exactly \(n\) convexity points. The pairs \(\{v_j,v_{j+m+1}\}\) are precisely the \(n\) longest diagonals of an odd regular polygon, so the convexity points are exactly their midpoints.

Moreover, the \(c_j\) form a regular \(n\)-gon with circumradius
\[
R\sin\frac{\pi}{2n}.
\]
Hence every odd integer \(n\ge3\) is realized as the finite number of convexity points of a planar convex body.

## Assumptions and scope
Indices are taken modulo \(n\). For a convex body \(K\) and a unit vector \(u\), write \(H(K,u)\) for the support line, \(F(K,u)\) for the support face, \(M_K(u)\) for the line halfway between \(H(K,u)\) and \(H(K,-u)\), and
\[
Z_K(u)=\frac12\bigl(F(K,u)+F(K,-u)\bigr)
\]
for the corresponding middle set.

For odd \(n\), a regular \(n\)-gon has no pair of parallel edges. The proof uses Schneider's characterization: for such a body, \(z\) is a convexity point if and only if every middle line through \(z\) has its middle set containing \(z\). It also uses the published fact that every exposed point of the convex hull of the middle hedgehog is a convexity point.

No statement about even regular polygons is included, because their parallel opposite edges place them outside the no-parallel-edge characterization used below.

## Proof
Identify the plane with \(\mathbb C\), put \(\zeta=e^{2\pi i/n}\), and take
\[
v_j=R\zeta^j.
\]
For the edge \(E_j=[v_j,v_{j+1}]\), the opposite supporting face is the single vertex \(v_{j+m+1}\). Hence its middle set is
\[
Z_j=\frac12(E_j+v_{j+m+1})
   =[c_j,c_{j+m+1}],
\]
where
\[
c_j=\frac{v_j+v_{j+m+1}}2.
\]
Schneider's polygonal description of the middle hedgehog says that all its points lie in the union of these edge middle sets. Therefore the convex hull \(A_{P_n}\) of the middle hedgehog is
\[
A_{P_n}=\operatorname{conv}\{c_0,\ldots,c_{n-1}\}.
\]
The points \(c_j\) are distinct and satisfy
\[
|c_j|
=\frac R2\left|1+e^{2\pi i(m+1)/n}\right|
=R\sin\frac{\pi}{2n}.
\]
They differ by successive rotations through \(2\pi/n\), so they are the vertices of a regular \(n\)-gon. In particular each \(c_j\) is exposed in \(A_{P_n}\). By Schneider's exposed-point lemma, every \(c_j\) is a convexity point of \(P_n\).

It remains to exclude all other points. Let \(z\) be a convexity point. Parametrize unit normals by
\[
u(\varphi)=(\cos\varphi,\sin\varphi)
\]
and set
\[
p(\varphi)=\frac12\bigl(h_{P_n}(u(\varphi))-h_{P_n}(-u(\varphi))\bigr),
\qquad
q_z(\varphi)=\langle z,u(\varphi)\rangle-p(\varphi).
\]
Then \(q_z\) is continuous and
\[
q_z(\varphi+\pi)=-q_z(\varphi).
\]
Hence \(q_z\) has a zero. A zero is exactly a middle line through \(z\). Since \(z\) is a convexity point, Schneider's characterization forces \(z\in Z_{P_n}(u(\varphi))\) at every zero. In particular \(z\) lies on the middle hedgehog.

Assume now that \(z\ne c_j\) for every \(j\). Whenever \(z\in Z_{P_n}(u(\varphi_0))\), the middle set cannot be a singleton, because all singleton middle sets are corners \(c_j\). Thus \(Z_{P_n}(u(\varphi_0))\) is one of the nondegenerate segments \([c_j,c_{j+m+1}]\), and \(z\) lies in its relative interior.

At such an edge-normal angle, Schneider's one-sided derivative identities give the following local behavior. If the segment endpoints are ordered as \(s,t\) with \(t-s\) pointing in the positive tangent direction \(u'(\varphi_0)\), then
\[
q'_{z,-}(\varphi_0)=\langle z-s,u'(\varphi_0)\rangle>0,
\qquad
q'_{z,+}(\varphi_0)=\langle z-t,u'(\varphi_0)\rangle<0.
\]
With the opposite orientation the signs are reversed. Thus every zero at which \(z\) belongs to the relative interior of a middle segment is a strict local extremum of \(q_z\), and in particular is not a sign-changing zero.

Choose one zero \(\varphi_0\). If necessary replace it by \(\varphi_0+\pi\) so that it is a strict local maximum. Then \(q_z<0\) immediately to the right of \(\varphi_0\). By anti-periodicity, \(\varphi_0+\pi\) is a strict local minimum, so \(q_z>0\) immediately to its left. The intermediate value theorem therefore supplies a sign-changing zero in \((\varphi_0,\varphi_0+\pi)\). Such a zero cannot have \(z\) in a middle-set segment, because those zeros are strict local extrema, and it cannot have a singleton middle set because \(z\ne c_j\). Thus this middle line passes through \(z\) while its middle set does not contain \(z\), contradicting Schneider's characterization of convexity points.

Therefore every convexity point equals one of the \(c_j\), proving the exact count.

## Verification
The proof is symbolic and does not depend on finite enumeration. The supplied `verify.py` is only an indexing and geometry sanity check. For odd \(n\) from \(3\) through \(101\), it verifies numerically that the endpoint identity
\[
\frac{v_{j+1}+v_{j+m+1}}2=c_{j+m+1}
\]
holds, that all \(c_j\) have radius \(R\sin(\pi/(2n))\), and that the middle-set segments have the asserted endpoints. These finite checks are not used as proof of the all-\(n\) theorem.

## Relationship to prior work
Schneider introduced the term convexity point and proved in 2015 that every non-centrally-symmetric planar convex body has three affinely independent convexity points. The same paper gives the exact middle-line characterization used here and proves that exposed points of the auxiliary middle-set hull are convexity points.

In 2016 Schneider introduced the middle-hedgehog viewpoint, observed that a triangle and a Reuleaux triangle have precisely three convexity points, and proved that a typical planar convex body has infinitely many. For polygons without parallel edges, that paper describes the middle hedgehog as a polygonal curve built from the edge middle sets and distinguishes weak and strong corners. It does not state a finite-cardinality classification for regular odd polygons.

Targeted searches for regular pentagons, regular odd polygons, exact finite counts, longest-diagonal midpoints, middle hedgehogs, and equivalent reflection-union formulations did not locate a statement that regular odd \(n\)-gons have exactly \(n\) convexity points. The closest indexed research results concern different regular-polygon reflection measures or a separate quadrilateral classification.

## Limitations
The theorem treats regular odd polygons only. It does not classify convexity points of arbitrary odd polygons, and it does not address regular even polygons, whose parallel opposite edges require a different analysis.

The originality search cannot exclude an unindexed observation in notes, exercises, or correspondence following Schneider's papers. The proof does not claim that odd finite cardinalities are the only possible finite cardinalities for general planar convex bodies.

## References
1. R. Schneider, *Reflections of planar convex bodies*, arXiv:1504.00541, first public version 2015-04-02. Relevant items: Lemma 2, the definition of \(A_K\), and Lemma 6.
2. R. Schneider, *The middle hedgehog of a planar convex body*, arXiv:1607.03014, first public version 2016-07-11; later DOI: 10.1007/s13366-016-0315-5. Relevant items: Theorems 1--3, Lemma 2.1, and the polygonal middle-hedgehog discussion in Section 3.
