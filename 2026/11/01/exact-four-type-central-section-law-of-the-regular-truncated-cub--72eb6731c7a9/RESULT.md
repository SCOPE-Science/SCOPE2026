# Exact four-type central-section law of the regular truncated cube

## Finding
Let \(P\) be the regular Euclidean truncated cube whose vertices are all sign changes and coordinate permutations of \((1,1,\sqrt2-1)\). Let \(U\) be a Haar-uniform unoriented plane normal, and let \(N\) be the number of sides of the polygon \(P\cap U^\perp\). Almost surely \(N\in\{4,6,8,10\}\), and each value has positive probability. The exact probabilities are given by the elementary spherical-triangle formulas below:

Write \(t=\sqrt2-1\), and define planar points
\[
 O=(0,0),\quad P_0=(t,0),\quad Q=(t/2,t/2),\quad R=(2t,t),
 \quad S=(1/\sqrt2,1/\sqrt2),\quad T=(1,1-t),\quad V=(1,0),\quad W=(1,1).
\]
For planar points \(I,J,K\), write \(\mathbf i=(1,I_1,I_2)\), \(\mathbf j=(1,J_1,J_2)\), and \(\mathbf k=(1,K_1,K_2)\), and set
\[
 \Omega(I,J,K)=2\arctan\left(
 \frac{|\det(\mathbf i,\mathbf j,\mathbf k)|}
 {\|\mathbf i\|\|\mathbf j\|\|\mathbf k\|+(\mathbf i\cdot\mathbf j)\|\mathbf k\|+(\mathbf j\cdot\mathbf k)\|\mathbf i\|+(\mathbf k\cdot\mathbf i)\|\mathbf j\|}
 \right).
\]
Then the **complete exact distribution** is
\[
 \begin{aligned}
 \Pr(N=4)&=\frac{12}{\pi}\Omega(O,P_0,Q),\\
 \Pr(N=6)&=\frac{12}{\pi}\big[\Omega(P_0,R,S)+\Omega(P_0,S,Q)+\Omega(S,T,W)\big],\\
 \Pr(N=8)&=\frac{12}{\pi}\big[\Omega(P_0,V,R)+\Omega(R,T,S)\big],\\
 \Pr(N=10)&=\frac{12}{\pi}\Omega(R,V,T).
 \end{aligned}
\]
Their decimal approximations are respectively \(0.15105269327335\), \(0.50022728825240\), \(0.28139735629611\), and \(0.06732266217814\). In particular, the decagonal sections occur with strictly positive probability, whereas the centrally symmetric truncated cube has no generic central section with more than ten vertices.

## Assumptions and scope
Plane normals are uniform on the unit sphere modulo antipodes. A plane is *generic* if none of the twenty-four vertices of \(P\) lies in the plane. This excludes finitely many great circles and hence a probability-zero set. Every other section is a two-dimensional convex polygon, and every section side is the intersection with the relative interior of one facet of \(P\). The theorem concerns center-passing planes, not all affine sections or a uniform distribution on plane offsets.

## Proof
The choice \(t=\sqrt2-1\) makes the surviving cube-face edges and newly truncated triangle edges equal: \(2t=\sqrt2(1-t)\). The faces are six octagons in coordinate planes \(x_i=\pm1\), and eight equilateral triangles in planes \(\pm x_1\pm x_2\pm x_3=2+t\). For any generic plane through the origin, a facet contributes one section side precisely when its vertices have both positive and negative dot products with the normal.

By signed-permutation invariance we may order the absolute normal coordinates as \(a>b>c>0\). Four coordinate-octagon facets always contribute. The other two contribute if and only if \(a<b+tc\). Among the four antipodal pairs of triangular facets, one pair contributes if and only if \(tb+c<a<(b+c)/t\), and another pair contributes if and only if \(b>ta+c\); the remaining two pairs never contribute. For example, on a representative triangle with vertex signs \((+,-,-)\), the three signed dot products are \(ta-b-c\), \(a-tb-c\), and \(a-b-tc\). Since \(b\ge c\), the minimum and maximum are the first two displayed values. The remaining sign cases follow by the same explicit comparison, or by antipodal symmetry. Therefore the number of sides obeys, for every generic normal,
\[
 N=4+2\mathbf1_{\{a<b+tc\}}+2\mathbf1_{\{tb+c<a<(b+c)/t\}}+2\mathbf1_{\{b>ta+c\}}.
\]

