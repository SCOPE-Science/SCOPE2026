# Second-order volume fluctuations of isotropic three-dimensional random zonotopes

## Finding

Let \(u_1,u_2,\ldots\) be independent uniform random unit vectors on \(S^2\subset\mathbb R^3\). For each integer \(n\ge3\), form the Euclidean zonotope \(Z_n=[0,u_1]+\cdots+[0,u_n]\), using Minkowski addition, and let \(V_n=\operatorname{Vol}_3(Z_n)\). Its exact expectation and variance are
\[
\mathbb E V_n=\binom n3\frac\pi8,
\qquad
\operatorname{Var}(V_n)
=\binom n3\left(\frac29-\frac{\pi^2}{64}\right)
+2\binom n2\binom{n-2}2
\left(\frac16-\frac{\pi^2}{64}\right).
\]
The second-order normalization is sharp, and the fluctuations have a **non-Gaussian, bounded-above limit**:
\[
\frac{V_n-\mathbb EV_n}{n^2}\ \xrightarrow{d}\ W
=\frac{\pi}{16}-\frac12\sum_{m=1}^{\infty}a_mX_m,
\quad
 a_m=\frac\pi4\frac{\binom{2m}m^2}{16^m(2m-1)(2m+2)},
\]
where the \(X_m\) are independent chi-square random variables with \(4m+1\) degrees of freedom. The series converges almost surely and in \(L^1\), and the centered version converges in \(L^2\). In particular,
\[
\mathbb EW=0,\qquad
\operatorname{Var}(W)=\frac1{12}-\frac{\pi^2}{128}>0,\qquad
\operatorname{ess\,sup}W=\frac\pi{16},
\]
and the distribution has no finite lower bound. This sharp one-sided support distinguishes the limit from a Gaussian law. No assertion is made about independent mathematical auditing.

## Assumptions and scope

The vectors are independent and identically distributed under normalized surface area on the *unit* two-sphere. Their Euclidean lengths are fixed at one; the segments are \([0,u_i]\) without an extra factor of \(1/n\). The ambient space is \(\mathbb R^3\); volume is ordinary three-dimensional Lebesgue measure. The zonotope is a parallelotope when \(n=3\), and almost surely full-dimensional for each \(n\ge3\). The limit holds as integer \(n\to\infty\) with dimension fixed. All expectations are with respect to the independent vectors.

## Proof

