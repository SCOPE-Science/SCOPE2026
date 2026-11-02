# Exact surface-area fluctuations of independently rotated three-dimensional Minkowski sums

## Finding

Let \(K\subset\mathbb R^3\) be any compact convex body with nonempty interior. Let \(R_1,R_2,\dots\) be independent Haar-uniform rotations in \(SO(3)\), put \(M_n=R_1K+\cdots+R_nK\), and write \(S_n=\operatorname{Area}(\partial M_n)\) for ordinary Euclidean surface area. No smoothness or symmetry is required of \(K\).

Let \(h:S^2\to\mathbb R\) be the support function of \(K\), \(c=(4\pi)^{-1}\int_{S^2}h\,d\omega\), and \(h=c+\sum_{\ell\ge1}h_\ell\) its orthogonal real spherical-harmonic decomposition, with \(h_\ell\) of degree \(\ell\) and \(L^2(S^2,d\omega)\) norm \(\|h_\ell\|_2\). Define
\[
\delta_\ell=\left(\frac{\ell(\ell+1)}2-1\right)\|h_\ell\|_2^2\quad (\ell\ge2),\qquad
D=\sum_{\ell\ge2}\delta_\ell=4\pi c^2-\operatorname{Area}(\partial K).
\]
These are finite nonnegative quantities. The first harmonic describes translations and is absent from them.

For each integer \(n\ge1\), **the exact expected surface area and variance** are
\[
\boxed{\mathbb ES_n=4\pi n^2c^2-nD},\qquad
\boxed{\operatorname{Var}(S_n)=2n(n-1)\sum_{\ell\ge2}\frac{\delta_\ell^2}{2\ell+1}}.
\]
Moreover, as \(n\to\infty\),
\[
\boxed{\frac{S_n-\mathbb ES_n}{n}\ \Longrightarrow\ W_K
=\sum_{\ell\ge2}\delta_\ell\left(1-\frac{X_\ell}{2\ell+1}\right)},
\]
where the \(X_\ell\) are mutually independent chi-square variables with \(2\ell+1\) degrees of freedom. This series is absolutely convergent almost surely and in \(L^1\), with variance \(2\sum_{\ell\ge2}\delta_\ell^2/(2\ell+1)\).

There is a **sharp, attainable variance inequality**
\[
\boxed{\operatorname{Var}(S_n)\le\frac{2n(n-1)}5D^2}.
\]
For \(n\ge2\) and \(D>0\), equality holds exactly when the support function has no nonzero spherical harmonics of degree \(\ell\ge3\), up to constant, first-harmonic, and degree-two components. Such nonball convex bodies exist. For every nonball, \(\operatorname{ess\,sup}W_K=D\), while \(W_K\) is unbounded below. In particular it is not Gaussian; its third cumulant is \(-8\sum_{\ell\ge2}\delta_\ell^3/(2\ell+1)^2<0\). For a ball \(D=0\) and all fluctuations vanish.

## Assumptions and scope

Minkowski addition is \(K+L=\{x+y:x\in K,y\in L\}\). The rotations are independent and distributed according to normalized Haar probability on \(SO(3)\). The surface area is the second-dimensional Hausdorff measure of the boundary (including nonsmooth bodies), not volume or averaged projected area. The sphere measure \(d\omega\) has total mass \(4\pi\). Real spherical harmonics are orthogonal in this unnormalized \(L^2\) convention; degree \(\ell\) has real dimension \(2\ell+1\). The body is allowed to be translated: this changes only the first harmonic and leaves every formula unchanged. The support function of a compact convex body is Lipschitz, so \(h\in H^1(S^2)\) and \(D<\infty\).

## Proof

**1. Quadratic support-area identity.** For a smooth strictly convex support function, the inverse Gauss map is \(x(u)=h(u)u+\nabla_{S^2}h(u)\). Its tangent Jacobian is \(\det(hI+\nabla_{S^2}^2h)\). In the two-dimensional tangent plane this determinant is \(h^2+h\Delta h+\det\nabla^2h\). Integration by parts and the Bochner identity on the unit sphere give
\[
\int_{S^2}h\Delta h\,d\omega=-\int_{S^2}|\nabla h|^2d\omega,
\qquad
\int_{S^2}\det\nabla^2h\,d\omega=\frac12\int_{S^2}|\nabla h|^2d\omega.
\]
Therefore
\[
\operatorname{Area}(\partial K)
=\int_{S^2}\left(h^2-\frac12|\nabla h|^2\right)d\omega.
\]
The identity continues to arbitrary convex bodies by convolution with a rotational approximate identity (which preserves support functions), addition of a small ball to ensure strict convexity, convergence in \(H^1\), and Hausdorff continuity of convex-body surface area. Since \(-\Delta h_\ell=\ell(\ell+1)h_\ell\), orthogonality yields \(4\pi c^2-S(K)=\sum_{\ell\ge2}\delta_\ell\). The \(\ell=1\) eigenvalue exactly cancels. This also establishes positivity and summability of the weights.

