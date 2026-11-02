# Growing-radius perimeter crossover for random polygons on hyperbolic circles

## Finding
Let \(n\) independent points lie on a hyperbolic circle of radius \(R_n>0\), sampled with uniform arclength. Let \(L_n\) be the perimeter of their geodesic convex hull. Write
\[
S_n=\sinh R_n,\qquad q_n=S_n/n,\qquad W_n=\frac{L_n}{2\pi S_n}.
\]
The exact finite-sample expectation is
\[
\mathbb E L_n=2n(n-1)\int_0^1\operatorname{arsinh}\bigl(S_n\sin(\pi x)\bigr)(1-x)^{n-2}\,dx. \tag{1}
\]
For every sequence of radii \(R_n>0\), if \(q_n\to s\) in the extended interval \([0,\infty]\), then
\[
W_n\longrightarrow F(s)\quad\text{in probability and in mean},
\]
where \(F(0)=1\), \(F(\infty)=0\), and, for \(0<s<\infty\),
\[
F(s)=\frac1{\pi s}\int_0^\infty e^{-y}\operatorname{arsinh}(\pi s y)\,dy. \tag{2}
\]
The crossover \(F\) is continuous and strictly decreasing from one to zero. Its sharp endpoint expansions are
\[
F(s)=1-\pi^2s^2+9\pi^4s^4+O(s^6)\quad(s\downarrow0), \tag{3}
\]
\[
F(s)=\frac{\log(2\pi s)-\gamma}{\pi s}+O(s^{-2})\quad(s\to\infty), \tag{4}
\]
where \(\gamma\) is Euler's constant. In particular, the nondegenerate perimeter-fraction regime is \(n\asymp\sinh R_n\), corresponding to \(R_n=\log n+O(1)\) when the radii diverge.

There is also a nondegenerate critical central limit theorem. If \(q_n\to s\in(0,\infty)\), then
\[
\sqrt n\bigl(W_n-F(q_n)\bigr)\Longrightarrow N\bigl(0,\sigma^2(s)\bigr), \tag{5}
\]
with strictly positive variance
\[
\sigma^2(s)=\frac{\operatorname{Var}\!\left(\operatorname{arsinh}(zZ)-b(z)(Z-1)\right)}{z^2},\quad
z=\pi s,\quad Z\sim\mathrm{Exp}(1),\quad b(z)=\mathbb E\frac{zZ}{\sqrt{1+z^2Z^2}}. \tag{6}
\]
The use of \(F(q_n)\), rather than \(F(s)\), in (5) is essential unless the radius sequence approaches its critical scale sufficiently quickly. Finally, at every fixed \(R>0\),
\[
\frac{\mathbb E L_n}{2\pi\sinh R}
=1-\frac{\pi^2\cosh^2 R}{(n+1)(n+2)}+O_R(n^{-4}). \tag{7}
\]

## Assumptions and scope
The ambient metric is the complete hyperbolic plane of Gaussian curvature exactly \(-1\). For each \(n\ge3\), its radius \(R_n\) is deterministic and positive; there is no distributional or regularity restriction across different \(n\). Points are independent and uniform by intrinsic arclength along the circle, not uniform in the disk's area. The hyperbolic geodesic hull is formed by the shortest geodesic segments in cyclic boundary order. Almost surely all sampled points are distinct and the hull has exactly \(n\) vertices. All limits are as \(n\to\infty\), and the notation \(O_R\) permits constants depending on a fixed radius. Formula (5) concerns the triangular array of independently resampled polygons; joint couplings across \(n\) are unnecessary.

