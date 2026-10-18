# Exact \(p\)-adic square-image density for upper-triangular \(2\times2\) matrices

## Finding
For every prime \(p\), let \(T_p\) be the ring of upper-triangular \(2\times2\) matrices over \(\mathbb Z_p\), identified with \(\mathbb Z_p^3\) by its three entries. Write \(S_p=\{X^2:X\in T_p\}\) and use normalized additive Haar measure \(\mu_p\) on \(T_p\). The exact measure of the image of squaring is
\[
\mu_p(S_p)=\delta_p=\begin{cases}
7/372,&p=2,\\[3pt]
\displaystyle\frac{p^3(p-1)(p^2+1)}{4(p+1)(p^5-1)},&p\text{ odd}.
\end{cases}
\]
In particular \(\delta_p=1/4-3/(4p)+O(p^{-2})\) along odd primes. For the finite ring \(T_{p,k}=UT_2(\mathbb Z/p^k\mathbb Z)\), if \(S_{p,k}=\{X^2:X\in T_{p,k}\}\), then
\[
\lim_{k\to\infty}\frac{|S_{p,k}|}{p^{3k}}=\delta_p.
\]

## Assumptions and scope
All primes \(p\) are included; \(\mathbb Z_p\) denotes the complete ring of \(p\)-adic integers, not the finite field. The probability is for a uniformly Haar-random **target matrix** to be some single square; it is not the probability of a randomly selected matrix root producing a particular square. Matrix entries are unrestricted. The exact formula concerns \(p\)-adic square-solvability, not integer square-solvability, and does not count square roots with multiplicity. Matrix zeros on either diagonal are an event of Haar measure zero, and the proof treats this boundary explicitly.

## Proof
**1. The local image condition.** Write \(X=\left(\begin{smallmatrix}x&y\\0&z\end{smallmatrix}\right)\). Direct matrix multiplication gives
\[
X^2=\begin{pmatrix}x^2&(x+z)y\\0&z^2\end{pmatrix}.
\]
Consequently, a target \(B=\left(\begin{smallmatrix}a&b\\0&c\end{smallmatrix}\right)\) is a square precisely when its diagonal entries have square roots \(x,z\in\mathbb Z_p\) and \(b\) belongs to at least one principal ideal \((x+z)\mathbb Z_p\), as the signs of \(x,z\) vary. This is the elementary criterion used for integral upper-triangular matrices in Franušić--Pejković; here it is applied in the local ring.

**2. Fixed-valuation fibers.** Exclude the Haar-null set where \(a=0\) or \(c=0\). Suppose both diagonals are nonzero squares with \(v_p(a)=2r\) and \(v_p(c)=2s\), where \(r,s\ge0\). Over the characteristic-zero field \(\mathbb Q_p\), each nonzero square has exactly two roots, related by sign. The union of the associated principal ideals is itself an ideal, namely the largest of the ideals \((x+z)\mathbb Z_p\) and \((x-z)\mathbb Z_p\). Its valuation exponent is
\[
m_p(r,s)=\begin{cases}
\min(r,s),&p\text{ odd or }r\ne s,\\
r+1,&p=2\text{ and }r=s.
\end{cases}
\]
Indeed, if \(r\ne s\), both sums have valuation \(\min(r,s)\). If \(r=s\) and \(p\) is odd, at least one of \(x+z,x-z\) has valuation exactly \(r\): otherwise their sum \(2x\) would be divisible by \(p^{r+1}\), impossible. For \(p=2\), write \(x=2^ru,z=2^rv\) with odd \(u,v\); exactly one of \(u+v,u-v\) is \(2\pmod4\), while the other is \(0\pmod4\). Thus the smaller valuation is exactly \(r+1\). A Haar-random upper-right entry \(b\) lies in \(p^{m_p(r,s)}\mathbb Z_p\) with probability \(p^{-m_p(r,s)}\).

**3. Scalar square density.** For a fixed \(r\ge0\), the Haar measure of scalar squares \(a\in\mathbb Z_p\) with valuation \(2r\) equals \(c_p p^{-2r}\), where
\[
c_p=\begin{cases}(p-1)/(2p),&p\text{ odd},\\1/8,&p=2.\end{cases}
\]
For odd \(p\), precisely half of the nonzero residue classes modulo \(p\) are unit squares, and lifting preserves that characterization. For \(p=2\), the unit squares are exactly the units congruent to \(1\pmod8\). Independence of the three target entries and Step 2 therefore give the absolutely convergent series
\[
\delta_p=c_p^2\sum_{r,s\ge0}p^{-2r-2s-m_p(r,s)}.
\]

