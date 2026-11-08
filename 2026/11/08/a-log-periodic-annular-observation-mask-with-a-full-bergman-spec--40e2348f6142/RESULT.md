# A log-periodic annular observation mask with a full Bergman spectral limit cycle

## Finding
Fix a Bergman weight \(\alpha>-1\), write \(\beta=\alpha+1>0\), and choose a logarithmic period \(L>0\) and an occupied width \(0<\tau<L\). On the unit disk define the self-similar radial observation region
\[
E_{L,\tau}=\{z\in\mathbb D: -\log(1-|z|^2)\pmod L\in[0,\tau)\}.
\]
This region consists of a central disk and infinitely many progressively thinner annuli accumulating at the boundary. Let \(T=P_\alpha\mathbf1_{E_{L,\tau}}P_\alpha\) act on the weighted analytic Bergman space \(A^2_\alpha(\mathbb D)\), where \(P_\alpha\) is the orthogonal Bergman projection. Define \(\omega=2\pi/L\),
\[
c_0=\tau/L,\qquad c_k=\frac{1-e^{-ik\omega\tau}}{ik\omega L}\quad(k\in\mathbb Z\setminus\{0\}),
\]
and the real-analytic periodic response
\[
G_\beta(s)=\sum_{k\in\mathbb Z}c_k\frac{\Gamma(\beta-ik\omega)}{\Gamma(\beta)}e^{ik\omega s}.
\]
This Fourier series converges absolutely, and \(G_\beta\) is nonconstant, strictly between zero and one, and has fundamental period \(L\). Its minimum and maximum are denoted \(m_\beta\) and \(M_\beta\).

**Spectral law.** If \(\lambda_n\) denotes the eigenvalue belonging to the normalized monomial of degree \(n\ge0\), then
\[
\lambda_n=G_\beta(\log(n+1))+O_{\beta,L,\tau}((n+1)^{-1}),\qquad
\sigma_{\mathrm{ess}}(T)=[m_\beta,M_\beta]\subset(0,1).
\]
In particular, \(T\) and \(I-T\) are both bounded below by a strictly positive constant; both the observed and unobserved regions uniformly sample analytic energy.

