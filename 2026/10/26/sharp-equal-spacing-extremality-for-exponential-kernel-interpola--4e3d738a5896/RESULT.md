# Sharp equal-spacing extremality for exponential-kernel interpolation matrices

## Finding
For each integer \(n\ge 2\), each length \(\ell>0\), and any distinct ordered sites \(x_1<\dots<x_n\), consider the normalized Matérn-half kernel
\[
K_{ij}=\exp(-|x_i-x_j|/\ell),\qquad 1\le i,j\le n.
\]
Let \(\kappa_2(K)=\lambda_{\max}(K)/\lambda_{\min}(K)\). Both \(\lambda_{\max}(K)\) and \(\lambda_{\max}(K^{-1})\) grow *strictly* when any one adjacent site correlation increases while the other correlations remain fixed. Therefore widening any one adjacent gap strictly improves the spectral condition number.

If \(x_{i+1}-x_i\ge h>0\) for every \(i\), put \(r=\exp(-h/\ell)\in(0,1)\) and let \(T_n(r)=[r^{|i-j|}]_{i,j=1}^n\). The **exact fixed-size sharp inequality** is
\[
\kappa_2(K)\le\kappa_2(T_n(r)),
\]
with equality **if and only if every gap equals \(h\)**. The optimal dimension-free inequality is
\[
\kappa_2(K)<\left(\frac{1+r}{1-r}\right)^2
=\coth^2\left(\frac{h}{2\ell}\right).
\]
The upper endpoint is the exact supremum over all finite cardinalities and all sites satisfying the separation constraint; it is never attained at finite cardinality.

For a target \(\Gamma>1\), a minimum-gap requirement gives \(\kappa_2(K)\le\Gamma\) for *every possible number of sites* **if and only if**
\[
\frac h\ell\ge \log\left(\frac{\sqrt\Gamma+1}{\sqrt\Gamma-1}\right).
\]
This is a sharp separation certificate; the necessity quantifies over arbitrarily large finite configurations on the real line.

## Assumptions and scope
The nodes lie on the entire real line; only an *adjacent minimum gap* is constrained, with no fixed finite container interval or fixed total span. The kernel is the one-dimensional exponential covariance, also called the Matérn kernel with smoothness \(\nu=1/2\), with a common positive length \(\ell\). A common positive multiplicative normalization of the kernel leaves the condition number unchanged. Matrices and spectra are considered in exact real arithmetic. The result does not assert corresponding extremality for Gaussian, higher-order Matérn, or general nonstationary kernels.

## Proof
**1. Gauss–Markov factorization and inverse.** Write \(a_i=\exp(-(x_{i+1}-x_i)/\ell)\in(0,1)\), so that \(K_{ij}=\prod_{k=i}^{j-1}a_k\) for \(i<j\), and \(K_{ii}=1\). Consider the lower triangular matrix \(L\) with \(L_{ij}=0\) for \(i<j\), \(L_{ii}=1\), and \(L_{ij}=\prod_{k=j}^{i-1}a_k\) for \(i>j\). Then
\[
K=L\operatorname{diag}(1,1-a_1^2,\dots,1-a_{n-1}^2)L^{\mathsf T}.
\]
All diagonal innovations are strictly positive, establishing positive definiteness. The inverse \(Q=K^{-1}\) is tridiagonal with
\[
\begin{aligned}
Q_{11}&=\frac1{1-a_1^2},&Q_{nn}&=\frac1{1-a_{n-1}^2},\\
Q_{ii}&=\frac1{1-a_{i-1}^2}+\frac{a_i^2}{1-a_i^2}&&(2\le i\le n-1),\\
Q_{i,i+1}&=Q_{i+1,i}=-\frac{a_i}{1-a_i^2}&&(1\le i<n),
\end{aligned}
\]
with all other entries zero. One can derive this by writing the exact quadratic form \(z^{\mathsf T}Qz=z_1^2+\sum_{i=1}^{n-1}(z_{i+1}-a_i z_i)^2/(1-a_i^2)\). The formulas also cover \(n=2\): the interior-diagonal line is then empty.

**2. Strict monotonicity of both extreme spectral factors.** Every entry of \(K\) is nondecreasing in each \(a_i\), and the entries whose indices straddle gap \(i\) are strictly increasing. The matrix \(K\) has positive entries, so its Perron eigenvector is strictly positive. Comparing Rayleigh quotients at this vector shows that \(\lambda_{\max}(K)\) strictly increases with any \(a_i\).

Let \(D=\operatorname{diag}(1,-1,1,-1,\dots)\). The sign-conjugated inverse \(B=DQD\) has nonnegative entries, positive diagonal, and strictly positive immediate off-diagonals; hence it is irreducible. Its entries are nondecreasing in each \(a_i\): this follows from the strict increase on \((0,1)\) of \(1/(1-a_i^2)\), \(a_i^2/(1-a_i^2)\), and \(a_i/(1-a_i^2)\). At least one entry increases strictly when an \(a_i\) increases. Perron–Frobenius comparison, or the positive Perron eigenvector in the Rayleigh quotient, therefore gives strict increase of \(\lambda_{\max}(B)=\lambda_{\max}(Q)=1/\lambda_{\min}(K)\). Multiplying the two strictly increasing positive factors yields strict increase of \(\kappa_2(K)\) in each \(a_i\), equivalently strict decrease in each adjacent gap.

