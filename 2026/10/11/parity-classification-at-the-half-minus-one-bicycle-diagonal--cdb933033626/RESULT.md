# Parity classification at the half-minus-one bicycle diagonal
## Finding
For every integer \(m\ge 3\), let \(P=V_0V_1\dots V_{2m-1}\) be a strictly convex plane bicycle \((2m,m-1)\)-gon: its sides all have one length \(s>0\), and its \((m-1)\)-diagonals all have one length \(d>0\). Then \(P\) is centrally symmetric. If its center is translated to the origin and \(X_i\) denotes the position vector of \(V_i\), then
\[
\lVert X_i\rVert^2=\lVert X_{i+2}\rVert^2
\]
for every index \(i\) modulo \(2m\).

Hence, when \(m\) is odd, all vertices lie on one circle centered at the symmetry center and the polygon is regular. When \(m\) is even, Tabachnikov's known construction supplies a one-parameter family of nonregular strictly convex examples because \(m-1\) is odd. Equivalently, along the family \(k=n/2-1\), strict convexity is globally rigid for \(n\equiv2\pmod 4\) and flexible for \(n\equiv0\pmod 4\).

## Assumptions and scope
A plane bicycle \((n,k)\)-gon is an equilateral \(n\)-gon whose \(k\)-diagonals \(V_iV_{i+k}\) all have the same length. Indices are cyclic. Strict convexity means that the exterior turning angles lie in \((0,\pi)\). The theorem concerns only \(n=2m\) and \(k=m-1\). It does not classify all bicycle polygons and, in the even-\(m\) case, it does not assert that Tabachnikov's family exhausts all nonregular examples.

## Proof
Let \(e_i=V_{i+1}-V_i\), and choose lifted edge-direction angles \(\theta_i\) so that the exterior turning angle at \(V_i\) is
\[
\alpha_i=\theta_i-\theta_{i-1}\in(0,\pi).
\]
Tabachnikov's Lemma 7.1 says that, for a convex bicycle \((n,k)\)-gon, each quadrilateral
\[
V_iV_{i+1}V_{i+k}V_{i+k+1}
\]
is an isosceles trapezoid whose parallel sides are \(V_iV_{i+k+1}\) and \(V_{i+1}V_{i+k}\).

Set \(n=2m\) and \(k=m-1\). For the trapezoid at index \(i\), let \(\phi_i\) be a direction of the base \(V_iV_{i+m}\). The two legs are the polygon edges with directions \(\theta_i\) and \(\theta_{i+m-1}\). Reflection symmetry of an isosceles trapezoid gives
\[
\theta_i+\theta_{i+m-1}\equiv2\phi_i\pmod{2\pi}.
\]
The trapezoid at index \(i+m\) has the same base line with opposite orientation and legs with directions \(\theta_{i+m}\) and \(\theta_{i-1}\), hence
\[
\theta_{i+m}+\theta_{i-1}\equiv2\phi_i\pmod{2\pi}.
\]
Subtracting gives
\[
\alpha_{i+m}\equiv\alpha_i\pmod{2\pi}.
\]
Both angles lie in \((0,\pi)\), so they are equal. Thus the turning-angle sequence has period \(m\). Since the total turn is \(2\pi\), every block of \(m\) successive turns sums to \(\pi\), and therefore
\[
\theta_{i+m}=\theta_i+\pi,
\qquad e_{i+m}=-e_i.
\]
It follows that \(V_{i+m}+V_i\) is independent of \(i\), so \(P\) is centrally symmetric. Translate the common midpoint to the origin. Then \(X_{i+m}=-X_i\), and in particular \(X_{i+m-1}=-X_{i-1}\).

Now use the common side and diagonal lengths:
\[
s=\lVert X_i-X_{i-1}\rVert,
\qquad
d=\lVert X_i-X_{i+m-1}\rVert=\lVert X_i+X_{i-1}\rVert.
\]
The parallelogram identity yields
\[
s^2+d^2=2\bigl(\lVert X_i\rVert^2+\lVert X_{i-1}\rVert^2\bigr).
\]
The left side is independent of \(i\), so subtraction at consecutive indices gives
\[
\lVert X_i\rVert^2=\lVert X_{i-2}\rVert^2.
\]
Thus the squared radii alternate between at most two values.

