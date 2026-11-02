# Scientific review: explicit Zimin factor automata

## Correctness — PASS
The ruler-position identity is proved by induction. Every factor has exactly one maximum-rank letter, which pins all its occurrences to centers spaced by a power of two. The resulting precise ending-position classes partition the state indices, establish every permitted transition and every forbidden one, and distinguish all reachable states by longest possible completion length. The suffix accepting-state criterion follows from divisibility of the final position. The edge totals are independently counted by label. The standalone checker gives an independent *implementation* of the online automaton and exhaustive finite occurrence sets for the stated ranges. Finite evidence is not used in place of the all-rank proof.

## Originality — PASS, historically qualified
The closest exact prior mathematical implication is the factor-membership criterion of Głowinski and Rytter (2013, Lemma 2). Its interleaving test decides membership but does not identify minimal right-context states, their labelled incidence graph, or their exact per-letter arc counts. Fici's 2009 treatment gives general automaton equivalence classes, state/edge bounds, and formulas; the 2011 general paper treats minimal-size automata and so may account for the easy *state count* as a corollary. The present assessed claim is the explicit canonical graph and edge-label law, not that state count in isolation. The same integer edge-total sequence occurs as the unrelated numerical entry OEIS A132925. Rytter–Shur 2014 addresses pattern embeddings rather than literal factors. No equivalent graph description was located in the searched records or inspected materials. The 2011 paper's complete text could not be inspected, which limits historical priority certainty.

## Value — PASS
Minimal factor automata are a canonical data structure for substring languages. For the exponentially long finite Zimin family, the theorem fully determines each right-context class, every labelled arc, the suffix-accepting states, and the symbol-resolved edge inventory by arithmetic formulas. It thereby supplies a closed, succinct description of a natural automata invariant, rather than an isolated integer sequence or generic algorithm. The new structural description remains useful even though linear-time factor membership was already known.

## Limitations
The statement concerns partial deterministic automata of literal contiguous factors and suffixes of finite Zimin words only. The result does not establish improved generic asymptotic matching speed, results for pattern substitutions, or exhaustive historical novelty. The closest inaccessible general source and the overlap with known state-count theory are explicitly recorded.

Self-review: passed. Independent audit: not yet performed.
