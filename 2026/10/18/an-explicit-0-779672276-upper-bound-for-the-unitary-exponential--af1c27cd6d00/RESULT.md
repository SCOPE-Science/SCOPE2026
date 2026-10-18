# An explicit \(0.779672276\) upper bound for the unitary–exponential divisor-sum comparison density

## Finding
Let \(\sigma^*(n)\) be the sum of unitary divisors and \(\sigma^{(e)}(n)\) the sum of exponential divisors of the positive integer \(n\). The natural density \(\delta\), if it exists, of positive integers satisfying \(\sigma^*(n)>\sigma^{(e)}(n)\) satisfies the rigorous bound
\[
\boxed{\delta<\frac{194918069}{250000000}=0.779672276<0.78.}
\]
The same inequality holds with \(\delta\) replaced by the upper asymptotic density, without requiring density existence. In conjunction with the previously published lower bound \(0.753659844\ldots\), it gives a rigorous two-sided interval for the unresolved density problem.

## Assumptions and scope
For every prime \(p\), set \(\rho_p(0)=1\), and for every integer \(a\ge1\) define
\[
\rho_p(a)=\frac{1+p^a}{\sum_{d\mid a}p^d}.
\]
Multiplicativity gives \(\sigma^*(n)/\sigma^{(e)}(n)=\prod_p\rho_p(v_p(n))\). At exponent one, \(\rho_p(1)=1+1/p\); for every exponent at least two, \(\rho_p(a)<1\), since the denominator contains the distinct terms \(p\) and \(p^a\).

The finite local prime cutoff is \(B=5003\). The exponent caps are \(12,10,6,5,4,3,3,3,3\) for \(p=2,3,5,7,11,13,17,19,23\), respectively, and \(2\) for each prime \(29\le p\le5003\). Only these exponents are included in the finite cylinder certificate; all other integers remain unrestricted in the theorem's domain.

## Proof
**Finite cylinder.** Put \(b=1001/1000\). For each prime \(p\le5003\) and exponent \(0\le a\le A_p\) within its cap, let \(k_p(a)\) be the *smallest integer* satisfying \(\rho_p(a)\le b^{k_p(a)}\). This integer is computable by cross-multiplication; no numerical logarithm is required for certification. Let \(E\) be the periodic set of positive integers whose exponents at primes up to \(5003\) are all within the caps and satisfy
\[
\sum_{p\le5003}k_p(v_p(n))\le-2.
\]
Then the local part of the divisor-sum ratio obeys
\[
\prod_{p\le5003}\rho_p(v_p(n))\le b^{-2}.
\]
For each allowed exponent \(a\), exactly \((p-1)p^{A_p-a}\) residue classes modulo \(p^{A_p+1}\) have valuation \(a\). Thus, defining \(M=\prod_{p\le5003}p^{A_p+1}\), a finite weighted dynamic program computes the exact density \(\mathop{\rm dens}(E)=G/M\). Start with \(D_0(0)=1\) and update for the successive primes via
\[
D_i(s)=\sum_{a=0}^{A_{p_i}}(p_i-1)p_i^{A_{p_i}-a}D_{i-1}(s-k_{p_i}(a)),
\qquad G=\sum_{s\le-2}D_{670}(s).
\]
An integer-only certificate recomputes all scores and coefficients and checks the strict inequality
\[
\boxed{G/M>11023/50000=0.22046.}
\]
The finite calculation has \(670\) primes and \(4216\) nonzero score states, yielding \(G/M=0.22046662690260477\ldots\). The displayed decimal is informational; acceptance uses the exact integer comparison.

**Prime tail.** For all positive integers \(n\), the log of the remaining ratio satisfies
\[
\sum_{p>5003}\log\rho_p(v_p(n))\le X(n),\qquad
X(n)=\sum_{p>5003,\,p\mid n}\frac1p,
\]
because \(\log(1+1/p)\le1/p\), while exponents at least two contribute negatively. The finite-prime divisibility events have the independent Bernoulli limits \(\Pr(p\mid n)=1/p\) by the Chinese remainder theorem. The convergent expected tail \(\sum_{p>5003}p^{-2}\) makes the corresponding infinite Bernoulli series an asymptotically valid tail distribution, independent of the fixed event \(E\). Its mean and variance are
\[
\mu=\sum_{p>5003}\frac1{p^2},\qquad
V=\sum_{p>5003}\frac1{p^3}\left(1-\frac1p\right).
\]
This limiting-distribution assertion may also be justified directly by approximating with finitely many tail primes. The unconditional average contribution from primes above a further cutoff \(N\) is at most \(\sum_{m>N}m^{-2}\), uniformly in the averaging limit. Restricting to the periodic event \(E\) costs at most the fixed factor \(1/\mathop{\rm dens}(E)\) in this tail estimate. Thus CRT independence for fixed prime sets passes to the full infinite tail.

