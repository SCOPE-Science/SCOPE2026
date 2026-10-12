# Review

## Correctness

PASS. The key mixed moment reduces exactly:
\[
\mathbb E[S_n\mathbf 1_{\{S_k>0\}}]
=
\mathbb E[S_k\mathbf 1_{\{S_k>0\}}]
=
\frac12\mathbb E|S_k|.
\]
The first equality uses independence and zero mean of the future increment block; the second uses symmetry. Summing over \(k\) proves the covariance identity without approximation.

For continuous symmetric iid increments, the Sparre-Andersen occupation count has the discrete arcsine law, equivalently beta-binomial parameters \((n,1/2,1/2)\), so its variance is \(n(n+1)/8\). The central limit theorem plus the uniformly bounded second moments of \(S_k/(\sigma\sqrt{k})\) gives convergence of first absolute moments and the universal correlation limit.

## Originality

PASS, with a residual risk from classical fluctuation literature. Ivanovs's full paper was inspected because it is unusually close: it treats Sparre-Andersen identities, occupation times, exchangeable increments, and random walks in one framework. Its random-walk section states distributional equivalences among occupation and extremal times, but the inspected text does not state an occupation-count/terminal-displacement covariance.

Döbler's full public text studies the symmetric-random-walk arcsine marginal and quantitative convergence. Targeted searches found no covariance or terminal-value formulation.

Hartmann--Majumdar's Brownian paper explicitly studies correlations among occupation time, time of maximum, and last-passage time. The inspected article does not include terminal position among the three variables, so it does not cover the Brownian endpoint identity or the discrete random-walk covariance formula.

## Value

PASS. Occupation time and terminal displacement are two basic path observables in one-dimensional fluctuation theory, but their marginal theories are usually presented separately. The exact identity reduces their dependence to the absolute first moments of the partial sums, and the combination with Sparre-Andersen universality produces a distribution-free nonzero limiting correlation.

The same constant \(4/(3\sqrt{\pi})\) appears exactly in the Brownian continuum model, giving a clean discrete-to-continuum dependence law rather than a routine marginal calculation.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK lattice_paths=131070 covariance_checks=16 arcsine_normalizations=200 arcsine_means=200 arcsine_variances=200 gaussian_checks=5 last_corr=0.752254651282 target=0.752252778064`.
