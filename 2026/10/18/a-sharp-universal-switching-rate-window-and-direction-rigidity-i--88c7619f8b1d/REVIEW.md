# Self-review

## Correctness — PASS
The six-state generator is irreducible and its environmental occupancies are exactly one half each. Eliminating OFF occupation leaves a three-by-three invertible ON resolvent. The explicit Vandermonde flux factorization is verified by a symbolic identity and direct exact-rational six-state stationary comparisons. The strict positivity decompositions for the three denominator coefficients, the derivative factorization, and both sharp limiting weight families give an analytical proof for all strictly positive weights and rates. The included verification program passed one symbolic resolvent factorization, 60 independent rational generator comparisons, and optimizer identity and boundary checks. Numerical examples are corroboration, not the proof.

## Originality — PASS in accessible sources
The same six-state ON/OFF microscopic model is **not new**: Roldán and Parrondo (2010) specify its rates, compute dissipation and characterize current behavior qualitatively, including small-potential and fast-switching limits. The inspected complete paper does not state the all-positive-weight Vandermonde law, universal optimal switching interval, or its sharp endpoints. Seifner et al. (2023) reproduce its microscopic rates and stationary numerical data without claiming current optimization. Lee et al. (2003) concerns a discrete-time three-state model, not this continuous-time six-state switching mechanism. A general previous record on switching two reversible Markov chains bounds reversal counts but admits reversals in some three-site examples; it does not imply no reversal for this detailed-balance-rate subclass or the exact optimizer. Broader 2018 work on sawtooth-potential ratchets could not be examined in full text; novelty remains provisional pending independent literature review.

## Mathematical value — PASS
The on/off flashing ratchet is a standard finite model of driven transport, and selecting switching frequency to maximize transport is its natural design question. An exact sign rigidity theorem rules out current reversals for every positive three-height arrangement in the stated class, while a universal, sharp interval for the unique maximizing switching rate is unexpectedly independent of the potential contrast. This is a global structural solution rather than a single parameter substitution or isolated numerical optimum.

## Limits and relevant prior literature
The conclusion applies only to homogeneous OFF hopping, symmetric location-independent flashing, three sites, and rate ratios \(w_j/w_i\). No general longer-ring or arbitrary-generator theorem follows. Full-text historical exclusion is not claimed; comparison with a plausible 2018 switched sawtooth model remains incomplete because access was unavailable. All provenance and mathematical independence claims remain for separate external assessment.

Self-review: passed. Independent audit: not yet performed.
