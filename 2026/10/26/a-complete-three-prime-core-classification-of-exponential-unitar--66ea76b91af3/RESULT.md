# A complete three-prime-core classification of exponential-unitary perfect numbers

## Finding
For \(n=\prod_{p}p^{a_p}\ge1\), let
\[
\sigma^{(e)*}(n)=\prod_{p\mid n}\left(\sum_{d\mid a_p,\ \gcd(d,a_p/d)=1}p^d\right).
\]
Write \(c(n)=\prod_{a_p\ge2}p^{a_p}\) for the powerful (squarefull) core and \(m(n)=\prod_{a_p=1}p\) for its coprime squarefree tail. The empty products are \(1\).

**Theorem.** If \(c(n)\) has at most three distinct prime divisors, then
\[
\boxed{\sigma^{(e)*}(n)=2n\quad\Longleftrightarrow\quad
n=cm,\ c\in\{36,1800,2700\},\ m\text{ squarefree},\ \gcd(c,m)=1.}
\]
Every number in these three families is also exponential-perfect for the ordinary exponential-divisor sum \(\sigma^{(e)}\). In particular, any exponential-unitary perfect integer that is **not** exponential-perfect must have at least four distinct prime factors in its powerful core. This is a classification in terms of *core* support, not merely the total number of distinct prime factors of \(n\): the tail \(m\) may have arbitrarily many distinct prime factors.

## Assumptions and scope
The prime exponents \(a_p\) are positive integers. A divisor \(d\) of the integer exponent \(a\) is *unitary* if \(\gcd(d,a/d)=1\). For \(a=1\), the single summand is \(p\); for \(a=2\), the two summands are \(p,p^2\). The function \(\sigma^{(e)*}\) is multiplicative by definition, and all equalities below are exact. The condition \(n\ge1\) includes \(n=1\), which is not exponential-unitary perfect because \(\sigma^{(e)*}(1)=1\ne2\).

## Proof
**Local excess bound.** Set
\[
R_p(a)=\frac{1}{p^a}\sum_{d\mid a,\ \gcd(d,a/d)=1}p^d.
\]
As \(a\) is itself unitary and \(1\) is unitary, \(R_p(a)>1\) whenever \(a\ge2\), while \(R_p(1)=1\). Moreover
\[
\boxed{R_p(2)=1+p^{-1},\qquad 1<R_p(a)\le1+p^{-2}\quad(a\ge3),}
\]
with equality in the second upper bound exactly for \(a=3\). To prove this, for \(a=3,4,5\) the only proper unitary divisor is \(1\), giving excesses \(p^{-2},p^{-3},p^{-4}\). For \(a=6\) the proper unitary divisors are \(1,2,3\), giving excess \(p^{-5}+p^{-4}+p^{-3}<p^{-2}\): after multiplication by \(p^5\) this is \(1+p+p^2<p^3\) for all \(p\ge2\). For \(a\ge7\), each proper divisor \(d\) satisfies \(d\le a/2\); hence \(a-d\ge4\) and
\[
R_p(a)-1\le\sum_{j=4}^{\infty}p^{-j}=\frac1{p^3(p-1)}<p^{-2}.
\]
Thus the local bound is proved. In particular \(R_p(a)\le1+1/p\) whenever \(a\ge2\), with equality exactly for \(a=2\).

Multiplicativity now gives
\[
\frac{\sigma^{(e)*}(n)}n=\prod_{p\mid c(n)}R_p(a_p).
\]
All primes in \(m(n)\) contribute the factor \(1\). If \(\omega(c(n))=0\), the ratio is \(1\), and if \(\omega(c(n))=1\), the ratio is at most \(3/2<2\).

If \(\omega(c(n))=2\), let the core primes be \(p<q\). Then
\[
R_p(a_p)R_q(a_q)\le(1+1/p)(1+1/q)\le(3/2)(4/3)=2.
\]
Equality forces \((p,q)=(2,3)\) and both exponents equal to \(2\), giving the unique two-prime core \(36\).

Now let \(\omega(c(n))=3\) with core primes \(p<q<r\). If \(p\ge3\), the product is at most \((4/3)(6/5)(8/7)=64/35<2\). Therefore \(p=2\). If \(q\ge7\), the product is at most \((3/2)(8/7)(12/11)=144/77<2\). If \(q=5\) and \(r\ge11\), it is at most \((3/2)(6/5)(12/11)=108/55<2\). Only \((p,q,r)=(2,5,7)\) or \((2,3,r)\), \(r\ge5\), remain.

For \((2,5,7)\), if all three exponents are \(2\), the product is \(72/35>2\). If any exponent is at least \(3\), applying the strict local bound to that exponent and the \(a=2\) bounds to the other two yields at most one of
\[
(5/4)(6/5)(8/7)=12/7,\quad
(3/2)(26/25)(8/7)=312/175,\quad
(3/2)(6/5)(50/49)=90/49,
\]
all strictly below \(2\). Thus this triple provides no equality.

