# An explicit \(0.784716\) upper bound for the unitary–exponential divisor-sum comparison density

## Finding
Write
\[\sigma^*(n)=\prod_{p^a\parallel n}(1+p^a),\qquad
\sigma^{(e)}(n)=\prod_{p^a\parallel n}\sum_{d\mid a}p^d.\]
Let \(\delta\) be the natural density of integers \(n\ge1\) for which \(\sigma^*(n)>\sigma^{(e)}(n)\). Then the density exists and
\[\boxed{\delta<\frac{784716}{1000000}=0.784716.}\]
This is an upper bound on the *frequency of strict comparison*, not a pointwise upper bound on either divisor-sum function.

## Assumptions and scope
The integers \(n\) are positive. The definition of exponential divisors uses positive divisors \(d\mid a\) of the prime-power exponent \(a\), and both sums at \(n=1\) equal one. For a prime \(p\) and exponent \(a\ge0\), set
\[r(p,0)=1,\qquad r(p,a)=\frac{p^a+1}{\sum_{d\mid a}p^d}\quad(a\ge1).\]
Thus the relevant logarithmic ratio is the additive arithmetic function \(F(n)=\sum_{p^a\parallel n}\log r(p,a)\).

## Proof
**The limiting law.** Let \(E_p\) be independent random variables with \(\Pr(E_p=a)=(1-p^{-1})p^{-a}\), \(a\ge0\). Since \(r(p,1)=1+p^{-1}\), whereas \(0<r(p,a)<1\) for \(a\ge2\), and \(\lvert\log r(p,a)\rvert\ll 1/p\) uniformly for all sufficiently large \(p\), we have \(\sum_p\mathbb E\lvert\log r(p,E_p)\rvert<\infty\). The Erdős–Wintner theorem identifies the limiting distribution of \(F(n)\) with that of the almost surely absolutely convergent series \(X=\sum_p\log r(p,E_p)\). Because \(F(p)=\log(1+1/p)\ne0\) for every prime and \(\sum_p1/p=\infty\), Lévy's continuity criterion gives \(\Pr(X=0)=0\). Therefore \(\delta=\Pr(X>0)\).

**Finite-prime majorant.** Choose \(Y=1000\), \(\beta=50001/50000>1\) and \(T=500\). For the primes \(p\le31\) prescribe caps
\[
(c_2,c_3,c_5,c_7,c_{11},c_{13},c_{17},c_{19},c_{23},c_{29},c_{31})
=(12,9,7,6,5,5,4,4,4,4,4).
\]
For these primes and each \(0\le a\le c_p\), set \(u_{p,a}\) to the unique integer satisfying
\[\beta^{u_{p,a}-1}<r(p,a)\le\beta^{u_{p,a}}.\]
In particular, \(u_{p,0}=0\). For each \(31<p\le1000\), set \(u_{p,0}=0\) and let \(u_{p,+}\) be the least integer with \(1+1/p\le\beta^{u_{p,+}}\). At exponents \(a\ge2\) one has
\[r(p,a)\le\frac{p^a+1}{p^a+p}<1<1+1/p,\]
so this single positive-exponent state dominates every such factor. Let \(S\) be the sum of these integer majorants for the independent \(E_p\), excluding the events \(E_p>c_p\) at the eleven small primes. Let \(U=\sum_{p>1000}\mathbf1_{E_p>0}/p\). Outside the excluded events,
\[X\le(\log\beta)S+U.\]
Consequently \(X>0\), \(U\le500\log\beta\) force \(S>-500\), hence \(S\ge-500\). By the union bound,
\[\delta\le\Pr(S\ge-500)+\sum_{p\le31}p^{-c_p-1}
+\Pr(U>500\log\beta).\tag{1}\]
Here \(S\) is evaluated only on the non-exceptional states; \(\Pr(S\ge-500)\) means their unnormalized total probability.

**Exact finite convolution.** For \(p\le31\), the states \(a=0,\ldots,c_p\) carry integer weights \((p-1)p^{c_p-a}\) over denominator \(p^{c_p+1}\). For \(31<p\le1000\), the two states carry weights \((p-1,1)\) over denominator \(p\). The standalone verifier computes all exponents \(u\) with integer cross-multiplication and takes the ordinary generating-function product of these weighted state polynomials. It certifies the exact integer inequality
\[\boxed{\Pr(S\ge-500)<784271/1000000}\tag{2}\]
and, by exact rational addition, \(\sum_{p\le31}p^{-c_p-1}<145/1000000\). Its complete coefficient array has \(153387\) positions, minimum exponent \(-52491\), and the tail starts at position \(51991\). No floating-point comparison is used in the certificate.

**Infinite-prime tail.** Independence and convexity of the exponential imply
\[\begin{aligned}
\mathbb E e^{1000U}&=\prod_{p>1000}\left(1+\frac{e^{1000/p}-1}{p}\right)\\
&\le\exp\left((e-1)1000\sum_{p>1000}p^{-2}\right)<e^{e-1}<6,
\end{aligned}\]
using \(\sum_{p>1000}p^{-2}<\sum_{n>1000}n^{-2}<1/1000\). Markov's inequality gives
\[\Pr(U>500\log\beta)<6\beta^{-500000}<300/1000000.\tag{3}\]
For the last strict inequality, \(\log\beta\ge1/50001\), \(500000/50001>999/100\), and the 30-term exponential Taylor lower sum at \(999/100\) exceeds \(20000\), all verified using rational arithmetic. Likewise the elementary rational exponential Taylor upper bound at \(7/4\), together with \(e<11/4\), proves \(e^{e-1}<6\). Combining (1)–(3) gives
\[\delta<\frac{784271+145+300}{1000000}=\frac{784716}{1000000}.\]

## Verification
Run `python3 verify_upper.py` with Python 3.10 or later, using only the standard library. It independently sieves the first \(168\) primes through \(1000\), computes every prime-exponent ceiling by exact integer inequalities, constructs the finite convolution, and checks every numerical inequality used above as an exact integer/rational comparison. The verifier reports `VERIFY_OK`, the number of coefficient positions, the cutoff, and approximate *diagnostic only* values. The proof's infinite-tail estimates and convergence are analytic, not inferred from finite tests.

## Relationship to prior work
Trudgian [1], first publicly posted December 17, 2013, explicitly asks for the density of the strict inequality and reports a sample proportion near \(0.778307\). His source gives the squarefree lower bound \(6/\pi^2\), not the present rigorous upper bound. A publicly catalogued finite-cylinder lower certificate [3] yields \(\delta\ge0.753659844\ldots\), which is logically a lower bound and does not imply the upper result. Tenenbaum and Verwee [2] give general effective Erdős–Wintner theory, which supplies distributional context but not this explicit inequality-specific upper bound. No equivalent upper certificate was found in the sources examined; this is not a claim that all possible literature has been exhausted.

## Limitations
The estimate is not an exact formula for \(\delta\), does not determine the density of equality, and is not known to be optimal. The finite convolution depends on a specific cutoff and discretization; refining it might improve the bound. Verification is internal mathematical review only, without independent audit. Historical-priority risk remains for specialized density bounds not found in the inspected literature.

## References
[1] T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615, first posted 2013-12-17 (original open question on PDF page 6).

[2] G. Tenenbaum and J. Verwee, *Effective Erdős–Wintner theorems*, arXiv:2002.07475 (continuity criterion and limiting Euler-product law, page 1).

[3] *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density*, publicly indexed mathematical result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-an-explicit-0-753659844-ldots-lower-bound-for-the-unitary-expone--831dd476bf82.
