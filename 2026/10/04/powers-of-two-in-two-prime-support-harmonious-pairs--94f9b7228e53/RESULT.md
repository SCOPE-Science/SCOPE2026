# Powers of two in two-prime-support harmonious pairs

## Finding
A pair of positive integers \((x,y)\) is harmonious (also called feebly amicable) when
\[
\frac{x}{\sigma(x)}+\frac{y}{\sigma(y)}=1.
\]
Let \(a,b\ge1\), and let \(q\) be an odd prime. Then
\[
\left(2^a,2^bq\right)
\]
is harmonious if and only if
\[
a=b
\]
and
\[
q=2^a-1
\]
is prime.

Equivalently, the harmonious pairs in this entire slice are exactly
\[
\left(2^a,2^a(2^a-1)\right)
\]
for Mersenne primes \(2^a-1\).

For example, the first cases are
\[
(4,12),\qquad(8,56),\qquad(32,992).
\]

## Assumptions and scope
The result concerns pairs in which one member is a power of two and the other has exactly the two prime divisors \(2\) and an odd prime \(q\), with the odd prime appearing to the first power. No ordering of the two members is assumed in the definition; for every surviving case with \(a\ge2\), the second member is larger.

The theorem does not classify harmonious pairs \((2^a,m)\) for arbitrary \(m\), nor pairs in which the odd prime occurs with exponent greater than one.

## Proof
Put
\[
A=2^a,\qquad B=2^b.
\]
Since \(q\) is odd,
\[
\sigma(A)=2A-1
\]
and
\[
\sigma(Bq)=(2B-1)(q+1).
\]
The harmonious equation becomes
\[
\frac{A}{2A-1}+\frac{Bq}{(2B-1)(q+1)}=1.
\]
After moving the first term to the right and clearing denominators,
\[
Bq(2A-1)=(A-1)(2B-1)(q+1).
\]
Collecting the terms containing \(q\) gives
\[
q(A+B-1)=(A-1)(2B-1).
\]
Set
\[
D=A+B-1.
\]
Then
\[
D\mid(A-1)(2B-1).
\]
But
\[
\gcd(D,A-1)=\gcd(B,A-1)=1,
\]
because \(B\) is a power of two while \(A-1\) is odd. Hence
\[
D\mid 2B-1.
\]
Since
\[
2D-(2B-1)=2A-1,
\]
we also have
\[
D\mid2A-1.
\]
Positivity now gives
\[
A+B-1=D\le2B-1,
\]
so \(A\le B\), while
\[
A+B-1=D\le2A-1
\]
gives \(B\le A\). Therefore
\[
A=B,
\]
so \(a=b\). Substituting into the collected equation yields
\[
q(2A-1)=(A-1)(2A-1),
\]
and hence
\[
q=A-1=2^a-1.
\]
Because \(q\) is assumed prime, \(2^a-1\) must be a Mersenne prime.

Conversely, if \(q=2^a-1\) is prime and \(b=a\), then substituting into the displayed rational identity gives equality, so \((2^a,2^a(2^a-1))\) is harmonious. This proves the classification.

## Verification
The accompanying `verify.py` checks the algebraic identity exactly with rational arithmetic, verifies the first known Mersenne-prime instances, and exhaustively tests all triples \((a,b,q)\) with \(1\le a,b\le12\) and odd primes \(q<5000\). Every computational solution satisfies \(a=b\) and \(q=2^a-1\).

The finite replay is only a regression check. Exhaustiveness for arbitrary \(a,b,q\) is supplied by the divisibility argument in the proof.

## Relationship to prior work
Kozek, Luca, Pollack, and Pomerance introduced the term harmonious pair and proved a global density upper bound for integers belonging to such pairs. Their paper gives \((4,12)\) as the opening example, but targeted full-text searches for Mersenne terminology and powers of two did not locate the classification above.

Bishop, Bozarth, Kuss, and Peet later used the synonymous term feebly amicable, developed elementary abundancy-index criteria, tabulated initial pairs, and posed further questions about the structure and distribution of these pairs. Their first public preprint appeared on 23 April 2021 and lists MSC 11A99.

OEIS A253534 and A253535 tabulate members of harmonious pairs and record examples such as \((4,12)\) and \((8,56)\), but the current entries do not state the all-exponent Mersenne characterization for pairs of the form \((2^a,2^bq)\).

Targeted searches for “feebly amicable powers of two,” “harmonious pair Mersenne,” and the structural form \((2^a,2^bq)\) did not locate a prior statement of this exact classification.

## Limitations
The theorem treats a deliberately structured two-prime-support slice. It does not determine all friends of a power of two, and it does not address odd-prime powers \(q^c\) with \(c>1\).

Literature non-detection is not a proof that an unindexed or unpublished argument is absent.

## References
1. Jamie Bishop, Abigail Bozarth, Rebekah Kuss, and Benjamin Peet, “The Abundancy Index and Feebly Amicable Numbers,” arXiv:2104.11366v1, first posted 23 April 2021.
2. Mark Kozek, Florian Luca, Paul Pollack, and Carl Pomerance, “Harmonious Pairs,” *International Journal of Number Theory* 11 (2015), 1633–1651.
3. OEIS A253534 and A253535, harmonious-pair member sequences.
