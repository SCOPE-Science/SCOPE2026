# The first three multiplicity layers of an aliquot-sum/totient divisibility
## Finding
Let
\[
s(n)=\sigma(n)-n
\]
be the aliquot sum of \(n\). For every integer
\[
n>1,\qquad \Omega(n)\le3,
\]
one has
\[
\varphi(n)\mid s(n)
\]
if and only if
\[
n\in\{2,6,10,12,44\}.
\]

Equivalently, these are exactly the nontrivial members with at most three prime factors counted with multiplicity of the congruence sequence
\[
\sigma(n)\equiv n\pmod{\varphi(n)}.
\]

Consequently every member
\[
n>44
\]
has
\[
\Omega(n)\ge4.
\]
This lower bound is sharp, because
\[
90=2\cdot3^2\cdot5,\qquad \Omega(90)=4,
\]
and
\[
\sigma(90)-90=144=6\varphi(90).
\]

## Assumptions and scope
The functions are the ordinary sum-of-divisors function \(\sigma\), Euler's totient \(\varphi\), and the total prime-factor count \(\Omega\), with multiplicity.

The theorem classifies exactly the multiplicative-complexity range
\[
1\le\Omega(n)\le3.
\]
The integer \(1\), which also satisfies the congruence, is excluded by the hypothesis \(n>1\).

No claim is made about a complete classification for
\[
\Omega(n)\ge4.
\]

## Proof
Write
\[
s(n)=\sigma(n)-n.
\]

First suppose
\[
\Omega(n)=1.
\]
Then \(n=p\) is prime,
\[
s(p)=1,\qquad \varphi(p)=p-1.
\]
Thus
\[
\varphi(p)\mid s(p)
\]
holds exactly when
\[
p-1=1,
\]
so the unique solution is
\[
p=2.
\]

Now suppose
\[
\Omega(n)=2.
\]

If
\[
n=p^2,
\]
then
\[
s(n)=p+1,\qquad \varphi(n)=p(p-1).
\]
For \(p=2\), the two values are \(3\) and \(2\), so divisibility fails. For \(p\ge3\),
\[
p(p-1)>p+1,
\]
so divisibility again fails.

It remains to consider
\[
n=pq,\qquad p<q
\]
for distinct primes. Here
\[
s(n)=p+q+1
\]
and
\[
\varphi(n)=(p-1)(q-1).
\]
If divisibility holds, then
\[
(p-1)(q-1)\le p+q+1,
\]
or equivalently
\[
(p-2)(q-2)\le4.
\tag{1}
\]
If \(p\ge3\), condition (1) leaves only
\[
(p,q)=(3,5),
\]
but then
\[
\varphi(15)=8\nmid9=s(15).
\]
Hence \(p=2\). The divisibility becomes
\[
q-1\mid q+3,
\]
so
\[
q-1\mid4.
\]
Since \(q>2\) is prime,
\[
q\in\{3,5\},
\]
giving precisely
\[
n\in\{6,10\}.
\]

Finally suppose
\[
\Omega(n)=3.
\]
There are three factorization shapes.

For a prime cube
\[
n=p^3,
\]
one has
\[
s(n)=p^2+p+1,\qquad \varphi(n)=p^2(p-1).
\]
The case \(p=2\) gives \(7\) and \(4\), so it fails. For \(p\ge3\),
\[
p^2(p-1)\ge2p^2>p^2+p+1,
\]
so no prime cube is a solution.

Next take
\[
n=p^2q
\]
with distinct primes, where \(p\) is the repeated prime. Then
\[
s(n)=p^2+pq+p+q+1
\]
and
\[
\varphi(n)=p(p-1)(q-1).
\tag{2}
\]

If \(p=2\), condition (2) becomes
\[
2(q-1)\mid3q+7.
\]
Hence
\[
q-1\mid10.
\]
Since \(q\) is an odd prime, this forces
\[
q\in\{3,11\}.
\]
Both values work, giving
\[
n\in\{12,44\}.
\]

If \(p=3\), the necessary size inequality from (2) is
\[
6(q-1)\le4q+13,
\]
so
\[
q\le9.
\]
The distinct prime possibilities are
\[
q\in\{2,5,7\},
\]
and direct substitution gives respectively
\[
6\nmid21,\qquad24\nmid33,\qquad36\nmid41.
\]

Assume now
\[
p\ge5.
\]
The necessary inequality
\[
p(p-1)(q-1)\le p^2+pq+p+q+1
\]
is equivalent to
\[
q(p^2-2p-1)\le2p^2+1.
\tag{3}
\]
For \(p=5\), (3) gives \(q<4\), so
\[
q\in\{2,3\}.
\]
For \(p\ge7\),
\[
2p^2+1<3(p^2-2p-1),
\]
so (3) gives \(q<3\), hence \(q=2\).

If \(q=2\), then
\[
s(p^2q)=p^2+3p+3.
\]
Divisibility by
\[
\varphi(p^2q)=p(p-1)
\]
would force
\[
p\mid3,
\]
impossible for \(p\ge5\).

