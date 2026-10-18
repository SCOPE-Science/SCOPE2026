# Unique octagonal-section rigidity and sharp mean along the cube–octahedron interpolation

## Finding
For each real \(1<t<3\), put
\[
K_t=[-1,1]^3\cap\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le t\}.
\]
For a unit normal \(u\in\mathbb S^2\), let \(N_t(u)\) be the number of vertices of the centered plane section \(K_t\cap u^\perp\). Outside finitely many great circles determined by vertex orthogonality, arrange the absolute coordinates of \(u\) as \(a>b>c>0\). All inequalities below are strict, and \(\mathbf1_E\) is the indicator of condition \(E\).

**Exact complete orientation classification.** If \(1<t<2\), write \(s=t-1\). Then
\[
\boxed{N_t(u)=4+2\mathbf1_{c>sb}+2\mathbf1_{b<sa}+2\mathbf1_{c<sa}.}
\]
If \(2<t<3\), write \(s=t-2\). Then
\[
\boxed{N_t(u)=4+2\mathbf1_{a<b+sc}
+2\mathbf1_{\{a>sb+c\,\text{ and }\,sa<b+c\}}
+2\mathbf1_{b>sa+c}.}
\]
At the joining value, \(\boxed{N_2(u)=8}\) for every generic direction. Each of the following values is attained on a nonempty open set of normal directions, and no other value occurs generically:
\[
\boxed{\begin{array}{c|c}
1<t<2&6,8,10\\
t=2&8\\
2<t<3&4,6,8,10
\end{array}.}
\]
In particular, the cuboctahedron \(K_2\) is the **unique member of this entire family** whose generic central sections all have the same number of vertices: every such section is an octagon.

**Sharp exact Haar mean.** For a Haar-uniform normal \(U\), the expected section vertex count is
\[
\boxed{\mathbb E N_{1+s}(U)=
\frac{24}{\pi}\arccos\frac1{1+s^2}
+\frac{12}{\pi}\arccos\frac{2s}{1+s^2},\quad 0<s<1,}
\]
and
\[
\boxed{\mathbb E N_{2+s}(U)=
\frac{12}{\pi}\arccos\frac{2-s^2}{2+s^2}
+\frac{24}{\pi}\arccos\frac{1+2s}{2+s^2},\quad 0<s<1.}
\]
The first function increases strictly from \(6\) to \(8\); the second decreases strictly from \(8\) to \(12\arccos(1/3)/\pi\). Therefore
\[
\boxed{\mathbb E N_t(U)\le8\quad(1<t<3),\qquad
\mathbb E N_t(U)=8\iff t=2.}
\]
The one-sided continuous extensions give the corresponding octahedral and cubical endpoint means.

## Assumptions and scope
All sections pass through the origin. A direction is called generic if no vertex of \(K_t\) lies in \(u^\perp\), and, when using the sorted-coordinate formulas, its three absolute coordinates are distinct and positive and no displayed indicator comparison is an equality. The excluded set has Haar measure zero. The class is the fixed three-dimensional intersection of an \(\ell_\infty\)-ball and a scaled \(\ell_1\)-ball; the assertion does not range over all centrally symmetric polytopes. A nondegenerate central section is a convex polygon, so its numbers of edges and vertices coincide.

## Proof
**1. Facet-count reduction.** All polytopes \(K_t\) with \(1<t<3\) have fourteen supporting facets: six coordinate facets \(x_i=\pm1\) and eight sign facets \(\sigma_1x_1+\sigma_2x_2+\sigma_3x_3=t\), \(\sigma_i\in\{\pm1\}\). For a generic plane through the origin, a facet contributes precisely one section edge if its vertices have both positive and negative scalar products with \(u\); otherwise it contributes none. Therefore \(N_t(u)\) equals the number of sign-changing facets. Coordinate permutations and sign changes of \(u\) preserve this number, so assume \(u=(a,b,c)\) with \(a>b>c>0\).

