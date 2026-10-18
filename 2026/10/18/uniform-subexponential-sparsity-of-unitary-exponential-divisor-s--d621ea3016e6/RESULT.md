# Uniform subexponential sparsity of unitary–exponential divisor-sum ratio fibers

## Finding
Write \(\sigma^*(n)\) for the sum of unitary divisors of the positive integer \(n\), and \(\sigma^{(e)}(n)\) for the sum of exponential divisors. For every real \(c>0\) and \(X\ge1\), let
\[
N_c(X)=\#\{1\le n\le X:\sigma^*(n)/\sigma^{(e)}(n)=c\}.
\]
Then, as \(X\to\infty\), **uniformly in \(c>0\)**,
\[
\boxed{\sup_{c>0}N_c(X)\le X\exp\left[-\left(\frac1{\sqrt2}+o(1)\right)\sqrt{\log X\,\log\log X}\right].}
\]
Consequently, the equality \(\sigma^*(n)=\sigma^{(e)}(n)\) holds for a quantitatively sparse set of integers.

## Assumptions and scope
All logarithms are natural. An exponential divisor of \(p^a\) has the form \(p^d\) with \(d\mid a\); a unitary divisor of a prime power is either \(1\) or the prime power itself. Both divisor sums are positive and multiplicative. In particular,
\[
\sigma^*(p)=p+1,\quad\sigma^{(e)}(p)=p,
\quad\sigma^*(p^a)=1+p^a,\quad\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d.
\]
The theorem is asymptotic, covers *every* positive real level \(c\), and does not assume that \(c\) is rational. Define \(P(n)\) as the largest prime divisor of \(n\) when \(n>1\), and \(P(1)=1\). Let \(\Psi(X,y)=\#\{n\le X:P(n)\le y\}\).

## Proof
**Large-prime injection.** Fix \(X\ge3\), \(y\ge2\), and any \(c>0\). Partition integers counted by \(N_c(X)\) into those with \(P(n)\le y\), those divisible by the square of a prime greater than \(y\), and the remaining integers. The first group has at most \(\Psi(X,y)\) elements; the second has at most
\[
\sum_{p>y}\left\lfloor\frac{X}{p^2}\right\rfloor
\le X\sum_{k>y}k^{-2}=O(X/y).
\]
For a remaining integer write \(n=pm\), where \(p=P(n)>y\) occurs to exponent exactly one, hence \(p\nmid m\), and \(1\le m<X/y\). Multiplicativity gives
\[
\frac{(p+1)\sigma^*(m)}{p\sigma^{(e)}(m)}=c,
\qquad p\big(c\sigma^{(e)}(m)-\sigma^*(m)\big)=\sigma^*(m).
\]
Since \(\sigma^*(m)>0\), this equation has at most **one** positive \(p\) for each fixed \(m\), even before imposing primality. Therefore, uniformly in \(c\),
\[
N_c(X)\le\Psi(X,y)+O(X/y),\tag{1}
\]
with an absolute implicit constant.

**Smooth-number estimate.** Put \(L=\log X\), \(V=\log L\), and choose
\[
y=\exp\!\left(\frac1{\sqrt2}\sqrt{LV}\right),
\qquad u=\frac{L}{\log y}=\sqrt{\frac{2L}{V}}.
\]
For sufficiently large \(X\), define
\[
\delta=\frac{\log u-2\log\log u}{\log y}>0,
\qquad s=1-\delta>3/4.
\]
Rankin's elementary inequality (applied to the positive Euler product) yields
\[
\Psi(X,y)\le X^s\prod_{p\le y}(1-p^{-s})^{-1}.
\]
The bound \(\sum_{p\le y}p^{-1}=O(\log\log y)\), together with \(y^\delta=u/(\log u)^2\), implies
\[
\sum_{p\le y}p^{-s}\le y^\delta\sum_{p\le y}p^{-1}
=O\left(\frac{u\log\log y}{(\log u)^2}\right).
\]
Since \(s>3/4\), all prime-power contributions of exponent at least two to the logarithm of the Euler product sum to \(O(1)\). Hence
\[
\log\Psi(X,y)\le L-u(\log u-2\log\log u)
+O\left(1+\frac{u\log\log y}{(\log u)^2}\right).
\]
Here \(\log u=(\tfrac12+o(1))V\), \(\log\log y=O(V)\), and
\[
u(\log u-2\log\log u)
=\left(\frac1{\sqrt2}+o(1)\right)\sqrt{LV},
\]
while the preceding error is \(o(\sqrt{LV})\). Therefore
\[
\Psi(X,y)\le X\exp\left[-\left(\frac1{\sqrt2}+o(1)\right)\sqrt{LV}\right].
\]
The other term in (1) satisfies \(X/y=X\exp(-\sqrt{LV}/\sqrt2)\). Combining these estimates proves the asserted uniform bound. The finitely many small \(X\) are irrelevant to this asymptotic claim.

## Verification
Run `python verify.py` with Python 3. It independently evaluates both divisor sums for all integers through \(100000\); for four prime thresholds, it checks the factorization identities and that the large-prime inversion recovers each prime exactly. It also compares the earliest equality solutions with the published table. The symbolic Euler-product argument, not these finite checks, establishes the infinite estimate.

## Relationship to prior work
Tim Trudgian's 2013 preprint *The sum of the unitary divisor function* (published 2015) compares the two divisor sums and asks whether equality occurs for infinitely many integers, recording the initial examples and invoking Erdős–Wintner for the existence of a density for the strict inequality. It does not provide this quantitative **uniform level-set** upper bound. OEIS A236474 lists equality solutions without asserting a uniform asymptotic estimate. Two later published studies on a finite-exponent equality classification and a density lower bound for the strict inequality likewise do not imply the uniform estimate here. The injection and Rankin method uses standard ingredients, but their combination yields the stated quantitative conclusion for these divisor-sum ratios.

## Limitations
The result does not prove finiteness or infinitude of any level set, or determine the true sharp rate. The coefficient \(1/\sqrt2\) is a proven exponent in this upper bound, not a claimed optimal constant. The standard Mertens prime-reciprocal bound is used without supplying an independent proof. Previously unindexed applications of the same large-prime injection principle remain an originality risk.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1, first posted 2013-12-17; *Publications de l'Institut Mathématique* 97(111) (2015), 175–180. DOI: 10.2298/PIM140617001T.
2. OEIS A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*, https://oeis.org/A236474 (initial entry 2014-01-29).
3. *The first 49 exponent layers of the unitary–exponential divisor-sum equality*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-first-49-exponent-layers-of-the-unitary-exponential-divisor--59314f8e910e (comparison of statements).
4. *An explicit lower bound for the unitary–exponential divisor-sum comparison density*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-an-explicit-0-753659844-ldots-lower-bound-for-the-unitary-expone--831dd476bf82 (comparison of statements).