**1. Exact determinant representation.** The standard zonotope volume identity (obtainable from multilinearity of mixed volume or subdivision into parallelotopes) gives
\[
V_n=\sum_{1\le i<j<k\le n}h(u_i,u_j,u_k),\qquad
h(u,v,w)=|\det(u,v,w)|.
\]
For independent uniform \(u,v,w\), condition on \(u,v\): the unit normal component of \(w\) is uniform on \([-1,1]\). Thus
\[
\mathbb E_w h(u,v,w)=\tfrac12\|u\times v\|
=\tfrac12\sqrt{1-(u\cdot v)^2}.
\]
Since \(u\cdot v\) is also uniform on \([-1,1]\),
\[
\mu=\mathbb Eh=\tfrac14\int_{-1}^1\sqrt{1-t^2}\,dt=\pi/8,
\qquad \mathbb Eh^2=\tfrac23\cdot\tfrac13=\tfrac29.
\]
**2. Overlap partition and exact variance.** Two summands with disjoint triples are independent. Those with exactly one common index have zero covariance: their conditional means given that vector both equal \(\mu\) by rotational invariance. For two triples with exactly two common indices,
\[
\operatorname{Cov}(h(u,v,w),h(u,v,w'))
=\mathbb E\left[\tfrac14\|u\times v\|^2\right]-\mu^2
=\tfrac16-\frac{\pi^2}{64}=:c>0.
\]
There are \(\binom n3\) diagonal terms and \(\binom n2\binom{n-2}2\) *unordered* pairs of distinct triples sharing exactly two indices. Twice the latter count yields the stated variance. Since \(c>0\),
\[
\lim_{n\to\infty}\frac{\operatorname{Var}(V_n)}{n^4}
=\frac c2=\frac1{12}-\frac{\pi^2}{128}>0.
\]
**3. The canonical second-order term.** Define the centered symmetric kernel
\[
g(u,v)=\tfrac12\sqrt{1-(u\cdot v)^2}-\mu.
\]
Its conditional mean given either vector is zero. The first-order Hoeffding projection of \(h\) vanishes, while its second-order projection equals \(g\). Consequently the exact Hoeffding decomposition is
\[
V_n-\mathbb EV_n=(n-2)\sum_{i<j}g(u_i,u_j)
+\sum_{i<j<k}h_3(u_i,u_j,u_k),
\]
where \(h_3=h-\mu-g(u,v)-g(u,w)-g(v,w)\) is fully degenerate. Because \(h_3\) is bounded, distinct canonical triple summands are orthogonal in \(L^2\), giving
\[
\mathbb E\left|n^{-2}\sum_{i<j<k}h_3(u_i,u_j,u_k)\right|^2=O(n^{-1}).
\]
**4. Explicit sphere-harmonic spectrum.** Use surface probability measure \(\sigma\) on \(S^2\). The integral operator \(Tf(u)=\int g(u,v)f(v)\,d\sigma(v)\) is rotation-equivariant. By Funk–Hecke, each real orthonormal spherical harmonic of degree \(\ell\) is an eigenfunction with eigenvalue
\[
\lambda_\ell=\tfrac12\int_{-1}^1
\left(\tfrac12\sqrt{1-t^2}-\mu\right)P_\ell(t)\,dt.
\]
The constant eigenvalue is zero, as are the odd-degree eigenvalues. For \(m\ge1\), direct evaluation gives
\[
\lambda_{2m}=\tfrac14\int_{-1}^{1}\sqrt{1-t^2}P_{2m}(t)\,dt
=-\frac\pi4\frac{\binom{2m}m^2}{16^m(2m-1)(2m+2)}=-a_m.
\]
To check the nontrivial integral, use
\(P_{2m}(t)=(-1)^m(1/2)_m/m!\,{}_2F_1(-m,m+1/2;1/2;t^2)\).
Integrate its terminating polynomial against \(\sqrt{1-t^2}\), using
\(\int_{-1}^1 t^{2r}\sqrt{1-t^2}\,dt=B(r+1/2,3/2)\); cancellation gives the terminating \({}_2F_1(-m,m+1/2;2;1)=(3/2-m)_m/(2)_m\). Factorial simplification yields the expression above. This also proves every nonconstant eigenvalue is strictly negative.

The asymptotic \(a_m=O(m^{-3})\) gives absolute uniform convergence of the zonal Legendre series, because each degree \(2m\) has multiplicity \(4m+1\). Its value at coincident arguments (where \(g(u,u)=-\mu\)) implies
\[
\sum_{m\ge1}(4m+1)a_m=\mu=\frac\pi8.
\]
Parseval gives
\[
\sum_{m\ge1}(4m+1)a_m^2=\int g(u,v)^2\,d\sigma(u)d\sigma(v)
=\frac16-\frac{\pi^2}{64}=c.
\]
**5. Distributional limit and support.** Expand \(g\) in a real orthonormal spherical-harmonic basis. For any fixed spectral cutoff, the multivariate central limit theorem for the empirical harmonic coefficients and the strong law for their squared norms give
\[
\frac1n\sum_{i<j}g(u_i,u_j)
\xrightarrow{d}
-\frac12\sum_{m\ge1}a_m(X_m-(4m+1)).
\]
This passage from finite to infinite spectrum is justified in \(L^2\), uniformly in \(n\), because the variance of the omitted canonical pair kernel is bounded by a constant times its squared Hilbert–Schmidt norm, which tends to zero. The cubic remainder in step 3 vanishes under the \(n^{-2}\) normalization. The trace identity turns the centered limit into \(W=\pi/16-\tfrac12\sum a_mX_m\). Absolute expected convergence follows from \(\sum(4m+1)a_m<\infty\). Its variance is \(\frac12\sum(4m+1)a_m^2=c/2\).

All terms \(a_mX_m\) are nonnegative. For every \(\varepsilon>0\), the finite number of leading chi-squares can simultaneously be sufficiently small with positive probability, while the remaining tail is less than \(\varepsilon\) with positive probability by its vanishing mean; this proves the upper endpoint \(\pi/16\) is sharp. The first chi-square component is unbounded and independent of the rest, so the lower support is unbounded.

## Verification

The included standalone program `verify_zonotope.py` verifies exact rational beta–Legendre integrals for degrees through \(28\), the binomial overlap coefficients, the trace/Hilbert–Schmidt spectral identities to a controlled numerical cutoff, and the volume determinant formula independently against convex hull volumes of all endpoint combinations for finite test samples. It also samples fresh uniform orientations to check the predicted finite-sample mean and variance. Run with `python verify_zonotope.py` in an environment with `numpy` and `scipy`; numerical checks are corroborative, not substitutes for the analytical argument.

## Relationship to prior work

Breiding, Bürgisser, Lerario and Mathis (arXiv:2109.14996, first public 2021-09-30; primary MSC2020 52A39) develop the zonoid algebra and formulas for expected absolute random determinants; their work supplies relevant geometric context but does not give the present finite-sample variance or the explicit one-sided fluctuation law. Schneider (arXiv:2202.06774, first public 2022-02-14; primary MSC2020 60D05) establishes expected valuations for random zonotopes and a central limit theorem under a *nonzero first Hoeffding projection*. For unit vectors distributed uniformly on the sphere, that first projection vanishes identically; the Gaussian conclusion of that theorem does not cover this case. Kabluchko and Zaporozhets (arXiv:1706.08092) calculate expected volumes of Gaussian zonotopes, a different radial model and a first-moment rather than second-order result. General degenerate U-statistic theory and spherical harmonics are used as standard tools and are not claimed as new.

## Limitations

The proof is specific to independent Haar-uniform unit directions and ordinary Euclidean volume in dimension three. It does not establish the same coefficients for random segment lengths, anisotropic directions, higher-dimensional volumes, or finite-sample distribution functions. The result has not undergone an independent audit, and an exhaustive historical-priority determination is not claimed.

## References

1. P. Breiding, P. Bürgisser, A. Lerario, L. Mathis, *The zonoid algebra, generalized mixed volumes, and random determinants*, arXiv:2109.14996v1 (2021-09-30), DOI: 10.1016/j.aim.2022.108361.
2. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774v1 (2022-02-14).
3. Z. Kabluchko, D. Zaporozhets, *Expected volumes of Gaussian polytopes, external angles, and multiple order statistics*, arXiv:1706.08092v1 (2017-06-25), DOI: 10.1090/tran/7708.
4. Standard background: Hoeffding's orthogonal decomposition of U-statistics and the Funk–Hecke theorem for spherical harmonics.
