# A logarithmically periodic counting law for abundant prime-square strata

## Finding
Let \(\sigma(n)=\sum_{d\mid n}d\). Call a positive integer \(n\) abundant when \(\sigma(n)>2n\). For real \(X\ge1\) let
\[
A_2(X)=\#\{2^a p^2\le X:\ a\in\mathbb Z_{\ge1},\ p\text{ an odd prime},\ \sigma(2^a p^2)>2^{a+1}p^2\}.
\]
Then abundance is equivalent to the exact condition \(p<2^{a+1}\). In particular, no member of this form is perfect. With \(\pi(y)\) the number of primes at most \(y\), one has the exact identity
\[
A_2(X)=\sum_{a\ge1}\biggl(\pi\biggl(\min\biggl\{2^{a+1}-1,\left\lfloor\sqrt{X/2^a}\right\rfloor\biggr\}\biggr)-1\biggr)_+,
\]
where a term is zero unless its cutoff is at least \(3\), and \((t)_+=\max\{t,0\}\). Only finitely many terms are nonzero.

Define the dyadic phase for sufficiently large \(X\):
\[
m=\left\lfloor\frac{\log_2 X-2}{3}\right\rfloor,\qquad s=\frac{X}{2^{3m+2}}\in[1,8).
\]
Uniformly for all such phases,
\[
A_2(X)=\frac{X^{1/3}}{\log X}\left(F(s)+o(1)\right),\qquad
F(s)=3\,2^{1/3}s^{-1/3}\bigl[2+(1+\sqrt2)\sqrt s\bigr].
\]
Consequently,
\[
\liminf_{X\to\infty}\frac{A_2(X)\log X}{X^{1/3}}=9(1+\sqrt2)^{2/3},
\qquad
\limsup_{X\to\infty}\frac{A_2(X)\log X}{X^{1/3}}=3\,2^{1/3}(3+\sqrt2).
\]
The minimum phase is \(s_*=16(3-2\sqrt2)\); the maximum is achieved at \(s=1\) or as \(s\to8^-\). These values are distinct, so there is no single constant \(C\) with \(A_2(X)\sim C X^{1/3}/\log X\).

## Assumptions and scope
Only ordinary positive integers are counted. Each \(2^a p^2\) has a unique decomposition because \(p\) is odd. The odd-prime exponent is exactly two, while the exponent of \(2\) varies without bound. Strict abundance is used, not a primitive-abundance condition; the term \(p=2\) is never counted. All logarithms without a base are natural logarithms. The analytic input is the classical prime number theorem \(\pi(y)\sim y/\log y\).

## Proof
**Exact criterion.** Multiplicativity gives
\[
\sigma(2^a p^2)=(2^{a+1}-1)(p^2+p+1).
\]
Writing \(t=2^{a+1}\), the excedent is
\[
\sigma(2^a p^2)-2^{a+1}p^2
= -p^2+(t-1)(p+1)=p(t-1-p)+(t-1).
\]
If \(p\le t-1\), both terms on the right are nonnegative and the second strictly positive. If \(p\ge t+1\), then the same expression is at most \(-2p+(t-1)<0\). Because \(t\) is even and \(p\) is odd, the case \(p=t\) is impossible. Therefore the excedent is never zero and is positive exactly when \(p<t\). The restrictions \(2^a p^2\le X\), \(p\ge3\) and \(p<t\) then give the exact prime-counting formula.

**Transition scale.** In the formula, \(2^{a+1}\le \sqrt{X/2^a}\) holds exactly when \(2^{3a+2}\le X\), that is, \(a\le m\). Thus, with \(t_m=2^{m+1}\),
\[
A_2(X)=\sum_{a=1}^{m}\bigl(\pi(2^{a+1})-1\bigr)
+\sum_{j\ge1}\Bigl(\pi\bigl(\sqrt{X/2^{m+j}}\bigr)-1\Bigr)_+.
\]
In the second sum the size cutoff is automatically no larger than the abundance cutoff; there are at most \(O(\log X)\) nonzero terms. Real-valued arguments of \(\pi\) are harmless. Note the endpoint convention \(\pi(2^{a+1}-1)=\pi(2^{a+1})\), since the latter is a composite power of two for \(a\ge1\).

**First geometric prime sum.** The prime number theorem, together with uniform geometric-tail bounds, gives
\[
\sum_{a=1}^{m}\pi(2^{a+1})
=\frac{2t_m}{m\log2}(1+o(1)).
\]
Indeed, for any fixed \(J\), the terms \(a=m,m-1,\ldots,m-J\) have ratios \(2^{-j}+o(1)\) relative to \(\pi(t_m)\), and their sum tends to the corresponding finite geometric sum. The earlier tail is bounded by \(\pi(t_m2^{-J})\,O(J+1)\) crudely, or more sharply by a dyadic summation using \(\pi(y)\ll y/\log y\) above \(\sqrt{t_m}\) and \(\pi(y)\le y\) below it. This tail is \(O(2^{-J}t_m/\log t_m)+o(t_m/\log t_m)\), uniformly in \(m\). Let \(J\to\infty\).

