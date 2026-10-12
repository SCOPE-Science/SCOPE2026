# Exact \(\Omega(n)\le3\) classification for \(n\mid\varphi(n)\sigma(n)\)
## Finding
Let \(\Omega(n)\) count prime factors with multiplicity. For every integer
\[
n>1,\qquad \Omega(n)\le3,
\]
the divisibility
\[
n\mid\varphi(n)\sigma(n)
\tag{1}
\]
holds if and only if either
\[
n=6,
\qquad
n=18,
\]
or
\[
n=p^2\bigl(p^2+p+1\bigr)
\tag{2}
\]
for a prime \(p\) such that
\[
p^2+p+1
\]
is also prime.

Equivalently, the repeated-prime branch is governed exactly by the cyclotomic value
\[
\Phi_3(p)=p^2+p+1.
\]

The first solutions are
\[
6,\ 18,\ 28,\ 117,\ 775,\ 88723,\ 2896363,\ldots
\]
corresponding in (2) to
\[
p=2,3,5,17,41,\ldots
\]

There are no prime-power solutions and no squarefree three-prime solutions in the stated multiplicity range.

## Assumptions and scope
The functions are Euler's totient \(\varphi\) and the ordinary sum-of-divisors function \(\sigma\).

For \(n>1\), condition (1) is equivalent to saying that the residue
\[
\bigl(\varphi(n)\sigma(n)+1\bigr)\bmod n
\]
equals \(1\). This is the residue-one slice of OEIS A056100.

The product
\[
\varphi(n)\sigma(n)
\]
is OEIS A062354. That entry also records the interpretation of this product as the number of conjugacy classes in the group of invertible \(2\times2\) matrices modulo \(n\).

The theorem classifies exactly the multiplicity range
\[
1\le\Omega(n)\le3.
\]
No claim is made for larger multiplicity.

## Proof
Prime powers never satisfy (1). Indeed, for
\[
n=p^a,
\]
one has
\[
\varphi(p^a)\sigma(p^a)
=
p^{a-1}\bigl(p^{a+1}-1\bigr).
\]
The second factor is congruent to \(-1\) modulo \(p\), so the \(p\)-adic valuation of the product is exactly
\[
a-1<a.
\]
Thus neither primes, prime squares, nor prime cubes satisfy (1).

Now let
\[
n=pq
\]
with distinct primes
\[
p<q.
\]
Then
\[
\varphi(n)\sigma(n)
=
(p^2-1)(q^2-1).
\]
If (1) holds, divisibility by \(q\) requires
\[
q\mid p^2-1=(p-1)(p+1).
\]
Since \(q>p\), this forces
\[
q=p+1.
\]
The only consecutive primes are \(2\) and \(3\), so
\[
n=6.
\]
Conversely,
\[
6\mid\varphi(6)\sigma(6)=24.
\]

Consider next a squarefree product of three distinct primes
\[
n=pqr,
\qquad
p<q<r.
\]
If (1) held, reduction modulo \(r\) would give
\[
r\mid(p^2-1)(q^2-1).
\]
Because \(r\) is prime, it would divide one of
\[
p-1,\ p+1,\ q-1,\ q+1.
\]
The first three are strictly between \(0\) and \(r\). Also \(q+1\le r\), and equality would make \(q,r\) consecutive primes differing by \(1\), forcing \(q=2,r=3\), impossible because \(p<q\). Thus
\[
0<q+1<r,
\]
so no factor is divisible by \(r\), a contradiction. Therefore no squarefree three-prime solution exists.

It remains to take
\[
n=p^2q
\]
with distinct primes \(p,q\), where \(p\) is the repeated prime. A direct factorization gives
\[
\varphi(p^2q)\sigma(p^2q)
=
p(p-1)(p^2+p+1)(q^2-1).
\tag{3}
\]
Condition (1) is therefore equivalent to the pair
\[
p\mid q^2-1
\tag{4}
\]
and
\[
q\mid(p-1)(p^2+p+1).
\tag{5}
\]

Suppose first that
\[
q<p.
\]
From (4),
\[
p\mid(q-1)(q+1).
\]
Since \(p>q\), the factor \(q-1\) is too small, while
\[
q+1\le p.
\]
Hence
\[
p=q+1.
\]
Two consecutive primes with difference \(1\) must be
\[
(q,p)=(2,3),
\]
giving
\[
n=3^2\cdot2=18.
\]
Directly,
\[
18\mid\varphi(18)\sigma(18)=234.
\]

