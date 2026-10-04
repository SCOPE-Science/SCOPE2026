# The mixed-sign two-divisor equation on squarefree \(2pq\)

## Finding
Let \(p<q\) be odd primes and put
\[
n=2pq.
\]
There exist distinct positive divisors \(d_1,d_2\mid n\) satisfying
\[
\sigma(n)=2n+d_1-d_2
\]
if and only if
\[
n\in\{30,42,70,78,110,130,154,170\}.
\]

Explicit ordered witnesses \((d_1,d_2)\) are
\[
\begin{array}{c|c}
n&(d_1,d_2)\\ \hline
30&(15,3)\\
42&(14,2)\\
70&(5,1)\\
78&(13,1)\\
110&(1,5)\\
130&(2,10)\\
154&(2,22)\\
170&(1,17).
\end{array}
\]

Thus the mixed-sign variant proposed in the \(2\)-near-perfect literature has a complete answer on the first squarefree family with three distinct prime factors.

## Assumptions and scope
The divisor-sum function is
\[
\sigma(n)=\sum_{d\mid n}d.
\]
The two divisors in the mixed-sign equation are required to be positive, distinct divisors of \(n\). They are not assumed proper a priori.

The theorem is restricted to squarefree even integers with exactly three prime factors,
\[
n=2pq,
\]
where \(p<q\) are odd primes. It does not classify the nonsquarefree family \(2^a p^b q^c\).

## Proof
For
\[
n=2pq
\]
one has
\[
\sigma(n)=3(p+1)(q+1).
\]
Hence the required difference is
\[
D:=d_1-d_2=\sigma(n)-2n=-pq+3p+3q+3.
\]

We split according to the smaller odd prime \(p\).

### Case \(p=3\)

Here
\[
D=12.
\]
The divisors of \(6q\) consist of
\[
\{1,2,3,6\}
\]
and their \(q\)-multiples.

Two divisors from the first set differ by at most \(5\), so they cannot have difference \(12\). Two \(q\)-multiples have difference divisible by \(q\), which would force \(q\mid12\), impossible for a prime \(q>3\). Hence exactly one divisor is a \(q\)-multiple. Since the difference is positive, it must be \(d_1\). Write
\[
d_1=tq,\qquad d_2=s,
\]
with
\[
s,t\in\{1,2,3,6\}.
\]
Then
\[
tq-s=12,
\qquad
q=\frac{12+s}{t}.
\]
Enumerating the sixteen pairs \((s,t)\) gives precisely
\[
(t,s,q)=(3,3,5),(2,2,7),(1,1,13).
\]
Thus
\[
n\in\{30,42,78\}.
\]

### Case \(p=5\)

Now
\[
D=18-2q.
\]
If \(q=7\), then \(D=4\) and the pair
\[
(d_1,d_2)=(5,1)
\]
works, giving \(n=70\).

Assume \(q\ge11\). Put
\[
E:=-D=2q-18>0.
\]
Then
\[
d_2-d_1=E.
\]
The divisors not involving \(q\) are
\[
\{1,2,5,10\}.
\]

If both \(d_1,d_2\) are chosen from this set, then \(E\le9\), so \(q\le13\). The primes \(q=11,13\) both work:
\[
q=11:\quad 5-1=4=E,
\]
\[
q=13:\quad 10-2=8=E.
\]

If both are \(q\)-multiples, then \(q\mid E\), hence \(q\mid18\), impossible for \(q\ge11\).

In the remaining case the larger divisor \(d_2\) must be the \(q\)-multiple. Write
\[
d_2=tq,\qquad d_1=s,
\]
with
\[
s,t\in\{1,2,5,10\}.
\]
Then
\[
tq-s=2q-18,
\]
or
\[
(t-2)q=s-18.
\]
For \(t=1\), this gives
\[
q=18-s,
\]
yielding the prime values \(q=17\) when \(s=1\) and \(q=13\) when \(s=5\). For \(t=2\) one would need \(s=18\), and for \(t=5,10\) the two sides have opposite signs. Therefore
\[
q\in\{7,11,13,17\},
\]
giving
\[
n\in\{70,110,130,170\}.
\]

### Case \(p=7\)

Here
\[
D=24-4q<0
\]
for every prime \(q>7\). Put
\[
E=4q-24=d_2-d_1.
\]
The non-\(q\) divisors are
\[
\{1,2,7,14\}.
\]
For \(q\ge11\), one has \(E\ge20\), larger than every difference between two members of this set. Two \(q\)-multiples would force
\[
q\mid E,
\]
hence \(q\mid24\), impossible.