**2. The lower chamber.** Set \(s=t-1\in(0,1)\). A coordinate facet has the form \(x_i=\pm1\), \(|x_j|+|x_k|\le s\), a diamond. Its scalar products straddle zero precisely when \(u_i<s\max(u_j,u_k)\). Since \(a>b>c\), the six coordinate facets contribute
\[
2\mathbf1_{b<sa}+2\mathbf1_{c<sa}.
\]
Each sign facet is a hexagon with the six vertices obtained by placing the signed coordinates \((1,s,0)\) in all orders. The all-positive and all-negative facets do not meet the central plane. Group the six mixed-sign facets into three opposite pairs, indexed by the coordinate \(i\) bearing the single negative sign. On such a facet the maximum scalar product is positive (both positive coordinates can be nonzero). The minimum scalar product is negative exactly when \(u_i>s\min_{j\ne i}u_j\): indeed, the two candidate negative expressions are \(-u_i+s m\) and \(-s u_i+m\), where \(m=\min_{j\ne i}u_j\); the first can become negative sooner because \(0<s<1\). The mixed pair for the largest and middle coordinates always crosses; the pair for the smallest crosses exactly if \(c>sb\). Hence the sign facets contribute \(4+2\mathbf1_{c>sb}\), proving the first boxed classification.

**3. The upper chamber.** Set \(s=t-2\in(0,1)\). A coordinate facet is an octagon cut out by \(|x_j|\le1\), \(|x_k|\le1\), \(|x_j|+|x_k|\le1+s\). Its maximal scalar product in the tangential variables is \(\max(u_j,u_k)+s\min(u_j,u_k)\). Four coordinate facets (those indexed by the two smaller absolute normal coordinates) always cross; the remaining opposite pair crosses precisely when \(a<b+sc\). Thus their total is \(4+2\mathbf1_{a<b+sc}\).

A sign facet is now a triangle with vertices the signed permutations of \((1,1,s)\). For a mixed-sign facet with a single negative coordinate of magnitude \(r\), and the two positive magnitudes \(p\ge q\), its extreme scalar products are exactly
\[
\min=-r+sp+q,\qquad \max=-sr+p+q.
\]
Consequently that facet and its opposite are crossed precisely when \(r>sp+q\) and \(sr<p+q\). These conditions are impossible if the negative coordinate is the smallest \(c\); they reduce to \(b>sa+c\) for the middle coordinate and to \(a>sb+c\) together with \(sa<b+c\) for the largest coordinate. Adding the crossing counts gives the second boxed formula.

**4. The rectification value.** At \(t=2\), the vertex set consists of all signed permutations of \((1,1,0)\). Its six coordinate facets are diamonds \(|x_j|+|x_k|\le1\), so precisely the pairs indexed by the middle and smallest coordinates cross, contributing four. The eight sign facets are triangles with vertices the signed permutations of \((1,1,0)\). Precisely the mixed-sign opposite pairs whose exceptional coordinate is the largest or the middle one cross, contributing another four. Thus \(N_2(u)=8\) for every generic \(u\).

**5. Realization of every value.** Strict inequalities describe open spherical chambers, so it suffices to exhibit triples \((a,b,c)\) for every \(0<s<1\). In the lower chamber, choose \(\epsilon=s(1-s)/100\). The triples \((1+\epsilon,1,1-\epsilon)\), \((2/s,1,s/2)\), and \((2/s,1,(1+s)/2)\) give respectively \(6,8,10\). In the upper chamber, the triples \((10/s,1,1/2)\), \((1+\epsilon,1,1-\epsilon)\),
\[
\left(\frac{1+s^{-1}}2,1,\min\left\{\frac{(s^{-1}-1)}{4s},\frac{1-s}4,\frac14\right\}\right),
\]
and \((1+\delta,1,(1-s)/2)\), where \(\delta=s(1-s)/10\), give respectively \(4,6,8,10\). Direct substitution confirms each strict sign pattern. The formulas contain at most three indicators, so no other counts occur.

**6. Haar expectation and strict optimality.** For any two nonzero vectors \(v,w\), a Haar-uniform plane through the origin separates them with probability \(\angle(v,w)/\pi\), since the corresponding Gaussian scalar products have sign disagreement probability equal to the angle divided by \(\pi\). For a generic plane, the number of section vertices equals the number of polytope edges it crosses, hence
\[
\mathbb E N_t(U)=\frac1\pi\sum_{\{v,w\}\text{ an edge of }K_t}\arccos\frac{\langle v,w\rangle}{|v||w|}.
\]
For \(1<t<2\), the vertices are the signed permutations of \((1,s,0)\). There are 24 edges around coordinate-facet diamonds, each with endpoint cosine \(1/(1+s^2)\), and 12 edges between neighboring sign facets, each with cosine \(2s/(1+s^2)\). For \(2<t<3\), the vertices are the signed permutations of \((1,1,s)\). There are 12 coordinate-coordinate edges, each with cosine \((2-s^2)/(2+s^2)\), and 24 coordinate-sign edges, each with cosine \((1+2s)/(2+s^2)\). These two exhaustive edge classes yield the stated expectation formulas. At \(t=2\), all 24 edges have cosine \(1/2\), so the mean is eight.

