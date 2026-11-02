# A logarithmic coplanar transition for the surface area of two-disc discotopes

## Finding

Let \(D_R(P)\) denote the closed Euclidean disk of radius \(R>0\), centered at the origin in a two-dimensional linear plane \(P\subset\mathbb R^3\). Let \(P,Q\) be planes with acute dihedral angle \(0<\theta\le\pi/2\), and set \(K_\theta=D_R(P)+D_S(Q)\), where \(S>0\) is the second radius and \(+\) denotes Minkowski addition. Write \(\mathcal A(\theta)=\mathcal H^2(\partial K_\theta)\) for ordinary Euclidean surface area (well-defined because \(K_\theta\) is full-dimensional).

Define the complete elliptic integral of the second kind by
\[
E(k)=\int_0^{\pi/2}\sqrt{1-k^2\sin^2 t}\,dt,\qquad 0\le k\le1.
\]
Then the exact surface-area law is
\[
\boxed{\mathcal A(\theta)=2\pi(R^2+S^2)+8RS\int_0^{\pi/2}E\!\left(\sqrt{1-\sin^2\theta\sin^2 t}\right)dt.}
\]
It is strictly increasing with \(\theta\) on \((0,\pi/2]\). Consequently, for all \(0<\theta\le\pi/2\),
\[
2\pi(R+S)^2<\mathcal A(\theta)\le 2\pi(R^2+S^2)+8RS\int_0^{\pi/2}E(\cos t)\,dt,
\]
where the upper equality holds exactly for perpendicular planes, and the lower bound is the sharp infimum approached as the planes coalesce. The continuous right-hand extension at \(\theta=0\) obeys the **sharp nonanalytic law**
\[
\boxed{\mathcal A(\theta)=2\pi(R+S)^2+\pi RS\,\theta^2\left(\log\frac8\theta-1\right)+O_{R,S}\!\left(\theta^4\log\frac1\theta\right)\quad(\theta\downarrow0).}
\]
In particular the extended area function has first derivative zero but no finite second derivative at the coplanar endpoint. For \(R=S=1\), the perpendicular-plane surface area is \(29.187822294579\ldots\).

For comparison, the volume and the mean width of the same body are respectively
\[
\operatorname{Vol}_3(K_\theta)=2\pi RS(R+S)\sin\theta,\qquad \overline w(K_\theta)=\frac\pi2(R+S).
\]
Thus mean width is angle-independent, whereas volume and area grow strictly with plane separation; the area has a logarithmic boundary layer not exhibited by the volume.

## Assumptions and scope

The disk planes pass through one common center, the radii are strictly positive, and the dihedral angle is the *acute* angle between their unoriented normals. For \(\theta>0\) the sum is a compact, full-dimensional, centrally symmetric convex body. All surface-area and volume statements use the ambient Euclidean metric. The quantity \(\mathcal A(0+)\) is a **one-sided limit** of full-dimensional surface areas; it is twice the planar disk area. The ordinary Hausdorff measure of the boundary of the degenerate planar disk at the exact value \(\theta=0\) would count its interior once rather than twice, and is not asserted equal to the limit.

## Proof

**1. Centered segment representation and normalization.** Write \(e_\phi=(\cos\phi,\sin\phi,0)\) and rotate coordinates so that
\[
v_\psi=(\cos\psi,\cos\theta\sin\psi,\sin\theta\sin\psi),\qquad 0\le\phi,\psi\le\pi.
\]
The support function of the first planar disk is reproduced exactly by the Minkowski integral
\[
D_R(P)=\frac R2\int_0^\pi[-e_\phi,e_\phi]d\phi,
\]
because \(\int_0^\pi|\langle u,e_\phi\rangle|d\phi=2\|\operatorname{proj}_P u\|\). The analogous formula with \(S,v_\psi\) holds for the second disk. These integrals are Hausdorff limits of ordinary zonotopes.

For a zonotope \(Z=\sum_i[-z_i,z_i]\subset\mathbb R^3\), the second intrinsic volume and three-volume satisfy
\[
V_2(Z)=4\sum_{i<j}\|z_i\times z_j\|,\qquad
\operatorname{Vol}_3(Z)=8\sum_{i<j<k}|\det(z_i,z_j,z_k)|.
\]
These are the standard Cauchy--Binet/zonotope minor identities, with generators of *full* length \(2z_i\). For a three-dimensional convex body the Euclidean surface area is \(2V_2\). Intrinsic volumes are Hausdorff-continuous, so the identities pass to the disk integrals. In particular \(V_2(D_R(P))=\pi R^2\), an independent normalization check.

**2. Exact area and its elliptic reduction.** Separating the within-disk pairs from the mixed pairs gives
\[
\mathcal A(\theta)=2\pi(R^2+S^2)+2RSJ(\theta),
\qquad J(\theta)=\int_0^\pi\!\int_0^\pi\|e_\phi\times v_\psi\|d\phi\,d\psi.
\]
For a fixed \(\psi\), the scalar product \(\langle e_\phi,v_\psi\rangle\) has the form \(b_\psi\cos(\phi-\alpha_\psi)\), where
\[
b_\psi=\sqrt{1-\sin^2\theta\sin^2\psi}.
\]
Translation of a full-period integral therefore yields \(\int_0^\pi\|e_\phi\times v_\psi\|d\phi=2E(b_\psi)\), and symmetry gives
\[
J(\theta)=4\int_0^{\pi/2}E\!\left(\sqrt{1-\sin^2\theta\sin^2 t}\right)dt.
\]
This proves the stated surface-area representation with all factors fixed.

