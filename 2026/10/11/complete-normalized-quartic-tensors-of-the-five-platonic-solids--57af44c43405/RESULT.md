# Complete normalized quartic tensors of the five Platonic solids
## Finding
Let \(P\subset\mathbb R^3\) be any of the five solid regular Platonic polyhedra, centered at its symmetry center, and let \(X\) be uniform with respect to three-dimensional volume on \(P\). Write
\[
R_2(P)=\mathbb E\|X\|_2^2,
\qquad
R_4(P)=\mathbb E\|X\|_2^4,
\qquad
\kappa(P)=\frac{R_4(P)}{R_2(P)^2}.
\]
For every Euclidean unit vector \(u=(u_1,u_2,u_3)\), define the angularly normalized fourth moment
\[
F_P(u)=\frac{5\mathbb E\langle X,u\rangle^4}{R_4(P)}.
\tag{1}
\]
For the tetrahedron, cube, and octahedron, use the coordinate orientations specified below. Set
\[
S_4(u)=u_1^4+u_2^4+u_3^4.
\]
Then the complete quartic profile has the form
\[
\boxed{F_P(u)=1+\eta(P)\left(S_4(u)-\frac35\right)}
\tag{2}
\]
with the following **exact table of the two scale-independent fourth-order invariants**:

| Polyhedron | \(\eta(P)\) | \(\kappa(P)\) |
| --- | ---: | ---: |
| Regular tetrahedron | \(-10/19\) | \(95/63\) |
| Cube | \(-10/19\) | \(19/15\) |
| Regular octahedron | \(5/8\) | \(80/63\) |
| Regular dodecahedron | \(0\) | \((338875-37475\sqrt5)/211722\) |
| Regular icosahedron | \(0\) | \((185-15\sqrt5)/126\) |

In particular, the **tetrahedron and cube have exactly the same normalized angular fourth-moment function**, although their radial fourth-to-second ratios differ. Their sharp directional range is
\[
\frac{15}{19}\le F_T(u)=F_C(u)\le\frac{65}{57},
\tag{3}
\]
where minima are at coordinate-axis directions and maxima are at body-diagonal directions. For the octahedron the ordering reverses:
\[
\frac56\le F_O(u)\le\frac54,
\tag{4}
\]
with minima at body diagonals and maxima at coordinate axes. The dodecahedron and icosahedron satisfy \(F_P(u)=1\) for **all** directions, a qualitative isotropy property already established in prior literature; the table supplies their exact radial ratios.

The two table entries reconstruct every degree-four volume-moment tensor component up to scale: \(R_4=\kappa R_2^2\), the covariance is \((R_2/3)I_3\), and the homogeneous polynomial \(\mathbb E\langle X,u\rangle^4\) determines its full symmetric rank-four tensor by polarization. No claim of novelty is made for the previously known qualitative invariance classification itself.

## Assumptions and scope
A “solid” means the filled three-dimensional polyhedron, **not** just its vertices or boundary; all integrals use uniform Lebesgue probability measure. The center is the fixed point of the full symmetry group. The quantities in (1) and \(\kappa\) are unchanged under a common scaling of the body.

For the tetrahedron take vertices
\[
(1,1,1),\quad(1,-1,-1),\quad(-1,1,-1),\quad(-1,-1,1).
\]
For the cube take \([-1,1]^3\). For the octahedron take
\[
\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\}.
\]
For the remaining two bodies any centered orientation is allowed because their quartic profile is direction-independent.

Módis and Kovács already classified which Platonic symmetry classes possess a rotation-invariant fourth-order moment: tetrahedral and cubic/octahedral classes do not, whereas the dodecahedral/icosahedral classes do. This **qualitative classification is prior work**, not the claimed contribution. The quantitative coefficients and all five radial ratios are the claim assessed here.

## Proof
**1. Angular quartic tensor for the first three bodies.** Every one of the specified coordinate realizations is preserved by flipping any **two** coordinate signs and by cyclically permuting the coordinates. Consequently the polynomial
\[
Q_P(u)=\mathbb E\langle X,u\rangle^4
\]
contains no mixed monomials with an odd exponent. Symmetry then gives just two coefficients,
\[
Q_P(u)=q_P\sum_i u_i^4+6p_P\sum_{i<j}u_i^2u_j^2,
\quad
q_P=\mathbb E X_1^4,\quad
p_P=\mathbb E X_1^2X_2^2.
\]
For \(\|u\|=1\), since \(2\sum_{i<j}u_i^2u_j^2=1-S_4(u)\), this reduces to
\[
Q_P(u)=3p_P+(q_P-3p_P)S_4(u).
\tag{5}
\]
Also
\[
R_4(P)=3q_P+6p_P.
\tag{6}
\]

These moments follow by direct integration:

