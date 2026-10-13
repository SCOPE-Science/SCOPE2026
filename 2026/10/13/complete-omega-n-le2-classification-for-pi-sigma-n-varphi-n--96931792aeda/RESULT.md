# Complete \(\Omega(n)\le2\) classification for \(\pi(\sigma(n))=\varphi(n)\)
## Finding
Let \(\pi(x)\) denote the number of primes not exceeding \(x\), let \(\sigma(n)\) be the sum of positive divisors, let \(\varphi(n)\) be Euler's totient, and let \(\Omega(n)\) count prime factors with multiplicity.

For every integer
\[
n>1,\qquad \Omega(n)\le2,
\]
the equation
\[
\pi(\sigma(n))=\varphi(n)
\tag{1}
\]
holds if and only if
\[
n\in\{3,9,34\}.
\]

Equivalently, \(3\) is the unique prime solution, \(9\) is the unique prime-square solution, and
\[
34=2\cdot17
\]
is the unique squarefree semiprime solution.

## Assumptions and scope
The theorem classifies exactly the first two multiplicative-complexity layers of the equation (1). Thus every \(n\) under consideration is a prime, a prime square, or a product of two distinct primes.

The prime-counting function is
\[
\pi(x)=\#\{p\le x:p\text{ is prime}\}.
\]

Two elementary upper bounds will be used. First, for every integer \(x\ge2\),
\[
\pi(x)\le
\begin{cases}
x/2,&x\text{ even},\\
(x+1)/2,&x\text{ odd}.
\end{cases}
\tag{2}
\]
Second, elementary residue sieves give
\[
\pi(x)\le4+\frac{x}{3}
\tag{3}
\]
and
\[
\pi(x)\le11+\frac{4x}{15}.
\tag{4}
\]
For (3), apart from \(2\) and \(3\), every prime lies in one of two reduced residue classes modulo \(6\); allowing two candidates per complete or partial block yields the displayed safe bound. For (4), apart from \(2,3,5\), every prime lies in one of eight reduced residue classes modulo \(30\); allowing eight candidates in the final partial block gives the displayed bound.

No claim is made for
\[
\Omega(n)\ge3.
\]

## Proof
First let
\[
n=p
\]
be prime. Then
\[
\sigma(p)=p+1,\qquad \varphi(p)=p-1.
\]
For \(p=2\),
\[
\pi(3)=2\ne1.
\]
For \(p=3\),
\[
\pi(4)=2=\varphi(3).
\]
If \(p\ge5\), then \(p+1\) is even, and (2) gives
\[
\pi(p+1)\le\frac{p+1}{2}<p-1.
\]
Hence \(3\) is the unique prime solution.

Now let
\[
n=p^2.
\]
Then
\[
\sigma(p^2)=p^2+p+1,\qquad \varphi(p^2)=p(p-1).
\]
For \(p=2\),
\[
\pi(7)=4\ne2.
\]
For \(p=3\),
\[
\pi(13)=6=\varphi(9).
\]
If \(p\ge5\), then \(p^2+p+1\) is odd, and (2) gives
\[
\pi(p^2+p+1)
\le
\frac{p^2+p+2}{2}.
\]
Moreover
\[
\frac{p^2+p+2}{2}<p^2-p
\]
because
\[
p^2-3p-2>0
\]
for every \(p\ge5\). Thus \(9\) is the unique prime-square solution.

It remains to take
\[
n=pq
\]
with distinct primes
\[
p<q.
\]
Then
\[
\sigma(n)=(p+1)(q+1),
\qquad
\varphi(n)=(p-1)(q-1).
\tag{5}
\]

Suppose first that
\[
p\ge5.
\]
Then \(p,q\) are odd, so \(\sigma(n)\) is even. By (2),
\[
\pi(\sigma(n))\le\frac{(p+1)(q+1)}2.
\]
The difference between twice the totient and the divisor sum is
\[
2(p-1)(q-1)-(p+1)(q+1)
=
(p-3)(q-3)-8.
\tag{6}
\]
At the smallest pair \((p,q)=(5,7)\), this difference is \(0\), and direct evaluation gives
\[
\pi(48)=15\ne24=\varphi(35).
\]
For every other pair with \(5\le p<q\), the right side of (6) is positive, so
\[
\pi(\sigma(n))
\le
\frac{\sigma(n)}2
<
\varphi(n).
\]
Hence this branch contains no solution.

