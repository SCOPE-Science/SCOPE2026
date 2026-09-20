# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The path proof reduces successful partial 3-assignments to proper 3-colourings together with independent sets of degree-two vertices whose two neighbours receive distinct colours. Encoding successive colour differences by signs in `Z_3` turns eligibility into equality of consecutive signs and yields the stated second-order recurrence. The cycle proof additionally enforces colour closure by a cubic root-of-unity filter; the displayed four-state transfer matrix has the stated characteristic polynomial, and its traces at `1`, `omega`, and `omega^2` give the two recurrences. Boundary cases were checked separately.

The all-lambda maximum-degree-two statement follows from disjoint-union multiplicativity, bipartite propagation for two colours, and the impossibility of forcing an initially uncoloured vertex when `lambda >= 4`. The minimum-domain formulae follow from sharp independent-set bounds on paths and cycles plus compatible 3-colourings.

A definition-level verifier exhaustively enumerates partial assignments for `P_n` through `n=8` and `C_n` through `n=8`, reconstructs the polynomials, and matches the recurrences exactly. It also checks the chromatic specialization and the isolated-vertex extension of the two-colour formula. These computations are supporting evidence, not a substitute for the proof.

## Originality

The originality assessment is **to the best of our knowledge**. Farr's arXiv:2609.17108v1 was inspected, including its definitions, basic examples, two-colour theorem, complexity theorem, and future-work discussion. Farr--Morgan arXiv:2406.15746 was inspected in the part introducing the forced-colouring polynomial and its basic examples. Searches using British and American spelling, `forced 3-colouring polynomial`, `forced colouring function`, `path`, `cycle`, and `maximum degree 2` found no path/cycle family recurrences or maximum-degree-two classification.

The 2025 Springer chapter `10.1007/978-3-031-86319-6_18`, corresponding to the Farr--Morgan preprint, was identified but was not separately checked line-by-line. The open preprint contains the relevant forced-colouring section and no family result was found there. A change introduced only in the final chapter could therefore affect originality. Because the invariant itself is recent, unindexed parallel work is also a residual risk.

The correction `FC_3(P_3;p)=6p^2(1-p)` is not claimed as original: it already appears correctly in the earlier Farr--Morgan work. The novelty claim concerns the general recurrences and maximum-degree-two classification. The extension of the two-colour product formula across isolated vertices is a consistency correction rather than the principal contribution.

## Value

The result gives a complete tractable boundary class for an invariant whose fixed-parameter evaluation is generally #P-hard for every `lambda >= 3`. It converts the first nontrivial colour case into short linear recurrences, completely evaluates all maximum-degree-two graphs by component factorization, and identifies exact minimum forcing-domain sizes. It also exposes two concrete consistency issues in the latest v1 formulas.

## Limitations

The theorem does not address maximum degree at least three. The originality search cannot exclude unindexed work or additions made only in the final 2025 Springer chapter. Independent audit has not been performed.
