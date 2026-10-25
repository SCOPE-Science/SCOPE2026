# Exact angular Hessian of Gaussian Ky Fan concentration around disks

## Finding

Fix an integer \(N\ge1\) and area \(s>0\). For the Bargmann--Fock localization operator \(T_\Omega\), let \(\Sigma_N(\Omega)\) be the sum of its \(N\) largest eigenvalues. Abreu's isoperimetric theorem says \(\Sigma_N(\Omega)\le\Sigma_N(D_s)\) whenever \(|\Omega|=s\), where \(D_s=\{z:\pi|z|^2<s\}\). This result determines the **complete angular second variation** around the disk under exact area preservation.

For any real smooth \(2\pi\)-periodic \(h\) with \(\widehat h_0=0\), set
\[
\Omega_\varepsilon=\{r e^{i\theta}:0\le\pi r^2<s+\varepsilon h(\theta)\},\qquad
\widehat h_m=\frac1{2\pi}\int_0^{2\pi}h(\theta)e^{-im\theta}\,d\theta.
\]
These domains have area exactly \(s\) for all sufficiently small real \(\varepsilon\). Put \(p_j(s)=e^{-s}s^j/j!\) and
\[
\kappa_{N,m}(s)=p_{N-1}(s)-\sum_{j=\max(0,N-m)}^{N-1}
\frac{p_j(s)p_{j+m}(s)}{\sum_{r=j+1}^{j+m}p_r(s)},\qquad m\ge1.
\]
Then
\[
\boxed{\Sigma_N(D_s)-\Sigma_N(\Omega_\varepsilon)=
\varepsilon^2\sum_{m=1}^\infty\kappa_{N,m}(s)|\widehat h_m|^2+o(\varepsilon^2).}
\]
The multipliers satisfy \(\kappa_{N,m}(s)\ge0\) by Abreu's global inequality, \(\kappa_{N,1}(s)=0\), and \(\lim_{m\to\infty}\kappa_{N,m}(s)=p_{N-1}(s)>0\). More sharply,
\[
\boxed{\kappa_{N,2}(s)=\frac{e^{-s}s^{N-1}}{(N-1)!}\frac{N+2s+1}{(N+s)(N+s+1)}>0.}
\]
In particular, the exactly area-preserving elliptic deformation \(h(\theta)=\cos(2\theta)\) has the sharp local deficit
\[
\boxed{\Sigma_N(D_s)-\Sigma_N(\Omega_\varepsilon)=
\frac{e^{-s}s^{N-1}}{4(N-1)!}\frac{N+2s+1}{(N+s)(N+s+1)}\varepsilon^2+o(\varepsilon^2).}
\]

## Assumptions and scope

The Hilbert space consists of entire functions with finite squared norm
\[
\|F\|^2=\int_{\mathbb C}|F(z)|^2e^{-\pi|z|^2}\,dA(z).
\]
The operator is \(T_\Omega F=P(\mathbf 1_\Omega F)\), where \(P\) is the orthogonal projection onto this Hilbert space. The orthonormal basis is \(e_j(z)=(\pi^j/j!)^{1/2}z^j\), \(j\ge0\). For bounded \(\Omega\), \(T_\Omega\) is positive trace class and has trace \(|\Omega|\). The perturbations require real \(h\in C^\infty(\mathbb T)\), \(\widehat h_0=0\), fixed \(N\in\mathbb N\), fixed \(s>0\), and \(|\varepsilon|\|h\|_\infty<s\); the remainder is taken as \(\varepsilon\to0\) with these data fixed.

## Proof

**1. Exact disk spectrum and the spectral gap.** In polar variables \(t=\pi r^2\), direct integration shows
\[
\langle T_{D_s}e_j,e_k\rangle=\delta_{jk}\lambda_j(s),\qquad
\lambda_j(s)=\frac1{j!}\int_0^s t^je^{-t}\,dt
=1-e^{-s}\sum_{r=0}^j\frac{s^r}{r!}.
\]
Thus \(\lambda_j(s)-\lambda_{j+1}(s)=p_{j+1}(s)>0\). In particular, \(\lambda_{N-1}>\lambda_N\), so the first \(N\) eigenvalues remain an isolated analytic spectral cluster under a small perturbation; their sum is twice differentiable.

**2. Trace-class differentiability and matrix entries.** Write \(M_{jk}(\varepsilon)=\langle T_{\Omega_\varepsilon}e_j,e_k\rangle\). An exact polar integration gives
\[
M_{jk}(\varepsilon)=\frac1{2\pi\sqrt{j!k!}}
\int_0^{2\pi}e^{i(j-k)\theta}
\int_0^{s+\varepsilon h(\theta)}t^{(j+k)/2}e^{-t}\,dt\,d\theta.
\]
The coherent-state rank-one projector has trace norm one and varies smoothly in the radial coordinate near \(t=s>0\). Integrating these projectors over the thin moving annulus shows that \(\varepsilon\mapsto T_{\Omega_\varepsilon}\) is twice continuously differentiable in trace norm. Consequently the isolated-cluster differentiation formula applies. Differentiating the displayed matrix entries yields
\[
M_{jk}'(0)=\sqrt{p_j(s)p_k(s)}\,\widehat h_{k-j},
\qquad
M_{jj}''(0)=p_j(s)\bigl(j/s-1\bigr)\frac1{2\pi}\int_0^{2\pi}h(\theta)^2\,d\theta.
\]
The first spectral derivative vanishes, because every diagonal derivative equals \(p_j\widehat h_0=0\).

