# Scientific review: bounded exceptions in dyadic Stirling valuations

## Correctness — PASS

For every positive \(c,h\), the interior theorem has the precise range \(0\le b<c\), \(1\le a<2^h\), \(2^h-a\ge 2t_b\), where \(t_b=\nu_2\binom{2c-b-1}{c}\). The published exact Stirling–Bernoulli partition expansion is used as an equality. The term with \(u_1=n-k\) has valuation \(t_b-s_2(n-k)\) after multiplication by \((n-k)!\). For \(d\ge(c-b-1)2^h\), Kummer's carry identity makes the binomial coefficient's valuation constant; for smaller \(d\), the estimate \(\nu_2\Lambda\le(w+d)/2\) and the threshold \(2^h-a\ge2t_b\) make every other term strictly higher in valuation. The counting bound follows from the finite set of excluded end positions. No cancellation or unproved extrapolation is used. The exact recurrence verifier checks 19,812 positive-index coefficients, including 18,537 certified-range indices, and all bounded-exception envelopes. The 2-adic valuation of zero is excluded and the top endpoint is handled separately.

## Originality — PASS within inspected evidence

Adelberg–Lengyel (2021), Theorem 3.1, covers the initial half of each \(2^h\)-block subject to a size condition; Section 3.4 explicitly asks whether the formula holds for asymptotically almost all \(k\). The new claim gives a stronger, uniform bounded-exception theorem with \(E(c)\) independent of \(h\). The proof technique and exact partition identity originate in that source and are explicitly credited. Adelberg (2019) supplies general binary Stirling bounds and a limiting theorem for scaled indices, but not this all-interior bounded-exception estimate. Other relevant related searches, including an article on central Stirling numbers, did not identify full coverage. Search incompleteness and an implicit existing consequence remain risks. Numerical novelty is not asserted.

## Mathematical value — PASS

The result proves a specific, numbered 2021 conjecture and improves its qualitative limiting statement to the quantitative \(O_c(2^{-h})\) rate, while providing explicit local windows of validity. Its value lies in replacing half-block coverage by almost-full-block coverage for every fixed \(c\) and in obtaining a uniform number of possible exceptions, not merely an isolated extension of a numerical table.

## Closest literature and limits

- A. Adelberg and T. Lengyel, *New Results on the p-adic Valuation of Stirling Numbers*, arXiv:2111.08766v1 (2021), Theorem 3.1, Section 3.4 (Conjecture 3.1), Appendix 5.4.
- A. Adelberg, *The 2-Adic Analysis of Stirling Numbers of the Second Kind via Higher Order Bernoulli Numbers and Polynomials*, arXiv:1912.01090v1 (2019), Theorems 2.1–2.6, Section 3.
- A. Adelberg and T. Lengyel, *New Results on the 2-Adic Valuation of the Central Stirling Numbers S(2k,k)*, Fibonacci Quarterly 63 (2025); accessible abstract covers the central family, and full text has not been compared.

The proof does not determine the actual valuations at every excluded boundary index. Absolute bibliographic novelty and independent scientific validation are not certified.

Self-review: passed. Independent audit: not yet performed.
