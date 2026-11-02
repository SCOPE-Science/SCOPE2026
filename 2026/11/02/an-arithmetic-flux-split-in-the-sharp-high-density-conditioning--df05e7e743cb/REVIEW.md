# Scientific review

## Correctness — PASS

The claim is precisely about the fixed normalized first-Hermite window on square lattices with reciprocal density \(q\in\mathbb Z\) or \(q\in\mathbb Z+1/2\), for \(q\ge3\). Direct Gaussian integration proves the coefficient normalization. Two Poisson summations give a norm-convergent Janssen representation. The four shortest dual vectors have exact common coefficient \((1-\pi q)e^{-\pi q/2}\). All remaining coefficients have an **infinite**, explicitly bounded norm tail at most \(100q e^{-\pi q}\). The Harper nearest-neighbor operator has symmetric spectral edges, with **exact** norm \(4\) at integer flux and \(2\sqrt2\) at half flux: approximate common-eigenvector combs prove attainability, and anticommutation provides the latter upper bound. Spectral perturbation and division by the positive lower frame bound give the claimed optimal-bound and condition-number asymptotics. No numerical step is used to establish an infinite theorem.

The standalone Python 3 checker passed 20,430 finite assertions for supplementary tail and Bloch-spectrum consistency. The proof itself verifies all quantifiers and normalizations; the checker does not certify originality or infinite spectral assertions.

## Originality — PASS under inspected evidence

Closest first-Hermite source: Faulhuber–Petersen, arXiv:2609.02610, Theorem 1.2, proves a **frame/non-frame classification**, not quantitative sharp frame bounds. Faulhuber–Shafkulovska–Zlotnikov, arXiv:2609.01296, Theorem 1.1 and Sections 2–3, use the same Laguerre/Janssen ingredients to establish **large Hermite-order** frame safety, not the fixed order-one, high-redundancy asymptotics. Their Laguerre ambiguity identity is acknowledged as prior. The 2025 open-access Hermite paper proves boundary safety for other orders, and the 2022–2023 Gabor bound-optimization paper treats hyperbolic secants and exponential windows. The 2017 Gaussian paper obtains Gaussian theta-function bounds, not the order-one Hermite constants. A mathematical-record search located neighboring arithmetic frame/non-frame and high-order safety results but no equivalent sharp two-sequence condition-number formula.

The magnetic nearest-neighbor norm calculation by itself is elementary Harper algebra and is not claimed to be new. The new mathematical statement is the **sharp quantitative transfer** of its arithmetic flux split to optimal frame-bound asymptotics, with explicit uniform tail control. Residual risk: an implicit equivalent expansion may occur in older or incompletely indexed Hermite/Janssen calculations. Searches cannot prove uniqueness.

## Value — PASS

This is a natural quantitative refinement of recent first-Hermite frame-set results: the full frame property does not measure conditioning. The theorem identifies a nontrivial phase-sensitive obstruction at the first exponentially small scale, separating the integer and half-integer sequences by an exact \(\sqrt2\) factor. This matters for stability of dense time-frequency sampling and gives an exact arithmetic effect that is invisible in a simple absolute-coefficient Janssen upper bound. The sharp constants are not merely restated qualitative sufficiency, a routine numerical improvement, or an arbitrary finite slice.

## Scope and remaining scientific risks

The result does not optimize lattice shape and does not classify other rational or irrational fluxes. Its error estimate is strong enough to determine only the displayed leading asymptotic; no finite-index equality is claimed. Existing generic Harper spectral identities are accepted as background, not asserted as original; no independent expert verification has taken place.

Self-review: passed. Independent audit: not yet performed.
