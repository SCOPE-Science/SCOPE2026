# Scientific review

## Correctness

**PASS.** Suppose \(2\le a<b\), \(a\mid g(b)\), and \(b\mid g(a)\), with \(g(t)=t^{2}-t+1\). The integer \(z=g(a)/b\) satisfies \(1\le z<a\) and \(bz\equiv1\pmod a\). The identity \(z^{2}g(b)\equiv g(z)\pmod a\) supplies a strictly smaller reciprocal pair, or the impossible case \(z=1\); this closes all quantifiers. For squarefree \(n\), exact multiplicativity gives \(\mathcal H(n)=\prod_{p\mid n}g(p)/n\). Its integrality forces a functional prime-divisibility graph, whose cycles must have length at least three. The displayed three-prime witness is supported by exact trial-division primality checks and exact product congruences in `verify.py`. Finite tests support, but do not establish, the infinite descent.

## Originality

**PASS, with residual risk.** The relevant recent full text is De Koninck–Letendre, arXiv:2610.10572v1, especially Section 5, Proposition 1. That proposition bounds the number of prime pairs satisfying the reciprocal sixth-cyclotomic divisibilities; it does not exclude them. The exact exclusion implies their proposition's first-power two-cycle count is zero, while leaving squared-exponent cycles untouched. OEIS A317480 tabulates integral reciprocal-gcd sums without providing this descent theorem. The existing explicit three-prime witness and its leastness are separate previously investigated facts and are not claimed as new. Targeted searches for reciprocal divisibility, sixth-cyclotomic two-cycles, equivalent directed-graph formulations, and dominating statements did not identify a covering assertion. This is best-knowledge originality rather than a proof of priority: the underlying descent technique is classical and an unindexed earlier application is possible.

## Mathematical value

**PASS.** The exact zero theorem removes the entire first-power/first-power two-cycle case from a genuine decomposition in recent analytic-number-theoretic research. Its scope is stronger than prime-pair exclusion because the lemma covers arbitrary integers. It also gives the sharp natural lower bound \(\omega(n)\ge3\) for nontrivial squarefree inputs with integral reciprocal-gcd sums. The implication is a structural result about the arithmetic prime-divisibility graph, not merely a numerical lookup, a notational variant, or a generic easy congruence check.

## Sources and limitations

The strongest direct comparison is De Koninck and Letendre (2026), Section 5, Proposition 1 (https://arxiv.org/html/2610.10572v1); their graph setup is in Section 2 and preliminary bound \(\omega(n)\ge2\) in Section 1. OEIS A317480 (https://oeis.org/A317480) records examples and the integrality predicate. The result does not exclude cycles with a squared-prime vertex, classify arbitrary exponents, or imply infinitude. The witness is used only to show the support bound is achievable. Undiscovered equivalent proofs remain an originality risk.

Self-review: passed. Independent audit: not yet performed.
