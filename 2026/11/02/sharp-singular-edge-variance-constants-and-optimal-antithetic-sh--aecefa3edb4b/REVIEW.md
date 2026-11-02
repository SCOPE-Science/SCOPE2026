# Review of the singular-edge shifted-grid coupling theorem

## Correctness — PASS
Unbiasedness is cellwise integration; positivity supplies a coupling-independent sharp moment threshold. A uniformly Cauchy centered power sum gives the exact limiting Hurwitz profile. Its oscillatory Fourier coefficients are evaluated by the gamma integral; Parseval verifies both constants. Countermonotone rearrangement optimizes the covariance and uniform marginal L2 errors justify optimization before the asymptotic limit. The calculations in `verify.py` pass for two exponents and two finite-grid comparisons; they support but do not certify the infinite theorem.

## Originality — PASS (qualified)
The two-global-shift antithetic construction and the rearrangement inequality are **not** new. Ben-Ameur, L'Ecuyer and Lemieux (2004) already analyze antithetic randomized lattice points. Wu's 2020 preprint treats independently paired random cells and regular integrands, whereas L'Ecuyer, Munger and Tuffin (2010) treat smooth shifted-lattice errors and include a qualitative unbounded-tail example, but not the stated sharp singular-edge constants. Goda, Kazashi and Suzuki (2022) work in Gaussian Sobolev spaces with different randomization. Neither the exact singular-profile coefficient nor the \(2\sin^2(\pilpha/2)\) all-coupling gain was found in the inspected literature or published-record searches. The claimed novelty is the compound **sharp singular-edge numerical classification**, not its constituent classical tools. A prior equivalent special-function calculation remains possible.

## Value — PASS
Weak endpoint singularities occur in transformation-based quadrature and integral kernels. The result quantifies when common-shift averaging is not even square integrable, and exactly how much an optimal second shift can reduce asymptotic variance where RMS is defined. The distinction from independent cellwise stratification and from arbitrary importance sampling is essential.

## Closest literature and limitations
Primary sources: arXiv:2011.15086; DOI:10.1287/moor.1040.0101; DOI:10.1214/10-EJS574; arXiv:2212.11476. No exact publication-priority certificate is claimed. One dimension, uniform marginal shifts, equal positive weights, two complete grids and fixed \(C^2\) positive multipliers only; no claim of optimality among all quadratures or stable numerical performance in floating-point arithmetic.

Self-review: passed. Independent audit: not yet performed.
