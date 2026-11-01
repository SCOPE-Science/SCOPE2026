# Four circular shadows sharply determine cubic-bandlimited convex bodies

## Finding

Let \(K\subset\mathbb R^3\) be a full-dimensional compact convex body whose support function on \(S^2\) is the restriction of a real polynomial of total degree at most three. Consider orthogonal projections to the three coordinate planes \(P_x=\{x=0\}\), \(P_y=\{y=0\}\), \(P_z=\{z=0\}\), and to \(P_\Delta=\{x+y+z=0\}\).

**Sharp four-view circular-shadow theorem.** If the projections of \(K\) to all four planes are Euclidean disks (with unrestricted radii and centers), then \(K\) is a Euclidean ball. More precisely, the first three projected disks alone are equivalent to
\[
h_K(u)=R+\langle a,u\rangle+c\,u_1u_2u_3\qquad(u\in S^2),
\]
where \(R>0\), \(a\in\mathbb R^3\), and \(c\in\mathbb R\). Their radii are necessarily equal to \(R\). On the fourth plane, in the orthonormal frame
\[
e=(1,-1,0)/\sqrt2,\qquad f=(1,1,-2)/\sqrt6,
\]
its third Fourier amplitude (with angular parameter \(e\cos\theta+f\sin\theta\)) is
\[
T_3(P_\Delta)=\frac{|c|}{3\sqrt6}.
\]
The Euclidean ball \(B_R(a)\) is the **unique** Hausdorff-nearest ball to \(K\), and the exact residual law is
\[
\inf_{r>0,b\in\mathbb R^3}d_H(K,B_r(b))=d_H(K,B_R(a))
=\frac{|c|}{3\sqrt3}=\sqrt2\,T_3(P_\Delta).
\]
This number vanishes exactly when the fourth projection is a disk.

**Optimal number of views.** For *every* choice of at most three two-dimensional linear planes in \(\mathbb R^3\), a nonball, smooth, strictly convex body with support harmonic degree at most three exists whose projections onto all the chosen planes are disks. Thus four is the exact minimum number of appropriately selected disk tests in this bandlimited class; no universal assertion for arbitrary four-plane choices is made.

## Assumptions and scope

The support function is \(h_K(u)=\max_{x\in K}\langle x,u\rangle\), defined for unit vectors \(u\). A planar compact convex body is a disk if and only if its support on its unit circle is a positive constant plus a first angular Fourier harmonic. No common center or radius is assumed across the observed projected disks. A polynomial of degree at most three on \(S^2\) is equivalently a sum of spherical harmonics of degrees \(0,1,2,3\). The Hausdorff distance is Euclidean; all four planes pass through the origin, and the polygonal approximation of a disk is not involved. The main theorem concerns finite-degree support functions, not arbitrary convex bodies.

For a real function \(g\) on the circle parametrized by \(u(\theta)\), define its third angular Fourier amplitude by
\[
T_3(g)=\sqrt{\left(\frac1\pi\int_0^{2\pi}g(\theta)\cos3\theta\,d\theta\right)^2+
\left(\frac1\pi\int_0^{2\pi}g(\theta)\sin3\theta\,d\theta\right)^2}.
\]
This is basis-independent, since a rotation or reversal of the orthonormal plane frame preserves the amplitude.

## Proof

**1. Support functions and coordinate disks.** Orthogonal projection restricts the ambient support function to the plane circle. By harmonic decomposition, write uniquely
\[
h_K(u)=\alpha+\langle a,u\rangle+Q(u)+C(u),
\]
where \(Q\) and \(C\) are restrictions of harmonic homogeneous polynomials of degrees two and three, respectively. The even and odd parts of every circle restriction decouple. A circular projection implies that \(Q\) restricts to a constant and \(C\) restricts to a first angular harmonic on that circle.

Write
\[
Q(x,y,z)=A x^2+B y^2+C_0 z^2+2Dxy+2Exz+2Fyz,
\]
with \(A+B+C_0=0\). On the \(xy\)-circle, absence of frequency two forces \(A=B,D=0\); on \(xz\), it forces \(A=C_0,E=0\); on \(yz\), it forces \(B=C_0,F=0\). Thus \(Q=0\).

