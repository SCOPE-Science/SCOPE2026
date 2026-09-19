# Almost BCD forces Banach–Mazur Euclidean cotangent fibers at the sharp square-root scale

## Statement

Let \((X,d,\mathfrak m)\) be a complete separable geodesic metric-measure space with locally finite Radon measure of full support. Assume that \(X\) satisfies \({\rm BCD}_\delta(K,\infty)\), is locally doubling, and supports a local weak \((1,1)\)-Poincaré inequality. For \(\mathfrak m\)-almost every \(x\), let \(T_x^*X\) be a finite-dimensional cotangent fiber and put \(k(x)=\dim T_x^*X\).

For every integer \(k\ge2\), there is \(\delta_k>0\) such that, whenever \(\delta<\delta_k\), every \(k\)-dimensional fiber in the preceding almost-everywhere conclusion satisfies
\[
 d_{\rm BM}(T_x^*X,\ell_2^k)
 \le 1+8\beta_k\sqrt\delta+O_k(\delta),
 \qquad
 \beta_k:=18k^2-17k+14.
\]
The same estimate holds for the dual tangent fiber because finite-dimensional Banach–Mazur distance is invariant under duality. Equivalently, after a linear change of coordinates the cotangent unit ball lies between a Euclidean ellipsoid and its \(1+8\beta_k\sqrt\delta+O_k(\delta)\) dilation.

If the essential cotangent dimension is bounded by \(N\), the estimate is uniform almost everywhere with \(\beta_N\) and an \(O_N(\delta)\) remainder, after decreasing the smallness threshold depending only on \(N\).

In dimension two there is a completely explicit version. For sufficiently small \(\delta\) with positive denominator,
\[
 d_{\rm BM}(T_x^*X,\ell_2^2)
 \le
 \sqrt{\frac{1+120\sqrt\delta+864\delta}
 {1-120\sqrt\delta-864\delta}}.
\]

The exponent \(1/2\) is optimal: the smooth non-Euclidean Minkowski perturbations constructed by Han and Liu satisfy
\[
 \Delta_{\rm BCD}(F_\tau)\asymp_\psi \tau^2,
 \qquad
 d_{\rm BM}((\mathbb R^n,F_\tau),\ell_2^n)-1\asymp_\psi |\tau|,
\]
for every nonquadratic perturbation profile \(\psi\) and all sufficiently small \(|\tau|\). Hence no general estimate of the form
\[
 d_{\rm BM}-1=O(\Delta_{\rm BCD}^{\alpha})
\]
can hold near the Euclidean class with any \(\alpha>1/2\).

## Proof of the upper estimate

Han and Liu define the normalized parallelogram defect of a finite-dimensional normed space \(E\) by
\[
 \mathfrak p_{\rm par}(E)
 :=\sup_{(p,q)\ne(0,0)}
 \frac{\left|\|p+q\|^2+\|p-q\|^2-2\|p\|^2-2\|q\|^2\right|}
 {\max\{\|p+q\|^2,\|p-q\|^2,2\|p\|^2,2\|q\|^2\}}.
\]
Their Theorem B proves under the hypotheses above that
\[
 \mathfrak p_{\rm par}(T_x^*X)\le 8\sqrt\delta
\]
for \(\mathfrak m\)-almost every \(x\).

Write
\[
 R(p,q)=\frac{\|p+q\|^2+\|p-q\|^2}{2\|p\|^2+2\|q\|^2}.
\]
The denominator in the definition of \(\mathfrak p_{\rm par}\) is at most \(2\|p\|^2+2\|q\|^2\), since \(\|p\pm q\|^2\le2\|p\|^2+2\|q\|^2\). Consequently
\[
 |R(p,q)-1|\le \mathfrak p_{\rm par}(E).
\]
Thus the von Neumann–Jordan constant obeys
\[
 C_{\rm NJ}(T_x^*X)\le1+8\sqrt\delta.
\]
(The reciprocal lower inequality follows by the standard change of variables \((p,q)\mapsto(p+q,p-q)\).)

Passer's quantitative Jordan–von Neumann theorem states that for every \(k\ge2\), if a real \(k\)-dimensional normed space \(E\) has \(C_{\rm NJ}(E)=1+\varepsilon\) with \(\varepsilon\) sufficiently small, then
\[
 d_{\rm BM}(E,\ell_2^k)
 \le K_k(\varepsilon),
 \qquad
 K_k(\varepsilon)=1+\beta_k\varepsilon+O_k(\varepsilon^2),
\]
where \(\beta_k=18k^2-17k+14\). Substitution of \(\varepsilon\le8\sqrt\delta\) gives the asserted estimate.

For \(k=2\), Passer's explicit theorem gives
\[
 d_{\rm BM}(E,\ell_2^2)
 \le
 \sqrt{\frac{1+15\varepsilon+13.5\varepsilon^2}
 {1-15\varepsilon-13.5\varepsilon^2}},
\]
and inserting \(\varepsilon=8\sqrt\delta\) yields the displayed formula.

## A Banach–Mazur lower lemma

The sharpness transfer uses the following elementary estimate, which is also useful independently.

**Lemma.** For every finite-dimensional real normed space \(E\),
\[
 \mathfrak p_{\rm par}(E)
 \le4\bigl(d_{\rm BM}(E,\ell_2^{\dim E})^2-1\bigr).
\]
Equivalently,
\[
 d_{\rm BM}(E,\ell_2^{\dim E})
 \ge\sqrt{1+\frac14\mathfrak p_{\rm par}(E)}.
\]

