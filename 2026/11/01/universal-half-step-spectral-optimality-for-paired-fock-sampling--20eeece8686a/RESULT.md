# Universal half-step spectral optimality for paired Fock sampling rings

## Finding
Let \(N\ge2\), \(r,s>0\), \(\omega=e^{2\pi i/N}\), and \(\delta\in\mathbb R\). Form the \(2N\) normalized reproducing kernels of the analytic Bargmann–Fock space at \(r\omega^k\) and \(s e^{i\delta}\omega^k\), for \(0\le k<N\), and let \(G(\delta)\) be their Hermitian Gram matrix. The half-step staggering \(\delta=\pi/N\) is the unique relative rotation modulo \(2\pi/N\) that simultaneously maximizes the least Gram eigenvalue and determinant and minimizes the greatest eigenvalue, spectral condition number, and every strictly convex spectral penalty \(\operatorname{tr}\varphi(G(\delta))\) for \(\varphi:[0,2N]\to\mathbb R\). Each comparison is strict away from the half-step. The theorem holds also when \(r=s\).

## Assumptions and scope
Use \(\mathcal F^2=\{f\text{ entire}:\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\}\), with reproducing kernel \(K(z,w)=e^{z\overline w}\). Its normalized kernel at \(z\) is \(k_z(w)=\exp(w\overline z-|z|^2/2)\). Gram entries are \(G_{zw}=\exp(\overline z w-(|z|^2+|w|^2)/2)\); the choice of conjugation convention changes no eigenvalues. The spectral condition number means the ratio of the greatest to least eigenvalue if the least is positive and \(+\infty\) when singular. Every eigenvalue lies in \([0,2N]\) because the Gram matrix is positive semidefinite with trace \(2N\). The parameter \(\delta\) is considered modulo \(2\pi/N\), which relabels the second ring.

## Proof
**Step 1: exact Fourier blocks.** With \(m\in\{0,\ldots,N-1\}\), cyclic Fourier transformation independently in the two rings gives a Hermitian \(2\times2\) block \(\begin{psmallmatrix}A_m&C_m(\delta)\\\overline{C_m(\delta)}&B_m\end{psmallmatrix}\), where
\[
\begin{aligned}
A_m&=Ne^{-r^2}\sum_{\ell\ge0}\frac{r^{2(m+N\ell)}}{(m+N\ell)!},\\
B_m&=Ne^{-s^2}\sum_{\ell\ge0}\frac{s^{2(m+N\ell)}}{(m+N\ell)!},\\
C_m(\delta)&=Ne^{-(r^2+s^2)/2}\sum_{\ell\ge0}\frac{(rs)^{m+N\ell}e^{i(m+N\ell)\delta}}{(m+N\ell)!}.
\end{aligned}
\]
Only the modulus of the off-diagonal entry matters. Define \(F_{N,m}(z)=\sum_{\ell\ge0}z^\ell/(N\ell+m)!\). Then \(|C_m(\delta)|=Ne^{-(r^2+s^2)/2}(rs)^m\big|F_{N,m}((rs)^N e^{iN\delta})\big|\).

**Step 2: strict angular minimum of the residue functions.** The Gauss multiplication formula for the Gamma function gives
\[
F_{N,m}(z)=\frac{1}{m!}\;{}_0F_{N-1}\!\left(;\left\{\frac{m+1+j}{N}:0\le j<N,\ j\ne N-m-1\right\};\frac{z}{N^N}\right).
\]
Every displayed denominator parameter is positive. The classical Laguerre–Pólya result for \({}_0F_q(;b;z)\) with positive denominator parameters, explicitly stated by Baricz and Singh, shows that all zeros of \(F_{N,m}\) are real negative. Its growth order is \(1/N<1\). Consequently Hadamard factorization yields \(F_{N,m}(z)=m!^{-1}\prod_{j\ge1}(1+z/x_j)\), with \(x_j>0\) and \(\sum_jx_j^{-1}<\infty\); there is no exponential factor. The function is nonconstant and of order below one, so at least one factor is present. For each fixed \(\rho>0\), each factor has squared modulus \(1+(\rho/x_j)^2+2(\rho/x_j)\cos\theta\) at \(z=\rho e^{i\theta}\). It follows (including zero factors by continuity) that \(|F_{N,m}(\rho e^{i\theta})|\) is uniquely minimized at \(\theta=\pi\pmod{2\pi}\), and is strictly larger at every other angle. Thus every \(|C_m(\delta)|\) is uniquely minimized at \(\delta=\pi/N\pmod{2\pi/N}\), even when \(r=s\).