## Proof
**Exact gap law and mean.** Let \(X_1,\dots,X_n\) be successive normalized central-angle gaps in cyclic order. They sum to one and have the uniform Dirichlet law \(\mathrm{Dirichlet}(1,\dots,1)\), so each \(X_i\) has density \((n-1)(1-x)^{n-2}\) on \((0,1)\). The hyperbolic cosine rule for two circle points at angular separation \(2\pi x\) gives
\[
\cosh d=1+2S_n^2\sin^2(\pi x),\qquad d=2\operatorname{arsinh}(S_n\sin(\pi x)). \tag{8}
\]
The sine here is nonnegative on \([0,1]\), including gaps exceeding a semicircle. The convex hull edges are exactly the cyclic chords (they are straight chords in the Klein model), hence
\[
W_n=\frac1{\pi S_n}\sum_{i=1}^n\operatorname{arsinh}\bigl(S_n\sin(\pi X_i)\bigr). \tag{9}
\]
Taking expectations proves (1).

**Sharp zero/infinite regimes.** The elementary inequalities \(\sin t\le t\), \(\operatorname{arsinh}t\le t\), and \(\operatorname{arsinh}t\ge t-t^3/6\), together with \(\sin t\ge t-t^3/6\) for \(0\le t\le\pi\), show
\[
0\le 1-W_n\le\frac{\pi^2(1+S_n^2)}6\sum_iX_i^3. \tag{10}
\]
The exact Dirichlet moment is \(\mathbb E\sum_iX_i^3=6/[(n+1)(n+2)]\). Thus \(W_n\to1\) in mean and probability whenever \(S_n/n\to0\). Conversely, concavity and monotonicity of \(\operatorname{arsinh}\) imply the deterministic Jensen bound
\[
0\le W_n\le\frac{\operatorname{arsinh}(\pi q_n)}{\pi q_n}, \tag{11}
\]
so \(W_n\to0\) when \(q_n\to\infty\). Each \(W_n\) lies in \([0,1]\) because chords do not exceed the associated circle arcs.

**Finite positive regime and fluctuations.** Couple all normalized gap vectors in law as \(X_i=Z_i/\sum_{j=1}^n Z_j\), for independent \(Z_j\sim\mathrm{Exp}(1)\). Put \(\bar Z_n=n^{-1}\sum_jZ_j\) and \(z_n=\pi q_n\). The map \(\operatorname{arsinh}\) is 1-Lipschitz and \(0\le t-\sin t\le t^3/6\), yielding
\[
\left|W_n-\frac1{z_n n}\sum_{i=1}^n\operatorname{arsinh}\left(\frac{z_nZ_i}{\bar Z_n}\right)\right|
\le\frac{\pi^2}6\sum_iX_i^3=O_{\mathsf P}(n^{-2}). \tag{12}
\]
For \(q_n\to s\in(0,\infty)\), the law of large numbers applied to (12) proves convergence to (2). For the CLT, Taylor-expand the summand around \(\bar Z_n=1\), with derivative \(-z_n Z_i/\sqrt{1+z_n^2Z_i^2}\). Because \(z_n\) stays inside a compact subinterval of \((0,\infty)\), the averaged quadratic remainder is \(O_{\mathsf P}(n^{-1})\), and the first-order expansion is
\[
\frac1{z_n n}\sum_i\operatorname{arsinh}\left(\frac{z_n Z_i}{\bar Z_n}\right)
=F(q_n)+\frac1{z_n n}\sum_i\left[\operatorname{arsinh}(z_nZ_i)-\mathbb E\operatorname{arsinh}(z_nZ)-b(z_n)(Z_i-1)\right]+o_{\mathsf P}(n^{-1/2}). \tag{13}
\]
The bracketed terms have mean zero, uniformly bounded moments above order two, and variances converging to the numerator of (6). The triangular-array Lindeberg theorem proves (5). Strict positivity follows since \(x\mapsto\operatorname{arsinh}(zx)\) is not affine on \((0,\infty)\) for any \(z>0\), whereas a zero variance would force this function to be affine almost everywhere under the positive exponential density.

