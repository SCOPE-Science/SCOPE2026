# Sharp exponential minimax interpolation cost on expanding Fock circles

## Finding

Let \(\mathcal F^2\) be the standard analytic Bargmann–Fock space, with
\[\|f\|_{\mathcal F}^2=\sum_{k=0}^\infty k!|a_k|^2,\qquad f(z)=\sum_{k=0}^\infty a_kz^k.\]
Fix \(\rho>0\). For each integer \(N\ge2\), set \(r_N=\sqrt{\rho N}\) and \(z_j=r_Ne^{2\pi i j/N}\) for \(0\le j<N\), and consider the normalized point-sampling operator
\[S_Nf=(e^{-\rho N/2}f(z_j))_{j=0}^{N-1}\]
with range norm \(\|y\|_N^2=N^{-1}\sum_j|y_j|^2\). This operator is onto. Its squared optimal interpolation amplification is
\[Q_N(\rho)=\sup_{\|y\|_N=1}\inf_{S_Nf=y}\|f\|_{\mathcal F}^2=\|S_N^\dagger\|^2.\]
The exact finite formula is
\[Q_N(\rho)=\left[\min_{0\le m<N}\left\{e^{-\rho N}\sum_{\ell\ge0}\frac{(\rho N)^{m+\ell N}}{(m+\ell N)!}\right\}\right]^{-1}.\]
This exact Fourier/Poisson-residue formula is classical (not claimed as new); the contribution is the **sharp minimax large-\(N\) law, its universal transition, and worst-harmonic localization** below.

For \(x\ge0\) define the Poisson rate function by
\[J_\rho(x)=x\log(x/\rho)-x+\rho,\qquad J_\rho(0)=\rho.\]
Define the strictly increasing identric-mean function
\[B(x)=e^{-1}\frac{(x+1)^{x+1}}{x^x}\quad(x>0),\qquad B(0)=e^{-1}.\]
For \(\rho>e^{-1}\), there is exactly one \(x_\rho>0\) with \(B(x_\rho)=\rho\). Put
\[M(\rho)=\begin{cases}\rho-1-\log\rho,&0<\rho\le e^{-1},\\J_\rho(x_\rho),&\rho>e^{-1}.\end{cases}\]

**Theorem.** For each fixed \(\rho>0\) there exist \(0<c_\rho<C_\rho<\infty\) and \(N_\rho\) such that, for every integer \(N\ge N_\rho\),
\[c_\rho\sqrt N\,e^{NM(\rho)}\le Q_N(\rho)\le C_\rho\sqrt N\,e^{NM(\rho)}.\]
In particular,
\[\lim_{N\to\infty}\frac{\log Q_N(\rho)-\frac12\log N}{N}=M(\rho)>0.\]
The regime changes **exactly** at \(\rho=e^{-1}\). More precisely, let \(m_N\) be any minimizing Fourier residue in the exact formula. If \(0<\rho<e^{-1}\), then \(m_N/N\to1\). If \(\rho>e^{-1}\) and \(x_\rho\notin\mathbb Z\), then \(m_N/N\to\{x_\rho\}\). If \(\rho>e^{-1}\) and \(x_\rho\in\mathbb Z\), then \(\min(m_N/N,1-m_N/N)\to0\). At \(\rho=e^{-1}\), all limiting residues are in \(\{0,1\}\). Finally,
\[M(\rho)=\frac1{8\rho}+O(\rho^{-2})\quad\text{as }\rho\to\infty.\]
Here \(\{x\}\) denotes the fractional part.

## Assumptions and scope

The Fock kernel is \(K(z,w)=e^{z\overline w}\). The Hilbert norm on the data space includes the factor \(1/N\), and each point evaluation is normalized by \(e^{-|z_j|^2/2}\); both normalizations are essential to the displayed constants. The parameter \(\rho>0\) is held fixed while \(N\to\infty\). Constants in the two-sided estimate need not be uniform in \(\rho\), notably near \(e^{-1}\) or other discrete identric values. All logarithms are natural. The finding concerns finite regular polygons expanding at squared radius \(\rho N\), not infinite interpolation sets or arbitrary perturbations of the sampling nodes.

## Proof

