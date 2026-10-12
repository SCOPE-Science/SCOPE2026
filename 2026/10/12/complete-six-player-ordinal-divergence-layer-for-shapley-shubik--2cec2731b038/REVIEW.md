# Self-review

## Correctness
**PASS.** The verifier exhausts every nontrivial monotone Boolean game through six players by enumerating minimal-winning antichains. The totals agree with \(M(n)-2\) through \(n=6\). Both indices are evaluated with exact integer arithmetic, and every mismatching pair is classified. Properness is checked in two equivalent ways. The displayed witness is independently replayed down to its swing-size spectrum.

Risk: the theorem is finite and makes no claim for seven or more players.

## Originality
**PASS.** Tomiyama's 1987 result already establishes that Shapley–Shubik and Banzhaf–Coleman need not be ordinally equivalent from six players onward, so that threshold is explicitly excluded from the novelty claim. Later work characterizes large classes where ordinal equivalence holds. Exact-number, alias, implication, and table searches did not locate the complete six-player census, the universal no-reversal/refinement property, the dummy-free layer, or the proper subcount.

Risk: the full 1987 article could not be retrieved. Available abstract-level material states qualitative six-or-more inequivalence but not the exact census; an unindexed historical table remains possible.

## Value
**PASS.** Ordinal equivalence between Shapley–Shubik and Banzhaf is a longstanding structural question in voting power. Once six players are known to be the first size where equivalence can fail, the complete first layer is a natural invariant. The strongest feature is structural rather than merely enumerative: every first disagreement is a tie refinement in the same direction, never a reversal, and it persists widely inside proper dummy-free games.

Self-review: passed. Independent audit: not yet performed.
