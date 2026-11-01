# Scientific review of the finite pure-level edge-loss law

## Correctness — PASS

The claim is the exact positive \(L^1\)-asymptotic constant at each fixed integer pure Landau level. The normalization is checked directly against the orthonormal complex Hermite definition and finite correlation kernel in Abreu–Gröchenig–Romero, arXiv:1704.03042, equations (1.4), (1.7), and (1.8). Radial Laguerre orthogonality yields probability densities; the infinite pure-level kernel has constant unit intensity. Equality of the finite intensity and disk masses reduces the absolute \(L^1\) error *exactly* to twice the sum of radial probability tails.

The Laguerre tridiagonal Jacobi matrix gives exact mean and variance. A finite-degree generating-function argument proves compact-uniform Hermite edge asymptotics, not merely a fitted numerical limit. Chebyshev bounds control the full complement of the \(O(\sqrt N)\) edge window and justify passing to an integral of the limiting tail. Mehler's identity evaluates the resulting Hermite absolute moment, giving the two central-binomial branches. All quantifiers are fixed-level \(N\to\infty\); the high-level asymptotic is explicitly sequential. The accompanying finite checks are not treated as proof.

## Originality — PASS, subject to historical-priority risk

The most directly relevant antecedent, Abreu–Gröchenig–Romero (2017), gives the same finite pure ensembles and \(O_r(\sqrt N)\) upper bound (Theorem 1.2) and explicitly says sharpness for positive levels is believed, not demonstrated. Its Theorem 1.8 contains the related radial distribution law, but neither theorem states a lower bound or an exact leading constant. The present result resolves that quantitative gap with a global tail-sum convergence proof and binomial constants at *all* levels. Haimi–Hedenmalm (2011) provides polyanalytic local/edge structures, and Haimi–Wennman (2016) gives pure-level linear-statistics fluctuations; neither text inspected states this exact absolute global intensity defect. Results on spectrally selected finite Weyl–Heisenberg ensembles are not automatically estimates for Hermite-index truncated pure ensembles; the focal paper itself distinguishes the two.

The semantic mathematical database was queried for pure polyanalytic Ginibre edge intensity, sharp \(L^1\) boundary loss, Hermite absolute moments, and equivalent Weyl–Heisenberg language. It returned no implication covering the present finite pure ensemble limit; the closest returned Hermite-mask half-line spectral-gap result studies a different operator and invariant. A claim-only overlap reading of the available earlier research ledger identified related Landau disk-concentration eigenvalues and Hermite masks but no global finite-pure-ensemble intensity constant. Nonmatching search results do not establish absolute uniqueness. In particular, stronger forms of local edge convergence and unexamined later work could make the quantitative constant implicit; the priority conclusion remains provisional pending broader independent literature review.

## Mathematical value — PASS

The 2017 focal paper identifies matching lower-order sharpness for positive levels as an unresolved quantitative point. The exact constant is positive at every level, nontrivially depends on the Landau index, has a closed central-binomial expression, and grows like \(4\sqrt r/\pi\) in a sequential high-index limit. It turns a uniform geometric upper-order statement into a sharp thermodynamic law for a canonical determinantal ensemble. The normalization, proof, and numerical tests are reproducible without a new external classification or a broad conjectural framework.

## Limitations and reproducibility

No joint \(r,N\)-limit, noncircular domain, spectral-cutoff variant, or fluctuation/variance result is claimed. No independent mathematical validation has occurred. The package contains a self-contained exposition and a finite `check.py` script; symbolic and numerical checks are supplementary only. The explicit exact density identities, variance, convergence/tail argument, and Mehler coefficient extraction are the essential proof components.

Self-review: passed. Independent audit: not yet performed.
