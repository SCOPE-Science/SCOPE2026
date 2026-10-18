# Sharp condition-number KL envelope for trace-matched Gaussian inverse covariance

## Finding
Let \(k\ge 2\) be an integer and \(K>1\). For each real symmetric positive-definite \(k\times k\) precision matrix \(B\) of spectral condition number \(\kappa_2(B)=K\), set
\[
 C=B^{-1},\qquad \omega=\frac{\operatorname{tr} C}{k},\qquad
 \mathcal D(B)=D_{\mathrm{KL}}\bigl(\mathcal N(0,\omega I_k)\,\|\,\mathcal N(0,C)\bigr).
\]
Write
\[
 d_K=\frac{K-1}{K},\quad c_K=\frac{(K-1)^2}{K},\quad
 \Phi_K(t)=c_Kt(1-t)-\log(1-d_Kt)-t\log K\quad (0\le t\le1).
\]
**Exact finite-dimensional sharp bound and every equality spectrum:**
\[
 \boxed{\sup_{\kappa_2(B)=K}\mathcal D(B)
 =\frac{k}{2}\max_{1\le m\le k-1}\Phi_K(m/k).}
\]
The supremum is attained. Up to a common positive scalar factor and orthogonal similarity, every maximizing \(B\) has only the two precision eigenvalues \(1\) and \(K\), with multiplicities \(k-m\) and \(m\) for an integer attaining the displayed maximum; and every such spectrum attains equality.

The function \(\Phi_K\) has exactly one maximum \(t_K\in(0,1)\), characterized by
\[
 c_K(1-2t_K)+\frac{d_K}{1-d_Kt_K}=\log K.
\]
The finite-dimensional maximizing integer is one of the valid integers \(\lfloor kt_K\rfloor\) and \(\lceil kt_K\rceil\), with zero or \(k\) excluded; ties are allowed. In the increasing-dimension limit,
\[
 \lim_{k\to\infty}\frac1k\sup_{\kappa_2(B)=K}\mathcal D(B)=\frac12\Phi_K(t_K).
\]
The resulting sharp per-coordinate envelope is asymptotic to \((K-1)^2/16\) as \(K\downarrow1\) and to \(K/8\) as \(K\to\infty\). At fixed \(k\) and \(K\to\infty\), the exact sharp value divided by \(k\) is instead asymptotic to
\[
 \frac{K}{2}\,\frac{\lfloor k^2/4\rfloor}{k^2}.
\]

This inequality is also sharp for the isotropic **uncoupled bulk** of a coupling-corrected one-step Lanczos inverse-covariance construction with a genuinely nonzero Lanczos residual: for every \(B\) as above, the matrix
\[
 A=\begin{pmatrix}1&1/2&0\\[2pt]1/2&5/4&0\\[2pt]0&0&B\end{pmatrix}
\]
with starting Lanczos vector equal to the first coordinate has one-step residual \(1/2\), Schur complement \(\operatorname{diag}(1,B)\), and isotropized bulk \(\omega I_k\). The full Gaussian KL discrepancy of the bulk-isotropized inverse covariance is exactly \(\mathcal D(B)\).

## Assumptions and scope
All matrices are finite-dimensional, real, symmetric and positive definite, with exact arithmetic. The directed divergence has the *approximation* \(\mathcal N(0,\omega I_k)\) as its first argument, and the *exact* \(\mathcal N(0,B^{-1})\) as its second. No assertion is made about the reverse KL divergence or about arbitrary non-isotropic replacements. The scalar \(\omega\) matches the exact covariance trace and is not optimized for this directed KL objective. Scaling \(B\) by any positive constant does not change the divergence, so normalizing the minimum precision eigenvalue to one causes no loss. The construction with \(A\) has dimension \(k+2\), and its one-step Krylov complement has dimension \(k+1\).

