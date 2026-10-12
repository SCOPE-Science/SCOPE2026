# The first two multiplicity layers of consecutive equal totients
## Finding
Let \(\Omega(m)\) denote the number of prime factors of \(m\), counted with multiplicity. For every integer
\[
n\ge2,
\]
if
\[
\varphi(n)=\varphi(n+1)
\]
and
\[
\Omega(n)\le2,\qquad \Omega(n+1)\le2,
\]
then
\[
n=3.
\]

Equivalently,
\[
(3,4)
\]
is the unique consecutive equal-totient pair in which both members are prime or semiprime when prime squares are counted as semiprimes in the multiplicity sense. Consequently every solution
\[
n>3
\]
of
\[
\varphi(n)=\varphi(n+1)
\]
satisfies
\[
\max\{\Omega(n),\Omega(n+1)\}\ge3.
\]

## Assumptions and scope
Here \(\varphi\) is Euler's totient function and \(\Omega(m)\) counts prime factors with multiplicity. Thus \(\Omega(m)\le2\) means that \(m\) is either prime, a square of a prime, or a product of two distinct primes; the integer \(1\) is outside the stated range \(n\ge2\).

The theorem classifies only the first two multiplicity layers. It does not claim a classification when one member has three or more prime factors, nor does it address the unresolved global questions surrounding
\[
\varphi(n)=\varphi(n+1).
\]

## Proof
Directly,
\[
\varphi(2)=1,\qquad \varphi(3)=\varphi(4)=2,\qquad \varphi(4)=2\ne4=\varphi(5),
\]
so among
\[
n\in\{2,3,4\}
\]
only \(n=3\) is a solution.

Assume now
\[
n\ge5.
\]
Let \(e\) be the even member of the consecutive pair \(\{n,n+1\}\), and let \(o\) be the odd member. Since
\[
e>4,\qquad \Omega(e)\le2,
\]
the even integer \(e\) cannot be a prime and cannot be a power \(2^2\). Therefore
\[
e=2r
\]
for an odd prime \(r\). Hence
\[
\varphi(e)=r-1.
\]

Because \(o\) is odd and \(\Omega(o)\le2\), exactly three forms are possible.

First suppose
\[
o=s
\]
for an odd prime \(s\). Equality of totients gives
\[
s-1=r-1,
\]
so \(s=r\). But \(e\) and \(o\) are consecutive, hence
\[
2r=r\pm1,
\]
which is impossible for a prime \(r\).

Next suppose
\[
o=s^2
\]
for an odd prime \(s\). Then
\[
r-1=\varphi(s^2)=s(s-1),
\]
so
\[
r=s^2-s+1.
\]
If
\[
e=o+1,
\]
then
\[
2(s^2-s+1)=s^2+1,
\]
and therefore
\[
(s-1)^2=0,
\]
impossible for a prime \(s\). If instead
\[
e=o-1,
\]
then
\[
2(s^2-s+1)=s^2-1,
\]
so
\[
s^2-2s+3=0.
\]
Its discriminant is \(-8\), again impossible.

Finally suppose
\[
o=ab
\]
with distinct odd primes
\[
a<b.
\]
Then
\[
r-1=(a-1)(b-1),
\]
hence
\[
r=ab-a-b+2.
\]
If
\[
e=o+1,
\]
the relation
\[
2r=ab+1
\]
reduces to
\[
ab-2a-2b+3=0,
\]
or equivalently
\[
(a-2)(b-2)=1.
\]
Since \(a,b\ge3\), this forces
\[
a=b=3,
\]
contrary to their distinctness.

If
\[
e=o-1,
\]
then
\[
2r=ab-1,
\]
which reduces to
\[
ab-2a-2b+5=0,
\]
or
\[
(a-2)(b-2)=-1.
\]
The left side is positive, a contradiction.

All possible forms of the odd member are exhausted. Thus no solution with \(n\ge5\) has both multiplicities at most \(2\), and the direct check leaves only
\[
n=3.
\]

## Verification
The accompanying checker computes \(\varphi(m)\) and \(\Omega(m)\) independently by a sieve through \(2{,}000{,}000\). It confirms that the only
\[
n\le2{,}000{,}000
\]
with
\[
\varphi(n)=\varphi(n+1),\qquad \Omega(n)\le2,\qquad\Omega(n+1)\le2
\]
is \(n=3\).

This finite computation is corroborative only. The unrestricted theorem is proved by the exhaustive parity and factorization argument above.

## Relationship to prior work
The equation
\[
\varphi(n)=\varphi(n+1)
\]
is classical. Graham, Holt and Pomerance studied the more general shifted equation
\[
\varphi(n)=\varphi(n+k)
\]
and, for \(k=1\), reported extensive computation while developing general structural and asymptotic questions. Their complete paper does not state a classification of solutions by the condition
\[
\Omega(n),\Omega(n+1)\le2.
\]

Bayless and Kinlaw later studied consecutive coincidences directly. Their article was published on 2 October 2015 and is classified primarily under MSC \(11N25\). The accessible publisher preview establishes the exact equation and the paper's global counting focus; because the full article was not available in this review, no whole-document noncoverage claim is made for that source.

Kinlaw, Kobayashi and Pomerance subsequently improved global bounds for the reciprocal sum of solutions and carried out much larger computation. Inspection of the complete paper shows a global analytic and computational treatment, not a first-two-multiplicity-layer theorem.

OEIS A001274 records the solution sequence beginning
\[
1,3,15,104,164,194,\ldots
\]
and extensive bounded computations. A list of solutions, however large, does not imply the unrestricted low-multiplicity classification proved here.

## Limitations
The theorem does not classify solutions once one of the consecutive integers has at least three prime factors counted with multiplicity. In particular, it gives no statement about the frequency, infinitude, or higher-\(\Omega\) structure of all solutions.

The 2015 Bayless--Kinlaw article was inspected through its publisher preview rather than complete full text. That access limitation is retained as an originality risk instead of being treated as evidence of noncoverage.

The exact public date stored in metadata is the earliest exact calendar date verified here for an archival source used to anchor this question. Older literature exists, but the inspected records for those older sources did not provide an exact public calendar day suitable for the date field.

## References
1. S. W. Graham, J. J. Holt and C. Pomerance, "On the solutions to \(\varphi(n)=\varphi(n+k)\)", in *Number Theory in Progress*, Vol. 2, de Gruyter, 1999, pp. 867--882.
2. J. Bayless and P. Kinlaw, "Consecutive coincidences of Euler's function", *International Journal of Number Theory* 12 (2016), 1011--1026, DOI 10.1142/S1793042116500639; published online 2 October 2015.
3. P. Kinlaw, M. Kobayashi and C. Pomerance, "On the equation \(\varphi(n)=\varphi(n+1)\)", *Acta Arithmetica* 196 (2020), 69--92.
4. OEIS Foundation, A001274, "Numbers \(k\) such that \(\varphi(k)=\varphi(k+1)\)".