If \(q=3\), then
\[
s(p^2q)=(p+2)^2.
\]
Divisibility by
\[
\varphi(p^2q)=2p(p-1)
\]
would force
\[
p\mid4,
\]
again impossible for \(p\ge5\). Thus the only repeated-prime solutions are \(12\) and \(44\).

It remains to exclude the squarefree shape
\[
n=pqr,\qquad p<q<r.
\]
If \(p,q,r\) are all odd, then
\[
\sigma(n)=(p+1)(q+1)(r+1)
\]
is even while \(n\) is odd, so
\[
s(n)=\sigma(n)-n
\]
is odd. But
\[
\varphi(n)=(p-1)(q-1)(r-1)
\]
is even, so divisibility is impossible.

Hence a squarefree solution would have
\[
n=2qr,\qquad 3\le q<r
\]
with \(q,r\) odd primes. Then
\[
s(n)=qr+3q+3r+3
\]
and
\[
\varphi(n)=(q-1)(r-1).
\]
If \(\varphi(n)\mid s(n)\), then also
\[
(q-1)(r-1)\mid s(n)-\varphi(n)=4q+4r+2.
\tag{4}
\]
Since the right side of (4) is positive,
\[
(q-1)(r-1)\le4q+4r+2,
\]
which is equivalent to
\[
(q-5)(r-5)\le26.
\tag{5}
\]
If \(q\ge11\), the left side of (5) is at least
\[
6\cdot8=48,
\]
a contradiction. Thus
\[
q\in\{3,5,7\}.
\]

For \(q=3\), condition (4) gives
\[
2(r-1)\mid4r+14.
\]
Subtracting \(4(r-1)\) shows
\[
2(r-1)\mid18,
\]
which is impossible for an odd prime \(r>3\).

For \(q=5\), condition (4) gives
\[
4(r-1)\mid4r+22.
\]
Subtracting \(4(r-1)\) gives
\[
4(r-1)\mid26,
\]
impossible.

For \(q=7\), condition (4) implies
\[
r-1\mid4r+30,
\]
hence
\[
r-1\mid34.
\]
Because \(r>7\) is an odd prime, the only possible even divisor would give
\[
r-1=34,\qquad r=35,
\]
not prime. This excludes every squarefree three-prime case.

We have therefore proved that the only solutions with
\[
n>1,\qquad \Omega(n)\le3
\]
are
\[
2,\ 6,\ 10,\ 12,\ 44.
\]
Directly,
\[
\frac{s(2)}{\varphi(2)}=1,\quad
\frac{s(6)}{\varphi(6)}=3,\quad
\frac{s(10)}{\varphi(10)}=2,\quad
\frac{s(12)}{\varphi(12)}=4,\quad
\frac{s(44)}{\varphi(44)}=2.
\]
Finally,
\[
\frac{s(90)}{\varphi(90)}=\frac{144}{24}=6,
\]
so the lower bound \(\Omega(n)\ge4\) for any further member is sharp.

## Verification
The attached `verify.py` independently factors every integer
\[
2\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)\le3,
\]
computes \(\sigma(n)\) and \(\varphi(n)\) exactly from the factorization, and checks
\[
\varphi(n)\mid\sigma(n)-n.
\]

It confirms that the complete finite hit set in this range is
\[
\{2,6,10,12,44\},
\]
and separately verifies the sharpness witness \(90\).

The computation is corroborative only. The unrestricted theorem follows from the exhaustive factorization-shape proof.

## Relationship to prior work
OEIS A066679 is exactly the sequence of integers satisfying
\[
\sigma(n)\equiv n\pmod{\varphi(n)}.
\]
Its displayed terms begin
\[
1,2,6,10,12,44,90,184,\ldots
\]
and its comments give a parametric family of larger members, but the inspected entry does not state a classification by \(\Omega(n)\).

Iannucci studies the equality
\[
\sigma(n)=n+\varphi(n),
\]
which is the quotient-one subcase of the same divisibility. His paper explicitly identifies A066679 as the ambient sequence where
\[
\sigma(n)-n
\]
is divisible by
\[
\varphi(n),
\]
then asks whether the quotient can equal \(1\) beyond \(n=2\). The paper proves necessary conditions for that equality subcase; it does not state the complete low-\(\Omega\) classification of the broader divisibility. The paper's primary Mathematics Subject Classification is \(11A25\).

Targeted searches for the exact congruence, the aliquot-sum divisibility formulation, semiprimes, prime squares, and the three-prime layer did not locate a theorem equivalent to or stronger than the classification proved here.

## Limitations
The theorem does not classify the full layer
\[
\Omega(n)=4
\]
or any higher layer. It only proves that multiplicity \(4\) is the smallest possible beyond the five displayed nontrivial low-complexity members.

Because the argument is elementary and the exact sequence has been public since 2002, an equivalent observation could occur in an unindexed problem note or discussion not surfaced by the searches.

## References
1. OEIS Foundation, A066679, “Numbers \(n\) such that \(\sigma(n)\) is congruent to \(n\) modulo \(\varphi(n)\),” entry authored 11 January 2002.
2. D. E. Iannucci, “On the Equation \(\sigma(n)=n+\varphi(n)\),” *Journal of Integer Sequences* 20 (2017), Article 17.6.2.
