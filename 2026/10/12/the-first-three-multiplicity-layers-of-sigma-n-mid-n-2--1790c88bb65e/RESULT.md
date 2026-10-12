# The first three multiplicity layers of \(\sigma(n)\mid n^2\)
## Finding
Let
\[
\sigma(n)=\sum_{d\mid n}d
\]
and let \(\Omega(n)\) count prime factors with multiplicity.

For every integer \(n>1\),
\[
\sigma(n)\mid n^2,\qquad \Omega(n)\le3
\]
holds exactly for
\[
n=6\quad\text{or}\quad n=28.
\]

Both are perfect numbers. Therefore every non-perfect member of the divisibility set
\[
\sigma(n)\mid n^2
\]
has
\[
\Omega(n)\ge4.
\]
This is sharp:
\[
364=2^2\cdot7\cdot13,\qquad
\sigma(364)=7\cdot8\cdot14=784,
\]
and
\[
\frac{364^2}{784}=169,
\]
while
\[
784\ne2\cdot364.
\]

## Assumptions and scope
The theorem concerns the exact multiplicative-complexity range
\[
\Omega(n)\le3
\]
inside the sequence defined by
\[
\sigma(n)\mid n^2.
\]
The integer \(1\) is excluded from the stated classification only to separate the nontrivial multiplicative layers; it also satisfies the divisibility.

No claim is made about a classification for
\[
\Omega(n)\ge4.
\]
The sharpness statement identifies the minimum possible multiplicity of a non-perfect member, not all members at that multiplicity.

## Proof
Suppose
\[
n>1,\qquad \sigma(n)\mid n^2,\qquad \Omega(n)\le3.
\tag{1}
\]
Because every prime-power divisor-sum factor divides \(\sigma(n)\), condition (1) implies that every prime divisor of each such factor must already divide \(n\).

If
\[
\Omega(n)=1,
\]
then \(n=p\) is prime. Since
\[
\sigma(p)=p+1
\]
is coprime to \(p\) and greater than \(1\), it cannot divide \(p^2\). Thus this layer is empty.

Now let
\[
\Omega(n)=2.
\]
If \(n=p^2\), then
\[
\sigma(p^2)=p^2+p+1
\]
is coprime to \(p\) and greater than \(1\), so it cannot divide \(p^4\).

The remaining shape is
\[
n=pq
\]
with distinct primes \(p<q\). The factor \(p+1\) divides \(\sigma(n)\), hence divides \(n^2\). Since
\[
\gcd(p,p+1)=1,
\]
every prime divisor of \(p+1\) must be \(q\). But
\[
1<p+1\le q,
\]
so necessarily
\[
p+1=q.
\]
Two primes differing by \(1\) must be \(2\) and \(3\). Hence
\[
n=6.
\]
Indeed,
\[
\sigma(6)=12\mid36.
\]

Finally suppose
\[
\Omega(n)=3.
\]
There are three factorization shapes.

For
\[
n=p^3,
\]
the number
\[
\sigma(p^3)=1+p+p^2+p^3
\]
is coprime to \(p\) and greater than \(1\), so it cannot divide \(p^6\).

Next let
\[
n=p^2q
\]
with distinct primes \(p,q\), where \(p\) denotes the repeated prime. Put
\[
A=\sigma(p^2)=p^2+p+1.
\]
Then \(A\mid n^2\), and
\[
\gcd(A,p)=1.
\]
Thus every prime divisor of \(A\) is \(q\). Since \(A\) is odd, \(q\) is odd.

Also
\[
q+1\mid n^2.
\]
Because
\[
\gcd(q,q+1)=1,
\]
every prime divisor of \(q+1\) is \(p\). But \(q+1\) is even, so
\[
p=2.
\]
Therefore
\[
A=2^2+2+1=7.
\]
Since the only prime divisor of \(A\) is \(q\),
\[
q=7,
\]
and hence
\[
n=28.
\]
Indeed,
\[
\sigma(28)=56\mid784.
\]

