# All-rank Fock Ky Fan shape Hessians and their universal spectral edge

## Finding
For each integer \(N\ge2\) and each \(x>0\), the complete second shape variation of the \(N\)-eigenvalue Ky Fan sum of Gaussian Fock localization at a disk diagonalizes in angular Fourier modes. For any real \(h\in C^2(\mathbb T)\) of mean zero, set \(\Omega_\varepsilon=\{r e^{i\theta}:0\le r^2<x+\varepsilon h(\theta)\}\), and let \(\mathcal K_N(\varepsilon)\) be the sum of the \(N\) largest eigenvalues of its localization operator. Then
\[
\lim_{\varepsilon\to0}\frac{\mathcal K_N(0)-\mathcal K_N(\varepsilon)}{\varepsilon^2}=e^{-x}\sum_{k=1}^\infty\Gamma_{N,k}(x)|\widehat h_k|^2,
\]
where \(p_j(x)=x^j/j!\), \(\widehat h_k=(2\pi)^{-1}\int_0^{2\pi}h(\theta)e^{-ik\theta}\,d\theta\), and
\[
\Gamma_{N,k}(x)=p_{N-1}(x)-\sum_{i=\max\{0,N-k\}}^{N-1}\frac{p_i(x)p_{i+k}(x)}{\sum_{j=i+1}^{i+k}p_j(x)}.
\]
In particular, \(\Gamma_{N,1}(x)=0\), all \(\Gamma_{N,k}(x)\ge0\) by the established global disk-optimality theorem, and the quadrupole coefficient is explicitly positive:
\[
\Gamma_{N,2}(x)=p_{N-1}(x)\frac{N+1+2x}{(N+x)(N+1+x)}.
\]
The new rank-dependent effect is a universal balanced-edge limit: for each fixed integer \(k\ge1\),
\[
\lim_{N\to\infty}\frac{N\Gamma_{N,k}(N)}{p_{N-1}(N)}=\frac{k^2-1}{4}.
\]
Thus for each fixed real mean-zero trigonometric polynomial \(h\),
\[
\lim_{N\to\infty}N^{3/2}\lim_{\varepsilon\to0}\frac{\mathcal K_N(0)-\mathcal K_N(\varepsilon)}{\varepsilon^2}\Bigg|_{x=N}
=\frac1{4\sqrt{2\pi}}\sum_{k\ge2}(k^2-1)|\widehat h_k|^2
=\frac1{8\sqrt{2\pi}}\frac1{2\pi}\int_0^{2\pi}\bigl(|h'(\theta)|^2-|h(\theta)|^2\bigr)\,d\theta.
\]
The right-hand side is strictly positive for every such nonzero \(h\) orthogonal to constants and first harmonics. The limiting angular stiffness is the Jacobi multiplier \(k^2-1\), with precisely the translation modes at zero.

## Assumptions and scope
The one-variable complex Bargmann–Fock Hilbert space has norm \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\); the orthonormal basis is \(e_j(z)=z^j/\sqrt{j!}\). Its localization operator \(T_\Omega\) is the positive trace-class Toeplitz compression with indicator symbol \(\mathbf1_\Omega\). For fixed \(x,N,h\), choose real \(|\varepsilon|\) small enough that \(x+\varepsilon h(\theta)>0\). The area \(|\Omega_\varepsilon|=\pi x\) holds exactly because \(h\) has zero mean. No assumed radial symmetry of the perturbed domains is made. The balanced-edge limit keeps the Fourier frequency \(k\) fixed while \(N\to\infty\) and \(x=N\). The final two-limit identity is asserted for fixed trigonometric polynomials only; the \(\varepsilon\)-limit is taken first.

