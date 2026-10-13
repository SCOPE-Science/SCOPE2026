# A sharp four-unit stability gap for \(\sigma(n)-\varphi(n+2)\)
## Finding
Define
\[
A(n)=\sigma(n)-\varphi(n+2).
\]

For every integer
\[
n>1,
\]
one has
\[
A(n)<5
\]
if and only if either \(n\) and \(n+2\) are twin primes, in which case
\[
A(n)=0,
\]
or
\[
(n,A(n))\in
\{(2,1),(7,2),(9,3),(23,4)\}.
\]

Hence the first four positive fibers are
\[
A^{-1}(1)=\{2\},
\qquad
A^{-1}(2)=\{7\},
\qquad
A^{-1}(3)=\{9\},
\qquad
A^{-1}(4)=\{23\}.
\]

Equivalently, apart from twin-prime starts and those four isolated exceptions,
\[
A(n)\ge5.
\]
This lower bound is sharp:
\[
A(4)=\sigma(4)-\varphi(6)=7-2=5.
\]

## Assumptions and scope
The functions are the ordinary sum-of-divisors function \(\sigma\) and Euler's totient \(\varphi\).

For later use define
\[
E(n)=\sigma(n)-n-1,
\]
the sum of the proper divisors of \(n\) other than \(1\), and define the cototient
\[
C(m)=m-\varphi(m).
\]
Then the exact decomposition
\[
A(n)=E(n)+C(n+2)-1
\tag{1}
\]
holds for every \(n\ge1\).

The theorem concerns the complete range
\[
0\le A(n)\le4
\]
for \(n>1\). No claim is made about higher fibers.

## Proof
From
\[
\sigma(n)=n+1+E(n)
\]
and
\[
\varphi(n+2)=n+2-C(n+2),
\]
equation (1) follows immediately:
\[
A(n)=E(n)+C(n+2)-1.
\]

We first treat composite \(n\).

For a composite integer,
\[
E(n)>0.
\]
Suppose
\[
E(n)\le4.
\]
Let \(p\) be the least prime divisor of \(n\).

If
\[
n=p^2,
\]
then the proper divisors other than \(1\) consist only of \(p\), so
\[
E(n)=p.
\]
Thus
\[
p\le4,
\]
and hence
\[
n\in\{4,9\}.
\]

If
\[
n\ne p^2,
\]
then \(p\) and \(n/p\) are distinct proper divisors. Therefore
\[
E(n)\ge p+\frac np.
\]
The two positive integers \(p\) and \(n/p\) are at least \(2\) and \(3\), respectively, so
\[
E(n)\ge5,
\]
a contradiction.

Consequently
\[
E(n)\le4
\]
for composite \(n\) is possible only at
\[
n=4,\ 9.
\]

Now if
\[
A(n)<5,
\]
then by (1) and
\[
C(n+2)\ge1
\]
we have
\[
E(n)\le4.
\]
Thus a composite solution with \(A(n)<5\) must be \(4\) or \(9\). Directly,
\[
A(4)=5,
\qquad
A(9)=13-10=3.
\]
Hence the only composite integer with
\[
A(n)<5
\]
is
\[
n=9,
\]
and it gives the unique value \(3\).

It remains to treat prime \(n\). For prime \(n\),
\[
E(n)=0,
\]
so (1) becomes
\[
A(n)=C(n+2)-1.
\tag{2}
\]

For
\[
n=2,
\]
one has
\[
C(4)=2,
\]
hence
\[
A(2)=1.
\]

Now let \(n\) be an odd prime and put
\[
m=n+2.
\]
Then \(m\) is odd.

If \(m\) is prime, then
\[
C(m)=1,
\]
so
\[
A(n)=0.
\]
These are exactly the twin-prime starts.

Suppose instead that \(m\) is composite and
\[
A(n)<5.
\]
By (2),
\[
C(m)\le5.
\tag{3}
\]

