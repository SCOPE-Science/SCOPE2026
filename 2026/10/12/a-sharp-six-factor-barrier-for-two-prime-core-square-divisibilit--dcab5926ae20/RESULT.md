# A sharp six-factor barrier for two-prime core-square divisibility
## Finding
Let
\[
\sigma(n)=\sum_{d\mid n}d
\]
and let
\[
\gamma(n)=\prod_{p\mid n}p
\]
be the product of the distinct prime divisors of \(n\). Let \(\Omega(n)\) count prime factors with multiplicity.

If \(n\) has exactly two distinct prime factors and
\[
\gamma(n)^2\mid \sigma(n),
\]
then
\[
\Omega(n)\ge6.
\]
The bound is sharp:
\[
96=2^5\cdot3,\qquad
\gamma(96)^2=36,\qquad
\sigma(96)=252=7\cdot36,
\]
so
\[
\Omega(96)=6.
\]

## Assumptions and scope
Write
\[
n=p^a q^b
\]
with primes
\[
p<q
\]
and positive integers \(a,b\).

The claim concerns the divisibility
\[
\gamma(n)^2\mid\sigma(n),
\]
which is the related problem considered in the final section of Broughan, De Koninck, Kátai and Luca. It is not the opposite equality
\[
\sigma(n)=\gamma(n)^2
\]
that is the main subject of their paper.

For a prime power,
\[
\sigma(p^a)=1+p+\cdots+p^a.
\]
In particular,
\[
p\nmid\sigma(p^a).
\]

## Proof
Suppose
\[
\gamma(n)^2=p^2q^2\mid\sigma(p^a)\sigma(q^b).
\tag{1}
\]
Because
\[
p\nmid\sigma(p^a)
\quad\text{and}\quad
q\nmid\sigma(q^b),
\]
condition (1) implies the two cross-divisibilities
\[
p^2\mid\sigma(q^b),
\qquad
q^2\mid\sigma(p^a).
\tag{2}
\]

Assume for contradiction that
\[
a+b\le5.
\tag{3}
\]

First, \(a\ge3\). If \(a=1\), then
\[
\sigma(p)=p+1<q^2,
\]
contradicting \(q^2\mid\sigma(p)\). If \(a=2\), then
\[
\sigma(p^2)=p^2+p+1<q^2.
\]
For \(p=2\), this is \(7<9\). For odd \(p\), one has \(q\ge p+2\), and
\[
p^2+p+1<(p+2)^2\le q^2.
\]
Thus
\[
a\ge3.
\tag{4}
\]

By (3) and (4), only \(b=1\) or \(b=2\) remain.

Suppose first that \(b=2\). Then (3) forces \(a=3\). From (2),
\[
q^2\mid\sigma(p^3)=(p+1)(p^2+1).
\]
If \(p=2\), then \(\sigma(2^3)=15\), which is not divisible by \(q^2\) for any prime \(q>2\). If \(p\) is odd, then \(q\ge p+2\), so \(q\nmid p+1\). Hence
\[
q^2\mid p^2+1,
\]
but
\[
p^2+1<q^2,
\]
a contradiction.

Now suppose \(b=1\). The first divisibility in (2) gives
\[
p^2\mid q+1.
\tag{5}
\]
By (3), \(a\) is \(3\) or \(4\).

If \(a=3\) and \(p=2\), then (5) gives \(q\equiv3\pmod4\), while
\[
q^2\mid\sigma(2^3)=15
\]
is impossible. If \(a=3\) and \(p\ge3\), then (5) gives
\[
q\ge p^2-1.
\]
But
\[
(p^2-1)^2-\sigma(p^3)
=
p\bigl(p^3-p^2-3p-1\bigr)>0
\]
for every \(p\ge3\). Therefore
\[
q^2>\sigma(p^3),
\]
contradicting the second divisibility in (2).

Finally let \(a=4\). Write from (5)
\[
q+1=kp^2
\]
with \(k\ge1\). Since
\[
\sigma(p^4)=p^4+p^3+p^2+p+1
<
(2p^2-1)^2
\]
for every \(p\ge2\), the divisibility
\[
q^2\mid\sigma(p^4)
\]
rules out \(k\ge2\). Hence \(k=1\) and
\[
q=p^2-1.
\]
If \(p\) is odd, then
\[
p^2-1=(p-1)(p+1)
\]
is composite. If \(p=2\), then \(q=3\), but
\[
9\nmid\sigma(2^4)=31.
\]
This is the last case.

Thus no two-prime-support solution can satisfy
\[
a+b\le5.
\]
Therefore every such solution has
\[
\Omega(n)=a+b\ge6.
\]

For sharpness,
\[
\sigma(96)=\sigma(2^5)\sigma(3)=63\cdot4=252
\]
and
\[
\gamma(96)^2=(2\cdot3)^2=36,
\]
so \(36\mid252\) and \(\Omega(96)=6\).

## Verification
The attached `verify.py` checks the algebraic inequalities used in the proof for representative prime ranges, exhaustively checks all prime pairs below a stated cutoff with
\[
a+b\le5,
\]
and confirms that none satisfies the core-square divisibility. It also verifies the sharpness witness
\[
n=96.
\]

The computation is corroborative only. The universal conclusion follows from the complete symbolic split above.

## Relationship to prior work
Broughan, De Koninck, Kátai and Luca explicitly introduce the related problem of identifying integers satisfying
\[
\gamma(n)^2\mid\sigma(n).
\]
They prove that on support exactly \(\{2,3\}\), the solutions are precisely
\[
2^i3^j
\]
with
\[
i\equiv5\pmod6,\qquad j\equiv1\pmod2.
\]
They also emphasize that this family does not exhaust all two-prime-support solutions and give much larger examples involving the prime pairs
\[
(2,1093)
\quad\text{and}\quad
(83,4871).
\]

Those results neither state nor imply a uniform lower bound on total prime-factor multiplicity for arbitrary two-prime supports. The present theorem supplies the exact first multiplicity threshold across all prime pairs. The source's \(\{2,3\}\) family supplies the sharp witness \(96=2^5\cdot3\).

Targeted searches for the exact divisibility, core/radical aliases, two-prime support, total multiplicity, and the cutoff \(\Omega\le5\) did not locate a statement equivalent to or stronger than this barrier.

## Limitations
The theorem does not classify the complete layer
\[
\Omega(n)=6
\]
and does not classify all two-prime-support solutions. It only proves the sharp minimum possible total multiplicity.

The proof does not address integers with three or more distinct prime factors. An equivalent elementary observation in an unindexed note or problem discussion remains a residual originality risk.

## References
1. K. A. Broughan, J.-M. De Koninck, I. Kátai and F. Luca, “On Integers for Which the Sum of Divisors is the Square of the Squarefree Core,” *Journal of Integer Sequences* 15 (2012), Article 12.7.5, published 8 September 2012.
