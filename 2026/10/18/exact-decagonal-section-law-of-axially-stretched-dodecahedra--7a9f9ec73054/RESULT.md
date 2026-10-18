# Exact decagonal-section law of axially stretched dodecahedra

## Finding
Let \(D\) be the regular dodecahedron with vertices
\[
(\pm1,\pm1,\pm1),\qquad
(0,\pm\varphi^{-1},\pm\varphi),\quad
(\pm\varphi^{-1},\pm\varphi,0),\quad
(\pm\varphi,0,\pm\varphi^{-1}),
\quad \varphi=(1+\sqrt5)/2.
\]
For \(t>0\), put \(D_t=\operatorname{diag}(t,1,1)D\). Select a plane through the origin by taking a uniformly distributed unoriented Euclidean unit normal. Define \(p_{10}(t)\) as the probability that its intersection with \(D_t\) is a decagon. Degenerate orientations have Haar measure zero.

Write \(s=t^2-1\) and
\[
F_{a,b,c}(s)=\arccos\!\left(
-\frac{1+cs}{\sqrt{(3+as)(3+bs)}}\right).
\]
All square roots are positive, and all inverse cosines are principal values in \([0,\pi]\). Define the seven-element set of ordered triples
\[
\mathcal T=\{(1,1,1),\ (1,2-\varphi,1-\varphi),\
(1+\varphi,2-\varphi,1),\ (0,1,0),\ (0,2-\varphi,0),\
(1,1+\varphi,\varphi),\ (0,1+\varphi,0)\}.
\]
Then the **exact global law**, valid for every \(t>0\), is
\[
\boxed{\displaystyle p_{10}(t)=\frac{8\sum_{(a,b,c)\in\mathcal T}F_{a,b,c}(t^2-1)
+4F_{1,1,-1}(t^2-1)-36\pi}{4\pi}.}
\]
Moreover, the exact regular-point Taylor expansion is
\[
\boxed{\displaystyle p_{10}(t)=6-\frac{15}{\pi}\arccos\frac13
-\frac{125\sqrt2}{27648\pi}(t^2-1)^3
+O\!\left((t^2-1)^4\right),\quad t\to1.}
\]
Thus the first and second variations under axial stretching vanish, but the cubic variation is nonzero. This is a shape-sensitivity statement for a continuous affine family, not merely the classical static normal-fan count.

## Assumptions and scope
Only central planes, uniformly chosen in the ordinary Euclidean Haar sense **after** applying the stretch, are considered. The dodecahedron is centered at the origin; the stretch is along its displayed first Cartesian coordinate. Positive stretches include compression. No assertion is made about noncentral planes, other affine deformations or monotonicity for all stretches. The formula has no singularity on \(t>0\); every listed denominator is a squared norm of a nonzero transformed normal.

## Proof
The twenty displayed vertices occur in ten antipodal pairs \(\pm w_i\). The polyhedron has exactly thirty edges, joining vertex pairs at squared Euclidean distance \(8-4\varphi\). An oriented plane with normal \(u\) crosses precisely those edges whose two endpoint dot products with \(u\) have opposite signs. Hence the number of sides is constant on each open chamber of the ten great circles \(u\cdot w_i=0\). When the body is stretched, these circle normals become \(\operatorname{diag}(t,1,1)w_i\); no chamber disappears or changes its edge-crossing count.

For rigorously enumerating chambers, work throughout in the exact ordered field \(\mathbb Q(\varphi)\), representing elements as integer pairs for \(a+b\varphi\). Every triple of distinct \(w_i\) is linearly independent. Each vertex ray of the spherical sign arrangement is one of the ninety oriented cross products of two normals. An open chamber is present exactly when its admissible extreme rays jointly make every prescribed strict inequality possible. Testing all \(2^{10}=1024\) sign vectors gives exactly \(92\) open chambers: \(20\) with six crossed edges and six corners, \(60\) with eight crossed edges and three corners, and \(12\) with ten crossed edges and five corners. The standalone checker establishes these identities without numerical tolerance or unverified enumeration.

Focus on the twelve ten-sided chambers. For one of their spherical polygon corners, choose the two signed active circle normals \(v_i=\pm w_i\), \(v_j=\pm w_j\) pointing inward. The spherical interior angle after stretch is
\[
\theta_{ij}(s)=\arccos\left(-\frac{v_i\cdot v_j+s(v_i)_1(v_j)_1}
{\sqrt{(3+s(v_i)_1^2)(3+s(v_j)_1^2)}}\right).
\]
The finite exact chamber enumeration gives eight and only eight triples \(((v_i)_1^2,(v_j)_1^2,(v_i)_1(v_j)_1)\), unordered in the first two coordinates, among all sixty ten-sided chamber corners: precisely the seven triples of \(\mathcal T\), each repeated eight times, and \((1,1,-1)\), repeated four times. Furthermore all these corners have \(v_i\cdot v_j=1\). These are **integer-ring exact identities** checked directly from the normals and sign inequalities. They are restated as hard-coded expected counts in the accompanying executable, rather than assumed by it.