Using the exact sieve of primes from \(5004\) through \(100000\), the ceiling-sum certificate gives
\[
\begin{aligned}
\mu&\le\frac{20243665461}{10^{15}}+\frac1{100000}<\frac{31}{10^6},\\
V&\le\frac{2200010}{10^{15}}+\frac1{2(100000)^2}<\frac{23}{10^{10}}.
\end{aligned}
\]
Here the terms past \(100000\) are bounded by the respective integrals of \(t^{-2}\) and \(t^{-3}\); the finite ceiling sums bound the exact rational prime sums from above. With \(T=2\log b>2/1001\), the one-sided Chebyshev inequality yields
\[
\Pr(X\ge T)\le\frac{V}{(T-\mu)^2}
<\frac{23/10^{10}}{(2/1001-31/10^6)^2}
<\frac3{5000}.
\]

**Comparison.** On \(E\cap\{X<T\}\), the logarithm of the full divisor-sum ratio is less than \(-2\log b+T=0\), and hence \(\sigma^*(n)<\sigma^{(e)}(n)\). Independence in the limiting prime-valuation model, together with the finite-cutoff approximation just described, gives lower asymptotic density of this deficient subset at least
\[
\frac{11023}{50000}\left(1-\frac3{5000}\right)
=\frac{55081931}{250000000}>\frac{11}{50}.
\]
Both inequalities entering this display are in fact strict. Therefore the upper density of the complementary strict comparison is less than \(194918069/250000000\), completing the proof.

## Verification
The self-contained Python 3 file `verify_upper_density.py` performs the finite certificate with exact integer weights, exact fraction bounds, and exact cross-multiplication for all discretized logarithms. It uses only Python's standard library and has no external dependencies. The executed certificate reported:

```
VERIFY_OK
small_primes=670 states=4216 cylinder_mass=0.220466626903
tail_primes=8922 ceil_second=20243665461 ceil_third=2200010
chebyshev_risk_bound=0.000594453973
deficiency_lower=55081931/250000000 > 11/50
finite_implication_cases=6595
CONCLUSION: upper_density_sigma_star_gt_sigma_e < 39/50
```

The last independent finite regression examines all integers \(2\le n\le30000\) and verifies the sufficient inequality whenever the local and tail certificates hold. Only the exact finite residue calculation and the infinite mathematical argument establish the density result; the regression is not an infinite proof.

## Relationship to prior work
Trudgian (2013) posed the density question, proved results for \(\sigma^*\), recorded the squarefree lower bound \(6/\pi^2\), and noted numerical proportions near \(0.778307\). The published published-finding corpus finding *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density* supplies a stronger lower bound using favorable local valuation cylinders but does not establish an upper bound. OEIS A322446 lists finite counts through powers of ten and a numerical limiting estimate; these counts do not imply a certified universal upper density bound. The present result gives a quantitative **upper** bound by certifying a positive-density class of deficient integers and rigorously controlling compensation by all other primes. In particular, the source's lower-bound cylinders alone cannot imply the new inequality.

## Limitations
The result bounds, but does not determine, the exact comparison density. The finite exponent caps and \(5003\)-prime cutoff are sufficient certificates rather than claimed optimal choices. The upper bound leaves a gap of about \(0.026\) above the previous rigorous lower bound; the observed numerical density is not itself certified as a limit by the enumeration. No claim about the infinitude of equality cases is made. A later unindexed proof of a stronger upper bound remains a literature-priority risk.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1 (first public 2013-12-17); *Publications de l'Institut Mathématique* 97 (2015), 175–180, DOI 10.2298/PIM140617001T.
2. *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density*, published-finding corpus (published 2026-10-04), full RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-an-explicit-0-753659844-ldots-lower-bound-for-the-unitary-expone--831dd476bf82.
3. OEIS A322446, *The number of solutions to usigma(k) > esigma(k) below powers of ten*, https://oeis.org/A322446.
