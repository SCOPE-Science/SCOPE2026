# Zero multiplicities and phase indices of the Sierpinski-gasket Fourier transform

## Finding
Let \(\mu\) be the equal-weight self-similar probability measure of the planar three-corner Sierpinski gasket with contraction ratio \(1/2\), and use the Fourier convention
\[
\widehat\mu(\xi)=\int_{\mathbb R^2}e^{-2\pi i\xi\cdot x}\,d\mu(x).
\]
Write \(Z\) for its real zero set, \(\operatorname{ord}_{\xi}\widehat\mu\) for the smallest nonzero total Taylor degree at a zero, and \(\operatorname{ind}_{\xi}\widehat\mu\) for the positively oriented local phase winding of \(\widehat\mu/|\widehat\mu|\). Set \(\nu_2(a)\) equal to the exponent of \(2\) dividing a nonzero integer \(a\).

**Theorem.** The zero set is discrete and is exactly
\[
Z=\left\{\frac23(u,v):u,v\in\mathbb Z,\quad
(u\bmod3,v\bmod3)\in\{(1,2),(2,1)\}\right\}.
\]
At \(\xi=\frac23(u,v)\in Z\), put \(r=1+\min(\nu_2(u),\nu_2(v))\). Then
\[
\operatorname{ord}_{\xi}\widehat\mu=r,
\qquad
\operatorname{ind}_{\xi}\widehat\mu=
\begin{cases}
0,&r\text{ even},\\
-1,&r\text{ odd and }(u,v)\bmod3=(1,2),\\
+1,&r\text{ odd and }(u,v)\bmod3=(2,1).
\end{cases}
\]
Every positive multiplicity occurs, but every nonzero local phase index has absolute value one.

