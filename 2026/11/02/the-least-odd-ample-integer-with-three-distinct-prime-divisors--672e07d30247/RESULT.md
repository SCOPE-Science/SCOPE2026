# The least odd ample integer with three distinct prime divisors

## Finding
Let the recursive divisor function be \(\kappa(1)=1\) and, for each integer \(n>1\),
\[
\kappa(n)=1+\sum_{\substack{d\mid n\\d<n}}\kappa(d).
\]
Call an integer *ample* if \(\kappa(n)>n\). Then the unique least odd ample integer with exactly three distinct prime factors is
\[
\boxed{N=3^{20}5^9 7^6=801204488268064453125}.
\]
Its exact recursive-divisor count is
\[
\kappa(N)=841632661765951062016>N.
\]
Moreover, odd ample numbers cannot have fewer than three distinct prime divisors. Thus \(N\) is the least odd ample integer on the **smallest possible number of prime supports**. The difference \(\kappa(N)-N\) is \(40428173497886608891\).

## Assumptions and scope
The integer \(n\) is positive and odd, and \(\omega(n)\) is its number of distinct prime divisors. No constraints on prime exponents are imposed. The theorem identifies the minimum of \(\{n\text{ odd}:\kappa(n)>n,\ \omega(n)=3\}\), proves uniqueness at the minimum, and separately excludes odd ample numbers of support cardinality at most two. It does **not** assert that \(N\) is the least odd ample integer without the prime-support constraint.

For prime powers, the value of \(\kappa\) depends only on the exponent vector, not on the underlying primes. Write
\[
K_{a,b,c}=\kappa(p^a q^b r^c),\qquad a,b,c\ge0,
\]
for any three distinct primes \(p,q,r\). The notation includes zeros solely to formulate recurrences; the target three-prime-support class has \(a,b,c\ge1\).

## Proof
**1. Prime-exponent reduction.** The interval of divisors of \(p^a q^b r^c\) is naturally indexed by \((i,j,h)\) with \(0\le i\le a\), \(0\le j\le b\), and \(0\le h\le c\). Its proper-divisor recursion therefore gives
\[
K_{0,0,0}=1,\qquad
K_{a,b,c}=1+\sum_{\substack{0\le i\le a,\,0\le j\le b,\,0\le h\le c\\(i,j,h)\ne(a,b,c)}}K_{i,j,h}
\]
for all other triples. Thus \(K_{a,b,c}\) is independent of the distinct primes chosen.

If \(n=p^a q^b r^c\) is odd with \(3\le p<q<r\) prime and all three exponents positive, then \(p\ge3\), \(q\ge5\), \(r\ge7\), so
\[
3^a5^b7^c\le n,\qquad \kappa(n)=K_{a,b,c}.
\]
Consequently, if \(n<N\) is ample, the smaller canonical representative \(m=3^a5^b7^c<N\) must also be ample (because \(K_{a,b,c}>n\ge m\)). We may therefore seek the global minimum entirely among canonical triples.

**2. An exact recurrence.** The formal generating series of the exponent-indexed values is
\[
\mathcal K(x,y,z)=\sum_{a,b,c\ge0}K_{a,b,c}x^ay^bz^c
=\frac{1}{2(1-x)(1-y)(1-z)-1}.
\]
Indeed, at each nonnegative exponent triple the proper-divisor recursion rearranges to twice \(K_{a,b,c}\) minus its full three-dimensional prefix sum being equal to one. Summing these identities as formal power series gives \(2\mathcal K=1/((1-x)(1-y)(1-z))+\mathcal K/((1-x)(1-y)(1-z))\), hence the displayed rational function. Multiplication by the denominator and coefficient comparison yields, for all nonzero exponent triples,
\[
\begin{aligned}
K_{a,b,c}={}&2(K_{a-1,b,c}+K_{a,b-1,c}+K_{a,b,c-1})\\
&-2(K_{a-1,b-1,c}+K_{a-1,b,c-1}+K_{a,b-1,c-1})\\
&+2K_{a-1,b-1,c-1}.
\end{aligned}
\]
All negative-index terms are zero, and \(K_{0,0,0}=1\). Hence each required value is an exact integer obtained without factoring large numbers.

