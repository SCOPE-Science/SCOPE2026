# All-order coherent-state growth of the Bargmann–Fock integration resolvent

## Finding
Let \(Jf(z)=\int_0^z f(\zeta)\,d\zeta\) act on the standard Gaussian Bargmann–Fock Hilbert space \(\mathcal F^2\). Write \(R_t=(I-tJ)^{-1}\) for \(t>0\). For **every fixed integer** \(N\ge0\),
\[
e^{-t^2/2}\|R_t\|=\left(\sum_{j=0}^{N}\frac{j!}{t^{2j}}\right)^{1/2}+O_N(t^{-2N-2})\qquad(t\to\infty).
\]
Thus
\[
\|R_t\|=e^{t^2/2}\left(1+\frac{1}{2t^2}+\frac{7}{8t^4}+O(t^{-6})\right).
\]
More precisely, writing \(\phi_j(z)=z^j/\sqrt{j!}\), \(u_t(z)=e^{-t^2/2}e^{tz}\), and \(w_{t,m}=\sum_{j=0}^{m-1}\sqrt{j!}\,t^{-j}\phi_j\), one has for each fixed integer \(m\ge1\)
\[
\left\|e^{-t^2/2}R_t-u_t\otimes w_{t,m}\right\|=O_m(t^{-m+1/2}).
\]
Here \((u\otimes w)f=\langle f,w\rangle u\), with the inner product linear in its first argument. In particular the dominant singular direction is asymptotically a coherent output state and a finite factorial input profile.

For the spectral resolvent as \(\rho=|\lambda|\downarrow0\),
\[
\|(\lambda I-J)^{-1}\|=\rho^{-1}e^{1/(2\rho^2)}\left(1+\frac{\rho^2}{2}+\frac{7\rho^4}{8}+O(\rho^6)\right).
\]
If \(r_\varepsilon\) is the radial boundary of the \(\varepsilon\)-pseudospectrum \(\{\lambda:\|(\lambda I-J)^{-1}\|>\varepsilon^{-1}\}\), then, with \(L=\log(1/\varepsilon)\),
\[
r_\varepsilon^{-2}=2L-\log(2L)+O(\log L/L)\qquad(\varepsilon\downarrow0).
\]
The spectrum itself is \(\{0\}\).

## Assumptions and scope
Use \(\|f\|_{\mathcal F^2}^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\). The scalar parameter \(t\) is taken positive without loss, because conjugating \(J\) by circle rotations changes its scalar phase. Every \(O_m\) and \(O_N\) constant may depend on the *fixed* integer subscript; this is a Poincaré asymptotic expansion, not a convergent infinite factorial series. The norm and rank-one estimates are infinite-dimensional operator-norm statements, not assertions about finite truncations.

## Proof
**1. Weighted shift and exact columns.** The orthonormal basis \((\phi_j)_{j\ge0}\) satisfies \(J\phi_j=(j+1)^{-1/2}\phi_{j+1}\). Consequently \(\|J^k\|=1/\sqrt{k!}\), so \(J\) is quasinilpotent, \(R_t=\sum_{k\ge0}t^kJ^k\) converges absolutely in operator norm, and for \(k\ge j\)
\[
\langle R_t\phi_j,\phi_k\rangle=t^{k-j}\sqrt{j!/k!},
\]
with coefficient zero for \(k<j\). The coherent state \(u_t=e^{-t^2/2}\sum_{k\ge0}t^k\phi_k/\sqrt{k!}\) has norm one. Therefore, for all \(j\ge0\),
\[
e^{-t^2/2}R_t\phi_j=\frac{\sqrt{j!}}{t^j}P_{\ge j}u_t,
\]
where \(P_{\ge j}\) is the orthogonal projection onto the span of \(\{\phi_k:k\ge j\}\).

**2. Low columns and high-tail control.** Fix \(m\ge1\) and let \(P_{<m}\) project onto the first \(m\) basis vectors. For \(j<m\), the difference from the claimed rank-one column equals \(-\sqrt{j!}\,t^{-j}P_{<j}u_t\). Its norm is at most
\[
e^{-t^2/2}\sqrt{j!}\,t^{-j}\left(\sum_{k<j}\frac{t^{2k}}{k!}\right)^{1/2}=O_j(e^{-t^2/2}t^{-1})
\]
for fixed \(j\ge1\), and is zero for \(j=0\). Hence the finite-column discrepancy is exponentially small in operator norm.

