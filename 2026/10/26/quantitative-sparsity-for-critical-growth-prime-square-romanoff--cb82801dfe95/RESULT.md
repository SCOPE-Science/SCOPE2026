# Quantitative sparsity for critical-growth prime-square Romanoff sums

## Finding
Let \(\mathcal P\) be any set of primes congruent to \(1\pmod 4\), and put
\[
a_k=2^k\prod_{\substack{r\in\mathcal P\\r\le k}}r\qquad(k\ge1).
\]
Let \(S_{\mathcal P}(X)\) count distinct positive integers at most \(X\) representable as
\[
n=p^2+q^2+a_k+a_l,
\]
where \(p,q\) are primes and \(k,l\ge1\). Define, for \(y\ge2\),
\[
H_{\mathcal P}(y)=\sum_{\substack{r\in\mathcal P\\r\le y}}\frac1r,\quad
 t=\frac1{\log 2},\quad
\delta=1-t+t\log t=0.086071332055934\ldots.
\]
There is an absolute constant \(C>0\), independent of \(\mathcal P\), such that, for every sufficiently large real \(X\),
\[
S_{\mathcal P}(X)\le CX\left\{\exp\left(-\delta H_{\mathcal P}(\sqrt{\log X})\right)+(\log X)^{-1/2}\right\}.\tag{1}
\]
In particular, taking \(\mathcal P\) to be all primes congruent to \(1\pmod4\),
\[
S_{\mathcal P}(X)\ll \frac{X}{(\log\log X)^{\delta/2}}.
\tag{2}
\]
More generally, if \(\sum_{r\in\mathcal P}1/r=\infty\), then \(S_{\mathcal P}(X)=o(X)\). The quantitative finite-scale inequality (1), rather than this qualitative density-zero conclusion alone, is the claimed result.

## Assumptions and scope
All logarithms are natural, products over an empty set equal one, and \(\mathcal P\) may be finite or infinite. The sequence is strictly increasing, with \(a_k\mid a_{k+1}\) and \(a_k\ge2^k\). Chebyshev's estimate \(\sum_{p\le z}\log p=O(z)\) implies \(\log a_k=O(k)\) uniformly in \(\mathcal P\): thus the construction lies at the logarithmic-counting threshold \(\#\{k:a_k\le X\}\asymp\log X\) (the lower bound follows from the same Chebyshev estimate). The argument uses only classical upper bounds on primes in progressions; it makes no assertion about an asymptotic formula or an optimal decay exponent.

## Proof
Fix \(X\) sufficiently large. Write \(y=\sqrt{\log X}\), \(K=\lceil y\rceil\), and
\[
\mathcal F=\{r\in\mathcal P:r\le y\},\quad Q=\prod_{r\in\mathcal F}r,\quad H=\sum_{r\in\mathcal F}\frac1r.
\]
The case \(\mathcal F=\varnothing\) follows at once from the trivial bound \(S_{\mathcal P}(X)\le X\), so suppose \(\mathcal F\ne\varnothing\). Define \(T(m)=\sum_{r\in\mathcal F}\mathbf1_{r\mid m}\), a \(Q\)-periodic nonnegative integer statistic. By the Chinese remainder theorem, over one complete block of \(Q\) integers the divisibility indicators are independent Bernoulli variables of means \(1/r\). With \(s=\log t>0\), the exponential Markov inequality and \(1+u\le e^u\) give
\[
\frac1Q\#\{1\le m\le Q:T(m)\ge tH\}
\le e^{-stH}\prod_{r\in\mathcal F}\left(1+\frac{e^s-1}{r}\right)
\le\exp\bigl(-(t\log t-t+1)H\bigr)=e^{-\delta H}.
\tag{3}
\]
Consequently the number of integers \(m\le X\) with \(T(m)\ge tH\) is at most \(Xe^{-\delta H}+Q\).

Independently, choose residues \(u,v\) uniformly among units modulo \(Q\). For each \(r\in\mathcal F\), \(-1\) has exactly two square roots modulo \(r\), so
\[
\Pr(r\mid u^2+v^2)=\frac{2}{r-1}.
\]
CRT again makes these indicators independent. If \(\mu=\sum_{r\in\mathcal F}2/(r-1)\), then \(\mu\ge2H\). Set \(b=\log(2/t)>0\). Applying exponential Markov to \(e^{-bT}\),
\[
\Pr(T(u^2+v^2)<tH)
\le e^{btH}\prod_{r\in\mathcal F}\left(1+\frac{2(e^{-b}-1)}{r-1}\right)
\le\exp\left(btH+(e^{-b}-1)\mu\right)
\le\exp\bigl((bt+t-2)H\bigr)=e^{-\delta H}.
\tag{4}
\]
The last identity follows from \(t\log2=1\); the two exponential rates coincide exactly for the chosen \(t\).

Because \(\vartheta(y)=\sum_{r\le y}\log r\ll y\), one has \(Q\le\exp(O(\sqrt{\log X}))\le X^{1/4}\) once \(X\) is sufficiently large, uniformly in \(\mathcal P\). The Brun--Titchmarsh inequality therefore gives, for every reduced residue class \(u\pmod Q\),
\[
\#\{p\le\sqrt X:p\text{ prime},\ p\equiv u\pmod Q\}
\le \frac{2\sqrt X}{\varphi(Q)\log(\sqrt X/Q)}
\ll\frac{\sqrt X}{\varphi(Q)\log X}.
\tag{5}
\]
The bound remains valid when \(Q=1\), by the classical prime-counting bound.

