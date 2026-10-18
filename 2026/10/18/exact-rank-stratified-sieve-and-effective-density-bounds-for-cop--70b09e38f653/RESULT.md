# Exact rank-stratified sieve and effective density bounds for coprime associated Pell indices

## Finding
Let \(Q_0=Q_1=1\) and \(Q_{n+2}=2Q_{n+1}+Q_n\). For every odd prime \(p\), define \(h_p\) as the multiplicative order of \(-3-2z\) in \((\mathbb F_p[z]/(z^2-2))^\times\). This order divides \(p-(2/p)\), where \((2/p)\) is the Legendre symbol. If \(h_p\) is even put \(e_p=h_p/2\); otherwise leave \(e_p\) undefined. Then for every integer \(n\ge1\),
\[
\gcd(n,Q_n)=\prod_{\substack{p\mid n,\ p\text{ odd}\\ e_p\text{ defined},\ e_p\mid n,\ n/e_p\text{ odd}}}p^{\nu_p(n)}.
\]
In particular, \(\gcd(n,Q_n)\) is a unitary divisor of \(n\), and the requisite odd-quotient condition cannot be omitted.

The ordinary natural density \(\delta\) of \(\{n\ge1:\gcd(n,Q_n)=1\}\) has the following completely explicit rational approximations. For \(Y\ge17\), let \(\mathcal P_Y\) be the odd primes \(p\le Y\) with defined \(e_p\), and put
\[
\delta_Y=1+\sum_{\substack{\varnothing\ne T\subseteq\mathcal P_Y\\ \nu_2(e_p)\text{ is constant on }T}}
\frac{(-1)^{|T|}}{2\operatorname{lcm}_{p\in T}(p e_p)}.
\]
The limit \(\delta=\lim_{Y\to\infty}\delta_Y\) exists, and, with \(\alpha=1+\sqrt2\),
\[
0\le \delta_Y-\delta\le
\frac{1.25506\log\alpha}{2}
\left(\frac1{\log Y}+\frac1{2(\log Y)^2}\right).
\]
The resulting certified numerical interval is
\[
\boxed{0.812<\delta<0.878.}
\]
The exact eleven-event upper bound uses primes \(3,7,11,17,19,23,31,41,43,47,59\) and equals
\[
\delta_{59}=\frac{154703748840589}{176325122256360}<0.878.
\]
The lower bound uses the full prime sieve up to \(100000\), as detailed below.

## Assumptions and scope
All \(n\) are positive integers, all \(p\) are odd rational primes, and \(Y\ge17\) is real (the finite sieve depends only on primes at most \(Y\)). \(\nu_p\) denotes the usual prime-adic valuation, and \(\nu_2(e_p)\) the exponent of \(2\) in \(e_p\). Empty products are one. The ring \(\mathbb F_p[z]/(z^2-2)\) is a quadratic field for inert \(p\) and a product of fields for split \(p\); \(-3-2z\) is a unit in either case since its norm is one. Natural densities refer to increasing integer indices \(n\), not densities among primes. The reported interval is a certified bound, not an evaluation of \(\delta\) to a decimal precision.

## Proof
**Local order.** Let \(\alpha=1+\sqrt2\) and \(\beta=1-\sqrt2\), so \(\alpha\beta=-1\) and \(Q_n=(\alpha^n+\beta^n)/2\). In the quadratic residue algebra modulo odd \(p\), the ratio \(\alpha/\beta=-\alpha^2=-3-2\sqrt2\) has norm one. If \(2\) is a square modulo \(p\), its conjugate inverse condition implies its order divides \(p-1\); otherwise Frobenius conjugation implies the order divides \(p+1\). Hence \(h_p\mid p-(2/p)\). Since \(2\) is invertible, \(p\mid Q_n\) holds exactly when \((\alpha/\beta)^n=-1\). In a cyclic group, this equation has a solution precisely when \(h_p\) is even, and the solutions are \(n=e_p(2j+1)\), for integers \(j\ge0\). Moreover, \(e_p\le(p+1)/2<p\), so \(p\nmid e_p\).

**Valuations.** Work in the unramified quadratic \(p\)-adic algebra \(\mathbb Z_p[z]/(z^2-2)\), a product of unramified discrete valuation rings in the split case. If \(p\mid Q_{e_p}\), let \(A=\alpha^{e_p}\) and \(B=\beta^{e_p}\). Both are units and \(p\mid A+B\). The odd-exponent lifting-the-exponent identity, valid componentwise, gives \(\nu_p(A^m+B^m)=\nu_p(A+B)+\nu_p(m)\) for every positive odd \(m\). These sums are scalars \(2Q_{e_pm}\), so \(\nu_p(Q_{e_pm})=\nu_p(Q_{e_p})+\nu_p(m)\ge\nu_p(m)=\nu_p(e_pm)\). Outside those indices \(p\nmid Q_n\). Every \(Q_n\) is odd, so \(p=2\) never contributes to the gcd. Taking the minimum of valuations with \(n\) yields the claimed product.

**Finite exact density.** For each odd prime with defined \(e_p\), the obstruction \(p\mid\gcd(n,Q_n)\) is the progression \(E_p=\{p e_p(2j+1):j\ge0\}\); it has density \(1/(2pe_p)\). If a nonempty finite set \(T\) includes primes whose \(e_p\) have different \(2\)-adic valuations, its events have empty intersection. Otherwise, with \(L_T=\operatorname{lcm}_{p\in T}(p e_p)\), their intersection is exactly \(\{L_T(2j+1):j\ge0\}\) and has density \(1/(2L_T)\). Finite inclusion-exclusion therefore gives \(\delta_Y\) as displayed. It is nonincreasing as \(Y\) increases.

