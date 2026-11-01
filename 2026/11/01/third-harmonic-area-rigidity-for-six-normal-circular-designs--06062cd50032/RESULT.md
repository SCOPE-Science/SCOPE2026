# Third-harmonic area rigidity for six-normal circular designs

## Finding

Let \(U=\{z_1,\ldots,z_6\}\subset\mathbb C\) consist of six **distinct** points of modulus one, with equal weights, satisfying the circle spherical \(2\)-design equations
\[
\sum_{j=1}^{6}z_j=\sum_{j=1}^{6}z_j^2=0.
\]
For any \(\ell>0\), there is a convex hexagon \(P(U,\ell)\), unique up to translation, whose six outer edge normals are the points of \(U\) and whose six edge lengths equal \(\ell\). Define the normalized first uncontrolled complex Fourier moment
\[
\mu(U)=\left|\frac16\sum_{j=1}^{6}z_j^3\right|.
\]
Then \(0\leq\mu(U)<1\), and its **exact Euclidean area** is
\[
\boxed{\operatorname{area}(P(U,\ell))=
\frac{\sqrt3\,\ell^2}{2}\left[1+2\cos\!\left(\frac23\arcsin\mu(U)\right)\right].}
\]
The magnitude \(\mu(U)\) is a complete invariant of the normal configuration under Euclidean isometries. It vanishes precisely at a regular hexagon. Writing \(D=3\sqrt3\ell^2/2-\operatorname{area}(P(U,\ell))\), the sharp quantitative inequalities are
\[
\boxed{\frac{2\sqrt3}{9}\ell^2\mu(U)^2\le D\le\frac{\sqrt3}{2}\ell^2\mu(U)^2.}
\]
Both coefficients are best possible across six-distinct-node designs. For \(0<\mu(U)<1\), both inequalities are strict; for \(\mu(U)=0\), equality is zero on both sides. The lower coefficient is attained as a limiting ratio at the regular hexagon, and the upper coefficient is approached as two equilateral triples coalesce. Consequently, the areas of genuine six-sided realizations form precisely
\[
\left(\sqrt3\ell^2,\frac{3\sqrt3}{2}\ell^2\right].
\]
Furthermore, for distinct equal-weight circle \(2\)-designs with \(3\), \(4\), or \(5\) nodes, the nodes must be a regular polygon. Thus six nodes are the first size permitting nonregular such designs.

## Assumptions and scope

A circle \(2\)-design means an unweighted configuration of **distinct** points on \(S^1\) reproducing integrals of every real polynomial of total degree at most two. Identifying \(S^1\) with complex numbers of modulus one makes this condition exactly the vanishing of its first and second complex power sums. The six edge lengths are all one common positive number \(\ell\), not arbitrary weights. Convexity refers to a genuine planar convex polygon (adjacent edge normals are distinct). The area is ordinary unnormalized Euclidean area. Rigid motions include reflections.

The formula does not assert a classification of designs of cardinality seven or higher, unequal-weight designs, or Minkowski polytopes in dimension three. Colliding normals are excluded but legitimate as limits for sharpness.

## Proof

**1. Small-node rigidity and six-node decomposition.** For \(N\) unit-modulus nodes let \(p_j=\sum z_i^j\), and \(e_j\) be their elementary symmetric polynomials. Newton's identities yield \(e_1=p_1\) and \(2e_2=p_1^2-p_2\). Thus the design equations give \(e_1=e_2=0\). Because the nodes have modulus one,
\[
e_{N-j}=e_N\,\overline{e_j}\quad(0\le j\le N).
\]
For \(N=3,4,5\), all intermediate elementary symmetric coefficients vanish, hence the monic root polynomial is of the form \(z^N-c\), \(|c|=1\). Its distinct roots are exactly a rotated regular \(N\)-gon. No one- or two-node circle \(2\)-design exists: one node cannot have zero first power sum; for two nodes zero first sum forces antipodes and a nonzero second sum.

For \(N=6\) the same coefficient identities give
\[
\prod_{j=1}^6(z-z_j)=z^6-e_3z^3+e_6.
\]
Factoring its quadratic in \(z^3\) shows that all six nodes are the disjoint union of **two equilateral triples**, each closed under multiplication by \(\omega=e^{2\pi i/3}\). Since the nodes are distinct, the two triples have different rotations. Modulo a common rotation and relabeling, the ordered outer normal angles are exactly
\[
0,\ \beta,\ 2\pi/3,\ 2\pi/3+\beta,\ 4\pi/3,\ 4\pi/3+\beta,
\qquad 0<\beta<2\pi/3.
\]
Conversely, every such two-triple configuration satisfies both design equations.

**2. Existence and uniqueness of its equal-edge polygon.** Assign the counterclockwise oriented edge of outer normal \(z\) the vector \(i\ell z\). Summing these six vectors gives zero because \(\sum z_j=0\). Successive edge directions rotate strictly forward by gaps \(\beta\) or \(2\pi/3-\beta\), each strictly between zero and \(\pi\); in one complete traversal their turning angle is \(2\pi\). The resulting closed path is the boundary of a convex hexagon with no collinear consecutive edges. Conversely, its ordered edge vectors are forced by the normals and length, so the polygon is unique up to translation.