Let \(r\) be the least prime divisor of \(m\). Since all multiples of \(r\) up to \(m\) are noncoprime to \(m\),
\[
C(m)\ge\frac mr.
\tag{4}
\]
Because \(m\) is composite and \(r\) is its least prime divisor,
\[
m\ge r^2.
\tag{5}
\]
Combining (3), (4), and (5) gives
\[
r\le5.
\]
Since \(m\) is odd,
\[
r\in\{3,5\}.
\]

If
\[
r=3,
\]
then (4) and (3) give
\[
m\le15.
\]
The odd composite integers in this range with least prime divisor \(3\) are
\[
9,\ 15.
\]
Their cototients are
\[
C(9)=3,
\qquad
C(15)=7.
\]
Thus only
\[
m=9
\]
survives, yielding
\[
n=7,
\qquad
A(7)=2.
\]

If
\[
r=5,
\]
then (4) gives
\[
m\le25,
\]
while (5) gives
\[
m\ge25.
\]
Hence
\[
m=25.
\]
Since
\[
C(25)=5,
\]
this gives
\[
n=23,
\qquad
A(23)=4.
\]

Together with the composite case \(n=9\) and the exceptional prime \(n=2\), these exhaust all possibilities with \(A(n)<5\).

## Verification
The attached `verify.py` independently checks every integer
\[
2\le n\le2{,}000{,}000.
\]
It computes \(\sigma(n)\), \(\varphi(n+2)\), and primality from exact integer sieves.

For every tested \(n\), it compares direct evaluation of
\[
A(n)<5
\]
with the theorem's predicate:
either \(n,n+2\) are both prime, or
\[
n\in\{2,7,9,23\}.
\]

It also confirms the exact exceptional values
\[
A(2)=1,\quad A(7)=2,\quad A(9)=3,\quad A(23)=4,
\]
and the sharp boundary value
\[
A(4)=5.
\]

The finite computation is corroborative only. The unrestricted theorem follows from the decomposition (1) and the divisor/cototient bounds in the proof.

## Relationship to prior work
OEIS A078119 is the exact database sequence
\[
A(n)=\sigma(n)-\varphi(n+2).
\]
Its current formula section records that
\[
A(n)\ge0
\]
for \(n>1\), with equality exactly when \(n,n+2\) are twin primes. The entry tabulates the initial positive values, including
\[
A(2)=1,\quad A(7)=2,\quad A(9)=3,\quad A(23)=4,
\]
but does not state that these four fibers are singletons or that every other nonzero value is at least \(5\).

Pomerance and Yang study the value distributions of the two component functions
\[
\sigma(n)-n
\]
and
\[
n-\varphi(n),
\]
including algorithms for their ranges and density questions. Their work supplies primary literature context for the aliquot-sum and cototient pieces appearing in (1), but does not study the shifted difference
\[
\sigma(n)-\varphi(n+2)
\]
or its small fibers.

Targeted searches for the exact database identifier, the shifted difference, the values \(1,2,3,4\), and the threshold formulation
\[
A(n)<5
\]
did not locate an equivalent or stronger theorem.

## Limitations
The theorem determines only the zero fiber and the first four positive fibers. It does not classify any value
\[
A(n)\ge5.
\]

The argument is elementary, so an equivalent observation may exist in an unindexed problem note or discussion of A078119 not surfaced by the searches.

The theorem does not address whether there are infinitely many zeroes; that is exactly the twin-prime problem already encoded by the zero fiber.

## References
1. OEIS Foundation, A078119, \(a(n)=\sigma(n)-\varphi(n+2)\), entry authored 6 December 2002.
2. C. Pomerance and H.-S. Yang, “Variant of a theorem of Erdős on the sum-of-proper-divisors function,” *Mathematics of Computation* 83 (2014), 1903–1913, DOI 10.1090/S0025-5718-2013-02775-5.
