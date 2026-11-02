# Scientific assessment

## Correctness — PASS

The prefix/suffix length-one argument reduces every binary non-overlapping code to a single orientation, up to complementation. An exact compatibility-graph reduction then equates the optimum to a maximum clique. The supplied coloring bound is a correct upper bound at every recursive branch, so complete traversal proves all 55 upper bounds. Explicit codebooks establish the lower bounds. The standard-library verifier and the independent C++17 implementation both regenerated the full 55-pair table. Finite checks are only asserted for their declared finite parameter range.

## Originality — PASS (qualified)

Chee et al. (arXiv:1209.0236) already determine the unqualified non-overlapping maximum for the small lengths, including 44 at length 11; those values are explicitly excluded from the new claim. The same paper gives a 42-word Dyck construction at length 11, which is compatible with minimum distance two, but not the matching upper bound. Blackburn (arXiv:1303.1026) proves unconstrained bounds. Yazdi–Kiah–Milenkovic (arXiv:1601.08176) and Levy–Yaakobi (arXiv:1804.05371) address error-correcting mutually uncorrelated constructions; Section 6 of the latter gives broad upper bounds but no exact short-length distance frontier. The closest same-object results therefore do not imply the table. Risk remains from specialized or unindexed exact tables, and historical priority has not received independent validation.

## Value — PASS

This closes the complete short-block substitution-distance tradeoff for a standard self-synchronizing code model. It identifies the first distance-two penalty at length 10 and the sharp one-substitution-correcting capacity of 14 at length 11, separating those values from the already-known unconstrained optimum of 44. These finite benchmarks are motivated by simultaneous framing and within-frame error correction, not by arbitrary constraints introduced for easier enumeration.

## Limits

Only binary codes, ordinary exact overlap avoidance, lengths 2–11, and pairwise aligned Hamming distances 2–11 are certified. No claim is made about robust frame recovery after corrupted delimiters, other lengths, or an independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
