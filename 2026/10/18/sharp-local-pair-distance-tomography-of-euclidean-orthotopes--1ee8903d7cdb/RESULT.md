# Sharp local pair-distance tomography of Euclidean orthotopes

## Finding

Fix an integer \(d\ge3\), and consider any Euclidean orthotope \(Q=\prod_{i=1}^{d}[0,a_i]\subset\mathbb R^d\) with all \(a_i>0\). Let \(X,Y\) be independent uniformly distributed points of \(Q\), and put
\[
\omega_d=\frac{\pi^{d/2}}{\Gamma(1+d/2)},\qquad R=\left(\frac{\prod_i a_i}{\omega_d}\right)^{1/d},\qquad D_Q(\rho)=\mathbb P\{\|X-Y\|_2/R<\rho\}.
\]
Define \(b_i=R/a_i\), with \(e_k(b)\) the degree-\(k\) elementary symmetric polynomial and \(e_0=1\). For the entire interval \(0\le\rho<\min_i b_i^{-1}\), the following is an **exact polynomial identity**:
\[
\boxed{D_Q(\rho)=\sum_{k=0}^{d}(-1)^k \frac{\Gamma(1+d/2)}{\pi^{k/2}\Gamma(1+(d+k)/2)}\,e_k(b)\,\rho^{d+k}.}\tag{1}
\]
Moreover \(e_d(b)=1/\omega_d\), independently of the orthotope. Consequently, **exactly the first \(d-1\) nontrivial local Taylor coefficients** (those of \(\rho^{d+1},\ldots,\rho^{2d-1}\)) determine the unordered ratios \(\{a_i/R\}_{i=1}^d\). For every \(0\le m<d-1\), the first \(m\) of those coefficients fail to determine the ratios, even locally at every orthotope with pairwise distinct side lengths.

