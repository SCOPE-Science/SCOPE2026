# Prime-square fibers of the proper-divisor product

## Finding
Let
\[
s(n)=\sigma(n)-n
\]
be the sum of the proper divisors of \(n\), and define
\[
B(n)=ns(n).
\]

For every prime \(p\), the complete fiber of \(B\) above the prime-square value
\[
B(p^2)=p^2(p+1)
\]
is
\[
B^{-1}\!\left(p^2(p+1)\right)=
\begin{cases}
\{6,9\},&p=3,\\
\{p^2\},&p\ne3.
\end{cases}
\]

Equivalently, the only collision of \(B\) involving a prime square is
\[
B(6)=B(9)=36.
\]

## Assumptions and scope
All integers are positive. The function \(s(n)\) denotes the sum of the proper positive divisors of \(n\), so \(s(1)=0\).

The theorem classifies one natural infinite family of fibers of \(B\), namely those containing a prime square. It does not classify arbitrary collisions of \(B\).

## Proof
Fix a prime \(p\), and suppose
\[
B(n)=B(p^2)=p^2(p+1).
\]
Because
\[
n\,s(n)=p^2(p+1),
\]
we have
\[
n\mid p^2(p+1).
\]
Since
\[
p\nmid p+1,
\]
the exponent of \(p\) in \(n\) is \(0\), \(1\), or \(2\).

First suppose
\[
\nu_p(n)=2.
\]
Write
\[
n=p^2d,
\qquad
d\mid p+1,
\qquad
\gcd(d,p)=1.
\]
The defining equation gives
\[
s(n)=\frac{p+1}{d}.
\]
If \(d>1\), then \(p^2\) is a proper divisor of \(n\), so
\[
s(n)\ge p^2>\frac{p+1}{d},
\]
a contradiction. Hence \(d=1\), so
\[
n=p^2.
\]

Next suppose
\[
\nu_p(n)=0.
\]
Then \(n=d\) for some
\[
d\mid p+1.
\]
The equation
\[
d\,s(d)=p^2(p+1)
\]
and \(\gcd(d,p)=1\) imply
\[
p^2\mid s(d).
\]
But \(d\le p+1\), and
\[
s(d)\le1+2+\cdots+(d-1)
=\frac{d(d-1)}2
\le\frac{p(p+1)}2
<p^2.
\]
This is impossible.

It remains to consider
\[
\nu_p(n)=1.
\]
Write
\[
n=pd,
\qquad
d\mid p+1,
\qquad
\gcd(d,p)=1.
\]
Since \(\sigma\) is multiplicative,
\[
s(pd)=\sigma(p)\sigma(d)-pd
=(p+1)\sigma(d)-pd.
\]
Thus
\[
pd\bigl((p+1)\sigma(d)-pd\bigr)=p^2(p+1).
\]
After dividing by \(p\) and using
\[
\sigma(d)=d+s(d),
\]
we obtain
\[
d\bigl(d+(p+1)s(d)\bigr)=p(p+1).
\]

Write
\[
p+1=dk.
\]
Then
\[
d\bigl(1+ks(d)\bigr)=pk.
\]
Because \(\gcd(d,p)=1\), it follows that
\[
d\mid k.
\]
Write
\[
k=dh.
\]
Substitution gives
\[
1+dhs(d)=ph.
\]
Reducing modulo \(h\) yields
\[
1\equiv0\pmod h,
\]
so
\[
h=1.
\]
Consequently
\[
k=d
\]
and hence
\[
p+1=d^2.
\]
Therefore
\[
p=d^2-1=(d-1)(d+1).
\]
Since \(p\) is prime, the only possibility is
\[
d=2,\qquad p=3.
\]
This gives
\[
n=pd=6.
\]

Conversely,
\[
s(6)=6,\qquad s(9)=4,
\]
so
\[
B(6)=6\cdot6=36=9\cdot4=B(9).
\]
The fiber classification follows.

## Verification
The accompanying `verify.py` enumerates every prime
\[
p\le5000
\]
and every divisor \(n\) of
\[
p^2(p+1).
\]
For each candidate divisor it computes \(s(n)\) from a prime factorization and checks the exact fiber identity. The only nontrivial fiber found is
\[
p=3,\qquad \{n:B(n)=B(9)\}=\{6,9\}.
\]

This computation is regression evidence only. The theorem for every prime is proved symbolically above.

## Relationship to prior work
Noppakaew and Pongsriiam introduced the collision problem for
\[
B(x)=xs(x)
\]
in the setting of products of arithmetic functions. Their Question 29 asks whether \(B\) has infinitely many collisions, and whether infinitely many of them are non-amicable. Their table begins with the non-amicable collision
\[
B(6)=B(9)=36.
\]

The present theorem identifies this first example as the unique collision in the entire infinite family of fibers containing a prime square. Thus any construction of infinitely many collisions must eventually avoid prime-square arguments.

The exact collision-value database OEIS A212327 also begins with \(36\) and records further values having at least two preimages under \(B\). Its current entry does not state a classification of fibers containing prime squares.

Targeted searches for prime-square fibers of \(ns(n)\), for solutions of
\[
ns(n)=p^2(p+1),
\]
and for the equivalence that \(9\) is the only prime square occurring in a collision did not locate an implication-equivalent theorem.

## Limitations
The theorem does not decide whether \(B\) has infinitely many collisions. It excludes prime squares, except \(9\), from participating in such collisions.

The proof is specific to prime squares. Higher prime powers lead to a less rigid divisor equation and are not claimed here.

The principal residual originality risk is an unindexed observation about the first collision \(36\) or about OEIS A212327 that derives the same infinite prime-square classification.

## References
1. Passawan Noppakaew and Prapanpong Pongsriiam, “Product of Some Polynomials and Arithmetic Functions,” Journal of Integer Sequences 26 (2023), Article 23.9.1.
2. OEIS A212327, “Numbers \(k\) such that \(A001065(x)x=k\) has at least two solutions.”