**Tail and existence.** Since \(Q_{e_p}\ge p\) and \(Q_{e_p}\le(\alpha^{e_p}+1)/2\), we have \(e_p\ge\log(2p-1)/\log\alpha>\log p/\log\alpha\). Thus
\[
\sum_{p>Y}\frac1{2p e_p}\le
\frac{\log\alpha}2\sum_{p>Y}\frac1{p\log p}.
\]
The classical Rosser--Schoenfeld bound \(\pi(t)<1.25506t/\log t\) for \(t\ge17\), followed by partial summation (discarding its nonpositive endpoint term), gives
\[
\sum_{p>Y}\frac1{p\log p}\le
1.25506\left(\frac1{\log Y}+\frac1{2(\log Y)^2}\right).
\]
The number \(n\le X\) belonging to any \(E_p\) with \(p>Y\) is at most \(X\sum_{Y<p\le X}1/(2pe_p)+\pi(X)\). Divide by \(X\), use \(\pi(X)/X\to0\), and let \(X\to\infty\). The finite-sieve densities sandwich the limsup and liminf of the untruncated coprime-index proportion, with their difference bounded by the displayed tail. This proves existence, the limit identity, and the effective error.

**Certified interval.** For the first eleven specified primes, exact subset inclusion-exclusion yields \(\delta_{59}=154703748840589/176325122256360<0.878\). For every odd prime \(p\le100000\) with defined \(e_p\), independently computed finite orders yield
\[
\sum_{\substack{p\le100000\\e_p\text{ defined}}}
\left\lceil\frac{10^{12}}{2pe_p}\right\rceil=137404000609.
\]
Hence \(\sum_{p\le100000}1/(2pe_p)\le0.137404000609\). The proved tail estimate at \(Y=100000\) is strictly below \(0.0502\) (using \(\log(1+\sqrt2)\)). The union bound consequently gives \(\delta\ge1-0.137404000609-0.0502>0.812\). Monotonicity gives \(\delta\le\delta_{59}<0.878\). This completes the proof.

## Verification
Run `python3 verify.py` from this package. It uses exact arithmetic to compute the quadratic-ring orders for every odd prime up to \(100000\), compares the computed first-divisibility ranks with the recurrence for the 167 odd primes below \(1000\), checks \(\gcd(n,Q_n)\) against the proved valuation criterion for all \(1\le n\le10000\) using matrix modular arithmetic, and recomputes the eleven-event exact rational sieve and the outward-rounded prime-event sum. All reported checks passed. These finite checks are not substituted for the proofs of the universal product and infinite density bound.

## Relationship to prior work
Mbirika, Schrader and Spilker (arXiv:2301.05758, first posted 2023-01-13) ask in Section 6.2 for arithmetic descriptions of \(\gcd(Q_n,n)\), and formulate an entry-point condition that does not impose oddness of the quotient. For example, \(e_3=2\) divides \(12\), while \(\gcd(Q_{12},12)=1\); the exact local condition includes oddness. Sanna (arXiv:1703.10478, 2017) proves existence and positivity of self-coprime-index density for general nondegenerate integer recurrences; these qualitative facts are prior work, not claimed new. Sanna and Tron (arXiv:1705.01805, 2017) give a Möbius/rank-density formula for Fibonacci indices and discuss extension to Lucas sequences of the first kind. Mastrostefano and Sanna (arXiv:1805.05114, 2018) extend general density existence to polynomial arguments. Unlike those statements, the present claim is a complete local valuation rule with the additional odd-index phase for this associated Pell sequence (a Lucas sequence of the second kind), an explicit parity-stratified finite-lcm density sieve with a numerical convergence bound, and a concrete certified interval. These are deductions using standard local tools; no broad priority or independence assertion is made.

## Limitations
The interval is relatively wide and does not determine the exact decimal value of the density. The computable order \(h_p\) requires arithmetic modulo each prime. The argument uses the published explicit prime-counting bound and a standard odd-exponent lifting lemma; verifying these externally is prerequisite to independent certification. The exact conditions and density sieve concern the specific recurrence stated, not arbitrary associated Lucas sequences. Overlap with unpublished or unindexed calculations remains possible.

## References
1. aBa Mbirika, Janee Schrader, Jürgen Spilker, *Pell and associated Pell braid sequences as GCDs of sums of k consecutive Pell, balancing, and related numbers*, arXiv:2301.05758 (first posted January 13, 2023), Section 6.2. https://arxiv.org/abs/2301.05758
2. Carlo Sanna, *On numbers n relatively prime to the nth term of a linear recurrence*, arXiv:1703.10478 (2017). https://arxiv.org/abs/1703.10478
3. Carlo Sanna and Emanuele Tron, *The density of numbers n having a prescribed G.C.D. with the nth Fibonacci number*, arXiv:1705.01805 (2017). https://arxiv.org/abs/1705.01805
4. Daniele Mastrostefano and Carlo Sanna, *On numbers n with polynomial image coprime with the nth term of a linear recurrence*, arXiv:1805.05114 (2018). https://arxiv.org/abs/1805.05114
5. J. Barkley Rosser and Lowell Schoenfeld, *Approximate formulas for some functions of prime numbers*, Illinois J. Math. 6 (1962), 64--94. https://doi.org/10.1215/ijm/1255631807
