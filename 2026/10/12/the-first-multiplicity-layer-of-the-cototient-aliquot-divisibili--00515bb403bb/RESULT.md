# The first multiplicity layer of the cototient–aliquot divisibility
## Finding
Let
\[
c(n)=n-\varphi(n)
\]
be the cototient and let
\[
s(n)=\sigma(n)-n
\]
be the aliquot sum.

Among composite integers satisfying
\[
c(n)\mid s(n),
\]
the minimum possible multiplicity
\[
\Omega(n)
\]
is
\[
3,
\]
and the unique boundary case is
\[
n=12.
\]

Equivalently, \(12\) is the only composite solution with
\[
\Omega(n)\le3.
\]
Every other composite solution therefore has
\[
\Omega(n)\ge4,
\]
and this second threshold is sharp because
\[
56=2^3\cdot7,
\qquad
c(56)=32,
\qquad
s(56)=64.
\]

## Assumptions and scope
The function \(\Omega(n)\) counts prime factors with multiplicity. The theorem concerns composite positive integers only.

The exact ambient database is OEIS A068418, whose defining condition is
\[
n-\varphi(n)\mid\sigma(n)-n.
\]
The closely related OEIS A068414 is the quotient-\(2\) subfamily
\[
\sigma(n)-n=2\bigl(n-\varphi(n)\bigr).
\]

No claim is made about a complete classification for
\[
\Omega(n)\ge4.
\]

## Proof
Every composite integer has
\[
\Omega(n)\ge2.
\]
We first exclude the entire layer
\[
\Omega(n)=2.
\]

If
\[
n=p^2
\]
for a prime \(p\), then
\[
c(n)=p
\]
and
\[
s(n)=p+1.
\]
Thus \(c(n)\nmid s(n)\).

If instead
\[
n=pq
\]
for distinct primes \(p<q\), then
\[
c(n)=pq-(p-1)(q-1)=p+q-1
\]
and
\[
s(n)=(p+1)(q+1)-pq=p+q+1.
\]
If \(c(n)\mid s(n)\), then
\[
p+q-1\mid2.
\]
But
\[
p+q-1\ge4,
\]
so this is impossible.

Now suppose
\[
\Omega(n)=3.
\]

For a prime cube
\[
n=p^3,
\]
one has
\[
c(n)=p^2
\]
and
\[
s(n)=p^2+p+1.
\]
Hence divisibility would force
\[
p^2\mid p+1,
\]
which is impossible.

Next consider
\[
n=p^2q
\]
with distinct primes \(p,q\), where \(p\) is the repeated prime. Direct calculation gives
\[
c(n)=p(p+q-1)
\]
and
\[
s(n)=p^2+pq+p+q+1.
\]
If \(c(n)\mid s(n)\), then in particular
\[
p\mid q+1.
\]
Write
\[
q+1=kp
\]
with a positive integer \(k\). Then
\[
s(n)=p\bigl(p+q+1+k\bigr),
\]
so the remaining divisibility is
\[
p+q-1\mid k+2.
\tag{1}
\]
Since
\[
q=kp-1,
\]
the divisor in (1) is
\[
p+q-1=p(k+1)-2.
\]
Both sides of (1) are positive, hence
\[
p(k+1)-2\le k+2,
\]
or
\[
k(p-1)+p\le4.
\tag{2}
\]
For primes \(p\ge3\), the left side of (2) is at least \(5\), impossible. Therefore
\[
p=2.
\]
Then (2) gives
\[
k\le2.
\]
Because \(q\ne2\) is prime,
\[
k=\frac{q+1}{2}\ge2,
\]
so
\[
k=2,\qquad q=3.
\]
Thus
\[
n=2^2\cdot3=12.
\]
Indeed,
\[
c(12)=12-\varphi(12)=8,
\qquad
s(12)=\sigma(12)-12=16,
\]
so \(12\) is a solution.

