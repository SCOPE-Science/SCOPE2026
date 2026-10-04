# Strongly pseudoperfect integers with \(\Omega(n)\le3\)

## Finding
A positive integer \(n\) is strongly pseudoperfect if there is a subset \(S\) of its positive divisors such that
\[
d\in S\quad\Longleftrightarrow\quad \frac{n}{d}\in S
\]
and
\[
\sum_{d\in S}d=2n.
\]

Let \(\Omega(n)\) count prime factors with multiplicity. Then the strongly pseudoperfect positive integers satisfying
\[
\Omega(n)\le3
\]
are exactly
\[
6\quad\text{and}\quad28.
\]

Both are perfect, so every non-perfect strongly pseudoperfect integer satisfies
\[
\Omega(n)\ge4.
\]
This is sharp: \(36=2^2\cdot3^2\) is non-perfect and strongly pseudoperfect because
\[
1+2+3+12+18+36=72=2\cdot36
\]
and the selected divisors occur in the complementary pairs
\[
(1,36),\quad(2,18),\quad(3,12).
\]

## Assumptions and scope
Only positive integers are considered. The function \(\Omega(n)\) counts prime factors with multiplicity, so the possibilities with \(\Omega(n)\le3\) are
\[
1,\quad p,\quad p^2,\quad pq,\quad p^3,\quad p^2q,\quad pqr,
\]
with distinct primes where appropriate.

The proof uses only the defining complementary-pair condition and the elementary necessary condition
\[
\sigma(n)\ge2n.
\]
It does not classify strongly pseudoperfect integers with four or more prime factors counted with multiplicity.

## Proof
Every strongly pseudoperfect integer satisfies
\[
\sigma(n)\ge2n,
\]
because its selected divisor sum is \(2n\) and all divisors are positive.

The integer \(1\) is not strongly pseudoperfect. A prime \(p\) is deficient, since
\[
\sigma(p)=p+1<2p.
\]
Likewise
\[
\sigma(p^2)=p^2+p+1<2p^2
\]
and
\[
\sigma(p^3)=p^3+p^2+p+1<2p^3.
\]

Now let \(n=pq\) with distinct primes \(p<q\). Abundance is necessary, so
\[
(p+1)(q+1)\ge2pq.
\]
Equivalently,
\[
(p-1)(q-1)\le2.
\]
Thus \(p=2\) and \(q=3\), giving \(n=6\). Since \(6\) is perfect, it is strongly pseudoperfect.

Next let
\[
n=p^2q
\]
with distinct primes \(p,q\). The necessary abundance inequality is
\[
(p^2+p+1)(q+1)\ge2p^2q,
\]
or
\[
q(p^2-p-1)\le p^2+p+1.
\]
If \(p\ge5\), the right-hand ratio is less than \(2\), so no prime \(q\) is possible. If \(p=3\), then \(q\le13/5\), hence \(q=2\). If \(p=2\), then \(q\le7\), hence
\[
q\in\{3,5,7\}.
\]
Therefore the only abundant candidates of this shape are
\[
12,\quad18,\quad20,\quad28.
\]

For a nonsquare \(p^2q\), a complement-closed divisor subset is a union of the three complementary divisor pairs. Their pair sums are easily checked:
\[
12:\quad13,\ 8,\ 7;
\]
\[
18:\quad19,\ 9,\ 11;
\]
\[
20:\quad21,\ 12,\ 9;
\]
\[
28:\quad29,\ 16,\ 11.
\]
No subset of the first three lists sums to \(24\), \(36\), or \(40\), respectively. For \(28\), all three pair sums total
\[
29+16+11=56=2\cdot28.
\]
Thus \(28\) is strongly pseudoperfect, in fact perfect.

It remains to eliminate squarefree integers
\[
n=pqr,\qquad p<q<r.
\]
The four complementary divisor-pair sums are
\[
A=1+pqr,\qquad B=p+qr,\qquad C=q+pr,\qquad D=r+pq.
\]
Since
\[
\frac{B+C+D}{pqr}
=
\frac1p+\frac1q+\frac1r+\frac1{pq}+\frac1{pr}+\frac1{qr}
\le
\frac12+\frac13+\frac15+\frac16+\frac1{10}+\frac1{15}<2,
\]
the sum \(B+C+D\) is strictly less than \(2pqr\). Hence any representation of \(2pqr\) must include \(A\), and the selected subset of \(\{B,C,D\}\) must sum to
\[
pqr-1.
\]

