# Same-model scientific review

## Correctness
PASS. The proof reduces the complex order-154 claim to the published square-free lifting theorem with p=11 and N'=14. The packaged exact verifier constructs GF(11^3), verifies an element of order 1330 and primitive 14th roots, covers representatives of both Frobenius orbits, and checks all 16383 nonempty principal determinants for each representative. Every zero count is zero; Frobenius preserves nonvanishing.

## Originality
PASS. Targeted searches for the exact order, aliases, finite-field premise, and stronger coverage found no statement of the order-154 result. The closest inspected papers prove only size-two/three cases, give a conditional lifting theorem whose explicit bound does not cover 154, or settle different orders 70 and 143. The supplied characteristic-11 order-14 premise is not stated in those sources.

The closest literature is arXiv:2409.09793, arXiv:2505.24326, and arXiv:2608.17746. The first gives low-size square-free principal-minor results and the conjecture; the second gives the conditional lifting mechanism and a sufficient-growth theorem that does not cover \(154\); the third certifies orders \(70\) and \(143\). Targeted exact-order and finite-characteristic searches found no order-
\(154\) statement. Residual risk remains from unindexed or unpublished work and from not inspecting the full text of arXiv:2608.17746.

## Value
PASS. The result resolves a natural concrete three-prime square-free case of the published principal-nonsingularity conjecture. It supplies a complete finite certificate for the exact missing premise of a general lifting theorem, rather than an arbitrary parameter slice, and extends the recent order-specific certificate program to a distinct arithmetic configuration 2·7·11.

## Limitations
The result is one exact square-free order, not a family theorem. It depends on a published lifting theorem and a finite exhaustive certificate. It establishes principal-minor nonvanishing only.

Same-model review: passed. Independent audit: not yet performed.
