# Superharmonic numbers with prime odd part are even perfect
## Finding
Let \(a\ge1\) and let \(p\) be an odd prime. Then \(n=2^a p\) is superharmonic if and only if \(a+1\) is prime and
\[
p=2^{a+1}-1
\]
is prime. Equivalently, among integers having exactly two distinct prime divisors and squarefree odd part, the superharmonic numbers are precisely the even perfect numbers. Their superharmonic index is \(1\).

## Assumptions and scope
For \(n>1\), write \(\tau(n)\) for the number of positive divisors and \(\sigma(n)\) for their sum. The integer \(n\) is superharmonic if
\[
\sigma(n)\mid n^k\tau(n)
\]
for some positive integer \(k\). The least such \(k\) is its index. The theorem concerns the natural two-prime slice in which the odd prime occurs to the first power. It does not classify \(2^a p^b\) when \(b>1\), nor odd superharmonic numbers.

Set \(A=a+1\) and \(M=2^A-1\). Then
\[
\tau(2^a p)=2A,
\qquad
\sigma(2^a p)=M(p+1).
\]
We use the elementary necessary condition from Cohen's Theorem 1: if \(r\) is prime and \(r\mid\sigma(n)\), then \(r\mid n\tau(n)\); moreover, if \(v_r(\sigma(n))>v_r(\tau(n))\), then \(r\mid n\).

## Proof
Assume first that \(n=2^a p\) is superharmonic. Let \(r\) be a prime divisor of \(M\). Since \(M\) is odd, \(r\ne2\). If \(r\ne p\), Cohen's first divisibility condition forces \(r\mid A\).

Let \(d=\operatorname{ord}_r(2)\). Because \(r\mid 2^A-1\), we have \(d\mid A\); also \(d\mid r-1\), so \(r\nmid d\). The lifting-the-exponent identity gives
\[
v_r(2^A-1)=v_r(2^d-1)+v_r(A/d)\ge 1+v_r(A).
\]
Thus
\[
v_r(\sigma(n))\ge v_r(M)>v_r(2A)=v_r(\tau(n)).
\]
Cohen's second condition would then require \(r\mid n\), contradicting \(r\ne p\). Hence every prime divisor of \(M\) is \(p\), so
\[
2^A-1=p^c
\]
for some integer \(c\ge1\).

Now let \(d=\operatorname{ord}_p(2)\). Again \(d\mid A\). Suppose \(d<A\), and put \(m=A/d>1\). Since every prime divisor of \(2^A-1\) is \(p\), there is an integer \(e\ge1\) with \(2^d-1=p^e\). Therefore
\[
Q=\frac{2^A-1}{2^d-1}=1+2^d+2^{2d}+\cdots+2^{(m-1)d}
\]
is a positive power of \(p\). Lifting the exponent once more gives
\[
v_p(Q)=v_p(m),
\]
so, because \(Q\) is a pure \(p\)-power,
\[
Q=p^{v_p(m)}\le m.
\]
But the displayed geometric sum has \(m\) positive terms, with all but the first greater than \(1\), so \(Q>m\), a contradiction. Hence
\[
\operatorname{ord}_p(2)=A.
\]
In particular, \(A\mid p-1\).

Let \(s\) be an odd prime divisor of \(p+1\). Since \(s\mid\sigma(n)\), Cohen's first condition gives \(s\mid n\tau(n)\). The prime \(s\) is neither \(2\) nor \(p\), so \(s\mid A\). But \(A\mid p-1\), hence \(s\mid p-1\) as well, contradicting \(\gcd(p-1,p+1)=2\). Therefore \(p+1\) is a power of \(2\): write
\[
p=2^u-1.
\]
Since \(p\) is prime, \(u\) is prime. The multiplicative order of \(2\) modulo \(p\) is then \(u\); comparing with \(\operatorname{ord}_p(2)=A\) yields \(u=A\). Consequently \(p=2^A-1=M\), so \(c=1\), and both \(A=a+1\) and \(p\) are prime.

Conversely, if \(A=a+1\) and \(p=2^A-1\) are prime, then \(2^a p\) is an even perfect number. Hence \(\sigma(n)=2n\), while \(\tau(n)=2A\), so \(\sigma(n)\mid n\tau(n)\). Thus \(n\) is harmonic, and therefore superharmonic of index \(1\).

## Verification
The proof is symbolic. The bundled `verify.py` independently factors the exact divisor-sum and divisor-count expressions for all \(1\le a\le20\) and all odd primes \(p\le200000\), applies the defining superharmonic divisibility condition, and compares every hit with the theorem. Its expected output is

`VERIFY_OK a_max=20 p_bound=200000 hits=[(1, 3, 1), (2, 7, 1), (4, 31, 1), (6, 127, 1), (12, 8191, 1), (16, 131071, 1)]`

This finite computation is corroborative only; the unrestricted classification is established by the proof above.

## Relationship to prior work
Cohen introduced superharmonic numbers and proved the prime-support/valuation criterion used above. Immediately after that theorem, he noted that the classical proof classifying harmonic numbers with two distinct prime factors does not carry over to superharmonic numbers, although the same classification appears to be true. The present result proves that expected classification on the infinite subfamily with squarefree odd part.

Pollack and Pomerance later obtained global distribution bounds for superharmonic numbers and discussed the narrower prime-deficient and prime-perfect conditions. Their results do not classify the present \(2^a p\) slice: prime-perfectness is strictly stronger than superharmonicity, while the superharmonic counting theorem is global rather than a two-prime structural converse.

## Limitations
The argument uses essentially that the odd part is a single prime. When an odd prime occurs with exponent greater than \(1\), the extra factor in \(\tau(n)\) can absorb new prime divisors of \(\sigma(n)\), so the proof does not extend formally. No claim is made about the full two-distinct-prime-factor question or the existence of odd superharmonic numbers.

## References
1. G. L. Cohen, “Superharmonic numbers,” *Mathematics of Computation* 78 (2009), 421–429. DOI: 10.1090/S0025-5718-08-02147-9. Electronically published 2008-09-05.
2. P. Pollack and C. Pomerance, “Prime-perfect numbers,” *Integers* 12 (2012), 1417–1437. DOI: 10.1515/integers-2012-0044.
