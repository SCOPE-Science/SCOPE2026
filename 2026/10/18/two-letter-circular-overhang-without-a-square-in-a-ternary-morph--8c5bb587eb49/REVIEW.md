# Scientific review

## Correctness — PASS

The proof supplies twelve explicit base occurrences inside a known fixed-point prefix, then an all-length lifting lemma. Its only potentially delicate inequality is \(|h(u_i)|+|h(u_{i+1})|\ge s+2\): cyclic absence of \(22\) yields a total length of at least three, while the offset is at most one. The proof independently establishes forbidden bigrams and uses the genuine suffix-code property of \(\{01,21,0\}\) to reverse-decode any alleged square. Induction and strict length growth finish the quantified result. The standalone finite checker passed; the theorem does not depend on extrapolation.

## Originality — PASS, with residual risk

Currie et al. (arXiv:2206.01776v1, especially the introduction and forbidden-factor Theorem 14) analyze this exact fixed point but the inspected sections do not establish occurrence of **every** two-letter circular overhang of both substitution towers. Bell and Shallit (arXiv:2102.03821v1, especially their examples) introduce Lie complexity and treat other morphic sequences; their general bound and examples do not imply the simultaneous overhang property for this fixed point. De Luca and Fici treat Sturmian, not ternary non-Sturmian, words. The different binary period-doubling calculation available in published records is not a specialization. Additional unindexed results on cyclic factors remain a plausible residual originality risk.

## Mathematical value — PASS

The same natural substitution that generates a well-studied low-complexity ternary word generates two infinite towers of periods whose cyclic phases remain realizable with **two letters of periodic overhang**, yet whose prescribed squares are all forbidden. This is a structural, infinite-family assertion about a natural word, not a finite census, routine parameter increment, or general claim that Lie complexity may coexist with square avoidance. It supplies constructive Lie-complexity witnesses at unbounded lengths and isolates a stronger local/global repetition separation. No full Lie-complexity classification or originality certification is claimed.

## Sources and limits

The principal primary sources are Currie et al. (2022), Bell and Shallit (2021), De Luca and Fici (2022), and Cassaigne et al. (2014). Explicit seed positions and a Python checker are provided; full classification of Lie-complexity support remains open here, and comparable unindexed work could exist.

Self-review: passed. Independent audit: not yet performed.
