# Sharp random-distance kurtosis and an exact radial–covariance defect

## Finding
Let \(d\ge2\), and let \(K\subset\mathbb R^d\) be any compact convex body with nonempty interior. Take independent volume-uniform points \(X,Y\in K\), and write \(D=\|X-Y\|_2\). Then
\[
\boxed{\frac{\mathbb E D^4}{(\mathbb E D^2)^2}\ge\frac{(d+2)(d+3)}{d(d+4)}.}\tag{1}
\]
The constant is optimal, and equality holds **precisely for Euclidean balls**, up to translation and positive scaling.

More strongly, let \(g=\mathbb EX\) be the volume centroid, write \(\rho(u)>0\) for the radial distance from \(g\) to \(\partial K\) in the unit direction \(u\in S^{d-1}\), and put
\[
\nu(du)=\frac{\rho(u)^d\,d\sigma(u)}{\int_{S^{d-1}}\rho(v)^d\,d\sigma(v)},
\qquad T(u)=\rho(u)^2.
\]
Here \(\sigma\) is the ordinary spherical area measure; \(\nu\) is a probability measure. Set \(\Sigma=\operatorname{Cov}(X)\) and \(m_2=\mathbb E\|X-g\|_2^2=\operatorname{tr}\Sigma>0\). The **exact sharp defect identity** is
\[
\boxed{\begin{aligned}
\frac{\mathbb E D^4}{(\mathbb E D^2)^2}
-\frac{(d+2)(d+3)}{d(d+4)}
={}&\frac{(d+2)^2}{2d(d+4)}
\frac{\operatorname{Var}_\nu(T)}{(\mathbb E_\nu T)^2}\\
&+\frac{\bigl\|\Sigma-(m_2/d)I_d\bigr\|_{\mathrm F}^2}{m_2^2}.
\end{aligned}}\tag{2}
\]
Both terms are nonnegative. The radial-variance coefficient in (2) is best possible even if only that term is retained as a stability lower bound: any non-ball coordinate cube has scalar covariance, so its covariance defect vanishes and its radial defect is positive. In dimension two, the sharp lower constant is \(5/3\); a square has ratio \(17/10\) and radial squared coefficient of variation \(1/20\).

The proof requires only that the region be bounded, of positive volume, and star-shaped about its volume centroid, with almost-everywhere positive finite radial function. Convexity is a natural sufficient hypothesis. Star-shapedness cannot simply be deleted: a uniformly sampled planar annulus of outer radius one and squared inner radius \(q\in(0,1)\) has moment ratio
\[
1+\frac{2(1+q+q^2)}{3(1+q)^2}<\frac53,
\]
which decreases toward \(3/2\) as \(q\uparrow1\).

## Assumptions and scope
The dimension is an integer \(d\ge2\). The set \(K\) is compact, convex and has positive \(d\)-dimensional Lebesgue measure; the uniform distribution is normalized by that volume. Points are sampled independently with replacement. Euclidean distances and second/fourth *raw* distance moments are intended, not invariant-line chord sampling, boundary arclength sampling, affine-gauge distance, or central moments of the distance itself. The normalized ratio is invariant under Euclidean motions and homotheties, but **not** arbitrary affine maps.

Every full-dimensional convex body contains its centroid in its interior. Consequently \(\rho\) is strictly positive, finite and continuous, and the polar identities used below are legitimate. For the stated wider star-shaped variant the conclusions concern the set up to null sets; a non-ball set differing from a ball only on a measure-zero subset cannot be distinguished by uniform-volume moments.

## Proof
Translate the centroid to the origin, so \(\mathbb EX=0\). Write
\[
m_2=\mathbb E\|X\|_2^2,\qquad m_4=\mathbb E\|X\|_2^4,\qquad\Sigma=\mathbb E[XX^{\mathsf T}].
\]
Independence of \(X\) and \(Y\), together with the zero mean, gives the two exact moment identities
\[
\mathbb ED^2=2m_2,\qquad
\mathbb ED^4=2m_4+2m_2^2+4\operatorname{tr}(\Sigma^2).\tag{3}
\]
For clarity, expand \(D^2=\|X\|^2+\|Y\|^2-2X\cdot Y\). The cross terms containing a single factor of \(Y\) or \(X\) vanish upon expectation, and
\(\mathbb E(X\cdot Y)^2=\sum_{i,j}(\mathbb EX_iX_j)(\mathbb EY_iY_j)=\operatorname{tr}(\Sigma^2)\).