Now suppose
\[
q>p.
\]
Then (5) cannot be satisfied through the factor \(p-1\), so
\[
q\mid p^2+p+1.
\tag{6}
\]
At the same time, (4) gives
\[
q\equiv\pm1\pmod p.
\tag{7}
\]

Put
\[
p^2+p+1=qt
\]
with \(t\ge1\).

If
\[
q\equiv1\pmod p,
\]
then reduction modulo \(p\) gives
\[
t\equiv1\pmod p.
\]
Because \(q>p\),
\[
t
=
\frac{p^2+p+1}{q}
<
\frac{p^2+p+1}{p+1}
<
p+1.
\]
Therefore
\[
t=1.
\]
Hence
\[
q=p^2+p+1,
\]
which must be prime.

If instead
\[
q\equiv-1\pmod p,
\]
then \(p\) is odd and \(q\ge2p-1\). Thus
\[
t
\le
\frac{p^2+p+1}{2p-1}
<
p.
\]
But modulo \(p\),
\[
-t\equiv1,
\]
so
\[
t\equiv-1\pmod p.
\]
The only positive integer below \(p\) with this residue is
\[
t=p-1.
\]
That is impossible because \(p^2+p+1\) is odd whereas
\[
q(p-1)
\]
is even. Hence the negative residue branch cannot occur.

We have proved that the \(q>p\) branch is exactly
\[
q=p^2+p+1
\]
with both \(p\) and \(q\) prime. Substitution into (3) shows the converse: since
\[
q\equiv1\pmod p,
\]
condition (4) holds, while (6) is automatic. Thus every integer in (2) satisfies (1).

Combining all factorization shapes with \(\Omega(n)\le3\) proves the theorem.

## Verification
The attached `verify.py` independently checks every integer
\[
2\le n\le3{,}000{,}000
\]
with
\[
\Omega(n)\le3.
\]
It factors \(n\), computes \(\varphi(n)\) and \(\sigma(n)\) exactly, and compares direct divisibility with the theorem's classification.

The verified hit set in that range is
\[
\{6,18,28,117,775,88723,2896363\}.
\]

The finite replay is corroborative only. The unrestricted classification follows from the prime-factor arguments above.

## Relationship to prior work
OEIS A056100 is the exact residue sequence
\[
\bigl(\varphi(n)\sigma(n)+1\bigr)\bmod n.
\]
Its entry notes the prime zero-residue behavior and provides tables and direct computational formulas, but does not state the residue-one classification for low multiplicity.

OEIS A062354 is exactly the product
\[
\varphi(n)\sigma(n).
\]
It records its prime-power formula and a group-theoretic conjugacy-class interpretation, but not divisibility by \(n\) or a low-\(\Omega\) classification.

Broughan, Ford, and Luca study the same product \(\varphi(n)\sigma(n)\) and use the normalized Euler product
\[
\frac{\varphi(n)\sigma(n)}{n^2}
=
\prod_{p^a\parallel n}
\left(1-\frac1{p^{a+1}}\right).
\]
Their primary Mathematics Subject Classification is \(11A41\). Their results concern square values of the product and the difference between its square root and \(n\); they do not state divisibility of the product by \(n\), nor the cyclotomic family in (2).

Targeted searches for the exact residue sequence, the divisibility \(n\mid\varphi(n)\sigma(n)\), the repeated-prime shape \(p^2q\), and the cyclotomic value \(p^2+p+1\) did not locate an equivalent or stronger \(\Omega(n)\le3\) theorem.

## Limitations
The theorem does not classify solutions with
\[
\Omega(n)\ge4.
\]
It also does not assert that infinitely many primes \(p\) have
\[
p^2+p+1
\]
prime.

Because the proof is elementary and the exact residue sequence has been public since 2000, an equivalent observation may occur in an unindexed note or discussion not surfaced by the searches.

## References
1. OEIS Foundation, A056100, \(a(n)=(\sigma(n)\varphi(n)+1)\bmod n\), entry authored 28 July 2000.
2. OEIS Foundation, A062354, \(a(n)=\sigma(n)\varphi(n)\), entry authored 6 July 2001.
3. K. A. Broughan, K. Ford, and F. Luca, “On square values of the product of the Euler totient and sum of divisors functions,” *Colloquium Mathematicum* 130 (2013), 127–137, DOI 10.4064/cm130-1-11.
