# The quenched sparse-parity transition for random bootstrap walks
## Finding
For each \(\alpha\ge0\), independent Bernoulli coefficients in the inclusion-induced Boolean bootstrap representation are sampled with level-dependent parameter
\[
r_n=2^{-1-\lfloor\alpha n\rfloor}.
\]
The associated pair of simple symmetric walks exhibits a sharp three-phase dichotomy, for almost every fixed coefficient environment: independent Brownian limits when \(\alpha<1/2\), eventually identical increments and a diagonal Brownian limit when \(\alpha>1/2\), and a nonconstant arcsine occupation-time cross-variation at the critical value \(\alpha=1/2\). All assertions hold under the quenched law of the input increments and on any fixed finite time horizon.

Specifically, writing \(Q_n(t)\) for the normalized cross-variation, its critical limiting law at time one is
\[
Q_n(1)\ \Longrightarrow\ \int_0^1\mathbf 1_{\{B_s>0\}}\,ds\ \sim\ \operatorname{Beta}(1/2,1/2),
\]
with mean \(1/2\) and variance \(1/8\). Thus the two-coordinate process has no bivariate Brownian limit at criticality. This assertion does not identify the full two-coordinate critical limiting process.

## Assumptions and scope
Let \((\xi_j)_{j\ge1}\) be iid fair signs. Independently sample all coefficients \((\beta_{n,K})\), with \(n\ge1\) and \(K\subseteq\{1,\ldots,n\}\), each Bernoulli with parameter \(r_n\); all coefficients are mutually independent. Put
\[
X_n=\sum_{j=1}^n\xi_j,\quad \kappa_n=\{j\le n:\xi_j=-1\},\quad N_n=|\kappa_n|=\frac{n-X_n}{2},
\]
\[
\zeta_0=1,\quad
\zeta_n=(-1)^{\sum_{K\subseteq\kappa_n}\beta_{n,K}},\quad
Y_n=\sum_{j=1}^n\zeta_{j-1}\xi_j,\quad
Q_n(t)=\frac1n\sum_{j=1}^{\lfloor nt\rfloor}\zeta_{j-1}.
\]
Write \(\mu\) for the coefficient-environment law and \(\mathbb P^\beta\) for the conditional law of the input signs at fixed coefficients. The theorem means that for every fixed \(\alpha\), a \(\mu\)-probability-one set of environments satisfies the following statements simultaneously for every finite \(T>0\) (equivalently, first for all positive integer \(T\)). Process convergence is weak convergence in the Skorokhod space \(D([0,T],\mathbb R^2)\) or \(D([0,T],\mathbb R^2)\) as appropriate; all limiting paths are continuous.

When \(0\le\alpha<1/2\), \(Q_n\to0\) almost surely uniformly on \([0,T]\) and
\[
n^{-1/2}(X_{\lfloor nt\rfloor},Y_{\lfloor nt\rfloor})\ \Longrightarrow\ (B_t^1,B_t^2),
\]
where \(B^1,B^2\) are independent standard Brownian motions. When \(\alpha>1/2\), almost surely \(\zeta_j=1\) for all sufficiently large \(j\), and the same rescaled pair converges to \((B_t,B_t)\).

At \(\alpha=1/2\),
\[
\sup_{0\le t\le T}\left|Q_n(t)-\frac1n\sum_{j=1}^{\lfloor nt\rfloor}\mathbf1_{\{X_{j-1}>0\}}\right|\longrightarrow0\quad\mathbb P^\beta\text{-almost surely},
\]
and
\[
\left(\frac{X_{\lfloor nt\rfloor}}{\sqrt n},Q_n(t)\right)_{0\le t\le T}
\ \Longrightarrow\ \left(B_t,\int_0^t\mathbf1_{\{B_s>0\}}\,ds\right)_{0\le t\le T}.
\]
The latter limit is not a constant multiple of time; thus the full rescaled pair cannot tend to any bivariate Brownian motion with a deterministic correlation.

