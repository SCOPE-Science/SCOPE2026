# Independent mathematical audit

## correctness

PASS

PASS — Exhaustively re-enumerated all (n!)^(2n) strict labeled preference profiles for n=2 and 3, all n! possible matchings for each, explicit blocking pairs, zero-based individual rank products P=∏(n−r) and regret R=max r. Independent code reproduced n2 equality=16, n3 optimizer-set equality=39672, strict Nash-optimizer inclusion in regret-set=6984 and exactly 3504 cross-regret stable-outcome comparisons with strict inverse Nash ordering. Independently checked all 24 matchings for the supplied n=4 preferences: exactly three stable vectors with (R,P)=(2,4608),(3,5184),(3,3456), yielding unique incompatible optima. For n≥5 each new pair is mutual top choice, so it must be matched in every stable outcome, old rank increases by k, old n−r utility remains 4−r, all new utilities n, and old maximum rank shifts by k: this analytic argument (not finite padding trials) preserves the separation for all n. All claims require balanced strict complete profiles, no ties.

## originality

PASS

PASS, qualified — Nash-optimal stable matching under rank-induced utilities and minimum-regret stable matching are classical as separate objectives; Desai–Rasheed–Ghalme–Gujar 2026 applies Nash welfare to this exact model. A full published Resultary primary finding for *egalitarian vs minimum-regret* establishes related n3 nested optimizer sets, but does not entail the different nonadditive Nash-vs-regret inclusion. The present exact n3 46,656-profile census and n4 sharp counterexample were not identified in checked published records. The inaccessible full Desai et al. article is a significant priority risk; abstract does not justify a whole-document noncoverage claim.

## value

PASS

PASS — Sharp compatibility threshold for two independently motivated stability/fairness objectives, complete small-market optimum-set census and explicit infinite-size separation. This is a natural boundary rather than arbitrary enumeration: it distinguishes when welfare optimization automatically satisfies a max-regret fairness guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
