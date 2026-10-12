# Review of the prime-power solvability-word theorem

## Correctness
PASS. The domain is all odd primes, exponents at least two, and primitive roots modulo the corresponding prime powers. The inverse-parity equivalence is reconstructed with explicit nonnegative solutions and exclusivity; the even-unit sum is evaluated exactly; its invertibility eliminates every proper stabilizer; and the unique involution gives complementarity. The finite verifier checks 33 moduli, 272 primitive-base cases, and direct equations independently. Finite tests do not replace the infinite proof. The moment identity and its parity bounds were individually checked against exact arithmetic.

## Originality
PASS with a specified remaining literature risk. The motivating article's Theorem 4.1 gives only a period dividing the multiplicative order; its Theorem 1.2 identifies inverse parity. Classical binary \(d\)-sequences already provide maximal-period and complement facts for primes. OEIS A167791 also records full periods of binary reciprocals for prime-power moduli admitting primitive base \(2\); this establishes an overlapping base-\(2\) subfamily, not claimed as new. The all-generator prime-power theorem includes moduli where base \(2\) has smaller order, such as \(49\), and proves output maximality for any primitive root via an invertible even-unit sum. Searches using equivalent output-sequence, least-significant-bit, \(d\)-sequence, and modular-generator terminology found no theorem explicitly covering this full prime-power conclusion. The 2008 \(d\)-sequence period paper's full text could not be obtained, and an implicit covering result is still possible; this risk requires human literature evaluation.

## Value
PASS. The 2026 source explicitly singles out periodicity of the solvability predicate, but its bound does not decide whether the output loses state information. Exact least period is the natural unknown invariant of that binary sequence. Beyond the previously known base-\(2\) prime-power subfamily, the theorem completely settles the primitive-root prime-power family, gives precise half-period anticorrelation and balance, and exposes a structural reason the output cannot collapse. A concrete nonprimitive example shows the distinction matters.

## Limits
Only odd prime powers with primitive-root bases are covered; the general output-period classification remains open here. Searches do not establish absolute novelty. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