| Body | \(q_P\) | \(p_P\) | \(R_2(P)\) | \(R_4(P)\) |
| --- | ---: | ---: | ---: | ---: |
| Tetrahedron | \(3/35\) | \(1/21\) | \(3/5\) | \(19/35\) |
| Cube | \(1/5\) | \(1/9\) | \(1\) | \(19/15\) |
| Octahedron | \(1/35\) | \(1/210\) | \(3/10\) | \(4/35\) |

For the cube the coordinates are independent uniform variables on \([-1,1]\), and the row follows from their even one-dimensional moments. For the octahedron, the absolute coordinates and the remaining slack have the uniform Dirichlet \((1,1,1,1)\) law, yielding the stated second and fourth monomial moments.

For the tetrahedron write \(X=\sum_{j=1}^4\lambda_jv_j\), with its four displayed vertices and \((\lambda_1,\ldots,\lambda_4)\) uniform Dirichlet \((1,1,1,1)\). Then \(X_1=2(\lambda_1+\lambda_2)-1\), with \(\lambda_1+\lambda_2\) having the Beta \((2,2)\) law. It follows that \(q_T=3/35\). Moreover \(X_1+X_2=2(\lambda_1-\lambda_4)\); the exact Dirichlet fourth moments give
\[
\mathbb E(X_1+X_2)^4=\frac{16}{35}.
\]
Hence \(2q_T+6p_T=16/35\), which gives \(p_T=1/21\). The second moments follow by the same Dirichlet computations. Substitution of these entries into (5)--(6) shows that the coefficient multiplying \(S_4(u)-3/5\) in (1) is
\[
\eta(P)=\frac{5(q_P-3p_P)}{R_4(P)}.
\tag{7}
\]
This equals \(-10/19\) for both the tetrahedron and cube and \(5/8\) for the octahedron.

**2. Exact radial ratios of all five solids.** Decompose a centered regular solid into congruent pyramids with apex at the center and bases its polygonal faces. Let \(R\) be its circumradius, \(r\) its distance from the center to a face, \(\rho\) its face circumradius, \(m\) its number of sides per face, and put
\[
\beta=\frac{\rho^2}{R^2},
\qquad
c=\cos\frac{2\pi}{m}.
\]
Since \(R^2=r^2+\rho^2\), every point sampled uniformly in the body can be represented as \(s(r\nu+Y)\), where \(\nu\) is a unit face normal, \(Y\) is uniform in the corresponding centered regular face, and the independent radial coordinate \(s\in[0,1]\) has density \(3s^2\). Partitioning the face into \(m\) triangles from its center, direct barycentric integration gives
\[
\mathbb E\|Y\|^2=\rho^2\frac{2+c}{6},
\qquad
\mathbb E\|Y\|^4=\rho^4\frac{7+6c+2c^2}{45}.
\tag{8}
\]
Consequently
\[
R_2=\frac35\left(r^2+\rho^2\frac{2+c}{6}\right),
\]
\[
R_4=\frac37\left(r^4+2r^2\rho^2\frac{2+c}{6}
+\rho^4\frac{7+6c+2c^2}{45}\right).
\tag{9}
\]
With \(B=1-\beta+\beta(2+c)/6\), these combine to the scale-free identity
\[
\boxed{
\kappa=\frac{25}{21}\left[1+
\frac{\beta^2(8+4c+3c^2)}{180B^2}\right].
}
\tag{10}
\]
The five geometric input pairs \((c,\beta)\) are
\[
\begin{array}{c|c|c}
\text{Tetrahedron}&-1/2&8/9\\
\text{Cube}&0&2/3\\
\text{Octahedron}&-1/2&2/3\\
\text{Dodecahedron}&(\sqrt5-1)/4&(10-2\sqrt5)/15\\
\text{Icosahedron}&-1/2&(10-2\sqrt5)/15
\end{array}
\tag{11}
\]
They follow from the regular face angle and standard circumradius/face-radius relations. To see the common last entry explicitly, write \(\varphi=(1+\sqrt5)/2\). The icosahedron with vertices \((0,\pm1,\pm\varphi)\) and cyclic permutations has squared circumradius \(\varphi+2\) and triangular faces of side length \(2\), hence face circumradius squared \(4/3\). The dodecahedron with vertices \((\pm1,\pm1,\pm1)\), \((0,\pm\varphi^{-1},\pm\varphi)\), and cyclic permutations has squared circumradius \(3\) and pentagonal faces of side length \(2/\varphi\), hence face circumradius squared \(\varphi^{-2}/\sin^2(\pi/5)\). Both ratios simplify to \((10-2\sqrt5)/15\). Substituting (11) into (10) gives the five exact radial ratios displayed above.

