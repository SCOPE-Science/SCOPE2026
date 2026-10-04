# The first multiplicity layer of triperfect numbers
## Finding
Let \(\Omega(n)\) denote the number of prime factors of \(n\), counted with
multiplicity. Every triperfect number
\[
\sigma(n)=3n
\]
satisfies
\[
\Omega(n)\ge5.
\]
Moreover,
\[
\Omega(n)=5
\quad\Longleftrightarrow\quad
n=120=2^3\cdot3\cdot5.
\]

## Assumptions and scope
The divisor-sum function is
\[
\sigma(n)=\sum_{d\mid n}d,
\]
and the abundancy index is
\[
I(n)=\frac{\sigma(n)}n.
\]
A triperfect number is a positive integer with \(I(n)=3\).

The theorem classifies the first possible total-prime-factor layer, where prime
factors are counted with multiplicity. It does not classify triperfect numbers
with \(\Omega(n)\ge6\).

## Proof
For a prime power,
\[
I(p^e)=1+\frac1p+\cdots+\frac1{p^e}.
\]
For fixed exponent \(e\), this decreases as \(p\) increases. For each exponent
partition of a fixed value of \(\Omega\), the largest possible abundancy is
therefore obtained by assigning its exponents to the smallest available primes;
the finitely many assignments can be compared directly.

For \(\Omega(n)\le4\), the largest possible abundancies for the five exponent
partitions of \(4\) are
\[
\frac{31}{16},\qquad
\frac52,\qquad
\frac{91}{36},\qquad
\frac{14}{5},\qquad
\frac{96}{35},
\]
corresponding respectively to
\[
(4),\ (3,1),\ (2,2),\ (2,1,1),\ (1,1,1,1).
\]
Every value is less than \(3\), and deleting prime factors can only decrease
the maximum. Hence every triperfect number satisfies
\[
\Omega(n)\ge5.
\]

Now suppose \(\Omega(n)=5\). An odd triperfect number would have odd
\(\sigma(n)=3n\). The classical parity criterion for the divisor sum says that
\(\sigma(n)\) is odd exactly when \(n\) is a square or twice a square. Since
\(n\) is odd, it would be a square, forcing \(\Omega(n)\) to be even. Thus
\(n\) is even.

Write
\[
n=2^a m,\qquad m\ {\rm odd},\qquad 1\le a\le5.
\]

If \(a=5\), then \(n=32\), which is not triperfect. If \(a=4\), then
\(m=q\) is an odd prime and
\[
I(n)\le\frac{31}{16}\frac43=\frac{31}{12}<3.
\]

Suppose \(a=3\). Then \(\Omega(m)=2\). If \(m=q^2\), then
\[
I(n)\le\frac{15}{8}\frac{13}{9}=\frac{65}{24}<3.
\]
Thus \(m=qr\) for distinct odd primes \(q<r\). The equation \(I(n)=3\)
becomes
\[
5(q+1)(r+1)=8qr,
\]
or
\[
(3q-5)(3r-5)=40.
\]
The only odd-prime solution is
\[
q=3,\qquad r=5,
\]
giving
\[
n=2^3\cdot3\cdot5=120.
\]

Suppose \(a=2\). Then the odd part has total multiplicity \(3\), and its
abundancy would have to be
\[
I(m)=\frac{12}{7}.
\]
If \(m=q^3\), then
\[
I(m)\le\frac{40}{27}<\frac{12}{7}.
\]
If \(m=q^2r\) with distinct odd primes, the equation becomes
\[
r\bigl(5q^2-7q-7\bigr)=7(q^2+q+1).
\]
For \(q=3\) this gives \(r=91/17\). For \(q\ge5\),
\[
7(q^2+q+1)<3(5q^2-7q-7),
\]
so \(r<3\), impossible.

