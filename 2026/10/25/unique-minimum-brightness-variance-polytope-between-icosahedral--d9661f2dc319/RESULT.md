# Unique minimum-brightness-variance polytope between icosahedral normal orbits

## Finding

There is a unique optimal division of total facet area between the two natural icosahedral normal orbits that minimizes the orientation-to-orientation variation of planar projected area. Its two orbit-level brightness observables have strictly **negative covariance**, making the mixture substantially more isotropic than either Platonic endpoint. The minimum comes with an exact quadratic stability identity.

Take \(\varphi=(1+\sqrt5)/2\) and let \(V\) be the twelve points
\[
(0,\pm1,\pm\varphi),\quad (\pm1,\pm\varphi,0),\quad (\pm\varphi,0,\pm1).
\]
Let \(\mathcal A\) consist of these vectors normalized to length one. Let \(\mathcal B\) consist of the normalized sums of the three vertices in each of the twenty triangular faces of \(\operatorname{conv}V\). Thus \(|\mathcal A|=12\), \(|\mathcal B|=20\), and the two antipodally symmetric orbits are disjoint.

For \(0\le p\le1\), define the positive area measure on the unit sphere
\[
\mu_p=\frac p{12}\sum_{a\in\mathcal A}\delta_a+\frac{1-p}{20}\sum_{b\in\mathcal B}\delta_b.
\]
By Minkowski existence and uniqueness, it is the surface-area measure of a convex polytope \(K_p\), uniquely determined up to translation. In particular \(S(K_p)=1\), and the natural centered representative is centrally symmetric. For \(0<p<1\), the polytope has exactly 32 facets; at \(p=1\) it is a regular dodecahedron, and at \(p=0\) a regular icosahedron, both rescaled to surface area one.

Write \(b_p(u)=\operatorname{area}(K_p\mid u^\perp)\), with \(U\) uniform on \(S^2\), and set
\[
\mathcal C(p)=\frac{\operatorname{Var}(b_p(U))}{(\mathbb E b_p(U))^2},\qquad \mathbb E b_p(U)=\frac14.
\]
Define
\[
f(t)=\frac{2}{3\pi}\left(\sqrt{1-t^2}+t\arcsin t\right),\qquad 0\le t\le1.
\]
The following three constants are explicit:
\[
\begin{aligned}
x&=\frac{\frac13+5f(1/\sqrt5)}6-\frac14,\\
y&=\frac{f(\sqrt{(1-2/\sqrt5)/3})+f(\sqrt{(1+2/\sqrt5)/3})}2-\frac14,\\
z&=\frac{\frac13+6f(1/3)+3f(\sqrt5/3)}{10}-\frac14.
\end{aligned}
\]
Then, for **every** \(p\in[0,1]\),
\[
\boxed{\mathcal C(p)=4\bigl(p^2x+2p(1-p)y+(1-p)^2z\bigr).}
\]
Moreover \(x>0\), \(z>0\), and the mixed covariance satisfies \(y<0\). Therefore there is exactly one minimizer,
\[
\boxed{p_* = \frac{z-y}{x-2y+z}=0.363533772216726898\ldots,}
\]
and the **globally sharp, exact** stability identity is
\[
\boxed{\mathcal C(p)-\mathcal C(p_*)=4(x-2y+z)(p-p_*)^2.}
\]
Numerically \(\mathcal C(p_*)=0.000126635076577680885\ldots\), whereas the icosahedral and dodecahedral endpoints have squared coefficients of variation \(4z=0.000597460472670077\ldots\) and \(4x=0.001569817007138095\ldots\), respectively.

## Assumptions and scope

The claim is for compact full-dimensional convex bodies in Euclidean three-space whose surface-area measure has support exactly on these two orbits, with a constant positive weight on each orbit. Up to a common surface-area scaling and translation, all such bodies are represented uniquely by \(K_p\). The parameter endpoints permit one orbit to vanish. The viewing direction is Haar-uniform on the sphere. Relative variance is invariant under positive scaling of the bodies.

## Proof

**Geometric realization.** Each orbit is antipodally symmetric, so \(\int v\,d\mu_p(v)=0\). Both span all of \(\mathbb R^3\) and are not supported on a great circle. Minkowski's theorem supplies the claimed unique polytope for each \(p\), with precisely the positive-mass facet normals. The reflection \(v\mapsto-v\) fixes \(\mu_p\), so uniqueness up to translation permits a centrally symmetric centered representative. For \(p=0,1\), the full Platonic symmetry and uniqueness identify the two endpoint bodies.

**Brightness as a two-orbit observable.** Define \(Z_{\mathcal A}(u)=12^{-1}\sum_{a\in\mathcal A}|a\cdot u|\) and \(Z_{\mathcal B}(u)=20^{-1}\sum_{b\in\mathcal B}|b\cdot u|\). Cauchy's projection formula gives
\[
b_p(u)=\frac12\bigl(pZ_{\mathcal A}(u)+(1-p)Z_{\mathcal B}(u)\bigr).
\]
Since \(\mathbb E|v\cdot U|=1/2\), both orbit observables have mean \(1/2\), hence \(\mathbb E b_p=1/4\).

