# Scientific review

## Correctness — PASS

The absorbing first hub announcement follows from the monotone neighbor-majority advantage; the exact sample-size law follows by integrating independent exponential first-activation times. The fixed-bias constant is derived from a biased-random-walk Green function, and the weak-signal law from a conditional binomial central-limit theorem and a beta-distributed exposure fraction. These are all-size arguments, not conclusions from experiments. The supplied Python verifier independently checks the finite Markov recurrence, full small-star event enumeration, and convergence of the explicit formulas in representative numerical regimes.

## Originality — PASS with publication-priority risk

Feldman et al. (2014) already prove consensus on the first hub opinion and high-probability correctness on stars; their Section 3 and Claim 1 are explicitly credited, not repackaged. Bahrani et al. (2019) establish majorities for other tree families, and Mohan–Prałat (2023) treat binomial random graphs. The exact arbitrary-rate finite formula, sharp \(1/m\) error constant and weak-bias crossover do not follow from these qualitative statements and were not identified in inspected relevant source text or mathematical-record searches. The underlying binomial and random-walk identities are classical. An unindexed exact prior derivation remains possible and should be checked by an independent specialist.

## Value — PASS

The exact erroneous-consensus probability is a meaningful measure of reliability of asynchronous social learning. Its sharp constant improves the previously available order bound, the critical window distinguishes reliable from irreducibly noisy consensus as signal quality approaches chance, and monotonicity quantifies the cost of a hub announcing too quickly. The star is a canonical irregular topology and these linked formulas are useful as a benchmark for network learning and message scheduling.

## Limits

Binary independent private signals, initially silent public opinions, a star network, and independent Poisson clocks with identical leaf rates are essential. All limiting claims keep the hub/leaf rate ratio fixed. Neither claims for arbitrary graphs nor publication-level originality certification are asserted.

Self-review: passed. Independent audit: not yet performed.