Next suppose
\[
p=3.
\]
Then
\[
\sigma(n)=4(q+1),
\qquad
\varphi(n)=2(q-1).
\]
If (1) holds, the modulo-\(6\) bound (3) gives
\[
2(q-1)
\le
4+\frac{4(q+1)}3,
\]
hence
\[
q\le11.
\]
The only possible primes are \(q=5,7,11\), and direct evaluation gives
\[
\pi(24)=9\ne8,
\qquad
\pi(32)=11\ne12,
\qquad
\pi(48)=15\ne20.
\]
Thus this branch has no solution.

Finally suppose
\[
p=2.
\]
Then
\[
\sigma(n)=3(q+1),
\qquad
\varphi(n)=q-1.
\]
If (1) holds, the modulo-\(30\) bound (4) gives
\[
q-1
\le
11+\frac{4(q+1)}5,
\]
so
\[
q\le64.
\tag{7}
\]
Therefore it is enough to inspect the odd primes \(q\le61\). The complete exact table is supplied in `small_cases.csv`. It has a unique match:
\[
q=17,
\qquad
\sigma(34)=54,
\qquad
\pi(54)=16,
\qquad
\varphi(34)=16.
\]
Thus \(34\) is the unique squarefree semiprime solution.

The prime, prime-square, and squarefree-semiprime cases exhaust the domain \(\Omega(n)\le2\), proving the theorem.

## Verification
The attached `verify.py` performs two independent exact checks.

First, it reconstructs every exceptional finite case left by the proof: the \(p=2\) branch through the exhaustive bound \(q\le61\), the \(p=3\) branch \(q\in\{5,7,11\}\), and the boundary pair \((5,7)\). Its generated values agree byte-for-byte with `small_cases.csv`.

Second, it factors every integer
\[
2\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)\le2,
\]
computes \(\sigma(n)\), \(\varphi(n)\), and \(\pi(\sigma(n))\) from integer sieves, and confirms that the only hits are
\[
3,\ 9,\ 34.
\]

The finite sweep is corroborative only. The absence of arbitrarily large low-\(\Omega\) solutions follows from the symbolic inequalities and the exhaustive finite reduction (7).

## Relationship to prior work
OEIS A067787 is the exact database sequence defined by
\[
\pi(\sigma(n))=\varphi(n).
\]
Its displayed terms begin
\[
3,\ 9,\ 34,\ 190,\ 224,\ 606,\ldots
\]
and its comments report computational searches with no further terms through \(10^6\) and, later, through \(10^9\). The inspected entry does not state a theorem classifying the prime, prime-square, or semiprime layers.

De Koninck and Luca study the joint arithmetic of \(\sigma\) and \(\varphi\) through
\[
H(n)=\frac{\sigma(\varphi(n))}{\varphi(\sigma(n))}.
\]
Their full paper explicitly uses \(\pi(x)\) as prime-counting notation and has primary Mathematics Subject Classification \(11A25\), but its theorems concern extremal order, average order, and density of the composition quotient rather than equation (1).

Targeted searches using the exact database identifier, the equation \(\pi(\sigma(n))=\varphi(n)\), semiprime and prime-square restrictions, and the equivalent prime-pair formulas did not locate a theorem equivalent to or stronger than the complete \(\Omega(n)\le2\) classification above.

## Limitations
The theorem does not classify any solution with
\[
\Omega(n)\ge3.
\]
In particular, it does not explain the later database terms \(190,224,606,\ldots\).

The proof uses deliberately coarse elementary prime-counting bounds; sharper analytic estimates are unnecessary for the first two multiplicity layers.

Because the equation has been public since 2002 and the proof is elementary, an equivalent observation may occur in an unindexed note or discussion not surfaced by the searches.

## References
1. OEIS Foundation, A067787, “Numbers \(n\) such that the number of primes not exceeding \(\sigma(n)\) equals \(\varphi(n)\),” entry authored 6 February 2002.
2. J.-M. De Koninck and F. Luca, “On the composition of the Euler function and the sum of divisors function,” *Colloquium Mathematicum* 108 (2007), 31–51, DOI 10.4064/cm108-1-4.
