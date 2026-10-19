# Sharp Gaussian-noise moment thresholds for row-power randomized Kaczmarz

## Finding

**Theorem (one-step unconditional moment spectrum).** Let \(m\ge 2\), \(d\ge 1\), \(\sigma>0\), \(s\ge 0\), and \(b\in\mathbb R^m\setminus\{0\}\). Fix arbitrary deterministic vectors \(\mu_1,\ldots,\mu_m\in\mathbb R^d\). Independently draw \(a_i=\mu_i+\sigma Z_i\), where the \(Z_i\) have independent standard real Gaussian coordinates, and set \(R_i=\|a_i\|_2\). Conditional on all the rows, sample \(I\) with probabilities
\[
 \Pr(I=i\mid a_1,\ldots,a_m)=\frac{R_i^{2s}}{\sum_{j=1}^m R_j^{2s}}.
\]
At \(s=0\) this means uniform sampling. Starting at zero, perform one unrelaxed Kaczmarz update for the observed linear equations, \(x_1=b_I a_I/R_I^2\). For every real \(q>0\),
\[
 \boxed{\quad \mathbb E\|x_1\|_2^q<\infty\quad\Longleftrightarrow\quad q<q_{\mathrm c}:=\min\{md,d+2s\}.\quad}
\]
The expectation jointly averages the observed Gaussian coefficient matrix and the row choice, and at each equality boundary it is infinite.

For the classical squared-row-norm rule \(s=1\), the *exact* second moment (whenever \(md>2\)) is
\[
 \boxed{\ \mathbb E\|x_1\|_2^2
 =\frac{\|b\|_2^2}{\sigma^2}e^{-\lambda/2}
 \sum_{j=0}^{\infty}\frac{(\lambda/2)^j}{j!\,(md+2j-2)},\quad
 \lambda=\frac{\sum_i\|\mu_i\|_2^2}{\sigma^2}.\ }
\]
It is infinite when \(md\le 2\), including arbitrarily small but nonzero Gaussian noise around a fixed nonsingular noiseless design. In the central Gaussian benchmark \(\mu_i=0\), \(b_i=1\), and \(s=1\), the entire finite part of the moment spectrum is
\[
 \boxed{\ \mathbb E\|x_1\|_2^q
 =\frac{2m\,\Gamma((d+2-q)/2)}{(md-q)\,\Gamma(d/2)\,(2\sigma^2)^{q/2}},
 \quad 0<q<\min\{md,d+2\}.\ }
\]

Hence for \(d=1\), row-norm-squared sampling has a finite one-step second moment exactly from \(m=3\) rows onward; for \(d=2\), it has a finite second moment from \(m=2\) onward. Uniform row sampling has infinite second moment in **both** dimensions, whatever the row count. Averaging any fixed finite number of independently Gaussian repeated coefficient measurements changes \(\sigma\), but never changes these finiteness thresholds.

## Assumptions and scope

All dimensions and Gaussian distributions are finite-dimensional and real. Noise is independent between matrix entries, with a common strictly positive variance; the noiseless row means are arbitrary. The right-hand side \(b\) is deterministic and has at least one nonzero component. It may be the right-hand side of a consistent full-column-rank noiseless system. Sampling uses the **observed**, not the underlying noiseless, row lengths. The observed rows are retained during row selection. The theorem concerns the unconditional distribution of the **first** iterate, not the conditional-on-data guarantee or a multi-step convergence rate.

The coefficient-normalization formula holds almost surely since all observed row lengths are nonzero almost surely. The probability rule is defined for \(s=0\) by the constant weights \(1\).

## Proof

**1. Reduction to a radial integral.** Conditional expectation over the row draw is exactly
\[
 \mathbb E(\|x_1\|_2^q\mid a_1,\ldots,a_m)
 =\frac{\sum_{i=1}^m |b_i|^q R_i^{2s-q}}{\sum_{j=1}^m R_j^{2s}}. \tag{1}
\]
For \(s=0\), the denominator is \(m\) and the numerator consists of inverse powers of nondegenerate Gaussian row lengths. The Gaussian density is continuous and strictly positive at zero, so an inverse radial moment in \(d\) dimensions is finite precisely when \(q<d\), agreeing with \(\min\{md,d\}=d\).

Now suppose \(s>0\). Write the concatenated observed matrix as a vector \(a\in\mathbb R^{md}\) and use polar coordinates \(a=\rho\theta\), where \(\rho>0\) and \(\|\theta\|_2=1\). Partition \(\theta=(\theta_1,\ldots,\theta_m)\) into \(d\)-dimensional blocks and put \(u_i=\|\theta_i\|_2\). Then (1) becomes
\[
 \rho^{-q}\frac{\sum_i |b_i|^q u_i^{2s-q}}{\sum_j u_j^{2s}}. \tag{2}
\]
On the unit sphere, \(\sum_j u_j^{2s}\) is bounded below by a strictly positive number (depending on \(m,s\)). Near the stratum \(u_i=0\) with another block nonzero, spherical measure contributes \(u_i^{d-1}\,du_i\) up to a smooth bounded nonvanishing factor. Consequently the angular integral of (2) is finite exactly when \(d+2s-q>0\): necessity uses any block \(i\) for which \(b_i\ne0\). Intersections of block-zero strata introduce no stronger condition because the denominator is globally bounded below on the sphere and the numerator is a sum of one-block terms.