Elementary differentiation gives
\[
\frac{d}{ds}\mathbb E N_{1+s}
=\frac{24}{\pi(1+s^2)}\left(\frac2{\sqrt{2+s^2}}-1\right)>0,
\]
and
\[
\frac{d}{ds}\mathbb E N_{2+s}
=\frac{24}{\pi(2+s^2)}\left(\sqrt2-\frac{2(s+2)}{\sqrt{s^2+2s+3}}\right)<0.
\]
For the second inequality, squaring the positive terms reduces it to \(s^2+6s+5>0\); the first is immediate from \(\sqrt{2+s^2}<2\). Endpoint substitution proves strict, unique maximality at \(t=2\).

## Verification
Run `python3 check_sections.py` with Python 3 and its standard library, in the same directory. The script constructs all edges independently from the coordinate-face and sign-face descriptions, verifies the 24-vertex/36-edge or 12-vertex/24-edge structures, compares the boxed chamber formulas with exact sign-crossing counts on 21,151 integer-normal/rational-parameter configurations, and checks positive-cone witnesses. It then compares the angular expectation formulas with Gaussian-direction integration at six parameter values. A successful run prints `EXACT_SECTION_CHAMBERS_OK` and `HAAR_EXPECTATION_MC_OK`. These finite checks support the algebra; the exhaustive continuous-domain classification and strict expectation inequalities are proved symbolically in the preceding sections, not inferred from sampling.

## Relationship to prior work
Birkemeyer, Brose, Brandenburg and Prün [1] develop the combinatorics and reconstruction theory of central sections, including the central section-vertex function. Their general structural statements and examples do not give the fourteen-facet chamber inequalities or sharp average for the continuous family above. De Loera, Lopez-Campos and Torres [2] investigate attainable section-vertex numbers and gap phenomena, chiefly for general polytopes and hypercubes; the inspected full-text version does not classify this interpolation. A general slice-enumeration framework [3] permits algorithms for section types but does not itself supply the present closed formulas.

Public exact results on the same cube–octahedron intersection family have determined the maximal inscribed tetrahedral-volume profile [4], its ordinary illumination number [5], and its antipodally even centro-affine facet spectrum [6]. Their conclusions concern different invariants: none provides the direction-resolved section-vertex function or the Haar-mean optimum. Known exceptional equatorial hexagonal or square sections of the cuboctahedron occur only in nongeneric vertex-containing directions and do not contradict the generic octagon theorem. An earlier unindexed special-case central-section calculation remains possible; absolute historical priority is not claimed.

## Limitations
The formulas classify **generic, central** hyperplane sections only. At nongeneric normals, planes may pass through vertices and have fewer polygon vertices; in particular, special equatorial sections of the cuboctahedron need not be octagons. The classification concerns a single 1-parameter family in dimension three, and it does not imply that the cuboctahedron is uniquely section-rigid among all convex polytopes. The formulas give the first moment of the Haar distribution, not closed probabilities for every section type away from the central parameter. Scientific priority has not been independently audited.

## References
1. A. Birkemeyer, A. E. Brose, M.-C. Brandenburg and N. Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195, first submitted 2026-09-14, https://arxiv.org/abs/2609.16195 .
2. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419, first submitted 2024-12-17, https://arxiv.org/abs/2412.12419 .
3. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The best ways to slice a polytope*, *Mathematics of Computation* 94 (2025), 1003–1042, https://arxiv.org/abs/2304.14239 .
4. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-tetrahedral-volume-profile-in-the-cube-octahedron-intersec--9ba1a511dacf .
5. *Exact illumination phase profile of the cube–octahedron intersection family*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-illumination-phase-profile-of-the-cube-octahedron-intersec--20022a556c31 .
6. *Sharp centro-affine spectral gap along the cube–octahedron interpolation*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-centro-affine-spectral-gap-along-the-cube-octahedron-inter--4397c6b224a3 .
