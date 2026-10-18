# Sharp affine least-squares stability separates the cube from its polar cross-polytope

## Finding
Let \(d\ge1\) be an integer. Write \(Q_d=[-1,1]^d\) and \(O_d=\{x\in\mathbb R^d:\sum_{j=1}^d|x_j|\le1\}\), equipped separately with normalized volume measure. On each body \(K\), let \(P_K\) be the \(L^2(K)\)-orthogonal projection onto all real affine functions and let \(\Lambda(K)=\|P_K\|_{L^\infty(K)\to L^\infty(K)}\). Set \((z)_+=\max\{z,0\}\).

The two exact constants are
\[
\boxed{\displaystyle
\Lambda(O_d)=1+\frac{d(d+3)}{2(d+1)}
\left(1-\frac{2}{(d+1)(d+2)}\right)^d,}
\]
and
\[
\boxed{\displaystyle
\Lambda(Q_d)=1+\frac{12}{(d+1)!}
\sum_{j=0}^d(-1)^j\binom dj
\left(\frac{3d-1}{6}-j\right)_+^{d+1}.}
\]
They coincide precisely in dimensions \(d=1,2\), when their values are respectively \(5/3\) and \(233/108\). In every dimension \(d\ge3\),
\[\boxed{\Lambda(O_d)>\Lambda(Q_d).}\]
Moreover,
\[
\Lambda(O_d)=\frac d2+O(1),\qquad
\Lambda(Q_d)=\sqrt{\frac{6d}{\pi}}+o(\sqrt d),\qquad
\lim_{d\to\infty}\frac{\Lambda(O_d)}{\sqrt d\,\Lambda(Q_d)}=\sqrt{\frac{\pi}{24}}.
\]
The same strict comparison and asymptotic ratio hold for the sharp negativity defects of nonnegative bounded data, after replacing each norm by \((\Lambda(K)-1)/2\) (their ratio has the same limit after normalization by \(\sqrt d\)).

## Assumptions and scope
The measure is *normalized Lebesgue volume* on each body, and both projectors use the full degree-at-most-one polynomial space \(\mathcal A_d=\operatorname{span}\{1,x_1,\ldots,x_d\}\). All functions are real-valued; taking complex-valued inputs does not change the operator norms because the integral kernels are real and their absolute values determine those norms. The dimension \(d\) ranges over **all positive integers**, not only finite test dimensions. The projected function is understood through its canonical continuous affine representative.

For any centrally symmetric body \(K\) with normalized volume law \(Y\), mean zero and invertible covariance matrix \(\Sigma\), the affine projector kernel is
\[
K_P(x,y)=1+x^{\mathsf T}\Sigma^{-1}y.
\]
Indeed the basis \(1,y_1,\ldots,y_d\) has block-diagonal Gram matrix \(\operatorname{diag}(1,\Sigma)\). Hence
\[
\Lambda(K)=\max_{x\in K}\mathbb E\bigl|1+x^{\mathsf T}\Sigma^{-1}Y\bigr|.
\]
The maximum exists by continuity, and convexity in \(x\) guarantees a maximizing extreme point on each polytope. Both \(O_d\) and \(Q_d\) have coordinate-symmetric scalar covariance.

## Proof
**Cross-polytope.** Under normalized volume on \(O_d\), the first coordinate has density
\[
f_d(t)=\frac d2(1-|t|)^{d-1}\mathbf1_{[-1,1]}(t),
\quad \mathbb E Y_1^2=\frac{2}{(d+1)(d+2)}.
\]
The other covariances vanish by sign symmetry. The vertices of \(O_d\) are \(\pm e_i\), and the convex maximum therefore occurs at one of them. Put \(a=(d+1)(d+2)/2\). By symmetry and the reproduction of constants,
\[
\begin{aligned}
\Lambda(O_d)
&=\mathbb E|1+aY_1|\\
&=1+d\int_{1/a}^1(ay-1)(1-y)^{d-1}\,dy\\
&=1+\frac{a-1}{d+1}\left(1-\frac1a\right)^d.
\end{aligned}
\]
Inserting \(a\) yields the first formula. This argument uses no asymptotic approximation.

**Cube.** Under normalized volume on \(Q_d\), the coordinates \(U_i\) are independent uniforms on \([-1,1]\), each of variance \(1/3\). Convexity in the evaluation point reduces the supremum to a cube vertex, and sign symmetry makes all vertices equivalent. Thus
\[
\Lambda(Q_d)=\mathbb E\left|1+3\sum_{i=1}^d U_i\right|.
\]
Write \(U_i=2V_i-1\), with \(V_i\) independent uniform variables on \([0,1]\), and \(B=\sum_iV_i\). Since the expression inside the absolute value has expectation one,
\[
\Lambda(Q_d)=1+12\mathbb E\left(\frac{3d-1}{6}-B\right)_+.
\]
For \(0\le t\le d\), the Irwin--Hall distribution has cumulative distribution
\[
\mathbb P(B\le t)=\frac1{d!}\sum_{j=0}^d(-1)^j\binom dj(t-j)_+^d.
\]
Integrating this cumulative distribution from zero to \((3d-1)/6\) gives the asserted **exact** finite sum.

