# Exact central-section probabilities for skew parallelotopes and cubic minimality among equiangular rhombohedra

## Finding

Let \(A\in\operatorname{GL}(3,\mathbb R)\) have columns \(v_1,v_2,v_3\), let \(P=A[-1,1]^3\), and let \(U\) be Haar-uniform on the Euclidean unit sphere. The generic section \(P\cap U^\perp\) is either a quadrilateral or a hexagon. Its full polygon-type distribution admits a finite, elementary formula for **every** invertible, possibly nonorthogonal, matrix \(A\).

Set \(G=A^\top A\), \(J\) equal to the \(3\times3\) all-ones matrix, \(M=J-2I\), and, for every sign vector \(\sigma\in\{-1,1\}^3\), set \(D_\sigma=\operatorname{diag}(\sigma_1,\sigma_2,\sigma_3)\), \(\Sigma_\sigma=MD_\sigma GD_\sigma M\), and
\[
r_{ij}(\sigma)=\frac{(\Sigma_\sigma)_{ij}}{\sqrt{(\Sigma_\sigma)_{ii}(\Sigma_\sigma)_{jj}}}.
\]
All diagonal terms are strictly positive and all displayed correlations are strictly between \(-1\) and \(1\). The exact probabilities are
\[
\boxed{\Pr(N=6)=1+\frac{1}{4\pi}\sum_{\sigma\in\{-1,1\}^3}\sum_{1\le i<j\le3}\arcsin r_{ij}(\sigma),\qquad \Pr(N=4)=1-\Pr(N=6).}
\]

For the natural **equiangular rhombohedra**, whose generator Gram matrices are \(G_\rho=(1-\rho)I+\rho J\) with \(-1/2<\rho<1\), this specializes to
\[
\boxed{p_6(\rho)=1+\frac3\pi\left[\arcsin\!\left(\frac{2\rho-1}{3-2\rho}\right)-\arcsin\!\sqrt{\frac{1+2\rho}{3(3-2\rho)}}\right].}
\]
The **unique global minimum** on the whole positive-definite equiangular family is the cube, at \(\rho=0\):
\[
\boxed{p_6(\rho)\ge p_6(0)=1-\frac6\pi\arcsin\!\left(\frac13\right),\quad\text{with equality exactly for }\rho=0.}
\]
The stability coefficient is sharp:
\[
p_6(\rho)=p_6(0)+\frac{\rho^2}{\sqrt2\pi}+O(\rho^3)\qquad(\rho\to0).
\]
Moreover, \(p_6(\rho)\to1/2\) as \(\rho\downarrow-1/2\) and \(p_6(\rho)\to1\) as \(\rho\uparrow1\). Its full range on the nondegenerate equiangular family is \([p_6(0),1)\). Over all nondegenerate three-dimensional parallelotopes, the range of hexagon probabilities is the entire interval \((0,1)\).

## Assumptions and scope

The cutting planes **pass through the center** and are sampled by rotation-invariant normal direction, not by sampling a random affine offset. Affine changes in the solid are not compensated by a corresponding change in the distribution of normals. The Gram matrix is positive definite; limiting singular solids are excluded. For a generic plane, vertex passages and degenerate incidences have probability zero. A section with four edges is called a quadrilateral without requiring regularity. The equiangular parameter \(\rho\) is the common cosine of the three pairwise generator angles; equal generator norms are fixed to one because uniform scaling leaves these probabilities unchanged.

## Proof

**1. Reduce to a triangle-inequality event.** Pull the cutting plane \(U^\perp\) back through \(A\). In cube coordinates the normal is \(w=A^\top U\), and the cube plane intersects both faces perpendicular to coordinate direction \(i\) exactly if \(|w_i|<|w_j|+|w_k|\). Thus the section is a hexagon exactly when the three positive quantities \(|w_1|,|w_2|,|w_3|\) satisfy strict triangle inequalities. Outside this chamber exactly one pair of opposite faces fails to contribute, so the section has four edges. These conclusions follow by solving the corresponding face equation over the two free coordinates in \([-1,1]\).

**2. Convert the Haar probability into Gaussian orthants.** Let \(g\sim N(0,I_3)\). Since \(g/\|g\|\) is uniform on the sphere and the triangle event is homogeneous, \(w=A^\top g\sim N(0,G)\) has exactly the desired angular law. In a fixed coordinate sign chamber \(\sigma\), set \(z=D_\sigma w\). The triangle inequalities are \(Mz>0\); crucially,
\[
M^{-1}=\tfrac12(J-I),
\]
which is entrywise nonnegative and maps every strictly positive vector to the positive orthant. Hence the eight Gaussian orthant events \(MD_\sigma w>0\) are mutually disjoint and exhaust exactly the hexagon event. The covariance of their normals is \(\Sigma_\sigma=MD_\sigma GD_\sigma M\), which is positive definite.

**3. Evaluate the orthant probabilities exactly.** For any centered nondegenerate trivariate normal \(Y\) with pairwise correlations \(r_{ij}\),
\[
\Pr(Y_1>0,Y_2>0,Y_3>0)
=\frac18+\frac1{4\pi}\bigl(\arcsin r_{12}+\arcsin r_{13}+\arcsin r_{23}\bigr).
\]
Indeed, expand \(\prod_i(1+\operatorname{sgn}Y_i)/8\); odd sign moments vanish by central symmetry, and each pair has \(\mathbb E[\operatorname{sgn}Y_i\operatorname{sgn}Y_j]=2\arcsin(r_{ij})/\pi\). The pair identity follows by integrating the angle of a two-dimensional standard Gaussian in a correlated linear coordinate system. Summing the eight orthants proves the general formula, with no independence or orthogonality assumption on the generators.

