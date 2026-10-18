# Unimodular logarithmic phase transitions in weighted Bergman moments

## Finding
Fix \(\alpha>-1\), write \(a=\alpha+1>0\), and consider the standard weighted analytic Bergman space on the disk. For every fixed \(0<\tau<2\), define the bounded, unimodular radial symbol
\[
\Phi_\tau(z)=\exp\!\left(i\left[\log\frac{1}{1-|z|^2}\right]^\tau\right),\qquad z\in\mathbb D,
\]
and let \(T_\tau=P_\alpha M_{\Phi_\tau}\). The normalized monomials are eigenvectors, with eigenvalues
\[
\lambda_n(\tau)=\frac{1}{B(n+1,a)}\int_0^1t^n(1-t)^{a-1}\exp\!\left(i\left[\log\frac1{1-t}\right]^\tau\right)dt.
\]
Put \(L_n=\log n\) for \(n\ge2\) and \(\kappa_n=\tau L_n^{\tau-1}\). The following three regimes hold, with limits for fixed \(a,\tau\):

**Subcritical phase, \(0<\tau<1\):**
\[
\lambda_n(\tau)=e^{iL_n^\tau}(1+o(1)),\qquad
\sigma_{\mathrm{ess}}(T_\tau)=\{z\in\mathbb C:|z|=1\}.
\]
**Critical phase, \(\tau=1\):**
\[
\lambda_n(1)=\frac{\Gamma(a-i)}{\Gamma(a)}n^i(1+O_a(n^{-1})),\qquad
\sigma_{\mathrm{ess}}(T_1)=\left\{z:|z|=\frac{|\Gamma(a-i)|}{\Gamma(a)}\right\}.
\]
The critical radius is strictly between zero and one.

**Supercritical logarithmic phase, \(1<\tau<2\):**
\[
\boxed{\lambda_n(\tau)=e^{iL_n^\tau}\frac{\Gamma(a-i\kappa_n)}{\Gamma(a)}(1+o(1)).}
\]
In particular,
\[
|\lambda_n(\tau)|=\frac{\sqrt{2\pi}}{\Gamma(a)}\kappa_n^{a-1/2}e^{-\pi\kappa_n/2}(1+o(1)),\qquad
\lim_{n\to\infty}\frac{\log|\lambda_n(\tau)|}{(\log n)^{\tau-1}}=-\frac{\pi\tau}{2}.
\]
Thus \(T_\tau\) is compact, has essential spectrum \(\{0\}\), but is in **no** finite Schatten class \(\mathcal S_q\), \(q>0\). In the compact regime, define \(N_\tau(s)=\#\{n\ge0:|\lambda_n(\tau)|>s\}\). Its exact logarithmic counting rate is
\[
\lim_{s\downarrow0}\frac{\log N_\tau(s)}{(\log(1/s))^{1/(\tau-1)}}=\left(\frac{2}{\pi\tau}\right)^{1/(\tau-1)}.
\]
The three regimes produce a genuine compactness transition for symbols of modulus exactly one, and a separate jump in the radius of the essential-spectrum circle at the critical exponent.

## Assumptions and scope
The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). The area measure \(dA\) is ordinary planar Lebesgue measure, and the norm on \(A^2_\alpha\) comes from the probability measure \(a(1-|z|^2)^{a-1}dA(z)/\pi\). The projection \(P_\alpha\) is its orthogonal analytic Bergman projection. The phase exponent satisfies \(0<\tau<2\) and is held fixed while the monomial degree tends to infinity. The value at the disk center is obtained by continuous extension. All logarithms used for positive real arguments are ordinary real logarithms; complex logarithms in the proof use the branch on the right half-plane. The claim concerns only this explicit family of bounded radial symbols and standard power weights; it does not address arbitrary radial weights, other exponents, or nonradial operators.

## Proof
**1. Diagonalization and beta-law reduction.** Rotation invariance makes \(T_\tau\) diagonal on the orthogonal monomials, and their squared norms are \(aB(n+1,a)\). The displayed integral follows. With \(x=n(1-t)\), write \(L=\log n\). Standard beta-integral estimates yield
\[
\lambda_n(\tau)=\frac1{\Gamma(a)}\int_0^{e^{L/2}}x^{a-1}e^{-x}e^{i(L-\log x)^\tau}\,dx+O_a(n^{-1})+O_a(e^{-c\sqrt n}),
\]
where the phase on this interval is real, \(c>0\) is fixed, and the errors are absolute and uniform in the unimodular phase. To verify the bound, use \(|(1-x/n)^n-e^{-x}|\le Cn^{-1}x^2e^{-x/2}\) for \(0\le x\le n/2\), dominate the remaining real tails exponentially, and use \(n^aB(n+1,a)=\Gamma(a)(1+O_a(n^{-1}))\).

