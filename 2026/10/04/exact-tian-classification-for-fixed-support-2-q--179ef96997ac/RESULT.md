# Exact Tian classification for fixed support \(\{2,q\}\)
## Finding
Fix an odd prime \(q\). For positive integers \(n,\alpha,\beta\), the equation
\[
\binom{n+1}{2}=2^{\alpha}q^{\beta}
\]
has exactly the following solutions.

* If \(q=2^A-1\) is prime for some integer \(A\ge 2\), then
  \[
  (n,\alpha,\beta)=(q,A-1,1).
  \]
* If \(q=2^A+1\) is prime for some integer \(A\ge 2\), then
  \[
  (n,\alpha,\beta)=(q-1,A-1,1).
  \]
  Primality here forces \(A\) to be a power of two.
* There is one further solution, namely
  \[
  (q,n,\alpha,\beta)=(3,8,2,2).
  \]

There are no others. Hence the fixed prime support \(\{2,q\}\) satisfies the two-prime Tian bound of at most two solutions. Equality occurs exactly for \(q=3\); for every \(q>3\) there is at most one solution.

## Assumptions and scope
The exponents \(\alpha\) and \(\beta\) are strictly positive, as in Tian's conjecture, and \(q\) is an odd prime. Put \(A=\alpha+1\), so \(A\ge2\). This theorem classifies only the fixed-support family containing the prime \(2\); it does not settle arbitrary pairs of odd primes.

## Proof
Multiplying the defining equation by \(2\) gives
\[
n(n+1)=2^Aq^\beta.
\]
Because \(\gcd(n,n+1)=1\), the two prime-power supports cannot be split between the two consecutive factors. Since both exponents are positive, the unordered pair \(\{n,n+1\}\) is exactly \(\{2^A,q^\beta\}\). Thus one of the two equations
\[
q^\beta=2^A+1,\qquad q^\beta=2^A-1
\]
must hold.

First suppose \(q^\beta=2^A+1\). If \(\beta>1\) is odd, then
\[
q^\beta-1=(q-1)(1+q+\cdots+q^{\beta-1})=2^A.
\]
The second factor is an odd integer greater than \(1\), impossible for a power of two. If \(\beta\) is even, write \(\beta=2c\). Then
\[
(q^c-1)(q^c+1)=2^A.
\]
Both factors are powers of two and differ by \(2\), so they must be \(2\) and \(4\). Hence \(q^c=3\), giving \(q=3\), \(c=1\), \(\beta=2\), and \(A=3\). This yields \((n,\alpha,\beta)=(8,2,2)\). The only remaining possibility is \(\beta=1\), so \(q=2^A+1\). If \(A\) had an odd divisor greater than one, writing \(A=2^s d\) with odd \(d>1\) would factor \((2^{2^s})^d+1\); therefore primality forces \(A\) to be a power of two. Here \(n=2^A=q-1\) and \(\alpha=A-1\).

Now suppose \(q^\beta=2^A-1\). If \(\beta\) is even, then \(q^\beta\equiv1\pmod 8\), so \(2^A=q^\beta+1\equiv2\pmod8\), impossible for \(A\ge2\). If \(\beta>1\) is odd, then
\[
q^\beta+1=(q+1)(q^{\beta-1}-q^{\beta-2}+\cdots-q+1)=2^A,
\]
and the second factor is an odd integer greater than \(1\), again impossible. Hence \(\beta=1\), so \(q=2^A-1\), \(n=q\), and \(\alpha=A-1\). Primality of \(2^A-1\) forces \(A\) to be prime.

For \(q=3\), the minus branch with \(A=2\) gives \((n,\alpha,\beta)=(3,1,1)\), while the even-exponent plus branch gives \((8,2,2)\). If \(q>3\), the plus and minus prime branches cannot both occur: equality \(2^B+1=2^A-1\) with \(B\ge2\) would force a positive multiple of \(4\) to equal \(2\). Thus the stated count follows.

## Verification
The proof is reversible at every step. The accompanying `verify.py` checks the two reduced exponential equations for every odd prime \(q<5000\), every \(2\le A<25\), and every \(1\le\beta<9\), and separately scans all \(2\le n\le200000\) for triangular numbers with exact support \(\{2,q\}\). It returns `VERIFY_OK structural=245824 direct=11 q3=2`.

The finite checks are regression tests only; the global theorem rests on the factorization and parity arguments above.

## Relationship to prior work
Zeng, Pintér, Fu, and Tian formulate Tian's conjecture for fixed prime factors and prove a general absolute upper bound of four solutions in the two-prime case via \(S\)-unit equations and Zsigmondy's theorem. Their article explicitly states that a general proof of the conjectured two-solution bound remains beyond their results. The present theorem resolves exactly the natural subfamily in which one prescribed prime is \(2\), improving the general four-solution bound to the conjectured two and classifying every solution. The mechanism is special to the unique even prime: coprimality of consecutive integers forces the two factors to be pure prime powers.

Targeted searches for the exact equation and its Fermat/Mersenne reformulations did not identify a published statement implying this classification. That search result is not itself a novelty proof; differently phrased or unindexed prior work remains possible.

## Limitations
The theorem does not address fixed supports consisting of two odd primes. It also does not claim that infinitely many Mersenne or Fermat primes exist. The exhaustive computation is bounded and is not used as an infinite proof. Bibliographic completeness cannot be guaranteed for elementary observations that may appear under different terminology.

## References
1. Z. Zeng, Á. Pintér, X. Fu, and J. P. Tian, “Tian’s Conjecture on the Prime Factorization of the Binomial Coefficient,” *Mathematics* 14 (2026), 127. DOI: 10.3390/math14010127. Publicly published 29 December 2025. Primary MSC 11D61.
