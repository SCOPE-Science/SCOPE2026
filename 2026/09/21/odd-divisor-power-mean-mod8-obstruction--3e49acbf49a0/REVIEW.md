# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked adversarially at the following points.

1. For odd prime \(p\) and even \(r\), \(p^r\equiv1\pmod8\), so each local divisor-mean factor can legitimately be treated by the stated 2-adic lemma.
2. The binomial identity
   \[
   F_N(1+8h)=\sum_{k=0}^{N-1}(8h)^k\binom{N-1}{k}/(k+1)
   \]
   was rederived from \(\sum_{j=k}^{N-1}\binom jk=\binom N{k+1}\). For \(k\ge2\), the factor \(8^k/(k+1)\) has 2-adic valuation at least 3, so discarding those terms modulo 8 is valid even when \(k+1\) is even.
3. The lemma's residue is always odd. Hence every local factor, and therefore \(M_r(n)\), is a 2-adic unit; no hidden division by 2 occurs in the modular argument.
4. For \(r\equiv0\pmod4\), every odd \(p\) satisfies \(p^r\equiv1\pmod{16}\). For \(r\equiv2\pmod4\), \(p^r\equiv p^2\pmod{16}\), giving exactly the local residues 1 and 5 stated in the proof.
5. Only primes occurring to odd exponent affect both the local 5-factor count and the Jacobi symbol \((2/n)\), so the passage from the product of local residues to the residue class of \(n\pmod8\) is exact.
6. In the perfect-power corollary, 2-adic unitality forces \(c\) odd; an even power of an odd integer is \(1\pmod8\). Thus the exclusion of \(n\equiv3,5\pmod8\) has no parity loophole.

A standalone exact computation checked all 500,000 pairs consisting of an odd \(n\le200000\) and \(r\in\{2,4,6,8,10\}\), with zero congruence mismatches. The same program directly found 21 odd RMS numbers in this range, all with residue 1 or 7 modulo 8. These checks support but do not replace the proof.

Correctness verdict: PASS.

## Originality

The closest located sources were checked as follows.

- The current OEIS A140480 entry was inspected. It defines RMS numbers and contains T. D. Noe's empirical 2008 comment that the then-known terms appeared to be \(\pm1\pmod8\); the entry later points to A224988 for even RMS numbers. No proof or general mod-8 formula is supplied there.
- A140480 and A003601 record C. O. Zizka's 2008 definition of \(\sigma_r\)-numbers by \(\sigma_r(n)/\tau(n)=c^r\). The present result applies uniformly to all even \(r\), and to more general even perfect-power exponents.
- A224988 was checked to separate the odd statement from the known even RMS sequence. The theorem makes no claim that even RMS numbers are \(\pm1\pmod8\).
- Oller-Marcén, *On arithmetic numbers* (arXiv:1206.1823), was inspected in accessible full text. It treats the ordinary divisor mean \(\sigma(n)/\tau(n)\) and its integrality, not the even-power divisor means or the congruence proved here.
- Exact and synonymous web searches included “RMS numbers”, “root/quadratic mean of divisors”, “sigma_2(n)/tau(n)”, “sigma_r-number”, and combinations with “mod 8”. No equivalent theorem or stronger result was located.
- The current SCOPE archive was searched for RMS, divisor power mean, and sigma-r mod-8 terminology; no overlapping record was found.

No specific inaccessible paper surfaced as a concrete source likely to contain the theorem. The main residual risk is informal, older sequence discussion or material using different terminology that is poorly indexed. Because the central RMS observation has circulated in OEIS since 2008, priority is claimed only for the proof/generalization to the best of our knowledge, not for the empirical observation itself.

Originality verdict: PASS, to the best of our knowledge.

## Value

The result converts a long-recorded empirical residue pattern for odd RMS numbers into a theorem and identifies the local 2-adic mechanism behind it. The stronger statement determines the entire mod-8 residue of \(\sigma_r(n)/\tau(n)\) for every odd \(n\) and every even \(r\), and yields a uniform obstruction for generalized \(\sigma_r\)-numbers whenever \(r\equiv2\pmod4\). The distinction between \(r\equiv0\) and \(2\pmod4\) also explains exactly when this mod-8 method can and cannot impose a condition on \(n\).

Value verdict: PASS.
