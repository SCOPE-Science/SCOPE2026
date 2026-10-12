# Complete two-factor classification for a divisor-sum–totient divisibility
## Finding
Let \(\sigma\) be the sum-of-divisors function, let \(\varphi\) be Euler's totient, and let \(\Omega(n)\) count prime factors with multiplicity.

Among the positive integers satisfying
\[
\sigma(n)\mid n\varphi(n),
\]
the complete layer
\[
\Omega(n)=2
\]
consists exactly of
\[
n=6
\]
and the squarefree semiprimes
\[
n=pq,\qquad 3\le p<q,\qquad q=p^2-p-1,
\]
for which \(p\) and \(q\) are both prime.

No prime square is a solution. For every odd-prime solution pair,
\[
\frac{n\varphi(n)}{\sigma(n)}=q(p-2).
\]

The first odd-prime examples are
\[
15=3\cdot5,\quad
95=5\cdot19,\quad
287=7\cdot41,\quad
1199=11\cdot109,\quad
4607=17\cdot271.
\]

## Assumptions and scope
The theorem classifies only the exact multiplicative-complexity layer
\[
\Omega(n)=2.
\]
Thus \(n\) is either a prime square or a product of two distinct primes.

The underlying divisibility set is OEIS A066995, defined by
\[
\sigma(n)\mid n\varphi(n).
\]
No claim is made here about integers with three or more prime factors, or about whether the polynomial
\[
p^2-p-1
\]
is prime for infinitely many primes \(p\).

## Proof
Let
\[
\Omega(n)=2
\]
and suppose
\[
\sigma(n)\mid n\varphi(n).
\tag{1}
\]

First consider a prime square
\[
n=p^2.
\]
Then
\[
\sigma(p^2)=p^2+p+1
\]
and
\[
n\varphi(n)=p^3(p-1).
\]
Since
\[
\gcd(p,p^2+p+1)=1,
\]
condition (1) would force
\[
p^2+p+1\mid p-1,
\]
which is impossible. Hence every solution in this layer is squarefree.

Write now
\[
n=pq
\]
with primes
\[
p<q.
\]
Then
\[
\sigma(n)=(p+1)(q+1)
\]
and
\[
n\varphi(n)=pq(p-1)(q-1).
\tag{2}
\]

Suppose first that
\[
p=2.
\]
From (2), divisibility by \(q+1\) gives
\[
q+1\mid 2(q-1).
\]
Therefore
\[
q+1\mid4.
\]
As \(q\ge3\) is prime, this forces
\[
q=3.
\]
Conversely, \(n=6\) satisfies (1).

It remains to suppose that \(p\) and \(q\) are odd. Since
\[
q+1\mid pq(p-1)(q-1)
\]
and
\[
\gcd(q+1,q)=1,\qquad \gcd(q+1,q-1)=2,
\]
we obtain
\[
\frac{q+1}{2}\mid p(p-1).
\tag{3}
\]
Put
\[
m=\frac{q+1}{2}.
\]
Because \(q>p\),
\[
m>\frac p2.
\]

If \(p\nmid m\), then (3) gives
\[
m\mid p-1.
\]
Every proper divisor of \(p-1\) is at most
\[
\frac{p-1}{2}<\frac p2,
\]
so necessarily
\[
m=p-1.
\]
Thus
\[
q=2p-3.
\]
Using (2), the required quotient would be
\[
\frac{pq(p-1)(q-1)}{(p+1)(q+1)}
=
\frac{pq(p-2)}{p+1}.
\]
Modulo \(p+1\), the numerator is congruent to
\[
(-1)(-5)(-3)=-15.
\]
Hence \(p+1\mid15\), impossible because \(p+1\) is an even integer at least \(4\).

Therefore
\[
p\mid m.
\]
Write
\[
m=pa,\qquad p-1=ab,
\]
with positive integers \(a,b\). Then
\[
p=ab+1,\qquad q=2pa-1.
\tag{4}
\]
Substituting (4) into (2), the divisibility is equivalent to
\[
p+1\mid qb(pa-1).
\tag{5}
\]
Modulo
\[
p+1=ab+2,
\]
one has
\[
q\equiv-2a-1,\qquad pa-1\equiv-a-1.
\]
Thus (5) is equivalent to
\[
ab+2\mid b-4a-6.
\tag{6}
\]

