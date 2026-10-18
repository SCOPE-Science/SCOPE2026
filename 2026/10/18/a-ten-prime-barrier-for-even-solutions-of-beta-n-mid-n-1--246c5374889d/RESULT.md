# A ten-prime barrier for even solutions of \(\beta(n)\mid n-1\)

## Finding
Let \(\beta(1)=1\) and let \(\beta\) be multiplicative, with
\[
\beta(p^e)=p^e-p^{e-1}+\cdots+(-1)^e
=\frac{p^{e+1}+(-1)^e}{p+1}
\]
for every prime \(p\) and integer \(e\ge1\). **Theorem.** If \(n>4\) is even and \(\beta(n)\mid n-1\), then the odd part of \(n\) is a square with at least nine distinct prime divisors. In particular,
\[
\omega(n)\ge10,\qquad
n\ge 2(3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19\cdot23\cdot29)^2
=20928465245153916450.
\]
The conclusion does not assert that any such composite integer exists.

## Assumptions and scope
All numbers are positive integers. The symbol \(\omega(n)\) counts **distinct** prime divisors. Divisibility is ordinary integer divisibility. The integer \(n\) is even, \(n>4\); the result does not concern odd potential solutions. For a positive odd integer \(t\), write \(r=\omega(t)\). The proof excludes \(r\le8\) without an upper bound on prime exponents or on \(n\).

## Proof
**1. Parity forces a square odd part.** For an odd prime \(p\), the alternating sum \(\beta(p^e)\) is odd exactly when \(e\) is even: each power of \(p\) is odd, so its \(e+1\) signed terms have parity \(e+1\). For powers of two, \(\beta(2^a)=(2^{a+1}+(-1)^a)/3\) is odd for all \(a\ge1\). Since \(n-1\) is odd and \(\beta(n)\mid n-1\), the odd prime exponents of \(n\) must all be even. Thus
\[
n=2^a t^2,\quad a\ge1,\quad t\text{ odd},\quad
\beta(n)=u_a\beta(t^2),\quad
u_a:=\beta(2^a)=\frac{2^{a+1}+(-1)^a}{3}.
\]
Moreover \(u_a\) and \(\beta(t^2)\) are odd.

**2. Exact finite products give uniform estimates.** For every odd prime \(p\) and \(e\ge1\),
\[
\frac{\beta(p^{2e})}{p^{2e}}
=\frac{p+p^{-2e}}{p+1}>\frac p{p+1}.
\]
For \(t>1\), consequently \(B:=\beta(t^2)/t^2\) satisfies
\[
B>\prod_{p\mid t}\frac p{p+1}.
\]
For \(t=1\), instead \(B=1\); both cases satisfy the strict bounds below. For at most eight distinct odd primes, the product is bounded below by using the eight smallest odd primes, because \(p/(p+1)\) increases with \(p\):
\[
B>\prod_{p\in\{3,5,7,11,13,17,19,23\}}\frac p{p+1}
=\frac{1062347}{2654208}>\frac25.\tag{1}
\]
If additionally \(3\nmid t\), the eight smallest eligible primes instead give
\[
B>\prod_{p\in\{5,7,11,13,17,19,23,29\}}\frac p{p+1}
=\frac{30808063}{59719680}>\frac12.\tag{2}
\]
Both displayed rational inequalities are exact integer comparisons, checked independently in `verify.py`.

**3. Bound the divisibility quotient.** Suppose \(r=\omega(t)\le8\), and set
\[
k:=\frac{n-1}{\beta(n)}\in\mathbb Z_{>0}.
\]
This integer is odd because both numerator and denominator are odd. The ratios of the power-of-two factor obey
\[
\frac{u_1}{2}=\frac12,\qquad
\frac{u_a}{2^a}\ge\frac58\ (a\ge3\text{ odd}),\qquad
\frac{u_a}{2^a}>\frac23\ (a\ge2\text{ even}).
\]
From (1), \(\beta(n)/n=(u_a/2^a)B>1/5\) in all three cases, whence
\[
1\le k=\frac{n-1}{\beta(n)}<\frac n{\beta(n)}<5.
\]
Thus \(k\in\{1,3\}\).

