# Scientific review

## Correctness

PASS. The row/column count \(a_i+b_j\) gives the exact locations eligible for zero labels. All remaining positive vertices except the uncovered-row/uncovered-column rectangle have a positive neighbor by construction. The only support exceptions are a singleton defender (requiring an additional one) and a near-spanning bipartite matching with exactly one unmatched row and column (also requiring an additional one). The strict lower-bound analysis proves the minimum profile including the exceptional \(2\)-by-\(2\) board. Independent direct-definition brute force reproduced the complete coefficients on six small rectangles; these are checks, not substitutes for the proof.

## Originality

PASS, with nonzero residual bibliographic risk. The 2023 introduction of total perfect Roman domination does not present a complete rook-graph enumerator; the 2022 Cartesian-product paper treats the weaker perfect Roman rule on paths and cycles; the 2018 regular-graph paper addresses parameter bounds. A previously established rook-graph result already covers the perfect Roman minimum \(2p\) and much of its minimum placement structure, so neither its scalar equality nor routine specialization is claimed novel. The new contribution is the complete total-perfect weighted enumeration together with the classification of the two exactly characterized totality obstructions for every defender support. Searches and the remaining limitations are detailed in `AUDIT.json`.

## Value

PASS. The totality requirement makes the Roman constraint nonlocal at isolated positive vertices. Resolving it for every possible defender pattern changes a ternary counting problem to a binary-support polynomial with a sharply delimited correction. This determines the entire distribution of valid functions, including every nonminimal weight, on a canonical two-parameter family of highly symmetric graphs. This is substantially more informative than another isolated numerical minimum.

## Limitations

The support sum is generally exponential; it is not a fast counting algorithm for arbitrary board sizes. The numerical minimum is already implied by the preceding weaker-parameter result. Undiscovered equivalent literature remains possible. Independent validation is not available.

Self-review: passed. Independent audit: not yet performed.
