# Scientific review

## Correctness

**PASS.** The theorem has an exact, closed domain: binary necklaces of positive length with no cyclic `11`, observing all cyclic length-four read multiplicities. Four-gram identities are derived locally from unique positive zero-gap necklaces, including imprimitive necklaces and lengths smaller than four. The totient formulas count orbits, not indexed rotations; the multinomial/stars-and-bars fixed-point calculation is exact. The singleton cases use distinct type-block cyclic orders and distinct multisets of excess lengths. Every generating-function summand corresponds to a disjoint feasible case. The stand-alone verification independently reproduces literal spectra and fibers at lengths 1 through 20; universal claims rest on the proof, not those examples.

## Originality

**PASS, with residual risk.** Kiah--Puleo--Milenkovic [1] prove general quasi-polynomial profile counting for restricted de Bruijn graphs, not this exact multiplicity-fiber and singleton classification. Chee and collaborators [2] count allowable necklaces and maximal-window-unique run-length-limited sequences, and [3] study de Bruijn codes constraining repeated-window separation. These results do not determine the ambiguity of unconstrained repeated four-gram counts within the specified cyclic forbidden-`11` language. A prior exact formula may exist under Markov-type terminology despite the searches and section-level full-text comparisons performed; that risk is not independent novelty certification.

## Mathematical value

**PASS.** Complete observation fibers, not merely a count of words, determine exact zero-error message capacity and all naturally uniquely decodable sources for a constrained assembly channel. The structural gap classification yields an onset theorem at length nine and separates the cubic number of available profiles from the merely linear number of uniquely reconstructible profiles, with exact periods twelve and six and asymptotic singleton fraction \(120/n^2+O(n^{-3})\). The contrast is not implied by the general dimension estimate for restricted flow polytopes.

## Limitations and nearest literature

The setting excludes cyclic adjacent `11`, uses oriented reads with multiplicity and is noiseless. It does not address reads with erasures, reverse-complement collapsing, the unconstrained binary channel or independent audit. References [1]--[3] are detailed in RESULT.md; the closest general coverage is [1], whereas [2] is the most directly relevant later literature on constrained cyclic sequences. The 2021 necklace-transition counting work is a methodological comparator, not proof of the exact read-fiber statement.

Self-review: passed. Independent audit: not yet performed.
