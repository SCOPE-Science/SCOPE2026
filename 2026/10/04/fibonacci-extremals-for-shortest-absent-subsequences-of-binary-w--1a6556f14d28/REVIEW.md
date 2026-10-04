# Same-model review

## Correctness
**PASS.** The proof reduces arbitrary two-symbol words at fixed universality index to two-letter arches using subsequence monotonicity, then evaluates the resulting boundary-matrix products exactly. The Fibonacci state bound is an induction with equality witnesses. For odd length, the length budget leaves exactly one three-letter component; every allowed interior and final component is enumerated, and the Fibonacci product inequality closes the upper bound. The explicit constructions attain both parity bounds. Independent Python enumeration through length \(14\) and a separate C census through length \(22\) reproduce the formulas.

## Originality
**PASS, with a stated residual risk.** Kosche–Koß–Manea–Siemer already give the fixed-universality extremal framework and the SAS gluing/monotonicity lemmas; that prior coverage is explicitly credited. Their inspected text does not give the binary Fibonacci evaluation or optimize under a fixed total word length. The later nearly-universal and binary Simon-congruence papers characterize related classes but likewise do not state the fixed-length parity law. published-finding corpus searches for binary shortest-absent-subsequence maxima, Fibonacci formulas, and fixed-length extremals returned no matching claim. The even-length formula is close to a specialization of prior fixed-universality work; the substantive surviving addition is the exact all-length theorem and the odd one-extra-symbol bound.

## Value
**PASS.** The source literature emphasizes that SAS sets can be exponentially large and that exact structure matters for compact representation. A word-length extremal function is a natural quantitative invariant. The result replaces a qualitative/exponential picture, in the binary case, by an exact closed form for every length and exposes a nontrivial parity effect: one extra symbol does not reach the unconstrained fixed-index maximum. The proof is short, structural, and reusable as a transfer-matrix template.

## Closest literature and limitations
The closest source is *Absent Subsequences in Words* (arXiv:2108.13968), especially Lemmas 3.11 and 3.13 and Proposition 3.14. *m-Nearly k-Universal Words* (arXiv:2202.07981) provides a more detailed absent-subsequence class characterization, and *α-β-Factorization and the Binary Case of Simon's Congruence* (arXiv:2306.14192) treats the binary congruence structure. The present claim is limited to the binary alphabet, shortest absent subsequences, and the extremal count; it does not classify every extremizer.

Same-model review: passed. Independent audit: not yet performed.