For \((2,3,r)\), write the core exponents \(a,b,c\ge2\) in that order. If \(a=b=2\), the first two ratios already multiply to \(2\), and \(R_r(c)>1\), so equality is impossible. If \(a,b\ge3\), even the maximal product satisfies
\[
R_2(a)R_3(b)R_r(c)\le(5/4)(10/9)(6/5)=5/3<2.
\]
If \(a\ge3,b=2\), the product is at most
\[
(5/4)(4/3)(6/5)=2,
\]
and equality forces \(a=3,r=5,c=2\), giving \(2^3 3^2 5^2=1800\). Finally if \(a=2,b\ge3\), the product is at most
\[
(3/2)(10/9)(6/5)=2,
\]
and equality forces \(b=3,r=5,c=2\), giving \(2^2 3^3 5^2=2700\). The two cases exhaust all possibilities.

Conversely, the ratios for the three cores are exactly
\[
(3/2)(4/3)=2,\qquad (5/4)(4/3)(6/5)=2,\qquad
(3/2)(10/9)(6/5)=2.
\]
Multiplication by any squarefree \(m\) coprime to the core leaves the ratio unchanged, so all listed \(n\) satisfy the equation. Every prime exponent in these cores belongs to \(\{2,3\}\), whose divisors are all unitary; hence \(\sigma^{(e)}(c)=\sigma^{(e)*}(c)\). The same holds after adjoining an exponent-one squarefree tail, proving the final assertion. \(\square\)

## Verification
The accompanying standalone Python 3 checker `artifacts/verify.py` constructs unitary divisors of exponents using exact integer arithmetic and calculates the exponential-unitary sum independently of the proof inequalities. It exhaustively checks every \(n\le500000\), all three-prime core choices from the first nine primes with each exponent in \(\{2,\ldots,13\}\), and local inequalities over exponents through \(300\). Actual output:

`VERIFY_OK direct_full_interval_N=500000 perfect_count=4338 cores=[36, 1800, 2700] exact_powerful_parameter_cases=150444 local_inequalities_checked=2682`

These finite checks are corroborative only: the unbounded theorem follows from the preceding symbolic inequalities and exhaustive case split.

## Relationship to prior work
Minculete and Tóth introduced the systematic modern treatment of exponential-unitary divisors, listed the examples \(36,1800,2700\), established the absence of odd exponential-unitary perfect numbers, and asked whether exponential-unitary perfectness can ever differ from ordinary exponential-perfectness. Their examples and parity theorem do not constitute a complete prime-core classification. The earlier two-prime-support classification establishes only the core \(36\) when there are two total distinct primes. A published fixed-prime-factor asymptotic for ordinary exponential-perfect numbers counts broader families but does not classify the relevant three-prime powerful cores. The OEIS enumeration of primitive examples likewise does not assert completeness. The contribution here is the complete all-exponents **three-prime-core cutoff** for exponential-unitary perfectness, including arbitrary coprime squarefree tails.

## Limitations
This result does not decide the existence of an exponential-unitary perfect integer that is not ordinary exponential-perfect: any such integer must have at least four distinct squarefull-core primes, but this is only a necessary condition. The conclusion does not classify cores of support \(4\) or greater. The cited primary open-access preprint, related results, and numerical sequence were examined, but the possibility of an unindexed or inaccessible equivalent classification remains a publication-priority risk. All proof steps are elementary exact inequalities; no finite computation is treated as an infinite certificate. Independent mathematical validation has not been performed.

## References
1. N. Minculete and L. Tóth, “Exponential unitary divisors,” arXiv:0910.2798v1 (2009-10-15), https://arxiv.org/html/0910.2798v1 ; subsequently *Ann. Univ. Sci. Budapest., Sect. Comp.* 35 (2011), 205–216.
2. “Two-prime classification of exponential unitary perfect numbers,” published research note (2026), https://github.com/Resultary/2026/blob/main/2026/9/20/SCOPE-e-unitary-perfect-two-prime-classification--567c0a0347f9/RESULT.md .
3. “Fixed-prime-factor layers of exponential-perfect numbers,” published research note (2026), https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-fixed-prime-factor-layers-of-exponential-perfect-numbers--c6019f5b8954/RESULT.md .
4. OEIS A391281, “Primitive e-unitary perfect numbers,” https://oeis.org/A391281 .
5. J. Kalita and H. K. Saikia, “e-Zumkeller Numbers and e-Unitary Zumkeller Numbers,” *Palestine Journal of Mathematics* 14(3) (2025), 684–691, https://pjm.ppu.edu/sites/default/files/papers/PJM_14(3)_2025_684_to_691.pdf.pdf .