Finally let \(m=qrs\) with distinct odd primes. If the least prime is at least
\(5\), then
\[
I(m)\le\frac65\frac87\frac{12}{11}
=\frac{576}{385}<\frac{12}{7}.
\]
Hence the least prime is \(3\). Writing the other two primes as \(r<s\), the
remaining equation is
\[
7(r+1)(s+1)=9rs,
\]
equivalently
\[
(2r-7)(2s-7)=63.
\]
The positive factor pairs of \(63\) yield no pair of distinct primes
\(3<r<s\).

It remains to consider \(a=1\). The odd part has total multiplicity \(4\) and
would require \(I(m)=2\). For the five exponent partitions of \(4\), now using
odd primes only, the respective maximal abundancies are
\[
\frac{121}{81},\qquad
\frac{16}{9},\qquad
\frac{403}{225},\qquad
\frac{208}{105},\qquad
\frac{768}{385}.
\]
All are less than \(2\), a contradiction.

Thus \(120\) is the unique triperfect number with
\(\Omega(n)=5\).

## Verification
The proof is symbolic and unrestricted. The accompanying checker verifies all
rational inequalities and finite factor equations used in the proof. It also
independently enumerates integers through \(10^6\), computes \(\sigma(n)\) and
\(\Omega(n)\) from a smallest-prime-factor sieve, and confirms that the only
triperfect integer in that range with \(\Omega(n)\le5\) is \(120\).

The finite enumeration is corroborative only and is not used to infer the
unrestricted theorem.

## Relationship to prior work
Cohen studied triperfect numbers in detail. His Theorem 4 proves, among other
things, that a triperfect number divisible by \(2^2\cdot3\cdot5\) must be
\(120\), and his Theorem 6 proves that an odd triperfect number has at least
nine distinct prime factors. Those statements do not by themselves show that
every triperfect number with five prime factors counted with multiplicity must
fall into the \(120\) divisibility pattern.

Kishore later strengthened the odd case to at least twelve distinct prime
factors. This is much stronger on the odd branch but does not classify the
small even multiplicity layer.

Cohen and Sorli studied even \(3\)-perfect numbers of the form
\[
2^aM
\]
with \(M\) odd and squarefree. They proved that, for \(a\le718\), the six
known examples are the only numbers of that restricted form. Their result is
bounded in \(a\) and assumes a squarefree odd part. The theorem here instead
classifies every triperfect number at the intrinsic boundary
\(\Omega(n)=5\), including nonsquarefree odd parts and without a bound on
the exponent of \(2\).

OEIS A005820 records the six known triperfect numbers, beginning with \(120\),
and states that they are believed to be complete. A finite exact table cannot
exclude an arbitrarily large triperfect number with five prime factors counted
with multiplicity; the proof above does.

## Limitations
The theorem gives no classification once \(\Omega(n)\ge6\), and it does not
address the open completeness question for the six known triperfect numbers.

The 1980 Cohen paper is historically earlier than the exact-day date used in
the metadata, but the inspected print evidence resolves its original
publication only to May 1980. The metadata therefore uses the earliest exact
public calendar date verified for a directly relevant primary source, the
Cambridge online release on 9 April 2009.

Older computational and historical literature that is not available in
searchable full text remains a residual originality risk.

## References
1. G. L. Cohen, "On odd perfect numbers (II), multiperfect numbers and
   quasiperfect numbers", *Journal of the Australian Mathematical Society*
   29 (1980), 369--384, DOI 10.1017/S1446788700021376.
2. M. Kishore, "Odd triperfect numbers are divisible by twelve distinct prime
   factors", *Journal of the Australian Mathematical Society* 42 (1987),
   173--182, DOI 10.1017/S1446788700028184.
3. G. L. Cohen and R. M. Sorli, "On Odd Perfect Numbers and Even 3-Perfect
   Numbers", *Integers* 12A (2012), Article A6,
   DOI 10.1515/integers-2012-0036.
4. OEIS Foundation, A005820, "3-perfect (triply perfect, tri-perfect,
   triperfect or sous-double) numbers".
