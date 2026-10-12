# Prime-square exponent rigidity for unitary–exponential divisor-sum equality
## Finding
Let \(\sigma^{*}\) denote the sum of unitary divisors and \(\sigma^{(e)}\) the sum of exponential divisors. If \(\ell\) is an odd prime and \(p,q\) are distinct primes, then
\[
\sigma^{*}\!\left(p^{\ell^2}q\right)=\sigma^{(e)}\!\left(p^{\ell^2}q\right)
\]
holds if and only if
\[
p=2
\]
and
\[
q=\Phi_{2\ell^2}(2)
=\frac{2^{\ell^2}+1}{2^\ell+1}
\]
is prime.

Thus the entire prime-square exponent stratum reduces to primality of one explicit cyclotomic value.

For the first three odd prime exponents,
\[
\ell=3:\ q=57=3\cdot19,
\]
\[
\ell=5:\ q=1016801=251\cdot4051,
\]
and
\[
\ell=7:\ q=4363953127297,
\]
with the last value prime. Hence the first solution on this ray is
\[
2^{49}\cdot4363953127297.
\]

## Assumptions and scope
For a prime power \(r^a\),
\[
\sigma^{*}(r^a)=1+r^a.
\]
An exponential divisor of \(r^a\) has the form \(r^d\) with \(d\mid a\), so
\[
\sigma^{(e)}(r^a)=\sum_{d\mid a}r^d.
\]
Both functions are multiplicative.

The theorem treats integers having exactly two distinct prime factors, with one prime occurring to exponent \(\ell^2\) for an odd prime \(\ell\), and the other occurring to exponent \(1\). It does not classify arbitrary exponents or arbitrary two-prime exponent pairs.

## Proof
Put
\[
a=\ell^2
\]
and
\[
n=p^a q.
\]
Because \(\ell\) is prime, the positive divisors of \(a\) are
\[
1,\ \ell,\ \ell^2.
\]
Therefore
\[
\sigma^{(e)}(p^a)=p+p^\ell+p^a,
\qquad
\sigma^{(e)}(q)=q,
\]
while
\[
\sigma^{*}(p^a)=1+p^a,
\qquad
\sigma^{*}(q)=1+q.
\]

Hence equality of the two divisor sums is equivalent to
\[
(1+p^a)(1+q)=q(p+p^\ell+p^a).
\]
After cancelling the common term \(q(1+p^a)\), this becomes
\[
p^a+1=q\left(p+p^\ell-1\right).
\tag{1}
\]

Set
\[
D=p+p^\ell-1.
\]
Equation (1) requires
\[
D\mid p^{\ell^2}+1.
\]

Suppose first that \(p>2\). Modulo \(D\),
\[
p^\ell\equiv1-p.
\]
Since \(\ell\) is odd,
\[
p^{\ell^2}+1
=(p^\ell)^\ell+1
\equiv(1-p)^\ell+1
=1-(p-1)^\ell
\pmod D.
\]
The residue
\[
R=1-(p-1)^\ell
\]
is nonzero, and
\[
|R|=(p-1)^\ell-1.
\]
But
\[
D-|R|
=
p^\ell-(p-1)^\ell+p
>0.
\]
Thus
\[
0<|R|<D,
\]
so \(D\) cannot divide \(p^{\ell^2}+1\). Therefore \(p>2\) is impossible.

Consequently
\[
p=2.
\]
Now
\[
D=2^\ell+1.
\]
Because \(\ell\) is odd,
\[
2^{\ell^2}+1=(2^\ell)^\ell+1
\]
is divisible by \(2^\ell+1\). Equation (1) therefore forces
\[
q=\frac{2^{\ell^2}+1}{2^\ell+1}.
\tag{2}
\]
For odd prime \(\ell\), the cyclotomic factorization gives
\[
\frac{x^{\ell^2}+1}{x^\ell+1}=\Phi_{2\ell^2}(x),
\]
so (2) is exactly
\[
q=\Phi_{2\ell^2}(2).
\]

Conversely, if this cyclotomic value is prime, then substituting (2) into (1) gives equality of the two divisor sums. Since the quotient is odd and greater than \(2\), the two primes are distinct.

This proves the equivalence.

## Verification
The attached checker verifies the algebraic reduction over many prime parameters using exact integer arithmetic. It confirms for odd primes
\[
3\le\ell\le31
\]
and primes
\[
3\le p\le97
\]
that
\[
p+p^\ell-1
\]
does not divide
\[
p^{\ell^2}+1,
\]
and checks the displayed strict remainder bound.

For \(p=2\), it verifies exact divisibility and the quotient identity for every tested odd prime \(\ell\). It also confirms
\[
57=3\cdot19,
\qquad
1016801=251\cdot4051,
\]
and deterministically verifies primality of
\[
4363953127297.
\]
Finally, it evaluates both divisor-sum formulas directly at
\[
2^{49}\cdot4363953127297
\]
and confirms equality.

These computations are corroborative only. The proof above is uniform in \(\ell,p,q\).

## Relationship to prior work
Trudgian's paper studies \(\sigma^{*}\), compares it with \(\sigma^{(e)}\), and asks whether equality occurs infinitely often. Its conclusion records only finitely many known equality examples, including
\[
2^{49}\cdot4363953127297.
\]
The paper does not give a structural explanation for that exponent-\(49\) example or classify prime-square exponent strata.

The exact sequence A236474 tabulates integers satisfying
\[
\sigma^{*}(n)=\sigma^{(e)}(n)
\]
and includes the same very large example among known terms. A finite list does not imply the theorem here.

A separate finite classification through exponent \(49\) covers the cases \(\ell=3,5,7\), but does not imply the unbounded statement for prime-square exponents \(\ell^2\) with \(\ell\ge11\). The present proof supplies the missing uniform reduction:
\[
p=2,\qquad q=\Phi_{2\ell^2}(2).
\]

## Limitations
The theorem does not prove that infinitely many values
\[
\Phi_{2\ell^2}(2)
\]
are prime, so it does not settle the general infinitude question for equality of the two divisor sums.

It also does not classify exponents that are not squares of odd primes, nor cases in which both prime exponents exceed \(1\).

The originality comparison covered the primary full text, the exact OEIS sequence, targeted statement searches, and the closest indexed finite classification. An equivalent unindexed observation remains a residual risk.

## References
1. T. Trudgian, “The sum of the unitary divisor function,” arXiv:1312.4615v1, first public 17 December 2013; later *Publications de l'Institut Mathématique* 97(111) (2015), 175–180.
2. OEIS Foundation, A236474, “Numbers whose sum of unitary divisors is equal to the sum of exponential divisors.”