**Step 3: spectral extremality.** The block eigenvalues are
\[
\lambda_m^{\pm}(\delta)=\frac{A_m+B_m\pm\sqrt{(A_m-B_m)^2+4|C_m(\delta)|^2}}2.
\]
Their sum is independent of \(\delta\), while their gap is strictly minimized at the half-step. Hence the smaller eigenvalue in each block strictly increases and the larger strictly decreases at the half-step relative to every other rotation. Taking the minimum or maximum over finitely many sectors proves the sharp least-eigenvalue and greatest-eigenvalue assertions. Distinct point evaluations in the Fock space are linearly independent (polynomial interpolation on the finite set); hence the half-step Gram matrix is positive definite. Condition-number optimality follows from the simultaneous extremal eigenvalues. The block determinants \(A_mB_m-|C_m(\delta)|^2\) are strictly maximized at the half-step and positive there; their product is \(\det G(\delta)\). Finally, every strictly convex \(\varphi\) satisfies \(\varphi(\lambda_m^-(\pi/N))+\varphi(\lambda_m^+(\pi/N))<\varphi(\lambda_m^-(\delta))+\varphi(\lambda_m^+(\delta))\) away from the half-step, by fixed-sum two-point convexity. Summing over all sectors gives the asserted strict universal convex spectral optimum.

## Verification
The accompanying standalone `verify.py` computes the exact cyclic-sector series numerically, independently builds the \(2N\)-point Gram matrix and diagonalizes it, and tests the rotation inequalities across \(N=2,\ldots,8\), multiple distinct and equal positive radii, and seven comparison angles. It passed 448 finite assertions. These finite experiments check formulas and examples, not the infinite hypergeometric-zero theorem, for which the cited analytic result and Hadamard argument are essential.

## Relationship to prior work
Aadi and Omari (first public July 21, 2022) treat stability and zero/uniqueness sets in analytic Fock spaces, a different infinite-set question. Marwah and Lütkenhaus (2018) characterize which matrices arise as coherent-state Gram matrices, without the two-ring angular optimization established here. Baricz and Singh (2017) explicitly record the negative-real-zero property of \({}_0F_q\) with positive denominator parameters, which is a **prior ingredient**, not a new assertion. An existing Hardy/Szegő two-circle kernel theorem shows an analogous half-step optimality but neither supplies the factorial-coefficient Fock block estimates nor the all-convex-functional claim here. The present claim does not assign novelty to standard reproducing-kernel, Fourier, or hypergeometric facts.

## Limitations
Only one-variable Gaussian analytic Fock space, two equal-size regularly spaced cyclic rings, fixed positive radii, and relative angular staggering are treated. Arbitrary irregular arrays, more than two rings, and weighted non-Gaussian Fock spaces are not included. No quantitative perturbation stability for nonregular arrays is asserted. Historical-priority uncertainty remains, particularly for other cyclic coherent-state or Gaussian radial-basis interpolation literature. No independent audit or validation has been performed.

## References
1. D. Aadi and Y. Omari, *Zero and uniqueness sets for Fock spaces*, arXiv:2207.10601, first posted 2022-07-21. https://arxiv.org/abs/2207.10601
2. A. S. Marwah and N. Lütkenhaus, *Characterization of Gram matrices of multi-mode coherent states*, arXiv:1809.05187, first posted 2018-09-13. https://arxiv.org/abs/1809.05187
3. Á. Baricz and S. Singh, *Zeros of some special entire functions*, arXiv:1702.00626, first posted 2017-02-02; see the observation after Theorem 2 concerning \({}_0F_q\). https://arxiv.org/abs/1702.00626