**Exact pair integral.** For unit vectors \(a,b\) with \(|a\cdot b|=t\), let \(G\) be a standard Gaussian three-vector and write \(G=RU\). Independence of \(R,U\), \(\mathbb E R^2=3\), and the standard two-dimensional Gaussian absolute-product integral give
\[
\mathbb E|a\cdot U|\,|b\cdot U|=\frac{2}{3\pi}\bigl(\sqrt{1-t^2}+t\arcsin t\bigr)=f(t).
\]
The Gaussian formula follows also by elementary integration in polar coordinates of the plane spanned by \(a,b\), so no numerical quadrature enters the argument.

**Complete orbit-pair enumeration.** All squared cosines and their **ordered pair multiplicities** are:

| Orbits | Squared cosine | Ordered multiplicity |
| --- | --- | ---: |
| \(\mathcal A\times\mathcal A\) | \(1\), \(1/5\) | 24, 120 |
| \(\mathcal B\times\mathcal B\) | \(1\), \(1/9\), \(5/9\) | 40, 240, 120 |
| \(\mathcal A\times\mathcal B\) | \((1-2/\sqrt5)/3\), \((1+2/\sqrt5)/3\) | 120, 120 |

To verify this without floating-point geometry, use \(\varphi^2=\varphi+1\), select the thirty vertex pairs at squared distance four, take the twenty triples with all three such edges, and square the normalized dot products. The 12-by-12, 20-by-20, and 12-by-20 tables have exactly the multiplicities displayed (the bundled checker reproduces them in \(\mathbb Q(\varphi)\)). Subtracting the common mean-product \(1/4\) yields exactly \(x=\operatorname{Var}(Z_{\mathcal A})\), \(y=\operatorname{Cov}(Z_{\mathcal A},Z_{\mathcal B})\), and \(z=\operatorname{Var}(Z_{\mathcal B})\), proving the quadratic formula.

**Strict interior optimum and stability.** The square-root and arcsine formulas, using the positive-term Taylor series for \(\arcsin\), yield certified rational intervals
\[
0.0003924<x<0.0003925,\quad -0.0001745<y<-0.0001743,\quad 0.0001493<z<0.0001495.
\]
For reproducibility the bundled checker bounds \(\pi\) by Machin's alternating arctangent formula and bounds every radical by integer-square-root rational brackets; it thereby certifies \(y<0<x,z\), without using finite sampling. As \(x-2y+z>0\), the quadratic is strictly convex. Its stationary point \((z-y)/(x-2y+z)\) lies strictly between zero and one because \(x>y\), \(z>y\). Completing the square proves the asserted **exact identity** and all equality cases. This finishes the proof.

## Verification

Run `python3 ICO_COV_CHECK.py` with Python 3 standard library only. The checker constructs the normal orbits from the twelve golden-ratio coordinates, enumerates each ordered pair squared cosine exactly in \(\mathbb Q(\varphi)\), bounds the kernels by rational arcsine series and square-root intervals, and certifies the strictly interior optimizer and signs of the mixed covariance. It does not depend on historical computation files or external services. Numerical decimals in this note are illustrations of the exact expressions.

## Relationship to prior work

Cauchy's formula and Minkowski's existence and uniqueness theorem are classical inputs, not new claims. The 2010 Coxeter-group treatment by Koca, Al Ajmi and Al-Shidhani gives a geometric construction context for the icosahedral face and vertex orbits. The 2026 paper by An studies high-order isotropy and **uniform** projection-area bounds for spherical-design Minkowski polytopes; its Theorems 2.2 and 6.1 do not compute the mixed covariance, the sharp two-orbit variance optimizer, or the exact quadratic stability coefficient here. Related exact random-shadow area moments for the five regular Platonic solids give endpoint values, but do not imply the strictly interior optimum without the mixed covariance calculation. The family is also naturally described as normalized **Blaschke interpolation** of the dual Platonic bodies (facet areas combine linearly, unlike Minkowski addition).

## Limitations

Uniqueness is **only** within the fixed two-orbit icosahedral facet-normal family at fixed total surface area; no optimum among arbitrary convex bodies or different normal supports is claimed. The result concerns uniformly oriented projected **area**, not silhouette complexity, projection perimeter, or volume. The center-symmetric representative is unique after translation and scale fixing; explicit vertex coordinates of the intermediate polytope are not needed for the stated brightness law. The originality comparison is relative to inspected literature and indexed records; it does not establish definitive historical priority. Independent mathematical review has not been performed.

## References

1. M. Koca, M. Al Ajmi, S. Al-Shidhani, *Quasi Regular Polyhedra and Their Duals with Coxeter Symmetries Represented by Quaternions II*, arXiv:1006.2973v1 (2010-06-15). https://arxiv.org/abs/1006.2973.
2. C. An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570v1 (2026-08-12), Sections 2, 3, 6. https://arxiv.org/abs/2608.11570.
3. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed. (2014), Section 8.2 (classical Minkowski theorem).
4. R. J. Gardner, *Geometric Tomography*, 2nd ed. (2006) (Cauchy's projection formula).