For the remaining columns, use invariance of \(P_{\ge m}\mathcal F^2\) under \(J\) and the exact norm \(\|J^kP_{\ge m}\|=\sqrt{m!/(m+k)!}\):
\[
\begin{aligned}
e^{-t^2/2}\|R_tP_{\ge m}\|&\le e^{-t^2/2}\sum_{k\ge0}t^k\sqrt{\frac{m!}{(m+k)!}}\\
&\le \sqrt{m!}\,t^{-m}\sum_{n\ge0}e^{-t^2/2}\frac{t^n}{\sqrt{n!}}.
\end{aligned}
\]
To bound the last sum, put \(s=t^2\) and \(p_n=e^{-s}s^n/n!\), the Poisson probabilities of mean and variance \(s\). Weighted Cauchy–Schwarz gives
\[
\left(\sum_{n\ge0}\sqrt{p_n}\right)^2
\le \left(\sum_{n\ge0}p_n\left[1+\frac{(n-s)^2}{s}\right]\right)
\left(\sum_{n\ge0}\frac1{1+(n-s)^2/s}\right)
\le 2(1+\pi\sqrt{s}).
\]
Indeed the first factor is \(2\), while a nonnegative unimodal function has its one-sided lattice sum bounded by its integral plus its maximum; the second lattice sum is at most \(1+\pi\sqrt{s}\). Therefore \(e^{-t^2/2}\|R_tP_{\ge m}\|=O_m(t^{-m+1/2})\). Combining this with the finite-column estimate proves the rank-one approximation.

**3. All orders.** Since \(\|u_t\|=1\),
\[
\|u_t\otimes w_{t,m}\|=\|w_{t,m}\|=\left(\sum_{j=0}^{m-1}\frac{j!}{t^{2j}}\right)^{1/2}.
\]
The reverse triangle inequality and step 2 show that the normalized resolvent norm differs from this expression by \(O_m(t^{-m+1/2})\). Given \(N\), take \(m=2N+3\). Then the error is \(O_N(t^{-2N-5/2})\) and removing the finite terms with \(j>N\) changes the square root by \(O_N(t^{-2N-2})\). This proves the first formula. The coefficient \(7/8\) follows by applying the ordinary square-root Taylor series to \(1+t^{-2}+2t^{-4}\).

**4. Pseudospectral radius.** Conjugation by rotations makes \(\|(\lambda I-J)^{-1}\|\) depend only on \(\rho=|\lambda|\) and equal \(\rho^{-1}\|R_{1/\rho}\|\). The resolvent norm increases strictly with \(1/\rho\): the weighted-shift matrix has nonnegative entries, and a top norm-attaining nonnegative vector exists because \(R_t-I\) is compact and \(\|R_t\|>1\); a strict increase in \(t\) then increases that vector's output norm. Thus a unique small-radius level boundary exists for sufficiently small \(\varepsilon\). Writing \(x=r_\varepsilon^{-2}\), the norm asymptotic implies \(2L=x+\log x+O(x^{-1})\), and substitution gives \(x=2L-\log(2L)+O(\log L/L)\).

## Verification
The standalone `checker.py` recomputes finite resolvent matrices from factorial ratios, checks the matrix resolvent identity, compares leading normalized-norm coefficients, checks finite tail bounds, and evaluates the Poisson estimate for test values. It uses NumPy and SciPy and reports 51 finite diagnostics. Those diagnostics illustrate the formula but do not establish any infinite-dimensional or asymptotic claim; those follow from the exact column identities and estimates above.

## Relationship to prior work
Constantin and Persson (2015, arXiv:1509.01401v1) studied the spectrum and explicit resolvent equations for Volterra-type integration operators on generalized Fock spaces. Their theory includes the Gaussian case, and the scalar exponential solution already explains the leading lower bound \(\|R_t\|\ge e^{t^2/2}\). The present statement does **not** claim the resolvent formula or quasinilpotence is new; its contribution is the infinite-dimensional rank-one operator-norm approximation, full factorial expansion, explicit subleading coefficients, and pseudospectral boundary.

Schindl (2026, arXiv:2610.11902v1) develops boundedness, compactness, and dynamical conditions for differentiation and integration in weight-sequence-generated analytic spaces. The Gaussian Hilbert model and its large-parameter resolvent norm are different quantitative questions. Equivalence to earlier factorial-weighted-shift pseudospectral estimates, possibly under other language, remains a priority risk.

## Limitations
Only one complex variable and the canonical unit Gaussian weight are treated. Estimates are pointwise in each fixed expansion order, not uniform in an order growing with \(t\). The formal infinite factorial series diverges for each fixed \(t\). No independent review or priority determination has been performed. The finite checker is not a proof and no claims are made about non-Gaussian Fock weights or Banach exponents distinct from two.

## References
1. Gerhard Schindl, *The differentiation and integration operator on weighted spaces of analytic functions in the weight sequence setting*, arXiv:2610.11902v1, publicly posted 8 October 2026. https://arxiv.org/abs/2610.11902
2. Olivia Constantin and Anna-Maria Persson, *The Spectrum of Volterra-type integration operators on generalized Fock spaces*, arXiv:1509.01401v1, publicly posted 4 September 2015. https://arxiv.org/abs/1509.01401
