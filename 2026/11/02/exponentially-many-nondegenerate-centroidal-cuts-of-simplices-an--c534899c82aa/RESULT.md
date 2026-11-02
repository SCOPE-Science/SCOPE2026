# Exponentially many nondegenerate centroidal cuts of simplices and their vertex truncations

## Finding
Let \(n\ge4\), let \(S\subset\mathbb R^n\) be any nondegenerate \(n\)-simplex with vertices \(v_1,\ldots,v_m\), where \(m=n+1\), and let \(\lambda_i\) be its affine barycentric coordinates. Its centroid is \(p\), characterized by \(\lambda_i(p)=1/m\). For a parameter \(0\le\varepsilon<1/m\), define the symmetrically vertex-truncated simplex
\[
K_\varepsilon=\{x\in S:\lambda_i(x)\le1-\varepsilon\text{ for every }i\}.
\]
For every nonempty proper subset \(A\subset\{1,\ldots,m\}\) of size \(k\), put \(l=m-k\) and
\[
H_A=\left\{x:\sum_{i\in A}\lambda_i(x)=\frac{k}{m}\right\}.
\]
Then \(p\) is the centroid both of \(K_\varepsilon\) and of its full-dimensional hyperplane section \(K_\varepsilon\cap H_A\). Moreover, \(H_A=H_{A^c}\), and all other pairs \(H_A,H_B\) with \(B\notin\{A,A^c\}\) are different. Thus **every** \(K_\varepsilon\), including a genuine nonsimplicial truncation whenever \(\varepsilon>0\), has at least \(2^n-1\) different centroidal hyperplane sections through its centroid.

The specified directions are nondegenerate critical points of the oriented halfspace-volume function, with **exact Morse indices and Hessian**. To state these, identify normals with coefficient vectors \(a\in E=\{a\in\mathbb R^m:\sum_i a_i=0\}\) and define
\[
F_\varepsilon(a)=\frac{\operatorname{Vol}_n\{x\in K_\varepsilon:\sum_i a_i\lambda_i(x)\ge0\}}{\operatorname{Vol}_n(K_\varepsilon)},\qquad a\in E\setminus\{0\}.
\]
For the oriented normal \(a^A\), whose entries are \(l\) on \(A\) and \(-k\) on \(A^c\), let \(B_{k,l}\) be the upper tail \(\mathbb P(\mathrm{Beta}(k,l)\ge k/m)\). Then
\[
F_\varepsilon(a^A)=\frac{B_{k,l}-k\varepsilon^n}{1-m\varepsilon^n},\qquad
B_{k,l}=\sum_{j=0}^{k-1}\binom{m-1}{j}\left(\frac{k}{m}\right)^j\left(\frac{l}{m}\right)^{m-1-j}.
\]
The tangent space to the oriented normal ray, within \(E\), is
\[
T_A=\left\{v\in E:\sum_{i\in A}v_i=\sum_{j\in A^c}v_j=0\right\}.
\]
For every \(v\in T_A\), write \(f_{k,l}(y)=y^{k-1}(1-y)^{l-1}/\mathrm B(k,l)\) for the beta density. Then the exact second differential is
\[
D^2F_\varepsilon(a^A)[v,v]=
\frac{f_{k,l}(k/m)}{(1-m\varepsilon^n)m^2}
\left[\frac{\sum_{j\in A^c}v_j^2}{k(l+1)}-\frac{\sum_{i\in A}v_i^2}{l(k+1)}\right].
\]
Its negative and positive eigenspace dimensions are respectively \(k-1\) and \(l-1\); in particular its nullity is zero on \(T_A\). Reversing the orientation replaces \(k\) with \(l\) and reverses the signs. The results are affine invariant; no regular-simplex assumption is needed.

## Assumptions and scope
The centroid of a hyperplane section is computed using induced \((n-1)\)-dimensional Lebesgue measure on that hyperplane. All bodies and sections are nondegenerate and full-dimensional within their affine hulls. The cut is *centroidal* if the section centroid coincides with the body's centroid. The normal-coordinate Hessian is taken in \(E\) at the explicitly normalized representative \(a^A\), not in physical Euclidean unit-normal coordinates. An invertible affine change of the simplex preserves the cuts and the signs of the transverse Hessian, but not numerical Euclidean eigenvalues. No assertion is made that the displayed \(2^n-1\) cuts exhaust all centroidal cuts in dimensions \(n\ge4\).