**Proof.** Put \(D=d_{\rm BM}(E,\ell_2^{\dim E})\). For every \(D'>D\), choose a Euclidean norm \(|\cdot|\) on the underlying vector space, after a harmless scalar normalization, such that
\[
 |z|\le\|z\|\le D'|z|.
\]
Set \(S=|p|^2+|q|^2\). The Euclidean parallelogram identity and the preceding norm comparison give
\[
\begin{aligned}
&\left|\|p+q\|^2+\|p-q\|^2-2\|p\|^2-2\|q\|^2\right|\\
&\qquad\le(D'^2-1)
\bigl(|p+q|^2+|p-q|^2+2|p|^2+2|q|^2\bigr)\\
&\qquad=4(D'^2-1)S.
\end{aligned}
\]
Meanwhile the denominator defining \(\mathfrak p_{\rm par}\) is at least
\[
 \max\{|p+q|^2,|p-q|^2\}\ge S,
\]
because the average of the first two quantities equals \(S\). Hence the quotient is at most \(4(D'^2-1)\). Take the supremum and then let \(D'\downarrow D\). \(\square\)

## Sharpness from smooth Minkowski perturbations

Han and Liu consider
\[
 F_\tau(v)^2=|v|^2\left(1+\tau\psi\left(\frac v{|v|}\right)\right),
\]
where \(\psi\) is smooth, even, and not the restriction of a quadratic form. Writing \(H(v)=|v|^2\psi(v/|v|)\), their perturbative estimate gives a positive quantity \(\mathcal Q(H)\) such that
\[
 \mathfrak p_{\rm par}(F_\tau^*)
 \ge\frac12\mathcal Q(H)|\tau|
\]
for sufficiently small \(|\tau|\). Their Theorem 4.11 simultaneously gives
\[
 \Delta_{\rm BCD}(F_\tau)\asymp_\psi\tau^2.
\]
Applying the lemma to \(F_\tau^*\), and using dual invariance of finite-dimensional Banach–Mazur distance, yields
\[
\begin{aligned}
 d_{\rm BM}(F_\tau,\ell_2^n)
 &=d_{\rm BM}(F_\tau^*,\ell_2^n)\\
 &\ge\sqrt{1+\frac18\mathcal Q(H)|\tau|}
 =1+\frac1{16}\mathcal Q(H)|\tau|+O_\psi(\tau^2).
\end{aligned}
\]
The general upper estimate, applied with errors decreasing to \(\Delta_{\rm BCD}(F_\tau)\), supplies the matching \(O_n(|\tau|)\) upper scale. Therefore the Banach–Mazur departure from Euclidean space is genuinely of order \(\sqrt{\Delta_{\rm BCD}}\) along these smooth Finsler examples.

## Consequence for Minkowski entropy defect

For a smooth strongly convex norm \(F\) on \(\mathbb R^n\), let
\[
 \Delta_{\rm BCD}(F)
 =\inf\{\delta\ge0:(\mathbb R^n,F,\mathcal L^n)\text{ satisfies }{\rm BCD}_\delta(0,\infty)\}.
\]
Then, as \(\Delta_{\rm BCD}(F)\downarrow0\),
\[
 d_{\rm BM}((\mathbb R^n,F),\ell_2^n)-1
 \le 8\beta_n\sqrt{\Delta_{\rm BCD}(F)}+O_n(\Delta_{\rm BCD}(F)).
\]
Thus small barycentric entropy defect quantitatively forces affine closeness of the norm ball to an ellipsoid. The perturbations above show that the square-root order is best possible.

## Relation to prior literature

Han and Liu prove the almost-BCD parallelogram estimate and the quadratic entropy scale of non-Riemannian Minkowski perturbations. Their paper does not state a Banach–Mazur estimate. Passer proves the finite-dimensional quantitative Jordan–von Neumann theorem, converting a small von Neumann–Jordan constant into a near-isometry with Euclidean space. Combining these two quantitative theories gives the cotangent-fiber upper bound; the lower lemma above transfers Han–Liu's perturbative parallelogram obstruction to Banach–Mazur distance and proves sharpness of the square-root entropy exponent.

Approximate parallelogram laws have a broader stability literature, including work of Chmieliński. That literature also emphasizes that dimension-free Hilbert-space conclusions are unavailable in unrestricted infinite dimension; the statement here is deliberately finite-dimensional and fiberwise.

## Limitations

The constants and the smallness threshold depend on the fiber dimension, and no claim of optimal constants is made. The conclusion is almost-everywhere and infinitesimal: it does not assert global Gromov–Hausdorff, measured Gromov–Hausdorff, or bi-Lipschitz closeness of \(X\) to a Riemannian space. No dimension-free infinite-dimensional analogue is asserted. Originality is to the best of our knowledge; the motivating preprint is recent, and differently phrased or not-yet-indexed parallel observations remain possible.

## References

1. B.-X. Han and D.-Y. Liu, *On the Geometry of Wasserstein Barycenter II: Riemannian Rigidity, Essential Non-Branching, and Finsler Models*, arXiv:2609.19564 (2026). https://arxiv.org/abs/2609.19564
2. B. Passer, *An Approximate Version of the Jordan von Neumann Theorem for Finite Dimensional Real Normed Spaces*, Linear and Multilinear Algebra 63 (2015), 68–77; arXiv:1305.3546. https://arxiv.org/abs/1305.3546
3. J. Chmieliński, *Normed spaces equivalent to inner product spaces and stability of functional equations*, Aequationes Mathematicae 87 (2014), 147–157. https://doi.org/10.1007/s00010-013-0193-y
