# Density dichotomy for prime-adic valuations of divisor power sums

## Finding

For a fixed integer \(r\ge 1\), define the divisor power sum
\[
\sigma_r(n)=\sum_{d\mid n}d^r
\]
and write \(V_{p,r}(n)=\nu_p(\sigma_r(n))\). Say that \(V_{p,r}\) diverges in natural density if, for every fixed integer \(K\ge1\), the set of positive integers \(n\) with \(V_{p,r}(n)<K\) has natural density zero.

**Theorem.** For \(p=2\), \(V_{p,r}\) diverges in natural density for every \(r\ge1\). For an odd prime \(p\), this divergence holds if and only if \(-1\) is an \(r\)-th power in \(\mathbb F_p^\times\), equivalently
\[
\nu_2(p-1)>\nu_2(r).
\]
If this condition fails, there is a finite constant \(C_{p,r}\) such that, for every real \(x\ge1\),
\[
\frac1x\sum_{n\le x}V_{p,r}(n)\le C_{p,r}.
\]
Thus the valuation family is tight in natural density in the non-root case, giving an exact dichotomy between density divergence and a uniform mean bound.

## Assumptions and scope

The parameters \(p\) and \(r\) are fixed throughout; \(p\) is prime and \(r\) is a positive integer. Natural density is taken among all positive integers. The theorem makes no uniformity claim as either parameter varies. The mean-bound alternative is stronger than merely saying that density divergence fails.

## Proof

Put
\[
S_{q,a}=1+q^r+q^{2r}+\cdots+q^{ar}
\]
for a prime \(q\) and integer \(a\ge1\). Multiplicativity gives
\[
V_{p,r}(n)=\sum_{q^a\parallel n}\nu_p(S_{q,a}).
\]

First suppose \(p=2\), or suppose \(p\) is odd and \(-1\) is an \(r\)-th power modulo \(p\). In the latter case choose a nonzero residue \(b\pmod p\) with \(b^r\equiv-1\pmod p\). Dirichlet's theorem implies that the reciprocal sum of primes \(q\equiv b\pmod p\) diverges. For each such prime, \(p\mid S_{q,1}=1+q^r\). When \(p=2\), the same divisibility holds for every odd prime \(q\), and the reciprocal sum of odd primes diverges.

For any finite set \(Q\) of primes from the relevant set, the events \(q\parallel n\) are independent in natural density, with probability \(1/q-1/q^2\). The sum of these probabilities diverges as the finite sets increase. If \(X_Q(n)=\#\{q\in Q:q\parallel n\}\), then its mean \(\mu_Q=\sum_{q\in Q}(1/q-1/q^2)\) tends to infinity and its variance is at most \(\mu_Q\). Chebyshev's inequality therefore shows, for every fixed \(K\), that the density of integers with \(X_Q(n)<K\) tends to zero as \(Q\) increases. Each such prime contributes at least one to \(V_{p,r}(n)\), so \(V_{p,r}\) diverges in natural density.

Now let \(p\) be odd and assume that \(-1\) is not an \(r\)-th power modulo \(p\). Then \(p\nmid S_{q,1}\) for every prime \(q\ne p\), while \(S_{p,a}\equiv1\pmod p\) for every \(a\). Hence only exponents \(a\ge2\) can contribute to \(V_{p,r}(n)\). Since
\[
S_{q,a}\le(a+1)q^{ar},
\]
we have
\[
\nu_p(S_{q,a})\le\log_p(a+1)+ar\log_p q.
\]
For every \(x\ge1\), the number of integers \(n\le x\) with \(q^a\parallel n\) is at most \(x/q^a\). Consequently
\[
\frac1x\sum_{n\le x}V_{p,r}(n)
\le \sum_{q\text{ prime}}\sum_{a\ge2}
\frac{\log_p(a+1)+ar\log_p q}{q^a}
=:C_{p,r}.
\]
The series converges: the inner sum is \(O_{p,r}((1+\log q)/q^2)\), and \(\sum_{m\ge2}(1+\log m)/m^2\) converges. Markov's inequality gives an upper density at most \(C_{p,r}/K\) for the set where \(V_{p,r}(n)\ge K\). In particular, for sufficiently large fixed \(K\), that upper density is strictly less than one, so density divergence is impossible; moreover the tail upper densities tend to zero as \(K\to\infty\). This proves the mean-bound and tightness assertions.

Finally, the multiplicative group \(\mathbb F_p^\times\) is cyclic of order \(p-1\). The equation \(z^r=-1\) is solvable precisely when \(\gcd(r,p-1)\mid(p-1)/2\), which is equivalent to \(\nu_2(r)<\nu_2(p-1)\). The proof covers all prime and exponent cases.

## Verification

The argument is symbolic and uses no finite computation as a substitute for an infinite statement. Its analytic input is Dirichlet's theorem that primes in a fixed reduced residue class have divergent reciprocal sum. Independence of the finitely many conditions \(q\parallel n\) follows from the Chinese remainder theorem. The convergent mean-bound series and all local factors are displayed explicitly.

## Relationship to prior work

Pollack and Pomerance studied density phenomena for the ordinary divisor sum \(\sigma_1(n)\), including growth of its prime-adic valuations. Amdeberhan, Moll, Sharma, and Villamizar gave exact local valuation formulas for \(\nu_p(\sigma_1(n))\). Those results concern \(r=1\) and/or the ordinary divisor sum; they do not state the root criterion for arbitrary \(\sigma_r\) together with the complementary uniform mean bound. MacMillan and Sondow's treatment of power-sum congruences supplies related finite-field context but not this density dichotomy.

## Limitations

No explicit rate of convergence in the density-divergent case is established. In the non-root case the result gives a finite uniform mean bound, not an exact limiting distribution or a sharp tail estimate. The parameters \(p\) and \(r\) are fixed, and no uniformity over growing parameter ranges is claimed.

## References

1. P. Pollack and C. Pomerance, “Some problems of Erdős on the sum-of-divisors function,” *Transactions of the American Mathematical Society, Series B* 3 (2016), 1–26. DOI: 10.1090/btran/10.
2. T. Amdeberhan, V. H. Moll, V. Sharma, and D. Villamizar, “Arithmetic Properties of the Sum of Divisors,” arXiv:2007.03088 (2020).
3. K. MacMillan and J. Sondow, “Proofs of Power Sum and Binomial Coefficient Congruences Via Pascal’s Identity,” arXiv:1011.0076 (2010).
