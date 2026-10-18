# Scientific review: four-block order rigidity

## Correctness — PASS

The theorem is universal over all nonnegative integer sequences and all \(24\) permutations. For each nonidentity permutation, the complete two-block hypotheses give five exact window equalities and fifteen valid ordering/nonnegativity inequalities. The attached rational certificates reconstruct the sum of the first block as a nonnegative combination of those inequalities modulo the exact equalities. The verifier checked the coefficient identity for every case using exact rational arithmetic, not a floating-point feasibility result. Nonnegativity then forces a zero first block, and the sliding-window condition propagates zero forever. The identity pattern has an independent elementary equivalence to a monotone Padovan recurrence with precisely stated initial inequalities. A direct construction check passed for \(50\) initial triples.

## Originality — PASS within inspected evidence

The closest primary source is Nacin's 2022-publicly-released Journal of Integer Sequences article, 23.1.2. Its actual PDF was read through the conclusion and references: Proposition 3 gives the monotone branch, and the three-block rank cases are addressed by Propositions 5–7. The concluding scope is explicitly permutations of degree three or less. The complete degree-four rigidity result, for all \(23\) nonidentity permutations with weak ties, is not stated or logically supplied by those conclusions. The OEIS A000931 record reports the underlying property, not this permutation classification. Actual specialized bibliographic and mathematical-result-index searches found no covering item. An equivalent theorem using different rank-order terminology may be absent from these sources; the search is not a proof of global originality.

## Mathematical value — PASS

The first unresolved rank-pattern block length after the published size-three classification displays a qualitatively sharp change: the size-three Fibonacci-type nonmonotone families disappear at size four. The theorem completely classifies a natural infinite-sequence class rather than giving a finite numerical table or an isolated example. A two-block rational certificate reduces the infinite conclusion to a finite exhaustive structural test and provides a reusable exact method for nearby local-order recurrence problems.

## Limitations and closest prior coverage

The result does not address varying patterns, non-ordered blocks, or block sizes five and above. The already-known identity-pattern branch is explicitly credited to earlier Padovan recurrence work, not advanced as a separately novel contribution. Independent verification has not been performed, and the originality assessment is limited to accessible inspected literature and searched records.

Self-review: passed. Independent audit: not yet performed.