## Proof
**1. Exact parity mean and quenched centering.** Fix an entire input-sign sequence. At level \(k\), precisely \(2^{N_k}\) Bernoulli coefficients contribute to the parity; they all have parameter \(r_k\). Therefore their conditional mean is exactly
\[
a_k:=\mathbb E_\mu[\zeta_k\mid\xi_1,\xi_2,\ldots]
=(1-2r_k)^{2^{N_k}}\in[0,1].
\]
Because distinct levels use disjoint independent coefficient families, the random variables \(\zeta_k-a_k\) are independent and centered under \(\mu\) conditional on the signs, uniformly bounded by two in absolute value. Hoeffding's inequality gives, for every \(\varepsilon>0\),
\[
\mathbb P_\mu\!\left(\left|\sum_{k=1}^m(\zeta_k-a_k)\right|>\varepsilon m\ \middle|\ \xi\right)
\le 2\exp(-\varepsilon^2m/8).
\]
The bound is uniform in the sign sequence and summable in \(m\). Conditional Borel--Cantelli, followed by Fubini, yields for \(\mu\)-almost all fixed environments and \(\mathbb P^\beta\)-almost all input paths
\[
\frac1m\sum_{k=1}^m(\zeta_k-a_k)\longrightarrow0.
\tag{1}
\]
The strong law also yields \(N_k/k\to1/2\) on these input paths.

**2. Subcritical independent Brownian pair.** Set \(\lambda_k=2r_k2^{N_k}=2^{N_k-\lfloor\alpha k\rfloor}\). For \(\alpha<1/2\), the strong law gives \(\lambda_k\to\infty\) exponentially. Hence \(0\le a_k\le\exp(-\lambda_k)\to0\). Equation (1) and Cesàro summation prove \(m^{-1}\sum_{k\le m}\zeta_k\to0\), and elementary control of partial sums then gives uniform convergence of \(Q_n\) to zero on every \([0,T]\).

Under any fixed environment, the two-dimensional increment \((\xi_j,\zeta_{j-1}\xi_j)\) is a martingale difference for the sign filtration, with conditional covariance
\[
\begin{pmatrix}1&\zeta_{j-1}\\\zeta_{j-1}&1\end{pmatrix}.
\]
The normalized predictable covariance process converges uniformly to \(tI_2\). Increments are bounded by \(\sqrt{2/n}\); thus the multivariate martingale functional central limit theorem yields two independent standard Brownian limits.

**3. Supercritical eventual coalescence.** For \(\alpha>1/2\), the strong law implies \(\sum_k2^{N_k}r_k<\infty\) along almost every input path: its terms decay exponentially since \(N_k/k\to1/2\). Conditional on such a path, the probability under \(\mu\) that the parity is odd is bounded by the probability of at least one active coefficient, hence by \(2^{N_k}r_k\). Borel--Cantelli and Fubini prove that \(\zeta_k=-1\) occurs only finitely often for almost every environment and almost every input path. Consequently \(Y_n-X_n\) becomes constant; Donsker's theorem proves the diagonal Brownian limit.

