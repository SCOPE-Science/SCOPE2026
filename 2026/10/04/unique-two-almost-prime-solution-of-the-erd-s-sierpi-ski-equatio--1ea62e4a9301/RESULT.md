# Unique two-almost-prime solution of the Erdős–Sierpiński equation
## Finding
Let \(\Omega(m)\) denote the number of prime factors of \(m\), counted with
multiplicity. If
\[
\sigma(n)=\sigma(n+1),
\qquad
\Omega(n)\le2,
\qquad
\Omega(n+1)\le2,
\]
then
\[
n=14.
\]
Hence
\[
\sigma(14)=\sigma(15)=24
\]
is the unique Erdős–Sierpiński solution in which both consecutive integers
have at most two prime factors counted with multiplicity.

## Assumptions and scope
The function
\[
\sigma(m)=\sum_{d\mid m}d
\]
is the ordinary sum-of-positive-divisors function. The convention
\(\Omega(1)=0\) is harmless; \(n=1\) does not satisfy the equation.

The restriction \(\Omega\le2\) is a multiplicative-complexity restriction.
A composite integer in this layer is either a prime square \(p^2\) or a
product \(pq\) of two distinct primes.

## Proof
First, neither \(n\) nor \(n+1\) can be prime.

If \(n=p\) is prime, then
\[
\sigma(n)=p+1=n+1,
\]
whereas
\[
\sigma(n+1)\ge n+2.
\]
If \(n+1=p\) is prime and \(n>1\) is composite, then \(n\) has a proper
divisor \(d\ge2\), so
\[
\sigma(n)\ge1+d+n\ge n+3>n+2=\sigma(n+1).
\]
The remaining endpoint \(n=1\) also fails directly.

Therefore both \(n\) and \(n+1\) are composite, and under the hypotheses
both have \(\Omega=2\). Let \(E\) be the even member and \(O\) the odd
member.

The exceptional even number \(E=4\) has a prime neighbor, already excluded.
Thus
\[
E=2p
\]
for an odd prime \(p\), and
\[
\sigma(E)=3(p+1).
\]

The odd composite \(O\) is either a prime square or a product of two distinct
odd primes.

Suppose first that
\[
O=q^2.
\]
If \(O=E+1\), then \(q^2=2p+1\), so
\[
p=\frac{q^2-1}{2}.
\]
The equality of divisor sums gives
\[
3(p+1)=q^2+q+1,
\]
hence
\[
q^2-2q+1=0,
\]
forcing \(q=1\), impossible.

If \(O=E-1\), then
\[
p=\frac{q^2+1}{2},
\]
and the same divisor-sum equality becomes
\[
q^2-2q+7=0,
\]
which has no real, hence no prime, solution.

It remains to take
\[
O=qr
\]
with distinct odd primes \(q<r\). Then
\[
\sigma(O)=(q+1)(r+1).
\]

If \(O=E+1\), then
\[
p=\frac{qr-1}{2}.
\]
Equating divisor sums gives
\[
\frac{3(qr+1)}2=(q+1)(r+1),
\]
or
\[
(q-2)(r-2)=3.
\]
Because \(q<r\) are odd primes, the only possibility is
\[
q=3,\qquad r=5.
\]
Then \(p=7\), so
\[
E=14,\qquad O=15.
\]

If \(O=E-1\), then
\[
p=\frac{qr+1}{2},
\]
and equality of divisor sums gives
\[
\frac{3(qr+3)}2=(q+1)(r+1),
\]
or
\[
(q-2)(r-2)=-3,
\]
impossible because both factors on the left are positive.

Thus the only solution in the stated multiplicative layer is
\[
(n,n+1)=(14,15).
\]

## Verification
The proof above is unrestricted and exhaustive.

The accompanying checker independently computes \(\Omega(m)\) and
\(\sigma(m)\) through \(10^6+1\) by a smallest-prime-factor sieve, examines
every consecutive pair with both \(\Omega\)-values at most \(2\), and confirms
that the only equal-divisor-sum pair is \((14,15)\). This finite computation is
corroborative only and is not used to infer the unrestricted theorem.

## Relationship to prior work
Guy and Shanks gave a one-page construction paper for solutions of
\[
\sigma(n)=\sigma(n+1).
\]
Their displayed list begins with \(n=14\), and one of their parametric forms is
\[
n=2p,\qquad n+1=3^m q.
\]
The case \(m=1\) yields \(14,15\). Their paper constructs selected solutions
and does not classify all solutions by total prime-factor count.

Benito later tabulated \(1268\) solutions through
\(1.5\cdot10^{10}\), again beginning with \(14,15\), and proved parity
properties of the common divisor sum. The full text contains no occurrence of
"semiprime" or "prime factor" and does not state the two-almost-prime
classification.

Yamada and Weingartner study distribution and infinitude questions for
equations of the more general form
\[
\sigma(n)=\sigma(n+k).
\]
Yamada's arXiv record classifies this subject under MSC \(11A25\).
These distribution results do not imply the exact low-\(\Omega\)
classification proved here.

OEIS A002961 is the exact database of starting values \(n\) satisfying
\(\sigma(n)=\sigma(n+1)\). It lists \(14\) first and notes that in all
recorded cases both consecutive integers are composite, but it gives no
unrestricted theorem singling out \(14\) by the condition
\(\Omega(n),\Omega(n+1)\le2\).

## Limitations
The theorem says nothing about solutions once either member has three or more
prime factors counted with multiplicity. It does not address the central open
question of whether infinitely many solutions exist.

Some older computational papers cited by Guy--Shanks and later surveys are not
available in searchable full text here. They remain a residual originality
risk, although the fully inspected Guy--Shanks and Benito sources do not state
the classification.

The historical Guy--Shanks source is earlier than the exact-day source used in
metadata, but the inspected bibliographic evidence dates that issue only to
October 1974. The metadata therefore uses the earliest public source for this
problem for which an exact UTC calendar date was verified.

## References
1. R. K. Guy and D. Shanks, "A Constructed Solution of
   \(\sigma(n)=\sigma(n+1)\)", *The Fibonacci Quarterly* 12 (1974), 299,
   DOI 10.1080/00150517.1974.12430740.
2. L. Benito, "Solutions of the problem of Erdős--Sierpiński:
   \(\sigma(n)=\sigma(n+1)\)", arXiv:0707.2190v1, submitted
   15 July 2007.
3. T. Yamada, "On equations \(\sigma(n)=\sigma(n+k)\) and
   \(\varphi(n)=\varphi(n+k)\)", arXiv:1001.2511v1, submitted
   14 January 2010. MSC \(11A25\).
4. A. Weingartner, "On the Solutions of \(\sigma(n)=\sigma(n+k)\)",
   *Journal of Integer Sequences* 14 (2011), Article 11.5.5.
5. OEIS Foundation, A002961, "Numbers \(k\) such that \(k\) and \(k+1\)
   have same sum of divisors".