## Proof
**Step 1: exact scalar reduction.** Let \(\lambda_1,\ldots,\lambda_k>0\) denote the precision eigenvalues. Define
\[
 a=\frac1k\sum_i\lambda_i,\qquad
 h=\frac1k\sum_i\lambda_i^{-1},\qquad
 \ell=\frac1k\sum_i\log\lambda_i.
\]
The centered-Gaussian divergence formula and \(\omega=h\) yield the exact identity
\[
 \frac{2}{k}\mathcal D(B)=ah-1-\log h-\ell=:F(\lambda_1,\ldots,\lambda_k).
\]
The right side is invariant under multiplying all eigenvalues by the same positive constant. Thus maximize it on the compact cube \([1,K]^k\), which contains all spectra normalized to have condition \(K\).

**Step 2: a strict endpoint principle.** Keeping all eigenvalues except one, \(x=\lambda_i\), fixed, direct differentiation gives
\[
 \frac{\partial F}{\partial x}=\frac1k\left(h-\frac{a-h^{-1}}{x^2}-\frac1x\right),
\]
\[
 \frac{\partial^2 F}{\partial x^2}=
 \frac1k\left[\frac{1-2/k}{x^2}+\frac{1}{kh^2x^4}+\frac{2(a-h^{-1})}{x^3}\right]>0.
\]
Indeed \(k\ge2\), \(h>0\), and the arithmetic-harmonic-mean inequality gives \(a\ge h^{-1}\). Therefore \(F\) is strictly convex in each eigenvalue separately. At any maximizer on \([1,K]^k\), each eigenvalue must be an endpoint. With \(m\) eigenvalues equal to \(K\) and \(k-m\) equal to one, put \(t=m/k\). Elementary substitution yields
\[
 a=1+(K-1)t,\quad h=1-d_Kt,\quad \ell=t\log K,
 \quad ah-1=c_Kt(1-t),
\]
and hence \(F=\Phi_K(t)\). For any \(0<m<k\) the exact covariance is not scalar, so the KL divergence is strictly positive, whereas \(m=0\) and \(m=k\) give zero. Thus the maximizer lies among \(m=1,\ldots,k-1\) and has actual condition number \(K\). Strict coordinate convexity also proves the stated classification of *every* equality spectrum.

