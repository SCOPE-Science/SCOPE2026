# An arbitrary-order exceptional point with a factorized nonequilibrium Gaussian steady state

## Finding
For every integer \(N\geq 2\), there is a stable nearest-neighbor Ornstein--Uhlenbeck chain with strictly positive, site-dependent trapping and independent thermal noise that simultaneously has an order-\(N\) exceptional point, an exactly factorized standard-Gaussian stationary distribution, and a nonzero stationary probability current. For the explicit family below, the stationary entropy-production rate and the entire time-dependent relative entropy of a natural localized Gaussian perturbation are closed-form expressions.

Write \(m=N-1\), and index sites by \(r=0,\ldots,m\). Choose \(\delta>0\) and \(k>\delta m/2\). Set the real tridiagonal \(N\)-by-\(N\) matrix \(L\) by
\[
L_{rr}=m/2-r,\qquad L_{r,r+1}=\tfrac12\sqrt{(r+1)(m-r)},\qquad L_{r+1,r}=-\tfrac12\sqrt{(r+1)(m-r)}
\]
for \(0\leq r<m\), with all other entries zero. Define \(K=\operatorname{diag}(k-\delta(m/2-r))_{r=0}^{m}\) and \(B=-kI+\delta L\). If \(W_t\) is standard \(N\)-dimensional Brownian motion, then
\[
 dX_t=BX_t\,dt+\sqrt{2K}\,dW_t
\]
has the following properties.

1. \(B\) has characteristic polynomial \((\lambda+k)^N\), minimal polynomial \((\lambda+k)^N\), and a single Jordan block of size \(N\) at \(-k\).
2. Its unique invariant law is \(\varphi_N=\mathcal N(0,I_N)\), a product of \(N\) independent unit-variance Gaussians. Its stationary current is \(J_\infty(x)=\delta Sx\,\varphi_N(x)\), where \(S=(L-L^{\mathsf T})/2\). This current is not identically zero.
3. With entropy production defined by \(\sigma=\int J_\infty(x)^{\mathsf T}K^{-1}J_\infty(x)/\varphi_N(x)\,dx\), the strictly positive result is
\[
 \sigma=\frac{\delta^2}{4}\sum_{i=1}^{N-1} i(N-i)\left(\frac1{k-\delta(m/2-(i-1))}+\frac1{k-\delta(m/2-i)}\right).
\]
4. If \(X_0\) has law \(\mathcal N(e_m,I_N)\), where \(e_m\) is the last coordinate basis vector, then for every \(t\geq0\)
\[
D_{\mathrm{KL}}\big(\mathcal L(X_t)\,\|\,\varphi_N\big)=\frac{e^{-2kt}}2\left[\left(\frac{\delta t}{2}\right)^2+\left(1-\frac{\delta t}{2}\right)^2\right]^{N-1}.
\]
In particular, for fixed \(N\), this equals \(\frac{\delta^{2(N-1)}}{2^N}t^{2(N-1)}e^{-2kt}(1+O(t^{-1}))\) as \(t\to\infty\), and is strictly decreasing for all \(t>0\). For this prescribed family, strict positivity of every local diffusivity is equivalent to the sharp condition \(k>\delta(N-1)/2\).

## Assumptions and scope
There are finitely many sites, \(N\ge2\); \(\delta>0\), \(k>\delta(N-1)/2\); and independent standard Brownian noise acts with site variance rate \(2K_{rr}\). The diffusion matrix and trapping coefficients are coupled as specified, corresponding to unit local fluctuation--dissipation ratios. No homogeneous-trap or equal-noise assumption is made. The current and entropy production use the overdamped Fokker--Planck convention with diffusion matrix \(K\), not \(2K\). The order-\(N\) exceptional point refers to the finite-dimensional drift matrix; no assertion that the entire infinite-dimensional Fokker--Planck generator has a single block is made.

## Proof
**Step 1: The single Jordan chain.** Let \(V=\mathbb R^2\), \(a=\tfrac12\begin{psmallmatrix}1&1\\-1&-1\end{psmallmatrix}\), and \(m=N-1\). Then \(a^2=0\) but \(a\ne0\). On \(V^{\otimes m}\), let \(T\) be the sum of the operators applying \(a\) to exactly one tensor factor. Restrict \(T\) to the symmetric tensor subspace of dimension \(m+1\). In the orthonormal normalized symmetric occupancy basis, ordered by the number \(r\) of second-coordinate factors, its matrix is exactly \(L\): a diagonal contribution \(m/2-r\), a positive transition \(r\to r-1\), and a negative transition \(r\to r+1\) with the displayed square-root factors. Because each tensor factor supports at most one application of \(a\), \(T^{m+1}=0\). But \(T^m e_2^{\otimes m}=m!(ae_2)^{\otimes m}\ne0\). Therefore \(L^{N}=0\ne L^{N-1}\), which in an \(N\)-dimensional space proves that \(L\) has a single nilpotent Jordan block of size \(N\). As \(B=-kI+\delta L\), claim 1 follows.

**Step 2: Stationarity, uniqueness, and current.** The symmetric part of \(L\) is its diagonal \(\operatorname{diag}(m/2-r)\), so \(B+B^{\mathsf T}=-2K\). The positive-definite diagonal matrix \(K\) exists exactly when \(k>\delta m/2\). Thus \(C=I_N\) solves the covariance Lyapunov equation \(BC+CB^{\mathsf T}+2K=0\). Since all eigenvalues of \(B\) equal \(-k<0\), the invariant covariance is unique and all initial laws converge weakly to the centered Gaussian law with covariance \(I_N\). The Fokker--Planck current is \(J=(Bx)\varphi_N-K\nabla\varphi_N=(B+K)x\varphi_N=\delta Sx\varphi_N\). It is nonzero because \(S_{0,1}\ne0\), and its divergence vanishes because \(S\) is skew-symmetric. The density therefore factors into independent scalar Gaussians without satisfying detailed balance.