Let \(A(X)=\#\{k\ge1:a_k\le X\}\). Since \(a_k\ge2^k\), \(A(X)\le(\log X)/(\log2)\). Representations with \(k<K\) or \(l<K\) give at most
\[
2K A(X)\pi(\sqrt X)^2\ll X(\log X)^{-1/2}\tag{6}
\]
distinct integers. For the remaining representations \(k,l\ge K\), all primes in \(\mathcal F\) divide both shifts, so \(Q\mid a_k,a_l\) and \(T(n)=T(p^2+q^2)\). The integers with \(T(n)\ge tH\) are counted by (3), at most \(Xe^{-\delta H}+Q\).

For \(T(n)<tH\), first remove the pairs for which \(p\mid Q\) or \(q\mid Q\). Their total possible representations are at most
\[
2\lvert\mathcal F\rvert\,\pi(\sqrt X)\,A(X)^2\ll X(\log X)^{-1/2},\tag{7}
\]
using \(\lvert\mathcal F\rvert\le y\) (indeed the left side is much smaller). For the remaining prime pairs, group their reduced residue classes \((u,v)\pmod Q\). Formula (4) says that at most \(\varphi(Q)^2e^{-\delta H}\) ordered residue pairs satisfy \(T(u^2+v^2)<tH\). Multiplying the bound (5) for the two prime coordinates and then by \(A(X)^2\) yields at most \(O(Xe^{-\delta H})\) representations, hence no more distinct integers. Since \(Q\ll X(\log X)^{-1/2}\), (3)--(7) prove (1).

When \(\mathcal P\) is the entire set of primes \(1\pmod4\), Mertens' theorem for primes in this progression gives
\[
H_{\mathcal P}(y)=\tfrac12\log\log y+O(1),\quad
H_{\mathcal P}(\sqrt{\log X})=\tfrac12\log\log\log X+O(1).
\]
Substitution into (1) gives (2), because \((\log X)^{-1/2}\) is negligible compared with any fixed negative power of \(\log\log X\). The same argument with \(H\to\infty\) proves the final assertion.

## Verification
The included standalone `check_local.py` enumerates reduced residue pairs modulo every prime \(r\equiv1\pmod4\) at most \(151\), checking exactly the count \(2(r-1)\) when \(u^2+v^2\equiv0\pmod r\), and checks the complementary nonzero-residue formula. It also checks the numerical exponent identity. It returned `VERIFY_OK 16 moduli delta 0.086071332055934`. These finite calculations check local normalization; the independence claims and the infinite inequalities are established analytically above, not inferred from the computations.

## Relationship to prior work
Ding and Verwee's Romanoff-type short-interval theorem concerns sums of one prime with structured lacunary shifts, not sums of two prime squares and two growing divisibility-chain shifts. Dai and Pan establish positive lower density under a bounded reciprocal-divisor sum for the latter object; our family with divergent reciprocal sum lies outside that hypothesis. Yan and Xu (first publicly posted 20 October 2026) establish the qualitative density-zero converse for all divisibility chains with divergent reciprocal sums. Their full proof controls the corresponding CRT discrepancy using second moments and a fixed modulus, giving a qualitative limit; it does not supply the uniform finite-\(X\) bound (1), the moving modulus, or the explicit \((\log\log X)^{-\delta/2}\) rate (2). Their local probability calculation for \(r\mid u^2+v^2\) is shared background, not claimed as new. The incremental assertion here is an effective, large-deviation refinement for a specific critical-growth family.

## Limitations
The exponent \(\delta/2\) is not shown to be sharp; the full-source coverage of the Dai--Pan paper could not be checked and may contain additional quantitative bounds. The published Yan--Xu qualitative theorem already implies the density-zero consequence, which must not be mistaken for the new part of the claim. Nothing here implies analogous rates for arbitrary divisibility chains or primes congruent to \(3\pmod4\). Brun--Titchmarsh is invoked in its classical uniform upper-bound form; all numerical experiments are finite.

## References
1. Y. Ding and J. Verwee, *Short intervals for the Romanoff-type sumset*, arXiv:2602.14368v1 (first public 16 February 2026), Journal of Number Theory 289 (2026), 114--131. https://arxiv.org/abs/2602.14368 ; https://arxiv.org/html/2602.14368v3 .
2. L. Dai and H. Pan, *On Erdős' generalization of the Romanoff theorem*, Journal of Number Theory 291, 65--73, DOI:10.1016/j.jnt.2026.04.003. Public abstract consulted; full text was not available to this review.
3. X.-H. Yan and Y.-T. Xu, *A necessary condition for a Romanoff type theorem*, arXiv:2610.28237v1 (first public 20 October 2026), https://arxiv.org/html/2610.28237v1 ; Sections 1--3 checked.
4. H. Davenport, *Multiplicative Number Theory*, third edition (revised by H. Montgomery), Springer (2000), for classical progression prime-counting estimates.
