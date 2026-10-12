# Prime-power spectrum of a subset-gcd deficit ratio

## Finding

Let \(D(n)\) be the number of nonempty subsets \(A\subseteq\{1,\ldots,n\}\) for which \(\gcd(A)\mid n\), and let \(\Phi(n)\) be the number of such subsets for which \(\gcd(\gcd(A),n)=1\). For every integer \(n\ge2\), define
\[
R(n)=\frac{2^n-D(n)}{2^n-\Phi(n)},\qquad
X(n)=\frac{\log_2 R(n)}{n}.
\]
Write \(L_j=\operatorname{lcm}(1,\ldots,j)\), let \(r(n)\) be the least integer \(d\ge2\) not dividing \(n\), and let \(p(n)\) be the least prime factor of \(n\).

**Theorem (exact logarithmic spectrum).** For every integer \(n\ge2\),
\[
\left|X(n)-\left(\frac1{r(n)}-\frac1{p(n)}\right)\right|
\le \frac{2+2\log_2(n+1)}n.
\]
Consequently, for every bounded continuous \(h:\mathbb R\to\mathbb R\),
\[
\begin{aligned}
\lim_{N\to\infty}\frac1N\sum_{n=2}^{N}h(X(n))
={}&\sum_{\substack{k\ge3\\ k\text{ a prime power}}}
\left(\frac1{L_{k-1}}-\frac1{L_k}\right)
 h\left(\frac1k-\frac12\right)\\
&+\sum_{\substack{q\ge3\\q\text{ prime}}}
\frac1q\prod_{\substack{\ell<q\\\ell\text{ prime}}}
\left(1-\frac1\ell\right)
 h\left(\frac12-\frac1q\right).
\end{aligned}
\]
The two series are nonnegative probability weights with total masses \(1/2\) each. In particular, the limiting law is purely atomic, with negative atoms indexed by prime powers and positive atoms indexed by odd primes.

The same estimates show that, for all even \(n\ge2\) and odd \(n\ge3\), respectively,
\[
0<R(n)\le(n+1)2^{-n/6},\qquad
R(n)\ge\frac{2^{n/6-1}}{n+1}.
\]
Thus \(R(n)\to0\) along even integers and \(R(n)\to+\infty\) along odd integers; hence its overall lower and upper limits are \(0\) and \(+\infty\).

## Assumptions and scope

All sets are subsets of the first \(n\) positive integers and are nonempty. The greatest common divisor of a subset is the positive gcd of its elements. The leading \(2^n\) in both deficits counts the empty subset as one extra object, making both deficits positive. The theorem applies to all integers \(n\ge2\), with no primality or factorization restriction. The limiting expression is convergence in distribution for integers sampled uniformly from \(\{2,\ldots,N\}\). The prime-power index means \(k=\ell^a\) for a prime \(\ell\) and integer \(a\ge1\).

## Proof

**1. Divisor-localization inequalities.** A nonempty subset whose gcd is divisible by \(d\) consists entirely of multiples of \(d\), and there are \(2^{\lfloor n/d\rfloor}-1\) such subsets. Denote by \(A_n=2^n-D(n)\) and \(B_n=2^n-\Phi(n)\) the positive deficits. Since \(r=r(n)\nmid n\), every nonempty subset made entirely of multiples of \(r\) is excluded from \(D(n)\). Conversely, every subset excluded from \(D(n)\) has a gcd \(d\ge r\). Including the extra empty-subset unit and applying a union bound gives
\[
2^{\lfloor n/r\rfloor}\le A_n\le
1+\sum_{d=r}^{n}\bigl(2^{\lfloor n/d\rfloor}-1\bigr)
\le(n+1)2^{\lfloor n/r\rfloor}.
\]
Since \(p=p(n)\mid n\), every nonempty subset made of multiples of \(p\) is excluded from \(\Phi(n)\). Conversely, every excluded subset has a gcd divisible by some prime factor of \(n\), hence its gcd is at least \(p\). Therefore
\[
2^{\lfloor n/p\rfloor}\le B_n\le
1+\sum_{d=p}^{n}\bigl(2^{\lfloor n/d\rfloor}-1\bigr)
\le(n+1)2^{\lfloor n/p\rfloor}.
\]
Taking binary logarithms and using \(0\le n/d-\lfloor n/d\rfloor<1\) proves the stated uniform bound for \(X(n)\). These are global inequalities, not asymptotics for a finite input range.

**2. Prime-power support and negative weights.** For every \(k\ge2\),
\[
r(n)=k\quad\Longleftrightarrow\quad L_{k-1}\mid n\quad\text{and}\quad L_k\nmid n.
\]
Its natural density is \(\beta_k=L_{k-1}^{-1}-L_k^{-1}\). This is positive exactly when \(k\) is a prime power: a new prime-power valuation enlarges the least common multiple, whereas a number with at least two different prime factors is already the product of coprime proper factors represented below \(k\). For \(k=\ell^a\) one has \(L_k=\ell L_{k-1}\), so \(\beta_k=(1-1/\ell)/L_{k-1}\). If \(k\ge3\) then \(2\mid n\) and \(p(n)=2\). Summing the densities over \(k\ge3\) telescopes to \(1/L_2=1/2\), since \(L_k\to\infty\).

