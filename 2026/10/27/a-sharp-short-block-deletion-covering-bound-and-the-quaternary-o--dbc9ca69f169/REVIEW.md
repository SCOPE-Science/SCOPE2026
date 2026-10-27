# Scientific review

## Correctness — PASS
The claimed theorem has two exact components. The all-alphabet lower bound follows from the displayed rational target weights, an exhaustive list of all fifteen equality patterns of a four-symbol-position word, and an elementary symbolic count of target pattern multiplicities. The proof does not use a finite-alphabet experiment to justify the universal quantifier. The exact four-symbol optimum is completed by a fully listed 19-word covering; the standalone verifier constructs distinct deletion shadows and checks all 64 target words. All assumptions (alphabet cardinality, word length, exactly one deletion, set rather than multiset descendants) are explicit. The listed checker was executed against the actual accompanying files and ended with `VERIFY_OK`.

## Originality — PASS within examined sources
The closest primary source is Xie–Sun–Ge (arXiv:2606.15379, 2026), which treats the same deletion-covering parameter but proves elementary/asymptotic bounds rather than the finite quaternary optimum or the present equality-pattern lower bound. Lenz–Rashtchian–Siegel–Yaakobi (arXiv:1911.09944) develops a general different fractional lower bound. Its Theorem 3 does not imply the present value at the stated parameters. Two nearby public exact results were read in full: a ternary length-five covering result and an odd-alphabet length-three covering result. Neither addresses nor implies the quaternary length-four statement. Published search and corresponding research records revealed no dominating theorem. An unindexed equivalent exact computation remains a priority risk; the conclusion is not a proof of global priority.

## Value — PASS
The paper explicitly identifies the difficulty of nonbinary single-deletion covering codes. The result improves the elementary finite bound for the first natural four-symbol length-four instance from 16 to 19 and closes it by an explicit code, while its rational-packing inequality holds for every alphabet size. An exact short-block extremal invariant plus a parameter-uniform structural bound is more than a normalization check or a routine recomputation from known tables. Its scope is deliberately bounded: no general exact formula for every alphabet, no longer blocklength result, and no uniqueness theorem are claimed.

Self-review: passed. Independent audit: not yet performed.
