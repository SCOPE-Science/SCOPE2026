# Independent audit — 2026-10-01

## Final claim

Every deficient-perfect integer of the form \(2^apq\) with odd primes \(p<q\) belongs to exactly one of the two divisor-parametrized families in RESULT.md; its deficiency is \(2^e\) or \(2^ep\), never a multiple of \(q\), giving a finite exact search for each fixed \(a\).

## Correctness — PASS

For \(n=2^apq\), with \(M=2^{a+1}-1\), direct expansion gives \(D(n)=pq-M(p+q+1)=(p-M)q-M(p+1)\). Positivity forces \(p>M\), and reduction modulo the larger prime excludes \(q\) from the deficient divisor. Since the odd part is squarefree, only \(D=2^e\) and \(D=2^ep\) remain. Substituting \(s=p-M\) produces exactly the two stated divisor parametrizations, and direct substitution proves both converses. The package verifier cross-checks the parametrization against the definition for \(1\le a\le7\) and enumerates through \(a=12\); independent checks of the initial examples reproduce their deficiencies.

Checked sources:
- M. Tang, X.-Z. Ren, M. Li, On near-perfect and deficient-perfect numbers, Colloquium Mathematicum 133 (2013), abstract/bibliographic scope inspected.
- M. Tang, M. Feng, On deficient-perfect numbers, Bulletin of the Australian Mathematical Society 90 (2014), primary article inspected.
- OEIS A271816, Deficient-perfect numbers.
- Published-record semantic search for deficient-perfect numbers of the form two-power times two odd primes.

Residual risks:
- The theorem is restricted to squarefree odd part with exactly two odd prime factors.

## Originality — PASS

Best-of-knowledge originality passes. The foundational paper classifies deficient-perfect numbers with at most two distinct prime factors, while the 2014 primary paper rules out odd deficient-perfect numbers with exactly three distinct prime divisors. OEIS records the initial even examples but not this two-family parametrization. The published-record search returned no prior exact classification of the squarefree even three-prime slice.

### Equivalent formulations

Searches:
- Resultary semantic query: deficient perfect numbers two power times p q squarefree odd part parametrization
- Search for deficiency divisor exclusion of the larger odd prime

Evidence:
- The exact published-record hit was the assigned finding.
- No synonymous fixed-exponent divisor parametrization was located.

Reasoning: Equivalent formulations include classifying possible deficiency divisors and parametrizing the prime pair by divisors of two explicit integers.

### Broader coverage

Searches:
- Tang--Ren--Li 2013 scope
- Tang--Feng 2014 full article
- OEIS A271816

Evidence:
- The 2013 work covers at most two distinct prime factors.
- The 2014 theorem excludes odd three-prime cases but does not classify the even slice.
- OEIS tabulates examples rather than a theorem.

Reasoning: The audited theorem addresses the first even three-distinct-prime slice not dominated by those classifications.

### Exact database or table

Searches:
- OEIS A271816
- Package exact enumeration for fixed exponents

Evidence:
- OEIS contains the initial solutions including 884 and later examples.
- The package verifier reproduces the known initial values and extends a bounded census.

Reasoning: Sequence membership does not mechanically imply the two-family parametrization or completeness for each fixed exponent.

### Claim versus prior implication

Searches:
- Tang--Ren--Li 2013 classification versus current three-prime slice
- Tang--Feng 2014 odd-three-prime exclusion

Evidence:
- The two-prime theorem has fewer distinct prime factors.
- The odd-three-prime impossibility has incompatible parity and does not imply the even classification.

Reasoning: The present two-family theorem is not a corollary of either identified classification.

### Source inspections

- **On deficient-perfect numbers** — Neighboring but not covering the even squarefree slice. Material read: Primary article, including the theorem excluding odd deficient-perfect numbers with exactly three distinct prime divisors and its literature context. Evidence: The theorem applies to odd numbers; the audited family is even and is parametrized rather than excluded.
- **OEIS A271816: Deficient-perfect numbers** — Confirms initial values but contains no completeness theorem for \(2^apq\). Material read: Sequence entries and commentary around the first three-prime examples. Evidence: The sequence lists 884 as an early three-distinct-prime term without the audited parametrization.

Checked sources:
- M. Tang, X.-Z. Ren, M. Li, On near-perfect and deficient-perfect numbers, Colloquium Mathematicum 133 (2013), abstract/bibliographic scope inspected.
- M. Tang, M. Feng, On deficient-perfect numbers, Bulletin of the Australian Mathematical Society 90 (2014), primary article inspected.
- OEIS A271816, Deficient-perfect numbers.
- Published-record semantic search for deficient-perfect numbers of the form two-power times two odd primes.

Residual risks:
- The full 2013 article was not directly inspected; its scope was checked from its abstract and the later primary-paper literature summary.
- Equivalent older coverage under another divisor-sum terminology remains a best-of-knowledge risk.

## Scientific value — PASS

The result closes a natural first even three-prime slice beyond the known two-prime classification and odd three-prime impossibility. It reduces an open-ended prime search to finitely many divisor tests for every fixed exponent and identifies a structural exclusion on the deficient divisor.

Checked sources:
- M. Tang, X.-Z. Ren, M. Li, On near-perfect and deficient-perfect numbers, Colloquium Mathematicum 133 (2013), abstract/bibliographic scope inspected.
- M. Tang, M. Feng, On deficient-perfect numbers, Bulletin of the Australian Mathematical Society 90 (2014), primary article inspected.
- OEIS A271816, Deficient-perfect numbers.
- Published-record semantic search for deficient-perfect numbers of the form two-power times two odd primes.

Residual risks:
- The full 2013 article was not directly inspected; its scope was checked from its abstract and the later primary-paper literature summary.
- Equivalent older coverage under another divisor-sum terminology remains a best-of-knowledge risk.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