Girard’s spherical excess theorem says that the spherical area of a five-cornered chamber equals the sum of its five interior angles minus \(3\pi\). Summing all twelve such chambers yields a total area of \(8\sum_{\mathcal T}F+4F_{1,1,-1}-36\pi\). Dividing by the sphere area \(4\pi\) establishes the boxed formula for every \(t>0\).

For the Taylor statement, set \(s=t^2-1\) and expand each displayed cosine argument
\[
X(s)=-\frac{1+cs}{\sqrt{(3+as)(3+bs)}}
= -\frac13+X_1s+X_2s^2+X_3s^3+O(s^4).
\]
With \(A=(a+b)/3\), \(B=ab/9\), let \(Q_1=-A/2\), \(Q_2=-B/2+3A^2/8\) and \(Q_3=3AB/4-5A^3/16\). Then
\[
X_1=-\frac{c+Q_1}{3},\quad X_2=-\frac{cQ_1+Q_2}{3},\quad
X_3=-\frac{cQ_2+Q_3}{3}.
\]
For \(f(X)=\arccos X\), the derivatives at \(X=-1/3\) are
\[
f'=-\frac{3\sqrt2}{4},\quad f''=\frac{9\sqrt2}{32},\quad f'''=-\frac{297\sqrt2}{256}.
\]
The coefficients of \(s,s^2,s^3\) in each angle are consequently
\[
 f'X_1,\qquad f'X_2+\tfrac12f''X_1^2,\qquad
 f'X_3+f''X_1X_2+\tfrac16f'''X_1^3.
\]
Substituting the eight displayed triples and multiplicities, exact arithmetic in \(\mathbb Q(\sqrt5,\sqrt2)\) gives their weighted sums \(0,0,-125\sqrt2/6912\). Dividing by \(4\pi\) proves the cubic coefficient. At \(s=0\), all sixty interior angles equal \(\arccos(-1/3)\), giving the stated constant term. Analyticity near \(s=0\) proves the remainder.

## Verification
Run `python verify_affine_dodeca.py` with Python 3 and SymPy. The script independently reconstructs all vertices, thirty edges, ten antipodal representative normals, ninety pair-intersection rays, every sign chamber and the eight corner classes by exact arithmetic in \(\mathbb Z[\varphi]\). It then checks the two vanishing Taylor coefficients and exact nonzero third coefficient using symbolic arithmetic, and reports four numerical spot tests. The proof above explains why the finite exact checks cover every chamber, rather than treating floating-point experiments as a substitute for proof.

As an additional diagnostic, independent random-normal simulations with eighty thousand samples at each of four stretch factors matched the formula within two standard deviations (this finite simulation is not used in the proof).

## Relationship to prior work
The rhombic enneacontahedron, known to arise from the ten diameters of a regular dodecahedron, encodes the **static** combinatorics of the same ten-circle arrangement (MathWorld, citing Towle 1996 and Ball–Coxeter 1987). Consequently the static counts of chamber types and the evaluation at \(t=1\) are not presented as independently new. The result claimed here is the *entire anisotropic, Euclidean-Haar, one-parameter decagon probability* and its nonzero cubic response. A published result on random central **icosahedron** sections concerns a different polytope and polygon types. Published random conical tessellation work studies a random hyperplane ensemble, not this fixed dodecahedral normal arrangement. These comparisons do not prove exhaustive historical priority.

## Limitations
The analysis is limited to the decagon probability, not a complete simultaneous formula for hexagon and octagon probabilities or arbitrary linear transformations. The result involves no unrestricted extrema. The full text of one relevant secondary published-result database entry could not be accessed; an earlier unindexed affine probability formula could still exist. Independent mathematical assessment has not been performed.

## References
- E. W. Weisstein, *Rhombic Enneacontahedron*, MathWorld, https://mathworld.wolfram.com/RhombicEnneacontahedron.html (background ten-diameter construction and earlier bibliography).
- J. O’Rourke, *Regular cross-sections of a dodecahedron*, MathOverflow, 30 March 2014 (section-existence background).
- D. Hug and R. Schneider, *Random Conical Tessellations*, arXiv:1508.07768, first posted 31 August 2015 (related spherical random geometry).
- J. Kim, V. Yaskin and A. Zvavitch, *The geometry of p-convex intersection bodies*, arXiv:1512.07289, first posted 22 December 2015 (broader section-geometric context).