**4. Exclude the quotient three.** If \(a\) is odd, then \(2^a\equiv-1\pmod3\), so \(n=2^a t^2\equiv-t^2\equiv0\text{ or }2\pmod3\), never \(1\pmod3\). Hence \(3\nmid n-1\) and \(k\ne3\). If \(a\) is even and \(k=3\), then \(3\mid n-1\) entails \(t^2\equiv1\pmod3\), so \(3\nmid t\). By (2) and \(u_a/2^a>2/3\),
\[
\frac{\beta(n)}n>\frac13,
\qquad k<3,
\]
contradicting \(k=3\). Therefore \(k=1\) in either parity case.

**5. Exclude quotient one beyond the two trivial even solutions.** For \(t>1\), each odd prime-power factor satisfies \(\beta(p^{2e})<p^{2e}\), hence \(\beta(t^2)<t^2\). Also \(u_a\le2^a-1\) for all \(a\ge1\). It follows that
\[
\beta(n)=u_a\beta(t^2)<(2^a-1)t^2
=2^at^2-t^2<n-1
\]
when \(t>1\); this contradicts \(k=1\). If \(t=1\), direct evaluation gives \(\beta(2)=1\), \(\beta(4)=3\), while \(\beta(2^a)<2^a-1\) for \(a\ge3\). Therefore \(k=1\) implies \(n\in\{2,4\}\), contrary to \(n>4\). No even \(n>4\) with \(r\le8\) solves the divisibility equation.

Hence an even candidate has \(r\ge9\) and \(\omega(n)=r+1\ge10\). The lower bound for \(n\) follows by taking the first nine odd primes, all to even exponents, and the smallest possible power of two.

## Verification
The supplied standalone Python program `verify.py` uses exact integer and rational arithmetic. It recomputes both eight-prime product certificates; tests the changes when a ninth prime is included; exhaustively evaluates all even \(2\le n\le500000\), obtaining only \(n=2,4\); cross-checks the multiplicative definition against a coprime-square counting definition through \(n=150\); and checks \(120\) large structured inputs. Execute with `python3 verify.py`; the final expected line is `VERIFY_OK`. The infinite statement follows from the proof above, not from finite enumeration.

## Relationship to prior work
László Tóth's publicly available 2011 preprint and 2013 journal survey introduce the same multiplicative function and pose as Problem 4 the existence of a composite \(n\ne4\) with \(\beta(n)\mid n-1\). The survey states a search through one million but gives no lower bound on the number of distinct prime factors of a hypothetical even solution. The present argument establishes an unconditional structural prime-support obstruction specifically for even numbers. This is not a resolution of the general problem or a consequence of the classical squarefree-only Lehmer problem for Euler's totient. A 2024 study of a similarly named alternating divisor sum concerns a different, nonmultiplicative function.

## Limitations
The theorem does not rule out even solutions with ten or more distinct prime divisors, and it says nothing about odd solutions. The estimate is a necessary condition, not a construction. The literature comparison covers the cited primary sources, targeted discovery queries and related records, not every unindexed text; implicit equivalent statements remain an originality risk. Computational checks have finite scope and do not replace the proof.

## References
1. L. Tóth, *A survey of the alternating sum-of-divisors function*, arXiv:1111.4842v1 (public November 21, 2011), https://arxiv.org/abs/1111.4842 .
2. L. Tóth, *A survey of the alternating sum-of-divisors function*, Acta Universitatis Sapientiae, Mathematica **5** (2013), 93–107, DOI:10.2478/ausm-2014-0007; https://acta.sapientia.ro/content/docs/10415--Volume5_Issue_1_07_paper.pdf .
3. OEIS A206369, alternating sum-of-divisors function, https://oeis.org/A206369 .
4. M. Caragiu and J. Swieringa, *On the alternating sum-of-divisors* (2024), https://pphmjopenaccess.com/jpjana/article/download/1408/1025/5044 , studies a different arithmetic function.