It remains to consider the squarefree shape
\[
n=pqr
\]
with distinct primes
\[
p<q<r.
\]
Again \(p+1\mid n^2\). Its prime divisors can only be \(q\) or \(r\), because it is coprime to \(p\). Since
\[
1<p+1\le q<r,
\]
one must have
\[
p+1=q.
\]
Thus
\[
p=2,\qquad q=3.
\]
Now
\[
\sigma(n)=3\cdot4\cdot(r+1)=12(r+1)
\]
must divide
\[
n^2=36r^2.
\]
Consequently
\[
r+1\mid3r^2.
\]
As
\[
\gcd(r+1,r)=1,
\]
this forces
\[
r+1\mid3,
\]
impossible because \(r\ge5\).

Therefore the only solutions with \(n>1\) and \(\Omega(n)\le3\) are \(6\) and \(28\).

For sharpness of the non-perfect threshold,
\[
364=2^2\cdot7\cdot13
\]
has
\[
\Omega(364)=4
\]
and
\[
\sigma(364)=\sigma(2^2)\sigma(7)\sigma(13)
=7\cdot8\cdot14=784.
\]
Since
\[
364^2=169\cdot784,
\]
it satisfies the divisibility, and since
\[
784\ne728,
\]
it is not perfect.

## Verification
The attached `verify.py` independently factors every integer through
\[
1{,}000{,}000,
\]
computes \(\sigma(n)\) and \(\Omega(n)\) exactly, and checks the theorem's low-multiplicity statement directly.

It also searches the same finite range for the least multiplicity of a non-perfect member and confirms that the first such multiplicity is \(4\), attained by \(364\).

The finite computation is corroborative only. The unbounded theorem follows from the exhaustive factorization-shape proof above.

## Relationship to prior work
OEIS A090777 is the exact database sequence defined by
\[
\sigma(n)\mid n^2.
\]
Its displayed terms begin
\[
1,6,28,120,364,496,\ldots
\]
and it supplies computational programs, but it does not state a classification by \(\Omega(n)\), semiprime shape, or the sharp non-perfect multiplicity threshold.

OEIS A245787 studies the strictly smaller set defined by
\[
\tau(n)\sigma(n)\mid n^2
\]
and explicitly identifies it as a subsequence of A090777. That stronger divisibility condition does not classify the low-\(\Omega\) layers of A090777.

Amdeberhan, Moll, Sharma and Villamizar study prime-adic valuations of \(\sigma(n)\). Their formulas describe
\[
\nu_p(\sigma(n))
\]
from the prime factorization of \(n\) and provide broad valuation bounds. Those results give useful context for prime-support restrictions but do not state or imply the complete \(\Omega(n)\le3\) classification above.

Targeted searches for the exact divisibility, semiprime and three-factor restrictions, the A090777 identifier, and the values \(6,28,364\) did not locate a published theorem equivalent to or stronger than this multiplicity-layer result.

## Limitations
The theorem does not classify any full layer with
\[
\Omega(n)\ge4.
\]
In particular, it does not determine all non-perfect solutions at the sharp boundary \(\Omega(n)=4\).

Because the proof is elementary and the exact sequence has been public for many years, an equivalent observation may exist in an unindexed note, problem discussion, or private computation not surfaced by the searches.

## References
1. OEIS Foundation, A090777, “Numbers \(k\) such that \(\sigma(k)\) divides \(k^2\),” entry authored 8 February 2004.
2. OEIS Foundation, A245787, “Numbers \(n\) such that \(\tau(n)\sigma(n)\) divides \(n^2\),” entry authored 8 August 2014.
3. T. Amdeberhan, V. H. Moll, V. Sharma and D. Villamizar, “Arithmetic properties of the sum of divisors,” arXiv:2007.03088v1, first posted 6 July 2020; *Journal of Number Theory* 223 (2021), 343–362.