**3. Strict extrema.** For \(0<k<1\), \(E(k)\) decreases strictly in \(k\), directly from its defining positive integral. For every \(t\in(0,\pi/2)\), the argument \(\sqrt{1-\sin^2\theta\sin^2 t}\) decreases strictly with \(\theta\in(0,\pi/2)\). Integration therefore shows strict increase. Since \(E(1)=1\), \(J(0)=2\pi\), which gives the lower limiting area. Substituting \(\theta=\pi/2\) gives the upper endpoint and proves all equality statements.

**4. Sharp logarithmic endpoint expansion.** Let \(z\downarrow0\). The classical complementary-modulus expansion (also obtainable by differentiating the defining integral) is
\[
E(\sqrt{1-z^2})=1+\frac{z^2}{2}\left(\log\frac4z-\frac12\right)+O\!\left(z^4\log\frac1z\right).
\]
Here the remainder, after substituting \(z=\sin\theta\sin t\), is integrable uniformly in small positive \(\theta\), since \(\int_0^{\pi/2}\sin^4t\,|\log\sin t|dt<\infty\). The two exact elementary beta-integrals needed are
\[
\int_0^{\pi/2}\sin^2t\,dt=\frac\pi4,
\qquad \int_0^{\pi/2}\sin^2t\log(\sin t)dt=\frac\pi8(1-2\log2).
\]
Consequently, with \(q=\sin\theta\),
\[
J(\theta)-2\pi=\frac\pi2 q^2\left(\log\frac8q-1\right)+O\!\left(q^4\log\frac1q\right).
\]
Multiplying by \(2RS\), and using \(q=\theta+O(\theta^3)\), yields the claimed complete first nonanalytic correction. The right derivative at zero exists and vanishes because the excess is \(o(\theta)\). But its second-order difference quotient diverges as \(2\pi RS\log(1/\theta)\), so the continuous extension has no finite second derivative at zero.

**5. Volume and mean width.** The triple-minor formula has no contribution from three generators in one disk plane. For two first-plane generators and one second-plane generator,
\[
|\det(e_\phi,e_{\phi'},v_\psi)|=|\sin(\phi'-\phi)|\sin\theta\sin\psi.
\]
The double integral in \(\phi,\phi'\) equals \(2\pi\), the integral in \(\psi\) equals \(2\), and the unordered-pair factor is \(1/2\). Thus this mixed contribution is exactly \(2\pi R^2S\sin\theta\). Interchanging the disks adds \(2\pi RS^2\sin\theta\), proving the volume identity. For a centered disk of radius \(R\), averaging its support function on the unit sphere gives mean width \(\pi R/2\). Additivity of support functions gives the mean-width identity. No asymptotic limit was used to prove either exact identity.

## Verification

Run `python check_surface.py` with Python 3, NumPy and SciPy. The checker compares the elliptic one-dimensional quadrature against a separate two-dimensional cross-product quadrature, numerically checks strict angular ordering and the endpoint coefficient, and reconstructs Minkowski sums of regular inscribed polygons using a three-dimensional convex hull. It checks that polygonal area and volume converge with the predicted quadratic discretization error to the closed formulas at several nonzero angles and two radius pairs. All checks completed with `ALL_TWO_DISC_ANGULAR_AREA_CHECKS_PASSED`.

These finite checks are not used as proof of strict monotonicity, exact identities, or asymptotic claims; the proof is given above. The checker's convex-hull area is based on inscribed polygonal disks, not on the discotope's algebraic boundary equation.

## Relationship to prior work

Mathis and Meroni's *Fiber Convex Bodies* (first publicly available May 26, 2021, arXiv:2105.12406) identifies the four planar disk faces and geometric structure of such sums; its analyzed discotope section does not give the present angle-dependent surface-area law or its coplanar singularity. Breiding, Bürgisser, Lerario, and Mathis's *The zonoid algebra, generalized mixed volumes, and random determinants* (arXiv:2109.14996, September 30, 2021) provides the broad intrinsic-volume/mixed-zonoid formalism. The double generator integral is a specialization of those general principles; **neither the general zonoid formula nor its use here is asserted to be independently new**. Gesmundo and Meroni's *The Geometry of Discotopes* (arXiv:2111.01241, November 1, 2021) analyzes algebraic boundaries and exposed faces, not the claimed strict area-versus-angle law. The specific contribution here is the sharp global angular inequality and the explicit logarithmic, non-\(C^2\) coplanar transition, supported by the exact elliptic reduction.

## Limitations

The shape family comprises *centered circular disks* in two distinct planes in \(\mathbb R^3\). The theorem does not cover arbitrary ellipses, independently translated disks, three or more summands, or higher dimensions. The singular limit concerns the continuous extension of three-dimensional surface area; the exactly flat set is lower-dimensional and requires the stated counting convention. Published and indexed coverage was compared, but differently indexed prior derivations could exist. The work has not undergone independent audit.

## References

1. L. Mathis and C. Meroni, *Fiber Convex Bodies*, arXiv:2105.12406 (first version 2021-05-26); Discrete & Computational Geometry 70 (2023), 1451--1475. https://arxiv.org/abs/2105.12406
2. P. Breiding, P. Bürgisser, A. Lerario, and L. Mathis, *The zonoid algebra, generalized mixed volumes, and random determinants*, arXiv:2109.14996 (first version 2021-09-30); Advances in Mathematics 2022. https://arxiv.org/abs/2109.14996
3. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241 (first version 2021-11-01); Le Matematiche 77 (2022), 143--171. https://arxiv.org/abs/2111.01241
4. NIST Digital Library of Mathematical Functions, Chapter 19, Section 19.12, complementary-modulus expansions of complete elliptic integrals. https://dlmf.nist.gov/19.12
