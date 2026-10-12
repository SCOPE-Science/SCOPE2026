# A forty-term obstruction for distinct semiprime Egyptian fractions

## Finding

Let \(r\) be the minimum number of **distinct** fractions \(1/(pq)\), where \(p<q\) are primes, in a finite sum equal to \(1\). Then
\[
\boxed{41\le r\le47}.
\]
In particular, no sum of at most \(40\) pairwise distinct squarefree-semiprime unit fractions equals \(1\). The upper bound is furnished by Watanabe's published \(47\)-term representation. This is a lower bound, **not** a proof that \(r=41\) or that \(r=47\).

## Assumptions and scope

Every denominator is the product of **two distinct primes**; denominations must be pairwise distinct, while the same prime may occur in several denominators. The theorem concerns the minimum number of terms in a representation of \(1\), not the existence of representations of arbitrary rationals or their maximal denominators.

Fix \(M=2000\), \(K=40\),
\[
\lambda=\frac{29}{4000},\qquad
\mu=\frac{\lambda-1/2001}{2}=\frac{54029}{16008000}>0.
\]

## Proof

Suppose \(1=\sum_{d\in S}1/d\) for a set \(S\) of \(k\le40\) distinct squarefree semiprimes. Partition \(S=H\sqcup T\) into the *head* \(H=\{d\in S:d\le2000\}\) and *tail* \(T=\{d\in S:d>2000\}\), writing \(t=|T|\). The tail has total reciprocal mass at most \(t/2001\).

For each prime \(p\) that divides a head denominator, put
\[
N_p=\{q:pq\in H\},\qquad
\rho_p=\sum_{q\in N_p}q^{-1}\pmod p.
\]
Here \(q^{-1}\) is the multiplicative inverse modulo \(p\). Multiply the assumed integer sum by \(p\), working in the localization at \(p\), and reduce modulo \(p\). Terms without a factor \(p\) vanish in this reduction. Consequently
\[
\sum_{q:pq\in S}q^{-1}\equiv0\pmod p.
\]
If \(\rho_p\ne0\), at least one tail denominator has prime factor \(p\). Since each tail semiprime has exactly two prime factors, the number \(b\) of head primes with \(\rho_p\ne0\) is at most \(2t\).

For each prime \(p\le2000\) and subset \(U\) of the primes \(q\ne p\) satisfying \(pq\le2000\), define
\[
F_p(U)=\sum_{q\in U}\left(\frac{1}{2pq}-\frac{\lambda}{2}\right)
-\mu\,\mathbf1_{\{\sum_{q\in U}q^{-1}\not\equiv0\pmod p\}},
\qquad C_p=\max_U F_p(U).
\]
Empty subsets are permitted, so \(C_p\ge0\). Summing each head edge over its two incident primes gives exactly
\[
\sum_{d\in H}\frac1d-\lambda|H|
=\sum_p\left(F_p(N_p)+\mu\mathbf1_{\{\rho_p\ne0\}}\right)
\le\sum_pC_p+\mu b.
\]
It follows that
\[
1\le\lambda(k-t)+\sum_pC_p+2\mu t+\frac{t}{2001}
=\lambda k+\sum_pC_p
\le40\lambda+\sum_pC_p.
\]
Thus it remains to show the right side is **strictly below one**.

The accompanying standalone verifier evaluates a rigorous upper bound for every \(C_p\). It enumerates all \(563\) possible squarefree semiprimes \(pq\le2000\), and for each of the \(168\) incident primes performs a two-choice dynamic program indexed by the residue \(\sum q^{-1}\pmod p\). All arithmetic used for the bound is **integer** arithmetic. With scale \(L=10^{12}\), it rounds every weight \((1/(pq)-\lambda)/2\) **upward**, and the penalty \(\mu\) **downward**, before maximizing. Therefore the computed \(\widehat C_p/L\) is at least \(C_p\), rather than an unverified numerical approximation.

The computation yields
\[
\sum_p\widehat C_p=704269451136,
\]
and hence the exact rational bound
\[
40\lambda+\sum_pC_p
\le\frac{29}{100}+\frac{704269451136}{10^{12}}
=\frac{7767730087}{7812500000}<1.
\]
This contradicts the assumed sum. Consequently \(r\ge41\). Watanabe's published \(47\)-term identity gives \(r\le47\).

## Verification

Run `python3 artifacts/verify.py` using Python's standard library. The program independently builds a complete prime sieve through \(2000\), enumerates every eligible semiprime, derives residue inverses modulo each prime, and computes all maxima by exact integer dynamic programming. Its final comparison is an integer inequality, with a strict rational margin. It prints the scales, certified upper fraction, and all positive local contributions. The saved replay is `artifacts/replay.txt`.

As boundary stress tests, the same code passed for coarser upward/downward rounding scales \(10^8\) and \(10^{10}\). The original \(48\)-term Johnson example was separately checked by exact rational summation and found to satisfy every prime-local cancellation congruence, confirming that the congruence is necessary rather than an unintended prohibition on valid examples. The finite computation is an exhaustive proof of the **head optimization only**; the symbolic tail estimate covers all denominators above \(2000\), with no unverified cutoff.

## Relationship to prior work

Watanabe (arXiv:2009.03275v2) constructs \(17\) examples with \(47\) terms, states that \(47\) is the **conjectured** minimum, and initially restricts his constructive search to prime factors at most \(53\). His Section 4.1 separately reports **no 46-term examples when the maximum prime factor is at most \(101\)**; neither that restricted computation nor the 47-term constructions establish an unconditional, unrestricted lower bound \(41\). Li (arXiv:2606.15159v2) proves the existence of a distinct-semiprime-unit-fraction representation for every positive integer, but his theorems do not quantitatively lower-bound the number of terms for \(1\). Li's subsequent arXiv:2609.32140 concerns existence for rationals with squarefree denominator and likewise does not present this minimum-rank obstruction in its accessible statement.

The bound here is unconditional over **all** primes, even though the only finite search involves head denominators at most \(2000\); the remaining infinite set is removed by a rigorous penalty inequality. The residue-dual argument differs from a bounded search for a short representation.

## Limitations

The exact minimum \(r\) is **not** determined: \(41\le r\le47\) is all that is proved. This method certifies the nonexistence of representations with at most \(40\) terms; it does not exclude \(41\)- through \(46\)-term representations, and it does not claim that Watanabe's conjectural value \(47\) is established. The localized optimization is a finite computation, but the prime-local cancellation and tail reduction are proven for arbitrary denominators.

## References

1. Shisheng Li, *Every natural number is a sum of distinct semiprime unit fractions*, arXiv:2606.15159v2 (first submitted 2026-06-13), Theorem 1.2 and Sections 1–2.
2. Tatsuru Watanabe, *New examples of the representation of 1 by the sum of reciprocals of semiprime numbers*, arXiv:2009.03275v2 (2020), Introduction, Sections 2–3.
3. Shisheng Li, *Unit fractions with semiprime denominators: an elementary proof of Erdős Problem #306*, arXiv:2609.32140 (2026), abstract and problem scope.
4. OEIS A201650, Johnson's 48-term squarefree-semiprime reciprocal representation of \(1\).
