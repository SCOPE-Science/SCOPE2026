# Independent audit — 2026-09-30

**Record:** `2026/09/09/048`  
**Audited source tree:** `f5e24ebf8d3e18e0cbc90937d755b9c5a00440de`

## Correctness — PASS

The cohomological argument is internally consistent. The shifted sheaf is lisse at zero while the unshifted quadratic-twisted Kloosterman sheaf has nontrivial tame ramification there, excluding a geometric isomorphism and hence nonzero second compactly supported cohomology. On the punctured affine line with zero and minus h removed, zeroth compactly supported cohomology also vanishes. Grothendieck-Ogg-Shafarevich gives first compactly supported cohomology dimension equal to four plus the Swan conductor at infinity; rank four and input breaks at most one half give Swan conductor at infinity at most two, hence dimension at most six and the stronger bound 6 sqrt(p). A fresh classical computation for every nonzero h at odd primes through 31 stayed below this bound; the package extends that numerical check through 61.

## Originality — PASS

General trace-function literature supplies square-root correlation estimates for bounded-conductor sheaves outside a bounded exceptional set, and the short-sum literature provides the surrounding framework. The inspected sources do not state the exact quadratic-twisted Kl2 translate pair with empty exceptional locus and the explicit constant 6 (or 12). The local ramification mismatch and Swan accounting are therefore the claim-specific content. This is not treated as a new method; originality is limited to the pinned uniform lemma and explicit bad-locus analysis.

The comparison explicitly checked equivalent formulations, broader coverage, exact tables/databases, and whether prior results logically imply the final claim.

## Scientific value — PASS

A uniform off-diagonal correlation lemma with an explicit constant and no bad shifts is a motivated Type-II input for short-sum arguments, and the empty-locus conclusion removes a case split that generic bounded-conductor theorems leave implicit. The record correctly does not claim the unfinished Burgess power saving. The result is a focused structural lemma rather than a numerical curiosity.

## Source inspections

- **Fouvry, Kowalski, Michel, Raju, Rivat, Soundararajan — On short sums of trace functions** — Journal abstract and scope of the short-trace-function framework. Supplies general short-sum context, not this exact translated quadratic-twisted Kl2 constant/bad locus. https://doi.org/10.5802/aif.3087
- **Qin — L-functions of Kloosterman sheaves** — Full-text section describing classical Kloosterman sheaf rank, lissity, tame ramification at zero, wild ramification and Swan conductor one. Confirms the local Kloosterman data used in the proof; does not state the present correlation theorem. https://doi.org/10.1112/plms.70003
- **General bounded-conductor trace-function correlation lemma** — The stated lemma gives square-root correlation outside an O(1) exceptional set for nonexceptional bounded-conductor trace functions. Broader qualitative coverage, but no exact constant 6 and no proof that this additive-shift pair has empty exceptional set. https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/sums-of-kloosterman-sums-over-squarefree-and-smooth-integers/82DDB083DA7D57577FCF157BFABFF84E

## Residual risks

- The explicit 6 sqrt(p) constant is a routine-looking specialization of standard sheaf-cohomology technology, so its conceptual novelty is limited.
- The proof relies on standard Deligne/Katz/Grothendieck-Ogg-Shafarevich inputs rather than re-proving them.
- Numerical checks are finite and serve only as consistency evidence; the all-prime conclusion rests entirely on the sheaf argument.

## Disposition

**PASS.** The final claim passes correctness, originality, and scientific value without changing `RESULT.md` or `SLOGAN.txt`.
