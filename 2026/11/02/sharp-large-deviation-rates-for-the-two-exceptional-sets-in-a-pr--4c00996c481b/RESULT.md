# Sharp large-deviation rates for the two exceptional sets in a prime-square Romanoff sieve

## Finding

For real \(Y\ge5\), let \(\mathcal P_Y\) be the odd primes at most \(Y\), and put
\[
Q_Y=\prod_{p\in\mathcal P_Y}p,\quad H_Y=\sum_{p\in\mathcal P_Y}\frac1p,\quad
\chi(p)=\begin{cases}1,&p\equiv1\pmod4,\\-1,&p\equiv3\pmod4,\end{cases}
\]
\[
T_Y(n)=\sum_{\substack{p\in\mathcal P_Y\\p\mid n}}\chi(p)
-\sum_{p\in\mathcal P_Y}\frac{\chi(p)}p.
\]
Define the two normalized exceptional proportions
\[
E_Y^{\rm all}=\frac1{Q_Y}\#\{1\le n\le Q_Y:T_Y(n)\ge H_Y/2\},
\]
\[
E_Y^{\rm sq}=\frac1{\varphi(Q_Y)^2}
\#\{1\le u,v\le Q_Y:\gcd(uv,Q_Y)=1,\ T_Y(u^2+v^2)<H_Y/2\}.
\]
Then both have exact, strictly positive logarithmic large-deviation rates:
\[
\boxed{\lim_{Y\to\infty}\frac{-\log E_Y^{\rm all}}{H_Y}
=\frac12\log\frac{1+\sqrt5}{2}+1-\frac{\sqrt5}{2}
=0.1225719237799\ldots,}
\]
\[
\boxed{\lim_{Y\to\infty}\frac{-\log E_Y^{\rm sq}}{H_Y}
=\frac{1-\log2}{2}=0.1534264097200\ldots.}
\]
Equivalently, by Mertens' theorem, these proportions are respectively
\((\log Y)^{-c_{\rm all}+o(1)}\) and \((\log Y)^{-c_{\rm sq}+o(1)}\),
where the displayed constants are \(c_{\rm all}\) and \(c_{\rm sq}\). The estimates concern the particular canonical nested prime sets \(\mathcal P_Y\), not arbitrary finite sets of primes.

## Assumptions and scope

All primes are ordinary rational primes; \(Y\to\infty\) through real values. Residue classes are uniform in \(\mathbb Z/Q_Y\mathbb Z\) for the first event and uniform independent units for the second. Every denominator is nonzero. No unproved hypothesis is used. The result is an asymptotic in the prime cutoff \(Y\), not a uniform bound in the original representation-counting variable or a quantitative rate for every divisibility chain.

## Proof

**1. The character prime sums.** Dirichlet's theorem together with the standard Mertens estimates for reduced classes modulo four gives
\[
\sum_{\substack{p\le Y\\p\equiv1\ (4)}}\frac1p
=\frac{H_Y}{2}+O(1),\qquad
\sum_{\substack{p\le Y\\p\equiv3\ (4)}}\frac1p
=\frac{H_Y}{2}+O(1),\qquad H_Y\to\infty,
\]
and \(H_Y=\log\log Y+O(1)\). In particular \(S_Y=\sum\chi(p)/p=O(1)\). Only these asymptotics, rather than precise Mertens constants, are needed.

**2. The all-residue rate.** For uniform \(n\bmod Q_Y\), the Chinese remainder theorem makes the indicators \(B_p=\mathbf1_{p\mid n}\) independent Bernoulli variables of success probability \(1/p\). Hence for each fixed real \(t\),
\[
\Lambda_Y(t):=\log\mathbb E e^{tT_Y(n)}
=\sum_{p\in\mathcal P_Y}\left[\log\left(1+\frac{e^{t\chi(p)}-1}{p}\right)-\frac{t\chi(p)}p\right]
=H_Y(\cosh t-1)+O_t(1).
\]
The error is bounded because \(\sum_p p^{-2}<\infty\); the same bound applies to the first two derivatives for fixed \(t\). At threshold \(H_Y/2\), exponential Markov with \(t_*=\operatorname{arsinh}(1/2)>0\) gives
\[
\limsup H_Y^{-1}\log E_Y^{\rm all}
\le \cosh t_*-1-t_*/2=-c_{\rm all}.
\]
For the reverse inequality, tilt the finite independent Bernoulli product measure by density \(e^{t_*T_Y-\Lambda_Y(t_*)}\). The tilted mean and variance of \(T_Y\) are respectively \(H_Y/2+O(1)\) and \(H_Y\cosh t_*+O(1)\). Each independent centered summand is uniformly bounded and the variance tends to infinity, so Lindeberg's central limit theorem applies. The tilted probability of the interval \([H_Y/2,H_Y/2+H_Y^{2/3}]\) tends to \(1/2\). Undoing the change of measure on that interval yields
\[
\log E_Y^{\rm all}\ge
\Lambda_Y(t_*)-t_*(H_Y/2+H_Y^{2/3})+o(H_Y)
=-c_{\rm all}H_Y-o(H_Y).
\]
Since \(\cosh t_*=\sqrt5/2\) and \(t_*=\log((1+\sqrt5)/2)\), this proves the first rate.

