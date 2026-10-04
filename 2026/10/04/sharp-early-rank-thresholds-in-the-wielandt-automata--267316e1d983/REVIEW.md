# Same-model review

## Correctness
PASS. The proof isolates the only rank-reducing letter, proves the separator lower bound, shows equality forces the unique word \(c(bc)^{s-1}\), and verifies its effectiveness by an explicit recurrence for missing states. The parity split at \(s_0=\lceil n/2\rceil\) proves the sharp failure of equality at the next deficiency. A finite power-automaton replay through \(n=14\) corroborates the symbolic proof without replacing it.

## Originality
PASS. The closest classical source proves the reset threshold of \(W_n\), a later two-cycle paper generalizes reset thresholds, and a 2019 full-text paper on minimum-rank words explicitly discusses \(W_n\) only as an endpoint/reset ingredient in constructions. Targeted searches for intermediate rank, compression, image-size, and equivalent wording did not find the stated profile, uniqueness, or half-range boundary. Residual risk remains because the observation is elementary and may exist under older or unindexed terminology.

## Value
PASS. The exact profile answers a natural structural question for a canonical slowly synchronizing family and separates early linear compression from the later quadratic reset bottleneck. The result covers an infinite parameter range, identifies the unique extremal words, and locates the first failure of the counting bound.

## Closest literature and limitations
The closest inspected works are Ananichev--Gusev--Volkov (2010), Gusev--Pribavkina (2014), and Kari--Ryzhikov--Varonka (2019). Their published results concern reset thresholds, generalized Wielandt-type reset behavior, or shortest words of minimum rank in other/derived automata. No inspected source states the same intermediate-rank theorem. An older equivalent statement under different terminology remains a residual bibliographic risk.

Same-model review: passed. Independent audit: not yet performed.
