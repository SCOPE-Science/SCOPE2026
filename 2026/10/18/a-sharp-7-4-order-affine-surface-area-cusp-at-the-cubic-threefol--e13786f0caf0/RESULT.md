# A sharp \(7/4\)-order affine-surface-area cusp at the cubic threefold-projection boundary

## Finding
Consider the constant-width convex bodies in \(\mathbb R^3\) with support functions
\[
h_\varepsilon(u)=1+\varepsilon u_1u_2u_3,\qquad u\in S^2,
\]
for \(0\le\varepsilon<\varepsilon_*:=3\sqrt6/8\). The endpoint is the largest admissible positive amplitude. Let \(\mathcal A(\varepsilon)\) denote the ordinary equiaffine surface area, normalized as \(\int_{\partial K_\varepsilon}\kappa^{1/4}\,dS\), where \(\kappa\) is Gaussian curvature. Its continuous endpoint extension \(\mathcal A_*\) and the finite coefficient \(L\) are defined explicitly below. As \(\delta\downarrow0\),
\[
\boxed{\mathcal A(\varepsilon_*-\delta)
=\mathcal A_*+L\delta
-\frac{256\pi}{21\sqrt6}\left(\frac{\sqrt6}{3}\right)^{7/4}\delta^{7/4}
+o(\delta^{7/4}).}
\]
The nonanalytic term is strictly negative and its coefficient is approximately \(10.96516235477069\). More sharply,
\[
\frac{d^2}{d\delta^2}\mathcal A(\varepsilon_*-\delta)
\sim -\frac{21}{16}\frac{256\pi}{21\sqrt6}
\left(\frac{\sqrt6}{3}\right)^{7/4}\delta^{-1/4}.
\]
Thus the affine-surface-area profile extends continuously with a finite first derivative to its sharp convexity endpoint, but has no finite second derivative there.

## Assumptions and scope
Here \(S^2\) has its ordinary spherical area measure \(d\omega\), \(u=(x,y,z)\in S^2\), and
\[
q(u)=xyz,\qquad s(u)=x^2y^2+y^2z^2+z^2x^2,
\]
\[
D(u,\varepsilon)=1-10\varepsilon q(u)
+\varepsilon^2\bigl(4s(u)+16q(u)^2-1\bigr).
\]
Put \(D_*(u)=D(u,\varepsilon_*)\), \(b(u)=-\partial_\varepsilon D(u,\varepsilon_*)\), and
\[
\mathcal A_*:=\int_{S^2}D_*(u)^{3/4}\,d\omega,
\qquad L:=\frac34\int_{S^2}b(u)D_*(u)^{-1/4}\,d\omega.
\]
At the twelve zeros of \(D_*\), the integrand defining \(L\) is interpreted almost everywhere. It is locally integrable. No explicit evaluation of \(\mathcal A_*\) or \(L\) is asserted. The second derivative is taken for positive \(\delta\), where \(K_{\varepsilon_*-\delta}\) has strictly positive principal radii.

## Proof
**1. Convexity and its endpoint.** For \(f(u)=u_1u_2u_3\), the curvature-radius operator is \(R_\varepsilon=\nabla_{S^2}^2h_\varepsilon+h_\varepsilon I=I+\varepsilon A\), where \(A=\nabla_{S^2}^2f+fI\). At a unit normal \(u\) and a unit tangent \(v\), let \(w=u\times v\). The restriction of \(f\) to the great circle \(u\cos t+v\sin t\) contains only modes \(1\) and \(3\). Writing each coordinate as \(\sqrt{1-w_i^2}\cos(t-\theta_i)\), the amplitude of the third mode is exactly \(\frac14\prod_{i=1}^3\sqrt{1-w_i^2}\). Consequently
\[
|\langle A(u)v,v\rangle|\le
2\prod_i\sqrt{1-w_i^2}
\le2(2/3)^{3/2}=\frac{8}{3\sqrt6}.
\]
The last inequality is AM--GM, since \(\sum_i(1-w_i^2)=2\). Equality requires \(w_i^2=1/3\), and the third-mode phase then selects three minimum-curvature normals on each of the four distinct body-diagonal great circles. Explicitly, for positive \(\varepsilon\), they are the twelve signed permutations of \((2,1,1)/\sqrt6\) with positive coordinate product. At each, \(R_{\varepsilon_*}\) has eigenvalues \(0\) and \(3/4\). This proves independently that \(\varepsilon_*=3\sqrt6/8\) is the exact endpoint, and that these twelve normals are the only contacts where a principal radius vanishes.

**2. Exact Gauss determinant.** The ambient Hessian of \(xyz\) is the symmetric matrix whose off-diagonal entries are respectively \(z,y,x\). Restricting it to \(u^\perp\) and subtracting \(2q(u)I\) gives \(A(u)\). Its tangent trace and determinant are
\[
\operatorname{tr}A=-10q,\qquad
\det A=16q^2+4s-1.
\]
It follows that \(\det R_\varepsilon=D(u,\varepsilon)\). For positive curvature radii, the Gauss parametrization yields \(dS=D\,d\omega\) and \(\kappa=1/D\), whence
\[
\mathcal A(\varepsilon)=\int_{S^2}D(u,\varepsilon)^{3/4}\,d\omega.
\]
This formula extends continuously to \(\varepsilon_*\) by dominated convergence.