**3. Exact area.** Put \(u=i\ell\), \(v=i\ell e^{i\beta}\) and \(s=u+v\). The six consecutive edge vectors are
\[
u,\ v,\ \omega u,\ \omega v,\ \omega^2u,\ \omega^2v.
\]
Computing the signed area by the shoelace identity \(\frac12\sum_{i<j}\operatorname{Im}(\overline{e_i}e_j)\), or grouping the three two-edge blocks, gives
\[
A(\beta)=\frac{\sqrt3}{4}|s|^2+\frac32\operatorname{Im}(\bar u v)
=\frac{\sqrt3\ell^2}{2}(1+\cos\beta)+\frac{3\ell^2}{2}\sin\beta.
\]
Therefore
\[
A(\beta)=\frac{\sqrt3\ell^2}{2}
\left[1+2\cos(\beta-\pi/3)\right].
\]
The third moment satisfies
\[
\frac16\sum_{j=1}^6 z_j^3=\frac12e^{3i\gamma}(1+e^{3i\beta}),
\]
where \(\gamma\) is a common rotation. Thus \(\mu=|\cos(3\beta/2)|=|\sin(3(\beta-\pi/3)/2)|\). As \(|\beta-\pi/3|<\pi/3\), inversion gives
\[
|\beta-\pi/3|=\frac23\arcsin\mu.
\]
Substitution yields the stated exact area formula. The only ambiguity for fixed \(\mu\) is the pair of angles \(\beta=\pi/3\pm(2/3)\arcsin\mu\), whose normal configurations are related by a planar reflection. Hence \(\mu\) determines the configuration, and therefore its equal-edge polygon, up to rigid motion and translation.

**4. Sharp stability.** Define \(\phi=(\arcsin\mu)/3\). Then \(0\le\phi<\pi/6\), \(\mu=\sin(3\phi)\), and the exact area deficit is
\[
D=\sqrt3\ell^2(1-\cos2\phi)=2\sqrt3\ell^2\sin^2\phi.
\]
The triple-angle identity \(\sin3\phi=\sin\phi(3-4\sin^2\phi)\) consequently gives, when \(\mu>0\),
\[
\frac{D}{\ell^2\mu^2}=\frac{2\sqrt3}{(3-4\sin^2\phi)^2}.
\]
As \(\phi\) runs from zero to just below \(\pi/6\), the denominator decreases strictly from \(9\) to just above \(4\), giving exactly the claimed sharp coefficients. For \(\mu=0\), \(D=0\) directly. The area is strictly decreasing with \(\mu\); its maximum at \(\mu=0\) is the regular hexagon area \(3\sqrt3\ell^2/2\), while \(\mu\uparrow1\) gives limiting area \(\sqrt3\ell^2\), the area of an equilateral triangle of side \(2\ell\) obtained when each triple of paired normal edges collapses into one edge.

## Verification

The self-contained program `verify.py` constructs the six oriented edges directly and checks polygon closure and shoelace area against both the angle formula and the third-moment formula for 1,200 seeded parameter choices, including random rotations and positive lengths. It also checks the quadratic stability and boundary values. Run `python verify.py` with Python 3; no external dependencies are needed. Its output reports 10,919 passing checks. The proof above is universal; the finite tests do not imply it.

Independent checks of the formulas at \(\beta=\pi/3\), \(\pi/6\), and the coalescent endpoint \(\beta\downarrow0\) respectively give areas \(3\sqrt3\ell^2/2\), \((3+\sqrt3)\ell^2/2\), and the limit \(\sqrt3\ell^2\).

## Relationship to prior work

The notion of spherical design and regular polygon examples is classical (Delsarte--Goethals--Seidel; Hong). The classification of small designs is included as a proof ingredient, **not asserted to establish historical priority for circle-design classification**. Chien and Kang characterize group-orbit \(2\)-designs using representation theory. An establishes the general correspondence between a spherical design and an equal-facet-area Minkowski polytope and exact isotropic surface tensors, principally in three dimensions, with a higher-dimensional extension that includes the circle case.

The claim here concerns a further, numerical nonlinear invariant: the **entire exact Euclidean area spectrum** of the first nonrigid six-normal planar realizations, the exact correspondence with their first uncontrolled harmonic, and sharp global quadratic constants. The inspected relevant full texts do not provide those conclusions; an older equivalent presentation under equal-sided threefold-symmetric hexagons or circle cubature remains possible.

## Limitations

Historical priority is provisional. The 1982 paper of Hong and Goethals--Seidel's 1981 chapter were identified, but their full texts were not accessible in this review. The classification via Newton identities may be classical. The claimed contribution is the joined area-versus-third-moment law and its sharp stability for this natural exact-design class. The argument does not extend the numerical formula to arbitrary numbers of nodes or weights. No independent audit was performed.

## References

- Congpei An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570v1 (first public posting 2026-08-12), https://arxiv.org/abs/2608.11570 .
- Kuan-Cheng Chien and Ming-Hsuan Kang, *Spherical 2-Designs from Finite Group Orbits*, arXiv:2508.12580v1 (2025), https://arxiv.org/abs/2508.12580 .
- Yiming Hong, *On spherical t-designs in R2*, European J. Combin. 3 (1982), 255--258, https://doi.org/10.1016/S0195-6698(82)80036-X .
- J. M. Goethals and J. J. Seidel, *Cubature Formulae, Polytopes, and Spherical Designs*, in *The Geometric Vein* (1981), pp. 203--218, https://doi.org/10.1007/978-1-4612-5648-9_13 .
- P. Delsarte, J.-M. Goethals, and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363--388, https://doi.org/10.1007/BF03187604 .