**Second geometric prime sum.** Since \(X=2^{3m+2}s\), for \(j\ge1\) the relevant cutoff equals
\[
\sqrt{X/2^{m+j}}=t_m\sqrt{s}\,2^{-j/2}.
\]
For each fixed \(j\), its ratio to \(t_m\) stays in the compact interval \([2^{-j/2},\sqrt8\,2^{-j/2})\), uniformly in \(s\in[1,8)\). By the prime number theorem with its standard uniformity on fixed compact multiplicative intervals, the sum of these terms satisfies
\[
\sum_{j\ge1}\Bigl(\pi(t_m\sqrt{s}\,2^{-j/2})-1\Bigr)_+
=\frac{t_m\sqrt{s}}{m\log2}\left(\frac{1}{\sqrt2-1}+o(1)\right).
\]
Uniformity and interchange of the infinite geometric tail follow by splitting at a fixed \(J\) and then at \(j=m\): for \(J<j\le m\), prime number upper bounds \(\pi(y)\ll y/\log y\) apply for arguments \(y\gg2^{m/2}\); the geometric sum is \(O(2^{-J/2}t_m/(m\log2))\). For \(j>m\) the trivial inequality \(\pi(y)\le y\) bounds the remaining series by \(O(2^{m/2})=o(t_m/m)\). Terms subtracting \(1\) contribute \(O(\log X)=o(t_m/m)\). These estimates are uniform in phase.

Combining the two sums yields
\[
A_2(X)=\frac{t_m}{m\log2}\left(2+(1+\sqrt2)\sqrt s+o(1)\right).
\]
Finally, \(t_m/X^{1/3}=2^{1/3}s^{-1/3}\) and \(\log X/(m\log2)=3+o(1)\), uniformly for \(1\le s<8\), proving the phase law.

**Extrema.** Write \(c=1+\sqrt2\). Differentiation of \(s^{-1/3}(2+c\sqrt s)\) shows its unique stationary point in \((1,8)\) satisfies \(c\sqrt s=4\), hence \(s_*=16/c^2=16(3-2\sqrt2)\), and is a strict minimum. The minimum value is \(9c^{2/3}\). At the two phase endpoints, \(F(1)=F(8)=3\,2^{1/3}(3+\sqrt2)\), the maximum. Integer sequences with phase converging to any chosen point exist by rounding \(2^{3m+2}s\). Therefore these are the global liminf and limsup.

## Verification
The standalone `verify.py` checks the exact algebraic criterion against independently computed divisor sums for every admissible integer through \(250000\), comparing all \(274\) candidates, \(98\) abundant and \(176\) deficient. It independently computes the exact prime-count formula and prints numerical phase samples, while checking the two stationary/endpoint constants. It uses only Python standard-library integer arithmetic for the exact tests. Successful execution begins:

`EXACT_CLASSIFICATION_OK bound=250000 tested=274 abundant=98 deficient=176 first=[18, 36, 72, 100, 144, 196, 200, 288, 392, 400, 576, 784]`

The phase samples converge slowly and are for illustration only. Neither the finite regression nor the numerical phase values prove the theorem. The unbounded conclusion uses the exact prime-counting identity, prime number theorem and uniform tail estimates.

## Relationship to prior work
Dean et al. (2015) establish explicit excedent formulas for the family \(2^a p^2\), including the identity equivalent to the one above, and study images of the excedent. The polynomial identity itself is therefore **not** claimed as original. Their inspected full text does not provide a counting function for abundant members of this family, a phase-dependent asymptotic, or the two extrema.

A known log-periodic count for *strict primitive abundant* integers with exactly two prime factors has support only on the distinct-odd-prime first-power layer \(2^a p\): that classification excludes the \(p^2\) family counted here. A known dyadic-phase result for *practical* numbers with exactly two distinct prime factors counts a different property; there, odd-prime powers of exponent at least two are bounded as lower-order terms rather than asymptotically enumerated. Neither prior result implies the explicit \(p^2\)-abundant phase profile. More generally, the global natural density of all abundant integers does not determine the sparse prime-square layer.

Focused searches covered abundance and excedent on \(2^a p^2\), prime-power strata, exact prime-count identities, dyadic phase laws and logarithmic oscillation. No published stronger or equivalent prime-square abundance count was located. This is a novelty assessment, not a claim that search can prove uniqueness.

## Limitations
The conclusion counts **integers** of the stated shape, not distinct values of the excedent function. No statement is made about odd-prime powers of higher exponent, about all abundant integers with two prime factors, or about the possible rate in the \(o(1)\) error. The method uses classical prime-distribution asymptotics and does not give an effective finite-\(X\) uniform error bound. Earlier unindexed results may state the same sparse-layer count using different terminology.

## References
1. R. Dean, R. Erdman, D. Klyve, E. Lycette, M. Pidde, and D. Wheel, “Families of Values of the Excedent Function \(\sigma(n)-2n\),” *Missouri Journal of Mathematical Sciences* 27 (2015), 37–46, DOI 10.35834/mjms/1449161366. Open-access text at https://scispace.com/pdf/families-of-values-of-the-excedent-function-sigma-n-2n-bumgcorybf.pdf.
2. “A log-periodic counting law for two-prime primitive abundant numbers,” a public mathematical result on the strict primitive-abundant two-prime layer (2013 and later literature discussed therein).
3. “Dyadic phase law for practical numbers with exactly two prime factors,” a public mathematical result on two-prime practical-number counts, building on Stewart’s practical-number criterion.
4. Classical prime number theorem: J. Hadamard and C. J. de la Vallée Poussin (1896).
