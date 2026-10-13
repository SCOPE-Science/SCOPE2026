# Complete \(\Omega\le2\) classification for \(\varphi(n)\mid n\sigma(n)\)
## Finding
Let \(\sigma(n)\) be the sum of positive divisors, let \(\varphi(n)\) be Euler's totient, and let \(\Omega(n)\) count prime factors with multiplicity.

For every integer \(n>1\) with
\[
\Omega(n)\le2,
\]
the divisibility
\[
\varphi(n)\mid n\sigma(n)
\tag{1}
\]
holds exactly for
\[
n\in\{2,3,4,6,10,14,15,21,26,35,39,55,155,203\}.
\]

More explicitly, the squarefree semiprime solutions are
\[
pq
\]
for
\[
(p,q)\in
\{(2,3),(2,5),(2,7),(2,13),
(3,5),(3,7),(3,13),
(5,7),(5,11),(5,31),(7,29)\},
\]
and the only prime-square solution is
\[
4.
\]

## Assumptions and scope
The theorem classifies the complete range
\[
1\le\Omega(n)\le2
\]
inside the public sequence defined by (1). Thus the only factorization shapes are
\[
p,\qquad p^2,\qquad pq
\]
with \(p<q\) primes in the last case.

No claim is made for
\[
\Omega(n)\ge3.
\]

## Proof
First take a prime
\[
n=p.
\]
Then
\[
\varphi(p)=p-1,\qquad p\sigma(p)=p(p+1).
\]
Modulo \(p-1\),
\[
p(p+1)\equiv2.
\]
Hence
\[
p-1\mid2,
\]
so
\[
p\in\{2,3\}.
\]
Both values work.

Now let
\[
n=p^2.
\]
Then
\[
\varphi(p^2)=p(p-1)
\]
and
\[
p^2\sigma(p^2)=p^2(p^2+p+1).
\]
After cancelling one factor \(p\), condition (1) is equivalent to
\[
p-1\mid p(p^2+p+1).
\]
Modulo \(p-1\), the right side is congruent to \(3\). Therefore
\[
p-1\mid3.
\]
The only prime possibility is
\[
p=2,
\]
which gives
\[
n=4.
\]

It remains to classify
\[
n=pq,\qquad p<q
\]
with distinct primes. The defining condition is
\[
(p-1)(q-1)\mid pq(p+1)(q+1).
\tag{2}
\]

Suppose first that
\[
p=2.
\]
Then (2) becomes
\[
q-1\mid6q(q+1).
\]
Modulo \(q-1\), the right side is congruent to \(12\), so
\[
q-1\mid12.
\]
With \(q>2\) prime, this gives
\[
q\in\{3,5,7,13\}.
\]

Now suppose that \(p\) and \(q\) are odd. Put
\[
P=\frac{p-1}{2},
\qquad
Q=\frac{q-1}{2}.
\]
Then (2) is equivalent to
\[
PQ\mid pq(P+1)(Q+1).
\tag{3}
\]

Because
\[
\gcd(P,p)=\gcd(P,P+1)=1
\]
and \(q>P\), the factor \(P\) is coprime to
\[
pq(P+1).
\]
Thus (3) forces
\[
P\mid Q+1.
\]
Write
\[
Q+1=kP.
\tag{4}
\]
Since \(Q>P\),
\[
k\ge2,
\]
and (4) also gives
\[
\gcd(P,Q)=1.
\]

The \(Q\)-part of (3), using
\[
\gcd(Q,q(Q+1))=1,
\]
is therefore exactly
\[
Q\mid p(P+1).
\tag{5}
\]
Now
\[
p(P+1)=(2P+1)(P+1)=2P^2+3P+1.
\]
From
\[
Q=kP-1
\]
we have
\[
kP\equiv1\pmod Q
\]
and
\[
\gcd(k,Q)=1.
\]
Multiplying (5) by \(k^2\) therefore shows that (5) is equivalent to
\[
Q\mid k^2+3k+2=(k+1)(k+2).
\]
Define the positive integer
\[
h=\frac{(k+1)(k+2)}{Q}.
\]
Using \(Q=kP-1\),
\[
h(kP-1)=(k+1)(k+2),
\]
so
\[
k(hP-k-3)=h+2.
\]
Consequently
\[
k\mid h+2.
\]
Write
\[
h+2=kt
\]
with \(t\ge1\). Then
\[
h=kt-2
\]
and the preceding identity reduces to
\[
(kt-2)P=k+t+3.
\tag{6}
\]