**2. Exact random quadratic decomposition.** Write \(U_{i\ell}(u)=h_\ell(R_i^{-1}u)\), and put \(t_\ell=\ell(\ell+1)/2-1\). Minkowski support functions add, so the previous identity gives, pathwise,
\[
S_n=4\pi n^2c^2-\sum_{\ell\ge2}t_\ell\left\|\sum_{i=1}^nU_{i\ell}\right\|_2^2.
\]
Every nonconstant harmonic has mean zero under Haar rotation, whence \(\mathbb E\|\sum_iU_{i\ell}\|_2^2=n\|h_\ell\|_2^2\). This proves the expectation, including the boundary case \(n=1\).

For \(n\ge2\), the centered quantity equals
\[
S_n-\mathbb ES_n=-2\sum_{1\le i<j\le n}\sum_{\ell\ge2}t_\ell\langle U_{i\ell},U_{j\ell}\rangle.
\]
Pair summands indexed by distinct unordered pairs are uncorrelated: for disjoint pairs use independence; for pairs sharing one index condition on that rotation, then each remaining independent Haar mean is zero. For one pair, the real irreducible \(SO(3)\) representations of different degrees are orthogonal, and Schur's matrix-coefficient orthogonality gives
\[
\mathbb E\left[\langle h_\ell,h_\ell\circ R^{-1}\rangle
\langle h_m,h_m\circ R^{-1}\rangle\right]
=\mathbf1_{\ell=m}\frac{\|h_\ell\|_2^4}{2\ell+1}.
\]
There are \(\binom n2\) unordered pairs, each carrying the factor \(-2\). This yields exactly \(4\binom n2\sum_\ell\delta_\ell^2/(2\ell+1)=2n(n-1)\sum_\ell\delta_\ell^2/(2\ell+1)\). Finiteness is justified by \(\sum\delta_\ell<\infty\).

**3. Non-Gaussian limit and infinite tail.** Fix finitely many degrees \(2\le\ell\le L\). For each rotation the joint vector of harmonic coefficients in their direct sum has mean zero and covariance block \(\|h_\ell\|_2^2I/(2\ell+1)\); distinct degrees are uncorrelated by irreducibility. The ordinary multivariate central limit theorem therefore gives independent Gaussian coefficient vectors in the limit. Their squared norms are independent \(\|h_\ell\|_2^2X_\ell/(2\ell+1)\). Hence the finite-mode version of \((S_n-\mathbb ES_n)/n\) converges to the corresponding finite sum in the displayed series.

For every \(n\), the expected nonnegative contribution of degree \(\ell\) to the surface-area deficit divided by \(n\) is \(\delta_\ell\). The absolute expectation of its centered contribution is consequently at most \(2\delta_\ell\). Thus the discarded tail beyond \(L\) is at most \(2\sum_{\ell>L}\delta_\ell\) in \(L^1\), uniformly in \(n\). This tends to zero. The limit's nonnegative chi-square-weighted part has expectation \(\sum\delta_\ell\), so the limiting series converges absolutely almost surely and in \(L^1\). This completes the full distributional convergence and, using the variance identity, its stated variance.

**4. Sharp bounds, support, and attainment.** Since \(2\ell+1\ge5\) and all \(\delta_\ell\ge0\),
\[
\sum_{\ell\ge2}\frac{\delta_\ell^2}{2\ell+1}
\le\frac15\sum_{\ell\ge2}\delta_\ell^2
\le\frac15\left(\sum_{\ell\ge2}\delta_\ell\right)^2.
\]
For positive total deficit equality forces every positive weight to be in degree two. It is attained, for example, by a nonzero sufficiently small \(\varepsilon\) in the strictly convex support function \(h(u)=1+\varepsilon P_2(u\cdot e_3)\), where \(P_2(t)=(3t^2-1)/2\). Taking \(0<\varepsilon<1/2\) makes the curvature matrix positive; the sole positive weight is \(\delta_2=8\pi\varepsilon^2/5\). Then \(W_K=\delta_2(1-\chi_5^2/5)\).

