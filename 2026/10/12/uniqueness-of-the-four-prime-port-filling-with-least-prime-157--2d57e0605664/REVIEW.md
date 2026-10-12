# Self-review of Uniqueness of the four-prime port filling with least prime 157

## Correctness

**PASS.** Fixing the least prime \(157\) converts the filling equation into an inherited three-prime port and then a last-two-prime equation. Positivity and the strict ordering of the remaining primes give exact finite ranges:
\[
1507<q\le4520
\]
and
\[
\frac{R_2}{c_2}<r\le\frac{2R_2}{c_2}.
\]
The packaged standard-library verifier exhausts all \(375\) prime values of \(q\) and all \(242779\) prime values of \(r\) in those proved ranges. Exactly one forced value of the final prime is integral, and it is \(16879\), producing the published filling. The defining port identity is then checked directly.

No finite experiment is being promoted to an infinite theorem: the proof itself establishes the finite search domain.

## Originality

**PASS.** The direct source proves existence and port-primitivity of \(157\cdot1979\cdot10093\cdot16879\), but port-primitivity only excludes proper divisors of that product. It does not exclude a different four-prime filling beginning with \(157\). The same paper later explicitly warns that its displayed smaller \(H\)-fillings do not constitute a complete classification.

Exact-parameter, least-prime, equivalent-equation, semantic-index, and own-ledger searches found no equivalent or stronger statement. The source's six-prime exploratory appendix is not a substitute: it is expressly exploratory and concerns a different support size.

## Value

**PASS.** The source identifies unexcluded smaller \(H\)-fillings as a genuine obstruction to organizing all inherited channels in the six-prime problem. The least-prime \(157\) branch is mathematically distinguished because it contains the paper's new four-prime filling and hence its new nine-prime primary pseudoperfect number. Proving that this entire branch has exactly one four-prime filling is therefore a motivated structural classification, not an arbitrary bounded computation.

## Closest literature and limitations

The closest source is Han Wang, arXiv:2605.21518v1. Its Proposition 8.3 proves that the displayed product fills the key port, Proposition 8.4 proves port-primitivity, and Appendix A.4 explicitly preserves the possibility of additional smaller fillings. The present result narrows that gap only for four-prime fillings whose least prime is \(157\); other least-prime branches remain open.

Self-review: passed. Independent audit: not yet performed.
