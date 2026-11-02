# Review: sharp anisotropy-uniform contraction of the exact Gaussian rotation--OU Strang sampler

## Correctness: PASS

Exact Gaussian OU transitions and a symmetric random rotation each preserve the target and are reversible. Their symmetric composition retains those properties. The full squared-coupling covariance map reduces to a symmetric two-by-two matrix, with the quoted exact Perron factor. Positivity, contraction of both coordinate directions at the limiting anisotropic endpoint, and a small-step matrix expansion give the claimed all-step uniform bound and limits. The Python checker independently tests 466 numerical comparisons; the analytical proof, rather than the tests, establishes all parameter quantifiers.

## Originality: PASS

Louis--Pavliotis--Vilmart (2026), Theorem 2, proves a continuous-time spectral-gap bound, and its Section 6.3 uses a related splitting template with RK4 evaluation of the perturbation. The present exact rotation scheme and exact discrete covariance contraction factor are additional. Abdulle--Pavliotis--Vilmart (2019) develops the continuous reversible Stratonovich construction; Duncan--Pavliotis--Zygalakis (2017) studies nonreversible deterministic drift splitting. None of the material inspected supplies this quantitative discrete Perron rate. General detailed-balance and splitting preservation facts are credited. An older equivalent specialized calculation remains possible, and the inspected older sources were not read exhaustively.

## Mathematical value: PASS

The result addresses a motivated numerical-sampler question: does the continuous target-preserving accelerated dynamics admit a stable, unbiased and quantitatively mixing discretization even for an ill-conditioned Gaussian target? The derived exact-subflow method answers this question in its two-dimensional quadratic regime and provides a sharp per-step rate useful for parameter benchmarking. No statement about the cost or bias of an approximate RK4 implementation, nonlinear targets, or higher dimensions is made.

## Limits and references

The exact sharpness concerns synchronous squared-coupling asymptotic rate, not the optimal Wasserstein contraction constant. See arXiv:2610.03191v1, arXiv:1903.03024 and arXiv:1701.04247 for the continuous model, precursor and splitting context.

Self-review: passed. Independent audit: not yet performed.
