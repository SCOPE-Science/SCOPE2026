# Three-chamber radial law and exact mean central-section area of the rhombic dodecahedron

## Finding

Let \(K\subset\mathbb R^3\) be the regular rhombic dodecahedron with vertices \((\pm2,0,0)\), their coordinate permutations, and the eight sign choices of \((1,1,1)\). Let \(U\) be Haar-uniform on \(S^2\), and let \(R=\max\{s\ge0:sU\in K\}\). The probability density \(f_R\) is explicitly determined by three nonempty analytic chambers and two intrinsic transition radii.

Put
\[
r_0=2\sqrt{2/3},\qquad r_1=\sqrt3,\qquad
\beta=\arctan\sqrt2,\qquad
\delta(r)=\arccos\frac{\sqrt2}{\sqrt{3(r^2-2)}}\quad(r\ge r_0).
\]
For \(\sqrt2<r<2\), the density is
\[
 f_R(r)=\frac{12\sqrt2}{\pi r^2}\begin{cases}
 \pi/2,&\sqrt2<r<r_0,\\
 \pi/2-2\delta(r),&r_0<r<r_1,\\
 \beta-\delta(r),&r_1<r<2.
 \end{cases}
\]
It vanishes outside \([\sqrt2,2]\); the density's values at the finitely many boundaries are immaterial. In particular, the complete law is determined by this formula, with \(F_R(r)=0\) for \(r\le\sqrt2\), \(F_R(r)=1\) for \(r\ge2\), and
\[
 F_R(r)=6(1-\sqrt2/r)\quad(\sqrt2\le r\le r_0).
\]
The density is continuous through the internal boundaries, but has a square-root derivative singularity on approach from above to \(r_0\); at \(r_1\), its one-sided derivatives have the exact jump
\[
 f_R'(r_1^+)-f_R'(r_1^-)=\frac{8\sqrt3}{\pi}.
\]
The upper endpoint has a sharp quadratic tail:
\[
 \mathbb P(R>2-\varepsilon)=\frac{3}{2\pi}\varepsilon^2+O(\varepsilon^3)
 \quad(\varepsilon\downarrow0).
\]

If \(H\) is a Haar-uniform two-dimensional linear subspace, a second exact consequence is the Euclidean-area identity
\[
 \boxed{\mathbb E\,\operatorname{area}_2(K\cap H)
 =8\sqrt3\log(1+\sqrt3)-2\pi
 =7.6432311838435444020\ldots.}
\]
This is not the mean area of the orthogonal projection. For the inradius-one homothetic copy \(K/\sqrt2\), this expected sectional area is \(4\sqrt3\log(1+\sqrt3)-\pi\).

## Assumptions and scope

All areas and distances are Euclidean; all spheres and Grassmannians carry their rotation-invariant probability measures. The polytope is specified without ambiguity by
\[
 K=\{x\in\mathbb R^3: |x_1|+|x_2|\le2,\ |x_1|+|x_3|\le2,\ |x_2|+|x_3|\le2\}.
\]
It has 14 vertices, 24 edges, and 12 congruent rhombic facets; its inradius is \(\sqrt2\). Equalities between the absolute coordinates of \(U\) form a sphere-null set, though the deterministic radial formula also holds on these boundaries.

## Proof

**1. Deterministic radial identity.** Write \(a\ge b\ge c\ge0\) for the ordered absolute coordinates of \(u\in S^2\). The inequalities defining \(K\) give
\[
 \rho_K(u)=\min_{1\le i<j\le3}\frac2{|u_i|+|u_j|}=\frac2{a+b}.
\]
Since \(1\le a+b\le\sqrt2\), the support is exactly \([\sqrt2,2]\). The twelve outward unit facet normals are \(m=(\pm e_i\pm e_j)/\sqrt2\), and the facets lie at signed distance \(\sqrt2\). Hence if \(\theta(u)\) is the smallest spherical distance from \(u\) to any of these twelve normals, then
\[
 \rho_K(u)=\frac{\sqrt2}{\cos\theta(u)},\qquad 0\le\theta(u)\le\pi/4.
\]