## Proof
**Disk spectral gap.** At the disk, monomials diagonalize the localization operator, with
\[
\lambda_j(x)=\frac1{j!}\int_0^x t^je^{-t}\,dt=1-e^{-x}\sum_{m=0}^j\frac{x^m}{m!},\qquad
\lambda_i-\lambda_j=e^{-x}\sum_{m=i+1}^jp_m(x)\quad(i<j).
\]
Hence \(\lambda_{N-1}>\lambda_N\). The rank-\(N\) spectral projection and its Ky Fan trace therefore vary twice differentiably under the given moving-boundary perturbation. Indeed, in the monomial basis write \(u_{t,\theta,j}=e^{-t/2}t^{j/2}e^{-ij\theta}/\sqrt{j!}\). For every \(t>0\), \(u_{t,\theta}\) has Hilbert norm one and \(T_{\Omega_\varepsilon}=(2\pi)^{-1}\int_0^{2\pi}\int_0^{x+\varepsilon h(\theta)}(u_{t,\theta}\otimes u_{t,\theta}^*)\,dt\,d\theta\). This rank-one Bochner integral is twice differentiable in trace norm: for \(t\) in a fixed compact subinterval of \((0,\infty)\), its integrand and its first \(t\)-derivative are continuous and uniformly bounded in trace norm.

**Exact boundary derivatives.** With \(i,j\ge0\), the matrix element is
\[
\langle T_{\Omega_\varepsilon}e_j,e_i\rangle
=\frac1{2\pi\sqrt{i!j!}}\int_0^{2\pi}e^{i(j-i)\theta}\int_0^{x+\varepsilon h(\theta)}t^{(i+j)/2}e^{-t}\,dt\,d\theta.
\]
Consequently, up to the harmless Fourier-conjugation convention,
\[
\bigl|\langle T'_0e_j,e_i\rangle\bigr|^2
=e^{-2x}p_i(x)p_j(x)|\widehat h_{j-i}|^2,
\quad\langle T''_0e_i,e_i\rangle
=e^{-x}p_i(x)\left(\frac ix-1\right)\frac1{2\pi}\int_0^{2\pi}h^2.
\]
The first derivative of the Ky Fan sum vanishes by \(\widehat h_0=0\). Telescoping \(\sum_{i=0}^{N-1}p_i(i/x-1)=-p_{N-1}\) gives
\[
\sum_{i=0}^{N-1}\langle T''_0e_i,e_i\rangle
=-2e^{-x}p_{N-1}\sum_{k\ge1}|\widehat h_k|^2.
\]

