# Rigidity of nonunitary-perfect integers with one repeated prime

## Finding
Let \(\sigma(n)\) be the sum of all positive divisors and \(\sigma^*(n)\) the sum of unitary divisors. A positive integer is **nonunitary perfect** when \(\sigma(n)-\sigma^*(n)=n\). Define \(\rho(n)=\#\{p:p^2\mid n\}\), the number of distinct prime divisors occurring with exponent at least two. For every positive integer \(n\) with \(\rho(n)\le1\),
\[
\sigma(n)-\sigma^*(n)=n
\quad\Longleftrightarrow\quad
n=2^{r+1}(2^r-1)\text{ with }2^r-1\text{ prime and }r\ge2.
\]
Consequently, any nonunitary-perfect number outside this classical family must have **at least two distinct squared prime divisors**. The examples on the right, not their existence, are classical; the classification for arbitrarily many squarefree cofactor primes is the point of the result.

## Assumptions and scope
All integers are positive. A divisor \(d\mid n\) is *unitary* if \(\gcd(d,n/d)=1\). A prime \(p\) contributes to \(\rho(n)\) exactly when its exponent in \(n\) is at least two. There is no bound on the size or number of prime divisors of \(n\) other than \(\rho(n)\le1\). When \(\rho(n)=1\), write \(n=p^a s\), with \(a\ge2\), \(s\) squarefree, and \(\gcd(p,s)=1\). Multiplicativity of \(\sigma\) and \(\sigma^*\) gives the exact identity
\[
\sigma(p^a s)-\sigma^*(p^a s)
=\sigma(s)\left(p+p^2+\cdots+p^{a-1}\right).
\tag{1}
\]
For \(s=1\), \(\sigma(s)=1\). The case \(\rho(n)=0\) has no nonunitary divisors and is excluded immediately.

## Proof
Suppose first that the single repeated prime \(p\) is odd. Define \(T=\sum_{j=1}^{a-1}p^j\). Then \(0<T/p^a<1/(p-1)\). If \(s\) is odd and \(s>1\), each prime \(q\mid s\) contributes an even factor \(q+1\) to \(\sigma(s)\); hence the left-hand side of (1) is even whereas \(n\) is odd. If \(s=1\), then \(\sigma(n)-\sigma^*(n)=T<p^a=n\). Thus \(2\mid s\) is necessary.

Write \(s=2t\), with \(t\) odd and squarefree. Equation (1) becomes \(\sigma(n)-\sigma^*(n)=3\sigma(t)T\). If \(t\) has at least two distinct prime factors, \(4\mid\sigma(t)\) whereas \(n=2p^at\equiv2\pmod4\), a contradiction. Hence \(t\) is either \(1\) or an odd prime, so \(\sigma(t)/t\le4/3\). But
\[
\frac{\sigma(n)-\sigma^*(n)}n
=\frac32\frac{\sigma(t)}t\frac{T}{p^a}
<\frac32\cdot\frac43\cdot\frac1{p-1}\le1,
\]
contradicting nonunitary perfectness. Therefore the unique repeated prime must be \(2\).

We now have \(n=2^a s\), with \(a\ge2\) and \(s\) odd squarefree. Since \(\sigma(2^a)-\sigma^*(2^a)=2^a-2\), equation (1) reduces to
\[
(2^a-2)\sigma(s)=2^a s.
\]
Set \(M=2^{a-1}-1\). Equivalently,
\[
M\sigma(s)=(M+1)s. \tag{2}
\]
If \(a=2\), then \(M=1\) and (2) requires \(\sigma(s)=2s\). This is impossible for odd squarefree \(s\): \(s=1\) is not perfect, while for \(s>1\), the \(2\)-adic valuation \(\nu_2(\sigma(s))\ge\omega(s)\) and \(\nu_2(2s)=1\), so \(s\) would have to be a single odd prime \(q\), yet \(q+1\ne2q\).

For \(a\ge3\) one has \(M>1\). Reducing (2) modulo \(M\) shows \(M\mid s\). The divisor-sum ratio is nondecreasing under divisibility: if \(u\mid v\) then \(\sigma(u)/u\le\sigma(v)/v\), with equality only when \(u=v\). Therefore
\[
\frac{M+1}{M}=\frac{\sigma(s)}s
\ge\frac{\sigma(M)}M\ge\frac{M+1}{M}.
\]
The second inequality is equality only for prime \(M\), since \(\sigma(M)\ge M+1\) and composite \(M>1\) has additional positive proper divisors. Both inequalities must be equalities; hence \(s=M\) and \(M=2^{a-1}-1\) is prime. Writing \(r=a-1\) proves the necessity.

Conversely, whenever \(M=2^r-1\) is prime and \(r\ge2\), put \(n=2^{r+1}M\). Its only repeated prime is \(2\), and
\[
\sigma(n)-\sigma^*(n)
=(2^{r+1}-2)(M+1)
=2^{r+1}(2^r-1)=n.
\]
This establishes both directions for every integer in the stated domain.

## Verification
The proof uses exact identities and inequalities, with no infinite claim inferred from a finite census. Run `python3 check.py` from the directory containing this file. The stand-alone script computes \(\sigma(n)-\sigma^*(n)\) through independent prime-power product formulas for all \(1\le n\le300000\), checks the theorem on those integers, tests additional structured cases, and verifies the Mersenne-prime family for exponents up to \(27\). The documented successful output is:

`VERIFY_OK interval 300000 all_nonunitary [24, 112, 1984, 32512] unique_powerful [24, 112, 1984, 32512] extra_exact_families 1782 Mersenne_tests 25`

## Relationship to prior work
Ligh and Wall (1987, pp. 333–334) introduced the nonunitary divisor sum, gave the prime-power factor formula used in (1), proved that the Mersenne-based family is nonunitary perfect, and conjectured that all nonunitary-perfect integers belong to it. The new assertion is the **converse under only the constraint \(\rho(n)\le1\)**, with no restriction on the number of squarefree prime factors. A 2024 MathOverflow argument establishes the corresponding converse when \(n=2^a p^b\) has exactly two distinct prime supports; it does not address any number of additional squarefree factors, nor a sole repeated odd prime with many singleton prime factors. Hagis (1990) studies odd nonunitary perfect integers; Graham (1989) classifies a different notion, **unitary** perfect integers with squarefree odd part. Neither is the statement here. The OEIS sequence A064591 records the known family, not the present full structural converse.

## Limitations
The theorem gives a necessary two-repeated-prime obstruction for *counterexamples* to the Ligh–Wall conjecture, not a proof of that conjecture. It says nothing about numbers with at least two repeated primes. The originality comparison is based on inspected primary texts, a relevant public problem discussion, sequence records, and targeted research searches; this is not a guarantee against an unindexed equivalent result. The brief inequality proof means that undiscovered older folklore is a genuine priority risk. The source literature appeared in November 1987 without a verified day-of-month; the separately recorded first fully day-resolved public source datum, OEIS A064591 (25 September 2001), is a conservative date anchor and is **not** asserted to be the original discovery date.

## References
1. S. Ligh and C. R. Wall, “Functions of Non-Unitary Divisors,” *The Fibonacci Quarterly* 25(4) (November 1987), 333–338. https://www.fq.math.ca/Scanned/25-4/ligh.pdf ; DOI: 10.1080/00150517.1987.12429676.
2. P. Hagis, Jr., “Odd Nonunitary Perfect Numbers,” *The Fibonacci Quarterly* 28(1) (1990), 11–15. Accessible transcript: https://studyres.com/doc/8796135/full-text .
3. S. W. Graham, “Unitary Perfect Numbers with Squarefree Odd Part,” *The Fibonacci Quarterly* 27(4) (1989), 316–322. https://www.fq.math.ca/Scanned/27-4/graham.pdf .
4. Joshua Zelinsky, proof for two-prime support, MathOverflow answer, 4 February 2024, https://mathoverflow.net/questions/306760/are-all-nonunitary-perfect-numbers-in-the-form-4k-where-k-is-an-even-perfect-num .
5. OEIS A064591, “Nonunitary perfect numbers,” originally indexed 25 September 2001, https://oeis.org/A064591 .