**2. The two noncompact regimes.** Let \(X\) have the \(\Gamma(a,1)\) distribution. For each fixed \(X>0\),
\[
(L-\log X)^\tau-L^\tau\longrightarrow0\quad\text{when }0<\tau<1.
\]
Dominated convergence in the beta-law reduction proves the subcritical eigenvalue formula. For \(\tau=1\), evaluation gives exactly
\[
\lambda_n(1)=\frac{B(n+1,a-i)}{B(n+1,a)}
=\frac{\Gamma(a-i)}{\Gamma(a)}\frac{\Gamma(n+a+1)}{\Gamma(n+a+1-i)}.
\]
The gamma-ratio asymptotic gives the critical formula. The strict bound \(|\Gamma(a-i)|<\Gamma(a)\) follows from the strict triangle inequality for the nonconstant character \(X^{-i}\) of a non-atomic gamma law. In either noncompact regime the arguments of the leading eigenvalues advance without bound, but the increment between consecutive arguments tends to zero. Consequently their cluster sets, hence their diagonal essential spectra, are precisely the circles asserted above.

**3. Complex Mellin stationary phase for \(1<\tau<2\).** Define \(\kappa=\tau L^{\tau-1}\), \(R=e^{L/2}\), and
\[
I_L=\int_0^R x^{a-1}e^{-x}e^{i(L-\log x)^\tau}\,dx.
\]
We prove the precise comparison
\[
I_L=e^{iL^\tau}\Gamma(a-i\kappa)(1+o(1)).\tag{1}
\]
Rotate the contour through the lower-right quadrant to \(x=re^{-i\theta}\), where \(\theta=\arctan(\kappa/a)\). On the sector \(0<|x|\le R\), the real part of \(L-\log x\) is at least \(L/2\), so the principal \(\tau\)-power is holomorphic. Its imaginary part is nonnegative, hence the exponential phase has modulus at most one. The small circular arc contributes zero because \(a>0\); the outer arc contributes at most a polynomial in \(R\) times \(e^{-R\cos\theta}\), which is negligible because \(R\cos\theta\to\infty\).

