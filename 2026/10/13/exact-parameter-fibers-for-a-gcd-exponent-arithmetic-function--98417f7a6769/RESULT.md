# Exact parameter fibers for a gcd-exponent arithmetic function
## Finding
Fix an integer \(n=\prod_{i=1}^r p_i^{e_i}>1\), put \(L=\operatorname{lcm}(e_1,\ldots,e_r)\), and for every positive integer \(\alpha\) define \(f_\alpha(n)=\prod_{i=1}^r p_i^{\gcd(e_i,\alpha)}\). Then for all positive integers \(\alpha,\beta\), \(f_\alpha(n)=f_\beta(n)\) if and only if \(\gcd(\alpha,L)=\gcd(\beta,L)\). Consequently the map \(\alpha\mapsto f_\alpha(n)\) has exact least positive period \(L\), its orbit has exactly \(\tau(L)\) values, namely \(\{f_d(n):d\mid L\}\), and in every complete block \(1\le\alpha\le L\) the value \(f_d(n)\) occurs exactly \(\varphi(L/d)\) times for each divisor \(d\mid L\).

## Assumptions and scope
Write the fixed integer as \(n=\prod_{i=1}^r p_i^{e_i}>1\), where the \(p_i\) are distinct primes and the \(e_i\) are positive integers. Let
\[
L=\operatorname{lcm}(e_1,\ldots,e_r).
\]
For every positive integer \(\alpha\), use the Mittou--Derbal function
\[
f_\alpha(n)=\prod_{i=1}^r p_i^{\gcd(e_i,\alpha)}.
\]
Here \(\tau\) is the divisor-counting function and \(\varphi\) is Euler's totient. The parameter \(\alpha\) is restricted to positive integers, matching the original definition.

## Proof
Unique factorization gives
\[
f_\alpha(n)=f_\beta(n)
\quad\Longleftrightarrow\quad
\gcd(e_i,\alpha)=\gcd(e_i,\beta)\quad(1\le i\le r).
\]
Because every \(e_i\) divides \(L\),
\[
\gcd(e_i,\alpha)=\gcd(e_i,\gcd(\alpha,L)).
\]
Hence equality of \(\gcd(\alpha,L)\) and \(\gcd(\beta,L)\) is sufficient.

For the converse, take the least common multiple of the coordinate gcds. Prime by prime,
\[
\nu_q\!\left(\operatorname{lcm}_i\gcd(e_i,\alpha)\right)
=\max_i\min\{\nu_q(e_i),\nu_q(\alpha)\}
=\min\{\nu_q(L),\nu_q(\alpha)\},
\]
so
\[
\operatorname{lcm}_i\gcd(e_i,\alpha)=\gcd(L,\alpha).
\]
Thus equality of all coordinate gcds forces
\[
\gcd(L,\alpha)=\gcd(L,\beta).
\]
This proves the fiber equivalence.

Each divisor \(d\mid L\) is attained by the parameter \(\alpha=d\), so the distinct fibers are indexed exactly by the divisors of \(L\). Therefore the orbit has \(\tau(L)\) values and is
\[
\{f_d(n):d\mid L\}.
\]
Within \(1\le\alpha\le L\), the condition \(\gcd(\alpha,L)=d\) is equivalent to
\[
\gcd(\alpha/d,L/d)=1,
\]
so its multiplicity is exactly \(\varphi(L/d)\).

Finally, the original source proves that \(L\) is a period. If \(T>0\) is any period, compare the parameters \(L\) and \(L+T\). The fiber equivalence gives
\[
L=\gcd(L,L)=\gcd(L,L+T)=\gcd(L,T),
\]
hence \(L\mid T\). Thus \(L\) is the least positive period.

## Verification
The standalone verifier exhausts every exponent tuple of support size at most four with each exponent between \(1\) and \(5\). For each tuple it checks the fiber equivalence throughout one complete period, the divisor-indexed orbit, the multiplicity formula, and the least-period assertion. Its output is:

`VERIFY_OK exponent_tuples=780 parameter_pairs=479656 max_exponent=5 max_support=4`

This is finite regression evidence only. The proof above is symbolic and has no exponent, support, or parameter cutoff.

## Relationship to prior work
Mittou and Derbal introduced \(f_\alpha\), proved the composition identity
\[
f_\alpha(f_\beta(n))=f_{\gcd(\alpha,\beta)}(n),
\]
proved that \(L=\operatorname{lcm}(e_1,\ldots,e_r)\) is a period in the parameter, and gave a sufficient condition for two parameters to produce the same value. Their statements do not identify all parameter fibers or prove that the displayed period is least.

Mittou's 2022 follow-up again uses the same \(L\)-periodicity while studying multiplicativity and divisibility-sequence properties; it does not state an exact fiber classification or least-period theorem. A 2025 follow-up defines the orbit \(O_n=\{f_\alpha(n)\}\), proves \(O_n\) lies in the set of exponential divisors, and classifies when equality with the full exponential-divisor set occurs. That result is complementary: the theorem here gives the exact cardinality, parameter fibers, and within-period multiplicities of \(O_n\) for every fixed \(n\).

## Limitations
The result concerns the gcd-exponent function \(f_\alpha\) at one fixed positive integer and positive parameters. It does not address the lcm-exponent companion function or classify relations between different base integers. The first-public-date field uses the earliest exact public full-text date verified for the focal 2021 paper, an author-upload date of 2021-04-06; the journal issue itself is identified only at month-level in the consulted metadata.

## References
1. B. Mittou and A. Derbal, “On new arithmetic function relative to a fixed positive integer. Part 1,” *Notes on Number Theory and Discrete Mathematics* 27(1) (2021), 22–26. DOI: 10.7546/nntdm.2021.27.1.22-26.
2. B. Mittou, “New properties of an arithmetic function,” *Mathematica Montisnigri* 53 (2022), 5–11. DOI: 10.20948/mathmontis-2022-53-1.
3. B. Mittou, “New properties of arithmetic functions related to gcd and lcm,” *Notes on Number Theory and Discrete Mathematics* 31(1) (2025), 91–97. DOI: 10.7546/nntdm.2025.31.1.91-97.