Every summand of \(W_K\) is at most \(\delta_\ell\). Conversely, for any \(\epsilon>0\), choose a finite cutoff leaving total tail weight below \(\epsilon\), use positive probability that every retained chi-square variable is small, and use Markov's inequality to make the nonnegative weighted tail small with positive probability. Hence \(\operatorname{ess\,sup}W_K=D\). Any positive weight gives an unbounded negative chi-square contribution while the others are bounded above, so the lower endpoint is unbounded. Chi-square cumulants give \(\kappa_3(W_K)=-8\sum\delta_\ell^3/(2\ell+1)^2\), strictly negative for a nonball. All claimed characterizations follow.

## Verification

The independent standalone script `verify.py` integrates the actual support-Gauss-map Jacobian \(\det(hI+\nabla^2h)\) by Gauss–Legendre and periodic angular quadrature. It compares this geometric integral with the spectral area formula for independently oriented degree-two perturbations and two-degree mixtures (degrees two and four) at several sample sizes. It then checks finite-sample means and variances for random orientations and the degree-two limit against the explicitly predicted \(\chi_5^2\) law. Execute `python verify.py` after installing NumPy and SciPy as described in `requirements.txt`; the final marker is `ALL_3D_ROTATED_MINKOWSKI_SURFACE_CHECKS_PASSED`. These finite checks validate normalization and formula consistency but are not the proof of the all-body theorem or its infinite series.

## Relationship to prior work

The deterministic boundary parameterizations for smooth Minkowski sums of Ruan and Chirikjian (arXiv:2012.15461, first public 2020-12-31) provide geometric background but do not analyze independent Haar-rotated repetitions or their random surface area. Schneider and Schuster (arXiv:1207.7286) develop rotation-invariant Minkowski classes and the use of spherical harmonics; their results concern density/universality of classes, not finite-sample area variance or chi-square fluctuations. Coupier and Davydov (arXiv:1211.1785) study *successive random reflections* and convergence rates, not independent complete \(SO(3)\) rotations and the second intrinsic-volume statistic. Leng, Liu, and Xi (DOI 10.4153/S0008414X22000505) study reconstruction from area measures and lightness functions, not rotational Minkowski-sum fluctuations.

Previously recorded planar results on randomly rotated Minkowski sums and iterated random planar symmetrization use \(SO(2)\) or reflections, where Fourier modes have dimension two. They cannot imply the spatial theorem: the irreducible representations now have dimensions \(2\ell+1\), yielding different chi-square degrees and the sharp factor \(2/5\). Existing exact planar covariance and inverse-stability results concern distinct functionals/sampling laws. Searches did not reveal an explicit pre-existing three-dimensional stochastic surface-area spectrum, but negative retrieval cannot establish historical uniqueness.

## Limitations

The random rotations must be independent and Haar-uniform. The theorem does not concern volume, non-Haar orientations, correlated copies, random scaling, or exact finite-sample distribution functions. The limiting chi-square law is derived for fixed \(K\) as \(n\to\infty\); no convergence rate is claimed. The two-mode numerical example cannot certify arbitrary nonsmooth convex bodies. A previously unindexed equivalent result remains a historical-priority risk; independent validation has not been carried out.

## References

1. S. Ruan and G. S. Chirikjian, *Closed-Form Minkowski Sums of Convex Bodies with Smooth Positively Curved Boundaries*, arXiv:2012.15461v1 (2020-12-31), https://arxiv.org/abs/2012.15461 .
2. R. Schneider and F. E. Schuster, *Rotation Invariant Minkowski Classes of Convex Bodies*, arXiv:1207.7286v1 (2012-07-31), https://arxiv.org/abs/1207.7286 .
3. D. Coupier and Yu. Davydov, *Random Symmetrizations of Convex Bodies*, arXiv:1211.1785v1 (2012-11-08), https://arxiv.org/abs/1211.1785 .
4. G. Leng, C. Liu, and D. Xi, *Reconstruction Problems of Convex Bodies from Surface Area Measures and Lightness Functions*, Canadian J. Math. 75 (2023), DOI 10.4153/S0008414X22000505 (online 2022-10-03), https://doi.org/10.4153/S0008414X22000505 .
