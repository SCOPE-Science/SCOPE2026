# Critical radial-mean covariogram convergence without boundary smoothness

## Finding
Let \(d\ge2\), and let \(K\subset\mathbb R^d\) be **any** convex body with \(0\in\operatorname{int}K\). For \(p>0\) and \(x\in\operatorname{int}(-K)\), define the radial \((-p)\)-mean \(M_{x,p}\) of \(K\) and \(K+x\) by
\[
\rho_{M_{x,p}}(u)^{-p}=\frac{\rho_K(u)^{-p}+\rho_{K+x}(u)^{-p}}2,
\qquad u\in S^{d-1},
\]
and put \(g_{K,p}(x)=\operatorname{vol}_d(M_{x,p})\). For every fixed \(\tau>0\), define the critically rescaled level set
\[
E_{p,\tau}=\bigl\{y\in p\operatorname{int}(-K):
 p[\operatorname{vol}_d(K)-g_{K,p}(y/p)]\le\tau\bigr\}.
\]
Denote by \(\nu(z)\) the outer unit normal to \(\partial K\), defined at \(\mathcal H^{d-1}\)-almost every boundary point. Then **without assuming smoothness, strict convexity, or polytopality**, the following convergence holds locally uniformly in \(y\):
\[
\boxed{\lim_{p\to\infty}p[\operatorname{vol}_d(K)-g_{K,p}(y/p)]
=\Phi_K(y)
:=\int_{\partial K}(z\cdot\nu(z))
\log\cosh\!\left(\frac{y\cdot\nu(z)}{2z\cdot\nu(z)}\right)
\,d\mathcal H^{d-1}(z).}
\]
Furthermore, for every \(\tau>0\), the complete sets converge **globally in Hausdorff distance**:
\[
\boxed{E_{p,\tau}\xrightarrow[p\to\infty]{d_H}
T_K(\tau):=\{y:\Phi_K(y)\le\tau\}.}
\]
The limit \(T_K(\tau)\) is a full-dimensional, compact, strictly convex, centrally symmetric body with smooth, strictly convex defining function. Thus the critical covariogram transition persists for arbitrary nonsmooth convex bodies, including simplices, polytopes with arbitrary facets, and mixed smooth/polyhedral bodies.

**Explicit polytopal specialization.** If \(K\) is a polytope whose facets have outward normals \(\nu_j\), areas \(A_j\), and positive support offsets \(h_j\) from the origin, then
\[
\boxed{\Phi_K(y)=\sum_j A_jh_j\log\cosh\!\left(\frac{y\cdot\nu_j}{2h_j}\right).}
\]
For the centered orthotope \(Q=\prod_{i=1}^d[-a_i,a_i]\) with \(a_i>0\) and \(V=\prod_i2a_i\), this becomes
\[
\Phi_Q(y)=V\sum_{i=1}^d\log\cosh\!\left(\frac{y_i}{2a_i}\right).
\]
In the special case \(a_i=a\), the **John and Löwner ellipsoids** of \(T_Q(\tau)\) are concentric Euclidean balls of respective radii
\[
\boxed{r_J=2a\sqrt d\,\operatorname{arcosh}\!\left(e^{\tau/(dV)}\right),\qquad
r_L=2a\,\operatorname{arcosh}\!\left(e^{\tau/V}\right).}
\]
The John ball touches the limit body precisely in the \(2^d\) signed body-diagonal directions; the Löwner ball touches precisely in the \(2d\) signed coordinate directions. This exact contact classification applies at every positive threshold. The cube's critical limit at one normalization was known previously; it is included here as a calibration, not claimed as a new limit theorem.

## Assumptions and scope
A convex body is compact, convex, and full-dimensional. The radial function is \(\rho_A(u)=\max\{t\ge0:tu\in A\}\) when \(0\in\operatorname{int}A\). The origin is fixed in the interior of \(K\); the radial construction is defined for translations keeping the origin in \(K+x\). The limits hold with dimension \(d\), body \(K\), and threshold \(\tau\) fixed while \(p\to\infty\). No rate uniform over all bodies, dimensions, or varying thresholds is asserted. Integrals over \(\partial K\) use standard Hausdorff measure and the almost-everywhere normal; no generalized curvature measure is needed. Lebesgue volume and unnormalized spherical surface measure are used consistently.

