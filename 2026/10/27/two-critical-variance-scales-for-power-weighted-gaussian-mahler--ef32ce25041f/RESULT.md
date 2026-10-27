# Two critical variance scales for power-weighted Gaussian Mahler means

## Finding
Let \(G_1,G_2,\ldots\) be independent standard circular complex Gaussian variables. For every integer \(n\ge1\) and real \(\alpha\ge0\), set
\[
P_{n,\alpha}(z)=\sum_{j=1}^{n} j^{-\alpha/2}G_j z^{j-1},\qquad
M_{n,\alpha}=\frac1{2\pi}\int_{-\pi}^{\pi}\log|P_{n,\alpha}(e^{it})|\,dt.
\]
Put \(H_n(s)=\sum_{j=1}^n j^{-s}\), and let \(\operatorname{Li}_2(x)=\sum_{k\ge1}x^k/k^2\) for \(0\le x\le1\). Then, for all \(n,\alpha\),
\[
\mathbb E M_{n,\alpha}=\tfrac12(\log H_n(\alpha)-\gamma),\quad
\operatorname{Var}(M_{n,\alpha})=\frac1{8\pi}\int_{-\pi}^{\pi}\operatorname{Li}_2\left(\left|\frac{\sum_{j=1}^{n} j^{-\alpha}e^{ijt}}{H_n(\alpha)}\right|^2\right)dt.
\]
For every **fixed** \(\alpha\ge0\), the sharp variance phase diagram is
\[
\operatorname{Var}(M_{n,\alpha})\sim
\begin{cases}
C_\alpha n^{-1},&0\le\alpha<\tfrac12,\\
(\log n)/(16n),&\alpha=\tfrac12,\\
\tfrac14(1-\alpha)^2\zeta(2\alpha)n^{-2(1-\alpha)},&\tfrac12<\alpha<1,\\
\pi^2/(24(\log n)^2),&\alpha=1,\\
C_\alpha^{\infty},&\alpha>1,
\end{cases}
\]
where the finite strictly positive constants are
\[
C_\alpha=\frac1{8\pi}\int_{\mathbb R}
\operatorname{Li}_2\!\left(\left|(1-\alpha)\int_0^1 x^{-\alpha}e^{iux}dx\right|^2\right)du
\quad(0\le\alpha<\tfrac12),
\]
\[
C_\alpha^{\infty}=\frac1{8\pi}\int_{-\pi}^{\pi}
\operatorname{Li}_2\!\left(\left|\frac{\sum_{j=1}^{\infty}j^{-\alpha}e^{ijt}}{\zeta(\alpha)}\right|^2\right)dt
\quad(\alpha>1).
\]
The transitions have **explicit logarithmic critical windows**. For each fixed \(\lambda\in\mathbb R\), with convergence uniform when \(\lambda\) varies over compact sets,
\[
\lim_{n\to\infty}\frac{16n}{\log n}
\operatorname{Var}\left(M_{n,\,1/2+\lambda/\log n}\right)
=\frac{e^{2\lambda}-1}{2\lambda},
\]
\[
\lim_{n\to\infty}\frac{24(\log n)^2}{\pi^2}
\operatorname{Var}\left(M_{n,\,1+\lambda/\log n}\right)
=\left(\frac{\lambda}{1-e^{-\lambda}}\right)^2.
\]
Both right sides are continuously defined as \(1\) at \(\lambda=0\). In the first window, \(n\) must be large enough that the displayed exponent is nonnegative.

## Assumptions and scope
The exponent is real and nonnegative. Gaussian variables have density \(\pi^{-1}e^{-|z|^2}\) on \(\mathbb C\); angular integration uses normalized Haar measure. The logarithm is the real logarithm of modulus, with its integrable singularities at zeros. The constant \(\gamma\) is Euler's constant; \(\zeta\) is the classical Riemann zeta function at arguments \(>1\). The result concerns expectation and variance, not distributional convergence. The two displayed critical-window formulas allow the exponent to depend on \(n\); the five-case diagram holds with a fixed exponent.

