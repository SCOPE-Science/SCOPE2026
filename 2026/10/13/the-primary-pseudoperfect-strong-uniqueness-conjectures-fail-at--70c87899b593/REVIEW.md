# Review

## Correctness
**PASS.** The factorization and reciprocal identity are exact. The strong-pseudoperfect witness consists of eight complementary divisor pairs, every listed number divides \(47058\), complement closure is exact, and the sum is \(94116=2\cdot47058\). `verify.py` replays these checks with integer arithmetic and deterministic trial-division primality tests.

## Originality
**PASS.** The 2023 focal paper states the contradicted assertions as Conjectures 46 and 47. OEIS A054377 records \(47058\) only as primary pseudoperfect. The current A334405 b-file does not list it. A 2026 full paper devoted to strongly pseudoperfect numbers was inspected and contains neither `47058` nor `primary pseudoperfect`. Targeted semantic searches returned as the closest result only an \(\Omega(n)\le3\) classification, which cannot decide this five-prime squarefree example. MathDB currently still marks the exact conjecture open. Residual risk is limited to unindexed or unpublished independent observations.

## Value
**PASS.** A direct explicit counterexample settles two named uniqueness conjectures negatively. The object is a standard primary pseudoperfect number, and the new ingredient is a compact, hand-checkable strongly pseudoperfect representation.

## Closest literature and limitations
The closest direct literature is McCormack--Zelinsky arXiv:2312.11661 and Wang--Zelinsky arXiv:2609.36068. The result does not classify all simultaneous primary and strongly pseudoperfect numbers or address infinitude.

Self-review: passed. Independent audit: not yet performed.