Normalize \((a,b,c)\) to the positive ray \((1,y,z)\), with \(0<z<y<1\). Four linear half-plane tests partition the triangular parameter chamber:
\[
 L_1=y+tz-1,\quad L_2=1-ty-z,\quad L_3=y+z-t,\quad L_4=y-z-t.
\]
The indicators in the preceding formula are \(\mathbf1_{\{L_1>0\}}\), \(\mathbf1_{\{L_2>0,L_3>0\}}\), and \(\mathbf1_{\{L_4>0\}}\). Exact intersection of these four lines with \(0\le z\le y\le1\) yields precisely six nonempty two-dimensional chambers, listed below in counterclockwise vertex order, with their side counts:

| Chamber polygon | Side count |
| --- | ---: |
| \(O,P_0,Q\) | 4 |
| \(P_0,R,S,Q\) | 6 |
| \(S,T,W\) | 6 |
| \(P_0,V,R\) | 8 |
| \(R,T,S\) | 8 |
| \(R,V,T\) | 10 |

The six polygons form a partition of \(0\le z\le y\le1\) up to edges. Their ordinary Euclidean areas sum to \(1/2\). The spherical area of the cone over each triangular cell is exactly \(\Omega\) as displayed above; triangulate the single quadrilateral from \(P_0\). Since the sphere has forty-eight congruent signed-permutation chambers of area \(\pi/12\), the probability of any union of cells equals \(12/\pi\) times its solid angle in one chamber. The resulting four formulas follow. Every listed polygon has positive area, and no additional generic section counts occur. This completes the proof.

## Verification
Two reproducible, distinct finite checks accompany this proof. `verification_partition.py` enumerates all sign cells using symbolic expressions over \(\mathbb Q(\sqrt2)\), computes exact cone solid-angle expressions, and checks numerical normalization. `verification_faces.py` independently constructs the entire twenty-four-vertex, fourteen-facet polyhedron, tests vertex-sign separation on every facet for forty thousand deterministic pseudorandom directions, and compares each result with the closed indicator formula; it found zero mismatches. The exact proof, not sampling, establishes exhaustiveness for all generic normals. Run both with Python, SymPy and NumPy installed.

## Relationship to prior work
The 2009 study of Platonic and Archimedean solids by Torquato and Jiao tabulates truncated-cube geometric data but addresses polyhedral packing rather than this angular section law. De Loera, Lopez-Campos and Torres (2024) study possible vertex counts of affine polytope sections and slicing algorithms; their general results do not give the distribution of the central sections of this specified solid. Other available exact section laws concern cubes, regular icosahedra, and truncated octahedra; these are different polytopes and do not imply the present four-class law by specialization. General finite hyperplane arrangement methods can in principle compute the law, but their existence alone does not identify these four probabilities or the six exact regions.

## Limitations
This is a statement about center-passing Euclidean sections, not random affine offsets, section areas, or nonregular truncation parameters. The explicit numerical values are derived from elementary exact arctangent expressions, without a claim that they simplify to a shorter radical formula. A comprehensive historical-priority audit of older stereological tables has not been completed, so the result is not asserted to be historically first.

## References
1. S. Torquato and Y. Jiao, *Dense Packings of Polyhedra: Platonic and Archimedean Solids*, first public arXiv version September 4, 2009, arXiv:0909.0940, https://arxiv.org/abs/0909.0940 .
2. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, first public arXiv version December 17, 2024, arXiv:2412.12419, https://arxiv.org/abs/2412.12419 .
