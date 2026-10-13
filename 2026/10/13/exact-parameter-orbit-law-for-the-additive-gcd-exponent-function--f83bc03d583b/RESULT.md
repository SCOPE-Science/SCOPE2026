# Exact parameter orbit law for the additive gcd-exponent function
## Finding
Let \(n=\prod_{i=1}^r p_i^{\alpha_i}>1\), put \(L=\operatorname{lcm}(\alpha_1,\ldots,\alpha_r)\), and define
\[
f_k(n)=\sum_{i=1}^r\gcd(k,\alpha_i)\qquad(k\ge1).
\]
For every divisor \(d\mid L\), write
\[
F(d)=\sum_{i=1}^r\gcd(d,\alpha_i).
\]
Then, for every positive integer \(k\),
\[
f_k(n)=F(\gcd(k,L)).
\]
Thus the full parameter orbit is the divisor-lattice profile of \(F\). In one complete period, any value \(y\) occurs exactly
\[
\sum_{\substack{d\mid L\\F(d)=y}}\varphi(L/d)
\]
times. Moreover, \(L\) is the exact least positive period. The minimum is \(r=\omega(n)\), attained precisely when \(\gcd(k,L)=1\), so it occurs \(\varphi(L)\) times per period. The maximum is \(\sum_i\alpha_i=\Omega(n)\), attained precisely when \(L\mid k\), hence once per period. Finally,
\[
\frac1L\sum_{k=1}^L f_k(n)=\sum_{i=1}^r\sum_{d\mid\alpha_i}\frac{\varphi(d)}{d}.
\]

## Assumptions and scope
The integer \(n>1\) is arbitrary, with distinct primes \(p_i\) and positive exponents \(\alpha_i\). The parameter \(k\) ranges over all positive integers. The theorem concerns the additive function introduced by Bouderbala and Karras, not the distinct multiplicative exponent functions that also use gcds of exponents.

## Proof
Because every \(\alpha_i\) divides \(L\),
\[
\gcd(k,\alpha_i)=\gcd(\gcd(k,L),\alpha_i),
\]
which proves \(f_k(n)=F(\gcd(k,L))\). For a fixed divisor \(d\mid L\), the integers \(1\le k\le L\) satisfying \(\gcd(k,L)=d\) are exactly \(k=dj\) with \(1\le j\le L/d\) and \(\gcd(j,L/d)=1\); hence there are \(\varphi(L/d)\) of them. Summing those weights over divisors having the same \(F\)-value gives the asserted complete value distribution.

The source proves that \(L\) is a period. To see it is the least positive period, suppose a positive period \(T<L\) existed. Periodicity would give \(f_L(n)=f_{L-T}(n)\). Since \(f_L(n)=\sum_i\alpha_i\) and every summand \(\gcd(L-T,\alpha_i)\) is at most \(\alpha_i\), equality of the sums forces \(\alpha_i\mid L-T\) for every \(i\). Therefore \(L\mid L-T\), impossible because \(0<L-T<L\).

Each gcd summand is at least \(1\), so the minimum is \(r\). Equality holds exactly when \(\gcd(k,\alpha_i)=1\) for every \(i\), equivalently \(\gcd(k,L)=1\). Each summand is at most \(\alpha_i\), so the maximum is \(\sum_i\alpha_i\), and equality holds exactly when every \(\alpha_i\mid k\), equivalently \(L\mid k\).

For the mean, each residue pattern modulo \(\alpha_i\) is repeated \(L/\alpha_i\) times in \(1\le k\le L\). The classical gcd-sum identity gives
\[
\sum_{k=1}^{\alpha_i}\gcd(k,\alpha_i)=\sum_{q\mid\alpha_i}\frac{\alpha_i}{q}\varphi(q).
\]
After division by \(L\) and summation over \(i\), this yields the displayed mean formula.

## Verification
The bundled verifier exhausts all ordered exponent tuples of support size at most \(4\) with every exponent between \(1\) and \(8\). For each tuple it checks the gcd-projection formula, the complete divisor-weighted distribution, the exact minimum and maximum multiplicities, absence of any smaller divisor-period, and the first-moment identity. It reports `VERIFY_OK exponent_tuples=4680 parameter_checks=323280 max_L=840 support_max=4 exponent_max=8`. This is regression evidence; the proof above is symbolic and applies without bounds.

## Relationship to prior work
Bouderbala and Karras define \(f_k\) and prove in their Theorem 2.2 that \(L=\operatorname{lcm}(\alpha_1,\ldots,\alpha_r)\) is a period. Their Theorem 2.4 gives one sufficient condition for equality between two parameter values. The present theorem sharpens the period statement to the exact least period and gives the complete parameter distribution through the divisor projection \(k\mapsto\gcd(k,L)\), including exact multiplicities, extrema, and mean. The inspected source does not state these conclusions.

## Limitations
The theorem determines the multiset of values in every period, but it does not give a closed formula for the number of distinct values of \(F\), because incomparable divisors of \(L\) can have equal \(F\)-values. No claim is made about analytic averages over varying \(n\).

## References
Bouderbala, M., & Karras, M. (2022). “On a new additive arithmetic function related to a fixed integer.” *Notes on Number Theory and Discrete Mathematics* 28(3), 575–580. DOI: 10.7546/nntdm.2022.28.3.575-580. Online First: 2022-09-27.
