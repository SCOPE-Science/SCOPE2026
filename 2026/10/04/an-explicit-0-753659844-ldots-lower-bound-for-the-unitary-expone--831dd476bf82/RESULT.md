# An explicit \(0.753659844\ldots\) lower bound for the unitary--exponential divisor-sum comparison density
## Finding
Let \(\sigma^*(n)\) denote the sum of unitary divisors of \(n\), and let \(\sigma^{(e)}(n)\) denote the sum of exponential divisors. If
\[
\delta=\lim_{x\to\infty}\frac{1}{x}\#\{n\le x:\sigma^*(n)>\sigma^{(e)}(n)\},
\]
then
\[
\delta\ge \frac{6097572635664749695003}{819750822146736480000\,\pi^2}=0.753659844064288\ldots.
\]
This improves the square-free lower bound \(6/\pi^2=0.607927101854027\ldots\) recorded in the source that posed the density question.

## Assumptions and scope
For a prime \(p\) and integer \(a\ge1\), multiplicativity gives
\[
\sigma^*(p^a)=1+p^a,\qquad \sigma^{(e)}(p^a)=\sum_{d\mid a}p^d.
\]
Put \(\rho_p(0)=1\) and, for \(a\ge1\),
\[
\rho_p(a)=\frac{1+p^a}{\sum_{d\mid a}p^d}.
\]
The finite prime set is \(P=\{2,3,5,7,11,13\}\), and only exponents \(0\le a_p\le5\) are used on \(P\). Every prime \(q\ge17\) is restricted to exponent \(0\) or \(1\). No assertion is made that this finite cylinder choice is optimal or that the displayed lower bound is the exact density.

## Proof
For an exponent vector \(\mathbf a=(a_p)_{p\in P}\in\{0,1,2,3,4,5\}^6\), set
\[
R(\mathbf a)=\prod_{p\in P}\rho_p(a_p).
\]
Let \(G\) be the vectors for which \(R(\mathbf a)\ge1\). Consider integers \(n\) satisfying \(v_p(n)=a_p\) for one \(\mathbf a\in G\), and \(v_q(n)\in\{0,1\}\) for every prime \(q\ge17\). For a tail prime with exponent one,
\[
\rho_q(1)=\frac{q+1}{q}>1.
\]
Hence \(\sigma^*(n)/\sigma^{(e)}(n)>1\) whenever \(R(\mathbf a)>1\), and also whenever \(R(\mathbf a)=1\) and at least one tail prime divides \(n\). The exact enumeration finds only five vectors with \(R(\mathbf a)=1\); if the tail is empty they yield only five individual integers. Removing finitely many integers does not change density.

For a fixed \(\mathbf a\), the density of integers having those exact valuations on \(P\) and square-free tail is
\[
\left(\prod_{p\in P}\frac{p-1}{p^{a_p+1}}\right)
\left(\prod_{q\ge17}\left(1-\frac1{q^2}\right)\right).
\]
The cylinders are disjoint, so their densities add. Exact rational enumeration over all \(6^6=46656\) vectors gives \(17230\) vectors in \(G\). Writing
\[
W=\sum_{\mathbf a\in G}\prod_{p\in P}\frac{p-1}{p^{a_p+1}},
\]
and using
\[
\prod_{q\ge17}\left(1-\frac1{q^2}\right)
=\frac{6/\pi^2}{\prod_{p\in P}(1-p^{-2})},
\]
the exact finite calculation yields
\[
\frac{6W}{\prod_{p\in P}(1-p^{-2})}
=\frac{6097572635664749695003}{819750822146736480000}.
\]
Therefore the density of this explicit subset is the displayed constant divided by \(\pi^2\), proving the lower bound.

## Verification
The standalone script `verify_density.py` uses only Python integer arithmetic and `fractions.Fraction`. It enumerates all \(46656\) exponent vectors, recomputes every local ratio from the divisor set of the exponent, checks the five equality vectors, and verifies the exact rational coefficient. A fresh replay produced:

`VERIFY_OK`

`patterns_total=46656 good_patterns=17230 equality_patterns=5`

`coefficient=6097572635664749695003/819750822146736480000`

`lower_bound=0.753659844064288`

The computation is finite and exact. The infinite-density step is the symbolic Euler-product calculation above, not an extrapolation from sampled integers.

## Relationship to prior work
Trudgian's paper defines the two multiplicative divisor sums, observes that every square-free integer satisfies \(\sigma^*(n)>\sigma^{(e)}(n)\), asks for the proportion of such integers, records the rigorous lower bound \(6/\pi^2\), and reports an empirical proportion about \(0.778307\) through \(10^9\). The present result does not determine the density; it supplies a substantially stronger explicit rigorous lower bound by admitting many nonsquarefree exponent patterns. General Euler-product formulas for prescribed exponent sets are standard; the claim here is the comparison-specific finite cylinder selection and its resulting bound.

## Limitations
The prime set \(P\), exponent cutoff \(5\), and the requirement that all larger-prime exponents be at most one are deliberately finite sufficient conditions. Patterns outside these cylinders can also satisfy the comparison, so the constant is not claimed optimal. Searches did not locate a published stronger or equivalent explicit lower bound, but an unindexed later treatment remains a residual originality risk. The argument proves only a lower bound, not the exact value suggested by computation.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1, first public 2013-12-17; Publ. Inst. Math. (Beograd) 97 (111), 175--180; DOI 10.2298/PIM140617001T.
2. OEIS A209061, comments and references on densities of integers defined by prescribed prime-exponent sets; used only as background for the standard Euler-product density mechanism.
