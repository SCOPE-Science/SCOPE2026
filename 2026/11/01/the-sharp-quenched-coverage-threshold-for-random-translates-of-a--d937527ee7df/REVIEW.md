# Scientific review

## Correctness
PASS. For a uniform query point in the doubled cube, the coordinatewise hit probabilities are independent uniforms and the negative log hit probability is Gamma(d,1). A maximum-of-exponentials representation identifies the exact expectation. The gamma Edgeworth term and the Gumbel extreme-value mean shift produce the explicitly stated constant, and a McDiarmid tail with exponent proportional to \(4^d/m\), followed by Borel–Cantelli and monotone threshold inversion, upgrades mean to almost-sure threshold. The extracted standalone standard-library verifier passed 120 deterministic cases. This computation is not a substitute for the analytic argument.

## Originality
PASS, with a material prior implication clearly separated. Zhigljavsky and Noonan (2020), Section 4.2, already give the all-parameter **finite expected covered fraction** of random smaller axis-parallel cubes inside a cube; the present finite sum is a special case and not claimed as novel. The evaluated claim is the **realized** partial-coverage hitting time, its exact dimension-dependent Gaussian window and its constant-order shift \(-\gamma-(1-s^2)/3\). Shelley and Tartakovsky (2026) address topology of deterministic translate unions; Penrose (2023) treats complete coverage by variable-radius balls, with abstract-level source access only. The accessible published mathematical comparisons found no stated equal or stronger hitting-time asymptotic. An earlier unindexed probabilistic corollary remains a meaningful priority risk.

## Mathematical value
PASS. The constant sample-size factor for **half coverage**, \(\exp(-\gamma-1/3)\), distinguishes a sharp high-dimensional geometric threshold from a leading exponential estimate. The almost-sure result is reproducible and supplies an exact benchmark for random partial coverage by equal cubes, unlike arbitrary parameter slicing. The scope is restricted to product cubes, fixed coverage fractions below one, and dimension tending to infinity.

## Literature and limitations
The closest substantial source is Zhigljavsky–Noonan 2020 (doi:10.1007/s43069-020-0015-8), which dominates the finite mean but not the stated sample-wise limit. Shelley–Tartakovsky arXiv:2610.25841 supplies the current union-of-translates context. The proof does not address complete coverage or non-product bodies. Earlier unindexed probability literature could affect priority.

Self-review: passed. Independent audit: not yet performed.
