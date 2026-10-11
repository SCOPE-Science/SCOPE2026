# Exact real \(\ell_4\) contraction factors for every four-state cyclic convolution

## Finding
Let \(K\) be any real circulant operator on \(\mathbb R^4\), defined by \((Kx)_j=\sum_{s=0}^3k_sx_{j+s\pmod4}\), and let \(H=\{x\in\mathbb R^4:\sum_jx_j=0\}\). Put \(a=k_0-k_2\), \(c=k_1-k_3\), \(b=k_0-k_1+k_2-k_3\), and \(r^2=a^2+c^2\). On real \(H\) with its inherited \(\ell_4\) norm, the exact fourth power of the induced norm is
\[
\|K|_H\|_{4\to4}^4=\max\left\{|b|^4,\ r^4+a^2c^2+|ac|\sqrt{2r^4+a^2c^2}\right\}.
\]
The formula includes the case \(a=c=0\) by continuity. Furthermore \(\|K|_H\|_{4\to4}\le2^{1/4}\|K|_H\|_{2\to2}\), and the multiplicative constant \(2^{1/4}\) is optimal even for irreducible aperiodic doubly stochastic four-state cyclic Markov kernels: \(K=(I+S)/2\), where \((Sx)_j=x_{j+1\pmod4}\), has \(\|K|_H\|_{4\to4}=2^{-1/4}\) and \(\|K|_H\|_{2\to2}=2^{-1/2}\).

## Assumptions and scope
Coordinates are indexed by \(\mathbb Z/4\mathbb Z\). All spaces, vectors, coefficients, and norms are over the **real** scalar field. The \(\ell_4\) norm is the unnormalized coordinate norm \((\sum_j|x_j|^4)^{1/4}\), whose uniform-probability renormalization makes no difference to an induced norm. Coefficients \(k_0,k_1,k_2,k_3\) are arbitrary real numbers, not necessarily nonnegative or summing to one. The subspace \(H\) is invariant under every circulant. The bound comparing \(\ell_4\) and \(\ell_2\) uses both restrictions to this same \(H\), not full-space matrix norms.

## Proof
Every \(x\in H\) has a **unique** representation
\[
x=(u+w,v-w,-u+w,-v-w),\qquad u,v,w\in\mathbb R.
\]
Direct expansion gives the positive-coefficient identity
\[
\|x\|_4^4=2\bigl(u^4+v^4+6w^2(u^2+v^2)+2w^4\bigr).
\]
The convolution acts on the coordinates as
\[
(u,v,w)\longmapsto(au+cv,-cu+av,bw).
\]
Set \(B=\left(\begin{smallmatrix}a&c\\-c&a\end{smallmatrix}\right)\), \(\rho^2=a^2+c^2\), and \(L=\|B\|_{\ell_4^2\to\ell_4^2}\). Since \(\|Bz\|_2^2=\rho^2\|z\|_2^2\), the same quartic identity yields
\[
\frac12\|Kx\|_4^4=\|B(u,v)\|_4^4+6b^2\rho^2w^2(u^2+v^2)+2b^4w^4.
\]
The elementary inequality \(L\ge\rho\) follows either from the explicit formula below or by averaging the fourth-power quotient over angles. Thus, for \(M=\max\{L,|b|\}\), every one of the three terms in the last expression is bounded above by \(M^4\) times the corresponding input term. This proves \(\|K|_H\|_4\le M\). Conversely, restriction to \(w=0\) attains \(L\), and restriction to \(u=v=0\) attains \(|b|\). Therefore
\[
\|K|_H\|_{4\to4}=\max\{L,|b|\}.
\]
It remains to evaluate \(L\). If \(\rho=0\), then \(L=0\). Otherwise write \(a=\rho\cos\theta\), \(c=\rho\sin\theta\) and parametrize \((u,v)=(\cos t,\sin t)\). The fourth-power quotient is
\[
\frac{\|B(u,v)\|_4^4}{\|(u,v)\|_4^4}=\rho^4\frac{3+\cos(4t-4\theta)}{3+\cos4t}.
\]
For \(\lambda\ge1\), the latter trigonometric ratio is at most \(\lambda\) for all \(t\) exactly when
\[
\sqrt{\lambda^2-2\lambda\cos4\theta+1}\le3(\lambda-1).
\]
Squaring (both sides nonnegative) gives \(8\lambda^2-(18-2\cos4\theta)\lambda+8\ge0\). The sharp \(\lambda\), the larger root, is
\[
\lambda_+=\frac{9-\cos4\theta+\sqrt{(9-\cos4\theta)^2-64}}{8}.
\]
Since \(\cos4\theta=1-8a^2c^2/\rho^4\), this becomes
\[
L^4=\rho^4+a^2c^2+|ac|\sqrt{2\rho^4+a^2c^2}.
\]
This establishes the asserted exact formula for all real coefficient quadruples, including degenerate limits.

