# The first total-multiplicity layer of the exceptional quotient-four totient problem
## Finding
Let
\[
R_4=\{n\ge1:\sigma(n)=4\varphi(n)\},
\]
where \(\sigma\) is the sum-of-divisors function and \(\varphi\) is Euler's totient. Let \(\Omega(n)\) count prime factors with multiplicity.

Among even integers in \(R_4\), the complete list with
\[
\Omega(n)\le3
\]
is
\[
14=2\cdot7
\]
and
\[
418=2\cdot11\cdot19.
\]

Equivalently,
\[
n\in R_4,\qquad 2\mid n,\qquad \Omega(n)\le3
\]
if and only if
\[
n\in\{14,418\}.
\]

Thus every other even solution of
\[
\sigma(n)=4\varphi(n)
\]
has at least four prime factors counted with multiplicity.

## Assumptions and scope
For a positive integer \(n\),
\[
\sigma(n)=\sum_{d\mid n}d
\]
and
\[
\varphi(n)=n\prod_{p\mid n}\left(1-\frac1p\right).
\]
The function \(\Omega(n)\) counts prime factors with multiplicity.

The result treats only the even quotient-four equation
\[
\sigma(n)=4\varphi(n)
\]
under the total-multiplicity restriction \(\Omega(n)\le3\). It does not classify the full even \(R_4\) family, which contains many solutions of higher multiplicative complexity.

## Proof
Assume that \(n\) is even,
\[
\Omega(n)\le3,
\]
and
\[
\sigma(n)=4\varphi(n).
\]

There are three possible support sizes.

First suppose \(n\) is a power of \(2\). Then
\[
n=2^a,\qquad 1\le a\le3.
\]
The equation becomes
\[
2^{a+1}-1=4\cdot2^{a-1}=2^{a+1},
\]
which is impossible.

Now suppose \(n\) has exactly two distinct prime factors. Since \(n\) is even and \(\Omega(n)\le3\), it has one of the forms
\[
2p,\qquad 4p,\qquad 2p^2,
\]
where \(p\) is an odd prime.

For
\[
n=2p,
\]
the equation is
\[
3(p+1)=4(p-1),
\]
so
\[
p=7
\]
and
\[
n=14.
\]

For
\[
n=4p,
\]
the equation is
\[
7(p+1)=8(p-1),
\]
which gives
\[
p=15,
\]
not a prime.

For
\[
n=2p^2,
\]
the equation is
\[
3(p^2+p+1)=4p(p-1).
\]
Hence
\[
p^2-7p-3=0.
\]
Its discriminant is
\[
61,
\]
which is not a square, so no integer \(p\) occurs.

It remains to consider exactly three distinct prime factors. The bound
\[
\Omega(n)\le3
\]
then forces \(n\) to be squarefree. Thus
\[
n=2pq
\]
for odd primes
\[
p<q.
\]
Using multiplicativity,
\[
\sigma(2pq)=3(p+1)(q+1)
\]
and
\[
\varphi(2pq)=(p-1)(q-1).
\]
Therefore the quotient-four equation is
\[
3(p+1)(q+1)=4(p-1)(q-1).
\]
After expansion,
\[
pq-7p-7q+1=0,
\]
or equivalently
\[
(p-7)(q-7)=48.
\tag{1}
\]

If both primes were below \(7\), the only ordered pair with \(p<q\) would be among \(3,5\), and (1) would fail. Thus the two factors in (1) are positive.

The positive factor pairs of \(48\), ordered with the smaller first, are
\[
(1,48),\ (2,24),\ (3,16),\ (4,12),\ (6,8).
\]
Adding \(7\) to each coordinate gives
\[
(8,55),\ (9,31),\ (10,23),\ (11,19),\ (13,15).
\]
Only
\[
(11,19)
\]
consists of two primes. Hence
\[
n=2\cdot11\cdot19=418.
\]

Direct substitution gives
\[
\sigma(14)=24=4\varphi(14)
\]
and
\[
\sigma(418)=720=4\varphi(418).
\]
This proves the classification.

## Verification
The accompanying checker factors every integer
\[
2\le n<200000
\]
exactly, filters to even \(n\) with
\[
\Omega(n)\le3,
\]
and evaluates \(\sigma(n)\) and \(\varphi(n)\) from the prime factorization. It finds exactly
\[
14,\ 418.
\]

The checker separately enumerates every positive factor pair of \(48\) and verifies that only
\[
(4,12)
\]
produces primes after adding \(7\), giving
\[
(p,q)=(11,19).
\]

The bounded computation is corroborative only. The proof above exhausts all factorization types allowed by \(\Omega(n)\le3\).

## Relationship to prior work
Broughan and Zhou study the sets
\[
R_a=\{n:\sigma(n)=a\varphi(n)\}
\]
and identify the even quotient-four case with three distinct prime factors as the exceptional unresolved part of their low-support classification. They completely characterize the even \(R_4\) solutions with two distinct prime factors and list many even three-support examples, beginning with
\[
418=2\cdot11\cdot19.
\]
They state that the full even three-support quotient-four case remained unresolved.

The present result imposes the different and strictly sharper size-of-factorization boundary
\[
\Omega(n)\le3.
\]
At three distinct prime supports this forces squarefreeness, and the unresolved equation collapses to the single factorization
\[
(p-7)(q-7)=48.
\]
Thus the first total-multiplicity layer of the exceptional branch is completely determined.

The exact database A068390 lists the solutions of
\[
\sigma(n)=4\varphi(n)
\]
and begins
\[
14,105,248,418,1485,3135,\ldots.
\]
This confirms the two surviving values in their ambient sequence, but a finite database does not prove that no later term has \(\Omega(n)\le3\).

## Limitations
The theorem does not settle the full even \(R_4\) problem with three distinct prime factors. In particular, solutions such as
\[
3596=2^2\cdot29\cdot31
\]
lie immediately beyond the boundary because
\[
\Omega(3596)=4.
\]

The originality comparison is limited to the inspected primary paper, exact database, targeted statement searches, and indexed research records. An equivalent low-total-multiplicity observation in unindexed notes remains a residual risk.

## References
1. K. A. Broughan and Q. Zhou, “On the Ratio of the Sum of Divisors and Euler's Totient Function II,” *Journal of Integer Sequences* 17 (2014), Article 14.9.2, published 12 August 2014.
2. OEIS Foundation, A068390, “Numbers \(k\) such that \(\sigma(k)=4\varphi(k)\).”
