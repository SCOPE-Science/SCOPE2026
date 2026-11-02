# Scientific review: pinned-row Kaczmarz selection

## Correctness

**PASS.** The statement restricts to positive diagonal systems, exact constraints, unconditional independent norm-squared row draws and exact Kaczmarz projection. Each draw annihilates exactly one error coordinate and otherwise leaves the state unchanged. Bernoulli survival of each coordinate yields the exact expectation, and maximizing over initial errors yields the sharp worst-case factor. A sorted-index exchange argument proves the global consecutive-window optimum, including the strict uniqueness of the window form for distinct weights. Ordinary finite inclusion-exclusion and geometric summation give the coupon-collection distribution and mean. All four triples of the four-row example are compared by exact rational numbers. The three-row Frobenius/CPQR example is proved algebraically. The standalone verifier passed 15,133 exact rational assertions. Boundary restrictions and the distinction from conditional zero-residual resampling are explicit. Finite checks are supplementary; universal conclusions are analytical.

## Originality

**PASS, with priority uncertainty.** Sun, Qi, Han and Xie's 2026 paper provides a general projected randomized-iteration rate and proposes Frobenius residual selection, but its inspected Sections 3.1–3.2, 5.2 and Appendix 7.2–7.3 do not solve diagonal all-cardinality optimal pinning or compare worst-case expected error against expected exact completion. Lok and Rebrova's 2023 subspace-constrained Kaczmarz paper provides the unconditional update and general rate bound, not the pair of exact discrete selection criteria. Strohmer–Vershynin provides the classical expected contraction estimate, and classical coupon collection supplies a fixed-distribution expectation; these ingredients are acknowledged rather than claimed as novel. The new combined claim is the complete consecutive-block rate-selection classification, exact finite-time criterion and a sharp conflict/worst-case surrogate gap for one natural method. Relevant published search records concerned different algorithms such as adaptive coordinate sampling, multistage pivoting and ordinary Kaczmarz rate bounds. A general unlocated normalized-weight *subset*-selection result might subsume the simple exchange lemma, and historical priority is not independently established. One distinction is essential: Sun et al. reject zero-residual draws in their Algorithm 1; the stated unbounded sample count concerns unconditional iid draws as in Lok–Rebrova, not Sun's count of accepted updates.

## Mathematical value

**PASS.** The pinned-row subset design problem is explicitly motivated by the 2026 preconditioning framework, and the correct mathematical objective can be either worst-case mean-square contraction or time until exact solution. The theorem solves the former for every diagonal dimension and fixed pin budget, shows a concrete conflict with the latter using only moderate squared row magnitudes, and identifies an arbitrarily bad Frobenius-skeleton proxy for the first objective. This distinguishes genuinely different performance measures rather than merely recomputing a known matrix norm. It is not a practical wall-clock/noisy-data superiority claim: pinning tiny rows may be costly or noise-sensitive, and rejecting zero-residual draws changes the conclusion.

## Closest literature and limitations

- Sun, Qi, Han and Xie, *On subspace-constrained preconditioning for randomized iterative methods* (2026), arXiv:2605.29304v1. Rate formula, surrogate criterion and different zero-residual rejection convention.
- Lok and Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation* (2023/2024), arXiv:2309.04889. Unconditional SCRK formulation and known general rate bound.
- Strohmer and Vershynin, *A randomized Kaczmarz algorithm with exponential convergence* (2007), arXiv:math/0702226. Classical randomized-row convergence bound.
- Steinerberger, *Randomized Kaczmarz converges along small singular vectors* (2020), arXiv:2006.16978. Related sharpness of slow spectral directions, not optimized fixed subsets.
- Anceaume, Busnel and Sericola (2014), arXiv:1402.5245, and Anceaume, Busnel, Schulte-Geers and Sericola (2015), arXiv:1504.03878. General nonuniform coupon-collector distributions and uniform-probability optimality, not selection from pinned matrix rows.

The finding does not extend to general matrices, adaptive sketches, methods rejecting zero-residual samples, data noise or total computational work. The original mathematical source ingredients are credited and no independent priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