**1. Exact singular values and extremizing data.** Let \(\omega=e^{2\pi i/N}\). The normalized kernel vectors at the nodes have Gram entries
\[G_{ij}=e^{-\rho N}\exp(\rho N\omega^{i-j}).\]
The matrix is circulant. Fourier expansion of its exponential shows that the eigenvalue of \(G/N=S_NS_N^*\), acting in the data norm, in Fourier mode \(y_j=\omega^{mj}\) is
\[p_{N,m}=e^{-\rho N}\sum_{\ell\ge0}\frac{(\rho N)^{m+\ell N}}{(m+\ell N)!}>0.\]
Since every eigenvalue is positive, \(S_N\) is onto and its Moore–Penrose right inverse has squared norm \(1/\min_m p_{N,m}\). Every minimizing Fourier mode is worst-case data. Its explicit minimum-norm interpolant is
\[f_{N,m}(z)=\frac{e^{\rho N/2}}{A_{N,m}}\sum_{\ell\ge0}\frac{(r_Nz)^{m+\ell N}}{(m+\ell N)!},\quad A_{N,m}=\sum_{\ell\ge0}\frac{(\rho N)^{m+\ell N}}{(m+\ell N)!}.\]
Direct substitution and coefficient orthogonality give \(S_Nf_{N,m}=y\) and \(\|f_{N,m}\|^2=1/p_{N,m}\).

**2. Rate of each residue.** Write \(t=m/N\in[0,1)\), and set
\[F_\rho(t)=\min_{\ell\ge0}J_\rho(t+\ell).\]
Stirling's inequalities, uniformly for \(k\) in any bounded multiple of \(N\), give the Poisson mass
\[e^{-\rho N}\frac{(\rho N)^k}{k!}=\Theta_\rho\!\bigl(N^{-1/2}e^{-NJ_\rho(k/N)}\bigr)\quad\text{when }k/N\ge\eta>0,\]
while at \(k=0\) it equals \(e^{-\rho N}\). A bounded set of aliases suffices uniformly for the exponential minimum: choose \(L_\rho>\rho+2\) so large that \(J_\rho(x)\) exceeds every \(F_\rho(t)\) by at least two when \(x\ge L_\rho\); the Poisson tail from \(k\ge L_\rho N\) is bounded geometrically using consecutive mass ratios. Consequently
\[\frac1N\log p_{N,m}=-F_\rho(m/N)+O_\rho(\log N/N)\]
uniformly in \(m\). The comparison is valid at \(m=0\) because its zero-index mass is handled separately. More sharply, choosing a minimizing alias and applying the one-sided Stirling bound yields, uniformly for all residues,
\[p_{N,m}\ge c_\rho N^{-1/2}\exp[-NF_\rho(m/N)].\]

**3. Exact phase optimization.** The adjacent-alias difference satisfies
\[J_\rho(x+1)-J_\rho(x)=\log\frac{B(x)}\rho,\quad \log B(x)=\int_x^{x+1}\log u\,du.\]
Thus \(B\) increases strictly on \([0,\infty)\), with \(B(0)=e^{-1}\), and \(x<B(x)<x+1\) for \(x>0\). If \(\rho\le e^{-1}\), all alias differences are nonnegative. Hence \(F_\rho(t)=J_\rho(t)\) on \([0,1]\), and strict convexity of \(J_\rho\) makes its maximum the larger of its endpoint values \(J_\rho(0)=\rho\), \(J_\rho(1)=\rho-1-\log\rho\). The latter is larger for \(\rho<e^{-1}\), with equality at the threshold.

If \(\rho>e^{-1}\), the unique \(x_\rho\) satisfies \(J_\rho(x_\rho)=J_\rho(x_\rho+1)\). Write \(x_\rho=L+\delta\), with integer \(L\ge0\) and \(0\le\delta<1\). At \(t=\delta\), the two consecutive aliases \(L+\delta\) and \(L+1+\delta\) have the same rate \(M=J_\rho(x_\rho)\) and every other admissible alias has strictly greater rate. At any \(t\ne\delta\), interpreted cyclically, the lattice \(t+\mathbb N_0\) has an admissible point strictly between \(x_\rho\) and \(x_\rho+1\), whose rate is strictly less than \(M\) by strict convexity. Therefore the unique maximizing fractional residue is \(\delta\) (with the two ends identified when \(\delta=0\)), and the maximal rate is \(M\). This also proves \(M>0\), since \(x_\rho<\rho<x_\rho+1\).

