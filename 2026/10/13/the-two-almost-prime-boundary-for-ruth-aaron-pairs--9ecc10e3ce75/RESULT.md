# The two-almost-prime boundary for Ruth–Aaron pairs
## Finding
Let
\[
S(n)=\sum_{p^a\parallel n}ap
\]
be the sum of the prime factors of \(n\), counted with multiplicity, and let
\[
\Omega(n)=\sum_{p^a\parallel n}a.
\]
If
\[
S(n)=S(n+1)
\]
and
\[
\Omega(n)\le2,\qquad \Omega(n+1)\le2,
\]
then
\[
n=5.
\]
Equivalently, the only Ruth–Aaron pair whose two members are each prime or semiprime is
\[
(5,6).
\]
In particular, no two consecutive semiprimes form a Ruth–Aaron pair.

The bound is sharp in prime-factor depth: the next possible value of the larger multiplicity is \(3\), and
\[
S(8)=2+2+2=6=S(9)=3+3,
\]
so \((8,9)\) is a Ruth–Aaron pair with
\[
\max\{\Omega(8),\Omega(9)\}=3.
\]

## Assumptions and scope
A prime has \(\Omega=1\). A semiprime has \(\Omega=2\), allowing a prime square.
The theorem concerns the ordinary Ruth–Aaron convention in which repeated prime factors are counted repeatedly in \(S\).

The statement is unrestricted in size. It classifies the complete layer
\[
\max\{\Omega(n),\Omega(n+1)\}\le2.
\]
It does not classify Ruth–Aaron pairs once one member has at least three prime factors counted with multiplicity.

## Proof
Assume first that one member is prime.

If \(n=p\) is prime and \(n+1=ab\) is semiprime, where \(a,b\) are primes and repetition is allowed, then the Ruth–Aaron equation gives
\[
p=a+b.
\]
Since also
\[
ab=p+1,
\]
we obtain
\[
ab=a+b+1,
\]
so
\[
(a-1)(b-1)=2.
\]
Because \(a,b\) are primes, the only possibility is
\[
\{a,b\}=\{2,3\},
\]
and hence
\[
p=5.
\]
This gives the pair \((5,6)\).

If instead \(n=ab\) is semiprime and \(n+1=p\) is prime, then
\[
p=a+b
\]
and
\[
ab+1=p.
\]
Therefore
\[
ab+1=a+b,
\]
which is equivalent to
\[
(a-1)(b-1)=0.
\]
This is impossible for primes \(a,b\ge2\).

Two consecutive primes can only be \(2\) and \(3\), and their prime-factor sums are unequal. Thus the only Ruth–Aaron pair in which at least one member is prime and both members satisfy \(\Omega\le2\) is \((5,6)\).

It remains to exclude the case in which both members are semiprime. Write
\[
n=ab,\qquad n+1=cd,
\]
where
\[
a\le b,\qquad c\le d
\]
are primes, with equality allowed. The Ruth–Aaron condition is
\[
a+b=c+d.
\]
Put
\[
t=c-a.
\]
Then
\[
d=b-t.
\]
Using \(cd-ab=1\), we find
\[
1=(a+t)(b-t)-ab=t(b-a-t).
\]
Both factors on the right are integers. Hence either
\[
t=1,\qquad b-a-t=1,
\]
or
\[
t=-1,\qquad b-a-t=-1.
\]

The second alternative gives
\[
b-a=-2,
\]
contradicting \(a\le b\).

In the first alternative,
\[
b=a+2,
\]
and
\[
c=d=a+1.
\]
Thus both \(a\) and \(a+1\) are prime. The only consecutive primes are \(2\) and \(3\), so \(a=2\). But then
\[
b=a+2=4,
\]
which is not prime. This contradiction excludes the semiprime-semiprime case.

Therefore \((5,6)\) is the unique Ruth–Aaron pair with both multiplicities at most \(2\).

Finally,
\[
S(8)=6=S(9),
\]
so the multiplicity bound \(2\) is best possible.

## Verification
The proof is symbolic and exhaustive. The accompanying checker verifies each algebraic reduction and independently computes \(S(n)\) and \(\Omega(n)\) for every
\[
1\le n\le2{,}000{,}000.
\]
It confirms that the only Ruth–Aaron pair in that range with both multiplicities at most \(2\) is \((5,6)\), and that \((8,9)\) realizes the sharp next layer.

The finite computation is corroborative only. The unrestricted theorem follows from the case split and the integer factorization
\[
t(b-a-t)=1.
\]

## Relationship to prior work
Pomerance's paper on Ruth–Aaron numbers uses the same multiplicity function \(S\) and proves global sparsity results for the full sequence. Its focus is asymptotic counting rather than a classification by a bounded number of prime factors.

Iannucci and Mintos study a different variant, using the sum \(P(n)\) of distinct prime divisors. Their complete 2005 paper explicitly contrasts \(P\) with the ordinary multiplicity function \(S\). Their Theorem 1 classifies the distinct-prime variant when the numbers of distinct prime factors are \(1\) and \(2\), and their parity observation already rules out the squarefree-squarefree subcase with two distinct prime factors on each side. Those results do not cover the ordinary multiplicity problem when prime squares are allowed, nor do they state the full \(\Omega\le2\) classification above.

OEIS A039752 records the ordinary multiplicity Ruth–Aaron numbers, beginning with
\[
5,8,15,77,125,714,\ldots.
\]
The table is consistent with the theorem but cannot prove that no arbitrarily large pair lies in the two-almost-prime layer.

## Limitations
The theorem says nothing about the distribution of Ruth–Aaron pairs once
\[
\max\{\Omega(n),\Omega(n+1)\}\ge3.
\]
It does not address the open infinitude question for Ruth–Aaron pairs.

The 1974 paper that introduced the phenomenon predates the exact-day source used in the metadata, but the inspected bibliographic records give only its journal year and issue. The earliest exact public calendar date verified here for a directly relevant primary paper is 29 June 2005.

Pomerance's 2002 full paper was inspected for its abstract, introduction, and global theorem context, together with targeted full-document term searches; because its machine text is partially corrupted, no whole-document noncoverage claim is based on those term searches alone.

## References
1. D. E. Iannucci and A. S. Mintos, "On consecutive integer pairs with the same sum of distinct prime divisors", *INTEGERS* 5 (2005), Article A12, published 29 June 2005.
2. C. Pomerance, "Ruth–Aaron numbers revisited", in *Paul Erdős and His Mathematics I*, Bolyai Society Mathematical Studies 11 (2002), 567–579.
3. C. Nelson, D. E. Penney and C. Pomerance, "714 and 715", *Journal of Recreational Mathematics* 7(2) (1974), 87–89.
4. OEIS Foundation, A039752, "Ruth–Aaron numbers (2)".