The recovery is optimally stable in the following uniform sense. For any \(0<u<v<\infty\), on the family of ratio vectors satisfying \(u\le b_i\le v\), write \(t_k(Q)=[\rho^{d+k}]D_Q(\rho)\). There is a constant \(C_{d,u,v}\) such that for any two orthotopes in this family,
\[
\boxed{\min_{\sigma\in S_d}\max_i\left|\frac{a_i}{R}-\frac{a'_{\sigma(i)}}{R'}\right|
\le C_{d,u,v}\left(\max_{1\le k<d}|t_k(Q)-t_k(Q')|\right)^{1/d}.}\tag{2}
\]
No exponent larger than \(1/d\) works uniformly in any neighborhood of the cube. At orthotopes with distinct side ratios, the inverse map is locally Lipschitz.

Thus a normalized radial *two-point distance* germ is a complete and minimally redundant similarity invariant for arbitrary-dimensional Euclidean orthotopes, despite not recovering general convex bodies.

## Assumptions and scope

The dimension \(d\) is an arbitrary fixed integer at least three. The orthotope is nondegenerate with mutually orthogonal positive edge lengths. The sampling points are independent and distributed according to normalized volume, not boundary measure, chord measure, or random-plane projection. The ball radius \(R\) is the radius of a Euclidean ball of the same volume, following the normalization of [1]. Distances are Euclidean. An orthotope's axis order, translation, orthogonal orientation, and common dilation cannot be recovered and are intentionally excluded; congruence after a scale normalization is recovered. The exact polynomial holds strictly before its first coordinate-overlap threshold; no all-radii polynomial is claimed. Stability is for exact population coefficients with compact positive ratio bounds and has no finite-sample assertion.

## Proof

**1. Local covariogram and exact coefficients.** The overlap \(g_Q(z)=\operatorname{vol}_d(Q\cap(Q+z))\) factors coordinatewise:
\[
g_Q(z)=\prod_{i=1}^d(a_i-|z_i|)_+.
\]
Since \(g_Q(z)/\operatorname{vol}_d(Q)^2\) is the density of \(X-Y\), the change of variables \(z=Ry\) and \(R^d/\operatorname{vol}_d(Q)=1/\omega_d\) give
\[
D_Q(\rho)=\frac1{\omega_d}\int_{\|y\|_2<\rho}\prod_{i=1}^d(1-b_i|y_i|)_+\,dy.
\tag{3}
\]
For \(\rho<1/\max_i b_i\), every factor is nonnegative on this ball. Expand the finite product over coordinate subsets. Rotational symmetry makes the monomial integral depend only on subset size \(k\), and the gamma integral yields
\[
\int_{\|y\|_2<\rho}\prod_{i=1}^k|y_i|\,dy
=\frac{\pi^{(d-k)/2}}{\Gamma(1+(d+k)/2)}\rho^{d+k}.
\tag{4}
\]
For completeness, integrate \(\prod_{i=1}^k|y_i|e^{-\|y\|_2^2}\) over \(\mathbb R^d\) by coordinates to get \(\pi^{(d-k)/2}\); in spherical coordinates the radial gamma factor is \(\Gamma((d+k)/2)/2\). Dividing the resulting sphere integral by \(d+k\) proves (4). Substituting it into (3) proves (1), with no remainder term on the displayed interval.

**2. Constructive finite reconstruction.** By definition,
\[
\prod_{i=1}^db_i=\frac{R^d}{\prod_i a_i}=\frac1{\omega_d}.
\tag{5}
\]
Every coefficient of \(\rho^{d+k}\), for \(1\le k\le d-1\), is a known nonzero scalar multiple of \(e_k(b)\); the leading coefficient is \(1\), and the degree-\(2d\) coefficient is fixed by (5). Thus the given \(d-1\) numbers determine the monic polynomial
\[
P_b(z)=\prod_{i=1}^d(z-b_i)=z^d-e_1(b)z^{d-1}+e_2(b)z^{d-2}-\cdots+(-1)^d/\omega_d.
\tag{6}
\]
Its positive real roots with multiplicities are precisely the \(b_i\); taking reciprocals recovers the side ratios \(a_i/R\). No assumptions of generic distinctness are needed for uniqueness.

**3. Sharp minimality.** Consider a tuple of distinct positive \(b_i\) satisfying (5). For \(m<d-1\), perturb only the coefficient \(e_{m+1}\) in (6), leaving all \(e_1,\ldots,e_m\) and \(e_d=1/\omega_d\) fixed. The original polynomial has \(d\) simple positive roots, so by continuity and the real implicit-function theorem, every sufficiently small real coefficient perturbation still has \(d\) distinct positive roots near them. The new roots define a different positive side-ratio multiset of product \(\omega_d\) and hence a noncongruent orthotope shape. Its first \(m\) nontrivial coefficients are exactly unchanged. This also proves local families of dimension at least \(d-1-m\) in a neighborhood of every distinct-root box. When \(m=0\), vary \(e_1\); when \(m=d-2\), vary \(e_{d-1}\). In either case \(e_d\) stays fixed.

**4. Compact uniform inverse stability.** Fix \(u\le b_i\le v\) and similarly for \(b'_i\). Let \(\delta=\max_{1\le k\le d-1}|t_k(Q)-t_k(Q')|\). All degree-\(d\) root-polynomial coefficients differ by at most \(C_0\delta\), because the leading and constant coefficients agree and the remaining coefficients are nonzero scalar multiples of the measured coefficients. On a common bounded complex disk the two polynomials therefore differ by at most \(C_1\delta\). For sufficiently small \(\delta\), draw complex radius-\(r\) disks around the roots of the first polynomial, taking \(r=(2C_1\delta)^{1/d}\). At every boundary point of a connected component of their union, each distance to a root is at least \(r\), so \(|P_b(z)|\ge r^d>C_1\delta\). Rouché's theorem gives exactly the same number of roots, counting multiplicity, of the second polynomial in each component. Every component has diameter at most \(2dr\); hence the two root multisets can be matched at maximum distance at most \(2dr\). Larger discrepancies are handled by increasing the constant, using compactness. Finally the reciprocal map is \(u^{-2}\)-Lipschitz on \([u,v]\), establishing (2). When all roots are distinct, the coefficient-to-root Jacobian is a nonsingular Vandermonde matrix; the implicit-function theorem supplies local Lipschitz recovery.

**5. Optimality of the exponent.** Choose any \(d\) distinct real numbers \(x_1,\ldots,x_d\), and let \(f(z)=\prod_i(z-x_i)\). For some sufficiently small nonzero real \(\tau\), \(f(z)+\tau\) also has \(d\) distinct real roots \(y_1,\ldots,y_d\). The two root multisets differ, while their elementary symmetric functions of orders \(1,\ldots,d-1\) agree exactly, because only the constant coefficient changed. For small positive \(\varepsilon\), put \(q_i=1+\varepsilon x_i\) and \(q'_i=1+\varepsilon y_i\), all positive. The identity for elementary symmetric functions of a shifted tuple shows \(e_k(q)=e_k(q')\) exactly for every \(k<d\), whereas \(\prod_iq_i-\prod_iq'_i=c\varepsilon^d\), with \(c\ne0\). Normalize them to the required fixed product by setting
\[
b_i=\frac{q_i}{(\omega_d\prod_jq_j)^{1/d}},\qquad b'_i=\frac{q'_i}{(\omega_d\prod_jq'_j)^{1/d}}.
\tag{7}
\]
The two normalization scalars differ by \(O(\varepsilon^d)\). Hence \(|e_k(b)-e_k(b')|=O(\varepsilon^d)\) for \(k<d\) (and the last elementary symmetric functions agree exactly), but the distance between the sorted normalized root multisets is \(\Theta(\varepsilon)\). After reciprocation, their side ratios also differ by \(\Theta(\varepsilon)\). All these boxes converge to the cube. An exponent \(\gamma>1/d\) in (2) would force \(\Theta(\varepsilon)\le C\varepsilon^{d\gamma}=o(\varepsilon)\), impossible. This proves sharpness.

## Verification

The standalone standard-library Python program `verify.py` independently evaluates the local probability from ball-uniform numerical quadrature of the coordinate-difference density for several three-, four-, and five-dimensional boxes. It checks the exact coefficient product constraint and finite-dimensional inversion, and separately simulates two independent interior-uniform points in a three-dimensional box. Executing `python3 verify.py` returned `VERIFY_OK` after extraction from the self-contained package. These finite tests assess formula normalization and computation; the statements for all dimensions, positivity of reconstructed roots, minimality, and sharp stability follow from the analytical proof above.

In dimension three the polynomial specializes to
\[
D_Q(\rho)=\rho^3-\frac38 e_1(b)\rho^4+\frac{2}{5\pi}e_2(b)\rho^5-\frac{3}{32\pi^2}\rho^6,
\]
for all sufficiently small \(\rho\), providing an independently checkable closed form.

## Relationship to prior work

Wang [1] introduced the volume-normalized radial pair-distance profile and proved a general Brunn–Minkowski inequality and small-radius perimeter term; the inspected source does not state a sharp finite-jet inversion for orthotopes. An earlier all-polygon study [2] establishes an exact local quartic and angular stability in dimension two, so the elementary planar polynomial is not asserted to be new. A separate orthotope tomography result [3] uses moments of *uniformly directed hyperplane projection volumes*, not random interpoint Euclidean distances: its dimension-sharp moment count and optimal root-stability exponent have an analogous algebraic flavor but do not imply the present distance-profile identity. Classical random-line free-path distributions in boxes [4] are different from the independent volume-point-pair distribution; their ability to recover side lengths from density singularities does not supply this local finite-jet theorem. Elementary symmetric-polynomial inversion and standard polynomial-root perturbation are credited as general tools, not themselves claimed as inventions. The new assessed mathematical claim is the combined exact all-dimensional local random-pair law, **minimal** scale-free determination and **optimal** inverse exponent for this specific radial data.

## Limitations

No identification theorem is claimed for general convex bodies or nonorthogonal parallelotopes. The local polynomial ceases to be valid after the first coordinate-width threshold; a full large-radius distribution is not evaluated. The sharp Hölder exponent concerns exact population coefficients in a compact positive shape class, not noisy finite samples. Inverse constants are dimension- and shape-range-dependent. Existing multidimensional distance-distribution or stereological sources not discoverable by the targeted bibliographic and indexed-result searches could potentially contain equivalent special cases; absolute historical priority is not certified. Some classical random-box and free-path full texts were not available for exhaustive statement-by-statement comparison.

## References

1. Sinan Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916v1 (1 October 2026), https://arxiv.org/html/2610.01916v1.
2. *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b.
3. *Sharp finite-moment tomography of orthotopes in every dimension*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-finite-moment-tomography-of-orthotopes-in-every-dimension--cb0a2e3c75db.
4. Samuel Holmin, Pär Kurlberg and Daniel Månsson, *On the free path length distribution for linear motion in an \(n\)-dimensional box*, arXiv:1702.08096v1 (2017), https://arxiv.org/abs/1702.08096.
