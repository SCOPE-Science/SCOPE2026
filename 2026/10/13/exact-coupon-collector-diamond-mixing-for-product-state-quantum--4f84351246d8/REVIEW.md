# Scientific assessment of exact product-refresh mixing

## Correctness — PASS
The complete claim follows from a direct Kraus normalization, commutation and idempotence of site resets, decomposition conditioned on complete coupon coverage, and an explicit orthogonal product input that saturates the diamond upper bound. Inclusion–exclusion yields the exact weighted expression. A summable binomial bound justifies the full Gumbel limit, while the classical comparison is proved by Walsh chi-square and magnetization concentration. Checks from the included actual `verify.py` path reproduced the independent Kraus, mask and product-witness relationships in 122 tests. The infinite statements are analytically proved and do not follow only from tests.

## Originality — PASS, with priority uncertainty
The directly relevant source is Temme–Wocjan, arXiv:2504.02651v1, specifically its general grand-coupling Kraus formula, its coupon-collector hypercube example, its one-sided tail bound, and the explicit open question concerning the stationary-probability prefactor. The source is credited for the quantization mechanism and the classical coupon connection. Its inspected version 1 and accessible final manuscript do not give the exact operational diamond norm, a matching product-state witness, arbitrary weighted product-state coverage equality, or the uniform diamond profile. Classical coupon and hypercube cutoff results are not claimed as new. Searches for the exact diamond norm and aliases found no covering result in the checked index and external literature. The possibility of a derivation in earlier unindexed literature, or one viewed as an implicit immediate consequence of standard reset algebra, remains the principal originality risk.

## Value — PASS
The exact result is an operationally strong (reference-ancilla-robust) finite-time mixing law for a natural product qsample-preparation family. It removes an avoidable stationary-minimum prefactor for this entire family, identifies a concrete sharp cutoff and its constant-order profile, and demonstrates an explicit factor-two separation from the corresponding classical total-variation location. These are useful exact benchmarks beyond numerical mixing experiments; the statement does not claim a broad result for interacting or noncommuting quantum samplers.

## Limitations
The theorem assumes rank-one resetting maps that commute, with independent draws; all local dimensions are finite and at least two. The claim does not cover interacting Gibbs targets, mixed targets, partial updates, or arbitrary grand couplings. Earlier implicit publication coverage is not fully excluded. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
