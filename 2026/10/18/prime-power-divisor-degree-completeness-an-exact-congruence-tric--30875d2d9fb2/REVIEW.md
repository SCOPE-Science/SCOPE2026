# Scientific review: prime-power polynomial divisor degrees

## Correctness — PASS

The finite-field factorization of cyclotomic polynomials yields exactly one degree-one factor and, for each prime-power level, a known multiplicity of factors whose degrees are multiplicative orders. The proof independently reconstructs the sufficient classes using the exact valuations of these orders and the interval-filling criterion for bounded coin sums. The obstruction cases prove exact *first* missing degrees, not merely the lack of some factor. The characteristic dividing the index and the even-base cases are included explicitly. Dirichlet's theorem with the prime number theorem in reduced arithmetic progressions supplies the claimed densities without an unproved hypothesis. The standalone checker has passed 1,242 exact factor-degree/order tests; its optional second implementation has passed 242 genuine finite-field polynomial factorizations. These are finite stress tests, not substitutes for the all-primes proof.

## Originality — PASS, with disclosed residual risk

The closest primary sources are Thompson's 2011 preprint and 2012 thesis/2014 journal article, which define the property and establish the general multiplicative-order factorization criterion. They already give the sufficient congruence classes \(p\equiv\pm1\pmod n\) for a fixed index \(n\), characterize same-characteristic powers, and mention \(n=5\) as a prime-index example. Those contributions are fully credited. The present claim simultaneously classifies all odd prime-power indices, finds the exact first missing degree on the complement, proves exponent-two stabilization of qualifying prime characteristics, and computes their prime-density limit. The generic factor-degree lemma implies this result only after the specialized multiplicative-order valuation and subset-sum analysis; no matching specialized statement was found in the inspected primary sections or targeted literature and published-results searches. A differently worded earlier classification, an uninspected appendix, or an unindexed table may still exist; search failure is not a uniqueness guarantee.

## Value — PASS

The problem of divisors of every degree is an established arithmetic question. Prime powers are its first natural indexed family; the result identifies an exact arithmetic progression description of *all* qualifying characteristics, proves that higher powers give no new restrictions beyond the square, locates the least failing degree in every excluded congruence class, and converts the classification into exact prime densities. These features are not an arbitrary chosen numerical slice and can serve as structural benchmarks for more general cyclotomic-index families. The result makes no new claim about non-prime-power indices or uniform errors for prime counts.

## Boundaries and literature comparison

Thompson, *On the divisors of \(x^n-1\) in \(\mathbb F_p[x]\)* (arXiv:1111.5403), and *Variations on a question concerning the degrees of divisors of \(x^n-1\)* (arXiv:1206.4355; DOI 10.5802/jtnb.866), provide the motivating framework. Chapter 6 of *Products of Distinct Cyclotomic Polynomials* develops the original polynomial property and sufficient characteristic classes. OEIS A336504 and A336505 tabulate related characteristic-specific sequences, but the displayed data and algorithms do not establish the all-prime, all-exponent classification. The comparison with Pollack–Thompson, arXiv:1206.2084, concerns a related number-field formulation, not the same prime-field criterion. The strongest unresolved risk is an obscure original-text formulation of the prime-power case. No claim of a complete survey of all archival literature is made.

Self-review: passed. Independent audit: not yet performed.