No single one of \(B,C,D\) can equal \(pqr-1\): for example,
\[
p+qr=pqr-1
\]
would give
\[
qr(p-1)=p+1,
\]
which is impossible, and the other two equations are analogous.

Suppose two pair sums are selected. The equation
\[
B+C=pqr-1
\]
becomes
\[
r(pq-p-q)=p+q+1.
\]
If \(p=2\), then
\[
r=1+\frac5{q-2},
\]
so integrality forces \(q\in\{3,7\}\), yielding no prime \(r>q\). If \(p\ge3\), then \(q\ge5\) and
\[
2(pq-p-q)>p+q+1,
\]
so the displayed equation would force \(r<2\), impossible.

The equation
\[
B+D=pqr-1
\]
is handled identically after interchanging \(q\) and \(r\): for \(p=2\) it gives
\[
q=1+\frac5{r-2},
\]
and for \(p\ge3\) it forces \(q<2\).

Finally,
\[
C+D=pqr-1
\]
becomes
\[
p(qr-q-r)=q+r+1.
\]
For \(p=2\), the left side after expansion has even parity while the right-side equation is equivalent to
\[
2qr-3q-3r=1,
\]
an impossibility. For \(p\ge3\), with \(q\ge5\) and \(r\ge7\),
\[
3(qr-q-r)>q+r+1,
\]
forcing \(p<3\), again impossible.

If all three of \(B,C,D\) are selected, then
\[
B+C+D=pqr-1,
\]
which is equivalent to
\[
(p-1)(q-1)(r-1)=2(p+q+r).
\]
For \(p=2\), this becomes
\[
(q-3)(r-3)=12,
\]
which has no solution in primes \(3<q<r\). For \(p=3\), it becomes
\[
(q-2)(r-2)=6,
\]
again impossible for primes \(3<q<r\). For \(p\ge5\), already at the smallest possible triple \((5,7,11)\) the left side is \(240\) while the right side is \(46\), and the difference increases when any prime increases. Hence this final case is impossible.

Thus the only strongly pseudoperfect integers with \(\Omega(n)\le3\) are \(6\) and \(28\). Since \(36\) supplies a non-perfect example with \(\Omega(36)=4\), the lower bound for non-perfect strongly pseudoperfect integers is sharp.

## Verification
The accompanying `verify.py` checks every algebraic candidate used in the proof and independently enumerates strongly pseudoperfect integers through \(10000\) by subset sums of complementary divisor-pair sums.

The regression confirms that among integers in that range with \(\Omega(n)\le3\), only \(6\) and \(28\) occur, and it verifies the explicit representation of \(36\).

The finite enumeration is not the proof of the all-integer claim. Exhaustiveness follows from the shape-by-shape inequalities and the complete complementary-pair analysis above.

## Relationship to prior work
The notion appears as OEIS A334405 and was named and studied by McCormack and Zelinsky. Their 2023 preprint proves congruence obstructions and a large-prime multiplication obstruction, records explicit families, and asks structural questions about strongly pseudoperfect numbers. It does not state a classification by \(\Omega(n)\).

Wang and Zelinsky's 2026 paper develops substantially stronger constructions and restrictions. In particular, it proves a rigidity theorem for strongly pseudoperfect numbers of the form \(2^k p\) when \(p\) is Mersenne, and analyzes several \(3\cdot2^a p\) families. The inspected full text does not give an all-shape classification for \(\Omega(n)\le3\).

OEIS A334405 begins
\[
6,28,36,60,84,90,\ldots
\]
and therefore displays the numerical phenomenon that the first non-perfect example has four prime factors counted with multiplicity, but it does not provide the unbounded \(\Omega(n)\le3\) classification proved here.

Targeted searches for strongly pseudoperfect semiprimes, three-prime-factor classifications, and \(\Omega\)-bounded classifications did not locate a covering theorem.

## Limitations
The theorem says nothing about the structure of strongly pseudoperfect integers once \(\Omega(n)\ge4\), except that the bound is attained by \(36\).

The literature comparison includes the current 2026 full-text paper and the relevant OEIS entry, but an unindexed note could contain the same elementary low-complexity observation.

## References
1. OEIS A334405, “Pseudoperfect numbers \(k\) such that there is a subset of divisors of \(k\) whose sum is \(2k\) and for each selected \(d\), \(k/d\) is also selected,” first entered 27 April 2020.
2. Tim McCormack and Joshua Zelinsky, “Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function,” arXiv:2312.11661v1, first posted 18 December 2023.
3. Audrey Wang and Joshua Zelinsky, “Strongly Pseudoperfect Numbers,” arXiv:2609.36068v1, first posted 28 September 2026.
