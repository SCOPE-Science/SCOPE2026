# Review of the binary four-mer greedy-superstring theorem

## Correctness — PASS

The proof reduces every live greedy string to its first and last original four-letter word; disjointness of the original groups excludes overlaps of four or more. The exact greedy recurrence takes every maximum-overlap tie and includes zero-overlap continuations; its memoization key is a canonical multiset of endpoint pairs. The optimum is determined independently by an exact subset/last-word dynamic program. Integer cross-products over all 65,535 input sets yield a sharp maximum of \(17/11\), with exactly four maximizing masks. An eight-word witness separately has optimum 11 and a fully legal greedy outcome of length 17. Replaying the included exhaustive checker and the separate witness checker confirms both calculations.

## Originality — PASS within inspected evidence

The August 2026 fixed-length greedy-superstring paper determines the unrestricted-alphabet length-three ratio \(9/5\) and provides lower bounds for lengths six and greater, not the complete binary four-mer case. Shibata's September 2026 constructions begin at length ten and use a growing alphabet. The September 2026 study of small string lengths proves unrestricted-alphabet four-mer lower bounds greater than \(15/8\), and explicitly describes the exact unrestricted ratio as unresolved; it does not provide a full two-symbol, four-mer classification. The previously recorded exact **binary three-mer** calculation has only 255 input sets and does not imply the present result. Actual literature and semantic research-index searches found no equivalent \(17/11\) theorem or four-extremizer classification. This search does not establish global priority; equivalent unindexed calculations remain possible.

## Value — PASS

The binary four-mer universe is the first sixteen-edge de Bruijn instance beyond the eight-edge length-three case and comprises 65,535 distinct inputs; arbitrary greedy tie-breaking is essential. This is a natural complete finite-alphabet classification of an approximation algorithm's worst case, not an arbitrary sampled slice. The exact constant and complete four-set symmetry orbit quantitatively separate fixed-binary behavior from published unrestricted-alphabet four-mer lower bounds. They also provide finite benchmark instances for understanding failure modes of maximum-overlap merging. The result does not claim a general asymptotic algorithmic guarantee.

## Scope and residual risks

The main upper-bound certificate is exhaustive finite computation rather than a closed-form inequality uniformly in length or alphabet size. The two checkers are independent implementations of different aspects (global recurrence versus literal witness); their agreement is not independent scientific validation. An unknown prior exact two-symbol classification would affect originality. No correctness claim is made beyond the stated finite domain.

Self-review: passed. Independent audit: not yet performed.
