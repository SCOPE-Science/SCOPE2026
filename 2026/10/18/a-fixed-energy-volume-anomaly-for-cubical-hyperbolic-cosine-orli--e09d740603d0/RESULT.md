# A fixed-energy volume anomaly for cubical hyperbolic-cosine Orlicz bodies

## Finding
For every fixed \(\beta>0\), let
\[
T_{n,\beta}=\left\{x\in\mathbb R^n:\sum_{i=1}^{n}\log\cosh x_i\le\beta\right\},
\qquad B_2^n=\{x\in\mathbb R^n:\|x\|_2\le1\}.
\]
Then as the integer dimension \(n\) tends to infinity,
\[
\boxed{\frac{\operatorname{vol}_n(T_{n,\beta})}{\operatorname{vol}_n(\sqrt{2\beta}\,B_2^n)}
=e^{\beta/2}\left(1-\frac{\beta+\beta^2/4}{n}+O_\beta(n^{-2})\right).}
\]
The implied constant may depend on the fixed positive \(\beta\) but not on \(n\). In particular, the normalized level-one volume converges to \(\sqrt e\) and has first relative finite-dimensional correction \(-5/(4n)\). Although the defining function has quadratic tangent \(\|x\|_2^2/2\), the high-dimensional body retains a nonunit limiting volume ratio.

## Assumptions and scope
The starting cube is \(K_n=[-1/2,1/2]^n\), with unit Euclidean volume. The boundary functional from Haddad–Jiménez–Resende is
\[
\Phi_K(y)=\int_{\partial K}(x\cdot\nu_K(x))
\log\cosh\left(\frac{y\cdot\nu_K(x)}{2x\cdot\nu_K(x)}\right)\,dS(x).
\]
For a cube, define this integral by summing over its facets, with the lower-dimensional edges irrelevant to surface measure. Each pair of opposite unit-area facets contributes \(\log\cosh y_i\). Consequently \(\Phi_{K_n}(y)=\sum_i\log\cosh y_i\), and \(T_{n,\beta}=\{\Phi_{K_n}\le\beta\}\). The body is compact, convex, and has nonempty interior. This facet specialization is a definition of the functional and is not an application of the source's smooth-boundary convergence theorem to a polytope. The theorem concerns fixed \(\beta\) and growing dimension; no uniformity when \(\beta\) grows with dimension is asserted.

## Proof
**1. An exact Dirichlet identity.** By coordinate symmetry, write \(z_i=\beta^{-1}\log\cosh |x_i|\). On each nonnegative coordinate ray, \(|x_i|=\operatorname{arcosh}(e^{\beta z_i})\), and the two signs together contribute the Jacobian
\[
J_{\beta}(z_i)=\frac{2\beta}{\sqrt{1-e^{-2\beta z_i}}}
=\sqrt{\frac{2\beta}{z_i}}\,g(\beta z_i),
\qquad g(t)=\sqrt{\frac{2t}{1-e^{-2t}}}
=e^{t/2}\sqrt{\frac{t}{\sinh t}}.
\]
Take continuous values at zero. The transformed domain is the standard simplex \(z_i\ge0\), \(\sum_i z_i\le1\). Repeating the substitution for a Euclidean ball of squared radius \(2\beta\), using \(|x_i|=\sqrt{2\beta z_i}\), gives the same base Jacobian without \(g\). The Dirichlet integral formula therefore proves the exact identity
\[
R_{n,\beta}:=\frac{\operatorname{vol}_n(T_{n,\beta})}{\operatorname{vol}_n(\sqrt{2\beta}\,B_2^n)}
=\mathbb E\prod_{i=1}^{n}g(\beta Z_i),
\]
where \((Z_0,Z_1,\ldots,Z_n)\) has the Dirichlet law with parameters \((1,1/2,\ldots,1/2)\), and \(Z_0=1-\sum_{i=1}^{n}Z_i\).

**2. A uniform logarithmic expansion.** Since \(\log(\sinh t/t)=t^2/6+O_\beta(t^4)\) uniformly for \(0\le t\le\beta\),
\[
\log g(t)=\frac t2-\frac{t^2}{12}+O_\beta(t^4).
\]
Put \(Q=\sum_{i=1}^{n}Z_i^2\). Since \(\sum_i Z_i=1-Z_0\),
\[
\sum_{i=1}^{n}\log g(\beta Z_i)
=\frac\beta2-\frac\beta2Z_0-\frac{\beta^2}{12}Q+E,
\quad |E|\le C_\beta\sum_{i=1}^{n}Z_i^4.
\]
The uniformity uses only fixed \(\beta\) and the bound \(0\le Z_i\le1\).

