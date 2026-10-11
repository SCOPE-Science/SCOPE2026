# Sharp convexity and volume hierarchy of one-mode zonal constant-width solids

## Finding
Fix any unit axis \(e\in\mathbb S^2\). For an odd integer \(\ell\ge3\), write \(P_\ell\) for the Legendre polynomial normalized by \(P_\ell(1)=1\), and consider
\[
h_{\ell,\varepsilon}(u)=1+\varepsilon P_\ell(u\cdot e),\qquad u\in\mathbb S^2.
\]
This is the support function of a full-dimensional convex body of constant width \(2\) **if and only if**
\[
|\varepsilon|\le \frac{2}{\ell(\ell+1)-2}.
\]
For every admissible coefficient its volume is
\[
\operatorname{Vol}(K_{\ell,\varepsilon})=
\frac{4\pi}{3}-\frac{2\pi[\ell(\ell+1)-2]}{2\ell+1}\,\varepsilon^2.
\]
Consequently the minimum for fixed degree, attained only at the two endpoint amplitudes, is
\[
V_\ell^{\min}=\frac{4\pi}{3}-\frac{8\pi}{(2\ell+1)[\ell(\ell+1)-2]}.
\]
These minima increase strictly along the odd degrees \(\ell=3,5,7,\ldots\). Among all single nontranslational odd zonal Legendre modes the unique minimizing *shape up to rigid motion* is the degree-three endpoint body; its width-two volume is \(128\pi/105\). The opposite signs are congruent by reflection in the equatorial plane.

A geometric distinction occurs at the convexity boundary. At the positive endpoint, the meridional principal radius vanishes at polar angles \(\theta=0,2\pi/3\) for degree \(3\), but **only** at \(\theta=0\) for every odd degree \(\ell\ge5\). For the negative endpoint the zero latitudes are their reflected angles \(\pi-\theta\). In particular, the degree-three boundary body has a circle of degenerate meridional curvature, whereas the higher-degree boundary bodies have only an axial degeneracy.

## Assumptions and scope
Here \(\theta=\arccos(u\cdot e)\in[0,\pi]\) is the polar angle and the support function is taken on the unit sphere in \(\mathbb R^3\). A smooth function \(h\) is the support function of a compact convex body precisely when \(\nabla^2_{\mathbb S^2}h+hI\) is nonnegative definite. For the axially symmetric functions above its principal radii are \(\rho_m=h+h_{\theta\theta}\) and \(\rho_a=h+\cot\theta\,h_\theta\), continuously extended at the poles. The index \(\ell=1\) is excluded because it is a translation of a ball, not a nontrivial change of shape. The result concerns exactly one odd zonal spherical-harmonic mode, not arbitrary sums of harmonics or arbitrary constant-width bodies.

