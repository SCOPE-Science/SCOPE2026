# Scientific review of the small-field truncated-polynomial envelope theorem

## Correctness
**PASS.** The embedding-versus-bilinear-factorization equivalence is proved directly using natural-basis squares and projection to an evolution envelope; it does not require polarization, so it remains valid in characteristic two. The explicit eight-row decompositions are checked coefficientwise in the complete ten-coordinate symmetric bilinear matrix space and exhaustively against all products over each finite field. For the lower bound, all projective linear forms are enumerated, and a necessary quotient-rank constraint provably prunes only subsets incapable of containing the four target matrices. Every surviving seven-element subset fails containment. Code and exact integer modular arithmetic are included.

## Originality
**PASS, with residual risk.** The closest directly motivating primary source, Costoya–Fernández Ouaridi–Viruel (arXiv:2609.32784v1), establishes the general envelope theory but derives the truncated-polynomial formula seven only for odd-characteristic fields with at least seven elements. Its Remark 5.4 states that the four-dimensional \(\mathbb F_3\) example requires more than seven summands, without computing the exact answer. The present upper certificate makes the exact number eight, and the characteristic-two result uses the full multiplication tensor instead of squaring. Bläser's general bilinear-rank setting does not alone yield an exact symmetric rank-eight certificate. Source-abstract-only and unindexed-coverage risks remain; no independent literature audit has occurred.

## Mathematical value
**PASS.** The claim resolves a concrete small-field rank gap highlighted by the motivating article and establishes the exact dimension of its first four-dimensional finite-field exception, rather than another lower bound or heuristic example. The companion binary case shows how to recover the embedding invariant when the squaring-map Waring approach loses all mixed terms. The exact arithmetic certificates are small and reusable as calibration instances for field-dependent evolution-envelope constructions.

## Scope and limitations
The result is restricted to the fourth truncated polynomial algebra over \(\mathbb F_2\) and \(\mathbb F_3\). It does not assert a formula for higher degrees, other fields, uniqueness of minimal envelopes, or unrestricted bilinear multiplication rank. The first relevant public source is dated 2026-09-26. Closest literature: arXiv:2609.32784v1, §3–§5; Bläser, SIAM J. Comput. 34 (2005), DOI:10.1137/S0097539703438277.

Self-review: passed. Independent audit: not yet performed.
