# Scientific review

## Correctness — PASS

The claim has three separate logical components: a new binary high-target witness, inherited unary low-target witnesses, and the zero-case boundary. For the high range, the actions induced on the second witness are \((\sigma,1)\) and \((\tau,0)\). Since the permutation component of \(ab\) has order \(k-1\), the powers \(a^k\) and \((ab)^{k-1}\) yield pure counter increments \(k\) and \(k-1\). Their greatest common divisor is one, proving generation of the entire direct product for **every** counter modulus. Independent minimality and quotient-final-set arguments establish exactly the prescribed accepting-state counts. The low range and unary obstruction are established by Rauch–Holzer [1]. A standalone exhaustive checker verifies 60 parameter triples; the infinite proof does not depend on extrapolation.

## Originality — PASS within examined literature

German's full 2026 right-quotient paper [2] achieves the full spectrum on an unrestricted alphabet and explicitly uses three letters for its high-range witness. The new theorem certifies the **minimal nonunary alphabet size two** by a distinct coupled-cycle construction. The point-stabilizer final-set mechanism and the unrestricted spectrum are prior work, not claimed as new. Rauch–Holzer [1] proves the unary spectrum, and German's later reversal work [3] treats another operation. Searches targeting binary quotients, group languages, and the construction did not disclose an equal or stronger binary-alphabet statement. The remaining scientific risk is a differently formulated or unindexed two-letter witness.

## Value — PASS

The result settles a natural optimal-alphabet refinement of a recently solved full-spectrum problem: it shows that the transition from the bounded unary spectrum to the full positive spectrum occurs **immediately at alphabet size two**, rather than requiring three letters. The coprime-cycle construction is explicit, uniform in every parameter, and structurally explains why one of the three generators can be eliminated. This is materially stronger than a routine finite example or an unmotivated parameter slice.

## Literature and limits

Closest source: [2], Sections 2–3 and Appendix 0.A, whose three-letter witness separates the symmetric-group and counter generators. Source [1], Section 3.7, establishes the bounded unary range and quotient operation. The proof does not optimize state counts and carries a residual risk of unlocated equivalent binary witnesses; no independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.

[1] Rauch–Holzer (2022), arXiv:2208.14731. [2] German (2026-05-11), arXiv:2605.10852v1. [3] German (2026-05-13), arXiv:2605.13385v1.
