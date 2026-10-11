# Sharp uniform angular stability for the short-pair distance coefficient of convex polygons

## Finding

Let \(P\subset\mathbb R^2\) be a nondegenerate convex polygon with \(N\ge3\) genuine vertices, area \(A\), perimeter \(L\), and interior angles \(\alpha_1,\ldots,\alpha_N\in(0,\pi)\). For independent points \(X,Y\) uniformly distributed in \(P\), put
\[
R=\sqrt{A/\pi},\qquad D_P(\rho)=\mathbb P\{|X-Y|<\rho R\}.
\]
There is a \(\rho_0(P)>0\) such that the following identity is **exact**, not merely asymptotic, whenever \(0\le\rho<\rho_0(P)\):
\[
D_P(\rho)=\rho^2-\frac{2L}{3\pi^{3/2}\sqrt A}\rho^3+C_4(P)\rho^4,
\qquad C_4(P)=\frac1{8\pi^2}\sum_{i=1}^N\left[1+(\pi-\alpha_i)\cot\alpha_i\right].
\tag{1}
\]
Write \(\overline\alpha=(N-2)\pi/N\). The fourth-order coefficient has the **sharp uniform quantitative angle-rigidity bound**
\[
\boxed{\displaystyle C_4(P)\ge\frac{N}{8\pi^2}\left[1-\frac{2\pi}{N}\cot\!\left(\frac{2\pi}{N}\right)\right]+\frac{1}{24\pi^2}\sum_{i=1}^N(\alpha_i-\overline\alpha)^2.}
\tag{2}
\]
Equality in (2) occurs precisely for **equiangular polygons** (including nonregular equiangular polygons). The coefficient \(1/(24\pi^2)\) is the largest universal coefficient valid for all integers \(N\ge3\); it is approached by a centrally symmetric family with \(N\to\infty\). This is a sharp statement about the fourth-order local probability coefficient, **not** a pointwise comparison of the full distance distributions for arbitrary radii.

## Assumptions and scope

All polygons are compact, two-dimensional, and convex, with no consecutive collinear sides; vertices and angles are cyclically indexed. The normalization \(R=\sqrt{A/\pi}\) is the radius of the equal-area disk. The probability uses two independent area-uniform points. Angles are in radians. Coefficients in (1) are dimensionless and unchanged by translation, rotation, or positive dilation. The small-radius threshold may depend on the polygon; no uniform threshold over all polygons is claimed.

## Proof

**1. A local quadratic covariogram.** Enumerate sides counterclockwise as \(E_i\), with length \(\ell_i\), outward unit normal \(n_i\), and support offset \(h_i\). Write \(P=\bigcap_i\{x:n_i\cdot x\le h_i\}\); the interior angle \(\alpha_i\) is between \(E_{i-1}\) and \(E_i\). If each support line moves inward by a sufficiently small amount \(s_i\), the new polygon retains the same cyclic normals and its area is exactly
\[
A(s)=A-\sum_i\ell_i s_i+\sum_i\left[\frac{\cot\alpha_i}{2}\left(s_{i-1}^2+s_i^2\right)+\frac{s_{i-1}s_i}{\sin\alpha_i}\right].
\tag{3}
\]
Indeed, each side length is affine in the adjacent offsets as long as the normal fan persists. The area satisfies \(A(h)=\tfrac12\sum_i h_i\ell_i(h)\), equivalently \(\partial A/\partial h_i=\ell_i\). Differentiating the side-length formula gives the diagonal Hessian terms \(\cot\alpha_i+\cot\alpha_{i+1}\) and the neighboring mixed terms \(1/\sin\alpha_i\), with all other mixed terms zero. Thus Taylor's quadratic formula is exact, giving (3). All original side lengths are strictly positive, so by compactness there is one positive radius of support perturbations for which the fan persists, uniformly over every direction used below.

