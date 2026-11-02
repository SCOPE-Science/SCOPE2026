# Scientific review: quaternary four-letter one-deletion codes

## Correctness — PASS

The objective is the maximum cardinality of a set of four-letter words with disjoint sets of three-letter deletion descendants. A positive rational weight of total \(25\) has weight at least \(1\) on every possible four-letter deletion set, leaving only four equality patterns. An equality packing of \(25\) would cover all three-letter outputs exactly once, but for each fixed outer symbol it must partition three nonconstant palindromes into pairs supplied by tight `0120` words. This is impossible. The exhibited 24-word family has no repeated deletion output, as checked directly over all 64 possible outputs. All quantifiers and equality boundaries are included in the proof.

## Originality — PASS (best available evidence)

The closest numerical benchmark is Table I(c) of Kulkarni–Kiyavash (arXiv:1211.3128v1), where the same four-symbol, length-four, one-deletion packing has a fractional upper bound of \(25\) and a documented construction of size \(20\), not an exact value. The proof establishes a genuine integral obstruction beyond the fractional certificate. Chee–Ge–Ling (arXiv:1008.1343) concern neighboring deletion regimes; Xie–Sun–Ge (arXiv:2606.15379v1) address covering rather than correcting. No accessible prior checked source supplies the exact value \(24\), but incompleteness of publication indexing remains a priority risk.

## Value — PASS

The result settles a concrete, naturally parameterized finite alphabet/deletion problem: it closes the numerical gap \(20\le A_4(4,1)\le25\) in a published table, improving its recorded construction and identifying a parity-based integrality obstruction at an optimum fractional packing bound. This is substantive beyond a new computational witness.

## Limits

The theorem is specific to four symbols, length four, and exactly one deletion; it makes no claim about general-length codes, decoding complexity, or uniqueness of maximum codes. The checker tests finite arithmetic and a complete 24-word witness, while the universal upper bound is proved mathematically. External independent mathematical validation is not performed.

Self-review: passed. Independent audit: not yet performed.