Thus \(d_2=tq\) and \(d_1=s\) with
\[
s,t\in\{1,2,7,14\}.
\]
The equation becomes
\[
(t-4)q=s-24.
\]
Because the right side is negative, only \(t=1,2\) are possible. The case \(t=1\) gives no integral prime \(q>7\), while \(t=2\) gives the unique solution
\[
s=2,\qquad q=11.
\]
Hence the only solution here is
\[
n=154.
\]

### Case \(p\ge11\)

Then \(q\ge13\), and
\[
D<0.
\]
Set
\[
E:=-D=pq-3p-3q-3=d_2-d_1.
\]
The non-\(q\) divisors are
\[
\{1,2,p,2p\}.
\]
Moreover,
\[
E-(2p-1)
=
pq-5p-3q-2
=
q(p-3)-5p-2
>0,
\]
because at the smallest possible pair \(p=11,q=13\) the right side is already \(47\), and it increases thereafter. Hence two non-\(q\) divisors cannot differ by \(E\).

Two \(q\)-multiples cannot work either: that would imply
\[
q\mid E.
\]
But
\[
E\equiv-3(p+1)\pmod q,
\]
and \(q>p+1\) with \(q>3\), so this divisibility is impossible.

Thus exactly one of the two divisors is a \(q\)-multiple. Since
\[
E>2p-1,
\]
the larger divisor \(d_2\) must be the \(q\)-multiple. Write
\[
d_2=tq,\qquad d_1=s,
\]
where
\[
s,t\in\{1,2,p,2p\}.
\]
Then
\[
(t-p+3)q=s-3p-3.
\]
The right side is negative, so \(t<p-3\). Therefore only \(t=1\) or \(t=2\) can occur.

If \(t=1\), then
\[
(p-4)q=3p+3-s\le3p+2.
\]
But \(q>p\), so
\[
(p-4)q>p(p-4)\ge7p>3p+2,
\]
a contradiction.

If \(t=2\), then
\[
(p-5)q=3p+3-s\le3p+2,
\]
while
\[
(p-5)q>p(p-5)\ge6p>3p+2,
\]
again a contradiction.

Thus there are no solutions with \(p\ge11\).

Combining the four cases gives exactly
\[
30,42,70,78,110,130,154,170.
\]
Direct substitution of the displayed witness pairs proves sufficiency.

## Verification
The accompanying `verify.py` checks every displayed witness directly from
\[
\sigma(2pq)=3(p+1)(q+1).
\]
It also reproduces the finite parameter reductions in the \(p=3,5,7\) cases from the symbolic equations in the proof and performs an independent bounded regression over all odd prime pairs below \(2000\). The regression finds exactly the eight stated values in that range.

The bounded regression is not used for the infinite exclusion. The proof for \(p\ge11\) is symbolic, and the \(p=3,5,7\) branches reduce to finite algebraic cases without a search cutoff.

## Relationship to prior work
Aryan, Madhavani, Parikh, Slattery, and Zelinsky introduced a systematic study of \(2\)-near-perfect numbers satisfying
\[
\sigma(n)=2n+d_1+d_2.
\]
In their open-problems section they explicitly proposed changing the signs, including
\[
\sigma(n)=2n+d_1-d_2,
\]
and remarked that the mixed-sign situation might be more difficult.

A later paper by Fearon, Foushee, Porosoff, Skula, Zelinsky, and Zhang completes the ordinary \(2\)-near-perfect classification with exactly two distinct prime factors and proves a theorem for the two-minus-sign variant. Its future-work section again identifies the one-plus-one-minus equation as “Hybrid \(2\)-near Perfect Numbers” and reports only initial computations, not a classification. This later source therefore strengthens the motivation and does not imply the squarefree \(2pq\) theorem above.

Targeted searches for the exact equation, the structural family \(2pq\), the eight-value set, and the phrase “Hybrid \(2\)-near Perfect Numbers” did not locate a prior complete classification. Semantic database searches returned related deficient-perfect, near-perfect, Zumkeller, and other divisor-sum results, but no statement implying this mixed-sign theorem.

## Limitations
The theorem concerns only the squarefree family \(2pq\). It does not classify hybrid solutions of the general form
\[
2^a p^b q^c
\]
or solutions with more prime factors.

The literature search cannot rule out an unindexed or unpublished proof of the same squarefree slice.

## References
1. Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery, and Joshua Zelinsky, “On \(2\)-Near Perfect Numbers,” arXiv:2310.01305v1, first posted 2 October 2023; *Integers* 24 (2024), Article A61.
2. Richard Fearon, Henry Foushee, Benjamin Porosoff, Alexander Skula, Joshua Zelinsky, and Kyle Zhang, “Complete characterization of \(2\)-near perfect numbers with exactly \(2\) prime factors,” arXiv:2508.06651v1, first posted 8 August 2025.