The full noncentral Gaussian joint density is continuous, positive at the origin, and bounded above there. The radial volume element is \(\rho^{md-1}\,d\rho\); hence the integral near the simultaneous zero-matrix configuration is finite exactly when \(q<md\). If \(q\ge md\), restrict to an open patch of angles on which every block length is bounded away from zero; (2) gives a strictly positive multiple of \(\rho^{-q}\), proving divergence. If \(q\ge d+2s\), restrict the other row lengths to a compact annulus away from zero and let one row with \(b_i\ne0\) approach zero; (1) behaves as a positive multiple of \(R_i^{2s-q}\), proving divergence. All tails with \(\rho\ge1\) are integrable because the Gaussian density decays quadratically in \(\rho\), while the angular integral is finite in the claimed range. This proves the sharp iff statement, including equality.

**2. Explicit Gaussian second moment.** At \(s=1,q=2\), the numerator in (1) is \(\|b\|_2^2\), so
\[
 \mathbb E\|x_1\|_2^2=\|b\|_2^2\,\mathbb E\left(\sum_i\|a_i\|_2^2\right)^{-1}. \tag{3}
\]
After division by \(\sigma^2\), the sum of squares is a noncentral chi-square variable with \(md\) degrees of freedom and noncentrality \(\lambda\). Its standard Poisson mixture contains central chi-square laws with degrees \(md+2j\), and each central reciprocal moment equals \(1/(md+2j-2)\) if the degrees exceed two. Tonelli's theorem yields the displayed series. The positive mass on its \(j=0\) component forces divergence for \(md\le2\).

**3. Exact central all-moment benchmark.** When every \(\mu_i=0\), let \(X_i=R_i^2/\sigma^2\), so the \(X_i\) are independent chi-square variables with \(d\) degrees of freedom. Their sum \(S\) is chi-square with \(md\) degrees; the fraction \(V=X_1/S\) is independent of \(S\) and beta-distributed with parameters \(d/2,(m-1)d/2\). Symmetry and (1) give
\[
 \mathbb E\|x_1\|_2^q=m\sigma^{-q}\,\mathbb E[S^{-q/2}]\,\mathbb E[V^{1-q/2}].
\]
Insert the elementary gamma and beta moment formulas and cancel \(\Gamma(md/2-q/2)\) against \(\Gamma(md/2+1-q/2)\). The result is the stated gamma-function expression; its two positivity requirements are precisely \(q<md\) and \(q<d+2\).

**4. Finite measurement averaging.** The average of any fixed positive integer number \(L\) of independent observations \(\mu_i+\sigma Z_{i,l}\) is distributed as \(\mu_i+(\sigma/\sqrt L)Z_i\). Since \(\sigma/\sqrt L>0\), steps 1–3 apply unchanged; only finite values, not moment-existence thresholds, change.

## Verification

The accompanying `reproduce.py` checks the exact central gamma/beta moment formula at six distinct dimension/moment triples against independently sampled weighted-row Kaczmarz updates (300,000 draws per configuration), compares the noncentral Poisson reciprocal-chi-square series with direct noncentral chi-square quadrature at three parameter triples, and checks the exact central second-moment identity on a dimension grid. The program was executed successfully with Python, NumPy and SciPy. Finite simulations do not establish divergence or any infinite-dimensional assertion; the polar-integrability proof establishes the sharp moment thresholds.

## Relationship to prior work

Gan and Wu (arXiv:2608.22259, first posted 2026-08-23) study randomized Kaczmarz and variants on doubly noisy systems, notably conditional-on-observed-matrix error estimates and convergence neighborhoods. Zhang, Zeng and Zhang (arXiv:2603.29372, 2026-03-31) treat relaxed greedy sampling and signal averaging. Their introductory equation (1.4) is the usual squared-row-norm sampling rule and (1.5) contains a conditional noise-horizon denominator involving the observed Frobenius norm. Bergou et al. (arXiv:2308.16904, 2023-08-31; SIAM J. Matrix Anal. Appl. 2024) likewise study doubly noisy Kaczmarz for fixed observed systems. The present result instead averages **over the Gaussian matrix realization** and characterizes the exact \(q\)-moment existence spectrum across a continuum of row-power sampling rules. Its standard-sampling second-moment identity is compatible with the known conditional Kaczmarz relation and is not claimed as a new conditional formula. Standard beta, gamma and noncentral chi-square identities are also established prior tools, not new lemmas.

## Limitations

The theorem only concerns one unrelaxed row projection from zero. The full observed matrix need not have full rank. Finite variance of the first update does not imply finite stationary variance, mean-square convergence, or robustness of many successive projections. A Gaussian distribution has positive density arbitrarily near an all-zero observed matrix even when its mean is well conditioned; probabilities of extreme events may therefore be very small in ordinary experiments. The central moment formula is a benchmark for zero-mean random rows rather than a claim of consistency of the underlying noise-free system. No closed-form tail constant is claimed for general noncentral means or power \(s\); the exact assertion is the moment-existence boundary.

## References

1. Y. Gan and G. Wu, *On Convergence Behavior of Randomized Kaczmarz-type Methods for Solving Doubly Noisy Linear Systems*, arXiv:2608.22259 (first posted 2026-08-23), https://arxiv.org/abs/2608.22259.
2. L. Zhang, J. Zeng and H. Zhang, *Relaxed Greedy Randomized Kaczmarz with Signal Averaging for Solving Doubly-Noisy Linear Systems*, arXiv:2603.29372 (first posted 2026-03-31), https://arxiv.org/abs/2603.29372.
3. E. H. Bergou, S. Boucherouite, A. Dutta, X. Li and A. Ma, *A Note on the Randomized Kaczmarz Algorithm for Solving Doubly Noisy Linear Systems*, SIAM Journal on Matrix Analysis and Applications 45 (2024), 992–1006; preprint arXiv:2308.16904, https://arxiv.org/abs/2308.16904.
4. T. Strohmer and R. Vershynin, *A Randomized Kaczmarz Algorithm with Exponential Convergence*, Journal of Fourier Analysis and Applications 15 (2009), 262–278.