## Proof
**1. Affine reduction and distinct sections.** An invertible affine map carries \(S\) to the standard simplex \(\{\lambda_i\ge0,\ \sum_i\lambda_i=1\}\) and carries barycenters of solids and sections to barycenters. The subgroup of affine vertex permutations preserving \(A\) acts transitively on the \(k\) barycentric coordinates in \(A\) and separately on the \(l\) coordinates in \(A^c\). It preserves \(K_\varepsilon\cap H_A\), so the section centroid has constant barycentric coordinate on each group. On \(H_A\), the two group sums are \(k/m\) and \(l/m\), whence each coordinate of its centroid is \(1/m\). The same full permutation group preserves \(K_\varepsilon\), whose centroid is consequently \(p\). A two-level normal determines its positive-coordinate subset uniquely up to complement, proving there are \((2^m-2)/2=2^n-1\) distinct listed hyperplanes.

**2. Exact truncation and halfspace mass.** In the original simplex, the cap \(\{\lambda_i>1-\varepsilon\}\) is homothetic to the full simplex with linear scale \(\varepsilon\), so its relative volume is \(\varepsilon^n\). For \(\varepsilon<1/m\), the \(m\) caps are disjoint and \(\operatorname{Vol}(K_\varepsilon)/\operatorname{Vol}(S)=1-m\varepsilon^n\). Every point of \(S\cap H_A\) has \(\lambda_i\le k/m\) for \(i\in A\) and \(\lambda_j\le l/m\) for \(j\notin A\). Both are at most \((m-1)/m<1-\varepsilon\); hence the section is **literally unchanged** by truncation. Furthermore, for all normals sufficiently close to \(a^A\), each removed vertex cap stays entirely on its original side of the moving central hyperplane. Exactly \(k\) caps are on the positive side, so locally
\[
F_\varepsilon(a)=\frac{F_0(a)-k\varepsilon^n}{1-m\varepsilon^n}.
\]
This identity implies both the value formula and the Hessian scaling once the untruncated case is established.

**3. Beta decomposition and critical values.** Let \(X=(X_1,\ldots,X_m)\) be uniform on the standard simplex, meaning \(X\sim\mathrm{Dirichlet}(1,\ldots,1)\). The sum \(Y=\sum_{i\in A}X_i\) has the \(\mathrm{Beta}(k,l)\) law. Because \(\sum_i a_i^A X_i=mY-k\), the halfspace event is \(Y\ge k/m\). The displayed binomial formula is the elementary integral of the integer-parameter beta density. Group-permutation symmetry, or differentiation of the next formula, makes \(a^A\) a stationary direction.