**3. Nondegenerate local zeros.** At \(u_0=(2,1,1)/\sqrt6\), use the orthonormal tangent frame \(v_1=(0,1,-1)/\sqrt2\) and \(v_2=(-1,1,1)/\sqrt3\). Set \(u(\xi,\eta)=\sqrt{1-\xi^2-\eta^2}\,u_0+\xi v_1+\eta v_2\). Exact differentiation gives
\[
D_*(u(\xi,\eta))
=\frac{27}{8}\xi^2+\frac9{16}\eta^2+O((\xi^2+\eta^2)^{3/2}),
\qquad b(u_0)=\frac{\sqrt6}{3}.
\]
Every other zero is related to this one by a signed coordinate permutation preserving \(xyz\), so has identical quadratic coefficients. These points are isolated, the quadratic forms are positive definite, and \(D_*\) is positive elsewhere.

**4. Second-derivative singularity.** Let \(F(\delta)=\mathcal A(\varepsilon_*-\delta)\), \(p=3/4\), and \(c(u)=4s+16q^2-1\). Then \(D(u,\varepsilon_*-\delta)=D_*(u)+\delta b(u)+\delta^2c(u)\). For \(\delta>0\) differentiation under the integral gives
\[
F''(\delta)=p(p-1)\!\int_{S^2}D^{p-2}(b+2\delta c)^2d\omega
+2p\!\int_{S^2}cD^{p-1}d\omega.
\]
The second integral stays bounded as \(\delta\downarrow0\), because \(D_*^{p-1}\) behaves as the locally integrable radius power \(r^{-1/2}\). Outside fixed disjoint neighborhoods of the twelve contacts the first integral is also bounded. Inside each neighborhood, rescale tangent coordinates by \(\sqrt\delta\). Dominated convergence after this rescaling, using the positive quadratic bound from step 3, shows that one contact contributes to the leading part of \(F''\) precisely
\[
p(p-1)a^2\frac{\pi}{\sqrt{bc}}\frac{(a\delta)^{p-1}}{1-p}
=-p\frac{\pi a^{p+1}}{\sqrt{bc}}\delta^{p-1},
\]
where \(a=\sqrt6/3\), \(b=27/8\), and \(c=9/16\) are **local constants** (not the function \(c(u)\) above). The planar integral follows from the substitution \(r^2=b\xi^2+c\eta^2\):
\[
\int_{\mathbb R^2}(a+r^2)^{p-2}d^2r
=\frac{\pi a^{p-1}}{1-p}.
\]
For rigor at large rescaled radii, a bound by a constant multiple of \((1+|v|^2)^{p-2}\) is integrable on \(\mathbb R^2\) since \(p<1\); on bounded coordinate patches the integrand is smooth away from the contacts. The spherical Jacobian equals \(1+O(\xi^2+\eta^2)\). Therefore summing twelve contributions yields
\[
F''(\delta)\sim
-\frac{9\pi a^{7/4}}{\sqrt{bc}}\,\delta^{-1/4}.
\]
The first derivative has the finite endpoint limit \(F'(0+)=L\) by integrability of \(D_*^{-1/4}\). Integrating the displayed second-derivative asymptotic twice yields
\[
F(\delta)=F(0)+L\delta
-\frac{12\pi a^{7/4}}{(7/4)\sqrt{bc}}\delta^{7/4}
+o(\delta^{7/4}).
\]
Finally \(\sqrt{bc}=9\sqrt6/16\), giving exactly the coefficient stated in the finding. The divergence of the negative second derivative proves the claimed loss of \(C^2\) regularity.

## Verification
The standalone file `verify_affine_cusp.py` reproduces the determinant identity from an independent orthonormal tangent matrix, checks each of the twelve endpoint contacts, symbolically differentiates the local spherical parametrization, and recomputes the sharp singular coefficient in two ways. It uses Python 3, SymPy, and NumPy. Run `python verify_affine_cusp.py` after extracting this file alongside the present text. The additional random-normal positivity sample in that program is illustrative only; the AM--GM great-circle proof above is the global argument. A symbolic checker or finite sample cannot by itself prove the infinite-dimensional limiting asymptotic.

## Relationship to prior work
Myroshnychenko--Ryabogin--Saroglou introduce the cubic constant-width family to demonstrate the exceptional threefold planar projection symmetry; their Theorem 5.4 establishes convexity for sufficiently small amplitudes, not an affine-surface-area endpoint expansion. The published sharp-convexity calculation for this precise family identifies the same endpoint and its twelve degeneracy normals, but contains no affine-surface-area cusp or fractional asymptotic. A separate published brightness calculation determines all planar projection areas, which are different functionals and do not imply the \(7/4\)-order affine-area asymptotic. Standard affine surface area theory supplies the Gauss-parametrized integral; the particular contact Hessian and exact singular coefficient require the calculation here.

## Limitations
This concerns the explicit cubic three-dimensional family, not all constant-width bodies or all threefold-projection exceptions. It is a one-sided expansion at the sharp positive convexity endpoint. The theorem does not evaluate the regular coefficients \(\mathcal A_*\) and \(L\) in elementary constants, nor assert a general stability inequality. General results about integrals with isolated quadratic degeneracies may contain equivalent machinery, and a differently worded earlier computation of this family's exact coefficient cannot be excluded solely by bibliographic search. Independent scientific validation has not been performed.

## References
1. S. Myroshnychenko, D. Ryabogin, C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1, first submitted 2026-09-23, especially Proposition 5.1 and Theorem 5.4, https://arxiv.org/abs/2609.27192.
2. *Sharp convexity threshold for the cubic constant-width support family*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-convexity-threshold-for-the-cubic-constant-width-support-f--b3681da24cdc.
3. *Exact brightness profile of the cubic threefold-projection exception*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-brightness-profile-of-the-cubic-threefold-projection-excep--a6ac80c263be.
4. M. N. Ivaki, *On the stability of the p-affine isoperimetric inequality*, Journal of Geometric Analysis (2014), https://doi.org/10.1007/s12220-013-9401-1 (support-function curvature and affine-area conventions).