## Proof
**1. Gaussian logarithm covariance.** If \((Z,W)\) are standard jointly circular complex Gaussians with \(\mathbb E Z\overline W=\rho\), the ordinary Laguerre generating function and Gaussian Laplace transform give
\[
\mathbb E\left[L_k(|Z|^2)L_\ell(|W|^2)\right]=\mathbf1_{k=\ell}|\rho|^{2k}.
\]
Indeed, multiplying generating series and taking expectations gives exactly \((1-|\rho|^2st)^{-1}\). In \(L^2\) of the standard exponential law,
\[
\log|Z|=-\frac\gamma2-\frac12\sum_{k=1}^{\infty}\frac{L_k(|Z|^2)}{k}.
\]
The coefficients follow by integration against \(e^{-x}\log x\); Parseval validates the series since \(\sum k^{-2}<\infty\). Hence
\[
\operatorname{Cov}(\log|Z|,\log|W|)=\tfrac14\operatorname{Li}_2(|\rho|^2).
\]
The formula extends to \(|\rho|=1\) by \(L^2\) convergence. The evaluation of \(P_{n,\alpha}\) has variance \(H_n(\alpha)\), and two evaluations at angular distance \(t\) have normalized covariance equal, up to an irrelevant unimodular factor, to \(F_{n,\alpha}(t)/H_n(\alpha)\), where \(F_{n,\alpha}(t)=\sum_{j=1}^n j^{-\alpha}e^{ijt}\). Integrating covariance proves the two finite-\(n\) identities.

**2. The first-chaos and higher-chaos split.** From \(x\le\operatorname{Li}_2(x)\le x+(\zeta(2)-1)x^2\) on \([0,1]\) and Fourier Parseval,
\[
\operatorname{Var}(M_{n,\alpha})
=\frac{H_n(2\alpha)}{4H_n(\alpha)^2}+R_{n,\alpha},\quad
0\le R_{n,\alpha}\le\frac{\zeta(2)-1}{4}\frac{\int_{-\pi}^{\pi}|F_{n,\alpha}(t)|^4\,dt/(2\pi)}{H_n(\alpha)^4}.
\]
This decomposition is exact at the first term, not an assumption of Gaussianity of the integrated logarithm.

**3. Fourier bounds.** Splitting a monotone power-weight sum at \(\lfloor1/|t|\rfloor\), and bounding the remaining tail by summation by parts and the geometric-sum estimate, gives for \(0\le\alpha<1\), uniformly for \(0<|t|\le\pi\),
\[
|F_{n,\alpha}(t)|\le C_\alpha\min\{n^{1-\alpha},|t|^{\alpha-1}\}.
\]
The constants can be chosen uniformly for \(\alpha\) in any compact subinterval of \([0,1)\). At \(\alpha=1\), the corresponding bound is \(C(1+|\log|t||)\) when \(|t|\ge1/n\), and \(C\log(n+1)\) otherwise. The latter estimates hold, with constants depending only on \(L\), whenever \(|\alpha-1|\le L/\log n\), because \(j^{|\alpha-1|}\le e^L\) for \(j\le n\). Therefore,
\[
\int_{-\pi}^{\pi}|F_{n,\alpha}(t)|^4dt
=\begin{cases}
O_\alpha(n^{3-4\alpha}),&0\le\alpha<3/4,\\
O(\log n),&\alpha=3/4,\\
O_\alpha(1),&3/4<\alpha\le1,
\end{cases}
\]
where the first estimate is also uniform for \(\alpha\) in a shrinking \(O(1/\log n)\) neighborhood of \(1/2\), and the last estimate is uniform for an analogous neighborhood of \(1\). The displayed \(O\)-statements follow by separately integrating on \(|t|\le1/n\) and its complement.

**4. The low-exponent branch.** For \(\alpha<1\), \(H_n(\alpha)\sim n^{1-\alpha}/(1-\alpha)\). At any fixed \(u\), the weighted Riemann sums converge to
\[
\frac{F_{n,\alpha}(u/n)}{H_n(\alpha)}\longrightarrow
\Phi_\alpha(u)=(1-\alpha)\int_0^1x^{-\alpha}e^{iux}dx.
\]
The preceding bound shows \(|F_{n,\alpha}(u/n)/H_n(\alpha)|\le C\min(1,|u|^{\alpha-1})\). When \(\alpha<1/2\), the square of this majorant is integrable on \(\mathbb R\); \(\operatorname{Li}_2(x)\le\zeta(2)x\). Dominated convergence after \(t=u/n\) proves \(n\operatorname{Var}(M_{n,\alpha})\to C_\alpha\). The constant is positive since \(\Phi_\alpha(0)=1\), and finite by the same estimate.