**4. Full transverse Hessian.** Fix an arbitrary \(v\in T_A\). Conditional on \(Y\), the within-group normalized vectors \((X_i/Y)_{i\in A}=U\) and \((X_j/(1-Y))_{j\in A^c}=V\) are independent uniform Dirichlet vectors and independent of \(Y\). Define the bounded random variables \(Z_+=\sum_{i\in A}v_iU_i\) and \(Z_-=\sum_{j\in A^c}v_jV_j\). Since the sums of perturbation coefficients within each group vanish,
\[
\mathbb EZ_+=\mathbb EZ_-=0,\quad
\mathbb EZ_+^2=\frac{\sum_{i\in A}v_i^2}{k(k+1)},\quad
\mathbb EZ_-^2=\frac{\sum_{j\in A^c}v_j^2}{l(l+1)},\quad
\mathbb E(Z_+Z_-)=0.
\]
The perturbed halfspace inequality is
\[
mY-k+t\{YZ_++(1-Y)Z_-\}\ge0.
\]
For all sufficiently small real \(t\), it is equivalent to \(Y\ge q(t)\), where
\[
q(t)=\frac{k-tZ_-}{m+t(Z_+-Z_-)}.
\]
Writing \(\Delta=Z_+-Z_-\), direct expansion gives
\[
q'(0)=-\frac{kZ_++lZ_-}{m^2},\qquad
\frac12q''(0)=\frac{\Delta(kZ_++lZ_-)}{m^3}.
\]
If \(G(s)=\mathbb P(Y\ge s)\), then \(G'=-f_{k,l}\) and \(G''=-f'_{k,l}\). Taking expectations in \(G(q(t))\), using independent centered \(Z_+,Z_-\), and using
\[
\frac{f'_{k,l}(k/m)}{f_{k,l}(k/m)}=\frac{m(k-l)}{kl},
\]
yields exactly the displayed quadratic Hessian for \(\varepsilon=0\). The first derivative vanishes. Differentiation under expectation is valid because all variables are bounded and \(q(t)\) remains in a compact subinterval of \((0,1)\). The two coefficients of the quadratic form have strictly opposite signs; the direct-sum dimensions are \(k-1\) and \(l-1\). Local truncation scaling from step 2 proves the full assertion for \(\varepsilon>0\). Since \(F\) is homogeneous of degree zero in \(a\), the radial direction is excluded; on the tangent \(T_A\), nondegeneracy is exact.

## Verification
Run the supplied `verify.py` in an environment with Python 3, NumPy and SciPy: `python verify.py`. It checks rational beta-tail identities, all dimension/sign formulas for small and moderate dimensions, independent numerical Dirichlet quadrature of both the positive- and negative-block Hessian coefficients, and the exact truncation geometry. Its actual execution concluded `ALL_CHECKS_PASSED`. The infinite-dimensional-in-parameter assertions and the exponential cut count are proved by the symbolic argument above; finite computation is not offered as a universal proof.

## Relationship to prior work
Patáková, Tancer, and Wagner (2020) prove that centroidal cuts correspond to critical points of the oriented halfspace-volume function (their Proposition 11) and give general lower bounds on barycentric hyperplanes. The new statement is the all-dimensional exact transverse Hessian and exponential collection of explicit nondegenerate cuts for the simplex and its strictly truncated polytopal family, not a claim to rediscover that general critical-point equivalence.

Myroshnychenko, Tatarko, and Yaskin (2024) determine a very different quantity: the minimum number of centroidal hyperplane sections over **all** convex bodies in sufficiently high dimensions. Their universal-minimum result does not bound the number from above for a simplex or describe its local critical-point spectrum.

The public 2026 record titled *Exactly seven centroidal hyperplane sections of every tetrahedron* establishes completeness in dimension three and already covers the seven-partition count there. This result therefore restricts its new substantive claim to dimensions at least four, adds the complete signed Hessian to every constructed partition cut, and proves persistence under positive symmetric vertex truncation. It does not infer an all-dimensional completeness theorem from the three-dimensional classification. Dirksen's work on central simplex-section volumes concerns extrema of **section volume**, a different functional from the halfspace-volume fractions and their centroidal stationary cuts here.

## Limitations
No completeness of the centroidal-direction list is proved for \(n\ge4\); additional centroidal directions could exist. The Hessian uses barycentric coefficient coordinates, so its *signature*, not its numeric eigenvalues, is affine invariant. The explicit truncation interval is \(0\le\varepsilon<1/(n+1)\); no claim extends the unchanged-section argument past its boundary. No quantitative lower bound on the number of centroidal cuts is claimed for arbitrary nonsymmetric convex bodies, and the result does not settle a universal Grünbaum–Loewner minimum problem.

## References
- Z. Patáková, M. Tancer, and U. Wagner, *Barycentric Cuts Through a Convex Body*, arXiv:2003.13536 (first submitted 2020-03-27); SoCG 2020, Article 62. Proposition 11 identifies critical oriented halfspace cuts with barycentric hyperplanes.
- S. Myroshnychenko, K. Tatarko, and V. Yaskin, *Answers to Questions of Grünbaum and Loewner*, arXiv:2404.15188 (first submitted 2024-04-23), particularly its definition of \(\mu(K)\) and high-dimensional global-minimum theorem.
- *Exactly seven centroidal hyperplane sections of every tetrahedron*, public published-finding corpus record 2026/10/4/SCOPE-exactly-seven-centroidal-hyperplane-sections-of-every-tetrahedro--d1e5b52777a2, especially its dimension-three completeness proof and its explicit limitation to that dimension.
- H. Dirksen, *Sections of the Regular Simplex – Volume Formulas and Estimates*, arXiv:1509.06408 (first submitted 2015-09-21); Math. Nachr. 290 (2017), 2567–2584 (distinct section-volume functional).
