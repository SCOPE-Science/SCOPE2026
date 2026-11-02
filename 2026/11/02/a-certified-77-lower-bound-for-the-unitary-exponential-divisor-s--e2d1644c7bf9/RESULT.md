# A certified \(77\%\) lower bound for the unitary–exponential divisor-sum comparison density
## Finding
For every positive integer \(n\), let \(\sigma^*(n)\) be its sum of unitary divisors, and \(\sigma^{(e)}(n)\) the sum of its exponential divisors. Define
\[
\delta=\lim_{x\to\infty}\frac{1}{x}\#\{1\le n\le x:\sigma^*(n)>\sigma^{(e)}(n)\}.
\]
The existence of this natural density follows from the limiting-distribution argument reported in the foundational literature. This note proves the explicit bound
\[
\boxed{\delta\ge
\frac{12117705984441349391635228560689}
{1593139205846841220399104000000\,\pi^2}
=0.770667314486686\ldots>\frac{77}{100}.}
\]
It improves the previously recorded explicit lower bound \(0.753659844064288\ldots\) and brings the rigorous lower bound within \(0.0077\) of the empirical proportion \(0.778307\) reported through one billion integers. It does not determine the true density.

## Assumptions and scope
If \(p\) is prime and \(a\ge1\), then
\[
\sigma^*(p^a)=1+p^a,\qquad
\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d.
\]
Set \(\rho_p(0)=1\) and
\[
\rho_p(a)=\frac{1+p^a}{\sum_{d\mid a}p^d}\quad(a\ge1).
\]
Let \(P=(2,3,5,7,11,13,17,19,23,29,31)\) and put
\[
(E_p)_{p\in P}=(12,8,5,4,2,2,2,2,2,2,2).
\]
For each integer vector \(\mathbf a=(a_p)_{p\in P}\) with \(0\le a_p\le E_p\), define \(R(\mathbf a)=\prod_{p\in P}\rho_p(a_p)\). The selected patterns are precisely those with \(R(\mathbf a)\ge1\). Every prime outside \(P\) is restricted to exponent zero or one. No assertion is made that this cylinder construction is optimal.

## Proof
First, multiplicativity implies that for any integer with \(v_p(n)=a_p\) for all \(p\in P\), and with all outside-prime exponents at most one,
\[
\frac{\sigma^*(n)}{\sigma^{(e)}(n)}=
R(\mathbf a)\prod_{\substack{q>31\\q\mid n}}\left(1+\frac1q\right).
\]
If \(R(\mathbf a)>1\), this is strictly greater than one. If \(R(\mathbf a)=1\), it is strictly greater than one provided any outside prime divides \(n\). The remaining numbers have all prime factors in \(P\) with the stipulated bounded exponents: there is at most one such number per exponent vector, hence finitely many exceptions.

For a fixed exponent vector, the natural density of integers satisfying these exact eleven prime-adic valuations and having squarefree cofactor supported on primes \(q>31\) equals
\[
d(\mathbf a)=\prod_{p\in P}\frac{p-1}{p^{a_p+1}}
\prod_{q>31}\left(1-\frac1{q^2}\right).
\]
This follows from the Chinese remainder theorem and the standard squarefree sieve. The Euler product converges absolutely because \(\sum_q q^{-2}<\infty\). The selected cylinder sets are pairwise disjoint. Thus \(\delta\) is at least the sum of \(d(\mathbf a)\) over every \(\mathbf a\) with \(R(\mathbf a)\ge1\).

The finite computation is an exact integer calculation, not a sample of integers. Write
\[
D=\prod_{p\in P}p^{E_p+1}
=36886693308870756519590386924324100736000000,
\]
and define the integer
\[
W=\sum_{\substack{0\le a_p\le E_p\\R(\mathbf a)\ge1}}
\prod_{p\in P}(p-1)p^{E_p-a_p}.
\]
The attached independent exact-integer enumerators give
\[
W=28604085934433764658299339805699268088627200.
\]
They enumerate all \(7,676,370\) exponent vectors, of which \(2,837,267\) have \(R\ge1\). Exactly six have \(R=1\). Every comparison \(R\ge1\) is done by cross-multiplying positive integers; no floating-point sign decisions occur.

Using \(\prod_{q>31}(1-q^{-2})=(6/\pi^2)\prod_{p\in P}(1-p^{-2})^{-1}\), the selected union has density
\[
\frac{W}{D}\cdot\frac6{\pi^2}\prod_{p\in P}\frac{p^2}{p^2-1}
=\frac{12117705984441349391635228560689}
{1593139205846841220399104000000\,\pi^2}.
\]
Finally, the classical rational inequality \(\pi<22/7\) shows, by direct rational comparison,
\[
\frac{12117705984441349391635228560689}
{1593139205846841220399104000000}\left(\frac7{22}\right)^2
=\frac{12117705984441349391635228560689}
{15736313788364717360676864000000}
>\frac{77}{100}.
\]
This completes the lower-bound proof.

## Verification
Execute `python3 verify_density.py` in a directory containing the attached verifier. The script has no nonstandard Python dependencies. It performs \(7,676,370\) exact integer comparisons, recomputes the sum and the Euler-product coefficient, and verifies the strict rational \(77\%\) threshold. The independently implemented C++ verifier (`verify_density.cpp`) uses fixed-width 256-bit integers via Boost.Multiprecision and provides a second check of the same certificate. Both were run from the final package.

## Relationship to prior work
Trudgian's *The sum of the unitary divisor function* (first made public December 17, 2013) asks for this density, proves a \(6/\pi^2\) squarefree lower bound, and reports an empirical proportion \(0.778307\). A later public mathematical record, *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density*, evaluates a six-prime finite cylinder system with cutoff five. The present work evaluates a strictly stronger eleven-prime cylinder with variable caps and rigorously crosses the \(77\%\) threshold. The two methods are related; the contribution is the materially sharper certified numerical enclosure rather than a new analytic density theorem. OEIS A322446 contains finite counts and not an asymptotic lower-bound proof.

## Limitations
The true value of \(\delta\) remains unknown, as does a comparably sharp upper bound. The eleven-prime certificate discards all valuations larger than the caps and all integers with a repeated prime factor greater than \(31\); many discarded integers satisfy the inequality. The result is a finite-arithmetic sharpening and not a general classification of all successful integers. Later or unlocated literature may contain a stronger certified lower bound.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1 (December 17, 2013), later in Publ. Inst. Math. (Beograd) 97 (2015), 175–180.
2. *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density*, publicly available record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-an-explicit-0-753659844-ldots-lower-bound-for-the-unitary-expone--831dd476bf82 .
3. OEIS A322446, *The number of solutions to usigma(k) > esigma(k) below 10^n*, https://oeis.org/A322446 .
