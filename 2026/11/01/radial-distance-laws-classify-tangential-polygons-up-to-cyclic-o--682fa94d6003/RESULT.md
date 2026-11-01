# Radial-distance laws classify tangential polygons up to cyclic ordering

## Finding
Let \(P\) be any nondegenerate convex Euclidean polygon all of whose \(n\ge3\) sides touch one inscribed circle, with incenter \(O\), inradius \(r>0\), and interior angles \(\theta_1,\ldots,\theta_n\) in cyclic order. Put
\[
 g_i=\frac{\pi-\theta_i}{2}\in(0,\pi/2),\qquad u_i=\tan g_i,\qquad T=\sum_{i=1}^n u_i.
\]
Then \(\sum_i g_i=\pi\), \(\operatorname{area}(P)=r^2T\), and \(\operatorname{perimeter}(P)=2rT\).

Choose \(Y\) uniformly by arclength from \(\partial P\), and independently choose \(X\) uniformly by area from \(P\). Their radial-distance laws, measured from \(O\), admit the following complete formulas.

**Boundary law.** For \(Z=\sqrt{(|Y-O|/r)^2-1}\) and every \(z\ge0\),
\[
 \Pr\{Z>z\}=\frac1T\sum_{i=1}^n (u_i-z)_+,
 \qquad (a)_+=\max\{a,0\}.
\]
Thus this transformed radial law is an exact piecewise-linear spline, with knots at the distinct \(u_i\) and derivative jumps equal to their multiplicities divided by \(T\).

**Interior law.** The area-sampling radial variable \(R=|X-O|\) satisfies
\[
 R\ \stackrel{\mathrm d}=\ \sqrt{U}\,|Y-O|,
 \qquad U\sim\operatorname{Uniform}[0,1],
\]
where \(U\) and \(Y\) are independent. Its cumulative distribution \(F(t)=\Pr\{R\le t\}\) obeys
\[
 F(t)=\frac{\pi t^2}{r^2T}\quad(0\le t\le r),
\]
and, for \(t>r\),
\[
 \boxed{F'(t)=\frac{2t}{r^2T}\sum_{i=1}^n
 \left(g_i-\arccos\frac rt\right)_+.}
\]
The derivative is continuous across every vertex-radius threshold; the expression is zero once \(t\ge r\sec(\max_i g_i)\).

**Exact inverse classification.** Either entire unnormalized radial-distance law, the law of \(|Y-O|\) or the law of \(|X-O|\), independently determines \(r\), \(n\), and the unordered multiset \(\{g_1,\ldots,g_n\}\), with multiplicities. Two tangential polygons have the same law for either sampling scheme if and only if their inradii and these multisets agree. The law does not retain cyclic order. At fixed data the Euclidean congruence classes are precisely the dihedral-ordering orbits of the multiset. When the \(n\) gaps are pairwise distinct, exactly
\[
 \boxed{\frac{(n-1)!}{2}}
\]
noncongruent tangential polygons share either law. In particular, the first generic nonuniqueness occurs already for quadrilaterals, with three classes.

## Assumptions and scope
A polygon has nonempty interior, exactly \(n\) genuine sides, and no zero exterior angles or redundant collinear vertices. Tangential means all supporting edge lines are tangent to the same interior circle; its center is unique. Normalized boundary arclength and normalized planar Lebesgue area are the two sampling measures. Distribution equality is equality of full Borel probability laws, not a finite histogram or selected moments. Convexity implies each exterior angle \(2g_i\) lies in \((0,\pi)\), and the turning-angle sum is \(2\pi\).

Conversely, every positive list \(g_1,\ldots,g_n\) with \(g_i<\pi/2\) and \(\sum_i g_i=\pi\), in any cyclic order, determines (up to rotation and translation) a convex polygon circumscribed about the radius-\(r\) circle: take outward unit normals whose successive rotations are \(2g_i\) and intersect their supporting halfplanes at distance \(r\). Every supporting side is nondegenerate because the normals are distinct and consecutive gaps are less than \(\pi\); boundedness follows because no closed semicircle contains all normals.

## Proof
**1. Tangency geometry.** The intersection of consecutive tangent lines with outward-normal gap \(2g_i\) lies at distance \(r\sec g_i\) from \(O\). Both tangent segments from this vertex to the incircle have length \(r\tan g_i=ru_i\). The side whose outward normal lies between consecutive vertices therefore has length \(r(u_{i-1}+u_i)\). Summing proves the perimeter formula. Triangulation into the triangles from \(O\) to each side proves the area formula.

