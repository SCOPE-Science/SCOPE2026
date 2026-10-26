# Self-review

## Correctness — PASS

The identity for the integer Laurent quotient \(B_p=Q(x^p)/Q(x)\) follows from the cubic cyclotomic factorization for every \(p\ne3\). The freshman's-dream congruence and non-zero-divisor cancellation in the Laurent domain give integral \(A_p=(Q^{p-1}-B_p)/p\). Its support is strictly inside \((-p,p)\), so the constant-term extraction from the first-order binomial expansion has no cross-digit contributions. This proves the linearization for every multiplier, including multiples of the prime. Cao–Sun's base-index evaluation and Fermat's theorem yield the explicit formula; iteration yields the prime-power corollary. Exact integer computations passed all 372 tested pairs. No finite computation is used as a proof of an infinite assertion.

## Originality — PASS with residual literature risk

The closest specific earlier statement is Cao and Sun, Theorem 1.1(i), restricted to the one index \(p-1\). The present statement supplies an explicit prime-square lift to every index \(pm-1\). Mellit–Vlasenko's general Dwork congruences show a modulo-prime digit factorization and higher-power relations but do not state the claimed explicit first-order boundary evaluation. Pan and Sun's supercongruence concerns \(pn\), not \(pn-1\); Sun's systematic generalized-trinomial paper concerns different displayed congruences and sums. Targeted theorem/source/database searches did not locate an equivalent all-multiplier formula. This absence is not a proof of global uniqueness. Some relevant secondary literature was only inspected in its pertinent sections and may contain unlocated formulations.

## Value — PASS

A natural, already solved prime-index congruence becomes a uniform family over infinitely many multipliers. The first-order correction is controlled exactly by the initial digit's value, rather than by an unspecified error term. The resulting prime-power tower is an explicit consequence. The structural reason—the narrow support of a cubic-cyclotomic quotient—is mathematically informative and reproducible, beyond an arbitrary numeric extension.

## Closest literature and limits

The derivation requires the cubic cyclotomic divisor property and the published Cao–Sun evaluation; it does not treat primes \(2,3\), arbitrary indices, or modulus \(p^3\). Comparisons were made with Cao–Sun, Sun's generalized-trinomial work, Mellit–Vlasenko, and Pan–Sun. The exact boundary identity has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
