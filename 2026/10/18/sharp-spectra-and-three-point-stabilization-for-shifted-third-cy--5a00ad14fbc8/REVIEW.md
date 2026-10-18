# Scientific review: shifted third-cyclotomic gcds

## Correctness — PASS
The domain and normalized gcd are explicit. The proof exhausts primes: \(2\) never occurs; for \(p\ge5\) dividing the shift the simple-root derivative caps valuations at the shift exponent; for \(p\ge5\) outside the shift, the factor \(d^2+3\) and a unique linear congruence determine every exponent; and for \(3\) the valuation of \(F(n)\) is at most one. The second finite difference forces complete stabilization after three terms. Hensel lifts, exact CRT counts and the prime-power period obstruction establish all claimed frequencies, attained maxima, spectra and least periods. A standard-library verifier reproduced extensive direct calculations. Its finite checks are not treated as an infinite proof.

## Originality — PASS relative to inspected sources
Bodin–Drouin, arXiv:2409.01224v1, Theorems 2.5 and 5.2 and Proposition 6.1, give general polynomial-gcd periodicity, simple-root local decomposition and local-period machinery. Those ingredients are not new and make the explicit cyclotomic application an important potential overlap risk. The inspected source does not supply the explicit uniform decomposition by prime factors of \(d\) versus \(d^2+3\), the three-term stabilization identity, nor the all-divisor full frequency law and sharp periods for every shift. Relevant older coprime-values literature was also compared. Drouin's related 2023 preprint could be located but not read in full; it remains a named residual risk. Unindexed equivalent work remains possible.

## Value — PASS
The family provides a natural exact laboratory for a generic polynomial-resultant periodicity theory: a generic resultant bound \(d^2(d^2+3)\) is replaced by exact attainable maximal gcd and minimal period, every possible gcd is classified with its density, and adding the third term provably removes precisely the extra shifted-discriminant prime powers. The statement covers unbounded shifts and all window lengths without arbitrary cutoffs; it is not a one-off parameter computation.

## Scope and limitations
No claims for arbitrary polynomials or arbitrary non-arithmetic shift sets. The comparison is based on inspected accessible primary literature and indexed mathematical records, and further independent scholarly comparison is warranted.

Self-review: passed. Independent audit: not yet performed.