**3. The fixed-cardinality extremizer.** If every adjacent gap is at least \(h\), then \(0<a_i\le r\). Raising these parameters one at a time to \(r\) cannot lower the condition number, and any strict increase raises it strictly. This yields \(\kappa_2(K)\le\kappa_2(T_n(r))\), with equality exactly when all \(a_i=r\). The latter means \(x_{i+1}-x_i=h\) for every \(i\), determining the set of sites up to translation.

**4. Sharp global constant and strict finite-size inequality.** The Toeplitz coefficients \(r^{|k|}\) have positive Fourier symbol
\[
f_r(\theta)=\sum_{k\in\mathbb Z}r^{|k|}e^{ik\theta}
=\frac{1-r^2}{1-2r\cos\theta+r^2}.
\]
The minimum and maximum are \(f_r(\pi)=(1-r)/(1+r)\) and \(f_r(0)=(1+r)/(1-r)\), respectively. The exact Fourier-integral Rayleigh representation
\[
z^{*}T_n(r)z=\frac1{2\pi}\int_{-\pi}^{\pi}f_r(\theta)\left|\sum_{j=1}^{n}z_j e^{ij\theta}\right|^2d\theta
\]
and Parseval's formula sandwich every eigenvalue between these bounds. For every *nonzero finite* vector \(z\), its nonzero trigonometric polynomial cannot be supported only at a single frequency, making both eigenvalue bounds strict. Therefore every finite \(T_n(r)\) has
\[
\kappa_2(T_n(r))<f_r(0)/f_r(\pi)=((1+r)/(1-r))^2.
\]
The unit constant vector and unit alternating vector give Rayleigh quotients
\[
1+2\sum_{k=1}^{n-1}(1-k/n)r^k\longrightarrow f_r(0),\qquad
1+2\sum_{k=1}^{n-1}(1-k/n)(-r)^k\longrightarrow f_r(\pi),
\]
respectively, as \(n\to\infty\). Combining these with the symbol bounds proves convergence of the extreme eigenvalues to the corresponding symbol edges and hence
\[
\sup_{n\ge2}\kappa_2(T_n(r))=((1+r)/(1-r))^2.
\]
No finite configuration attains this limit.

**5. Optimal separation rule.** Solving \(((1+r)/(1-r))^2\le\Gamma\) for \(r=\exp(-h/\ell)\) gives the stated logarithmic condition. Sufficiency follows from the sharp dimension-free upper bound. If this condition fails, the asymptotic Toeplitz extremizers give a sufficiently large finite equally spaced configuration with \(\kappa_2(K)>\Gamma\), proving necessity.

## Verification
The standalone `check.py` uses exact rational arithmetic to validate the Gauss–Markov precision identity, inverse formulas, and entrywise monotonicity for 1,890 directed gap modifications, plus 52 numerical symmetric-eigenvalue boundary checks. On the finite tested instances it separately verifies strict monotonicity of both extreme eigenvalues and the sharp dimension-free upper bound. These experiments illustrate, and do not substitute for, the all-dimension analytical proof above. Reproduce by running `python check.py` with Python 3.9 or later; no third-party modules are required.

## Relationship to prior work
Avesani–Iske–Multerer–Wenzel (2026), Sections 4.5 and 5.1, identify the ratio of kernel scale to point separation as a driver of stability for multiscale kernel interpolation, proving generally applicable but kernel-dependent upper bounds. Their Proposition 4.10 does not identify finite-size extremizing point configurations or an optimal explicit separation constant. The present result is a sharp specialization for the one-dimensional exponential/Matérn-half kernel; the general separation theory is not claimed as new.

Terenin and collaborators (2022/2024), Section 3.1 and Appendix A, establish existence of dimension-independent kernel stability bounds from separation and decay, not an exact optimal bound or equal-spacing uniqueness for this kernel. The classical work on Kac–Murdock–Szegő matrices, including Fikioris (2018) and Higham's (2021) exposition, supplies the regularly spaced Toeplitz case and its structural inverse. The new statement compares *arbitrary irregular meshes* by strict spectral implication, then identifies the exact universal separation constant. Standard Perron–Frobenius and Toeplitz-symbol facts are used as established inputs.

## Limitations
The extremal geometry is specific to the exponential kernel in one spatial dimension. The sharp dimension-free constant is a supremum over *unbounded numbers of sites and no fixed total span*, not an attained worst instance for a bounded-domain or fixed-extent design. It measures the matrix two-norm condition number, not interpolation error, floating-point backward stability, or the performance of any particular greedy center-selection algorithm. The result has not undergone independent peer review. Standard results on Gaussian Markov covariance and totally positive matrices may contain equivalent earlier specializations; bibliographic priority is not conclusively established by finite searching.

## References
1. S. Avesani, A. Iske, M. Multerer, and T. Wenzel, *Greedy multiscale kernel algorithms*, arXiv:2610.21615v1 (first posted 2026-10-15), especially Sections 4.5 and 5.1. https://arxiv.org/html/2610.21615v1
2. A. Terenin et al., *Numerically Stable Sparse Gaussian Processes via Minimum Separation using Cover Trees*, arXiv:2210.07893, especially Section 3.1 and Appendix A. https://arxiv.org/html/2210.07893v4
3. G. Fikioris, *Spectral properties of Kac–Murdock–Szegő matrices with a complex parameter*, arXiv:1804.08140 (2018). https://arxiv.org/pdf/1804.08140
4. N. J. Higham, *What Is the Kac–Murdock–Szegö Matrix?* (2021). https://nhigham.com/2021/07/06/what-is-the-kac-murdock-szego-matrix/
