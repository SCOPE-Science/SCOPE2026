# Exact Haar polygon-type law for central icosahedron sections

## Finding

Let \(\varphi=(1+\sqrt5)/2\), and let \(I\subset\mathbb R^3\) be the regular icosahedron
\[
I=\operatorname{conv}\bigl\{(0,\pm1,\pm\varphi),\ (\pm1,\pm\varphi,0),\ (\pm\varphi,0,\pm1)\bigr\}.
\]
Choose \(U\) uniformly from the unit sphere and let \(N(U)\) be the number of vertices of the plane section \(I\cap U^\perp\). Then, with probability one, \(N(U)\) is either \(10\) or \(12\). Put \(\theta=\arccos(1/\sqrt5)\). Their probabilities and the mean are exactly
\[
\begin{aligned}
\mathbb P\{N(U)=12\}&=\frac{15\theta}{\pi}-5\approx0.286245735243501,\\
\mathbb P\{N(U)=10\}&=6-\frac{15\theta}{\pi}\approx0.713754264756499,\\
\mathbb E N(U)&=\frac{30\theta}{\pi}\approx10.572491470487002.
\end{aligned}
\]
More precisely, away from the measure-zero exceptional great circles, the normal sphere has exactly \(20\) geodesic triangular chambers, each producing a dodecagon, and \(12\) geodesic pentagonal chambers, each producing a decagon. The respective chamber areas on the unit sphere are \(3\theta-\pi\) and \(2\pi-5\theta\).

## Assumptions and scope

The section plane passes through the icosahedron's center, and its orientation has the rotation-invariant (Haar) probability distribution. A uniformly random oriented normal \(U\) induces the same distribution of unoriented planes because the section is unchanged under \(U\mapsto-U\). A normal is *generic* when no vertex of \(I\) lies on the section plane. The non-generic normals are contained in six great circles and have spherical measure zero. All exact distribution assertions concern this Haar model. No assertion is made about noncentral sections or arbitrary nonregular icosahedra.

## Proof

**1. The vertex signs and the edge count.** The icosahedron has \(12\) vertices in six antipodal pairs and \(30\) edges. For a generic section through its interior, every section vertex is the unique crossing of an icosahedron edge, and a polytope edge is crossed exactly when its endpoints have opposite signs of \(\langle U,\cdot\rangle\). Hence \(N(U)\) is the number of sign-changing edges.

Use the following representatives of the six antipodal vertex axes, scaled by a common positive factor \(2\):
\[
\begin{split}
W_0&=(0,2,1+\sqrt5),\quad W_1=(0,2,-1-\sqrt5),\\
W_2&=(2,1+\sqrt5,0),\quad W_3=(2,-1-\sqrt5,0),\\
W_4&=(1+\sqrt5,0,2),\quad W_5=(1+\sqrt5,0,-2).
\end{split}
\]
Every \(W_i\) has squared norm \(10+2\sqrt5\), and each pair of distinct axes has \(|\langle W_i,W_j\rangle|=2+2\sqrt5\). Consequently, all their normalized absolute inner products are \(1/\sqrt5\), and no three axes are linearly dependent. Between distinct axes, the icosahedron edges are precisely the pairs of vertices having positive inner product; the \(30\) such pairs each have angular separation \(\theta\).

**2. Exhaustive exact chamber classification.** For a mask \(m\in\{0,\ldots,63\}\), set \(s_i(m)=1\) if bit \(i\) of \(m\) is set and \(s_i(m)=-1\) otherwise. The open sign chamber for \(m\) consists of normals with \(s_i(m)\langle U,W_i\rangle>0\) for every \(i\). Because there are no triple intersections of the six bounding great circles, a vertex of the corresponding closed spherical polygon must be one of the \(30\) oriented vectors \(\pm(W_i\times W_j)\), \(i<j\). Such a vector is a vertex of the chamber exactly when it satisfies all six weak sign inequalities. Thus testing \(64\) masks and \(30\) oriented crosses each is exhaustive, not statistical sampling.

All these sign tests belong to \(\mathbb Q(\sqrt5)\). For example, the sign of \(a+b\sqrt5\) with integral coefficients is decided by the signs of \(a,b\) and, when necessary, comparison of \(a^2\) with \(5b^2\). The following table gives the complete output of the exact inequalities. Bit \(0\) refers to \(W_0\). The last column counts the section vertices by testing the \(30\) positive-inner-product edges.

| Masks (decimal) | Number of chambers | Corners per chamber | Section vertices |
| --- | ---: | ---: | ---: |
| 0, 3, 5, 6, 9, 10, 17, 23, 24, 29, 34, 39, 40, 46, 53, 54, 57, 58, 60, 63 | 20 | 3 | 12 |
| 1, 2, 7, 8, 21, 25, 38, 42, 55, 56, 61, 62 | 12 | 5 | 10 |

For each of the first \(20\) chambers, all three interior angles equal \(\theta\). For each of the remaining \(12\), all five angles equal \(\pi-\theta\). Indeed, at an intersection of the great circles indexed by \(i,j\), the interior angle is
\[
\arccos\!\left(-\frac{s_i(m)s_j(m)\langle W_i,W_j\rangle}{\lVert W_i\rVert\lVert W_j\rVert}\right).
\]
The same exhaustive sign test gives the indicated angles at every listed corner. There are precisely \(32\) chambers: six great circles in general position have \(6^2-6+2=32\) complementary regions, in agreement with the complete mask table. This proves the full generic section-type classification.