**4. Geometric summation.** Separating the two halves of the lattice \((r,s)\) at \(r=s\) yields the exact identity
\[
H_p:=\sum_{r,s\ge0}p^{-2(r+s)-\min(r,s)}
=\frac{1+p^{-2}}{(1-p^{-2})(1-p^{-5})}.
\]
For odd \(p\), substitute \(m_p=\min\) and \(c_p=(p-1)/(2p)\), and simplify to
\[
\delta_p=\frac{(p-1)^2}{4p^2}H_p
=\frac{p^3(p-1)(p^2+1)}{4(p+1)(p^5-1)}.
\]
For \(p=2\), the terms on the diagonal \(r=s\) have an additional factor \(1/2\), and the uncorrected diagonal contribution is \(\sum_{r\ge0}2^{-5r}=(1-2^{-5})^{-1}\). Thus
\[
\delta_2=\frac1{64}\left(H_2-\frac{1}{2(1-2^{-5})}\right)
=\frac7{372}.
\]
The expansion along odd primes follows directly by expanding the rational function in powers of \(p^{-1}\).

**5. Finite-level convergence.** Let \(E_k\subseteq T_p\) be the inverse image of \(S_{p,k}\) under reduction modulo \(p^k\). The \(E_k\) form a decreasing sequence of compact-open sets, with \(\mu_p(E_k)=|S_{p,k}|/p^{3k}\). Their intersection is \(S_p\): if \(B\in\bigcap_kE_k\), the compact nonempty sets \(\{X\in T_p:X^2\equiv B\pmod{p^k}\}\) are nested, so a common limit point satisfies \(X^2=B\) exactly. Continuity from above of probability measure yields \(\mu_p(S_p)=\lim_{k\to\infty}\mu_p(E_k)\), proving the finite-level assertion.

## Verification
A standalone standard-library program, `verify.py`, independently counts distinct square images over each residue ring by enumerating diagonal-root fibers and using gcd ideals for the off-diagonal entry. It checks every exponent \(1\le k\le8\) for \(p=2\), \(1\le k\le5\) for \(p=3\), \(1\le k\le3\) for \(p=5\), and \(1\le k\le2\) for \(p=7\). All computed proportions exceed the exact Haar limits and decrease with \(k\); independent truncated rational series agree with the formulas to absolute tolerance \(10^{-12}\). These finite checks support, but do not prove, the all-prime infinite result, which follows from Steps 1--5.

## Relationship to prior work
Franušić and Pejković (2026) use the square-root criterion for upper-triangular integer matrices in their investigation of the cardinalities of Jordan Diophantine sets. Their local ingredients motivate considering the natural square-image locus, but their theorems concern sizes and existence of such sets over the integers, not normalized \(p\)-adic Haar density of single squares. Dujella and Franušić (2026) study **differences** of two integer-matrix squares, a different image problem. Panja and Prasad (2022) study polynomial images on upper-triangular algebras over algebraically closed fields, while Kaushik and Singh (2023) study sums of powers over finite fields. Neither setting implies the rational local density and its dyadic correction. The novelty claim concerns precisely the complete \(p\)-adic probability formula and the finite-level limit, not the basic matrix-squaring identity.

## Limitations
This is a local, not a global integral-solvability theorem; local square-solvability at any prime is only a necessary condition for a matrix to be a square over \(\mathbb Z\). No uniform effective convergence rate in \(k\) is claimed. While no directly covering exact Haar-density formula was identified in the literature compared, an implicit derivation in earlier local-ring counting work could exist. Independent mathematical audit has not been performed.

## References
1. Z. Franušić and T. Pejković, *Cardinalities of Jordan Diophantine sets of upper triangular integer matrices* (2026), arXiv:2610.10773, first publicly posted 2026-10-07, primary MSC 11C20. https://arxiv.org/abs/2610.10773
2. A. Dujella and Z. Franušić, *Differences of squares of upper-triangular 2×2 integer matrices* (2026).
3. S. Panja and S. Prasad, *The image of polynomials and Waring type problems on upper triangular matrix algebras* (2022), arXiv:2206.08827. https://arxiv.org/abs/2206.08827
4. R. Kaushik and A. Singh, *Waring Problem For Triangular Matrix Algebra* (2023), arXiv:2311.09598. https://arxiv.org/abs/2311.09598