**Crossover properties and fixed-radius coefficient.** In (2), \(F(s)=\mathbb E[Z\operatorname{arsinh}(\pi s Z)/(\pi sZ)]\). Since \(\operatorname{arsinh}(t)/t\) strictly decreases for \(t>0\), \(F\) is strictly decreasing; dominated convergence gives its endpoints. Expanding \(\operatorname{arsinh}t=t-t^3/6+3t^5/40+O(t^7)\) and using \(\mathbb E Z^m=m!\) produces (3) with a remainder justified by splitting the exponential integral at \(Z=s^{-1/2}\). For (4), write \(\operatorname{arsinh}(zy)=\log(2zy)+h(zy)\), where \(h\ge0\), \(h(t)=O(\min\{|\log t|,t^{-2}\})\); integrating against \(e^{-y}\) gives \(\mathbb E h(zZ)=O(z^{-1})\), while \(\mathbb E\log Z=-\gamma\). For fixed \(S=\sinh R\), the small-gap expansion in (9) is
\[
\operatorname{arsinh}(S\sin(\pi x))=\pi Sx-\frac{\pi^3S(1+S^2)}6x^3+O_R(x^5). \tag{14}
\]
Together with \(\mathbb E\sum_iX_i^5=120/[(n+1)(n+2)(n+3)(n+4)]\), this proves (7).

## Verification
The supplied standard-library program `verify.py` checks exact-coordinate hyperbolic cosine-law Monte Carlo calculations against the independent marginal-beta integral (1), checks the crossover limits and monotonicity at test scales, and numerically tests (3), (4), and (7). It also evaluates the variance functional (6) independently. Execute `python3 verify.py`; the expected final line is `ALL_CHECKS_PASSED`. The program is a finite corroboration, not a proof of limiting distributions, uniqueness of historical priority, or error terms beyond the derived estimates. The proof above supplies the universal quantifiers.

## Relationship to prior work
Besau, Rosen, and Thäle (first public preprint May 21, 2020; published 2021) establish central limit theorems for volume-related random inscribed polytopes in projective Riemannian and Finsler settings. Their theorems use a fixed smooth body and do not assert the changing-radius, relative-perimeter crossover and critical normalization (2)–(6) here. Fodor (first public preprint February 10, 2019; published 2021) studies optimal deterministic perimeter approximation of hyperbolic convex discs, not the distribution of boundary-iid random polygon perimeters. Related research on Euclidean randomly inscribed polygons and random hyperbolic line tessellations uses different sampling geometries. The argument here is explicit and direct; no independence from all possible earlier literature is asserted.

## Limitations
The results are restricted to curvature \(-1\), geodesic circles, uniform-arclength independent sampling, and intrinsic geodesic perimeter. They do not give area fluctuations, noncircular convex-body behavior, finite-sample normal approximation bounds, or almost-sure convergence under arbitrary cross-sample couplings. At critical scaling the CLT must be centered by \(F(q_n)\), not automatically by the fixed limit \(F(s)\). Historical priority remains provisional, particularly for older geometric-probability literature outside searchable full text. Independent mathematical validation has not been performed.

## References
1. F. Fodor, *Perimeter Approximation of Convex Discs in the Hyperbolic Plane and on the Sphere*, arXiv:1902.03655 (first public February 10, 2019); *Discrete & Computational Geometry* 66 (2021), 1190–1201, DOI:10.1007/s00454-021-00291-7.
2. F. Besau, D. Rosen, and C. Thäle, *Random inscribed polytopes in projective geometries*, arXiv:2005.10502 (first public May 21, 2020); *Mathematische Annalen* 381 (2021), 1345–1372, DOI:10.1007/s00208-021-02257-9.
3. E. Gallego and G. Solanes, *Perimeter, Diameter and Area of Convex Sets in the Hyperbolic Plane*, *Journal of the London Mathematical Society* 64 (2001), 161–178, DOI:10.1112/S002461070100223X.
4. Y. Yu. Nikitin and T. A. Polevaya, *Limit Theorems for Areas and Perimeters of Random Inscribed and Circumscribed Polygons*, *Journal of Mathematical Sciences* 258 (2021), 873–882, DOI:10.1007/s10958-021-05586-x (comparison limited to the accessible abstract).