The \(\ell_2\) norm of the restriction equals \(\max\{\rho,|b|\}\), because the Fourier decomposition gives one real eigenvalue \(b\) and a real rotation-dilation block with factor \(\rho\). For every \(z\in\mathbb R^2\),
\[
\|Bz\|_4\le\|Bz\|_2=\rho\|z\|_2\le2^{1/4}\rho\|z\|_4,
\]
so \(\|K|_H\|_4\le2^{1/4}\max\{\rho,|b|\}\). At \((k_0,k_1,k_2,k_3)=(1/2,1/2,0,0)\), we have \(a=c=1/2\), \(b=0\), and the formula yields \(L^4=1/2\), whereas \(\rho^2=1/2\). Hence the factor \(2^{1/4}\) is attained. The kernel is a lazy directed four-cycle walk: it is nonnegative, doubly stochastic, irreducible and aperiodic.

## Verification
`verify.py` checks the exact quartic decomposition, the transformed decomposition, the discriminant polynomial identity underlying the radical formula and the rational sharpness witness using symbolic integer/rational arithmetic. The proof of the universal trigonometric supremum and the all-coefficient upper bound is given above; finite tests are not substituted for those arguments. To reproduce, run `python verify.py` with SymPy installed; it prints `VERIFY_OK` if every asserted identity holds.

## Relationship to prior work
The circulant-operator literature studies induced norms, particularly Hilbert-space spectral norms and special equal-off-diagonal circulant families. Bouthat, Khare, Mashreghi and Morneau-Guérin (arXiv:2109.09728), and Sahasranand (arXiv:2111.11389), give general-context results and bounds for matrices with one diagonal coefficient and all off-diagonal coefficients equal; neither provides an arbitrary-real-kernel four-cycle norm on the mean-zero \(\ell_4\) space. A separately available exact \(2\times2\) \(\ell_4\) matrix-norm formula for \(\left(\begin{smallmatrix}a&c\\c&-a\end{smallmatrix}\right)\) supplies the same two-frequency-block value \(L\). The additional claim here is the sharp **three-dimensional Fourier-block gluing identity** for the centered cyclic operator and the optimal Markov spectral-versus-\(\ell_4\) gap; it is not a claim that the two-dimensional radical is new.

## Limitations
This is a four-state **real** result on the centered subspace, not the norm of an arbitrary circulant on all \(\ell_4^4\). The quartic positivity and exact gluing may fail in other exponents, larger cycles or complex scalar spaces. The sharp factor is attained in four states only; no larger-state universal constant is asserted. An unindexed equivalent result may exist despite targeted comparisons.

## References
1. J. W. Zhou and Z. L. Jiang, *Explicit formulae for spectral norms of circulant-type matrices with some given entries*, arXiv:1305.5607v1 (24 May 2013).
2. L. Bouthat, A. Khare, J. Mashreghi and F. Morneau-Guérin, *The \(p\)-norm of circulant matrices*, arXiv:2109.09728v1 (20 September 2021).
3. K. R. Sahasranand, *The \(p\)-norm of circulant matrices via Fourier analysis*, arXiv:2111.11389v1 (22 November 2021).
4. *Exact skew geometric mean constant of \(\ell_4\)*, publicly available mathematical result, record 7a18ef79086d (2026); provides the exact two-dimensional matrix norm used in the comparison.