For \(u\in\mathbb S^1\), \(t\ge0\), define \(d_i(u)=\max\{0,-n_i\cdot u\}\). Intersecting \(P\) with \(P+tu\) moves its \(i\)-th support line inward by \(t d_i(u)\), hence, uniformly in \(u\) for sufficiently small \(t\),
\[
g_P(tu):=|P\cap(P+tu)|=A-t\sum_i\ell_i d_i(u)+t^2Q(u),
\]
\[
Q(u)=\sum_i\left[\frac{\cot\alpha_i}{2}\bigl(d_{i-1}(u)^2+d_i(u)^2\bigr)+\frac{d_{i-1}(u)d_i(u)}{\sin\alpha_i}\right].
\tag{4}
\]
The formula makes no smooth-boundary approximation; it is an identity for the polygonal intersections.

**2. Exact angular integration.** Writing \(d\theta\) for ordinary arclength on the unit circle,
\[
\int_{\mathbb S^1}d_i\,d\theta=2,\qquad
\int_{\mathbb S^1}d_i^2\,d\theta=\frac\pi2,
\]
\[
\int_{\mathbb S^1}d_{i-1}d_i\,d\theta=\frac12\bigl(\sin\alpha_i-\alpha_i\cos\alpha_i\bigr).
\tag{5}
\]
The last equality follows by integrating the product of two positive cosine parts over the overlap of their semicircles. The normals make angle \(\pi-\alpha_i\), so the overlap has angular width \(\alpha_i\). Equations (4)–(5) yield
\[
\int_{\mathbb S^1}Q(u)\,d\theta=\frac12\sum_i[1+(\pi-\alpha_i)\cot\alpha_i].
\]
The random-pair probability equals \(A^{-2}\int_{|z|<\rho R}g_P(z)\,dz\). In polar coordinates, the constant, linear, and quadratic terms of (4) integrate respectively to
\[
\pi A r^2,\qquad-\frac{2L}3r^3,\qquad\frac{r^4}{8}\sum_i[1+(\pi-\alpha_i)\cot\alpha_i].
\]
Substituting \(r=\rho\sqrt{A/\pi}\) proves (1), including exact termination at the fourth power near zero.

**3. Global rigidity inequality.** Put
\[
f(a)=1+(\pi-a)\cot a,\quad 0<a<\pi,\qquad\beta=\pi-a.
\]
Then \(f(a)=1-\beta\cot\beta\) and
\[
\frac12 f''(a)=\frac{\sin\beta-\beta\cos\beta}{\sin^3\beta}=:H(\beta).
\tag{6}
\]
The numerator is positive for \(0<\beta<\pi\): its derivative is \(\beta\sin\beta>0\) and its limit at zero is zero. A direct derivative gives
\[
H'(\beta)=\frac{\beta(1+2\cos^2\beta)-3\sin\beta\cos\beta}{\sin^4\beta}.
\]
The numerator here vanishes at zero and its derivative is \(4\sin\beta(\sin\beta-\beta\cos\beta)>0\). Therefore \(H\) increases strictly, and \(\lim_{\beta\downarrow0}H(\beta)=1/3\). In particular, \(f''(a)>2/3\) for every interior angle \(a\). Thus \(f(a)-a^2/3\) is strictly convex. Since \(\sum_i\alpha_i=(N-2)\pi=N\overline\alpha\), Jensen's inequality gives
\[
\sum_i f(\alpha_i)\ge N f(\overline\alpha)+\frac13\sum_i(\alpha_i-\overline\alpha)^2.
\tag{7}
\]
Here \(f(\overline\alpha)=1-(2\pi/N)\cot(2\pi/N)\), yielding (2). Strict convexity proves equality exactly when all angles agree. Such polygons exist for every \(N\) (regular polygons suffice), hence the base term and equality statement are sharp.

**4. Optimality of the universal stability coefficient.** Let \(N=2m\ge6\) grow. Set \(b=2\pi/N\), \(\varepsilon=1/(5N)\), and prescribe cyclic exterior turning angles
\[
\beta_1=\beta_{m+1}=b+\varepsilon,\qquad
\beta_2=\beta_{m+2}=b-\varepsilon,
\]
with all other exterior angles equal to \(b\). The turning sequence is repeated after \(m\) steps; each half has total turning \(\pi\). Consecutive unit-length edge vectors can therefore be chosen in these directions: the second half of the edge sequence is exactly the negative of the first. The resulting closed edge path is a strictly convex, centrally symmetric equilateral polygon; its interior angles are \(\alpha_i=\pi-\beta_i\).