**3. Finite exhaustive cutoff.** Put \(N=801204488268064453125\). Every positive exponent triple with \(3^a5^b7^c\le N\) lies in
\[
1\le a\le43,\qquad1\le b\le29,\qquad1\le c\le24,
\]
because \(3^{44}>N\), \(5^{30}>N\), and \(7^{25}>N\). To avoid relying on unchecked tabulated entries, the supplied standard-library Python verifier (`verify.py`) constructs **every** value in the enclosing integer box, cross-checking the seven-neighbor recurrence against the original proper-divisor formula via independently maintained three-dimensional prefix sums. It enumerates and records all and only the triples in the product cutoff, computes the exact integers and their \(\kappa\)-values, and asserts
\[
\begin{gathered}
\#\{(a,b,c)\ge(1,1,1):3^a5^b7^c\le N\}=4650,\\
\#\{(a,b,c)\ge(1,1,1):3^a5^b7^c<N\}=4649,\\
K_{a,b,c}\le3^a5^b7^c\quad\text{for each of those 4649 triples}.
\end{gathered}
\]
At the single remaining candidate the program establishes the exact equality
\[
(a,b,c)=(20,9,6),\quad 3^a5^b7^c=N,\quad
K_{a,b,c}=841632661765951062016.
\]
These assertions implement a rigorous exhaustive finite certificate once `verify.py` is executed as provided; no tested prefix is substituted for the infinite theorem. Because every hypothetically smaller odd three-support ample number maps to a strictly smaller canonical representative, the finite certificate proves the theorem for *all* odd three-support integers.

**4. Minimal support is three.** For an odd number with at most two distinct prime factors, the usual divisor sum satisfies
\[
\frac{\sigma(n)}n\le\prod_{p\mid n}\frac{p}{p-1}
\le\frac32\frac54=\frac{15}{8}<2.
\]
Thus \(n\) is deficient. Every proper divisor of a deficient integer is also deficient, as \(\sigma(d)/d\le\sigma(n)/n\) for \(d\mid n\). Induction over deficient integers yields \(\kappa(d)\le d\) for all of them: the induction step gives
\[
\kappa(d)\le1+\sum_{\substack{e\mid d\\e<d}}e
=1+\sigma(d)-d\le d.
\]
Hence no deficient integer is ample. Since \(N\) is odd, ample, and supported on three primes, this support cardinality is minimal.

**5. Uniqueness.** Any odd three-prime-support integer equal to \(N\) must have exponent profile among the product-cutoff triples. The only canonical candidate at the threshold is \((20,9,6)\). If its actual primes exceed \((3,5,7)\) in any coordinate, their product is strictly greater than \(N\). Therefore equality holds only for \(N=3^{20}5^9 7^6\).

## Verification
Run `python3 verify.py` using Python 3 standard library only. The checker derives the cutoff exponent bounds directly from powers, compares each entry of the computed three-dimensional table with a distinct direct proper-divisor calculation, checks 343 small divisor-lattice values by a third independent recurrence, and verifies seven values using the binomial closed form published by Fink. It then asserts the complete finite cutoff, unique minimum and exact recursive-divisor count.

Expected terminal marker: `VERIFY_OK`. Expected exact scope: `all_triples_checked=4650`, `strictly_smaller_triples_checked=4649`, `independent_direct_divisor_cases=343`, `independent_closed_formula_cases=7`. The SHA-256 digest of the ordered cutoff census lines is `529cb672da45e752463f3b8e33cb90d47124aef11b6dd0296f752b4f7b449a96` (as generated by the checker). The mathematical reduction to this exhaustive finite census is proved in the preceding section, not assumed from observations.

## Relationship to prior work
Fink's 2020 paper introduces ample integers, proves that deficient integers are not ample, gives prime-exponent closed formulas, and exhibits rare odd ample examples. Fink's 2023 paper derives a Dirichlet series and general convolution identities for the recursive divisor function. Those theorems and formulas are used and credited here; they do not state this exact three-prime-support minimum.

A later published treatment, *Finite abundant prime supports force ample numbers* (2026), proves existence of infinitely many ample integers supported on any finite prime set whose Euler product exceeds two. Since \((3/2)(5/4)(7/6)>2\), that existence theorem covers the support \(\{3,5,7\}\), but explicitly does not give an effective bound on the least such integer. The present theorem is an **exact least-witness and uniqueness determination**, not a new existence theorem. A hidden equivalent table or unindexed earlier exhaustive census remains possible; bibliography searches alone cannot certify absolute priority.

## Limitations
Only the least odd ample integer among three-prime-support numbers, and minimality of three supports, is determined. The theorem does not classify all three-support ample integers, determine the smallest ample integer avoiding any larger set of primes, or settle independent least-witness questions in other restricted supports. The numerical claims depend on executing the supplied exact finite verifier; isolated output logs are not a substitute for its mathematics and code.

## References
1. Thomas Fink, “Recursively abundant and recursively perfect numbers,” arXiv:2008.10398v1, first publicly posted 24 August 2020; https://arxiv.org/abs/2008.10398 .
2. T. M. A. Fink, “Properties of the recursive divisor function and the number of ordered factorizations,” arXiv:2307.09140v1, first publicly posted 18 July 2023; https://arxiv.org/abs/2307.09140 .
3. “Finite abundant prime supports force ample numbers,” public mathematical record, October 2026; https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-finite-abundant-prime-supports-force-ample-numbers--3a5bff12f682 .
