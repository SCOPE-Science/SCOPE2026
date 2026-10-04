# The unique semiprime in Tóth's auxiliary set is \(15\)

## Finding
Let \(\mathcal S\) be the set of odd positive integers \(n\) satisfying
\[
\frac{2n}{\sigma(n)}-1=\frac1x
\]
for some positive integer \(x\).

Then the only semiprime in \(\mathcal S\) is
\[
15=3\cdot5.
\]
Indeed,
\[
\sigma(15)=24
\]
and
\[
\frac{30}{24}-1=\frac14.
\]

Equivalently, every composite \(n\in\mathcal S\) other than \(15\) satisfies
\[
\Omega(n)\ge3.
\]

## Assumptions and scope
A semiprime means a product of exactly two primes counted with multiplicity, so an odd semiprime is either \(pq\) for distinct odd primes \(p<q\), or \(p^2\) for an odd prime \(p\).

The theorem concerns Tóth's auxiliary set \(\mathcal S\), introduced in the study of spoof odd perfect numbers. It does not classify all members of \(\mathcal S\), and it does not address the density conjectures for that set.

## Proof
The defining equation is equivalent to
\[
x\bigl(2n-\sigma(n)\bigr)=\sigma(n).
\]

First let
\[
n=pq
\]
with distinct odd primes \(p<q\). Then
\[
\sigma(n)=(p+1)(q+1)
\]
and
\[
d:=2n-\sigma(n)=pq-p-q-1.
\]
Membership in \(\mathcal S\) requires
\[
x=\frac{(p+1)(q+1)}{pq-p-q-1}
\]
to be a positive integer.

Since
\[
(p+1)(q+1)-(pq-p-q-1)=2p+2q+2>0,
\]
one has \(x>1\). Also \(p\ge3\) and \(q\ge5\), and
\[
4d-\sigma(n)=3pq-5p-5q-5.
\]
The right-hand side is \(0\) at \((p,q)=(3,5)\), and is strictly increasing in either variable throughout \(p\ge3,\ q\ge5\). Hence
\[
x\le4.
\]
Therefore
\[
x\in\{2,3,4\}.
\]

If \(x=2\), then
\[
(p-3)(q-3)=12.
\]
Both factors are positive even integers. The only ordered even factorization compatible with \(p<q\) is \(2\cdot6\), which would give \(p=5,\ q=9\), impossible because \(q\) is prime.

If \(x=3\), then
\[
(p-2)(q-2)=6.
\]
Both factors are odd, whereas their product is even, so this is impossible.

If \(x=4\), then
\[
(3p-5)(3q-5)=40.
\]
Each factor is positive and congruent to \(1\pmod3\). Among complementary positive divisors of \(40\), the only ordered pair with both factors congruent to \(1\pmod3\) and arising from odd primes is
\[
(3p-5,3q-5)=(4,10),
\]
which gives
\[
(p,q)=(3,5).
\]
Thus the distinct-prime case yields only \(n=15\).

Now let
\[
n=p^2
\]
for an odd prime \(p\). Then
\[
\sigma(n)=p^2+p+1,
\qquad
d=2p^2-\sigma(n)=p^2-p-1.
\]
For \(p=3\),
\[
\frac{\sigma(n)}d=\frac{13}{5}
\]
is not an integer. For every \(p\ge5\),
\[
d<\sigma(n)<2d,
\]
because
\[
\sigma(n)-d=2p+2>0
\]
and
\[
2d-\sigma(n)=p^2-3p-3>0.
\]
Thus \(1<\sigma(n)/d<2\), so it cannot equal a positive integer \(x\).

No prime square lies in \(\mathcal S\). Combining the two cases proves that \(15\) is the unique semiprime in \(\mathcal S\).

## Verification
The accompanying `verify.py` checks every algebraic branch exactly. It enumerates the divisor factorizations occurring for \(x=2,3,4\), verifies the prime-square inequalities, and directly checks that \(15\) satisfies the defining equation with \(x=4\).

As a regression check only, it also enumerates odd semiprimes up to \(200000\) and confirms that \(15\) is the sole member of \(\mathcal S\) in that range. The finite census is not used for the infinite theorem.

A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Tóth defines \(\mathcal S\) by the same reciprocal abundancy equation and studies it because its members supply the ordinary components used in spoof odd perfect numbers. The paper reports a large computation of \(\mathcal S\) and notes the lack of a sufficiently developed theoretical framework that would avoid brute-force testing. It does not state a semiprime classification.

OEIS A222263 records the same set. Its initial terms include \(15\), and its example verifies the value \(x=4\) for \(15\), but the entry does not state that \(15\) is the unique semiprime.

Targeted searches for semiprimes in A222263, for the structural form \(pq\), for the reciprocal equation restricted to two prime factors, and for the exact assertion that \(15\) is unique did not locate a prior theorem.

## Limitations
This theorem settles only the first nontrivial factor-count layer. It does not classify members with three or more prime factors, nor does it improve the known density bounds for \(\mathcal S\).

Failure to locate an indexed equivalent statement is not a proof that none exists in unpublished or unindexed work.

## References
1. László Tóth, “On the Density of Spoof Odd Perfect Numbers,” arXiv:2101.09718v1, first posted 24 January 2021; *Computational Methods in Science and Technology* 27 (2021).
2. OEIS A222263, odd positive integers \(n\) such that \(2n/\sigma(n)-1\) is the reciprocal of a positive integer.