**3. Second derivative of the Ky Fan eigenvalue sum.** Perturbation of the isolated rank-\(N\) spectral projector gives
\[
\Sigma_N''(0)=\sum_{j=0}^{N-1}M_{jj}''(0)
+2\sum_{j=0}^{N-1}\sum_{k=N}^\infty
\frac{|M_{jk}'(0)|^2}{\lambda_j(s)-\lambda_k(s)}.
\]
There are no terms with both indices inside the rank-\(N\) cluster: their pairwise effects cancel on summation. All displayed denominators are strictly positive and bounded below by \(\lambda_{N-1}-\lambda_N\). The series converges absolutely, since the derivative is trace-class (and \(h\) is smooth).

The Poisson identity \(jp_j(s)/s=p_{j-1}(s)\) for \(j\ge1\) implies the exact telescoping formula
\[
\sum_{j=0}^{N-1}p_j(s)\bigl(j/s-1\bigr)=-p_{N-1}(s).
\]
Moreover \(\lambda_j-\lambda_{j+m}=\sum_{r=j+1}^{j+m}p_r\). Re-index the off-diagonal sum by \(m=k-j\), noting that \(0\le j<N\le j+m\) precisely for \(\max(0,N-m)\le j\le N-1\). Parseval for real mean-zero \(h\) says
\[
\frac1{2\pi}\int_0^{2\pi}h(\theta)^2\,d\theta
=2\sum_{m\ge1}|\widehat h_m|^2.
\]
Substitution gives \(\Sigma_N''(0)=-2\sum_{m\ge1}\kappa_{N,m}(s)|\widehat h_m|^2\), proving the stated expansion, including its exact factor.

**4. Explicit modes and asymptotics.** For \(m=1\), the only boundary-crossing pair is \((N-1,N)\), and its contribution is \(p_{N-1}p_N/p_N=p_{N-1}\); hence \(\kappa_{N,1}=0\). For \(m=2\), the two possible boundary-crossing pairs contribute
\[
\frac{p_{N-1}p_{N+1}}{p_N+p_{N+1}}
=\frac{s}{N+s+1}p_{N-1},\qquad
\frac{p_{N-2}p_N}{p_{N-1}+p_N}
=\frac{N-1}{N+s}p_{N-1}.
\]
For \(N=1\), the second pair is absent and the second expression is zero. Subtracting both from \(p_{N-1}\) gives the boxed closed form. For fixed \(j\in\{0,\ldots,N-1\}\), \(p_{j+m}\to0\) and \(\sum_{r=j+1}^{j+m}p_r\ge p_{j+1}>0\); the at-most-\(N\) crossing terms therefore tend to zero as \(m\to\infty\). Finally, Abreu's isoperimetric inequality holds for every sufficiently small perturbation \(h(\theta)=\cos(m\theta)\), so its quadratic coefficient must be nonnegative; this proves \(\kappa_{N,m}\ge0\) without assuming it from numerical tests.

## Verification

The supplied `CHECK.py` uses exact rational arithmetic to verify the telescoping identity, the translation cancellation, and the algebraic elliptic-mode reduction for many rational positive areas and all tested ranks; running it reports `CHECK_OK`. Independently, finite Fock-matrix quadrature with multiple areas and ranks numerically reproduced the coefficient of the elliptic mode as \(\varepsilon\to0\). The numerical tests are supplementary: the proof above uses exact matrix elements, trace-class spectral perturbation and algebraic identities for all parameters.

## Relationship to prior work

Abreu, *The isoperimetric inequality for the Ky Fan norm* (arXiv:2607.28376v1, first posted 2026-07-30), proves the global maximizing-disk inequality and the exact value of its upper bound using Husimi majorization; its proof does not compute angular second variations or their Fourier multipliers. Nicola–Riccardi–Tilli (arXiv:2503.07069) prove the Ky Fan isoperimetric inequality for radial competitors; they do not consider smooth nonradial elliptic deformations. Gómez–Guerra–Ramos–Tilli (arXiv:2307.09304) establish global quantitative stability for the first eigenvalue with Fraenkel-asymmetry controls; that does not give the displayed exact rank-dependent angular Hessian. Ramos, *Eigenfunctions, free boundaries, and time-frequency localization* (arXiv:2607.21590), proves a local extremal property for the first eigenvalue and separately identifies higher-eigenvalue and Ky Fan questions as future directions; its Section 8.3 does not supply these multipliers. These comparisons do not constitute a proof of absolute historical novelty.

## Limitations

The expansion is local and is not uniform in \(N\), \(s\), the deformation profile, or high-frequency angular directions. It does not classify equality sets of the global isoperimetric inequality for \(N>1\), determine higher-order terms, assert monotonicity or strict positivity of every \(\kappa_{N,m}\) for \(m\ge2\), or establish an optimal global quantitative stability constant. An earlier unindexed local-variation calculation could overlap with the coefficient formula.

## References

1. L. D. Abreu, *The isoperimetric inequality for the Ky Fan norm*, arXiv:2607.28376v1 (2026), https://arxiv.org/abs/2607.28376.
2. F. Nicola, F. Riccardi and P. Tilli, *The isoperimetric inequality for partial sums of Toeplitz eigenvalues in the Fock space*, arXiv:2503.07069v2 (2025), https://arxiv.org/abs/2503.07069.
3. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2307.09304v1 (2023), https://arxiv.org/abs/2307.09304.
4. J. P. G. Ramos, *Eigenfunctions, free boundaries, and time-frequency localization*, arXiv:2607.21590v2 (2026), https://arxiv.org/abs/2607.21590.
