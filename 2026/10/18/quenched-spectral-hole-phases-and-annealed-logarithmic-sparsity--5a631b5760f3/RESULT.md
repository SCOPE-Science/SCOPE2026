# Quenched spectral-hole phases and annealed logarithmic sparsity in compound-Poisson grey spherical fields

## Finding
Fix \(c>0\) and \(0<\beta<1\). Let \(T_\beta\) have the positive Mainardi/Mittag-Leffler mixing law characterized by \(\mathbb E e^{-sT_\beta}=E_\beta(-s)\), and let independent unit-jump Poisson subordinators \(H_\ell\) have rates \(c\log(\ell+1)\), for \(\ell\ge1\). Independently take isotropic Gaussian harmonic blocks \(Z_\ell\in\mathbb R^{2\ell+1}\) with covariance \(C_\ell I\), where \(C_\ell=(\ell+1)^{-4}\), and set \(A_\ell=\sqrt{H_\ell(T_\beta)}Z_\ell\). These blocks define a finite-variance, strongly isotropic non-Gaussian spherical random field.

For \(L\ge1\), write \(M_L=\sum_{\ell=1}^{L}\mathbf1_{\{A_\ell=0\}}\) for the number of **completely absent multipoles**, and \(D_L=\sum_{\ell=1}^{L}(2\ell+1)\mathbf1_{\{A_\ell=0\}}\) for their total harmonic multiplicity. The following hold.

1. Conditional on \(T_\beta=t>0\), put \(\theta=ct\). For \(0<\theta<1\), almost surely
   \[M_L\sim\frac{L^{1-\theta}}{1-\theta},\qquad D_L\sim\frac{2L^{2-\theta}}{2-\theta}.\]
   If \(\theta=1\), then \(M_L/\log L\to1\) almost surely, and \(D_L/L\) converges in distribution to twice the standard Dickman variable \(\mathcal D\), whose Laplace transform is
   \[\mathbb E e^{-s(2\mathcal D)}=\exp\left(\int_0^1\frac{e^{-2sx}-1}{x}\,dx\right),\quad s\ge0.\]
   If \(\theta>1\), both counts eventually become constant and finite almost surely. Nevertheless, for \(1<\theta\le2\), the conditional expectation of that finite limiting weighted count is **infinite**. The conditional critical statements also apply to the deterministic-time specialization \(T\equiv1\) with \(c=1\).
2. The observable spectral-hole growth exponent satisfies, almost surely,
   \[\lim_{L\to\infty}\frac{\log(1+M_L)}{\log L}=(1-cT_\beta)_+.\]
   Hence it has a point mass \(\Pr(T_\beta\ge1/c)\in(0,1)\) at zero, and on \(0<u<1\) a density \(c^{-1}M_\beta((1-u)/c)\), where \(M_\beta\) denotes the Mainardi density (not the count \(M_L\)).
3. Despite the random, typically sublinear quenched powers, the unconditional expectations satisfy the sharp, universal logarithmic laws
   \[\mathbb E M_L\sim\frac{L}{c\Gamma(1-\beta)\log L},\qquad
   \mathbb E D_L\sim\frac{L^2}{c\Gamma(1-\beta)\log L}.\]
   In particular, the annealed rates are not obtained by replacing the random exponent by a typical deterministic exponent.

## Assumptions and scope
All Poisson processes, Gaussian blocks, and the mixing time are independent before the common time evaluation. The Poisson processes have unit jumps and strictly positive rates for \(\ell\ge1\). The \(Z_\ell\) are independent Gaussian vectors; conditional on the nonnegative scales, their laws are rotationally invariant within each harmonic irreducible representation. The finite-variance spherical expansion \(\sum_{\ell\ge1}\sum_{m=-\ell}^{\ell}A_{\ell,m}Y_{\ell,m}\) converges in mean square because
\[\sum_{\ell\ge1}(2\ell+1) C_\ell\,\mathbb EH_\ell(T_\beta)
= c\mathbb ET_\beta\sum_{\ell\ge1}(2\ell+1)(\ell+1)^{-4}\log(\ell+1)<\infty.\]
The distribution is an independent-subordinator grey spherical random field of the indicated compound-Poisson type; no pointwise sample continuity is claimed. The source's notation for its deterministic spectral scale need not be identical to the actual covariance spectrum \(C_\ell\mathbb EH_\ell(T_\beta)\). The \(\theta=1\) conditional statement is valid for any deterministic evaluation time \(t=1/c\), including the \(\beta=1\) deterministic-time boundary.

## Proof
**Exact conditional hole law.** Each independent Poisson subordinator obeys \(H_\ell(t)\sim\operatorname{Pois}(ct\log(\ell+1))\). Since a nondegenerate Gaussian vector is almost surely nonzero, a harmonic block vanishes exactly when its Poisson count is zero. Conditional on \(T_\beta=t\), the indicators \(I_\ell=\mathbf1_{\{A_\ell=0\}}\) are independent Bernoulli variables with
\[\Pr(I_\ell=1\mid T_\beta=t)=(\ell+1)^{-ct}.\]
Writing \(\theta=ct\), summation of regularly varying sequences gives the conditional means
\[m_L(t)=\sum_{\ell=1}^{L}(\ell+1)^{-\theta},\qquad d_L(t)=\sum_{\ell=1}^{L}(2\ell+1)(\ell+1)^{-\theta}.\]
For \(0<\theta<1\), these are respectively asymptotic to \(L^{1-\theta}/(1-\theta)\) and \(2L^{2-\theta}/(2-\theta)\).