Writing \(r=\kappa u\) and
\[
E_L(x)=(L-\log x)^\tau-L^\tau+\kappa\log x,
\]
the rotated integral is exactly
\[
I_L=e^{iL^\tau-\kappa\theta-i a\theta-i\kappa\log\kappa}\kappa^a
\int_0^{R/\kappa}u^{a-1}e^{-\kappa u\cos\theta}
 e^{i\kappa(u\sin\theta-\log u)}e^{iE_L(\kappa u e^{-i\theta})}\,du.
\]
For any fixed \(M>\max\{1,1/(2a)\}\), the very-small range \(0<u<\kappa^{-M}\) contributes \(o(\kappa^{-1/2})\) to the displayed integral: there \(|\kappa u e^{-i\theta}|<1\), and its original phase has modulus at most the linearized phase factor \(e^{-\kappa\theta}\). The large range \(u>\kappa^2\) is exponentially negligible even allowing the factor \(e^{\kappa\theta}\), because \(\kappa\cos\theta\to a>0\). On the intervening range the Taylor expansion, together with its first two derivatives on compact positive \(u\)-sets, gives
\[
E_L(\kappa u e^{-i\theta})=O_{a,\tau,M}\bigl(L^{\tau-2}(\log\kappa)^2\bigr)=o(1).
\]
The real phase \(\psi(u)=u\sin\theta-\log u\) has the unique nondegenerate critical point \(u_*=(\sin\theta)^{-1}\), with \(\psi''(u_*)=\sin^2\theta\). Outside a fixed neighborhood of that point, integration by parts gives \(O(\kappa^{-1})\): near zero use \(u\psi'(u)\to-1\) and \(a>0\), while at infinity use the exponential amplitude \(e^{-(a+o(1))u}\). In that neighborhood stationary phase, with the vanishing Taylor perturbation, yields
\[
\int_0^{R/\kappa}\cdots du
=e^{i\kappa(1+\log\sin\theta)+i\pi/4}
\left(\frac{2\pi}{\kappa}\right)^{1/2}(\sin\theta)^{-a}e^{-\kappa\cot\theta}(1+o(1)).
\]
Here \(\kappa\cot\theta=a\), \(\kappa(\pi/2-\theta)\to a\), and \(\kappa\log\sin\theta\to0\). Substitution gives
\[
I_L=e^{iL^\tau}\sqrt{2\pi}\kappa^{a-1/2}e^{-\pi\kappa/2}
 e^{i(-\kappa\log\kappa+\kappa-a\pi/2+\pi/4)}(1+o(1)).
\]
The uniform sectorial Stirling formula gives exactly the same expression for \(e^{iL^\tau}\Gamma(a-i\kappa)\), establishing (1). The absolute \(O_a(n^{-1})\) reduction error is negligible relative to the right-hand side because \(\kappa=o(\log n)\) for \(\tau<2\). Division by \(\Gamma(a)\) completes the supercritical eigenvalue asymptotic.

**4. Spectral consequences.** Stirling's modulus formula gives the sharp logarithmic decay. Since \(\kappa_n\to\infty\), the diagonal is compact. Since \(\log|\lambda_n|=-O((\log n)^{\tau-1})=o(\log n)\), for each fixed \(q>0\) its \(q\)-powers dominate a divergent harmonic-series tail; no \(\mathcal S_q\) membership is possible. Finally, two-sided logarithmic bounds
\[
\exp\![-(c+\epsilon)(\log n)^{\tau-1}]
\le |\lambda_n|\le
\exp\![-(c-\epsilon)(\log n)^{\tau-1}],
\qquad c=\frac{\pi\tau}{2},
\]
valid for all sufficiently large \(n\), squeeze the counting function and prove the displayed limit for \(N_\tau(s)\).

## Verification
The companion standalone Python checker evaluates the exact critical beta/gamma ratio, tests the subcritical gamma-law approximation numerically, and integrates the rotated logarithmic-phase contour at moderate large logarithmic scales, comparing it to the predicted complex gamma factor. It checks agreement and improvement as the logarithmic scale grows. These finite checks confirm normalization and the contour orientation, not the all-parameter stationary-phase estimate, which is proved above. Run with `python3 verify_logchirp.py` after installing `mpmath`.

## Relationship to prior work
Li and Wang (2026) establish a broad compactness characterization for bounded-symbol Toeplitz operators on radial weighted Bergman spaces; that criterion does not state a sharp complex eigenvalue asymptotic for the present unimodular logarithmic chirps. Koita, Kupin, Naboko, and Touré (2020) obtain singular-value asymptotics for symbols whose *modulus itself* decays logarithmically; here the symbol modulus never decays and compactness is solely due to cancellation. Bendaoud et al. (2020) develop general spectral and Schatten criteria for radial complex symbols, but the directly inspected introductory results do not provide the power-log phase transition or the gamma asymptotic. Maximenko and Pacheco (2025) discuss radial eigenvalue sequences and logarithmic metric regularity; their published abstract does not assert this symbol-specific formula. The classical beta/gamma identities and one-dimensional stationary phase are used as standard tools, not claimed as inventions. A separate earlier result for a reciprocal *algebraic* boundary phase has stretched-exponential, every-Schatten behavior; its formula does not imply this slower power-log transition. A related earlier two-fixed-frequency radial phase produces noncompact essential annuli, not the increasing-frequency Mellin cancellation considered here.

## Limitations
The asymptotic is proved only for each fixed \(0<\tau<2\), with the nontrivial logarithmic phase estimate restricted to \(1<\tau<2\). No claim is made for \(\tau\ge2\), for uniformity in the exponent near either endpoint, or for arbitrary weights or nonradial symbols. The original spectral phase and Schatten conclusions are unverified by an independent audit. Exact historical priority cannot be guaranteed; an equivalent complex Mellin asymptotic could occur in older or unindexed literature, and one plausible related full text was only partially accessible.

## References
1. Y. Li and Z. Wang, *Compact Toeplitz operators on radial weighted Bergman spaces*, arXiv:2608.23733 (first public version 2026-08-24).
2. M. Koita, S. Kupin, S. Naboko, and B. Touré, *On spectral properties of compact Toeplitz operators on Bergman space with logarithmically decaying symbol and applications to banded matrices*, arXiv:2006.02586 (2020).
3. Z. Bendaoud, S. Kupin, K. Toumache, B. Touré, and R. Zarouf, *Toeplitz Operators with Radial Symbols on Bergman Space and Schatten-von Neumann Classes*, J. Math. Phys. Anal. Geom. **16** (2020), 3–26, DOI:10.15407/mag16.01.003.
4. E. A. Maximenko and C. G. Pacheco, *Toeplitz operators in Bergman space induced by radial measures*, arXiv:2503.23649 (2025).