Equation (6) is now finite.

If
\[
P=1,
\]
then \(p=3\) and
\[
(k-1)(t-1)=6.
\]
The condition \(Q>P\) excludes \(k=2\). The remaining factor pairs give
\[
(k,t)\in\{(3,4),(4,3),(7,2)\},
\]
hence
\[
q\in\{5,7,13\}.
\]

Suppose
\[
P\ge2.
\]
From (6),
\[
2(kt-2)\le k+t+3,
\]
or
\[
2kt-k-t\le7.
\tag{7}
\]
For \(t\ge4\), the left side of (7) is already at least \(10\), so
\[
t\le3.
\]
The remaining possibilities are:
\[
t=1,\quad 3\le k\le8;
\]
\[
t=2,\quad 2\le k\le3;
\]
\[
t=3,\quad k=2.
\]
Substitution into
\[
P=\frac{k+t+3}{kt-2}
\]
leaves, after the integrality and primality conditions,
\[
(k,t,P,Q,p,q)
=
(2,3,2,3,5,7),
\]
\[
(3,2,2,5,5,11),
\]
\[
(5,1,3,14,7,29),
\]
and
\[
(8,1,2,15,5,31).
\]
The other bounded pairs give either a nonintegral \(P\) or a composite \(p\).

Together with the \(p=3\) and \(p=2\) branches, this gives exactly the eleven squarefree semiprime pairs displayed in the finding.

Every step in the odd-semiprime reduction is reversible: from
\[
P\mid Q+1
\quad\text{and}\quad
Q\mid p(P+1),
\]
one has
\[
\gcd(P,Q)=1,
\]
so (3) follows. Direct substitution therefore establishes the converse for every listed pair.

Combining primes, prime squares, and squarefree semiprimes proves the classification.

## Verification
The attached `verify.py` independently checks every integer
\[
2\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)\le2.
\]
It factors each \(n\), computes \(\sigma(n)\) and \(\varphi(n)\) exactly, and compares the direct divisibility with the theorem's finite classification.

The finite replay is corroborative only. The unrestricted conclusion follows from the symbolic proof, in particular the reduction of every odd semiprime to the bounded integer equation
\[
(kt-2)P=k+t+3.
\]

## Relationship to prior work
OEIS A066994 is the exact database sequence defined by
\[
\varphi(n)\mid n\sigma(n).
\]
Its entry gives terms and computational predicates but no classification by \(\Omega(n)\), no semiprime theorem, and no structural reduction of the odd semiprime branch.

The same entry records A020492, the integers satisfying the stronger condition
\[
\varphi(n)\mid\sigma(n),
\]
as a subsequence. Broughan and Zhou study this stronger divisibility for integers with at most three distinct prime factors. Their results do not imply the present theorem because multiplication by \(n\) creates additional solutions; for example,
\[
26,\ 39,\ 155,\ 203
\]
belong to A066994 without being forced by the stronger condition.

De Koninck and Luca study the joint behavior of \(\sigma\) and \(\varphi\) through a composition quotient. Their primary Mathematics Subject Classification is \(11A25\), but their stated theorems concern orders, averages, and densities rather than the divisibility in (1).

Targeted searches for the exact database identifier, the equation, semiprime aliases, the fourteen-value low-multiplicity list, and the half-prime variables \(P,Q\) found no equivalent or stronger classification.

## Limitations
The theorem says nothing about integers with
\[
\Omega(n)\ge3.
\]
It also does not provide an asymptotic count for A066994.

The principal originality risk is an elementary observation in an unindexed problem source or discussion of A066994. The exact sequence page and the inspected low-prime-support literature do not expose this classification.

## References
1. OEIS Foundation, A066994, “Numbers \(k\) such that \(\varphi(k)\) divides \(k\sigma(k)\),” entry authored 27 January 2002.
2. K. A. Broughan and Q. Zhou, “On the Ratio of the Sum of Divisors and Euler's Totient Function II,” *Journal of Integer Sequences* 17 (2014), Article 14.9.2.
3. J.-M. De Koninck and F. Luca, “On the composition of the Euler function and the sum of divisors function,” *Colloquium Mathematicum* 108 (2007), 31–51, DOI 10.4064/cm108-1-4.