**Second-order spectral response.** For an isolated rank-\(N\) spectral cluster, second-order perturbation of the sum cancels terms internal to that cluster and yields
\[
\mathcal K_N''(0)=\sum_{i=0}^{N-1}\langle T''_0e_i,e_i\rangle
+2\sum_{i=0}^{N-1}\sum_{j=N}^{\infty}
\frac{|\langle T'_0e_j,e_i\rangle|^2}{\lambda_i-\lambda_j}.
\]
Each denominator is at least \(\lambda_{N-1}-\lambda_N>0\), so the series converges by the Hilbert–Schmidt bound on \(T'_0\). Grouping \(j=i+k\) and using Parseval yields \(\mathcal K_N''(0)=-2e^{-x}\sum_{k\ge1}\Gamma_{N,k}|\widehat h_k|^2\), proving the claimed exact Hessian. For \(k=1\) only \(i=N-1\) occurs and its summand equals \(p_{N-1}\), so the coefficient vanishes. For \(k=2\), substituting \(p_{j+1}/p_j=x/(j+1)\) and simplifying gives the displayed quadrupole coefficient. Nonnegativity for other modes also follows directly by applying Abreu's global isoperimetric Ky Fan inequality to \(h(\theta)=\cos(k\theta)\); this known global inequality is not claimed here as new.

**Balanced-edge limit.** Set \(x=N\) and \(b_N=p_{N-1}(N)\). For every fixed integer offset \(s\), ratios of neighboring factorial weights give the uniform finite-offset expansion
\[
\frac{p_{N+s}(N)}{b_N}=1-\frac{s(s+1)}{2N}+O_s(N^{-2}).
\]
For fixed \(k\), put \(a_s=s(s+1)/2\) and write \(i=N-k+u\) for \(0\le u<k\). Expanding the \(k\) crossing terms gives
\[
\frac1{b_N}\sum_{i=N-k}^{N-1}\frac{p_i p_{i+k}}{\sum_{j=i+1}^{i+k}p_j}
=1-\frac1{kN}\sum_{u=0}^{k-1}\left[a_{u-k}+a_u-\frac1k\sum_{s=u-k+1}^{u}a_s\right]+O_k(N^{-2}).
\]
Direct finite summation gives \(\sum_u(a_{u-k}+a_u)=k(k^2-1)/3\) and \(\sum_u k^{-1}\sum_{s=u-k+1}^u a_s=k(k^2-1)/12\), hence the coefficient \((k^2-1)/4\). Finally, Stirling's formula gives \(e^{-N}b_N=e^{-N}N^N/N!\sim(2\pi N)^{-1/2}\). Finite Fourier support allows termwise passage to the displayed rank-edge limit. Parseval proves its equivalent angular Dirichlet form.

## Verification
Run `python3 verify_all_rank.py` with Python, NumPy, and SciPy. On the packaged checker, 474 finite assertions passed. They include exact rational tests of translation cancellation and quadrupole curvature, finite-degree summation identities for the balanced-edge coefficient, direct truncated Fock-matrix eigenvalue second differences, and convergence of factorial-ratio approximations. These numerical truncations do not prove the infinite-dimensional spectral expansion; the proof above uses trace-norm differentiability and spectral perturbation theory.

## Relationship to prior work
Nicola–Riccardi–Tilli (arXiv:2503.07069) optimized partial Toeplitz eigenvalue sums among radial domains, and (arXiv:2607.20965) established existence of unrestricted optimizers. Abreu (arXiv:2607.28376, first public 2026-07-30) subsequently proved the unrestricted global disk inequality for every rank. The present result neither rediscovers nor extends that global inequality. Instead it computes the full nonradial Fourier second variation at **every** rank and its universal balanced large-rank edge limit, which are not specified by the global inequality. Ramos (arXiv:2607.21590) studies local shape variation and rigidity for the **first individual** eigenvalue, and discusses higher eigenvalues separately. A previously known rank-two curvature calculation coincides with the \(N=2\) specialization here; only the general-rank formula and balanced-edge law are asserted as new.

## Limitations
No characterization of all global equality sets is claimed; this remains open in the cited literature. The formula for finite rank is a second-order statement about fixed sufficiently regular area-preserving boundary perturbations, not an all-distances quantitative stability theorem. The balanced-edge limit is for fixed angular frequencies, with the small-deformation limit preceding the rank limit; it does not establish simultaneous uniformity in high angular frequencies. No explicit strict positive lower bound for every finite-rank high Fourier coefficient is asserted beyond the quadrupole formula. Claims of originality are best-knowledge comparisons, not definitive publication-priority or independent mathematical certification.

## References
1. L. D. Abreu, *The isoperimetric inequality for the Ky Fan norm*, arXiv:2607.28376 (first public 2026-07-30), https://arxiv.org/abs/2607.28376.
2. F. Nicola, F. Riccardi, P. Tilli, *On the existence of extremizers for the sum of eigenvalues of Toeplitz operators*, arXiv:2607.20965 (2026), https://arxiv.org/abs/2607.20965.
3. F. Nicola, F. Riccardi, P. Tilli, *The isoperimetric inequality for partial sums of Toeplitz eigenvalues in the Fock space*, arXiv:2503.07069 (2025), https://arxiv.org/abs/2503.07069.
4. J. P. G. Ramos, *Eigenfunctions, Free Boundaries, and Time-Frequency Localization*, arXiv:2607.21590v2 (2026), https://arxiv.org/html/2607.21590v2.
