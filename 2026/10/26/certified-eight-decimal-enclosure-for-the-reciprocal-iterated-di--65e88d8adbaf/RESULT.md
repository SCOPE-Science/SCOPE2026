# A certified numerical enclosure for the Erdős–Ramanujan hybrid divisor-sum constant

## Finding

Let \(\tau(n)\) denote the number of positive divisors of \(n\). John M. Campbell's hybrid divisor-sum theorem defines a positive constant \(c_3\) by
\[
\sum_{n\le x}\frac{1}{\tau(\tau(n))}
\sim c_3\frac{x}{\log\log x}.
\]
The constant satisfies the **rigorously certified strict enclosure**
\[
\boxed{0.8367013214802<c_3<0.8367013318136}.
\]
In particular, \(0.83670132<c_3<0.83670134\). The existing source proves an absolutely convergent series for \(c_3\) and bounds it between \(6/\pi^2\) and \(1\); the contribution here is its explicitly verified narrow numerical enclosure, not the original asymptotic theorem or series.

## Assumptions and scope

Let \(E_p\), for primes \(p\), be independent nonnegative-integer-valued random variables with
\[
\Pr(E_p=e)=\frac{p-1}{p^{e+1}}\qquad(e\ge0).
\]
Write \(\operatorname{odd}(m)=m/2^{\nu_2(m)}\) and
\[
V=\prod_p\operatorname{odd}(E_p+1).
\]
Almost surely only finitely many factors differ from one, since \(\Pr(E_p\ge2)=p^{-2}\) is summable. The constant given by Campbell's powerful-number expansion equals
\[
c_3=\mathbb E\frac{1}{\tau(V)}.
\]
Indeed, the prime-power exponent distribution is the limiting distribution of the valuations of a uniformly chosen integer, and grouping the outcomes with exponents at least two reproduces the powerful-part weights in Campbell's Lemmas 8–9. No numerical approximation to the original asymptotic error term is asserted.

## Proof

**Analytic truncation.** Put \(T=1000\) and \(P=10^8\). Define the finite-product proxy \(\widetilde V\) by retaining \(\operatorname{odd}(E_p+1)\) for primes \(p\le T\), retaining only the factor \(3\) if \(E_p=2\) for primes \(T<p\le P\), and replacing all other factors by \(1\). Then \(\widetilde V\mid V\), so \(\tau(\widetilde V)\le\tau(V)\). The proxy differs from the original factorization only if some prime in \((T,P]\) has exponent at least four or some prime above \(P\) has exponent at least two. Therefore
\[
0\le \mathbb E\frac1{\tau(\widetilde V)}-c_3
\le \sum_{p>T}p^{-4}+\sum_{p>P}p^{-2}
\le\frac1{3T^3}+\frac1P=:\Delta.
\]
The two last inequalities follow by bounding the prime sums by the corresponding integer sums and applying the integral test; they require no unproved prime-distribution hypothesis.

**Finite distributions.** For each \(p\le T\), form the outcomes \(\operatorname{odd}(e+1)\) with weights \((p-1)p^{-e-1}\). For \(T<p\le P\), the proxy has a Bernoulli factor equal to \(3\) with probability
\[
u_p=\Pr(E_p=2)=\frac{p-1}{p^3}.
\]
Hence the number of factors \(3\) from these latter primes has probability generating function
\[
\prod_{T<p\le P}(1-u_p+u_p z).
\]
No factorization of \(\tau(V)\) over primes is assumed: one tracks the distribution of the *product* of odd parts, then applies \(1/\tau\) to that product.