Write the cubic (using coefficients distinct from those above)
\[
C(x,y,z)=p x^3+q y^3+r z^3+s x^2y+t x^2z+v xy^2+w y^2z+j xz^2+k yz^2+\gamma xyz.
\]
A binary homogeneous cubic in \((x,y)\) has no third angular harmonic precisely when it is \((x^2+y^2)\) times a linear form. Applying this on the \(xy\), \(xz\), and \(yz\) circles yields, respectively,
\[
v=p,\ s=q;\qquad j=p,\ t=r;\qquad k=q,\ w=r.
\]
Substitution gives
\[
C(x,y,z)=(x^2+y^2+z^2)(p x+q y+r z)+\gamma xyz.
\]
Since \(C\) is harmonic, taking a Euclidean Laplacian gives \(10(px+qy+rz)=0\), so \(p=q=r=0\). Thus \(C=\gamma xyz\) and the first-three-disk classification follows. Conversely \(xyz=0\) on each coordinate circle, so this displayed support automatically gives those three radius-\(R\) disks (whenever it actually supports a convex body). Positivity \(R>0\) follows because each projected disk has nonempty interior.

**2. Fourth view and its exact coefficient.** On \(P_\Delta\), put \(u(\theta)=e\cos\theta+f\sin\theta\) with the stated orthonormal \(e,f\). A direct multiplication shows
\[
u_1(\theta)u_2(\theta)u_3(\theta)
=\frac1{\sqrt6}\left(\sin\theta-\frac43\sin^3\theta\right)
=\frac{\sin3\theta}{3\sqrt6}.
\]
The first Fourier harmonic \(\langle a,u(\theta)\rangle\) does not affect the third amplitude, and the constant \(R\) affects neither. Consequently \(T_3(P_\Delta)=|c|/(3\sqrt6)\). The fourth projection is a disk if and only if \(c=0\); in that case the support is exactly that of \(B_R(a)\).

**3. Exact best-ball Hausdorff distance and uniqueness.** Support-function distance equals Euclidean Hausdorff distance for compact convex sets. The arithmetic-geometric mean inequality applied to \(u_1^2,u_2^2,u_3^2\) gives
\[
\sup_{u\in S^2}|u_1u_2u_3|=\frac1{3\sqrt3},
\]
with equality at precisely the eight signed directions \((\pm1,\pm1,\pm1)/\sqrt3\). Hence \(d_H(K,B_R(a))=|c|/(3\sqrt3)\). To prove no other ball is closer, partition these eight directions into the four with positive coordinate product and the four with negative product. Each quartet has vector sum zero. For a candidate ball \(B_r(b)\), average the difference \(h_K-h_{B_r(b)}\) over these two quartets. The means are \(R-r\pm c/(3\sqrt3)\). Their absolute maximum is at least \(|c|/(3\sqrt3)\). Equality forces \(r=R\); then, on the quartet where \(c\,u_1u_2u_3=|c|/(3\sqrt3)\), the four linear errors must all have the same required sign and sum to zero, so all vanish. These four directions span \(\mathbb R^3\), forcing \(b=a\). If \(c=0\), distinct balls have positive Hausdorff distance, so uniqueness also holds. Combining with step 2 yields the asserted \(\sqrt2\) identity.

**4. Why any three planes fail.** The real space \(\mathcal H_3(\mathbb R^3)\) of harmonic homogeneous cubics has dimension \(10-3=7\). Its restriction to any great circle contains only angular frequencies one and three. Killing the third harmonic imposes at most two homogeneous real-linear conditions. For any prescribed three planes, at most six linear conditions therefore leave some nonzero \(H\in\mathcal H_3\) whose restrictions to the three circles contain only first harmonics. The function \(h_\varepsilon(u)=1+\varepsilon H(u)\) is a support function of a smooth, strictly convex body for all sufficiently small nonzero \(\varepsilon\), because its spherical curvature-radius form \(I+\varepsilon(\nabla^2_{S^2}H+HI)\) remains uniformly positive definite on the compact sphere. Its three observed projections are translated unit disks. Since a nonzero degree-three spherical harmonic cannot equal a constant plus a linear function, this body is not a Euclidean ball. Fewer than three tests are weaker. This completes the sharp minimum-view proof.