**Conditional strong laws.** Standard multiplicative Chernoff bounds give \(\Pr(|M_L-m_L|>\varepsilon m_L\mid t)\le2\exp(-C_\varepsilon m_L)\), summable in \(L\) if \(\theta<1\); Borel-Cantelli proves the first strong law. For \(D_L\), summands are independent, bounded by \(2L+1\), and their total variance is at most \((2L+1)d_L\). Bernstein's inequality gives an exponentially small deviation bound on the order \(\exp(-C_\varepsilon L^{1-\theta})\), hence the second strong law. At \(\theta=1\), \(m_L\sim\log L\); apply Chernoff on \(L_j=\lfloor e^{j^2}\rfloor\), where deviation probabilities are summable, and use monotonicity and \(\log L_{j+1}/\log L_j\to1\) to interpolate. At \(\theta>1\), \(\sum_\ell\Pr(I_\ell=1\mid t)<\infty\), so Borel-Cantelli implies only finitely many holes. However, the eventual weighted count has conditional expectation \(\sum_\ell(2\ell+1)(\ell+1)^{-\theta}\), which is infinite exactly for \(\theta\le2\).

**Critical law.** If \(\theta=1\), independence gives, for \(s\ge0\),
\[\mathbb E\big[e^{-sD_L/L}\mid t\big]=\prod_{\ell=1}^L\left[1+\frac{e^{-s(2\ell+1)/L}-1}{\ell+1}\right].\]
Taking logarithms, the sum of quadratic remainders tends to zero: its large-\(\ell\) part is controlled by \(\sum\ell^{-2}\), while the fixed-\(\ell\) part vanishes because its numerator tends to zero. The linear term is a Riemann sum converging to \(\int_0^1(e^{-2sx}-1)dx/x\). Convergence of Laplace transforms proves the stated distributional limit. Its identification as twice a Dickman variable is an established weighted-Bernoulli theorem and is **not** claimed as an independent discovery.

**Random exponent.** For every fixed \(t>0\), the established three conditional regimes give \(\log(1+M_L)/\log L\to(1-ct)_+\). Integrating the conditional probability-one statement yields the almost sure identity under the mixture. The Mainardi density is continuous, positive on \((0,\infty)\), and the affine map \(t\mapsto1-ct\) gives the stated atom and continuous density.

**Annealed logarithmic laws.** The Mainardi mixing representation gives exactly \(\Pr(I_\ell=1)=E_\beta(-c\log(\ell+1))\). Since \(0<\beta<1\), the density at zero is \(M_\beta(0)=1/\Gamma(1-\beta)\); hence its Laplace transform has the sharp large-argument expansion \(E_\beta(-s)\sim1/[s\Gamma(1-\beta)]\). Finally, comparison of sums with integrals yields
\[\sum_{\ell\le L}\frac{1}{\log(\ell+1)}\sim\frac{L}{\log L},\qquad
\sum_{\ell\le L}\frac{2\ell+1}{\log(\ell+1)}\sim\frac{L^2}{\log L}.\]
Substituting the exact absence probabilities proves both annealed asymptotics. These estimates do not require uniform conditional strong laws in the random mixing time.

## Verification
Run the self-contained included `verify.py` with Python 3, SciPy, and its standard library. It checks 481 identities or numerical approximations: exact rational conditional means and variance estimates at integer exponents, the critical weighted-hole Laplace limit, the closed Mittag-Leffler transform for \(\beta=1/2\), and critical first and second moments. The symbolic/probabilistic arguments above, not finite computation, establish the infinite asymptotics.

## Relationship to prior work
Beghin, Leonenko and Marinucci (2026) introduce grey spherical fields and explicitly include independent compound-Poisson subordinators; their full accessible paper develops characteristic functions, moments, high-frequency coefficient limits, and Gaussian comparisons. Those building blocks are treated as known. Greco and Marinucci (2026) study sparsity of isotropic spherical fields and explicitly distinguish dropping entire multipoles from their stronger notion of sparsity; no strong-sparsity claim is made here. Bhattacharjee and Schulte (2022) and earlier Dickman work already establish the critical weighted-Bernoulli limit, which is included here only to explain the boundary regime. The focus of this finding is the **joint almost-sure/annealed phase classification** in the common-Mittag-Leffler-time compound-Poisson spherical model, including the random spectral-hole exponent and the distinct almost-sure and integrability thresholds. Search of related published mathematical result records and these primary full texts did not identify a statement of that combined classification, although general conditional occupancy theory may imply its ingredients.

## Limitations
This theorem analyzes **completely missing harmonic degrees**, not within-degree coefficient sparsity. The logarithmic Poisson rates are selected to expose a natural critical power-law disappearance regime; no optimality among arbitrary rate sequences is claimed. The critical Dickman limit is known as a weighted-Bernoulli result. The random exponent is not an estimator that identifies \(T_\beta\) on the event \(cT_\beta>1\). Scientific priority has not been independently audited. The results do not assert samplewise continuity, general multivariate-dependent-subordinator extensions, or rates of convergence beyond those explicitly proved.

## References
- L. Beghin, N. Leonenko, D. Marinucci, *Grey Random Fields on the Sphere*, arXiv:2610.11806, first public 2026-10-08; especially Sections 3–4 and Appendix A.
- G. Greco, D. Marinucci, *Sparsity for isotropic spherical random fields*, arXiv:2601.21535, first public 2026-01-29; especially Section 1 and Definitions 1.3–1.4.
- C. Bhattacharjee, M. Schulte, *Dickman Approximation of weighted random sums in the Kolmogorov distance*, arXiv:2211.10171, first public 2022-11-18; Section 1 and Theorem 1.1.
- C. Bhattacharjee, L. Goldstein, *Dickman approximation in simulation, summations and perpetuities*, arXiv:1706.08192, first public 2017-06-26.