If
\[
b-4a-6>0,
\]
then
\[
0<b-4a-6<ab+2,
\]
contradicting (6). If
\[
b-4a-6=0,
\]
then
\[
b=4a+6
\]
and (4) gives
\[
q=(2a+1)(4a^2+4a-1),
\]
which is composite.

We may therefore write
\[
4a+6-b=t(ab+2)
\]
for a positive integer \(t\). Equivalently,
\[
b(1+ta)=4a+6-2t.
\tag{7}
\]

If \(t\ge3\), then (7) gives
\[
b<\frac43,
\]
so \(b=1\). It follows that
\[
t=\frac{4a+5}{a+2}=4-\frac3{a+2}.
\]
The only positive integral possibility is
\[
a=1,\qquad t=3,
\]
which gives \(p=2\), contrary to the present odd-prime case.

If \(t=1\), then (7) gives
\[
b=4.
\]
Consequently
\[
q=(2a+1)(4a-1),
\]
again composite.

Finally, if \(t=2\), equation (7) gives
\[
b=2.
\]
Hence
\[
p=2a+1
\]
and
\[
q=2pa-1=p^2-p-1.
\]

This proves necessity.

Conversely, let \(p\) be an odd prime and suppose
\[
q=p^2-p-1
\]
is prime. Then
\[
q+1=p(p-1)
\]
and
\[
q-1=(p+1)(p-2).
\]
Therefore
\[
\sigma(pq)=(p+1)(q+1)=p(p-1)(p+1),
\]
whereas
\[
pq\,\varphi(pq)=pq(p-1)(q-1)
=pq(p-1)(p+1)(p-2).
\]
Hence
\[
\frac{pq\,\varphi(pq)}{\sigma(pq)}=q(p-2)\in\mathbb Z.
\]
Together with \(n=6\), this completes the classification.

## Verification
The attached `verify.py` performs exact finite checks independent of the symbolic case split.

It exhaustively examines every integer
\[
2\le n\le5{,}000{,}000
\]
with
\[
\Omega(n)=2,
\]
computes \(\sigma(n)\) and \(\varphi(n)\) from the prime factorization, and compares direct divisibility against the theorem's criterion. It also checks the polynomial branch for primes in the tested range and confirms that no prime square is accepted.

The finite computation is corroborative only. The universal classification follows from the proof above.

## Relationship to prior work
OEIS A066995 is the exact database set defined by
\[
\sigma(n)\mid n\varphi(n).
\]
Its entry gives terms, computational programs, and cross-references, but no structural characterization of the complete \(\Omega(n)=2\) layer.

The closely related OEIS A011775 reverses the outer divisibility and asks for
\[
n\mid\varphi(n)\sigma(n).
\]
That is a different condition. Its known local criterion and infinite families do not imply the present classification.

De Koninck and Luca study the interaction of \(\sigma\) and \(\varphi\) through the composition quotient
\[
H(n)=\frac{\sigma(\varphi(n))}{\varphi(\sigma(n))}.
\]
Their paper provides primary subject classification \(11A25\) and broad distributional context for the same two classical arithmetic functions, but its stated theorems concern orders, averages, and densities of \(H\), not the divisibility defining A066995. Full-text searches located no semiprime theorem for the present condition.

Targeted database, literature, and semantic-result searches for the exact divisibility, its semiprime restriction, and the polynomial
\[
p^2-p-1
\]
found no equivalent or stronger statement.

## Limitations
The theorem does not classify solutions with
\[
\Omega(n)\ge3.
\]
It also does not establish that there are infinitely many odd-prime solution pairs, because that would require infinitely many primes \(p\) for which
\[
p^2-p-1
\]
is prime.

The principal originality risk is an unindexed elementary observation or problem solution involving A066995. The exact database entry and the inspected arithmetic-function literature do not expose such a classification.

## References
1. OEIS Foundation, A066995, “Numbers \(k\) such that \(\sigma(k)\) divides \(k\varphi(k)\),” entry authored 27 January 2002.
2. J.-M. De Koninck and F. Luca, “On the composition of the Euler function and the sum of divisors function,” *Colloquium Mathematicum* 108 (2007), 31–51, DOI 10.4064/cm108-1-4.
3. OEIS Foundation, A011775, “Numbers \(k\) such that \(k\) divides \(\varphi(k)\sigma(k)\).”