It remains to exclude the squarefree shape
\[
n=pqr
\]
with distinct primes
\[
p<q<r.
\]
Expansion gives
\[
c(n)=pq+pr+qr-p-q-r+1
\]
and
\[
s(n)=pq+pr+qr+p+q+r+1.
\]
Therefore any divisibility
\[
c(n)\mid s(n)
\]
would imply
\[
c(n)\mid2(p+q+r).
\tag{3}
\]

But
\[
c(n)-2(p+q+r)
=
pq+pr+qr-3p-3q-3r+1.
\]
For distinct primes the minimum occurs at
\[
(p,q,r)=(2,3,5),
\]
where the right side equals \(2\). It increases when any of \(p,q,r\) increases, because the corresponding coefficient is the sum of the other two primes minus \(3\), which is positive. Hence
\[
c(n)>2(p+q+r)>0.
\]
This contradicts (3).

Thus \(12\) is the unique composite solution with
\[
\Omega(n)\le3.
\]

Finally,
\[
56=2^3\cdot7
\]
has
\[
\Omega(56)=4,
\]
and
\[
\varphi(56)=24,\qquad
\sigma(56)=120,
\]
so
\[
56-\varphi(56)=32
\]
and
\[
\sigma(56)-56=64=2\cdot32.
\]
Therefore the lower bound \(\Omega(n)\ge4\) for every solution other than \(12\) is sharp.

## Verification
The attached `verify.py` independently factors every composite integer
\[
4\le n\le1{,}000{,}000
\]
with
\[
\Omega(n)\le3,
\]
computes \(\sigma(n)\) and \(\varphi(n)\) exactly, and tests the defining divisibility.

It confirms that the complete finite hit set in this range is
\[
\{12\}.
\]
It separately checks the sharpness witness \(56\).

The finite computation is corroborative only. The unrestricted classification follows from the exhaustive factorization-shape proof above.

## Relationship to prior work
OEIS A068418 is the exact database sequence of composite integers satisfying
\[
n-\varphi(n)\mid\sigma(n)-n.
\]
Its displayed terms begin
\[
12,\ 56,\ 260,\ 992,\ 1320,\ldots
\]
and its comments give infinite-looking construction patterns, but the inspected entry does not state a multiplicity-layer classification.

OEIS A068414 is the quotient-\(2\) subfamily
\[
\sigma(n)=3n-2\varphi(n).
\]
It begins
\[
1,\ 12,\ 56,\ 260,\ 992,\ldots
\]
and records a Mersenne-prime construction, but again does not state the theorem above.

Erdős studied the two functions
\[
\sigma(n)-n
\quad\text{and}\quad
n-\varphi(n)
\]
as value-distribution objects. His 1973 paper treats their ranges and density questions separately; it does not impose divisibility between the two values.

Pomerance and Yang later revisited these same functions from the viewpoint of their ranges and algorithms for missing values. Their work has primary Mathematics Subject Classification \(11A25\), but does not state the low-\(\Omega\) divisibility classification proved here.

Targeted searches for the exact divisibility, its cototient/aliquot aliases, the database identifier, and the low-multiplicity formulation found no equivalent or stronger theorem.

## Limitations
The theorem determines only the first multiplicity layer and the sharp next threshold. It does not classify the full layer
\[
\Omega(n)=4.
\]

The main originality risk is an unindexed elementary observation about A068418. The exact database entries and the inspected literature on the two component functions do not expose such a statement.

## References
1. OEIS Foundation, A068418, composite integers \(n\) such that \(n-\varphi(n)\) divides \(\sigma(n)-n\), entry authored 3 March 2002.
2. OEIS Foundation, A068414, integers satisfying \(\sigma(n)=3n-2\varphi(n)\), entry authored 3 March 2002.
3. P. Erdős, “Über die Zahlen der Form \(\sigma(n)-n\) und \(n-\varphi(n)\),” *Elemente der Mathematik* 28 (1973), 83–86.
4. C. Pomerance and H.-S. Yang, “Variant of a theorem of Erdős on the sum-of-proper-divisors function,” *Mathematics of Computation* 83 (2014), 1903–1913, DOI 10.1090/S0025-5718-2013-02775-5.
