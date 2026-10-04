# Exact first three fibers of the alternating-divisor totient gap

## Finding
Let the positive divisors of \(n\) be written in decreasing order
\[
n=d_0>d_1>\cdots>d_{t-1}=1,
\]
and define
\[
\chi(n)=d_0-d_1+d_2-d_3+\cdots+(-1)^{t-1}d_{t-1}.
\]
Put
\[
\Delta(n)=\chi(n)-\varphi(n).
\]

Then the first three fibers of \(\Delta\) are exactly
\[
\Delta(n)=0
\quad\Longleftrightarrow\quad
n=1\ \text{or}\ n\ \text{is prime},
\]
\[
\Delta(n)=1
\quad\Longleftrightarrow\quad
n=p^2\ \text{for a prime}\ p,\ \text{or}\ n=8,
\]
and
\[
\Delta(n)=2
\quad\Longleftrightarrow\quad
n=27,\ \text{or}\ n=2q\ \text{for an odd prime}\ q.
\]

In particular, every composite integer \(n\) satisfies the strict inequality
\[
\chi(n)>\varphi(n).
\]

## Assumptions and scope
The function \(\chi\) is the nonmultiplicative alternating sum-of-divisors function in decreasing divisor order, as studied by Caragiu and Swieringa and recorded as OEIS A071324. The gap sequence \(\Delta(n)\) is OEIS A382545.

The result is for all positive integers. No density or asymptotic assertion about higher fibers is made.

## Proof
The cases \(n=1\) and prime \(n\) are immediate:
\[
\chi(1)=\varphi(1)=1,
\]
and for prime \(p\),
\[
\chi(p)=p-1=\varphi(p).
\]

Now let \(n\) be composite, and let \(p\) be its least prime divisor. The second-largest divisor is \(n/p\), so write
\[
\chi(n)=n-\frac np+R(n),
\]
where
\[
R(n)=d_2-d_3+d_4-d_5+\cdots.
\]
The tail is nonempty because \(n\) is composite. Pairing consecutive terms shows that each pair is a positive integer; if one final term is unpaired, it is also positive. Hence
\[
R(n)\ge1.
\]

Define
\[
T(n)=n\left(1-\frac1p\right)-\varphi(n).
\]
The standard Euler product gives \(T(n)\ge0\), and therefore
\[
\Delta(n)=R(n)+T(n).
\]
Thus every composite \(n\) has
\[
\Delta(n)\ge1,
\]
which already proves the strict inequality and the complete zero fiber.

First suppose that \(n=p^a\) is a prime power with \(a\ge2\). Then \(T(n)=0\), and direct subtraction of the first two terms gives
\[
\Delta(p^a)
=
p^{a-2}-p^{a-3}+\cdots+(-1)^a
=
\frac{p^{a-1}+(-1)^a}{p+1}.
\]
For \(a=2\), this equals \(1\). For \(a=3\), it equals \(p-1\), giving the additional value \(1\) only at \(p=2\), namely \(n=8\), and the value \(2\) only at \(p=3\), namely \(n=27\). If \(a\ge4\), then
\[
\Delta(p^a)\ge3:
\]
for even \(a\ge4\), the minimum is attained at \(p=2,a=4\) and equals \(3\); for odd \(a\ge5\), the minimum is at least
\[
\frac{2^4-1}{3}=5.
\]
This completely classifies the prime-power contributions to the fibers \(1\) and \(2\).

It remains to consider integers having at least two distinct prime factors. Let \(q\) be the second-smallest distinct prime factor of \(n\), and write
\[
A=\prod_{\substack{r\mid n\\r\ne p}}
\left(1-\frac1r\right),
\]
where the product is over distinct primes. Then
\[
T(n)=n\left(1-\frac1p\right)(1-A).
\]
Since the factor for \(q\) occurs in \(A\),
\[
A\le1-\frac1q,
\]
so
\[
T(n)
\ge
\frac{n(p-1)}{pq}
\ge p-1,
\]
because \(pq\mid n\). Consequently
\[
\Delta(n)=R(n)+T(n)\ge p.
\]

Therefore no integer with at least two distinct prime factors can have \(\Delta(n)=1\). If \(\Delta(n)=2\), the preceding inequality forces \(p=2\), and since both \(R(n)\) and \(T(n)\) are positive integers, necessarily
\[
R(n)=T(n)=1.
\]
But
\[
T(n)\ge\frac{n}{2q},
\]
so \(T(n)=1\) implies \(n\le2q\). As \(2q\mid n\), this forces
\[
n=2q.
\]
Conversely, for any odd prime \(q\), the divisors of \(2q\) are
\[
2q,\ q,\ 2,\ 1,
\]
hence
\[
\chi(2q)=2q-q+2-1=q+1
\]
and
\[
\varphi(2q)=q-1,
\]
so
\[
\Delta(2q)=2.
\]
This completes all three classifications.

## Verification
The accompanying `verify.py` computes the divisor list, \(\chi(n)\), \(\varphi(n)\), and \(\Delta(n)\) independently from integer factorizations for every
\[
1\le n\le200000.
\]
It verifies the nonnegativity theorem and all three stated fiber classifications on that entire range.

It also checks the first thirty terms of OEIS A382545 as an external sequence anchor. The finite computation is regression evidence only; the all-integer classification is proved symbolically above.

## Relationship to prior work
Caragiu and Swieringa studied \(\chi\) in 2024, stated the open inequality
\[
\chi(n)\ge\varphi(n),
\]
and proved it for their super-increasing class. Their paper also records the least-prime lower bound that motivates the decomposition used here.

A 2025 note by Jaiswal proves the inequality for every positive integer by writing
\[
\chi(n)=n-\frac nq+\text{positive alternating tail},
\]
where \(q\) is the least prime factor. That result establishes nonnegativity of \(\Delta\), but it does not determine equality or the first positive fibers.

OEIS A382545 is exactly the sequence
\[
\Delta(n)=\mathrm{A071324}(n)-\mathrm{A000010}(n).
\]
Its current entry records nonnegativity and the prime identity \(\Delta(p)=0\), together with computed terms, but does not state the complete fibers at \(0\), \(1\), or \(2\). The theorem above converts the first three numerical layers into exact infinite classifications.

Targeted searches for equality cases, the fibers \(\Delta=1,2\), prime-square exceptions, and the semiprime family \(2q\) did not locate an implication-equivalent theorem.

## Limitations
Only the fibers
\[
\Delta(n)\in\{0,1,2\}
\]
are classified. Higher fibers can receive contributions from substantially more prime-factor patterns, and no general classification for fixed larger gaps is claimed.

The strongest residual originality risk is an unindexed observation about OEIS A382545 or a short note deriving these fibers from the known inequality proof. The current OEIS entry, the full two-page 2025 proof, and the relevant portions of the 2024 article were inspected and do not state the classification.

## References
1. Mihai Caragiu and Kaleb Swieringa, “On the Alternating Sum-of-Divisors,” JP Journal of Algebra, Number Theory and Applications 63(2) (2024), 97–110, DOI 10.17654/0972555524006.
2. Shreyansh Jaiswal, “On two Conjectures by Atanassov on the Alternating sum-of-divisors function,” OEIS-hosted note linked from A071324, 2025.
3. OEIS A071324, “Alternating sum of all divisors of n; divisors nonincreasing, starting with n.”
4. OEIS A382545, “a(n) = A071324(n) - A000010(n).”
