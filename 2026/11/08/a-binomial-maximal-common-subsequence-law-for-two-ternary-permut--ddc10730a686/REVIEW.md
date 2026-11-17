# Independent mathematical audit

## correctness

PASS

For X=(012)^r,Y=(021)^s, r,s positive, the greedy embedding criterion is exactly the pair of weak-descent budgets r−1 and s−1. A proper common word with slack in a budget can be extended by inserting an unused position of the other input; zero-cost insertions rule out equal neighboring symbols and force endpoints 0 and nonzero. The complete four strict-transition costs imply |w|=r+s at double saturation; the transfer series (2+x+y)/(1−xy(3+x+y)) yields the binomial recurrence and count. When r>2s or s>2r the whole shorter word embeds in the longer, giving unique MCS; cases at equality are included. Independent exhaustive distinct-subsequence enumeration for every 1≤r,s≤4 confirms exact MCS sets, all-maximal-is-longest, and count. Repository verify.py actual source read: tests through r,s≤5, lengths through 30, and recurrence through 40. Universal result rests on proof, not finite enumeration.

## originality

PASS

Known algorithms for general MCSs count/represent arbitrary inputs but do not state closed expression and all-optimizer structure for these two unequal ternary permutation powers. A same-day adjacent-swap result gives the equal-power central binomial count for q≥4, expressly mentions the known ternary equal-power case, but requires equal repetition counts; it does not cover the unequal-parameter phase boundary or uniqueness regime. This audit accepts the full two-parameter claim best-of-knowledge, with equal-power part acknowledged as known.

## value

PASS

Exact number and full structure of inclusion-maximal common subsequences for a natural pair of periodic ternary words; identifies a nontrivial exponential-to-singleton change at factor-two repetition ratio. This gives an exact benchmark not supplied by general MCS enumeration and is not merely renaming or a tiny isolated enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