**2. Boundary radial law.** On a side, write a boundary point as \(Y=O+rn_i+s\tau_i\), where \(n_i\) is the outward unit normal and \(\tau_i\) its counterclockwise perpendicular. Then \(|Y-O|^2=r^2+s^2\) and the signed coordinate \(s\) ranges from \(-ru_{i-1}\) to \(ru_i\). The arclength with \(\sqrt{(|Y-O|/r)^2-1}>z\) equals
\[
 r(u_{i-1}-z)_+ +r(u_i-z)_+.
\]
Summing over the sides yields \(2r\sum_i(u_i-z)_+\); division by the total perimeter \(2rT\) gives the boundary law, including repeated knots and every endpoint.

**3. Area sampling and independent radial scaling.** On the triangle joining \(O\) to a boundary element of arclength \(d\ell\), use \(O+s(Y-O)\), \(0<s<1\). Its Jacobian is \(rs\,ds\,d\ell\), since the supporting side has distance \(r\) from \(O\). Normalizing by \(r\operatorname{perimeter}(P)/2\) gives the product probability measure \(2s\,ds\times d\ell/\operatorname{perimeter}(P)\). Thus the boundary point is uniform in arclength, independent of a scale with density \(2s\), proving the asserted distributional factorization. This is the precise cone-measure specialization; no independent-radius assertion is needed for nontangential polygons.