**Step 3: Entropy production.** For \(Z\sim\mathcal N(0,I_N)\), \(\mathbb E[Z^{\mathsf T}S^{\mathsf T}K^{-1}SZ]=\operatorname{tr}(S^{\mathsf T}K^{-1}S)\). On bond \((i-1,i)\), \(S_{i-1,i}=\frac12\sqrt{i(N-i)}\) and \(S_{i,i-1}=-S_{i-1,i}\). Summing the two weighted squared entries per bond proves the displayed formula and its positivity.

**Step 4: Exact relative entropy.** The covariance of the process remains \(I_N\) when initialized with that covariance. Its mean is \(e^{Bt}e_m\). Two Gaussians with the same covariance \(I_N\) have relative entropy equal to half the squared distance between their means. In the tensor representation above, \(e_m=e_2^{\otimes m}\), while \(e^{\delta ta}e_2=\frac{\delta t}{2}e_1+(1-\frac{\delta t}{2})e_2\). Because the one-factor operations commute, the propagated mean is \(e^{-kt}(e^{\delta ta}e_2)^{\otimes m}\), yielding the exact product norm. The large-time expansion follows from the leading quadratic coefficient in the bracket. Finally, if \(\mu(t)=e^{Bt}e_m\), then \(\frac{d}{dt}\|\mu(t)\|^2=\mu(t)^{\mathsf T}(B+B^{\mathsf T})\mu(t)=-2\mu(t)^{\mathsf T}K\mu(t)<0\), since the matrix exponential is invertible and the initial mean is nonzero. Hence the relative entropy decreases strictly for \(t>0\).

## Verification
Run `python verification/check.py` with SymPy 1.14 or later. Exact symbolic checks for each \(N\in\{2,3,4,5,6,7,8\}\) verify the nilpotency index, the Lyapunov identity, the nonzero current, the entropy-production trace and bond-sum agreement, and the tensor-predicted propagated norm at four rational times. The proof above, rather than those finitely many checks, establishes every stated integer dimension and all admissible real parameters.

## Relationship to prior work
Pal and Gupta (arXiv:2609.05391v1, first posted 2026-09-04) establish order-\(N\) exceptional points in a unidirectionally coupled uniform-trap OU chain, and separately factorized Gaussian nonequilibrium states for antisymmetric couplings. Their full model analysis does not state the simultaneous arbitrary-order exceptional point and factorized invariant law of this heterogeneous trapping-and-noise construction, nor its exact relative-entropy identity. Their disordered dimers have exceptional points but do not yield this connected all-order family. The spin-matrix / symmetric-power method for higher-order exceptional points is **already established**, including the spin-array construction in Du et al. (arXiv:2205.07566v1), and the generic drift--diffusion Lyapunov/exceptional-point separation is established in Rodríguez (arXiv:2601.16121v1). Neither ingredient is presented as novel. The contribution is their concrete simultaneous realization as a strictly dissipative locally thermal OU chain, with exact current, entropy production, and all-time relaxation law. Barrera, Högele and Pardo (arXiv:2009.10590) establish general Jordan-driven polynomial relaxation corrections in small-noise OU thermalization; that covers the asymptotic mechanism, but not this site-resolved all-time KL formula or its irreversible factorized steady-state construction. The possibility that this synthesis or its exact identity appears in unindexed work remains a priority risk.

## Limitations
The construction is deliberately tuned: the diagonal diffusivities match the sitewise restoring coefficients, and the off-diagonal nonreciprocity obeys the square-root spin-chain profile. Arbitrary nonreciprocal or heterogeneous chains need not have either property. The stated positive-diffusion bound is sharp only within this family. The exact KL formula pertains to a unit displacement at the final site and invariant initial covariance, not all starting distributions. Although the drift has an exceptional point, relaxation in the stated KL experiment is monotonically decreasing; the result does not claim transient amplification of this divergence. No robustness under perturbations, nonlinear forces, or infinite-chain limit is established. Independent external validation has not been performed.

## References
- S. K. Pal and S. Gupta, *Non-reciprocally interacting Ornstein-Uhlenbeck processes: Exceptional points, Anomalous relaxation, Pseudo-equilibrium and Boundary refrigeration*, arXiv:2609.05391v1 (2026-09-04), https://arxiv.org/abs/2609.05391.
- Du, Wang, Zhang and Wu, *Light transfer transitions beyond higher-order exceptional points in parity-time and anti-parity-time symmetric waveguide arrays*, arXiv:2205.07566v1 (2022), https://arxiv.org/abs/2205.07566.
- F. E. Quintela Rodríguez, *Exceptional points in Gaussian channels: diffusion gauging and drift-governed spectrum*, arXiv:2601.16121v1 (2026), https://arxiv.org/abs/2601.16121.
- G. Barrera, M. A. Högele, and J. C. Pardo, *Cutoff thermalization for Ornstein--Uhlenbeck systems with small Lévy noise in the Wasserstein distance*, arXiv:2009.10590 (2020), https://arxiv.org/abs/2009.10590.