**5. The central and upper branches.** At \(\alpha=1/2\), the exact first-chaos term is \((\log n)/(16n)+O(n^{-1})\) and the fourth-power bound makes \(R_{n,\alpha}=O(n^{-1})\). For fixed \(1/2<\alpha<1\), the first-chaos term is asymptotic to \(\tfrac14(1-\alpha)^2\zeta(2\alpha)n^{-2(1-\alpha)}\) while the fourth-power bound makes the remainder little-oh of it: compare the powers \(3-4\alpha\) and \(2-2\alpha\), treating \(\alpha=3/4\) separately. At \(\alpha=1\), the first-chaos term is \(\zeta(2)/(4(\log n)^2)+o((\log n)^{-2})\) and the remainder is \(O((\log n)^{-4})\). Since \(\zeta(2)=\pi^2/6\), this gives the displayed coefficient. For \(\alpha>1\), the normalized Fourier series converges uniformly to \(\sum_{j\ge1}j^{-\alpha}e^{ijt}/\zeta(\alpha)\); continuity and boundedness of \(\operatorname{Li}_2\) on \([0,1]\) give the stated strictly positive limiting variance.

**6. Both logarithmic windows.** Let \(L=\log n\), and fix \(\lambda\) in a compact interval. For \(\alpha_n=1/2+\lambda/L\), the bounds in step 3 give \(R_{n,\alpha_n}=O(n^{-1})\) uniformly. Elementary integral comparison, uniformly in bounded \(\lambda\), gives
\[
H_n(\alpha_n)\sim2n^{1/2}e^{-\lambda},\qquad
\frac{H_n(2\alpha_n)}{L}\to\int_0^1e^{-2\lambda s}ds=\frac{1-e^{-2\lambda}}{2\lambda}.
\]
Substituting into step 2 proves the first crossover. For \(\alpha_n=1+\lambda/L\), the uniform logarithmic Fourier bound yields \(R_{n,\alpha_n}=O(L^{-4})\). The corresponding sums obey
\[
\frac{H_n(\alpha_n)}{L}\to\int_0^1e^{-\lambda s}ds=\frac{1-e^{-\lambda}}\lambda,
\qquad H_n(2\alpha_n)\to\zeta(2).
\]
Again step 2 gives the second crossover. Integral comparison makes both convergences uniform on compact \(\lambda\)-sets. This exhausts every claimed boundary regime.

## Verification
The included `verify_powerlaw_mahler.py` evaluates the exact dilogarithm integral with uniform-angle FFT quadrature, checks the coefficient Parseval identity, checks positivity and the first-chaos remainder, and compares the leading rates and the two crossover predictions. It has passed 24 finite Parseval/bound checks, 12 asymptotic-remainder checks, and three independent Jensen-root Monte Carlo comparisons, along with numerical tables. This is corroboration, not a substitute for the proof. For reproducibility run `python verify_powerlaw_mahler.py` with NumPy and SciPy installed. The numerical integral is not a certification of a uniform error term. The symbolic asymptotic constants follow from the estimates in steps 3–6 rather than from these computations.

## Relationship to prior work
Kiro and Nishry's *Fluctuations for Zeros of Gaussian Taylor Series* develops Gaussian analytic covariance methods and sharp zero-count variances, including a dilogarithm representation for the covariance of logarithmic moduli. Here the observable is instead the **boundary Jensen average itself**, with polynomial truncation growing and a power-weighted covariance profile; the first-chaos transition and both \(1/\log n\) exponent windows are not statements of their zero-count theorems. Kabluchko, Khoruzhenko and Marynych consider regularly varying random-polynomial coefficients and zero-process regimes; their principal observables are zero locations and local correlations, not the exact variance of a circular logarithmic mean. The unweighted \(\alpha=0\) specialization is not asserted to be novel; the five-regime parameter dependence and two crossover functions are the contributions here.

## Limitations
The theorem is confined to independent circular complex Gaussian coefficients and exactly power-law variance weights. It gives second moments only; no central limit theorem or tail estimate follows. The \(\alpha>1\) constant is given by a convergent integral rather than a closed elementary expression. The proof does not assert finite-\(n\) monotonicity in \(\alpha\), nor a uniform approximation through parameter ranges wider than the stated logarithmic windows. Historical priority, especially under terminology based on Jensen functionals rather than Mahler measures, remains subject to external verification.

## References
1. A. Kiro and A. Nishry, *Fluctuations for Zeros of Gaussian Taylor Series*, arXiv:1911.13051 (first posted 2019-11-29); J. London Math. Soc. 104 (2021), 1172–1203. https://arxiv.org/abs/1911.13051 ; https://doi.org/10.1112/jlms.12457 .
2. Z. Kabluchko, B. Khoruzhenko and A. Marynych, *On the Distribution Patterns of Zeros for Random Polynomials with Regularly Varying Coefficients*, arXiv:2511.12302 (first posted 2025-11-15). https://arxiv.org/abs/2511.12302 .
