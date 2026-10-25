# Exact random-shadow diameter law for the regular octahedron and its endpoint shapes

## Finding
Let \(O=\operatorname{conv}\{\pm e_1,\pm e_2,\pm e_3\}\subset\mathbb R^3\), and let \(E\) be a Haar-uniform two-dimensional linear subspace. Define the **Euclidean diameter of the planar orthogonal shadow**
\[
D=\operatorname{diam}_2(P_EO),\qquad d_0=2\sqrt{2/3}.
\]
For \(0<t<1/\sqrt3\), put
\[
\alpha(t)=\arccos\!\left(\frac{t^2}{1-t^2}\right),\qquad
\beta(t)=\frac\pi2-2\arcsin\!\left(\frac{t}{\sqrt{1-t^2}}\right).
\]
The **exact complete CDF**, at \(d_0\le d\le2\), is
\[
\boxed{F_D(d)=\frac2\pi\left[3\alpha(t)-\pi-3t\beta(t)\right],\quad t=\sqrt{1-d^2/4}.}
\]
The continuous endpoint extensions are \(F_D(d_0)=0\), \(F_D(2)=1\); the CDF is zero below \(d_0\) and one above \(2\). There are no atoms. On the open support, its **exact density** is
\[
\boxed{f_D(d)=\frac{3d}{2\pi\sqrt{1-d^2/4}}\,
\beta\!\left(\sqrt{1-d^2/4}\right).}
\]
Both endpoints have sharp, qualitatively different tails, as \(\varepsilon\downarrow0\):
\[
\boxed{\Pr(D<d_0+\varepsilon)
=\frac{9\sqrt3}{2\pi}\varepsilon^2+O(\varepsilon^3),}
\]
\[
\boxed{\Pr(D>2-\varepsilon)
=3\sqrt\varepsilon-\frac6\pi\varepsilon+O(\varepsilon^{3/2}).}
\]
The lower tail also has an explicit **conditional orientation law**. Given \(D<d_0+\varepsilon\), choose the sign vector \(\sigma=(\operatorname{sgn}U_1,\operatorname{sgn}U_2,\operatorname{sgn}U_3)\), where \(E=U^\perp\) and \(U\) is a uniform unit normal. Define
\[
t_\varepsilon=\sqrt{1-(d_0+\varepsilon)^2/4},\quad
\delta_\varepsilon=1/\sqrt3-t_\varepsilon,\quad
W_\varepsilon=\frac{(\sigma_1U_1,\sigma_2U_2,\sigma_3U_3)-(1,1,1)/\sqrt3}{\delta_\varepsilon}.
\]
For sufficiently small positive \(\varepsilon\), \(\sigma\) is exactly uniform on eight sign vectors and independent of \(W_\varepsilon\). As \(\varepsilon\downarrow0\), \(W_\varepsilon\) converges in distribution to uniform **planar area** on the equilateral triangle
\[
\boxed{T=\{w\in\mathbb R^3:w_1+w_2+w_3=0,\ w_1,w_2,w_3\ge-1\}.}
\]
Equivalently, the three numbers \((W_i+1)/3\) converge jointly to \(\operatorname{Dirichlet}(1,1,1)\). At the upper endpoint, if \(m=\min_i|U_i|\), then conditional on \(D>2-\varepsilon\), the index of the smallest absolute normal coordinate is uniform on three indices and independent of \(m\), while \(m/\sqrt{1-(2-\varepsilon)^2/4}\) converges to \(\operatorname{Uniform}[0,1]\).

## Assumptions and scope
The octahedron is normalized to have vertices \(\pm e_i\), so each vertex has unit Euclidean norm and each original edge length is \(\sqrt2\). The projection is **orthogonal** onto a plane through the origin; the resulting projected convex polygon is measured with the Euclidean metric intrinsic to that plane. Haar-uniform unoriented planes are equivalently the orthogonal complements of uniform spherical normals \(U\in S^2\), with \(U\) and \(-U\) describing the same plane. The orientation sign vector is auxiliary: choosing either oriented representative gives the same sign-corrected vector and same limiting triangle. Conditioning events use strict inequalities; these agree with their nonstrict versions because the law is continuous. The conditional statements hold with \(\varepsilon>0\) sufficiently small that the indicated thresholds lie inside the support.

