# Mathematical review

## Correctness — PASS

The argument forces exactly \(a\) zeros and \(c\) ones in the first \(a+c\) positions by excluding both smaller and larger zero counts using the two source-word transition constraints. Conversely an explicit assignment of each phase's symbols to their source runs proves the entire fixed-composition concatenation identity. Distinct Myhill–Nerode quotients are separated by the number of zeros required in the remainder of a particular fixed-length phase; distinct prefix lengths have distinct accepted residual lengths. This yields the exact two-rectangle quotient count, with one shared boundary and one dead state. Every positive-parameter boundary, including unit run lengths, is covered. Independent finite checks of 256 language-and-quotient instances and 4096 grid-NFA DFA minimizations agree with the theorem. They support but do not replace the all-parameter proof.

## Originality — PASS, with residual risk

The closest full-length primary treatment is Biegler–Daley–McQuillan (2009), which treats general two-word shuffles and bounds for shared-periodic operands. Its assumptions and conclusions do not entail this arbitrary four-parameter, opposite-run, exact-quotient theorem. Brzozowski–Davies–Madan (2018) concerns pattern-matching ideals rather than the shuffle of two fixed words. Eremondi–Ibarra–McQuillan studies decision problems, not the precise quotient count. The withdrawn 2022 self-shuffle preprint concerns identical, rather than complementary-ordered, operands; only its abstract was available. Semantic records and targeted web searches did not reveal an equivalent statement, but this is not a proof of absolute novelty. Unindexed or inaccessible special cases remain a residual risk.

## Mathematical value — PASS

State complexity of finite-word shuffle can be exponentially large, even though its naive nondeterministic grid is quadratic. The theorem identifies an exact nontrivial structural regime in which all interleavings collapse into two independent composition phases and gives a sharp count for every four-tuple, plus the entire depth profile and language cardinality. This complete natural family is informative for deterministic recognition and interleaving models, not a finite list or a generic state-count bound.

## Scientific limits

The claim is restricted to opposite-order two-run binary operands with all run lengths positive; different run orders and larger alphabets are not classified. Interleaving multiplicities are deliberately ignored. Global priority remains unverified, and the withdrawn self-shuffle manuscript was not fully inspectable.

Self-review: passed. Independent audit: not yet performed.