## Proof
**1. Radial translation derivative for rough bodies.** Choose \(r>0\) with \(rB_2^d\subset K\). The support inequalities imply, whenever \(\|x\|<r\),
\[
(1-\|x\|/r)K\subset K+x\subset(1+\|x\|/r)K.
\]
Hence \(\rho_{K+x}(u)/\rho_K(u)=1+O(\|x\|)\), uniformly in \(u\). For spherical-almost every \(u\), the radial boundary point \(z=\rho_K(u)u\) has a unique outer normal \(\nu(z)\) and a tangent hyperplane in the differentiability sense. Since \(z\cdot\nu(z)>0\), the tangent-plane expansion at the boundary point \(\rho_{K+ty}(u)u-ty\), whose displacement is \(O(t)\), gives
\[
\lim_{t\to0}\frac{\rho_{K+ty}(u)/\rho_K(u)-1}{t}
=\frac{y\cdot\nu(z)}{z\cdot\nu(z)}=:q_y(u).
\]
The almost-everywhere assertion follows from the standard differentiability theorem for convex boundaries and the bi-Lipschitz radial parametrization of a convex boundary about an interior point. The uniform radial sandwich supplies the necessary domination even at exceptional nonsmooth rays.

**2. Pointwise limit by a radial integral.** Write \(R=\rho_K(u)\), \(w_p=\rho_{K+y/p}(u)/R\), and
\[
c_p(u)=\frac{1+w_p(u)^{-p}}2.
\]
For almost every direction, \(p\log w_p\to q_y(u)\), so \(c_p\to(1+e^{-q_y})/2\). Using the exact polar volume formula,
\[
F_p(y):=p[\operatorname{vol}_d(K)-g_{K,p}(y/p)]
=\frac1d\int_{S^{d-1}}R^d\,p\bigl[1-c_p^{-d/p}\bigr]d\sigma(u).
\]
The uniform radial sandwich bounds \(|p\log w_p|\) on every bounded set of \(y\), and hence dominates the displayed integrand by an integrable constant multiple of \(R^d\). Dominated convergence yields
\[
\lim_{p\to\infty}F_p(y)
=\int_{S^{d-1}}R^d\left[\log\cosh\frac{q_y(u)}2-\frac{q_y(u)}2\right]d\sigma(u).
\]
For the radial map \(u\mapsto z=R u\), the cone-volume Jacobian is
\[
R^d\,d\sigma(u)=(z\cdot\nu(z))\,d\mathcal H^{d-1}(z)
\quad\text{almost everywhere}.
\]
The linear term cancels by the divergence theorem, \(\int_{\partial K}\nu(z)\,d\mathcal H^{d-1}(z)=0\). The remaining term is precisely \(\Phi_K(y)\).

**3. Locally uniform convergence.** For \(y_1,y_2\) in a fixed bounded set, the two translated bodies \(K+y_1/p\) and \(K+y_2/p\) contain a common centered ball of radius \(r/2\) for large \(p\). The same support sandwich applied to their difference gives
\[
\left|\log\frac{\rho_{K+y_1/p}(u)}{\rho_{K+y_2/p}(u)}\right|
\le C\|y_1-y_2\|/p
\]
uniformly in \(u\). The logarithm of a radial negative-power mean is \(1\)-Lipschitz in the logarithm of either input radius (its derivative is a logistic weight between zero and one). Consequently the functions \(F_p\) are equi-Lipschitz on every fixed ball. Their pointwise convergence to the continuous function \(\Phi_K\) is therefore locally uniform.

**4. No remote components of critical sublevels.** For any positive radii \(a,b\), their radial \((-p)\)-mean lies between \(\min(a,b)\) and \(2^{1/p}\min(a,b)\). Therefore, with the ordinary covariogram \(g_K(x)=\operatorname{vol}_d(K\cap(K+x))\),
\[
g_K(x)\le g_{K,p}(x)\le2^{d/p}g_K(x),\qquad
0\le \operatorname{vol}_d(K)-g_{K,p}(x).
\]
The last inequality follows independently from the power-mean bound \(M_{-p}(a,b)^d\le(a^d+b^d)/2\) and equality of the two volumes. Thus \(F_p(y)\le\tau\) implies
\[
p[\operatorname{vol}_d(K)-g_K(y/p)]\le\tau+Cp^{0}
\]
with \(C\) depending on \(d\) and \(\operatorname{vol}_d(K)\), not on \(p\). The classical covariogram has its unique maximum at zero. Its first directional deficit is the brightness norm
\[
\lim_{t\downarrow0}\frac{\operatorname{vol}_d(K)-g_K(tu)}{t}
=h_{\Pi K}(u)=\frac12\int_{\partial K}|u\cdot\nu(z)|\,d\mathcal H^{d-1}(z)>0.
\]
The convergence here is uniform in unit directions by the Lipschitz property of \(g_K\). Hence there is \(c_K>0\) such that the deficit exceeds \(c_K\|x\|\) near zero. Because \(K\) is bounded, this forces all \(y\) with \(F_p(y)\le\tau\) into a fixed compact ball for sufficiently large \(p\). Combined with local uniform convergence, it gives global Hausdorff convergence of the sublevel sets.