## Proof
**1. Deterministic reduction to a minimum coordinate.** Write \(v_i=P_Ee_i\). The projected body is \(P_EO=\operatorname{conv}\{\pm v_1,\pm v_2,\pm v_3\}\), which is centrally symmetric. The diameter of any centrally symmetric convex hull of finitely many antipodal vertex pairs is twice its largest vertex norm: the pair \(\pm v_i\) attains that distance, and every pair of points has distance at most twice the maximal norm by the triangle inequality. Orthogonal projection onto \(U^\perp\) gives \(\|v_i\|^2=1-U_i^2\). Consequently
\[
\boxed{D=2\max_i\sqrt{1-U_i^2}=2\sqrt{1-m^2},\quad m=\min_i|U_i|.}
\]
Because \(0\le m\le1/\sqrt3\), the support is \([2\sqrt{2/3},2]\); each open subinterval is attained on positive-area patches of the sphere. The statistic is thus a three-coordinate spherical order statistic, not the diameter of a central *section* of the octahedron.

**2. Exact spherical region.** For \(0\le t\le1/\sqrt3\), let \(Q(t)=\Pr(m\ge t)\). Eight sign octants are symmetric. Their common spherical region is
\[
\Omega_t=\{u\in S^2:u_1\ge t,\ u_2\ge t,\ u_3\ge t\},\qquad Q(t)=\frac{2}{\pi}\operatorname{area}(\Omega_t).
\]
For \(0<t<1/\sqrt3\), this is a spherical triangle with three circular arcs \(u_i=t\), and vertices given by permutations of \((t,t,\sqrt{1-2t^2})\). Two inward tangent gradients \(e_i-tu\) and \(e_j-tu\) at any vertex have dot product \(-t^2\) and equal squared norm \(1-t^2\). Hence each interior angle is \(\alpha(t)=\arccos(t^2/(1-t^2))\).

Parametrize one boundary arc, say \(u_1=t\), by \(u_2=\sqrt{1-t^2}\cos\phi\) and \(u_3=\sqrt{1-t^2}\sin\phi\). The requirement \(u_2,u_3\ge t\) gives angular span
\[
\beta(t)=\frac\pi2-2\arcsin\frac{t}{\sqrt{1-t^2}},
\]
so that this arc has length \(\sqrt{1-t^2}\,\beta(t)\). Its signed geodesic curvature with the positive orientation of the region is \(t/\sqrt{1-t^2}\), giving a geodesic-curvature integral \(t\beta(t)\) on each of the three arcs. Gauss--Bonnet on the unit sphere therefore gives
\[
\operatorname{area}(\Omega_t)+3t\beta(t)+3(\pi-\alpha(t))=2\pi,
\]
which rearranges to
\[
\operatorname{area}(\Omega_t)=3\alpha(t)-\pi-3t\beta(t).
\]
Inserting this into \(Q(t)=2\operatorname{area}(\Omega_t)/\pi\) and setting \(t=\sqrt{1-d^2/4}\) gives the stated CDF. This region varies continuously from one octant at \(t=0\) to a single diagonal point at \(t=1/\sqrt3\). Level sets for interior thresholds are finite unions of circular arcs, so they have zero spherical area and cannot create atoms.

**3. Density and normalization.** Differentiating the two angular expressions yields \(\alpha'(t)=t\beta'(t)\). Thus
\[
Q'(t)=-\frac6\pi\beta(t).
\]
Since \(dt/dd=-d/(4t)\), the chain rule gives the stated density \(f_D(d)=3d\beta(t)/(2\pi t)\). The density is strictly positive on the open support because \(\beta(t)>0\) there. The endpoint CDF values imply \(\int_{d_0}^2f_D(d)\,dd=1\), so no probability mass has been lost.

**4. Upper endpoint.** The last derivative gives the minimum-coordinate density \(f_m(t)=6\beta(t)/\pi\), which has the expansion
\[
f_m(t)=3-\frac{12}{\pi}t+O(t^3),\quad t\downarrow0.
\]
It follows that
\[
1-Q(t)=\Pr(m<t)=3t-\frac6\pi t^2+O(t^4).
\]
For \(d=2-\varepsilon\), its associated threshold is \(t=\sqrt{\varepsilon-\varepsilon^2/4}=\sqrt\varepsilon+O(\varepsilon^{3/2})\), giving the second tail formula. Moreover, for each fixed \(r\in[0,1]\),
\[
\Pr\{m/t\le r\mid m<t\}=\frac{1-Q(rt)}{1-Q(t)}\longrightarrow r.
\]
Permutation symmetry gives exactly uniform independent location of the minimum coordinate, outside the measure-zero tie set. This proves the upper conditional statement.