**3. The quadratic-unit rate.** For independent uniform units \(u,v\bmod Q_Y\), the CRT gives independent local events \(p\mid u^2+v^2\). For \(p\equiv3\pmod4\) this is impossible, whereas for \(p\equiv1\pmod4\) it occurs with probability \(w_p=2/(p-1)\): the ratio \(u/v\) is uniform in \(\mathbb F_p^\times\), and \(-1\) has exactly two square roots. Write \(Z_Y=\sum_{p\equiv1\ (4)}B'_p\) with these independent Bernoulli variables and
\[
M_Y=\mathbb EZ_Y=\sum_{\substack{p\le Y\\p\equiv1\ (4)}}\frac2{p-1}=H_Y+O(1).
\]
We have \(T_Y(u^2+v^2)=Z_Y-S_Y\), so the second event is \(Z_Y<H_Y/2+S_Y=M_Y/2+O(1)\). Its log moment generating function satisfies
\[
K_Y(t):=\log\mathbb E e^{tZ_Y}
=\sum_{p\equiv1\ (4)}\log(1+w_p(e^t-1))
=M_Y(e^t-1)+O_t(1),
\]
again with bounded first and second derivative errors. Exponential Markov at \(t_0=-\log2\) gives
\[
\limsup H_Y^{-1}\log E_Y^{\rm sq}\le
(e^{t_0}-1)-t_0/2=-c_{\rm sq}.
\]
Under the exponential tilt \(e^{t_0Z_Y-K_Y(t_0)}\), the mean and variance of \(Z_Y\) are \(M_Y/2+O(1)\) and \(M_Y/2+O(1)\). Lindeberg's theorem gives tilted probability tending to \(1/2\) for the interval \([M_Y/2-H_Y^{2/3},\ H_Y/2+S_Y)\). Reversing the tilt on this interval provides
\[
\log E_Y^{\rm sq}\ge K_Y(t_0)-t_0M_Y/2-o(H_Y)
=-c_{\rm sq}H_Y-o(H_Y).
\]
Thus \(c_{\rm sq}=(1-\log2)/2\). The tilting steps establish lower as well as upper exponential bounds; a one-sided Chernoff estimate alone would not prove the claimed limits. \(\square\)

## Verification

Run `python3 verify.py` with the standard Python library. It independently computes exact rational convolution laws of the CRT Bernoulli variables for nine prime cutoffs, and exhaustively enumerates all residue classes and all unit pairs at cutoffs \(Y=5,7,11\). The program reports `VERIFY_OK prime_set_cutoffs=9 direct_CRT_cutoffs=3`. These finite checks do not prove the limits. The limit proof uses the character-class prime harmonic estimates, finite-product moment expansions, and a tilted triangular-array central limit theorem.

## Relationship to prior work

Yan and Xu, *A necessary condition for a Romanoff type theorem*, arXiv:2610.28237v1 (first posted 2026-10-20), define exactly these two exceptional events in their Lemma 2.1 for a general finite set of odd primes. Their bounds are \(E^{\rm all}\le4/H\) and \(E^{\rm sq}\le10/H\), proved by second moments and Chebyshev's inequality. The new statement is the sharp logarithmic rate along the canonical all-primes cutoff, which is not implied by either moment bound. The local congruence counts in their proof are compatible with and motivate the exact independent Bernoulli factorization used here. General exponential tilting, large-deviation, and mod-Poisson methods provide applicable analytic machinery; their existence alone does not supply these two arithmetically specialized constants without the splitting-prime analysis. The positive-density theorem of Dai and Pan concerns a different implication and does not state the exceptional-tail limits.

## Limitations

The rates do not identify leading constants, uniform finite-cutoff errors, or effective estimates for the original Romanoff representation set as its summation bound grows. The proof depends on standard Mertens estimates in residue classes and a central limit theorem under exponential tilting; its elementary exact congruence computations are not alone an infinite proof. Literature priority may require further review, especially of general precise-deviation theorems whose hypotheses can be specialized to this independent Bernoulli model.

## References

1. X.-H. Yan and Y.-T. Xu, *A necessary condition for a Romanoff type theorem*, arXiv:2610.28237v1, 2026-10-20, Section 2, Lemma 2.1, and Section 3. https://arxiv.org/html/2610.28237v1
2. L.-X. Dai and H. Pan, *On Erdős' generalization of the Romanoff theorem*, Journal of Number Theory 291 (2027), 65–73, DOI 10.1016/j.jnt.2026.04.003 (bibliographic comparison only).
3. Standard results: Mertens theorem in residue classes modulo four; exponential change of measure and the Lindeberg central limit theorem for independent bounded triangular arrays.