Let \(N(R)=\#(Z\cap\{\xi:|\xi|\le R\})\), and let \(N_{=r}(R)\) count its zeros of exact order \(r\). For all \(R\ge0\) and every integer \(r\ge1\),
\[
N_{=r}(R)=N(R/2^{r-1})-N(R/2^r).
\]
As \(R\to\infty\), for every fixed \(r\),
\[
N(R)=\frac\pi2R^2+O(R+1),\qquad
N_{=r}(R)=\frac{3\pi}{8}\,4^{-(r-1)}R^2+O(R/2^{r-1}+1).
\]
In particular, the asymptotic distribution of zero orders is geometric:
\[
\lim_{R\to\infty}\frac{N_{=r}(R)}{N(R)}=\frac3{4^r}.
\]
The total multiplicity-weighted count is
\[
\sum_{\substack{\xi\in Z\\|\xi|\le R}}\operatorname{ord}_{\xi}\widehat\mu
=\frac{2\pi}{3}R^2+O(R+1).
\]
The zero-index classes \(-1,0,+1\), respectively, contain asymptotically the proportions \(2/5,1/5,2/5\) of all distinct zeros. More precisely, their leading counts are \(\pi R^2/5,\pi R^2/10,\pi R^2/5\), respectively, with error \(O(R+1)\). The number of positive-index zeros equals the number of negative-index zeros in **every** origin-centered disk, not only asymptotically.

## Assumptions and scope
The measure is the law of the almost surely convergent random series
\[
X=\sum_{j=1}^\infty2^{-j}D_j,\qquad
\mathbb P(D_j=(0,0))=\mathbb P(D_j=(1,0))=\mathbb P(D_j=(0,1))=\tfrac13,
\]
where the digits are independent. This fixes the coordinate convention: the gasket is the triangle with vertices \((0,0),(1,0),(0,1)\), not an equilateral-coordinate rescaling. The Euclidean radius \(R\) is measured in these coordinates. The statements concern the real-frequency Fourier transform and its isolated real zeros; the Taylor order is a real-analytic total-degree order, not a one-complex-variable zero multiplicity. The local phase index is defined on any sufficiently small counterclockwise circle around a zero.

## Proof
**1. Mask and nonvanishing of the infinite tail.** Independence and uniform compact convergence give
\[
\widehat\mu(\xi)=\prod_{j=1}^\infty M(2^{-j}\xi),\qquad
M(t)=\tfrac13(1+e^{-2\pi i t_1}+e^{-2\pi i t_2}).
\]
On each compact complex-frequency set, \(M(2^{-j}\xi)=1+O(2^{-j})\) uniformly. Thus the infinite product converges locally uniformly and is nonzero wherever none of its individual factors vanishes. Three unit complex numbers sum to zero exactly when the last two are the two nontrivial cube roots of unity. Hence
\[
Z(M)=\big((1/3,2/3)+\mathbb Z^2\big)\cup
\big((2/3,1/3)+\mathbb Z^2\big).
\]
The zero set of the factor at level \(j\) is \(2^jZ(M)\). Since multiplication by two interchanges the two nontrivial residue classes modulo three, these factor-zero sets form a nested sequence:
\[
2^j Z(M)=2^{j-1} Z_1,\qquad Z_1=2Z(M),\qquad Z_{j+1}\subset Z_j.
\]
Their union therefore equals \(Z_1=Z\). This proves the asserted exact zero set and its discreteness, while also preventing zeros caused by an infinite product of nonzero factors.

**2. Orders and local phase.** Fix \(\xi_0=\frac23(u,v)\in Z\) and let \(r=1+\min(\nu_2(u),\nu_2(v))\). Precisely the first \(r\) factors vanish at \(\xi_0\). Set
\[
\omega=e^{-2\pi i/3},\qquad L(h)=\omega h_1+\overline\omega h_2.
\]
For the orientation \((u,v)\bmod3=(1,2)\), the exact first-order Taylor expansions of the vanishing factors are
\[
M(2^{-j}(\xi_0+h))=
-\frac{2\pi i}{3\,2^j}
\begin{cases}L(h),&j\text{ odd},\\ \overline{L(h)},&j\text{ even}\end{cases}
+O(|h|^2).
\]
The other orientation interchanges \(L\) and \(\overline L\). Consequently, for the first orientation,
\[
\widehat\mu(\xi_0+h)
=C_{\xi_0}L(h)^{\lceil r/2\rceil}
\overline{L(h)}^{\lfloor r/2\rfloor}+O(|h|^{r+1}),
\]
where
\[
C_{\xi_0}=\left(-\frac{2\pi i}{3}\right)^r
2^{-r(r+1)/2}\prod_{j>r}M(2^{-j}\xi_0)\ne0.
\]
The other orientation conjugates the linear factors but not the harmless nonzero constant. Since \(|L(h)|^2=h_1^2+h_2^2-h_1h_2\ge |h|^2/2\), the leading term is uniformly bounded away from zero after division by \(|h|^r\) on the unit circle. Hence \(\xi_0\) is an isolated zero of exact Taylor order \(r\). The real-linear map \(h\mapsto L(h)\) reverses orientation: its determinant is negative. Its conjugate preserves orientation. The homotopy from the actual Fourier transform to its nonzero leading term on a small circle is valid by the uniform remainder estimate; the winding is therefore \(-1\) for odd \(r\) in the first orientation, \(+1\) for odd \(r\) in the reversed orientation, and zero for even \(r\). In particular, even-order zeros have local leading phase independent of direction despite being higher-order isolated complex zeros.

**3. Exact rescaling and densities.** The level-\(r\) condition \(\operatorname{ord}_{\xi}\widehat\mu\ge r\) is equivalent to \(2^{r-1}\mid u\) and \(2^{r-1}\mid v\), so
\[
\{\xi\in Z:\operatorname{ord}_{\xi}\widehat\mu\ge r\}=2^{r-1}Z.
\]
Taking exact disk counts proves the displayed finite-radius identities. The set \(Z\) comprises two cosets of the lattice \(2\mathbb Z^2\); one fundamental square has area four and contains two zeros. Standard disk/lattice-cell counting yields \(N(R)=\pi R^2/2+O(R+1)\), and the rescaling identity yields the exact-order asymptotic. Summing the exact tail counts gives
\[
\sum_{\xi\in Z,\,|\xi|\le R}\operatorname{ord}_{\xi}\widehat\mu
=\sum_{j\ge0}N(R/2^j)
=\frac{\pi R^2}{2}\sum_{j\ge0}4^{-j}+O(R+1)
=\frac{2\pi}{3}R^2+O(R+1).
\]
The error sum is finite since \(Z\) has positive separation from the origin; it consists of a geometric \(O(R)\) part plus only \(O(\log(R+2))\) constant-size errors. Summing the geometric densities over even orders gives proportion \(1/5\) of zero-index nodes; summing over odd orders gives \(4/5\). Reflection \((u,v)\mapsto(v,u)\) preserves the Euclidean norm and the order but exchanges the odd-order index signs. Thus positive and negative counts coincide exactly, and each has limiting proportion \(2/5\). This proves all assertions.

## Verification
Run `python3 check_sierpinski_vortices.py` with Python 3 and its standard library. The checker enumerates exact integer-coordinate zeros inside four disks, verifies the exact nested-radius count identity, independently evaluates truncated mask products, and computes local phase windings on eight representative circles of orders one through four. It passed at radii \(9,27,90,180\): respectively \(124,1150,12724,50914\) distinct zeros. These finite calculations are diagnostics only; the proof of the unrestricted statements is the analytic infinite-product argument and the lattice count above.

## Relationship to prior work
The affine-IFS measure representation and Fourier tools are classical; see Dutkay and Jorgensen (2006). More directly, Chen and Ai (2025), equations (1.3), (2.1), and (2.2), explicitly treat planar three-digit mask-zero cosets and the union-of-dilates zero-set formula. Thus neither the mask-zero formula nor its use for Fourier orthogonality is claimed as new. The contribution here is the complete **Taylor-zero divisor**, the **signed local Fourier phase indices**, and their **exact finite-radius nesting and asymptotic order/charge distributions** for the canonical dyadic measure. Those refinements are not statements of the inspected spectrality theorems. The related 2015 Deng–Lau Sierpinski-type spectrality article could not be inspected in full and remains a priority risk.

## Limitations
Only the equal-weight three-digit dilation-two measure in the stated affine coordinates is treated. The measure is singular; no absolute continuity or Fourier-decay conclusion is asserted. The winding index is a real two-dimensional topological degree, not a holomorphic divisor multiplicity, and high Taylor order must not be conflated with high winding. The uniqueness/novelty comparison is limited to the identified accessible literature; no independent priority or mathematical audit has been performed. The computational checker proves none of the infinite-count assertions by enumeration alone.

## References
1. D. E. Dutkay and P. E. T. Jorgensen, *Fourier frequencies in affine iterated function systems*, arXiv:math/0604547 (first posted 25 April 2006), https://arxiv.org/abs/math/0604547 .
2. J.-L. Chen and W.-H. Ai, *On the spectral properties of a class of planar Sierpinski self-affine measures*, arXiv:2508.20809 (first posted 28 August 2025), https://arxiv.org/abs/2508.20809 .
3. Y. Deng and K.-S. Lau, *Sierpinski-type spectral self-similar measures*, *Journal of Functional Analysis* (2015), DOI 10.1016/j.jfa.2015.06.013. Full text not inspected; abstract-level comparison only.