If \(m\) is odd, the central-symmetry identity \(\lVert X_{i+m}\rVert=\lVert X_i\rVert\) changes parity of the index, so the two alternating radii are equal. All vertices therefore lie on a circle centered at the symmetry center. Because the center lies in the interior of a strictly convex centrally symmetric polygon, each consecutive central angle belongs to \((0,\pi)\). Equal polygon sides are equal chords of this circle, so all consecutive central angles are equal. Their sum is \(2\pi\), hence each is \(\pi/m\), and \(P\) is regular.

If \(m\) is even, then \(n=2m\) is even and \(k=m-1\) is odd. Tabachnikov's Theorem 10 constructs a one-parameter family of noncongruent convex bicycle \((n,k)\)-gons for every even \(n\) and odd \(k\le n/2\). Choosing a nonregular parameter value in the strict-convexity range gives the flexible half of the dichotomy.

## Verification
The argument is analytic and uses no finite enumeration as a substitute for proof. The critical imported fact is Tabachnikov's Lemma 7.1, whose proof in the source is the congruence of two adjacent triangles followed by the convexity exclusion of the parallelogram branch. The two identities used after central symmetry are the Euclidean parallelogram identity and the monotonicity of chord length \(2R\sin(\delta/2)\) for \(0<\delta<\pi\).

Boundary checks are explicit: \(m=3\) gives the already-known bicycle \((6,2)\) rigidity; \(m=4\) lies in Tabachnikov's even-\(n\), odd-\(k\) flexible family; \(m=5\) recovers the decagon case \((10,4)\). The proof itself applies uniformly to all \(m\ge3\).

## Relationship to prior work
Tabachnikov introduced the polygonal problem and asked for which \((n,k)\) nonregular convex bicycle polygons exist. His Theorem 9 proves regularity for several arithmetic families, while Theorem 10 constructs nonregular one-parameter families when \(n\) is even and \(k\) is odd. The present result treats the different line \(n=2m\), \(k=m-1\), and shows that every member first acquires central symmetry and a two-radius structure; parity then decides between global rigidity and the known flexible construction.

Connelly and Csikós classified first-order flexibility of regular bicycle polygons. Their classification records the known deformable cases and is consistent with the present odd-\(m\) rigidity, but it is a local infinitesimal classification and does not imply the global theorem here. Tabachnikov and Tsukerman later restated the global classification problem and proved a two-circle theorem for the distinct family \((4k,k)\); their theorem does not cover \((2m,m-1)\) for \(m\ge3\).

## Limitations
The flexible even-\(m\) existence statement is prior work and is included only to make the parity classification complete. No uniqueness theorem is claimed for flexible even-\(m\) polygons. The originality search cannot exclude an unindexed elementary observation or unpublished note containing the same half-minus-one argument. The theorem assumes strict convexity; no claim is made here about degenerate convex polygons with collinear consecutive edges.

## References
1. S. Tabachnikov, *Tire track geometry: variations on a theme*, arXiv:math/0405445v1, first public version 24 May 2004; Israel J. Math. 151 (2006), 1–28, DOI 10.1007/BF02777353. See Problem 3, Lemma 7.1, Theorems 9–10, and Remark 8.3.
2. R. Connelly and B. Csikós, *Classification of first-order flexible regular bicycle polygons*, Studia Sci. Math. Hungar. 46 (2009), 37–46, DOI 10.1556/SScMath.2008.1074. The paper lists 52C25 among its primary classifications.
3. S. Tabachnikov and E. Tsukerman, *On the discrete bicycle transformation*, arXiv:1211.2345, first public version 10 November 2012. See the discussion of the bicycle-polygon classification problem and its Theorem 9.
