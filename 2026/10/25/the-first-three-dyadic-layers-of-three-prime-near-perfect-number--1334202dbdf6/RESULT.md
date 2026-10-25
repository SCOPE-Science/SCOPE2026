# The first three dyadic layers of three-prime near-perfect numbers

## Finding
Let \(\sigma(n)\) denote the sum of the positive divisors of \(n\). An integer \(n\) is **near-perfect** if there is a positive proper divisor \(d\mid n\) such that \(\sigma(n)=2n+d\). For two distinct odd primes \(p<q\) and \(a\in\{1,2,3\}\), the complete classification is

\[
\sigma(2^apq)=2^{a+1}pq+d,\quad d\mid 2^apq,\quad 0<d<2^apq
\quad\Longleftrightarrow\quad
2^apq\in\{5624,9112,11096,13736,17816\}.
\]

Each number on the right has \(a=3\). In increasing order, the pairs \((n,d)\) are \((5624,152),(9112,136),(11096,8),(13736,68),(17816,8)\). Thus no such number exists for \(a=1\) or \(a=2\); the third dyadic layer is the first nonempty one.

## Assumptions and scope
All variables \(p,q\) are odd rational primes satisfying \(3\le p<q\); the dyadic exponent is precisely \(a\in\{1,2,3\}\), and the odd exponents are exactly one. No upper bound on \(p\), \(q\), or \(n\) is assumed. The definition uses **one omitted proper divisor**, not two omitted divisors and not a deficiency equation. We do not classify higher dyadic exponents or repeated odd-prime factors.

## Proof
Put \(H=2^{a+1}-1\). Multiplicativity of the divisor sum gives

\[
\Delta:=\sigma(2^apq)-2(2^apq)=H(p+1)(q+1)-(H+1)pq
=H(p+q+1)-pq=H(p+1)+(H-p)q.
\]

Near-perfectness is equivalent to \(0<\Delta<2^apq\) and \(\Delta\mid 2^apq\), with \(d=\Delta\) uniquely determined.

**First bound (smallest odd prime).** If \(\Delta>0\), then

\[
\left(1+\frac1p\right)\left(1+\frac1q\right)>1+\frac1H.
\]

Since \(q>p\), this implies \((1+1/p)^2>1+1/H\), equivalently \(p^2-2Hp-H<0\). Consequently

\[
3\le p <H+\sqrt{H(H+1)},
\]

so, because \(H(H+1)\) is not a square, \(p\le H+\lfloor\sqrt{H(H+1)}\rfloor\). These bounds are respectively \(6,14,30\) for \(a=1,2,3\).

**Second bound (larger odd prime).** If \(p<H\), the displayed formula for \(\Delta\) gives \(\Delta>H(p+1)>2^ap\) because \(H>2^a\). As \(\Delta\mid 2^apq\), it must contain the prime factor \(q\), and therefore \(q\mid \Delta\). Reducing the identity modulo \(q\) yields \(q\mid H(p+1)\), hence \(q\le H(p+1)\). If \(p=H\), then \(\Delta=H(p+1)=H2^{a+1}\), which cannot divide \(2^aHq\) because \(q\) is odd. If \(p>H\), positivity forces \((p-H)q<H(p+1)\), and again \(q\le H(p+1)\).

Thus **all** possible \(p,q\) lie in the finite exact ranges

\[
3\le p\le H+\lfloor\sqrt{H(H+1)}\rfloor,
\qquad p<q\le H(p+1),
\]

with prime \(p,q\). These are derived from the necessary conditions, not numerical search cutoffs. The two additional filters \(q\mid H(p+1)\) for \(p<H\) and \((p-H)q<H(p+1)\) for \(p>H\) reduce the finite candidates further.

**Exhaustive exact arithmetic.** The primality and divisibility checker in `verify.py` applies precisely these bounds and filters, then evaluates \(\Delta\mid 2^apq\) using integers. The complete small-prime cases are:

| \(a\) | \(H\) | eligible \(p\) | reduced prime-pair candidates | passing \((n,d)\) |
|---|---:|---|---:|---|
| 1 | 3 | 3, 5 | 1 | none |
| 2 | 7 | 3, 5, 7, 11, 13 | 5 | none |
| 3 | 15 | 3, 5, 7, 11, 13, 17, 19, 23, 29 | 45 | \((5624,152),(9112,136),(11096,8),(13736,68),(17816,8)\) |

This finite certificate is exhaustive by the proved bounds. For \(a=3\), only \(p=17,19\) pass: at \(p=17\), the final primes are \(67,101,131\); at \(p=19\), they are \(37,73\). Substitution establishes the five displayed redundant divisors, and proves both directions.

## Verification
Run `python verify.py` using Python 3 without external libraries. The checker enumerates every bounded prime pair by trial-division primality, applies the mathematically necessary reduced filters, tests exact positive proper-divisor conditions, and asserts all three solution lists and all five direct divisor sums. The expected final line is `VERIFY_OK: 440 prime-pair tests, five direct divisor-sum witness checks`. The finite loop is conclusive here **because the proof bounds both primes**, not because a finite numerical scan establishes an infinite result.

## Relationship to prior work
Shevelev's 2010 preprint introduces near-perfect numbers and proves families with two prime supports. Ren and Chen (2013), Theorem 1.2, classify numbers with exactly two distinct prime factors and **already list all five numerical examples** here among initial known numbers with three prime factors (page 521). Their displayed examples do not establish that this infinite family contains only five; indeed, their Conjecture 1.3 concerns finiteness for a fixed number of distinct prime factors. This result supplies an exact classification for the naturally ordered first three dyadic-exponent layers of a three-prime, squarefree-odd-part family. Existing published small-support investigations and related divisibility problems distinguish deficient, almost-perfect and two-omission equations, which do not imply this one-omission complete list.

## Limitations
The examples themselves and their five numerical values are previously published; only the proposed completeness proof for the stated infinite family is assessed here. Higher powers of two and nonsquarefree odd parts remain unresolved by this argument. Searches cannot establish publication priority: equivalent proofs could occur in unindexed, unpublished or inaccessible literature. Independent verification has not been performed.

## References
1. V. Shevelev, *On perfect and near-perfect numbers*, arXiv:1011.6160v1 (first posted 2010-11-29), https://arxiv.org/abs/1011.6160 (full HTML revision v3 also inspected).
2. X.-Z. Ren and Y.-G. Chen, *On near-perfect numbers with two distinct prime factors*, Bulletin of the Australian Mathematical Society 88 (2013), 520–524, https://doi.org/10.1017/S0004972713000178 (full five-page article inspected; see page 521, Theorem 1.2, following example list and Conjecture 1.3).
3. OEIS A181595, *Near-perfect numbers*, https://oeis.org/A181595 (known examples, not an exhaustive three-prime classification).