**5. Properties of the limiting body.** Differentiation under the integral is justified since \(z\cdot\nu(z)\ge r>0\). For any nonzero \(v\),
\[
v^\mathsf T\nabla^2\Phi_K(y)v
=\frac14\int_{\partial K}
\frac{(v\cdot\nu(z))^2}{z\cdot\nu(z)}
\operatorname{sech}^2\!\left(\frac{y\cdot\nu(z)}{2z\cdot\nu(z)}\right)
\,d\mathcal H^{d-1}(z)>0.
\]
Indeed, the normal measure of a full-dimensional bounded convex body cannot be supported on a great subsphere. Evenness is immediate, and \(\log\cosh t\ge |t|-\log2\) gives the coercive bound
\[
\Phi_K(y)\ge h_{\Pi K}(y)-d\operatorname{vol}_d(K)\log2.
\]
Thus every positive sublevel is a compact, centrally symmetric, strictly convex body with smooth defining boundary. Its interior dilates give the approximation from within in the Hausdorff argument.

**6. Polytopes and exact cubical contacts.** On each polytope facet \(z\cdot\nu_j=h_j\) is constant, giving the displayed finite sum. For a cube \(Q=[-a,a]^d\), its signed coordinate facets yield \(\Phi_Q(y)=V\sum_i\log\cosh(y_i/(2a))\), where \(V=(2a)^d\). The function \(s\mapsto\log\cosh\sqrt s\) is strictly concave for \(s>0\), since \(\tanh t/t\) is strictly decreasing. At fixed Euclidean radius \(\|y\|=r\), strict concavity and majorization therefore give
\[
V\log\cosh\frac{r}{2a}
\le\Phi_Q(y)\le
Vd\log\cosh\frac{r}{2a\sqrt d}.
\]
Equality on the left occurs exactly along signed coordinate axes and on the right exactly along signed body diagonals. Solving the two equality equations gives the stated inradius and outradius. The unique John and Löwner ellipsoids must be centered Euclidean balls by the full signed-permutation symmetry of the body, so their radii are these sharp extrema. Strictness identifies all contact directions.

## Verification
An independently implemented angular quadrature evaluates the radial-mean volume before taking the limit and compares it against the surface-normal formula for both a nonsymmetric triangle and a square at multiple \(p\) values. The finite checks verify the predicted limiting values and decreasing errors, together with the exact cubical contact formulas. The accompanying standard-library Python program can be executed with \(\texttt{python3 verify.py}\). The all-dimensional and all-body assertions follow from the proof, not from numerical sampling.

## Relationship to prior work
Haddad, Jiménez and Resende (arXiv:2610.11700, first posted October 8, 2026) introduced this radial mean, established the critical transition for **\(C^3\)** convex boundaries, and identified the \(\log\cosh\) boundary functional. Their formula and smooth theorem are the starting point, not claimed as new. The contribution here is that **the actual radial-mean critical limit and global Hausdorff convergence hold for every convex body** with no regularity or strict-convexity hypothesis; the proof uses almost-everywhere normals and the ordinary covariogram's universal first variation. Earlier exact cubical convergence and related geometric properties of the integral-defined bodies have also been recorded, but do not give the general nonsmooth convergence statement. The projection-body derivative of the ordinary covariogram is classical (Matheron), and a modern account for arbitrary convex bodies is supplied by Haddad et al., *Affine isoperimetric inequalities for higher-order projection and centroid bodies*.

## Limitations
The statement concerns the critical scaling \(\delta=\tau/p\), with fixed body, dimension and positive threshold. It does not prove the quadratic subcritical regime for arbitrary nonsmooth bodies, quantitative rates of Hausdorff convergence uniform in body geometry, or finite-\(p\) differentiability of the smoothed covariogram. The cubical radii are for the **limiting body**, not the finite-\(p\) level sets. Historical priority beyond the inspected sources remains open, and no independent audit has been performed.

## References
1. J. Haddad, C. H. Jiménez, M. Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1 (2026-10-08), https://arxiv.org/html/2610.11700v1.
2. J. Haddad, D. Langharst, E. Putterman, M. Roysdon, D. Ye, *Affine isoperimetric inequalities for higher-order projection and centroid bodies*, Mathematische Annalen 393 (2025), DOI 10.1007/s00208-025-03271-x, https://link.springer.com/article/10.1007/s00208-025-03271-x.
3. Classical cone-volume change of variables, almost-everywhere differentiability of convex boundaries, and Matheron's covariogram first-variation identity; statements and normalizations are reconstructed in the proof above.