**4. Sharp prefactor.** The uniform lower bound in step 2 and \(F_\rho(t)\le M\) imply
\[\min_m p_{N,m}\ge c_\rho N^{-1/2}e^{-NM}.\]
For the reverse inequality, choose \(m_N=N-1\) when \(\rho\le e^{-1}\). Otherwise select a residue within distance \(1/N\) of \(\delta\), using \(m_N=N-1\) when \(\delta=0\). In every case the competing aliases at this residue converge to one or both strictly positive arguments that realize \(M\), and their rates differ from \(M\) by \(O_\rho(1/N)\). Stirling's upper estimate makes their total probability at most \(C_\rho N^{-1/2}e^{-NM}\). All other aliases lie at a fixed positive rate gap from \(M\), so their entire tail obeys the same bound. Therefore
\[\min_m p_{N,m}\le C_\rho N^{-1/2}e^{-NM},\]
which gives the two-sided minimax estimate after inversion. Uniform logarithmic convergence in step 2 and the strict maximizer classification in step 3 force the stated localization for **any** minimizing-residue sequence.

**5. Large-radius rate.** Taylor expansion of the logarithmic integral gives
\[\log B(x)=\log(x+\tfrac12)-\frac1{24(x+\tfrac12)^2}+O(x^{-4}).\]
Thus \(x_\rho=\rho-\tfrac12+O(\rho^{-1})\) and insertion into \(J_\rho\) gives \(M(\rho)=1/(8\rho)+O(\rho^{-2})\).

## Verification

The finite identity is independently checkable by evaluating the circulant normalized Gram matrix and comparing its Fourier eigenvalues to positive Poisson congruence sums. The included standard-library checker performs these finite comparisons at several \(N\) and \(\rho\) values, and verifies the rate optimization numerically. Its diagnostics are supplementary: the infinite-dimensional Fock interpolation identity and asymptotic conclusions rest on the proof above, not on finite computation. The stand-alone checker may be run as `python3 checks/fock_circle_check.py` from the extracted package root.

## Relationship to prior work

Alpay, De Martino, and Diki (2026) study complex representer theorems and interpolation/minimization in Fock and Hardy RKHSs, including superoscillations; their original April 24 preprint motivates the minimum-norm interpolation viewpoint. Horoshko, De Bièvre, Kolobov, and Patera (2016) already diagonalize the Gram matrix of equally spaced coherent states and identify the same Poisson residue probabilities in their equation (9): that exact Fourier spectral identity is **not** claimed as new. Their analysis concerns quantum circular-state entanglement rather than the sharply optimized least eigenvalue as both the number and circle radius grow together. Seip's classical Fock interpolation theory concerns density of infinite sets and does not state this finite-polygon double-scaling law. The 2024 paper *Optimal circular states* discusses a related coherent-state family; only bibliographic material and a first-page preview were available for inspection, so its deeper contents remain an explicit priority risk. The contribution isolated here is the uniform \(\sqrt N\)-prefactor order, the explicit identric-mean variational rate, the exact \(e^{-1}\) threshold and the limiting worst Fourier harmonics.

## Limitations

The asymptotic estimate is for each fixed \(\rho>0\); no uniform crossover window \(\rho=\rho_N\) approaching the critical threshold is proved. No claim is made about irregular configurations, higher-dimensional Fock spaces, interpolation under node perturbations, or the exact multiplicative asymptotic constant. The Poisson-residue diagonalization and generic kernel representer theorem are known. An inaccessible related 2024 primary work may contain an equivalent minimax theorem; a literature search cannot establish historical uniqueness.

## References

1. N. Alpay, A. De Martino, K. Diki, *Representer Theorem in Complex Reproducing Kernel Hilbert Spaces with Applications to Fock and Hardy Spaces and Superoscillations*, arXiv:2604.22165v1, first posted April 24, 2026. https://arxiv.org/abs/2604.22165
2. D. B. Horoshko, S. De Bièvre, M. I. Kolobov, G. Patera, *Entanglement of quantum circular states of light*, arXiv:1602.07852, especially the Fourier/Poisson decomposition in equation (9). https://arxiv.org/abs/1602.07852
3. K. Seip, *Density theorems for sampling and interpolation in the Bargmann–Fock space*, 1992, arXiv:math/9204238. https://arxiv.org/abs/math/9204238
4. S. Luo, S. Tang, Y. Zhang, *Optimal circular states*, Journal of Physics A (2024), DOI:10.1088/1751-8121/ad8792; full text not inspected.
