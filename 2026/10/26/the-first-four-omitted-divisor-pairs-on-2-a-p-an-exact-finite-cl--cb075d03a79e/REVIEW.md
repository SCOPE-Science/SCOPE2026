# Scientific review: first four-pair omission in the dyadic semiprime family

## Correctness — PASS

The claim is exactly limited to integers \(2^a p\) with \(a\ge1\) and an odd prime \(p\). The complement involution on divisors has exactly \(a+1\) pairs \(\{2^i,p2^{a-i}\}\), and the total deficit is \(2^{a+1}-1-p\). Pair \(i=0\) is too large; pair \(i=a\) creates an impossible parity. Thus every omission of any positive order is exactly represented by the integral quotient formula (2) with a subset of \(\{1,\ldots,a-1\}\). If \(n\le630194176\), primality forces \(a\le27\).

Complete exact exhaustion tests \(17550\) triple index sets and \(80730\) quadruple sets. For triples, the only odd integer quotients are \(3531,4595,76083\), all composite. For quadruples the eight possible integer quotients reduce to exactly three primes, with the least resulting integer \(630194176\). The four direct complementary pairs sum to \(2096550=\sigma(n)-2n\). The standalone checker independently recomputes all divisor sums and excludes smaller omission orders for that integer. No extrapolation from a partial finite search is used. Risk: code, arithmetic, and the finite bound must all be preserved together; a finite range does not establish a global statement beyond that range.

## Originality — PASS, subject to independent priority review

Wang–Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068v3 (2026), studies few omitted divisors and other prime-support families, but the inspected text does not give this full low-exponent three-/four-pair spectrum. A published mathematical note on the first multi-pair example for \(2^a p\) already introduces the general bit-mask quotient and identifies the first two-pair case; those facts are explicitly acknowledged, not represented as new. The new mathematical output is the complete three- and four-pair census through exponent \(27\), including no three-pair cases, the three precise four-pair cases, and the first four-pair witness. Exact-parameter searches did not identify a known table containing these results. The full text of the close published note was not retrievable; broader or less-indexed results remain a bibliographic risk.

## Mathematical value — PASS

Omission order counts the complementary divisor pairs that a strongly pseudoperfect representation must discard. This is a natural measure of representation complexity, highlighted by studies of near-perfect and strongly pseudoperfect numbers with few omitted divisors. A first realization threshold for order four and the full low-exponent spectrum resolve a concrete motivated finite question. The absence of order three up to the point where order four first appears shows that realizable omission sizes are not encountered in ascending order of their sizes. The exact list supplies useful calibration for future structural classification and search of the higher-order representations. No assertion is made about an infinite family, general minimal-order classifications, or a global nonexistence of three-pair omissions.

Self-review: passed. Independent audit: not yet performed.
