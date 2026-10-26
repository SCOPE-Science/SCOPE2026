# Scientific review

## Correctness — PASS
The matrix integral identifies \(F_t\) as stochastic. The two-state minimal polynomial produces an exact inverse with nonpositive off-diagonals. For the three-state directed cycle, exact circulant inversion and spectral reconstruction yield the displayed coefficient; a convergent power series with coefficients \(3^k+(-1)^k(4k-1)>0\) for every integer \(k\ge2\) proves its strict positivity for all positive time. Its exact sine factor proves all resonance statements. The included checker reconstructs the function from its matrix Taylor series rather than assuming the closed form. Limitation: numerical checks are not the infinite-time proof.

## Originality — PASS (best-knowledge)
The main predecessors develop numerical inversion of \(\varphi\)-functions and reciprocal Bernoulli/rational expansions. Boito–Eidelman–Gemignani 2018 even uses cyclic permutation matrices for approximation experiments. Neither that full text nor Gemignani 2023 states the globally strict directed-cycle sign theorem, minimal state dimension, or exact resonant crossing set. Searches of mathematical research records using equivalent formulations found no directly covering result. The local Taylor-series sign at small time is already implicit in classical Bernoulli coefficients; novelty is restricted to the global all-time classification and exact resonance formula. An equivalent unnoticed application of a general matrix-function theorem remains possible.

## Value — PASS
Inverse \(\varphi_1\)-operators arise when recovering forcing terms from integrated observations of positive linear dynamics. A positive stochastic average does not imply that its inverse retains the Z-/M-matrix sign pattern: the theorem locates the sharp universal two-state boundary, proves failure at every time for the smallest irreducible nonreversible cycle, and identifies infinitely many exact damped spectral crossings. This is an interpretable structural classification, not a single small-step counterexample or a numerical table. Scope is finite-state exact arithmetic, with an explicit three-cycle witness rather than an all-generator three-state classification.

## Closest literature and uncertainty
Gemignani, arXiv:2302.07565 (§§1–3,5), and Boito–Eidelman–Gemignani, arXiv:1801.04573 (§§1–3), were inspected in full text. The later Aceto–Gemignani work, arXiv:2406.01437, and its journal overview were inspected for plausible overlap. Prior rational-representation theorems can evaluate the inverse and imply its short-step expansion, but none of the inspected materials establishes the required strict all-time entry sign or oscillatory equality set. Search incompleteness and a possible equivalent classical circulant identity are residual originality risks. No independent review has been performed.

Self-review: passed. Independent audit: not yet performed.
