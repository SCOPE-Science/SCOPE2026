# A four-prime barrier for the Pillai gcd-sum plus-one congruence
## Finding
Let
\[
P(n)=\sum_{k=1}^{n}\gcd(k,n)
\]
be Pillai's gcd-sum function. If \(n>1\) and
\[
n\mid P(n)+1,
\]
then either \(n\) is prime or \(n\) is squarefree with at least four distinct prime factors. Equivalently, every composite solution is squarefree and satisfies
\[
\omega(n)\ge4.
\]

Thus the conjecture recorded in OEIS A018804 in 2014,
\[
n>1,\qquad n\mid P(n)+1
\quad\Longrightarrow\quad
n\text{ is prime},
\]
is valid on the complete multiplicative-complexity layer
\[
\Omega(n)\le3,
\]
although the unrestricted conjecture is now known to be false.

## Assumptions and scope
The classical gcd-sum function is multiplicative and, for a prime \(p\) and integer \(a\ge1\),
\[
P(p^a)=p^{a-1}\bigl((a+1)p-a\bigr).
\]
For a squarefree integer
\[
n=p_1p_2\cdots p_r,
\]
this gives
\[
P(n)=\prod_{j=1}^{r}(2p_j-1).
\]

Here \(\omega(n)\) counts distinct prime factors and \(\Omega(n)\) counts prime factors with multiplicity. The statement concerns the divisibility condition \(n\mid P(n)+1\), not the different condition \(n\mid P(n)\).

## Proof
Suppose
\[
n>1,\qquad n\mid P(n)+1.
\tag{1}
\]

First, \(n\) must be squarefree. Indeed, if \(p^a\Vert n\) with \(a\ge2\), then the prime-power formula shows
\[
p\mid P(p^a).
\]
By multiplicativity,
\[
p\mid P(n),
\]
so
\[
P(n)+1\equiv1\pmod p,
\]
contradicting (1). Therefore every solution of (1) is squarefree.

It remains to exclude composite squarefree integers with two or three prime factors.

Let first
\[
n=pq,\qquad p<q.
\]
If \(p=2\), then
\[
P(n)+1=3(2q-1)+1=2(3q-1).
\]
Divisibility by \(2q\) would force
\[
q\mid1,
\]
which is impossible.

Now suppose \(p,q\) are odd. Then
\[
\frac{P(n)+1}{n}
=
4-\frac2p-\frac2q+\frac2{pq}.
\]
If this is an integer, it is even because \(P(n)+1\) is even and \(n\) is odd. It is positive and strictly less than \(4\), so it must equal \(2\). Hence
\[
(2p-1)(2q-1)+1=2pq,
\]
which simplifies to
\[
(p-1)(q-1)=0,
\]
a contradiction. Thus no composite solution has two distinct prime factors.

Now let
\[
n=pqr,\qquad p<q<r.
\]

Assume first that \(p=2\). Then
\[
\frac{P(n)+1}{n}
=
6-\frac3q-\frac3r+\frac2{qr}.
\]
Since \(q\ge3\) and \(r\ge5\), this quantity is strictly between \(4\) and \(6\). If (1) holds, the quotient is therefore \(5\). Consequently,
\[
3(2q-1)(2r-1)+1=10qr,
\]
or
\[
r(q-3)=3q-2.
\tag{2}
\]
For \(q=3\), (2) is impossible. For \(q=5\), it gives \(2r=13\). For \(q\ge7\),
\[
r=3+\frac7{q-3}<q,
\]
contrary to \(r>q\).

It remains to consider odd primes
\[
3\le p<q<r.
\]
Then
\[
\frac{P(n)+1}{n}
=
\left(2-\frac1p\right)
\left(2-\frac1q\right)
\left(2-\frac1r\right)
+\frac1{pqr}.
\]
The expression increases with each prime and at \(p=3,q=5,r=7\) already exceeds \(5\). It is also strictly less than \(8\). Since \(P(n)+1\) is even and \(n\) is odd, an integral quotient must therefore be
\[
6.
\]
Expanding
\[
(2p-1)(2q-1)(2r-1)+1=6pqr
\]
gives
\[
r\bigl(pq-2p-2q+1\bigr)=2pq-p-q.
\tag{3}
\]

For \(p=3,q=5\), the coefficient of \(r\) in (3) is \(0\) while the right side is \(22\). For \(p=3,q=7\), equation (3) gives \(r=16\). For \(p=3,q\ge11\), put
\[
D=pq-2p-2q+1,\qquad N=2pq-p-q.
\]
Then
\[
qD-N=q^2-10q+3>0,
\]
so (3) would give \(r=N/D<q\), impossible.

Finally suppose \(p\ge5\), hence \(q\ge7\). Then
\[
qD-N
=
p(q^2-4q+1)-2q^2+2q
\]
and therefore
\[
qD-N
\ge
5(q^2-4q+1)-2q^2+2q
=
3q^2-18q+5>0.
\]
Again (3) yields \(r<q\), a contradiction.

Thus no composite solution has at most three distinct prime factors. Combining this with squarefreeness proves that every composite solution of (1) has at least four distinct prime factors.

## Verification
The attached `verify.py` checks the prime-power formula directly against the defining gcd sum on a finite exact range, checks the symbolic identities used in the two- and three-prime cases, and exhaustively verifies every
\[
2\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)\le3.
\]
Every solution in that range is prime.

The verifier also evaluates the composite counterexample currently recorded by OEIS A018804,
\[
n=3\cdot37\cdot43\cdot42307\cdot116341,
\]
and confirms
\[
P(n)+1=26n.
\]
This demonstrates the distinction between the proved low-complexity barrier and the false unrestricted conjecture.

The finite computation is corroborative only; the theorem follows from the complete case analysis above.

## Relationship to prior work
Broughan's 2001 paper gives the multiplicativity and prime-power formula for the gcd-sum function and lists the subject classification beginning with MSC \(11A05\). It does not state the plus-one divisibility classification proved here.

Tóth's 2010 survey treats the different problem
\[
n\mid P(n).
\]
For squarefree integers with at most three distinct prime factors, that survey determines the solutions of this unshifted divisibility problem. The argument and conclusion do not imply the present result because replacing \(P(n)\) by \(P(n)+1\) changes every local congruence.

OEIS A018804 records the exact plus-one conjecture, dated 22 October 2014, and now records a five-prime composite counterexample found in 2025. The database does not state a squarefreeness theorem or an exclusion of the two- and three-prime layers for the plus-one condition.

A Mathematical Reflections link attached to the OEIS entry was also checked because it is a plausible source of an elementary divisibility observation. The archived target available for inspection did not expose a matching gcd-sum problem, so no whole-document noncoverage claim is based on that link.

## Limitations
The theorem does not exclude squarefree solutions with four or more distinct prime factors. In particular, it does not settle whether a four-prime composite solution exists.

The known composite counterexample has five distinct prime factors, so the lower bound \(\omega(n)\ge4\) is not claimed to be sharp. An equivalent elementary proof could exist in an unindexed problem source; this remains the principal originality risk.

## References
1. K. A. Broughan, “The gcd-sum Function,” *Journal of Integer Sequences* 4 (2001), Article 01.2.2; published 25 October 2001.
2. L. Tóth, “A Survey of Gcd-Sum Functions,” *Journal of Integer Sequences* 13 (2010), Article 10.8.1.
3. OEIS Foundation, A018804, “Pillai's arithmetical function.”
