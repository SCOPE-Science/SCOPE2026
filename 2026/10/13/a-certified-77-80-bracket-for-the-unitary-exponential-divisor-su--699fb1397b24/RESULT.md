# A certified \(77\%\)–\(80\%\) bracket for the unitary–exponential divisor-sum comparison

## Finding
For positive integers \(n\), let \(\sigma^*(n)\) be the sum of unitary divisors and \(\sigma^{(e)}(n)\) the sum of exponential divisors. Define
\[
\mathcal A=\{n\ge1:\sigma^*(n)>\sigma^{(e)}(n)\},\qquad
\underline d(\mathcal A)=\liminf_{X\to\infty}\frac{\#(\mathcal A\cap[1,X])}{X},\quad
\overline d(\mathcal A)=\limsup_{X\to\infty}\frac{\#(\mathcal A\cap[1,X])}{X}.
\]
Then the following **unconditional two-sided bracket** holds:
\[
\boxed{\frac{77}{100}<\underline d(\mathcal A)\le\overline d(\mathcal A)<\frac45.}
\]
More precisely, with
\[
A=\frac{2016299456056220800244533835602991}{265252859812191058636308480000000},\qquad
U=\frac{17145880455178697494282924151970863011}{21479832291515325918007548199218750000},
\]
the proof establishes
\[
\frac{A}{\pi^2}\le \underline d(\mathcal A)\le\overline d(\mathcal A)\le U,
\]
where \(A/\pi^2\approx0.7701852775863\) and \(U\approx0.7982315793942\). This does not assert the exact density. The bounds remain valid whether or not a natural density is assumed to exist.

## Assumptions and scope
For each prime \(p\), set \(\nu_p(n)\) to be its exponent in \(n\). Multiplicativity gives
\[
\rho_p(0)=1,\qquad
\rho_p(a)=\frac{1+p^a}{\sum_{d\mid a}p^d}\quad(a\ge1),\qquad
\frac{\sigma^*(n)}{\sigma^{(e)}(n)}=\prod_{p\mid n}\rho_p(\nu_p(n)).
\]
For the finite certificate, take the primes and exponent caps in order
\[
P=(2,3,5,7,11,13,17,19,23,29),\qquad
E=(12,9,6,4,3,3,2,2,2,2).
\]
For a vector \(\mathbf a=(a_p)_{p\in P}\) with \(0\le a_p\le E_p\), define
\[
R(\mathbf a)=\prod_{p\in P}\rho_p(a_p),\quad
D=\prod_{p\in P}p^{E_p+1},\quad
w(\mathbf a)=\prod_{p\in P}(p-1)p^{E_p-a_p}.
\]
The exact natural density of integers with these specified small-prime exponents is \(w(\mathbf a)/D\). Let \(G\) denote the vectors with \(R(\mathbf a)\ge1\). Only the single stated comparison set and its lower and upper asymptotic densities are addressed.

## Proof
**1. Local signs.** If \(a=1\), then \(\rho_p(1)=1+1/p>1\). If \(a\ge2\), the exponential-divisor sum includes both \(p\) and \(p^a\), so \(\rho_p(a)<1\). Hence, for the primes \(q>29\), the logarithm of the contribution of any prime power dividing \(n\) satisfies
\[
\log\rho_q(\nu_q(n))\le\frac{\mathbf1_{q\mid n}}q.
\]

**2. A lower-density cylinder union.** Restrict \(\mathbf a\) to \(G\) and every larger prime \(q>29\) to exponent zero or one. All tail factors are at least one. If \(R(\mathbf a)=1\), the final comparison is strict as soon as any tail prime divides \(n\); the cases with no tail prime form a finite set because every exponent in \(\mathbf a\) is bounded. The density of this union (excluding finitely many possible exceptions) is
\[
L=\frac{\sum_{\mathbf a\in G}w(\mathbf a)}{D}\prod_{q>29}\left(1-\frac1{q^2}\right)
=\frac6{\pi^2}\frac{\sum_{\mathbf a\in G}w(\mathbf a)}{D\prod_{p\in P}(1-p^{-2})}.
\]
The squarefree-tail Euler product follows by finite inclusion–exclusion and the convergent sum of reciprocal prime squares. Integer enumeration gives \(\sum_{\mathbf a\in G}w(\mathbf a)=2060396086464126833643545810150335261409280\), making \(L=A/\pi^2\). Machin's identity and alternating-arctangent rational bounds verify \(\pi^2<987/100\), so
\[
L>\frac{100A}{987}
=\frac{2016299456056220800244533835602991}{2618045726346325748740364697600000}
>\frac{77}{100}.
\]

**3. Tail Markov obstruction.** Let
\[
T(n)=\sum_{\substack{q>29\\q\mid n}}\frac1q,\qquad
\mu=\sum_{q>29}\frac1{q^2},
\]
where both sums are over primes. For a small-prime vector with \(R(\mathbf a)<1\), positivity of the full divisor-sum ratio requires
\[
T(n)>-\log R(\mathbf a)\ge 1-R(\mathbf a).
\]
For every fixed small-prime valuation cylinder, the asymptotic average of \(T\) over all integers in that cylinder is
\[
\frac{w(\mathbf a)}D\,\mu.
\]
Indeed, for any fixed tail prime \(q\), the Chinese remainder theorem gives density \(w(\mathbf a)/(Dq)\) for the intersection with \(q\mid n\). Interchanging the prime sum with the limit is justified by the uniform estimate for primes \(q>Y\):
\[
\frac1X\sum_{n\le X}\sum_{\substack{q>Y\\q\mid n}}\frac1q
\le\sum_{q>Y}\frac1{q^2}\longrightarrow0.
\]
Markov's inequality therefore bounds the upper density of favorable integers in a negative-ratio cylinder by
\[
\frac{w(\mathbf a)}D\min\left(1,\frac{\mu}{1-R(\mathbf a)}\right).
\]

**4. Rational finite upper certificate.** A sieve of primes through \(100000\), integer upper-rounding with denominator \(10^{10}\), and \(\sum_{m>100000}m^{-2}<1/100000\) give
\[
\mu<\frac{72465244}{10^{10}}<\frac{29}{4000}.
\]
Put \(Q=10^6\). For each vector with \(R(\mathbf a)=u/v<1\), use the rational upper approximation
\[
b(\mathbf a)=\min\left(Q,\left\lceil\frac{29Qv}{4000(v-u)}\right\rceil\right).
\]
Then the total upper density is at most
\[
1-\frac1{QD}\sum_{R(\mathbf a)<1}w(\mathbf a)(Q-b(\mathbf a)).
\]
The leading \(1\) includes every small-prime exponent vector omitted by the finite caps without imposing any favorable property on it. Exhaustive exact enumeration of the \(5896800\) capped vectors yields
\[
\begin{aligned}
D&=2655901350996199279464314052991681920000000,\\
\sum_{R<1}w&=593415378686113363806646633931531172741120,\\
\sum_{R<1}wb&=57538357810785019098554221682665403810192916480,
\end{aligned}
\]
and consequently the right-hand side equals \(U<4/5\). This establishes the claimed upper-density bound and completes the theorem.

## Verification
The standalone standard-library script `verify_density.py` enumerates every permitted prime-exponent vector with exact integers, computes the specified density weights, checks the six exact-product equality vectors, and reproduces \(A\), \(U\), the rational lower certificate, the tail reciprocal-square majorant, and the two strict rational threshold comparisons. It does not infer the infinite statement from finite experimentation: the proof's Euler-product, Chinese-remainder, and Markov steps are separate analytic arguments. Run from the same directory using `python3 verify_density.py`. The final exact certificate reports `EXACT_CERTIFICATE_OK`, \(5896800\) patterns, and \(2096262\) vectors with \(R\ge1\).

## Relationship to prior work
Trudgian's *The sum of the unitary divisor function* (first publicly submitted 2013-12-17) posed the proportion question, proved the squarefree baseline \(6/\pi^2\), and reported a finite-range proportion near \(0.778307\). A subsequent exact finite-cylinder result established the one-sided lower bound \(0.753659844064288\ldots\) using six primes and small exponents. That result does **not** imply an upper bound smaller than one; increasing a finite lower-bound census alone is not the principal contribution here. The essential new ingredient is a **tail-sensitive, conditional Markov majorant** in every negative small-prime cylinder, producing an explicit nontrivial upper bound below \(0.8\) while sharpening the lower bound beyond \(0.77\). OEIS A322446 tabulates finite initial counts only, not this two-sided theorem.

## Limitations
Neither displayed constant is claimed optimal, and the exact natural density is not calculated. The upper estimate uses a first moment of the large-prime tail and can be improved by finer moment or cylinder information. The exact finite arithmetic is a certificate for a rational inequality, not an exhaustive enumeration of all integers. Searches and comparisons did not locate a stronger prior two-sided bound, but unindexed earlier analysis remains possible. Nothing here establishes infinitude or classification of equality solutions \(\sigma^*(n)=\sigma^{(e)}(n)\).

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1 (first public 2013-12-17), final arXiv:1312.4615v3; *Publ. Inst. Math. (Beograd)* 97 (2015), 175–180. DOI 10.2298/PIM140617001T.
2. *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density* (2026), published mathematical record identifier `831dd476-bf82-4273-849f-84ab869fe344`; compared at the level of theorem and proof.
3. OEIS A322446, *The number of solutions to usigma(k) > esigma(k) below powers of ten*, first contributed 2019; finite data only.