**4. Evaluate the equiangular family.** Substitution of \(G_\rho=(1-\rho)I+\rho J\) into the preceding covariances gives two sign classes. The two common-sign patterns each have three equal off-diagonal correlations
\[
a(\rho)=\frac{2\rho-1}{3-2\rho}.
\]
The six mixed-sign patterns each have one correlation \(a(\rho)\) and two correlations
\[
b(\rho)=-\sqrt{\frac{1+2\rho}{3(3-2\rho)}}.
\]
Summing the eight orthant formulas yields \(p_6(\rho)=1+(3/\pi)(\arcsin a(\rho)+\arcsin b(\rho))\), as stated.

**5. Rigidity, stability, and range.** Direct differentiation on \(-1/2<\rho<1\) gives
\[
\boxed{p_6'(\rho)=\frac{3\sqrt2}{\pi(3-2\rho)\sqrt{1-\rho}}\left(1-\frac1{\sqrt{1+2\rho}}\right).}
\]
Its sign is strictly negative for \(\rho<0\) and strictly positive for \(\rho>0\). Thus zero is the unique global minimum. Expanding the derivative at zero gives \(p_6'(\rho)=(\sqrt2/\pi)\rho+O(\rho^2)\), which integrates to the sharp quadratic term. The endpoint limits follow by continuity of the two arcsine arguments in the displayed formula. Since the function is continuous and increasing from its minimum to a limiting value one on \([0,1)\), the stated equiangular range follows.

For the general range, strictly positive values hold because a nonempty open cone of normals satisfies strict triangle inequalities, while a nonempty open cone violates one triangle inequality, for every invertible \(A\). For orthogonal generator matrices \(A_t=\operatorname{diag}(t,1,1)\), the hexagon probability tends to zero as \(t\to\infty\): the necessary condition \(t|U_1|<|U_2|+|U_3|\) fails almost surely in the limit. Meanwhile equiangular generators with \(\rho\uparrow1\) yield probabilities tending to one. Continuity of the exact Gaussian/solid-angle formula in a positive-definite Gram matrix and connectedness of the positive-definite cone show that **every** value in \((0,1)\) occurs, and neither endpoint does. \(\square\)

## Verification

The standalone Python 3 program `verify_parallelotope.py` implements the correlation/arcsine formula and independently computes spherical solid angles of the eight triangle-inequality cones using the generator matrices. These are distinct analytic routes, with the latter using the standard three-vector solid-angle determinant identity rather than Gaussian orthants. It additionally samples Gaussian normals and counts cube edge-plane intersections directly, for seven equiangular parameters and a nonequiangular Gram matrix. Finite-difference derivatives are compared with the symbolic derivative displayed in the proof. Its reproducible execution prints `VERIFY_OK`. These finite checks are independent numerical consistency checks, not infinite proofs, and do not certify historical novelty.

## Relationship to prior work

Lonke [1] studies Haar-random central sections of the **orthogonal** cube, and his earlier cube specialization already fixes \(p_6(0)\). A separate published analysis [2] gives the complete unequal **rectangular** box distribution and proves that the cube **maximizes** its hexagonal-section probability within diagonal box Gram matrices. Its full proof explicitly excludes oblique parallelotopes. Our new content is the formula for arbitrary off-diagonal Gram matrices and the opposite **strict global minimality** of the cube among equal-length equiangular nonorthogonal generator families; neither follows by an affine map because Haar normal distributions are not affine-invariant. A separate published section-width optimization [3] treats all parallelotopes, but optimizes an area-times-width functional, not this angular polygon-type probability. Older stereological literature [4,5] treats frequencies of polygonal sections with potentially different plane sampling; the exact specializations and complete texts were not all available for direct comparison. We claim no novelty for the known Gaussian orthant identity, the classical cube probability, or the general solid-angle identity.

## Limitations

The general probability law is specific to central planes in three dimensions, not to affine-offset cuts. The rhombohedral minimization is restricted to a geometrically natural one-parameter equiangular family; it does **not** assert cube minimality over all skew parallelotopes, where hexagon probabilities can be arbitrarily small. Classical trivariate Gaussian orthant evaluation makes the general formula explicit but elementary; its novelty depends on whether equivalent stereological expressions were recorded earlier. In particular, Voss [4] gives a broadly titled 1982 study on polygon frequencies with analytic formulas for some families of polyhedra, but its full text could not be accessed; this is a significant historical-priority risk. The published orthotope result [2] and the 1982 study should be prioritized in any external audit. Numerical checks do not provide an independent audit.

## References

[1] Y. Lonke, *On Random Sections of the Cube*, original arXiv submission 1998-12-21, arXiv:math/9812123, https://arxiv.org/abs/math/9812123.

[2] *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes*, published-finding corpus, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-hexagon-law-and-cubic-rigidity-for-central-sections-o--45d2a55425d4.

[3] *Exact Busemann–Petty section-width profile of three-dimensional parallelotopes*, published-finding corpus, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-busemann-petty-section-width-profile-of-three-dimensional--d822061e585b.

[4] K. Voss, *Frequencies of n-polygons in planar sections of polyhedrons*, Journal of Microscopy 128 (1982), 111–120, https://doi.org/10.1111/j.1365-2818.1982.tb00443.x.

[5] J. Ohser and F. Mücklich, *Stereology for some classes of polyhedrons*, Advances in Applied Probability 27 (1995), https://doi.org/10.2307/1427832.

[6] A. van Oosterom and J. Strackee, *The solid angle of a plane triangle*, IEEE Transactions on Biomedical Engineering 30 (1983), 125–126, https://doi.org/10.1109/TBME.1983.325207.