**4. Critical occupation-time regime.** For \(\alpha=1/2\), since \(N_k=(k-X_k)/2\),
\[
\lambda_k=2^{N_k-\lfloor k/2\rfloor}
=2^{k/2-\lfloor k/2\rfloor}2^{-X_k/2},
\qquad 2^{-X_k/2}\le\lambda_k\le\sqrt2\,2^{-X_k/2}.
\]
For \(X_k\ge M\), \(1-a_k\le\lambda_k\le\sqrt2\,2^{-M/2}\); for \(X_k\le-M\), \(a_k\le\exp(-\lambda_k)\le\exp(-2^{M/2})\). Thus, for each fixed positive integer \(M\),
\[
\frac1m\sum_{k=1}^m\left|a_k-\mathbf1_{\{X_k>0\}}\right|
\le\frac1m\#\{k\le m:|X_k|\le M\}
+\sqrt2\,2^{-M/2}+e^{-2^{M/2}}.
\tag{2}
\]
For every fixed \(M\), the local central-binomial estimate \(\mathbb P(|X_k|\le M)\le C_M(k+1)^{-1/2}\) gives \(\mathbb E\#\{k\le m:|X_k|\le M\}=O_M(\sqrt m)\). Markov's inequality and Borel--Cantelli on dyadic times, followed by monotonicity of the visit count, prove that the visit fraction in (2) tends almost surely to zero. Then letting \(M\to\infty\) shows
\[
\frac1m\sum_{k=1}^m\left|a_k-\mathbf1_{\{X_k>0\}}\right|\longrightarrow0\qquad\text{almost surely}.
\]
Together with (1), this implies \(m^{-1}\sum_{k\le m}(\zeta_k-\mathbf1_{\{X_k>0\}})\to0\) almost surely. A deterministic partial-sum lemma—if \(s_m/m\to0\), then \(n^{-1}\max_{m\le nT}|s_m|\to0\)—upgrades the conclusion to uniform-in-time convergence. Shifting indices from \(k\) to \(k-1\) changes the normalized sum by at most \(1/n\).

Donsker's theorem and continuity of the occupation-time functional at Brownian paths (whose zero set has zero Lebesgue measure almost surely) yield the asserted joint limit for \((X,Q_n)\). Lévy's arcsine law gives its nondegenerate time-one marginal. Finally, the general bootstrap-walk Brownian criterion requires convergence of the normalized cross-variation to a deterministic constant whenever the two-coordinate limit is a Brownian motion with deterministic covariance. The nonconstant arcsine weak limit excludes this at criticality.

## Verification
A standalone standard-library Python checker, `verify.py`, directly enumerates independent Bernoulli parity configurations, verifies the closed parity-mean identity via a distinct recurrence, checks the binomial mixture representation over all input-sign paths at small times, and verifies exact conditional cross-increment covariances. Run with `python verify.py`. It performs 684 exact-rational assertions in the packaged version. These finite checks do **not** establish the infinite-time phase transition; that follows from the preceding proof, including the quenched Fubini steps and martingale invariance theorem.

## Relationship to prior work
Hamza and Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (1 October 2026), define the inclusion-induced Boolean coefficient representation and prove quenched Brownian normality under a uniform ellipticity assumption on the coefficient probabilities (Section 3, Theorem 2). The exponentially vanishing coefficients considered here are outside that assumption. The result supplies a sharp quenched classification and a critical nonconstant cross-variation in this natural sparse family, not a new classification of arbitrary Boolean representations.

Collevecchio, Hamza, Shi, and Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000 and *Electronic Journal of Probability* **27** (2022), establish the necessary-and-sufficient deterministic cross-variation criterion for Brownian limits (Theorem 6) and investigate deterministic sign-type transforms with non-Gaussian limits (Section 4). This prior criterion and the known Brownian occupation-time law are used here; the new assertion is their realization at the exact sparse random-coefficient threshold, quenched almost surely, along with the two adjacent phases.

## Limitations
The result fixes the explicit level-homogeneous Bernoulli choice \(r_n=2^{-1-\lfloor\alpha n\rfloor}\), a fair input walk, and independence across all coefficients and from the input. It does not classify general coefficient dependence, provide convergence rates, or identify the full joint critical limiting law of \((X,Y)\). The environment-generic assertions are almost sure, not uniform over every coefficient realization. Although targeted comparisons found no covering sparse-threshold theorem, equivalent unpublished or differently indexed results remain a priority risk. No independent audit or external validation is asserted.

## References
1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1, first posted 2026-10-01, https://arxiv.org/html/2610.01658v1 (specifically Sections 2--3 and Appendices).
2. A. Collevecchio, K. Hamza, M. Shi, and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000, https://arxiv.org/html/2010.16000v2; *Electronic Journal of Probability* **27** (2022), Article 92, doi:10.1214/22-EJP818 (especially Theorem 6 and Section 4).
3. Classical results used: Hoeffding concentration; Borel--Cantelli; Donsker's invariance principle; martingale functional central limit theorem; Lévy's arcsine law for Brownian occupation time.