## Proof
**1. A positive cosine expansion gives the sharp meridional test.** The Legendre generating function factors as
\[
(1-2t\cos\theta+t^2)^{-1/2}=(1-te^{i\theta})^{-1/2}(1-te^{-i\theta})^{-1/2}.
\]
Let \(c_j=\binom{2j}{j}4^{-j}>0\). Comparing the coefficient of \(t^\ell\), for odd \(\ell\) we obtain
\[
P_\ell(\cos\theta)=\sum_{\substack{1\le k\le\ell\\k\ \mathrm{odd}}}a_{\ell,k}\cos(k\theta),\qquad
 a_{\ell,k}=2c_{(\ell+k)/2}c_{(\ell-k)/2}>0.
\]
The coefficients sum to \(1\). Define
\[
C_\ell=\sum_{k\ge3}(k^2-1)a_{\ell,k}.
\]
At \(\theta=0\), using \(P_\ell'(1)=\ell(\ell+1)/2\), differentiation gives
\[
C_\ell=\frac{\ell(\ell+1)}{2}-1>0.
\]
It follows that
\[
\rho_m(\theta)=1-\varepsilon\sum_{k\ge3}(k^2-1)a_{\ell,k}\cos(k\theta)\ge1-|\varepsilon|C_\ell.
\]
If \(\varepsilon>1/C_\ell\), the value of \(\rho_m\) at \(\theta=0\) is negative. If \(\varepsilon<-1/C_\ell\), its value at \(\theta=\pi\) is negative, since all relevant \(k\) are odd. Hence the claimed amplitude interval is necessary and sufficient for \(\rho_m\ge0\).

**2. Meridional convexity implies full convexity in this axial family.** Set
\[
a(\theta)=h(\theta)\sin\theta+h_\theta(\theta)\cos\theta.
\]
The smooth pole conditions give \(a(0)=a(\pi)=0\), and \(a'(\theta)=\rho_m(\theta)\cos\theta\). If \(0<\theta\le\pi/2\), then \(a(\theta)=\int_0^\theta\rho_m(t)\cos t\,dt\ge0\). If \(\pi/2\le\theta<\pi\), then \(a(\theta)=-\int_\theta^\pi\rho_m(t)\cos t\,dt\ge0\). Thus \(\rho_a(\theta)=a(\theta)/\sin\theta\ge0\). At each pole the two curvatures agree by rotational symmetry. Both principal radii are therefore nonnegative throughout, proving sufficiency. Moreover \(P_\ell\) is odd and \(|P_\ell(x)|\le1\) on \([-1,1]\); the admissible range has \(|\varepsilon|\le1/5\), so \(h\ge4/5>0\), guaranteeing that the resulting body contains a positive-radius ball. Finally, \(h(u)+h(-u)=2\) proves constant width.

**3. Exact volume and strict hierarchy.** Put \(q=P_\ell(u\cdot e)\), and \(\lambda=\ell(\ell+1)\). Spherical harmonic identities give
\[
\Delta_{\mathbb S^2}q=-\lambda q,\qquad\int_{\mathbb S^2}q^2\,d\sigma=\frac{4\pi}{2\ell+1},\qquad\int q\,d\sigma=0.
\]
For \(A=\nabla^2q+qI\), integrated Bochner identities yield
\[
\int\operatorname{tr}A\,d\sigma=0,\quad
\int\det A=-\frac{\lambda-2}{2}\int q^2,\quad
\operatorname{tr}A=(2-\lambda)q.
\]
Using the support-function volume identity
\[
3\operatorname{Vol}(K)=\int_{\mathbb S^2}h\det(\nabla^2h+hI)\,d\sigma,
\]
and expanding \(h=1+\varepsilon q\), the cubic term vanishes because \(q\) and \(A\) change sign under the antipodal map (while \(\det A\) does not). The resulting quadratic coefficient is \(-\frac12(\lambda-2)\int q^2\), proving the displayed volume formula. The coefficient is strictly negative for \(\ell\ge3\), so the endpoints minimize volume at fixed degree. Since the denominator \((2\ell+1)[\ell(\ell+1)-2]\) is strictly increasing for \(\ell\ge3\), these endpoint minima increase strictly across all admissible odd degrees. At \(\ell=3\), \(\varepsilon=\pm1/5\) gives \(128\pi/105\).

**4. Boundary meridional-curvature degeneracy.** At the positive endpoint, equality \(\rho_m(\theta)=0\) requires \(\cos(k\theta)=1\) for every \(k\ge3\) appearing with positive coefficient. When \(\ell=3\), only \(k=3\) appears, so the zeros in \([0,\pi]\) are \(0,2\pi/3\). For every odd \(\ell\ge5\), both \(k=3\) and \(k=5\) occur with positive coefficients. Simultaneous equality \(\cos3\theta=\cos5\theta=1\) then forces \(\theta=0\) on \([0,\pi]\), since \(3\) and \(5\) are coprime. Reflection gives the negative endpoint cases.

## Verification
A companion exact-arithmetic program (`verify.py`) reconstructs the cosine expansion, the threshold coefficient and the volume integral directly from the two support radii for degrees \(3,5,7,9\); it also checks the stated first endpoint volumes. The program is a finite consistency test. The uniform all-degree theorem follows from the preceding identities and positivity proof, not from finite enumeration.

## Relationship to prior work
Hynd's 2025 study of extreme three-dimensional constant-width bodies develops the support-radius viewpoint and characterizes extremality of axially symmetric bodies by their planar generators, but does not give the sharp all-degree zonal one-mode convexity, volume hierarchy or degenerate-curvature latitudes. Antunes and Bogosel (2018) explicitly formulate three-dimensional constant-width volume as a quadratic form of spherical-harmonic coefficients; the volume identity above is a specialization of that known spectral formula, not independently novel. The new content is the **exact nonlinear admissible amplitude for every odd zonal Legendre mode**, followed by the complete and sharp infinite-degree extremal and meridional-degeneracy classification. General cubic harmonic curvature bounds and other symmetry classes do not imply this one-mode all-degree statement.

## Limitations
This theorem makes no claim about the global minimum-volume constant-width solid (the Blaschke–Lebesgue problem), about combinations of Legendre modes, about non-zonal harmonics, or about extremality under arbitrary Minkowski decompositions. All original-status statements are limited to the literature and research records actually inspected; an unindexed equivalent treatment remains possible. The lower volume of the one-mode degree-three body is not claimed to beat the volumes of Meissner bodies.

## References
1. R. Hynd, *On extreme constant width bodies in \(\mathbb R^3\)*, arXiv:2501.16940v1, first public 2025-01-28, especially §§4–5, https://arxiv.org/html/2501.16940v1.
2. P. Antunes and B. Bogosel, *Parametric Shape Optimization using the Support Function*, arXiv:1809.00254v3, especially §4.2, formulas (13)–(15) and §6.3, https://arxiv.org/html/1809.00254v3.
