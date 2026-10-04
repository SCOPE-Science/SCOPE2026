# Review: Exact Tian classification for fixed support \(\{2,q\}\)

## Correctness
**PASS.** The reduction from \(\binom{n+1}{2}=2^{\alpha}q^{\beta}\) to \(\{n,n+1\}=\{2^A,q^\beta\}\) is exact because consecutive integers are coprime and both prime exponents are positive. Each remaining branch is exhausted: odd exponents greater than one leave a nontrivial odd factor, even exponents in the plus branch force the unique neighboring powers of two \(2\) and \(4\), and even exponents in the minus branch fail modulo \(8\). The endpoint counts and the \(q=3\) exception are then direct. The standalone exact-integer verifier agrees throughout its bounded test domain.

## Originality
**PASS, with residual bibliographic risk.** The closest current source, DOI 10.3390/math14010127, formulates the fixed-prime conjecture and gives a four-solution absolute bound for two primes, but does not state or imply the exact support \(\{2,q\}\) classification. Searches for the exact equation, Mersenne/Fermat reformulations, and the \(q=3\) equality case did not identify a stronger covering result. published-finding corpus's closest semantic returns concern other two-prime-support problems and do not imply this triangular-number theorem. Because the proof is elementary, an unindexed or differently phrased prior observation remains possible.

## Value
**PASS.** This is a natural, non-arbitrary slice of an explicitly current open conjecture: fixing the unique even prime changes the structure enough to make the sharp conjectured bound provable and yields a complete solution classification. It improves the cited general two-prime bound from four to two in this entire support family, identifies the unique equality support, and exposes the precise Mersenne/Fermat mechanisms.

## Closest literature and limitations
The primary comparison is Zeng–Pintér–Fu–Tian (DOI 10.3390/math14010127), especially the abstract, Section 3.2 Theorem 4, and the conclusion. The theorem here does not settle arbitrary odd-prime pairs and does not turn bounded computation into an infinite argument. Bibliographic searches cannot exclude unpublished, unindexed, or differently named elementary observations.

Same-model review: passed. Independent audit: not yet performed.