**Strict dual comparison in every dimension.** The exact formulas yield
\(\Lambda(O_1)=\Lambda(Q_1)=5/3\) and \(\Lambda(O_2)=\Lambda(Q_2)=233/108\). For every \(d\ge1\), Bernoulli's inequality gives the explicit strict bound
\[
\begin{aligned}
\Lambda(O_d)
&\ge1+\frac{d(d+3)}{2(d+1)}
\left(1-\frac{2d}{(d+1)(d+2)}\right)\\
&=\frac d2+\frac{d^3+4d^2+7d+2}{(d+1)^2(d+2)}>\frac d2.
\end{aligned}
\]
On the other hand Cauchy--Schwarz, applied to the exact cube expectation, gives
\[
\Lambda(Q_d)\le\sqrt{\mathbb E\left(1+3\sum U_i\right)^2}
=\sqrt{1+3d}.
\]
For \(d\ge13\), \(d/2>\sqrt{1+3d}\), proving strict separation without a numerical approximation. The remaining ten dimensions \(3\le d\le12\) are an **exhaustive finite set**, and substitution into the exact rational expressions gives the strictly positive gaps checked by `check.py`. Their exact rational numerators and denominators are printed by the checker, not merely assessed from floating-point samples.

**Sharp growth and positivity loss.** The cross-polytope formula immediately yields \(\Lambda(O_d)/d\to1/2\). For the cube, \(d^{-1/2}\sum U_i\) converges in distribution to a centered Gaussian of variance \(1/3\). The squares of \((1+3\sum U_i)/\sqrt d\) have uniformly bounded expectations \(3+1/d\); therefore their absolute values are uniformly integrable. Taking absolute moments gives
\[
\frac{\Lambda(Q_d)}{\sqrt d}\longrightarrow
3\mathbb E|N(0,1/3)|=\sqrt{\frac6\pi}.
\]
This proves the ratio limit.

Lastly, for a fixed evaluation point \(x\), the kernel integrates to one, so the maximal negative value of \((P_K f)(x)\) among \(0\le f\le1\) is the kernel's negative mass,
\[
\int(-K_P(x,y))_+\,d\mu(y)=\frac12\left(\int|K_P(x,y)|\,d\mu(y)-1\right).
\]
Taking the maximum over \(x\) gives the sharp negativity defect \((\Lambda(K)-1)/2\). Strict separation and the same asymptotic normalized ratio follow.

## Verification
The included standalone `check.py` computes both formulas with Python exact rational numbers. It certifies equality in dimensions one and two, the ten positive exact gaps for dimensions three through twelve, the analytic lower-bound identity for tested integer dimensions, and the variance upper-bound inequality. It performs independent numerical quadratures of the one-coordinate Beta density and of the piecewise-polynomial Irwin--Hall density in dimensions one through seven. On the reviewed run, **365 assertions passed**. The all-dimensional part of the comparison relies on the displayed Bernoulli and Cauchy--Schwarz arguments, not on the checker. The asymptotic claim relies on the proved central-limit and uniform-integrability argument, not on numerical extrapolation.

Reproduce with `python check.py` from the extracted embedded files. SciPy is optional for the numerical quadrature cross-checks; the exact-rational certificate uses only Python's standard library.

## Relationship to prior work
Barthe, Guédon, Mendelson, and Naor (2005) establish a probabilistic realization of normalized volume on \(\ell_p\) balls and give sharp-to-constants results on moments of linear functionals. Their Theorem 1 and Section 2.2 provide the relevant probabilistic background, but those moment estimates **do not state the additive reproducing-kernel endpoint norm, exact finite-dimensional values, or the dual-pair equality/strictness classification**. The rough linear versus square-root contrast is consistent with, and in growth order can be inferred from, their moment estimates; that growth-order observation is **not claimed independently novel**.

Hangelbroek, Narcowich, Sun, and Ward (2010) study \(L^\infty\) stability of least-squares projectors associated with localized kernel approximation bases on manifolds. Their precise object and hypotheses differ from these volume-normalized affine polynomial projectors, and their operator bounds do not supply the constants here.

A published result on the local affine projector on a simplex obtains an exact positivity defect and endpoint norm by the related kernel-sign method. Its domain is a single simplex rather than either centrally symmetric dual body; an affine equivalence exists in the present two-dimensional cube--cross-polytope pair but not in dimensions at least three. The simplex constant does not imply the two exact formulas or the all-dimensional strict comparison.

## Limitations
The theorem concerns the exact degree-one *orthogonal* projector under normalized uniform volume, not interpolation at nodes, higher-degree polynomial approximation, arbitrary convex bodies, or projection constants minimized over all linear projectors. It does not claim a general ordering under polarity for all convex bodies. The finite sum for the cube can suffer cancellation when evaluated in floating point; the supplied verification uses rational arithmetic. Although targeted primary-text and published-finding comparisons found no equivalent dual-pair theorem, earlier unlocated treatments of polynomial Lebesgue constants could contain an equivalent formulation; a separate independent priority review remains necessary.

## References
1. F. Barthe, O. Guédon, S. Mendelson, A. Naor, *A Probabilistic Approach to the Geometry of the \(\ell_p^n\) Ball*, Annals of Probability 33 (2005), 480--513, arXiv:math/0503650 (first publicly timestamped 2005-03-29), https://arxiv.org/abs/math/0503650.
2. T. Hangelbroek, F. Narcowich, X. Sun, J. Ward, *Kernel Approximation on Manifolds II: The \(L^\infty\) Norm of the \(L^2\) Projector*, 2010 preprint, arXiv:1005.2424 (first publicly timestamped 2010-05-13), https://arxiv.org/abs/1005.2424.
3. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published mathematical finding, 2026-10-04, identifier `99c2b9dd9b34` (cited for scientific comparison, not for independent verification).