**Complete ordinary spectral distribution cycle.** Define \(\nu_N=N^{-1}\sum_{n=0}^{N-1}\delta_{\lambda_n}\). Whenever \(\log N\pmod L\to\theta\), these probability measures converge weakly to
\[
\nu_{\beta,\theta}=\bigl[t\mapsto G_\beta(\theta-t)\bigr]_{\#}\operatorname{Exp}(1),
\]
where \(E\) is exponentially distributed with mean one. Every \(\theta\in[0,L)\) occurs, and all weak subsequential limits have this form. The family contains continuum-many distinct measures, so \(\nu_N\) does not converge.

In contrast, the logarithmically weighted empirical measures converge without extracting subsequences:
\[
\frac{1}{H_N}\sum_{n=1}^N\frac{\delta_{\lambda_n}}n
\ \Longrightarrow\ \frac1L\int_0^L\delta_{G_\beta(s)}\,ds,
\qquad H_N=\sum_{n=1}^N\frac1n.
\]

**Sharp weight-degeneration law.** Set
\[
H(s)=\sum_{k\ne0}c_k\Gamma(-ik\omega)e^{ik\omega s}.
\]
It is real, smooth and nonconstant, and as \(\beta\downarrow0\), uniformly in \(s\),
\[
G_\beta(s)=\tau/L+\beta H(s)+O_{L,\tau}(\beta^2),\qquad
M_\beta-m_\beta=\beta(\max H-\min H)+O_{L,\tau}(\beta^2).
\]
The coefficient of \(\beta\) is strictly positive. At the opposite endpoint \(\beta\to\infty\), \(m_\beta\to0\) and \(M_\beta\to1\).

## Assumptions and scope
Use probability-normalized area measure \(d\mu_\alpha(z)=(\alpha+1)\pi^{-1}(1-|z|^2)^\alpha dA(z)\). Analytic functions in \(A^2_\alpha\) have norm squared \(\int_{\mathbb D}|f|^2d\mu_\alpha\). The basis is
\[
e_n(z)=\sqrt{\frac{\Gamma(n+\beta+1)}{\Gamma(\beta+1)n!}}z^n.
\]
All results hold for **every fixed** \(\alpha>-1\), \(L>0\) and \(0<\tau<L\). Boundary circles of the region have zero measure; their inclusion is immaterial. The limit \(\beta\downarrow0\) or \(\beta\to\infty\) is taken with \(L\) and \(\tau\) fixed.

## Proof
**Step 1: Exact diagonal integral and Fourier multipliers.** Angular orthogonality diagonalizes the radial restriction operator. With \(t=|z|^2\), its eigenvalues are
\[
\lambda_n=\frac1{B(n+1,\beta)}\int_0^1t^n(1-t)^{\beta-1}
F(-\log(1-t))\,dt,\quad F(x)=\mathbf1_{[0,\tau)}(x\pmod L).
\]
The Fourier coefficient of \(F\) at integer \(k\) is \(c_k\). Integrating a Fourier mode with the beta density gives, for all integers \(k\),
\[
\mathbb E[(1-t)^{-ik\omega}]
=\frac{\Gamma(\beta-ik\omega)}{\Gamma(\beta)}
\frac{\Gamma(n+\beta+1)}{\Gamma(n+\beta+1-ik\omega)}.
\]
The resulting exact Fourier series for \(\lambda_n\) converges absolutely: for fixed \(n\), the beta moment of order \(k\) is \(O(|k|^{-n-1})\), while \(c_k=O(|k|^{-1})\). It follows by approximating the step function in \(L^1\) against the continuous beta density (or by Abel summation). The formula includes the zero-frequency value \(c_0\).

**Step 2: A uniform quantitative gamma limit.** If \(t\) has the \(\operatorname{Beta}(n+1,\beta)\) law, then \(Y_n=(n+1)(1-t)\) has a density
\[
p_n(y)=\frac{\Gamma(n+\beta+1)}{\Gamma(n+1)\Gamma(\beta)(n+1)^\beta}
 y^{\beta-1}\left(1-\frac{y}{n+1}\right)^n
\mathbf1_{(0,n+1)}(y).
\]
For fixed \(\beta>0\), Stirling's ratio and \(n\log(1-y/(n+1))=-y+O((y+y^2)/(n+1))\) show that \(\|p_n-y^{\beta-1}e^{-y}/\Gamma(\beta)\|_{L^1}=O_\beta((n+1)^{-1})\). To justify the integral estimate, split at \(y=(n+1)^{1/3}\); on the lower interval multiply the Taylor remainder by the integrable gamma majorant, and on the upper interval both densities have an exponentially small tail. (The elementary inequality \((1-y/(n+1))^n\le e^{-ny/(n+1)}\) supplies the uniform tail bound.) Since \(F\) takes values in \([0,1]\), this total-variation bound is uniform in the logarithmic phase and yields
\[
\lambda_n=\mathbb E\,F(\log(n+1)-\log Y)+O_\beta((n+1)^{-1}),\quad Y\sim\operatorname{Gamma}(\beta,1).
\]
This expectation is \(G_\beta(\log(n+1))\). The gamma characteristic function \(\mathbb E Y^{-ik\omega}=\Gamma(\beta-ik\omega)/\Gamma(\beta)\) gives the displayed Fourier series; exponential decay of the Gamma function on vertical lines proves real analyticity.

**Step 3: Essential spectral interval and sampling gap.** Because the gamma density is strictly positive, every shifted interval of logarithmic residues has positive probability, so \(0<G_\beta(s)<1\). The first Fourier coefficient is nonzero because \(0<\tau<L\) and \(\Gamma\) has no zeros; hence the response is nonconstant and its fundamental period is \(L\). Every point of the circle occurs as a limit of \(\log(n+1)\pmod L\), since consecutive logarithms differ by a quantity tending to zero. The spectral limit points of the diagonal operator are therefore exactly \(G_\beta([0,L])=[m_\beta,M_\beta]\). The finitely many initial eigenvalues are strictly inside \((0,1)\); combining them with the compact limiting interval yields both \(\inf_n\lambda_n>0\) and \(\inf_n(1-\lambda_n)>0\).

**Step 4: All spectral counting laws.** Let \(\varphi:[0,1]\to\mathbb R\) be continuous. The uniform eigenvalue approximation shows that replacing \(\lambda_n\) by \(G_\beta(\log(n+1))\) in \(\nu_N(\varphi)\) changes the result by \(o(1)\). If \(\log N\pmod L\to\theta\), a Riemann sum on \(n/N\in[\varepsilon,1]\), followed by \(\varepsilon\downarrow0\), yields \(\int_0^1\varphi(G_\beta(\theta+\log u))du\). Taking \(u=e^{-t}\) gives the claimed exponential pushforward. Any sequence of cutoffs has a subsequence on which the circle phase converges, and every phase is realized by integers near \(e^{jL+\theta}\). The first moments of the limiting measures have the Fourier expansion
\[
\int x\,d\nu_{\beta,\theta}(x)=\sum_{k\in\mathbb Z}
\frac{c_k\Gamma(\beta-ik\omega)}{\Gamma(\beta)(1+ik\omega)}e^{ik\omega\theta}.
\]
Its first harmonic is nonzero. Thus the first moment is a nonconstant continuous function of phase; its range contains an interval, giving continuum-many distinct limits and nonconvergence. For logarithmic weights, the elementary comparison of \(\sum_{n\le N}n^{-1}\varphi(G_\beta(\log n))\) with \(\int_1^N\varphi(G_\beta(\log t))dt/t\) has \(o(\log N)\) error, and the latter integral averages one periodic function over \([0,\log N]\). This proves Haar pushforward convergence.

**Step 5: Weight endpoints.** For \(k\ne0\), uniformly in integer \(k\) after summation, \(\Gamma(\beta-ik\omega)/\Gamma(\beta)=\beta\Gamma(-ik\omega)+O(\beta^2)\) as \(\beta\downarrow0\). Vertical-line Gamma decay bounds the sum of remainders, giving the displayed uniform expansion and its sharp positive spectral-width coefficient. For \(\beta\to\infty\), if \(Y\sim\operatorname{Gamma}(\beta,1)\), then \(\log(Y/\beta)\to0\) in probability. Choosing phases strictly inside the occupied and vacant subintervals shows \(\max G_\beta\to1\) and \(\min G_\beta\to0\).

## Verification
Run `python bergman_log_annulus_check.py` with Python 3.10+, NumPy and SciPy. The program separately computes concentration eigenvalues as finite sums of regularized incomplete-beta annulus integrals, compares them against the exact beta Fourier series, compares high-degree eigenvalues with the Gamma-smoothed response, and checks the small-weight spectral-width scaling. All tolerances and finite truncations are in the code. The infinite-dimensional conclusions are established by Steps 1–5, not by finite experiments.

## Relationship to prior work
The diagonal beta integral is classical, and the spectral-theorem treatment of weighted radial Bergman Toeplitz operators appears in Rozenblum–Vasilevski (arXiv:2203.04170, first submitted March 8, 2022). Suárez's work and Grudsky–Maximenko–Vasilevski characterize broader radial Toeplitz eigenvalue algebras and logarithmically slowly oscillating sequences. Looi (arXiv:2603.10879) independently analyzes single-frequency logarithmic oscillations of Bergman Toeplitz eigenvalues to disprove a Berezin-transform criterion. Those established facts are **not** claimed as new. The present specific contribution is the complete spectral *empirical-measure limit cycle* for a binary self-similar annular observation region, the canonical logarithmic spectral law, and the sharp weighted collapse and expansion of its essential spectral interval. Taskinen's periodic planar-domain Toeplitz theory concerns translationally periodic domains and does not directly supply these disk boundary-scale statistics.

## Limitations
This is a result for a binary radial mask on the unit disk, fixed logarithmic period and fixed weight. It does not give exact finite-index optimizer degrees, optimal finite-cutoff discrepancy constants, or a theory for nonradial or randomly perturbed annuli. The small- and large-weight limits are taken after determining the fixed-weight essential spectrum; no uniform two-parameter cutoff estimate is asserted. Originality remains subject to possible earlier equivalences in radial Toeplitz and Mellin-convolution literature. No independent mathematical validation is claimed.

## References
- G. Rozenblum and N. Vasilevski, *Commutative algebras of Toeplitz operators on the Bergman space revisited: Spectral theorem approach*, arXiv:2203.04170, first public March 8, 2022, Sections 2–3, especially formulas (2.4) and (3.3).
- D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, arXiv:0710.0797 (2007).
- S. M. Grudsky, E. A. Maximenko and N. L. Vasilevski, *Radial Toeplitz operators on the unit ball and slowly oscillating sequences*, Communications in Mathematical Analysis 14 (2013), 77–94, Theorem 1.3.
- S. Looi, *The Berezin liminf criterion fails for radial Toeplitz operators*, arXiv:2603.10879 (2026), Section 3 and Remark 3.7.
- J. Taskinen, *On Bergman–Toeplitz operators in periodic planar domains*, arXiv:2412.12551, first public December 17, 2024; published 2025.