**4. Area radial derivative.** Let \(\rho(\phi)\) denote the radial distance from \(O\) to the polygon boundary in direction \(\phi\). Within the fan of a side, whose limiting ray angles differ from its normal direction by \(-g_{i-1}\) and \(+g_i\), one has \(\rho(\phi)=r/\cos(\phi-\arg n_i)\). For \(t>r\) put \(\alpha(t)=\arccos(r/t)\). On this fan, exactly \((g_{i-1}-\alpha(t))_++(g_i-\alpha(t))_+\) radians have \(\rho(\phi)>t\). Hence
\[
 m(t):=|\{\phi:\rho(\phi)>t\}|=2\sum_i(g_i-\alpha(t))_+.
\]
Polar integration of \(\operatorname{area}(P\cap B_t(O))=\frac12\int_0^{2\pi}\min\{t^2,\rho(\phi)^2\}\,d\phi\) gives \(F'(t)=tm(t)/(r^2T)\). For \(t\le r\), the complete disk is included and its area is \(\pi t^2\). This proves both parts of the interior formula, including the threshold endpoints by continuity.

**5. Exact inversion of the boundary law.** The essential infimum of \(|Y-O|\) is \(r\), so the original law first recovers the scale. Its transformation then yields the continuous piecewise-linear function \(S(z)=\Pr\{Z>z\}\). Let \(v_1<\cdots<v_k\) be its distinct positive knots and let \(b_j>0\) be the jump of its one-sided derivative at \(v_j\). Step 2 gives \(b_j=m_j/T\), where \(m_j\) is the multiplicity of \(u=v_j\). The turning-angle identity yields the explicit inverse
\[
 T=\frac{\pi}{\sum_{j=1}^k b_j\arctan v_j},\qquad
 m_j=T b_j,\qquad g_j=\arctan v_j.
\]
Thus even the number of sides and all repeated gaps are recovered without any prior knowledge of \(n\). The reconstructed values \(m_j\) are positive integers for genuine polygonal input.

**6. Exact inversion of the interior law.** From the observed small-radius CDF, recover \(A=\operatorname{area}(P)\) through \(A=\pi/\lim_{t\downarrow0} F(t)/t^2\). The largest radius for which \(F(t)=\pi t^2/A\) is precisely \(r\): beyond \(r\), a disk loses a positive cap at each side. For \(0<\alpha<\pi/2\), substitute \(t=r\sec\alpha\) and construct
\[
 H(\alpha)=\frac{A}{2t}F'(t)=\sum_i(g_i-\alpha)_+.
\]
The distinct knots of the convex, piecewise-linear function \(H\) occur exactly at the gaps \(g_i\). Its derivative increases by the multiplicity of each gap at that knot. Thus the area law independently recovers precisely the same multiset; this does not rely on the boundary law's inversion.

**7. Congruence fibers.** Ordered normal gaps reconstruct the polygon from tangent halfplanes up to rigid rotation and translation. Orientation reversal reverses the cyclic word. Conversely, a congruence maps the uniquely determined incircle to the uniquely determined incircle and therefore acts on outward normals by rotation or reflection, inducing one of these dihedral operations. All permutations of an admissible multiset remain admissible by the construction in the scope paragraph. Hence congruence classes at fixed law are exactly the multiset's dihedral orbits. If all entries differ, each orbit has \(2n\) words among \(n!\) orderings, giving \((n-1)!/2\) classes.

For an exact rational quadrilateral witness take
\[
 (u_1,u_2,u_3,u_4)=(1/2,1/3,2,3).
\]
Here \(\arctan(1/2)+\arctan(1/3)=\pi/4\) and \(\arctan2+\arctan3=3\pi/4\). All angles satisfy the required strict bounds. Its \(24\) orderings form exactly three dihedral orbits; tangent-line intersections are rational, and every orbit has the same radial distributions, area \(35r^2/6\), and perimeter \(35r/3\).

## Verification
The standalone script `verification/check_radial_fingerprint.py` uses only the Python 3 standard library. It constructs rational unit-circle tangent normals by exact rational double-angle rotations, intersects neighboring tangent lines, and independently computes shoelace area and the second and fourth polar moments using exact triangle integration. It compares these with the derived tangent-length formulas for six rational polygon families and permuted orders, checks all supporting-face incidences and boundary tail lengths, and checks the three dihedral classes of the explicit quadrilateral. A separate midpoint-angle ray quadrature compares the radial angular-level formula with direct intersections of rays and tangent halfplanes.

Run `python3 verification/check_radial_fingerprint.py`. The obtained output was `RADIAL_INVERSE_CHECK_OK: 12578 exact rational comparisons; 15 numerical ray checks; 6 rational polygon families; 3 quadrilateral congruence classes`. Finite checks support the algebraic identities and examples; the universal inverse statements follow from steps 1–7, not from this enumeration. No external data or packages are required.

## Relationship to prior work
Gui, Hu, and Li, *A Pólya–Szegő Theorem for Tangential Polygons* (arXiv:2607.28768v1, 2026-07-30), use the same natural tangent-half-angle parameters in their torsional-rigidity comparison. Their stated theorem concerns PDE shape optimization, not inverse radial-distance laws or dihedral ordering fibers.

Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk* (arXiv:2608.27491v1, 2026-08-26), proves the polygonal cone-measure directional transfer and its arclength specialization for tangential polygons. That result supplies conceptual context for step 3 but does not identify the boundary radial hinge spectrum or classify its inverse congruence fibers.

Kim, Yaskin, and Zvavitch, *Distribution functions of sections and projections of convex bodies* (arXiv:1512.07289v1, first public 2015-12-22), study geometric tomography from distributions of direction-dependent section or projection measurements. Their two-dimensional examples establish nonuniqueness under different data, not the present exact all-tangential classification from a random point's radial distance.

A publicly available 2026 result entitled *Inverse classification of projection-width distributions for tangential symmetric polygons* classifies the **uniform-direction width law** for centrally symmetric tangential polygons by their half-cycle gap multiset. That independent measurement is not the arclength-boundary or uniform-interior radial-distance law, and the published theorem does not cover general nonsymmetric tangential polygons. The present theorem reconstructs the gap data directly from a different observable on all tangential polygons and reaches the generic first ambiguity at four sides rather than eight. Its angular parametrization and dihedral mechanism are related, so priority for those general ideas is not claimed.

## Limitations
All claims require an exactly tangential, nondegenerate planar convex polygon and access to an exact full radial law. The theorem does not reconstruct the cyclic order from unlabeled distance data, does not apply to arbitrary nontangential polygons, and gives no conditioning or finite-sample error bound. Coincident knots and nearly coincident knots are mathematically covered but may be hard to distinguish numerically. A stronger equivalent statement in older geometric-tomography literature cannot be excluded with absolute certainty.

## References
[1] C. Gui, Y. Hu, Q. Li, *A Pólya–Szegő Theorem for Tangential Polygons*, arXiv:2607.28768v1, first submitted 2026-07-30. https://arxiv.org/abs/2607.28768

[2] S. Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk*, arXiv:2608.27491v1, first submitted 2026-08-26. https://arxiv.org/abs/2608.27491

[3] J. Kim, V. Yaskin, A. Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first submitted 2015-12-22. https://arxiv.org/html/1512.07289v1

[4] *Inverse classification of projection-width distributions for tangential symmetric polygons*, publicly available 2026-10-11. https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-inverse-classification-of-projection-width-distributions-for-tan--2ee871113939/RESULT.md