Only four deviations from \(\overline\alpha=\pi-b\) occur, with values \(\pm\varepsilon\) twice each. Therefore the ratio of the excess coefficient over the squared angle deviation is
\[
\frac{C_4(P_N)-N f(\overline\alpha)/(8\pi^2)}{\sum_i(\alpha_i-\overline\alpha)^2}
=\frac{f''(\pi-b)}{16\pi^2}+O(\varepsilon^2)
\longrightarrow\frac{1}{24\pi^2},
\]
by (6) as \(b,\varepsilon\to0\). Any larger uniform quadratic coefficient fails for this family, proving global sharpness. No optimality at fixed \(N\) is claimed for the variance coefficient.

## Verification

The accompanying standard-library Python program `verify.py` checks the exact directional intersection-area quadratic formula against direct convex-polygon clipping, numerically integrates the direction-dependent quadratic coefficient, tests the angle stability inequality on regular and nonregular polygons, and exhibits convergence of the even-sided sharpness ratio. Running `python3 verify.py` returns `VERIFY_OK`. These finite computations corroborate normalization, signs, indexing, and several boundary cases; the all-polygon and all-\(N\) results rely on the preceding analytic argument, not on numerical enumeration.

For a unit square, (1) gives the familiar exact small-distance law \(D_P(\rho)=\rho^2-8\rho^3/(3\pi^{3/2})+\rho^4/(2\pi^2)\), providing an independent normalization check.

## Relationship to prior work

Wang's 2026 study [1] introduced the normalized short-pair distribution for convex bodies and established its first small-range correction in terms of perimeter. Formula (1) resolves the next order for polygons, while (2) supplies a sharp, uniform angle-variance refinement and an exact equality classification; those are not statements of [1]. Earlier polygon-distance frameworks [2–4] compute complete distance distributions by integration or triangulation. Their computational generality can in principle recover individual polygon coefficients and is not claimed as new here. The distinguishing result is the explicit angular-only fourth coefficient together with its global minimization, quantitative rigidity, and optimal universal constant; those statements are not supplied by the inspected algorithms. Published quantitative stability results for reduced polygons [5] and tangential quadrilaterals [6] concern different area and semiperimeter deficits and do not imply the pair-distance coefficient bound (2).

## Limitations

The proof applies to full-dimensional convex Euclidean polygons with finitely many positive-length edges and strictly interior angles; not to nonconvex polygons, smooth bodies, or higher dimensions. The polynomial identity holds for sufficiently small radius depending on the polygon, not for every distance. The angular variance coefficient is sharp uniformly across all side counts, but no fixed-side-count optimality for that coefficient is asserted. Algorithms for arbitrary polygonal distance distributions predate this theorem, and an equivalent historical statement under different terminology remains possible. A relevant older general polygon-distance paper [4] was accessible only through its abstract, so exact overlap with that source remains a literature risk.

## References

1. Sinan Wang, *A Brunn–Minkowski Theory for the Distribution of Random Pairs of Points in Convex Bodies*, arXiv:2610.01916v1 (public 1 October 2026), https://arxiv.org/html/2610.01916v1.
2. Ross Pure, Salman Durrani, Fei Tong, Jianping Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757v1 (2019), https://arxiv.org/pdf/1903.07757.
3. Fei Tong and Jianping Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407v1 (2016), https://arxiv.org/pdf/1602.03407.
4. K. B. Baltzis, *Distance Distribution in Convex n-Gons: Mathematical Framework and Wireless Networking Applications*, Wireless Personal Communications 71 (2013), 1487–1503, https://doi.org/10.1007/s11277-012-0887-9.
5. *Quantitative area stability for reduced polygons*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-quantitative-area-stability-reduced-polygons--c9d16da8d26f/RESULT.md.
6. *Sharp angle-variance stability for Ivanova's tangential-quadrilateral inequality*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-sharp-angle-variance-stability-tangential-quadrilaterals--cce8a9a33e16/RESULT.md.