**3. Fourth-order isotropy for the dodecahedron and icosahedron.** Their common rotational symmetry group has order \(60\). Its element types are one identity, fifteen half-turns, twenty rotations through \(2\pi/3\), twelve through \(2\pi/5\), and twelve through \(4\pi/5\). On spherical harmonics of degree \(\ell\), the rotation character is
\[
\chi_\ell(\theta)=1+2\sum_{j=1}^{\ell}\cos(j\theta).
\]
The character vectors on these five types for \(\ell=2\) and \(\ell=4\) are respectively
\[
(5,1,-1,0,0),\qquad(9,1,0,-1,-1).
\]
The multiplicity of the invariant subspace in each harmonic degree is its averaged character, so both vanish:
\[
\frac{5+15-20}{60}=0,
\qquad
\frac{9+15-12-12}{60}=0.
\]
Decomposing the homogeneous quartic moment polynomial into spherical harmonics of degrees \(4,2,0\) therefore shows that the only invariant quartic polynomial is proportional to \(\|u\|^4\). Since the spherical angular average of \(\langle X,u\rangle^4\) is \(R_4/5\), it follows that \(F_P(u)\equiv1\). This isotropy conclusion agrees with the published symmetry classification; the new numerical quantities are those in the table.

**4. Sharp ranges.** For \(\|u\|=1\), the elementary inequalities
\[
\frac13\le S_4(u)\le1
\]
are attained precisely when all three coordinate magnitudes agree or when one coordinate has magnitude one, respectively. Applying them to (2) proves (3)--(4), including all equality directions.

## Verification
Run `python verify.py` in an environment with the dependencies listed in `requirements.txt`. The script proves the face-integral formulas and five radial-ratio expressions by exact rational/radical symbolic identities, reconstructs the tetrahedral Dirichlet fourth moments, independently verifies the tetrahedral/cubic coefficients, and checks the harmonic character sums. It also builds all five solids from vertices, triangulates their hulls, and samples uniform volume points from center-to-facet tetrahedra as a separate numerical diagnostic. The symbolic identities, not the finite sample, underwrite the universal claims.

## Relationship to prior work
Tonon's full 2005 open article develops **quadratic inertia tensors** of arbitrary tetrahedra; it does not compute the fourth tensor of the five regular solids. Richter and Schicker's 2014 full manuscript gives the geometry of all five Platonic bodies and a corresponding volume disintegration theory, but no exact quartic tensor table. Reid's 2016 paper gives metric relations for rectified polyhedra, including Platonic solids, but not these moments.

The closest direct paper is Módis and Kovács (2024), which studies **higher-order moments of the same solids** and expressly classifies the degrees at which their moments are rotation invariant. Their Table 2 already implies the qualitative icosahedral/dodecahedral fourth-order isotropy and the lack of such isotropy in the other three bodies. Those qualitative results are treated here as known. Their 8-page manuscript does not give the normalized anisotropy coefficients, the tetrahedron–cube equality of angular profiles, or the five exact radial ratios.

Earlier work by Sulikashvili investigates how third- and fourth-order inertia affects the motion of certain bodies, explicitly including the cube; that possible prior treatment of individual cubic coefficients is not excluded. The present claim is the complete quantified, scale-free **five-body** spectrum, not individual moments in isolation.

## Limitations
The theorem covers **uniformly filled** Platonic solids and their common scalings only. Surface-area distributions, vertex configurations, arbitrary affine images, and other Archimedean solids have different fourth-order moment tensors.

The known qualitative symmetry-based classification is not new, and some elementary entries (especially the cube) may have appeared in mechanics texts or unindexed tables. A 1987 higher-inertia mechanics article and a 1958 Platonic inertia paper were not fully accessible; their exact historical coverage remains a risk. 

## References
1. F. Tonon, *Explicit Exact Formulas for the 3-D Tetrahedron Inertia Tensor in Terms of its Vertex Coordinates*, *Journal of Mathematics and Statistics* 1 (2005), 8–11. DOI: 10.3844/jmssp.2005.8.11.
2. W.-D. Richter and K. Schicker, *Ball numbers of platonic bodies*, author preprint dated February 17, 2014, https://www.math.uni-rostock.de/~richter/W-DR2014-3.pdf.
3. S. Reid, *Rectifications of Convex Polyhedra*, arXiv:1604.00580v1, April 3, 2016.
4. M. Módis and F. Kovács, *On rotational invariance of higher-order moments of regular polyhedra*, *Facta Universitatis, Series: Architecture and Civil Engineering* 22 (2024), 15–22. DOI: 10.2298/FUACE230630022M.
5. R. S. Sulikashvili, *The effect of third- and fourth-order moments of inertia on the motion of a solid*, *Journal of Applied Mathematics and Mechanics* 51 (1987), 208–212. DOI: 10.1016/0021-8928(87)90066-9.
6. J. Satterly, *The Moments of Inertia of some Polyhedra*, *The Mathematical Gazette* 42 (1958), 11–13. DOI: 10.2307/3608345.