**3. Odd-prime support and positive weights.** The condition \(r(n)=2\) is equivalent to \(n\) odd. For any odd prime \(q\), the integers with \(p(n)=q\) are those divisible by \(q\) and by no smaller prime. Their density, calculated using finite inclusion–exclusion over the primes at most \(q\), is
\[
\alpha_q=\frac1q\prod_{\substack{\ell<q\\\ell\text{ prime}}}
\left(1-\frac1\ell\right).
\]
For such integers \(r(n)=2\). These weights sum to \(1/2\). Indeed, the remaining integers avoid all primes up to \(Q\), with density \(\prod_{\ell\le Q}(1-1/\ell)\to0\); the product tends to zero because its reciprocal dominates the diverging harmonic sum \(\sum_{m\le Q}1/m\).

**4. Distribution.** For fixed \(k\) and \(q\), the uniform error in Step 1 tends to zero, and Steps 2–3 give the natural density of each level of \(1/r(n)-1/p(n)\). For cutoff \(K,Q\), the portion not represented by these finitely many levels has upper natural density at most \(1/L_K+\prod_{\ell\le Q}(1-1/\ell)\), which tends to zero as the cutoffs increase. Uniform continuity of \(h\) on a compact interval containing all \(X(n)\) for sufficiently large \(n\), followed by the two tail bounds, gives the displayed limit for any bounded continuous \(h\).

**5. Parity escape.** For even \(n\), \(p(n)=2\) and \(r(n)\ge3\). Step 1 implies
\[
R(n)\le(n+1)2^{\lfloor n/3\rfloor-n/2}\le(n+1)2^{-n/6}.
\]
For odd \(n\ge3\), \(r(n)=2\) and \(p(n)\ge3\), giving
\[
R(n)\ge\frac{2^{\lfloor n/2\rfloor-\lfloor n/3\rfloor}}{n+1}
\ge\frac{2^{n/6-1}}{n+1}.
\]
Both asymptotic assertions follow without numerical experiments.

## Verification

The standalone `verify_subset_defects.py` uses independent finite-count formulas based on Möbius inversion to check the exact subset counts and both localization inequalities for all \(2\le n\le1500\). It also checks, for all \(1\le n\le200000\), the exact residue-class enumeration of least nondivisors. Successful output begins `VERIFY_OK`. Finite checks test formulas and edge cases; the infinite theorem rests on the preceding argument.

## Relationship to prior work

Pongsriiam, *Relatively Prime Sets, Divisor Sums, and Partial Sums* (arXiv:1306.4891v1; Journal of Integer Sequences 16 (2013), Article 13.9.1), defined these counts, established the gcd-divisor interpretation of \(D(n)\), and expressly asked in Question 3.3 about the upper and lower limits of the displayed ratio. His later *Local behaviors of the number of relatively prime sets* (2015/2016), Theorem 9, establishes the alternating sign of \(D(n)-\Phi(n)\), which gives only a weaker comparison of the deficits and does not establish their exponential escape rates or the atomic limit law. Łydka (2019) treats different inequalities for related subset-counting functions. The OEIS entry A224840 tabulates \(D(n)\) and its interpretation, not this log-ratio distribution.

## Limitations

The theorem establishes a weak limiting distribution on the logarithmic scale, not a limiting distribution for the unscaled ratio, which diverges on one parity and vanishes on the other. It does not evaluate the two summatory expressions separately proposed in Question 3.3, nor does it imply a uniform relative asymptotic for the individual deficits. Originality comparisons cover identified sources, not every possible unindexed proof.

## References

1. P. Pongsriiam, *Relatively Prime Sets, Divisor Sums, and Partial Sums*, arXiv:1306.4891v1 (20 June 2013), https://arxiv.org/abs/1306.4891 ; Journal of Integer Sequences 16 (2013), Article 13.9.1, https://cs.uwaterloo.ca/journals/JIS/VOL16/Pongsriiam/pong2.html .
2. P. Pongsriiam, *Local behaviors of the number of relatively prime sets*, International Journal of Number Theory 12 (2016), 1575–1593, DOI:10.1142/S1793042116500962, https://www.researchgate.net/publication/287391047_Local_behaviors_of_the_number_of_relatively_prime_sets .
3. A. Łydka, *On some properties of the function of the number of relatively prime subsets*, arXiv:1910.02418v1 (2019), https://arxiv.org/html/1910.02418v1 .
4. OEIS A224840, *Divisor sum of the arithmetic function A085945*, https://oeis.org/A224840 .
