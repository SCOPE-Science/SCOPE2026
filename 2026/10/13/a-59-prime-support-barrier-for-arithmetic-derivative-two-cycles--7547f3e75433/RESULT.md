# A 59-prime support barrier for arithmetic-derivative two-cycles
## Finding
Let \(D\) denote the arithmetic derivative on positive integers, defined by
\[
D(p)=1
\]
for every prime \(p\), together with the Leibniz rule
\[
D(xy)=D(x)y+xD(y).
\]

Suppose distinct positive integers \(n,m\) satisfy
\[
D(n)=m,
\qquad
D(m)=n.
\]
Then
\[
\omega(n)+\omega(m)\ge59,
\]
where \(\omega\) counts distinct prime divisors. Consequently,
\[
\max\{\omega(n),\omega(m)\}\ge30.
\]

The previously published general support bound for a nontrivial two-cycle is \(34\) total prime factors; the argument below raises it to \(59\).

## Assumptions and scope
The result concerns a nontrivial positive period-\(2\) orbit of the ordinary arithmetic derivative.

A theorem of Ufnarovski and Åhlander proves that in any such orbit both members are squarefree and their prime supports are disjoint. Thus we may write
\[
n=\prod_{i=1}^{r}p_i,
\qquad
m=\prod_{j=1}^{s}q_j,
\]
where all \(r+s\) primes appearing in the two products are distinct.

That structural theorem is used as an established premise. The new argument concerns the support size \(r+s\).

## Proof
For a squarefree positive integer,
\[
\frac{D(n)}{n}=\sum_{p\mid n}\frac1p.
\]
Therefore the two cycle equations give
\[
\frac{m}{n}
=
\sum_{i=1}^{r}\frac1{p_i}
=:A
\]
and
\[
\frac{n}{m}
=
\sum_{j=1}^{s}\frac1{q_j}
=:B.
\]
Multiplication yields
\[
AB=1.
\]
Since \(A,B>0\), the arithmetic-geometric mean inequality gives
\[
A+B\ge2.
\tag{1}
\]

Because the two prime supports are disjoint,
\[
A+B
=
\sum_{\ell\mid nm}\frac1\ell
\]
is a sum of reciprocals of exactly
\[
N=r+s
\]
distinct primes.

Let
\[
P_1<P_2<\cdots
\]
be the increasing sequence of primes. Among all sets of \(N\) distinct primes, the reciprocal sum is maximized by the first \(N\) primes. Hence
\[
A+B
\le
\sum_{i=1}^{N}\frac1{P_i}.
\tag{2}
\]

An exact rational calculation gives
\[
\sum_{i=1}^{58}\frac1{P_i}
=
\frac{
632922102284802030608735614303171023883353726199065754232874723702048629323675218406677909479222722729203736409
}{
316660540451402206051523961799780143689087330537799173695893334666158783075592938409825136155637880209438531070
}
<2.
\tag{3}
\]
The \(58\)-th prime is
\[
P_{58}=271.
\]

If \(N\le58\), then (2) and (3) imply
\[
A+B<2,
\]
contradicting (1). Thus
\[
N=r+s\ge59.
\]

Finally,
\[
r+s\ge59
\]
implies
\[
\max\{r,s\}\ge30,
\]
which proves the stated corollary.

## Verification
The accompanying checker generates the first \(59\) primes by exact integer trial division and sums their reciprocals with rational arithmetic.

It verifies
\[
P_{58}=271,
\qquad
P_{59}=277,
\]
and proves by integer cross-multiplication that
\[
\sum_{i=1}^{58}\frac1{P_i}<2
<
\sum_{i=1}^{59}\frac1{P_i}.
\]
The first inequality is the only finite certificate needed for the theorem. The second shows that the reciprocal-sum method cannot raise the support threshold beyond \(59\) merely by replacing an arbitrary support by the first \(N\) primes and applying \(A+B\ge2\).

The checker also verifies the exact numerator and denominator printed in the proof.

## Relationship to prior work
Ufnarovski and Åhlander introduced the dynamical question for the arithmetic derivative and proved the key reduction for a hypothetical nontrivial two-cycle: the two members must be squarefree, their prime supports are disjoint, and the two reciprocal prime sums have product \(1\).

Kovič developed quantitative restrictions for the same two-cycle problem. His Proposition 18 proves
\[
r+s\ge34.
\]
It also gives the conditional bounds
\[
r+s\ge57
\]
when neither member is even, and
\[
r+s\ge110
\]
when neither member is divisible by \(2\) or \(3\). The present bound
\[
r+s\ge59
\]
is unconditional and therefore strictly improves the published general bound; it also improves the published odd-cycle bound by two.

Kovič's Proposition 17 already uses a one-sided reciprocal-sum estimate when the smaller cycle member is odd. The new point is to use both cycle equations simultaneously:
\[
AB=1
\quad\Longrightarrow\quad
A+B\ge2,
\]
then compare the combined disjoint support with the extremal initial-prime reciprocal sum.

Dahl, Olsson, and Loiko give an independent exposition of the logarithmic-derivative identity
\[
\frac{D(n)}n
=
\sum_{p^a\parallel n}\frac{a}{p}.
\]
Their paper is useful for checking the normalization used here but does not address this two-cycle support bound.

## Limitations
The theorem is conditional only on the existence of a nontrivial positive two-cycle; no such cycle is known. It does not prove the conjecture that fixed points are the only positive periodic points.

The number \(59\) is sharp for the particular total-reciprocal-sum obstruction: the reciprocal sum of the first \(59\) primes already exceeds \(2\). Stronger support bounds would therefore require additional information about how the primes split between the two cycle members, congruence constraints, or other dynamical structure.

The literature comparison inspected the full primary articles of Ufnarovski--Åhlander and Kovič, including the exact two-cycle propositions, together with later arithmetic-derivative literature and exact statement-level searches. An equivalent improvement in unindexed notes remains a residual possibility.

## References
1. V. Ufnarovski and B. Åhlander, “How to Differentiate a Number,” *Journal of Integer Sequences* 6 (2003), Article 03.3.4.
2. J. Kovič, “The Arithmetic Derivative and Antiderivative,” *Journal of Integer Sequences* 15 (2012), Article 12.3.8.
3. N. Dahl, J. Olsson, and A. Loiko, “Investigations on the properties of the arithmetic derivative,” arXiv:1108.4762, 2011.
