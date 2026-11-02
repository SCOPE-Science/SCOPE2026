# Scientific review

## Correctness — PASS

The claim is for the standard binary Rudin–Shapiro word and for one tortoise operation. The proof explicitly covers complete finite-factor generation from the eight allowed adjacent pairs of the four-letter uniform morphism; the full eight length-five left-special list with preceding contexts exactly `ac` and `db`; injection of binary coding on length-eight four-letter factors; the recurrence-based count \(p(m+1)-p(m)=8\); exact exhaustive classification of all eight length-12 collision doubletons; and a prefix-inheritance argument that excludes all other collisions at longer lengths. Berthé's published \(p(n)=8n-8\) input is valid for all relevant lengths. The included standard-library checker was executed successfully with all assertions; no finite experiment was extrapolated to infinity.

## Originality — PASS (best-knowledge; residual priority risk)

The closest inspected primary text, Campbell–Rampersad (arXiv:2604.25811v2), defines tortoise complexity and proves only a bounded loss for general linear-complexity binary words, while its worked examples are paperfolding and Thue–Morse. An exact deficit eight after length twelve for Rudin–Shapiro is not a direct consequence. Berthé's historical Theorem 4 computes ordinary complexity, not tortoise complexity. Searches of the available mathematical-result index using both the precise claim and the relevant synonyms and automatic-word names returned other coding and automata topics, no matching statement. A known period-doubling tortoise calculation concerns a different automatic word and does not imply this case. A previously unindexed derivation cannot be excluded by these searches alone.

## Value — PASS

The newly introduced invariant is natural for fixed-point automatic words. The result gives a complete infinite-length exact formula with a sharp initial cutoff, contrasting the existing examples where collisions eventually disappear or the deficit has different behavior. It sharpens a general bounded-deficit theorem into an explicit permanent obstruction and supplies an elementary reusable bridge from local extension-context rigidity to an infinite orbit-count formula.

## Restrictions and residual risks

Binary standard Rudin–Shapiro only; one tortoise operation; no higher-iterate formula or full priority guarantee. The finite checker is reproducible, not independently audited mathematics. Sources are credited for every external premise.

Self-review: passed. Independent audit: not yet performed.
