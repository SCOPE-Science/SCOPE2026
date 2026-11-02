# Scientific review: clockwise scans with uniform relocation

## Correctness

**PASS.** The fixed-relocation-pattern count is reconstructed from a bijection between disjoint labeled circular arcs and clockwise label permutations with nonnegative gap compositions. It gives exactly \(k!\binom{n-t-1+k}{k}\) valid uniform relocation tuples. Averaging over the binomial relocation count proves the exact finite formula. The strict stochastic ordering and both asymptotic limits are supported by explicit ratio and Taylor estimates. Independent exact-fraction finite-state enumerations and direct path checks agree with the law for cycles of sizes 2–7, but are not substituted for the infinite proof.

## Originality

**PASS, with historical-priority risk.** The closest inspected complete texts study either resets to a fixed site and first-passage/escape laws (Villarroel–Montero–Vega 2021 and Riascos et al. 2019) or a general birthday-based Markov-chain sampling algorithm (Benjamini–Morris 2007). None states or directly implies the exact first-repeat distribution under independent uniform relocation, nor the sharp capped-to-Rayleigh transition with an endpoint atom. A classical circular-arc packing calculation supplies a proof ingredient and is not claimed as new. The older Siegel–Holst report was accessible at abstract/metadata level, not in full; a corresponding earlier regenerative-scan treatment remains possible.

## Value

**PASS.** The same finite Markov model interpolates between a deterministic complete lap and independent uniform samples, and the theorem locates their sharp collision-scale boundary. The limit identifies an atom that is missed by ordinary birthday approximations; its exact finite distribution and strict monotonicity provide benchmark probabilities for correlated finite-state sampling and exploration.

## Independent validation and scope

The calculation is specific to uniform, state-independent relocations and deterministic clockwise motion. The many-relocation theorem concerns weak convergence rather than an error bound.

Self-review: passed. Independent audit: not yet performed.