**Step 3: unique continuous optimum.** Differentiation gives
\[
 \Phi_K'(t)=c_K(1-2t)+\frac{d_K}{1-d_Kt}-\log K,
 \quad
 \Phi_K^{(3)}(t)=\frac{2d_K^3}{(1-d_Kt)^3}>0.
\]
Moreover,
\[
 \Phi_K'(0)=K-1-\log K>0,\qquad
 \Phi_K'(1)=1-K^{-1}-\log K<0.
\]
Because \(\Phi_K'\) is strictly convex and has opposite endpoint signs, it has one zero in \((0,1)\): a second crossing upward would force the value at one to be positive. Therefore \(\Phi_K\) increases strictly before \(t_K\) and decreases strictly afterwards. On the integer grid the maximum is at an adjacent floor or ceiling, clipped to \(1,\ldots,k-1\).

**Step 4: limiting laws.** Uniform continuity of \(\Phi_K\) on \([0,1]\) gives the dense-grid limit at fixed \(K\). Writing \(K=1+\varepsilon\), Taylor expansion, uniform in \(t\in[0,1]\), gives \(\Phi_K(t)=\tfrac12\varepsilon^2t(1-t)+O(\varepsilon^3)\). The leading maximum is at \(t=1/2\), proving the weak-anisotropy asymptotic. For \(K\to\infty\), the inequality \(0\le-\log(1-d_Kt)\le\log K\) ensures uniform convergence \(\Phi_K(t)/K\to t(1-t)\), yielding \(t_K\to1/2\), the large-\(K\) \(K/8\) per-coordinate law, and the fixed-\(k\) coefficient \(\tfrac12\max_m(m/k)(1-m/k)\).

**Step 5: genuine Lanczos realization.** In the displayed \(A\), the leading \(2\times2\) block is positive definite, and the remaining block is \(B\succ0\), hence \(A\succ0\). Starting with the first unit coordinate \(q_1\), one Lanczos step gives \(q_1^\top A q_1=1\) and nonzero residual \(Aq_1-q_1=(1/2)e_2\). Relative to the resolved coordinate and its complement, the Schur complement is \(S=\operatorname{diag}(1,B)\). The inverse Schur boundary direction is the first vector of that complement; it is orthogonal to the remaining \(k\)-dimensional bulk. The exact inverse covariance on this bulk is \(B^{-1}\), and trace matching replaces it by \(hI_k\) while preserving the leading \(2\times2\) covariance block. Since centered-Gaussian KL divergences add under independent blocks, the full covariance-replacement error equals \(\mathcal D(B)\). Choosing an endpoint extremizer proves sharpness even with nonzero Lanczos coupling.

## Verification
Run `python3 verify.py` with a standard Python 3 installation. It checks the exact multiplicity formula numerically, the strict coordinate derivative against finite differences, sampled interior spectral vectors against the sharp bound, the maximizing discrete multiplicities, and the explicit positive-definite Lanczos realization. These finite checks are supplementary: the endpoint principle and limiting laws are established by the displayed analytical argument.

For example, with \(K=4\) and \(k=10\), the exact maximizing endpoint multiplicity is \(m=4\), giving \(\mathcal D(B)/k\approx0.171078599745\). As \(k\to\infty\), the sharp value per coordinate approaches approximately \(0.172454768108\). The bound \(\tfrac12(K-1)^2\) per coordinate from the motivating literature equals \(4.5\) in this example.

## Relationship to prior work
Fifen, Karambal and Hennig (2026, arXiv:2609.10080v1) introduce the coupling-aware Lanczos inverse-covariance approximation, its trace-matched isotropic bulk, and in Theorem 13 a general sufficient bound \(\mathcal D(B)/k\le\tfrac12(K-1)^2\). These constructions and the ordinary Gaussian divergence formula are not new here. The result proved above instead solves the *exact finite-dimensional optimization under fixed condition number*, identifies all extremal spectra and their multiplicities, and gives a sharp large-condition-number order of \(K\), not the order-\(K^2\) sufficient bound.

Zhang et al. (2021/2023, arXiv:2102.05485) analyze relationships between two directed Gaussian KL divergences and triangle-like comparison bounds; their optimization fixes a KL constraint, not an inverse-covariance condition number and trace-matched scalar approximation. Maze and Wagner (2009/2010, arXiv:0910.0948) establish sharp relationships among arithmetic, geometric and harmonic means when two of those means are prescribed; their theorems do not give the joint fixed-spectral-range optimization of \(ah-1-\log h-\ell\) here. Classical Kantorovich-type bounds control the arithmetic-harmonic product alone; this objective also contains the logarithmic-mean term and its optimum is not generally at equal endpoint multiplicities.

## Limitations
This is an exact arithmetic, real SPD, centered-Gaussian covariance statement, not a convergence or posterior-calibration guarantee for a stochastic numerical algorithm. It assumes the isotropic variance is the *exact* trace average; it does not cover error in estimating this trace, finite precision, non-Gaussian inference, or a bulk with retained off-diagonal couplings. The nonzero-Lanczos-residual realization is a constructed family demonstrating sharpness, not a claim about the spectrum of a general Krylov complement. The mathematical optimization is complete under the stated condition-number constraint, while possible equivalent statements in unindexed spectral-mean literature remain a bibliographic risk.

## References
1. H. Fifen, I. Karambal, P. Hennig, *Stochastic Lanczos Quadrature for Computational Uncertainty in Linear Algebra*, arXiv:2609.10080v1 (posted 2026-09-09), especially Section 4.2 and Theorem 13. https://arxiv.org/html/2609.10080
2. Y. Zhang, W. Liu, Z. Chen, J. Wang, K. Li, *On the Properties of Kullback-Leibler Divergence Between Multivariate Gaussian Distributions*, arXiv:2102.05485 (original 2021; version 5 dated 2023), Sections 2–4. https://arxiv.org/pdf/2102.05485
3. G. Maze, U. Wagner, *A Note on the Weighted Harmonic-Geometric-Arithmetic Means Inequalities*, arXiv:0910.0948, Theorems 1.1–1.2. https://arxiv.org/pdf/0910.0948