**2. Spherical Voronoi cells.** Consider \(m=(1,1,0)/\sqrt2\) and the orthonormal tangent vectors \(v=(1,-1,0)/\sqrt2\), \(w=(0,0,1)\). The Voronoi cell of \(m\) among the twelve facet normals is
\[
 \mathcal V_m=\{u\in S^2:u_1\ge|u_3|,\ u_2\ge|u_3|\}.
\]
Indeed, a unit normal maximizing \(m'\cdot u\) chooses the two largest absolute coordinates of \(u\) with their signs. Parameterize \(u\in\mathcal V_m\) by
\[
 u=\cos\theta\,m+\sin\theta(\cos\phi\,v+\sin\phi\,w).
\]
The two defining inequalities reduce exactly to
\[
 \cot\theta\ge |\cos\phi|+\sqrt2|\sin\phi|.
\]
By quadrant symmetry it suffices to study \(0\le\phi\le\pi/2\). Here the right side equals
\[
 h(\phi)=\cos\phi+\sqrt2\sin\phi
 =\sqrt3\cos(\phi-\beta),\qquad\beta=\arctan\sqrt2.
\]
For \(\alpha=\arccos(\sqrt2/r)\), let \(L(\alpha)\) be the measure of \(\phi\in[0,\pi/2]\) satisfying \(h(\phi)<\cot\alpha\). Since \(h\) increases from \(1\) to \(\sqrt3\) and then decreases to \(\sqrt2\), elementary interval intersections give
\[
 L(\alpha)=\begin{cases}
 \pi/2,&0<\alpha<\pi/6,\\
 \pi/2-2\arccos(\cot\alpha/\sqrt3),
 &\pi/6<\alpha<\arctan(1/\sqrt2),\\
 \beta-\arccos(\cot\alpha/\sqrt3),
 &\arctan(1/\sqrt2)<\alpha<\pi/4.
 \end{cases}
\]
All twelve spherical Voronoi cells are congruent, and the spherical area element is \(\sin\theta\,d\theta\,d\phi\). Differentiating the area of their intersection with the twelve spherical caps of radius \(\alpha\) yields
\[
 \frac{d}{d\alpha}\mathbb P\{\theta(U)\le\alpha\}
 =\frac{12}{4\pi}\,(4L(\alpha))\sin\alpha
 =\frac{12}{\pi}L(\alpha)\sin\alpha.
\]
Since \(d\alpha/dr=\sqrt2/[r\sqrt{r^2-2}]\) and \(\sin\alpha=\sqrt{r^2-2}/r\), the density is \(12\sqrt2 L(\alpha)/(\pi r^2)\). The three angular thresholds map precisely to \(r_0\), \(r_1\), and \(2\), proving the complete density. In the first chamber, direct integration gives the displayed cumulative formula. At \(r_1\), \(\delta'(r_1)=\sqrt6\); the jump of the multiplier's derivative is \(\delta'(r_1)\), proving the stated jump. The onset of \(\arccos\) at argument \(1\) gives the square-root singularity at \(r_0\).

To obtain the upper tail, near each of the six coordinate-axis directions use tangent coordinates \((y,z)\), so that \(a=\sqrt{1-y^2-z^2}\), \(b=\max(|y|,|z|)\). The condition \(2/(a+b)>2-\varepsilon\) specifies a tangent square \(|y|,|z|<\varepsilon/2+O(\varepsilon^2)\). Each square has area \(\varepsilon^2+O(\varepsilon^3)\), and six disjoint patches divided by the total spherical area \(4\pi\) give the claimed tail.

**3. Mean section area.** Every central section has radial function \(\rho_K\) restricted to its plane. Its polar-area identity is
\[
 \operatorname{area}_2(K\cap H)=\frac12\int_{S^1\cap H}\rho_K(v)^2\,d\vartheta(v).
\]
Choosing the normal \(H^\perp\) uniformly, and then a uniform tangent direction, produces a Haar-uniform vector on \(S^2\); therefore
\[
 \mathbb E\operatorname{area}_2(K\cap H)
 =\pi\mathbb E\rho_K(U)^2
 =\frac14\int_{S^2}\rho_K(u)^2\,d\sigma(u).
\]
There are 48 coordinate ordering and sign chambers. On one chamber use gnomonic coordinates \(u=(1,s,t)/\sqrt{1+s^2+t^2}\) with \(0\le t\le s\le1\). The sphere Jacobian equals \((1+s^2+t^2)^{-3/2}\), and \(\rho_K(u)=2\sqrt{1+s^2+t^2}/(1+s)\). Thus
\[
 \mathbb E\operatorname{area}_2(K\cap H)
 =48\int_0^1\!\int_0^s
 \frac{dt\,ds}{(1+s)^2\sqrt{1+s^2+t^2}}
 =48\int_0^1\frac{\operatorname{arsinh}(s/\sqrt{1+s^2})}{(1+s)^2}\,ds.
\]
Integration by parts and
\[
 \frac1{(1+s)(1+s^2)}=
 \frac1{2(1+s)}+\frac{1-s}{2(1+s^2)}
\]
reduce the last integral to \(24(J_1-J_3)\), where
\[
 J_1=\int_0^1\frac{ds}{(1+s)\sqrt{1+2s^2}}
 =\frac{\log(1+\sqrt3)}{\sqrt3},\qquad
 J_3=\int_0^1\frac{s\,ds}{(1+s^2)\sqrt{1+2s^2}}=\frac\pi{12}.
\]
For \(J_1\), substitute \(q=\tanh\bigl(\tfrac12\operatorname{arsinh}(\sqrt2s)\bigr)\), giving the rational integral \(\sqrt2\int_0^{\sqrt2/(1+\sqrt3)}dq/(1+\sqrt2q-q^2)\), whose endpoint logarithm is displayed. For \(J_3\), substitute \(q=\sqrt{1+2s^2}\) to obtain \(\int_1^{\sqrt3}dq/(1+q^2)=\pi/12\). Therefore the mean equals \(8\sqrt3\log(1+\sqrt3)-2\pi\). The independent density moment relation gives the consistency identity \(\pi\int r^2f_R(r)dr=8\sqrt3\log(1+\sqrt3)-2\pi\).

## Verification

The accompanying `verify.py` independently reconstructs the 14 vertices and 24 edges, cuts those edges by 18,000 sampled plane normals, computes section areas by planar shoelace integration, and compares the sample mean against the exact expression. It also checks the radial relation against the 12 facet inequalities, the three density masses against sampled angular frequencies, density normalization, transition continuity, and two independently derived high-precision integral expressions for the mean. The standalone program completed successfully. Numerical finite testing is supportive evidence; the preceding spherical-area and gnomonic arguments establish the universal claims.

## Relationship to prior work

Cesaroni and Novaga (first publicly posted September 19, 2026) prove a sharp surface-area/inradius extremal theorem for all parallelohedra, with the regular rhombic dodecahedron as the unique equality case. Their extremal theorem motivates the geometric object; it does not provide the present random-direction radial density or mean central-section area. Classical spherical Voronoi decomposition and polar-area identities are used but not claimed as new. Omri Abas (first posted August 10, 2026) gives a general co-area method for random widths of polytopes and explicit cases including the rhombic dodecahedron's own width. The present radial distance is, instead, the reciprocal of the width of the **polar cuboctahedron**; its three evaluated chambers and the exact central-sectional mean require the explicit angular and gnomonic calculations above. Brandenburg, De Loera, Luo, and Meroni (2026) give a general algorithm for pointwise volumes and moments of polyhedral-norm-ball slices. Their applications concern cubes, and the inspected text does not evaluate the Haar-averaged central section area for this rhombic dodecahedron. An equivalent earlier cuboctahedral width distribution remains a genuine historical-priority risk.

## Limitations

This theorem covers one specified Euclidean regular rhombic dodecahedron and Haar-uniform central plane orientations; it does not give distributions for translated/noncentral sections, arbitrary affine deformations, or the area of an individual random section. The available abstract of the potentially relevant 2026 broad width-density paper was inspected, but its full text could not be accessed through available sources. Historical priority is therefore not established conclusively. All exact claims are analytic; the finite verifier is not a substitute for proof.

## References

1. A. Cesaroni and M. Novaga, *The rhombic dodecahedral conjecture*, first publicly posted 2026-09-19, `https://arxiv.org/abs/2610.13975`; original listing `https://cvgmt.sns.it/paper/7990/`.
2. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, first publicly posted 2026-08-10, `https://arxiv.org/abs/2609.26202`.
3. M.-C. Brandenburg, J. A. De Loera, Y. Luo, and C. Meroni, *Critical moments of slices and slabs of the cube (and other polyhedral norms)*, first posted 2026-03-26, `https://arxiv.org/abs/2603.25643`.
4. The regular rhombic dodecahedron's standard 14-vertex description: `https://en.wikipedia.org/wiki/Rhombic_dodecahedron`.
