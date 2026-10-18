# Review of the early odd-greedy prime stopping-profile classification

## Correctness — PASS

The proof establishes the canonical greedy denominator at each stage, including the unit numerator reductions, and uses exact congruences modulo \(4,5,9,7\) to classify all primes \(p>3\). The parity restriction correctly rules out any odd finite length. The division steps require only invertible constants in their stated moduli. The density count is \(144+36+78+30=288=\varphi(1260)\); the prime number theorem in progressions justifies the densities. The four sharpness witnesses, combined with Dirichlet and the generalized Chinese remainder theorem, exclude *every* smaller candidate modulus, not just divisors. The standalone exact checker confirms 9,590 prime inputs and the 288 residue classes. A finite check alone would not establish these infinite assertions.

## Originality — PASS, with residual risk

Pihko's 2001 and 2010 texts discuss the algorithm, numerator growth, and long runs, including examples with numerator \(2\). Louwsma–Martino (2023, 2025) fully classifies the two-term case; the two-term branch is credited. Earlier general fixed-horizon congruence work and the four-term result are acknowledged rather than presented as new. The contribution is the explicit sharp modulus \(1260\), the *first complete six-term prime-denominator criterion*, and the exact four-way prime densities, which are not numerically determined by those broader existence/periodicity statements. The closest indexed searches returned related but non-equivalent restricted-denominator Egyptian fraction results, not this claim. A differently phrased or unindexed prime-class table might nevertheless cover it.

## Mathematical value — PASS

Early stopping lengths are a natural quantitative invariant in the odd-greedy algorithm, whose eventual termination is open. This gives the exact first nontrivial prime-parameter horizon beyond the previously characterized two- and four-step cases, a sharp congruence conductor rather than just a crude computable period, and rational prime densities. These furnish exact baseline frequencies for longer greedy runs. The claim does not resolve eventual termination or long-horizon distributions.

## Relationship and limits

Nearest primary literature: Pihko, Fibonacci Quarterly 39 (2001) and 48 (2010); Louwsma–Martino, arXiv:2309.07280 and Integers 25 (2025). The dated 2011 archival paper is background on restricted Egyptian fractions, not a source of this specific result. Complete comparison with unindexed old tables cannot be guaranteed. Independent mathematical replication and external review remain necessary.

Self-review: passed. Independent audit: not yet performed.