**5. Lower endpoint and conditional triangle.** Put \(t_0=1/\sqrt3\). The componentwise-positive patch \(\Omega_{t_0-\delta}\) shrinks to \(v=(1,1,1)/\sqrt3\). Writing \(u=v+\delta w\), the inequalities \(u_i\ge t_0-\delta\) become \(w_i\ge-1\), while the sphere equation becomes
\[
\sum_iw_i=-\frac{\sqrt3}{2}\delta\sum_iw_i^2.
\]
Consequently the rescaled patch converges, with its normalized induced area measure, to Euclidean area on the planar equilateral triangle \(T\). This is a standard local-chart change of variables: the sphere is a smooth graph above its tangent plane, the graph Jacobian tends uniformly to one on the bounded rescaled patch, and its boundary consists of three smoothly perturbed line segments. The triangle vertices are the permutations of \((2,-1,-1)\), its side length is \(3\sqrt2\), and its planar area is \(9\sqrt3/2\). Hence
\[
\operatorname{area}(\Omega_{t_0-\delta})
=\frac{9\sqrt3}{2}\delta^2+O(\delta^3),
\qquad Q(t_0-\delta)=\frac{9\sqrt3}{\pi}\delta^2+O(\delta^3).
\]
The normal threshold corresponding to \(d_0+\varepsilon\) obeys \(t_0-t_\varepsilon=\varepsilon/\sqrt2+O(\varepsilon^2)\). This gives
\[
\Pr(D<d_0+\varepsilon)=Q(t_\varepsilon)
=\frac{9\sqrt3}{2\pi}\varepsilon^2+O(\varepsilon^3).
\]
All eight sign patches are isometric and have exactly equal conditional mass; applying the same local-coordinate limit in each gives the asserted uniform sign law and uniform triangle limit. The affine map \(z_i=(w_i+1)/3\) maps \(T\) onto the probability simplex with constant Jacobian, giving \(\operatorname{Dirichlet}(1,1,1)\). This completes the proof.

## Verification
Run the accompanying standalone standard-library script with `python3 verify.py`. It independently reconstructs all six projected vertices and their pairwise Euclidean distances for 400 integer-normal triples; evaluates the probability event by a **separate spherical latitude--longitude integral** with endpoint-smoothed quadrature; checks the analytically differentiated density against numerical CDF differences, both endpoint coefficients and the tangent triangle's area; and compares predicted CDF values with 260,000 independently seeded Gaussian-to-Haar unit normals. Successful completion prints `ALL_PROJECTED_OCTAHEDRON_DIAMETER_CHECKS_OK`. These finite and numerical checks are corroboration, not an infinite proof. The analytic steps above establish the exact law and conditional weak limits.

## Relationship to prior work
Finch's work on random-direction widths of regular polyhedra and of cross-polytopes motivates studying distributions of projection measurements. A random **one-dimensional width** of the octahedron is proportional to the **largest** absolute coordinate of a uniformly random spherical direction, while the planar-projection diameter here is governed by the **smallest** absolute normal coordinate; the earlier width distributions do not themselves give this planar diameter CDF.

Böröczky and Henk's work on random projections of regular polytopes includes the frequency of vertex counts of two-dimensional octahedral silhouettes. A combinatorial silhouette count does not determine the distribution of their metric diameters.

Other published exact laws determine the **inradius of the planar projection of the octahedron**, the **diameter of a central planar section of the octahedron**, or the **one-dimensional width of the octahedron**. These are distinct functionals: the projected-octahedron inradius is polar to a **cube-section circumradius**, while the octahedron-section diameter is polar to a **cube-projection inradius**. Neither polarity nor a distribution of widths identifies the projected-octahedron diameter. The current CDF and endpoint conditional laws are not stated in the relevant inspected complete mathematical result texts. A classical equivalent under the aliases circumradius of a shadow, Feret diameter, or a minimum spherical coordinate remains a possible historical-priority risk.

## Limitations
The result is specific to a three-dimensional regular octahedron with the normalization above, Haar-uniform orthogonal two-dimensional projections, and Euclidean diameter. It does not assert a corresponding closed formula in higher dimensions, for affine offsets, nonuniform directions, anisotropically scaled octahedra, or arbitrary convex bodies. The lower- and upper-endpoint statements are limiting laws, not finite-threshold exact conditional distributions. The source comparison is evidence of presently inspected novelty, not a proof of historical priority; no independent mathematical audit has been performed.

## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671v1, first posted 4 October 2011, https://arxiv.org/abs/1110.0671.
2. S. R. Finch, *Mean Width of a Regular Cross-Polytope*, arXiv:1112.0499v1, first posted 2 December 2011, https://arxiv.org/abs/1112.0499.
3. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479v1, first posted 26 November 2015, https://arxiv.org/abs/1511.08479.
4. K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, preprint SC-97-21, 1997, https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf.
5. M. P. do Carmo, *Differential Geometry of Curves and Surfaces*, Prentice-Hall, 1976, chapter on Gauss--Bonnet (standard spherical-curvature theorem).
