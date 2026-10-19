# Mathematical review

**Correctness — PASS.** The obligatory de Bruijn-edge multiset has exactly \(F_{k-1}\) units of positive/negative degree imbalance, from states beginning `10` and ending `11`. Every necessary compensating path must have length at least \(k-2\) because a shorter path would equate the incompatible pairs `11` and `10`. A length-\((k-2)\) path exists between any negative and positive states; the augmented graph is balanced and connected, so an Euler circuit attains the lower bound. The required word count is proved by separating words with and without `11`; boundaries \(k=3\) and all larger \(k\) are covered. The standalone verifier constructs and checks optimal hosts for \(k=3,\ldots,16\), with no inference from finite data to the infinite theorem.

**Originality — PASS against the inspected evidence.** Burstein–Kitaev [1] studies unavoidable pattern sets; Moreno–Matamala [2] studies lexicographic minimum de Bruijn sequences within forbidden languages rather than shortest unrestricted cyclic covers; Chen–Kitaev–Sun [3] studies exact-once universal cycle existence. The same Fibonacci-product numbers appear at OEIS A023607, but an integer-sequence record is not evidence of the present covering optimization theorem. Earlier `111`-avoidance cyclic-cover work is a different implication domain, with Tribonacci rather than Fibonacci language growth. Equivalent theorems in other presentations or unindexed literature remain a residual risk.

**Mathematical value — PASS.** The exact optimum at every window size is a natural shortest-periodic-test-string invariant. The constructive bound works even if forbidden windows are introduced, while the excess-to-required ratio grows linearly; this demonstrates structural inefficiency invisible in the exact-once universal-cycle framework. The result holds for a symmetry orbit of four forbidden triples.

**Limits.** The theorem neither enumerates all optimal cycles nor handles arbitrary forbidden pattern sets; independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.

References: [1] arXiv:math/0311399; [2] arXiv:0711.1695; [3] arXiv:2005.00165; [4] OEIS A023607.
