# Exact p-adic square-image density for upper-triangular 2-by-2 matrices

## Finding
For each prime \(p\), let \(T_p=UT_2(\mathbb Z_p)\) be the additive Haar-probability space of upper-triangular two-by-two matrices with three independent \(p\)-adic entries. Let \(S_p=\{X^2:X\in T_p\}\) be the *set of square targets*, not the distribution of squares of random roots. Then
\[
 \mu_p(S_p)=\delta_p=
 \begin{cases}
  7/372,&p=2,\\
  \dfrac{p^3(p-1)(p^2+1)}{4(p+1)(p^5-1)},&p\text{ an odd prime}.
 \end{cases}
\]
Along odd primes, the **correct asymptotic expansion** is
\[
 \delta_p=\frac14-\frac1{2p}+\frac3{4p^2}+O(p^{-3}).
\]
For \(T_{p,k}=UT_2(\mathbb Z/p^k\mathbb Z)\) and its set \(S_{p,k}\) of distinct squares,
\[
 \lim_{k\to\infty}\frac{|S_{p,k}|}{p^{3k}}=\delta_p.
\]

## Assumptions and scope
The entries of target matrices are unrestricted elements of \(\mathbb Z_p\), with normalized additive Haar measure. In particular \(\mathbb Z_p\) means the ring of \(p\)-adic integers, not \(\mathbb F_p\). The result addresses local solvability of a *single* upper-triangular square and counts neither preimages with multiplicity nor integer solutions. The loci where one target diagonal entry is zero have Haar measure zero but are permitted in the definition. No effective modular convergence rate, or global integer-square criterion, is asserted.

## Proof
Write \(X=\begin{pmatrix}x&y\\0&z\end{pmatrix}\). Then
\[
 X^2=\begin{pmatrix}x^2&(x+z)y\\0&z^2\end{pmatrix}.
\]
A target \(B=(\begin{smallmatrix}a&b\\0&c\end{smallmatrix})\) is a square precisely when \(a=x^2,c=z^2\) for some \(x,z\in\mathbb Z_p\) and \(b\in(x+z)\mathbb Z_p\). Since changing signs of nonzero diagonal roots allows both \(x+z\) and \(x-z\), the permitted \(b\)'s form the union of two principal ideals; this union is the larger ideal.

Except on the measure-zero set \(ac=0\), write \(v_p(a)=2r\), \(v_p(c)=2s\), with \(r,s\ge0\). The smaller of the valuations of \(x+z\) and \(x-z\) is
\[
 m_p(r,s)=\begin{cases}
 \min(r,s),&p\text{ odd, or }r\ne s,\\
 r+1,&p=2\text{ and }r=s.
 \end{cases}
\]
For unequal valuations this follows from the ultrametric inequality. If \(r=s\) and \(p\) is odd, simultaneous divisibility of both \(x+z,x-z\) by \(p^{r+1}\) would force \(2x\) to have too large a valuation. If \(p=2\) and \(r=s\), the reduced odd units \(u,v\) have precisely one of \(u+v,u-v\) congruent to \(2\pmod4\); hence the minimum valuation is \(r+1\). The resulting Haar probability for the off-diagonal target is \(p^{-m_p(r,s)}\).

For fixed \(r\), the Haar measure of target scalar squares having valuation \(2r\) is \(c_p p^{-2r}\), where \(c_2=1/8\) (odd-unit squares are exactly \(1\pmod8\)) and \(c_p=(p-1)/(2p)\) for odd \(p\) (half the nonzero residues are squares and square units lift). The independent target entries therefore give the absolutely convergent series
\[
 \delta_p=c_p^2\sum_{r,s\ge0}p^{-2r-2s-m_p(r,s)}.
\]
For the uncorrected minimum-valuation sum, splitting into \(r<s\), \(r=s\), and \(r>s\) gives
\[
 H_p=\sum_{r,s\ge0}p^{-2r-2s-\min(r,s)}
 =\frac{1+p^{-2}}{(1-p^{-2})(1-p^{-5})}.
\]
Thus at odd primes
\[
 \delta_p=\frac{(p-1)^2}{4p^2}H_p
 =\frac{p^3(p-1)(p^2+1)}{4(p+1)(p^5-1)}.
\]
At \(p=2\), exactly the diagonal \(r=s\) terms acquire one further factor \(1/2\), whence
\[
 \delta_2=\frac1{64}\left(H_2-\frac1{2(1-2^{-5})}\right)=\frac7{372}.
\]
Writing \(u=p^{-1}\), the odd-prime expression becomes
\[
 \delta_p=\frac{(1-u)(1+u^2)}{4(1+u)(1-u^5)}
 =\frac14-\frac u2+\frac{3u^2}4+O(u^3),
\]
which proves the stated corrected asymptotic. In particular the coefficient of \(p^{-1}\) is \(-1/2\), **not** \(-3/4\).

To prove convergence of the modular densities, let \(E_k\subseteq T_p\) be all targets whose reduction modulo \(p^k\) is a square. Each \(E_k\) is compact open, these sets decrease, and \(\mu_p(E_k)=|S_{p,k}|/p^{3k}\). Their intersection is precisely \(S_p\): the corresponding nonempty compact sets of roots satisfying \(X^2\equiv B\pmod{p^k}\) are nested and have a common point, giving an exact root in \(T_p\). Continuity of Haar probability from above now gives the limit.

## Independent checks and limits
A standard-library finite-ring check counts distinct square targets from diagonal square-root fibers by the gcd of possible sums \(x+z\); this directly tests the finite-ring image measure at \(p=2,3,5,7\) for bounded exponents. Independent symbolic manipulation verifies the summation identity and the corrected large-\(p\) expansion. Such tests cannot replace the proof for every prime or for \(k\to\infty\). The previously published text had the incorrect coefficient \(-3/4\) in its leading asymptotic, although the exact rational density itself and the dyadic formula were correct. This document corrects that mathematical statement without modifying the exact densities or their domains.

## Relationship to prior work
Franušić and Pejković (2026) provide the elementary upper-triangular matrix square-root criterion when studying Jordan Diophantine sets of integer matrices. That criterion does not by itself evaluate the Haar measure of square targets in \(UT_2(\mathbb Z_p)\), including the distinct dyadic behavior. Dujella and Franušić (2026) study differences of two integral matrix squares. Panja and Prasad (2022) consider polynomial images over algebraically closed fields, while Kaushik and Singh (2023) consider Waring problems for finite-field triangular algebras. The current result is the exact local square-target density and convergence of finite-ring image proportions, rather than the matrix multiplication identity. An earlier implicit derivation in unindexed local arithmetic literature remains a bibliographic possibility.

## References
1. Z. Franušić and T. Pejković, *Cardinalities of Jordan Diophantine sets of upper triangular integer matrices* (2026), arXiv:2610.10773, https://arxiv.org/abs/2610.10773.
2. A. Dujella and Z. Franušić, *Differences of squares of upper-triangular 2×2 integer matrices* (2026).
3. S. Panja and S. Prasad, *The image of polynomials and Waring type problems on upper triangular matrix algebras* (2022), arXiv:2206.08827, https://arxiv.org/abs/2206.08827.
4. R. Kaushik and A. Singh, *Waring Problem For Triangular Matrix Algebra* (2023), arXiv:2311.09598, https://arxiv.org/abs/2311.09598.