**Outward integer arithmetic.** The executable verifier uses \(Q=10^{40}\). Its small-prime dynamic program stores integer masses \(q_v\), each divided by \(Q\) being a lower bound for the probability of the corresponding odd product \(v\). It truncates exponents only when a power threshold \(10^{22}\) has been crossed and prunes tiny states; all truncated, pruned, and downward-rounded mass is retained as a *deficit*. For the large-prime polynomial, integers \(r_k\), with \(0\le k\le4\), similarly lower-bound the probability of exactly \(k\) selected exponent-two primes. Every transition uses integer floor division, so every stored coefficient remains a genuine lower bound. Let
\[
q_{v,k}=\left\lfloor\frac{q_vr_k}{Q}\right\rfloor,
\quad M=\sum_{v,k}q_{v,k},
\quad A=\sum_{v,k}\left\lfloor\frac{q_{v,k}}{\tau(v3^k)}\right\rfloor,
\quad B=\sum_{v,k}\left\lceil\frac{q_{v,k}}{\tau(v3^k)}\right\rceil.
\]
All these are explicitly computed integers. The represented events are disjoint and have total true probability at most one, while the missing mass can contribute at most one per unit probability. Thus
\[
\boxed{\frac A Q-\Delta\le c_3\le\frac{B+Q-M}{Q}}.
\]
The lower inequality also uses the analytic truncation bound. The ceiling in \(B\) is essential: flooring the final reciprocal contributions does not by itself yield an upper bound.

The exact-integer run returns
\[
\begin{aligned}
A&=8367013318135509892186352836613985176166,\\
B&=8367013318135509892186352836613985178670,\\
M&=9999999999999996795473552682174647177884.
\end{aligned}
\]
Substituting these integers and \(\Delta=1/10^8+1/(3\cdot1000^3)\), and comparing rational numbers by cross-multiplication, proves the displayed strict enclosure.

## Verification

Run `python3 verify.py` using a Python 3 standard-library interpreter. It uses an odd-only Eratosthenes sieve through \(10^8\), exact integer fixed-point coefficients, direct divisor counting for the finite states, and an independent small-instance rational convolution check. The full computation yields \(536\) retained small-prime states, processes \(5{,}761{,}287\) primes in \((1000,10^8]\), and prints:

```
CERTIFIED_LOWER_FLOOR_13 8367013214802
CERTIFIED_UPPER_CEIL_13 8367013318136
CONTRIBUTION 8367013318135509892186352836613985176166
CEILING_CONTRIBUTION 8367013318135509892186352836613985178670
REPRESENTED_MASS 9999999999999996795473552682174647177884
SMALL_STATES 536
LARGE_PRIMES 5761287
SANITY_RATIONAL_STATES 7
VERIFY_OK rational_tiny=PASS exact_integer_interval=PASS prime_tail=PASS
```

The computation is *finite* and exhaustive only within its stated truncated probabilistic state space; the rigorous tail inequalities above connect it to the infinite constant. No Monte Carlo sampling, numerical quadrature, floating-point rounding, or assumption that a finite prefix of primes is complete is used.

## Relationship to prior work

Campbell, *On divisor sums due to Erdős and Ramanujan*, arXiv:2605.00695, version 2 of 16 October 2026, proves the asymptotic, gives the powerful-number series and bounds \(6/\pi^2\le c_3\le1\) (Lemmas 8–9 and Theorem 2). Those are inputs, not claimed contributions. The present result supplies a rapidly convergent exact-integer computation that identifies the constant to a certified narrow interval. Searches for this constant, its reciprocal iterated-divisor formulation, the powerful-part series, and a prior numerical evaluation did not locate an equivalent certified enclosure. This is a best-knowledge comparison rather than a universal priority guarantee.

## Limitations

The new conclusion is a numerical interval for an already-defined, already-proved asymptotic constant; it is not a new asymptotic formula, an effective error term in the summatory function, a closed form, or a computation of the related constants for other divisor sums. The interval is certified conditionally only on the standard arithmetic of independent prime-adic valuations and the correctly specified source constant, both justified above. An unindexed independent numerical evaluation remains possible.

## References

1. John M. Campbell, *On divisor sums due to Erdős and Ramanujan*, arXiv:2605.00695v2 (2026), especially Lemmas 7–9 and Theorem 2. https://arxiv.org/html/2605.00695v2
2. arXiv historical record of the first version, posted 1 May 2026: https://arxiv.org/abs/2605.00695