The radial polar-coordinate formula for uniform volume in the star-shaped domain is
\[
\mathbb E\|X\|^j
=\frac{d}{d+j}\,
\frac{\int_{S^{d-1}}\rho(u)^{d+j}\,d\sigma(u)}
{\int_{S^{d-1}}\rho(u)^d\,d\sigma(u)},\qquad j\in\{2,4\}.\tag{4}
\]
Indeed, use \(dx=r^{d-1}dr\,d\sigma\), integrate \(r\) from zero to \(\rho(u)\), and divide by \(\operatorname{Vol}_d(K)=\frac1d\int\rho^d\,d\sigma\). Thus, for the probability law \(\nu\) defined above,
\[
m_2=\frac d{d+2}\mathbb E_\nu T,\qquad
m_4=\frac d{d+4}\mathbb E_\nu T^2.\tag{5}
\]
Equation (3) divided by \((2m_2)^2\), followed by (5), yields
\[
\frac{\mathbb ED^4}{(\mathbb ED^2)^2}
=\frac12+\frac{(d+2)^2}{2d(d+4)}
\left(1+\frac{\operatorname{Var}_\nu(T)}{(\mathbb E_\nu T)^2}\right)
+\frac{\operatorname{tr}(\Sigma^2)}{m_2^2}.\tag{6}
\]
The matrix identity
\[
\operatorname{tr}(\Sigma^2)
=\frac{m_2^2}{d}+\bigl\|\Sigma-(m_2/d)I_d\bigr\|_{\mathrm F}^2\tag{7}
\]
is exact. Substituting it in (6) and simplifying
\[
\frac12+\frac{(d+2)^2}{2d(d+4)}+\frac1d
=\frac{(d+2)(d+3)}{d(d+4)}
\]
proves (2), then (1). No finite numerical enumeration is used for the all-dimensional conclusion.

For any centered Euclidean ball of radius \(R>0\), \(\rho\equiv R\) and \(\Sigma=R^2I_d/(d+2)\); both right-hand terms in (2) vanish. Conversely, equality makes the radial variance zero. Since \(\rho>0\), this forces \(\rho(u)\) constant for \(\nu\)-almost every direction, hence, by continuity of the radial function of a convex body, constant everywhere. Thus \(K\) is a ball. For the wider star-shaped class this is equality up to volume-null differences. Cubes centered at the origin have isotropic covariance but nonconstant \(\rho\), verifying sharpness of the radial stability coefficient.

For the annulus assertion, rotational symmetry gives \(\Sigma=(m_2/2)I_2\). Its squared radial coordinate is uniform on \([q,1]\), so \(m_2=(1+q)/2\), \(m_4=(1+q+q^2)/3\). Equation (3) yields \(\mathbb ED^4/(\mathbb ED^2)^2=1+m_4/(2m_2^2)\), equal to the displayed expression, which lies strictly below \(5/3\) whenever \(0<q<1\). This example lies outside the star-shaped assumption.

## Verification
The included standalone `verify.py` uses only Python 3 standard-library modules. It checks (3)--(7) in exact rational arithmetic for Euclidean balls in dimensions two through forty and for axis-aligned boxes (including anisotropic boxes) in dimensions two through twelve. Crucially, its box fourth moments are also computed independently by summing one-coordinate difference moments. A separate polar-angle quadrature for a planar non-square rectangle agrees with direct coordinate moments; exact annulus formulas check failure beyond star-shaped sets; an independent seeded direct two-point experiment provides a probabilistic sanity check.

Run `python3 verify.py`. The expected final line is `ALL_CHECKS_PASSED`. The infinite-dimensional-range theorem relies on equations (3)--(7), not on these finitely many checks.

## Relationship to prior work
The paper of Bonnet, Gusakova, Thäle and Zaporozhets [1] derives sharp estimates for the *first* mean Euclidean distance normalized by mean width (first intrinsic volume). It does not compare the fourth-to-second moment ratio or give the exact two-term radial/covariance defect (2). Bäsel [2], particularly Sections 8--10 and formula (19), obtains exact second and fourth point-distance moments of regular polygons and records the planar general fourth-moment expansion associated with Voss [3]. The present sharp **all-convex-body, all-dimensional** ratio inequality, ball rigidity, and identity (2) are not statements in those inspected sections. The general expansion formula itself is not claimed as new.

A published result on fourth-chord moments of parallelograms [4] compares *boundary-to-interior* fourth moments, whereas (1) compares the fourth and second moments of a **single interior-to-interior distance distribution**. The published beta stochastic comparison for difference-body gauge distances [5] concerns an affine-gauge random variable and simplex equality, not Euclidean distances normalized by their own second moments. Neither stated theorem entails (1) by parameter matching. The older Voss paper [3] is highly related because it treats general chord-power integrals; only its abstract and the exact identity quoted in [2] were accessible, so an equivalent older inequality remains a priority risk.

## Limitations
The sharp estimate is for exact population moments under a uniform-volume sampling law. It does not address finite-sample estimation or recover arbitrary convex shapes from two moments. It cannot be extended verbatim to non-star-shaped regions, as the annulus calculation shows. The quantitative defect controls variation of the radial function in the **radius-weighted angular measure** and covariance anisotropy; no explicit Hausdorff-distance or Banach--Mazur-distance modulus follows here. The historical priority assessment is provisional, especially for older chord-power literature; no independent mathematical validation has been performed.

## References
[1] G. Bonnet, A. Gusakova, C. Thäle and D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, arXiv:2010.03351v1, 2020-10-07, https://arxiv.org/abs/2010.03351.

[2] U. Bäsel, *The moments of the distance between two random points in a regular polygon*, arXiv:2101.03815v1, 2021-01-11, https://arxiv.org/abs/2101.03815, especially Sections 8--10 and equation (19).

[3] K. Voss, *Powers of chords for convex sets*, Biometrical Journal 24 (1982), 513--516, DOI:10.1002/bimj.4710240524 (historical source of general planar chord-moment identities; full text not inspected).

[4] *Fourth-chord moment amplification and angular phase transition for parallelograms*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e.

[5] *A sharp beta stochastic bound for difference-body distances*, published mathematical research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-sharp-beta-stochastic-bound-for-difference-body-distances--4609b4d88176.