**3. The probability law from edge crossing.** If \(x,y\) are two points on a common sphere with spherical angle \(\theta\in[0,\pi]\), a uniform spherical normal \(U\) separates them with probability \(\theta/\pi\). To see this, orthogonally project \(U\) onto the two-dimensional span of \(x,y\): its argument is uniform on the circle, and the arcs giving opposite signs occupy angular fraction \(\theta/\pi\). All \(30\) icosahedron edges have angle \(\theta\). By linearity of expectation, without any assumption of independence,
\[
\mathbb E N(U)=\sum_{e\in E(I)}\mathbb P\{e\text{ is crossed}\}=\frac{30\theta}{\pi}.
\]
Since the chamber classification proves that \(N(U)\in\{10,12\}\) almost surely, writing \(p=\mathbb P\{N(U)=12\}\) yields \(\mathbb E N(U)=10+2p\). Solving gives the stated exact probabilities.

**4. Independent spherical-area identity.** Girard's spherical polygon formula gives triangular-chamber area \(3\theta-\pi\) and pentagonal-chamber area \(5(\pi-\theta)-3\pi=2\pi-5\theta\). They satisfy
\[
20(3\theta-\pi)+12(2\pi-5\theta)=4\pi.
\]
Consequently, the area proportion of dodecagon chambers independently reproduces \(\mathbb P\{N(U)=12\}=20(3\theta-\pi)/(4\pi)\).

## Verification

The included `verify_icosahedron.py` uses only the Python standard library. It enumerates every one of the \(64\) potential six-bit sign patterns and every pair of bounding great circles using exact arithmetic in \(\mathbb Z[\sqrt5]\). It verifies nonconcurrency, all \(30\) edges and their five-per-vertex degrees, all \(32\) nonempty chambers, the two full mask lists, the \(20/12\) chamber split, the \(3/5\) corner counts, all angle types and all \(10/12\) section counts. It also numerically cross-checks the two independent analytic probability formulas and the spherical-area total. Run `python3 verify_icosahedron.py` and check that its first line reads `EXACT_CHAMBER_ENUMERATION_OK`.

The infinite continuum of random normals is handled by the chamber proof and the rotational symmetry argument, not by a finite sample. The finite enumeration is exhaustive for a mathematically proved finite list of sign cases; its exact sign decisions do not use tolerances.

## Relationship to prior work

De Loera, Lopez-Campos, and Torres (arXiv:2412.12419, first public December 17, 2024) analyze the possible vertex counts of polytope sections and specifically the icosahedron's four-vertex gap; their analyzed results do not give the rotation-invariant central-section law. Jeon (arXiv:2603.00017, first public February 2, 2026) constructs one distinguished equatorial decagon and its radius but does not classify generic central sections or normal-space area fractions. Kabluchko and Seidel (arXiv:2006.09492) give expected face counts for random sections of regular simplices, cubes and crosspolytopes; their classes do not include the three-dimensional icosahedron, and their expected-value results do not yield the two-point distribution here. Frederick (2023) describes the same six-great-circle spherical icosidodecahedral tessellation, including its \(20\) triangular and \(12\) pentagonal regions. The MathPages article *N Points On Sphere all in One Hemisphere* independently tabulates the area fractions of each of these icosahedral triangular and pentagonal regions, approximately \(0.014312286762175\) and \(0.059479522063042\), respectively; the corresponding spherical-area calculations are therefore prior art. The differentiating statement here is the exact classification of which spherical sign chambers produce 10- versus 12-vertex central sections and its integration into the full Haar section-type law with an independent edge-crossing expectation.

## Limitations

The classification is almost sure: planes containing an original vertex can have different or degenerate sections, and the result does not catalog them. The theorem applies only to centered plane sections of a regular icosahedron under uniform rotation, not to offset cuts, perturbed geometries or nonuniform orientation distributions. The six-great-circle combinatorial tessellation and its two spherical-area fractions were already calculated elsewhere. The present two probabilities can be recovered from those area fractions once the chamber-to-section incidence theorem is established. Accordingly, only that incidence classification and its application to the section law are proposed as distinctive, and an equivalent formula might be implicit in older spherical-geometric or stereological work. The absence of an indexed match is not a proof of historical uniqueness.

## References

1. J. A. De Loera, G. Lopez-Campos, and A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419 (first posted December 17, 2024), https://arxiv.org/html/2412.12419v3.
2. Y. Jeon, *A Ten-Face Non-Edge-Sharing Wing Set on the Regular Icosahedron and a Decagonal Equatorial Balance*, arXiv:2603.00017 (first posted February 2, 2026), https://arxiv.org/html/2603.00017v2.
3. Z. Kabluchko and H. Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492 (first posted June 16, 2020), https://arxiv.org/html/2006.09492v2.
4. G. Frederick, *Great Circle Bow-Ties of the Icosahedron*, August 5, 2023, https://geometryofthinking.com/2023/08/05/great-circle-bow-ties-of-the-icosahedron/.
5. *N Points On Sphere all in One Hemisphere*, MathPages, https://www.mathpages.com/home/kmath327/kmath327.htm (Section on the six icosahedral great circles; date of initial publication not verified).