**3. Exact moments and the finite-size coefficient.** With \(D_n=(n+2)(n+4)(n+6)(n+8)\), the Dirichlet moments are
\[
\mathbb E Z_0=\frac2{n+2},\qquad
\mathbb E Z_0^2=\frac8{(n+2)(n+4)},\qquad
\mathbb E Q=\frac{3n}{(n+2)(n+4)},
\]
\[
\mathbb E Q^2=\frac{105n+9n(n-1)}{D_n},\qquad
\mathbb E\sum_{i=1}^{n}Z_i^4=\frac{105n}{D_n}.
\]
In particular, \(\mathbb E(Z_0+Q)^2=O(n^{-2})\) by Cauchy–Schwarz, and \(\mathbb E|E|=O_\beta(n^{-3})\). Because \(\log g(\beta Z_i)\le\beta Z_i/2\), the total exponential is uniformly bounded above by \(e^{\beta/2}\). The elementary inequality \(|e^{-a}-1+a|\le C a^2\) for bounded nonnegative \(a\), with the analogous Lipschitz bound for the small remainder \(E\), permits expectation term by term. Thus
\[
R_{n,\beta}=e^{\beta/2}\left[1-\frac\beta2\mathbb E Z_0-\frac{\beta^2}{12}\mathbb E Q+O_\beta(n^{-2})\right]
\]
\[
=e^{\beta/2}\left[1-\frac\beta{n+2}-\frac{\beta^2n}{4(n+2)(n+4)}+O_\beta(n^{-2})\right]
=e^{\beta/2}\left[1-\frac{\beta+\beta^2/4}{n}+O_\beta(n^{-2})\right].
\]
This completes the proof for all fixed positive levels. In particular the limit is \(e^{\beta/2}\), not one.

## Verification
The standalone file `check_volume.py` independently verifies exact rational Dirichlet moments in dimensions 1 through 44, 999 Jacobian-function inequalities and Taylor comparisons, direct planar area quadratures at three different levels, and Monte Carlo Dirichlet checks in three larger dimensions. Its finite-dimensional outputs are corroboration only. The infinite-dimensional conclusion and the uniform error bound follow from the analytical moment argument above. Use `python check_volume.py` with Python 3; the exact rational part requires only the standard library, while optional planar and sampling checks use `mpmath` and `numpy`.

## Relationship to prior work
Haddad, Jiménez and Resende introduced the boundary-integral hyperbolic-cosine functional as the critical transition shape associated with their smooth covariogram construction. The facet evaluation for the unit-volume cube gives the present Orlicz body, but their main work does not compute its dimension-dependent normalized volume. Previously established John/Löwner ellipsoid formulas for cubical transition bodies concern extremal radii and affine distances, not this volume ratio or its correction. Barthe–Wolff and Kabluchko–Prochno study high-dimensional volume properties of general Orlicz balls, primarily in the extensive-energy scale; their stated results do not give this fixed-energy two-term law. The new point is the exact Dirichlet representation followed by its sharp geometric volume asymptotic, not the general definition of an Orlicz body.

## Limitations
The estimate assumes one fixed level as dimension grows. It is not a uniform estimate in a dimension-dependent level, nor a theorem about arbitrary Orlicz functions, arbitrary parallelotopes without the prescribed unit-volume normalization, or the validity of a smooth-body limit theorem at a nonsmooth cube. A prior unindexed equivalent small-energy Orlicz-volume formula could affect historical priority; published-source checks cannot establish absolute novelty. The proof and independently reproducible checks establish the mathematical identity for the stated family.

## References
- J. Haddad, C. H. Jiménez and M. Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1, publicly available October 8, 2026, https://arxiv.org/html/2610.11700v1 .
- F. Barthe and P. Wolff, *Volume properties of high-dimensional Orlicz balls*, arXiv:2106.01675, 2021, https://arxiv.org/abs/2106.01675 .
- Z. Kabluchko and J. Prochno, *The maximum entropy principle and volumetric properties of Orlicz balls*, arXiv:2007.05247, 2020, https://arxiv.org/abs/2007.05247 .