## Verification

The standalone standard-library Python file `verify.py` reconstructs the exact linear constraints on quadratic and cubic coefficients over the rational numbers: it checks that the three coordinate-disk conditions have rank six on all six quadratic coefficients (including the trace constraint) and rank nine on ten cubic coefficients (including three harmonicity constraints), leaving exactly the \(xyz\) coefficient. Adding the fourth-view coefficient makes the cubic matrix full rank. It also checks the diagonal-circle trigonometric identity numerically at deterministic angles and the exact \(\sqrt2\) constant. Execute `python3 verify.py` in the extracted finding directory. Those tests support but are not a substitute for the preceding all-parameter arguments.

## Relationship to prior work

Myroshnychenko, Ryabogin and Saroglou [1] prove that rotational symmetry of order at least four of *every* planar projection forces a ball; they also provide the \(u_1u_2u_3\) threefold-symmetry exception. Their Theorems 1.2–1.4 and Proposition 5.1 are global-over-planes statements and do not give a sharp finite number of circular views for polynomial support functions, nor the best-ball Hausdorff residual from a fourth view. The present result uses the same support-restriction viewpoint but asks a different finite-measurement question and makes the cubic ambiguity explicit.

Golubyatnikov and Rovenski [2] investigate circular *projection maps* and generalized convexity/visibility, a different usage of the term circular projection; their accessible text does not supply this cubic bandlimit classification. Kuz'minykh's all-projections sphere characterization [3] is historical context, not a finite-four-view implication. An indexed sharp-convexity result [4] specifies admissible perturbation amplitude, not finite-view determination. A particularly close indexed calculation [5] gives the full planar-shadow **area** profile of the specific cubic \(1+\varepsilon u_1u_2u_3\), including coordinate disks and the four diagonal minimal-brightness planes. That established special-family projection information is not claimed as new here. Neither an area law for a preselected cubic nor its optimal amplitude classifies every bandlimited support satisfying three disk tests, proves the any-three-planes obstruction, or establishes the best-ball Hausdorff residual from a fourth third harmonic. Their full files were not inspected, and this unresolved scope is a historical-priority risk. Projection-function determination via *all directions* [6] concerns areas and widths rather than four complete disk shapes. None of these comparisons by itself proves global historical priority.

## Limitations

The polynomial-degree bound is indispensable: finitely many arbitrary disk projections do not characterize a general convex body. Four *particular* planes work here, while arbitrary quadruples need not. The exact \(\sqrt2\) residual law requires the first three coordinate projections to be disks and does not assert stability under perturbations of all four measurements. The theorem does not determine the sharp admissible range of \(c\), a separate convexity problem. No independent external proof audit has been carried out; historical unindexed finite-bandlimit tomography results remain a residual priority risk.

## References

[1] S. Myroshnychenko, D. Ryabogin and C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192, first public 2026-09-23, https://arxiv.org/abs/2609.27192 (especially Theorems 1.2–1.4, Proposition 5.1 and Section 5).

[2] V. Golubyatnikov and V. Rovenski, *Some extensions of the class of k-convex bodies*, arXiv:0809.3643, 2008, https://arxiv.org/html/0809.3643v1 (Introduction and Sections 1–2).

[3] A. V. Kuz'minykh, *The isoprojection property of the sphere*, Soviet Math. Doklady 14 (1973), 891–895, cited in [1]; primary full text not inspected.

[4] *Sharp convexity threshold for the cubic constant-width support family*, indexed mathematical-research record `2026/10/4/SCOPE-sharp-convexity-threshold-for-the-cubic-constant-width-support-f--b3681da24cdc`; only the indexed scientific summary was accessible.

[5] *Exact brightness profile of the cubic threefold-projection exception*, indexed mathematical-research record `2026/10/11/SCOPE-exact-brightness-profile-of-the-cubic-threefold-projection-excep--a6ac80c263be`; scientific summary checked, full paper unavailable.

[6] P. Goodey, R. Schneider and W. Weil, *On the Determination of Convex Bodies by Projection Functions*, Bull. London Math. Soc. 29 (1997), 82–88, https://doi.org/10.1112/S0024609396001968; abstract examined, complete text not inspected.
