# A marked exponential exit law for Poisson-reset stable flights

## Finding
Fix \(0<\alpha<2\), \(\sigma,r>0\), and \(-1<\Lambda<1\). Let \(X\) be a one-dimensional symmetric \(\alpha\)-stable Lévy flight with Poisson resetting at rate \(r\) to \(\Lambda L\), stopped at the first exit \(T_L\) from \((-L,L)\). Put
\[
c_{\alpha,\sigma}=\frac{\sigma^\alpha\Gamma(1+\alpha)\sin(\pi\alpha/2)}{\pi},\qquad
\lambda_\Lambda=\frac{c_{\alpha,\sigma}}{\alpha}\big[(1-\Lambda)^{-\alpha}+(1+\Lambda)^{-\alpha}\big].
\]
Define a probability measure \(\Pi_\Lambda\) on \(\mathbb R\setminus(-1,1)\) by
\[
\Pi_\Lambda(dy)=\frac{c_{\alpha,\sigma}}{\lambda_\Lambda}|y-\Lambda|^{-1-\alpha}{\bf1}_{\{|y|\ge1\}}\,dy.
\]
Then the **joint** weak limit is
\[
\left(\frac{T_L}{L^\alpha},\frac{X_{T_L}}{L}\right)
\Longrightarrow (E_\Lambda,H_\Lambda),\qquad
E_\Lambda\sim\operatorname{Exp}(\lambda_\Lambda),\quad H_\Lambda\sim\Pi_\Lambda,
\]
where \(E_\Lambda\) and \(H_\Lambda\) are independent. In particular, for \(s\ge0\) and bounded continuous \(g\),
\[
\lim_{L\to\infty}\mathbb E\left[e^{-sT_L/L^\alpha}g(X_{T_L}/L)\right]
=\frac{c_{\alpha,\sigma}}{\lambda_\Lambda+s}
\int_{|y|\ge1}|y-\Lambda|^{-1-\alpha}g(y)\,dy.
\]
Right-side exit has limiting probability
\[
p_+=\frac{(1-\Lambda)^{-\alpha}}{(1-\Lambda)^{-\alpha}+(1+\Lambda)^{-\alpha}}.
\]
Given right-side exit, the scaled overshoot \((X_{T_L}-L)/L\) has limiting survival function \(((1-\Lambda)/(1-\Lambda+u))^\alpha\) at \(u\ge0\). Given left-side exit, the corresponding positive overshoot \((-L-X_{T_L})/L\) has limit survival function \(((1+\Lambda)/(1+\Lambda+u))^\alpha\). Each side/overshoot mark is asymptotically independent of the scaled exit time.

## Assumptions and scope
The underlying process \(Y\), started from \(\Lambda L\), has characteristic function
\[\mathbb E[e^{ik(Y_t-Y_0)}]=\exp(-t\sigma^\alpha|k|^\alpha).\]
Its Lévy measure is \(\nu(dz)=c_{\alpha,\sigma}|z|^{-1-\alpha}\,dz\). At times of an independent rate-\(r\) Poisson clock, the position resets exactly to \(\Lambda L\); fresh Lévy increments and reset periods are independent. This statement fixes every parameter as \(L\to\infty\). The exit position is the actual post-jump position, not a boundary projection. No Gaussian case \(\alpha=2\), boundary-starting regime, growing reset rate, or uniform rate of convergence is claimed.

## Proof
**Step 1: Marked single-excursion estimate.** Let \(R\sim\operatorname{Exp}(r)\) be an independent reset time and \(\tau_L\) the unreset exit time from \((-L,L)\) from \(\Lambda L\). For any bounded continuous \(g\), show
\[
L^\alpha\mathbb E[\mathbf1_{\{\tau_L<R\}}g(Y_{\tau_L}/L)]\longrightarrow
\frac{c_{\alpha,\sigma}}r\int_{|y|\ge1}|y-\Lambda|^{-1-\alpha}g(y)\,dy.\tag{1}
\]
For a cutoff \(\delta L\), decompose increments of \(Y\) into independent, symmetric, centered jumps \(M\) of size at most \(\delta L\) and a compound-Poisson sum \(J\) of larger jumps. The large-jump intensity equals \(2c_{\alpha,\sigma}\delta^{-\alpha}L^{-\alpha}/\alpha\); hence the probability of at least two such jumps before \(R\) is \(O_\delta(L^{-2\alpha})\). The martingale \(M\) satisfies, by its quadratic variation and Doob's inequality,
\[
\mathbb P\{\sup_{t\le R}|M_t|>\varepsilon L\}
\le \frac{8c_{\alpha,\sigma}}{r(2-\alpha)}
\frac{\delta^{2-\alpha}}{\varepsilon^2}L^{-\alpha}.\tag{2}
\]
Choose \(0<\varepsilon<\min(1-\Lambda,1+\Lambda)/4\) and \(0<\delta<\varepsilon\). Outside the two exceptional events in (2) and the two-large-jump event, an exit before \(R\) must be produced by the unique large jump. Its landing position divided by \(L\) differs by at most \(\varepsilon\) from \(\Lambda+z/L\). Conversely, if that unique jump lands at distance more than \(2\varepsilon\) outside \([-1,1]\), it forces exit. Only jumps landing within a width-\(O(\varepsilon)\) band of \(\{-1,1\}\) can change this decision. That band's Lévy measure is \(O(\varepsilon L^{-\alpha})\), uniformly for small \(\delta\). By independence, the expected number of jumps with rescaled size in a Borel set bounded away from zero before \(R\) equals \(r^{-1}\nu(L\,\cdot)\), and replacing 'exactly one' by this expected count makes an \(O_\delta(L^{-2\alpha})\) error. First let \(L\to\infty\) for fixed cutoffs; then \(\delta\downarrow0\) with \(\varepsilon\) fixed in (2), and finally \(\varepsilon\downarrow0\). For nonuniformly continuous bounded \(g\), first restrict to a compact set of landing positions and then control the tail by \(O(R_0^{-\alpha}L^{-\alpha})\). Thus (1) holds as a finite signed measure limit tested against every bounded continuous \(g\). Taking \(g\equiv1\) gives
\[p_L:=\mathbb P(\tau_L<R)=\lambda_\Lambda/(rL^\alpha)+o(L^{-\alpha}).\tag{3}\]

**Step 2: Include the time transform.** Write \(q_L(s,g)=\mathbb E[e^{-s\tau_L/L^\alpha}\mathbf1_{\{\tau_L<R\}}g(Y_{\tau_L}/L)]\). Since \(\tau_L<R\) on success and \(1-e^{-u}\le u\), Cauchy-Schwarz with \(\mathbb E R^2=2/r^2\) yields
\[
|q_L(s,g)-q_L(0,g)|\le \frac{s\|g\|_\infty}{L^\alpha}
\sqrt{\frac2{r^2}}\sqrt{p_L}=o(L^{-\alpha}).
\]
Consequently (1) remains valid with the exponential factor.

**Step 3: Exact regeneration and its limit.** A failed excursion occupies time \(R\) and begins an independent copy. Hence the exact, all-excursions renewal identity is
\[
\mathbb E[e^{-sT_L/L^\alpha}g(X_{T_L}/L)]
=\frac{q_L(s,g)}{1-a_L(s)},\quad
 a_L(s)=\mathbb E[e^{-sR/L^\alpha}\mathbf1_{\{R<\tau_L\}}].\tag{4}
\]
As \(R\) has a continuous distribution, ties have probability zero. By subtracting the successful term from \(\mathbb E[e^{-sR/L^\alpha}]=r/(r+s/L^\alpha)\), using (3) and the same time-factor bound,
\[
1-a_L(s)=\frac{\lambda_\Lambda+s}{rL^\alpha}+o(L^{-\alpha}).\tag{5}
\]
Divide the limits of numerator and denominator of (4). For all \(s\ge0\) and bounded continuous \(g\), this yields the claimed transform. The right side factors as \(\lambda_\Lambda/(\lambda_\Lambda+s)\) times \(\int g\,d\Pi_\Lambda\), proving joint weak convergence and independence. Integrating the density over the two exterior half-lines gives the side probabilities; integrating the power-law tails beyond a further distance \(u\) gives the conditional overshoot laws.

## Verification
All constants follow from the exact stable Lévy measure and independent exponential-clock moments. The included standalone `verify.py` checks the Lévy-density normalization across several indices, the elementary boundary integrals, the special Cauchy case \(\alpha=1,\Lambda=1/3,\sigma=r=1\), the right/left mark masses and the Laplace-factorization algebra. In that case \(\lambda_\Lambda=9/(4\pi)\), and right/left exit probabilities are \(2/3\) and \(1/3\). The computer checks test closed-form consequences; the proof of the infinite-volume limit is Steps 1–3.

## Relationship to prior work
Żbik and Palmowski (arXiv:2610.20410v1, Sections II–IV) prove the leading **mean** exit time for precisely the continuous-time reset-stable model, consistent with \(\mathbb ET_L\sim L^\alpha/\lambda_\Lambda\). This does not specify the exit location or establish the independence of the full exit mark and the time. Żbik and Dybiec (arXiv:2311.16014, Sections II–IV) analyze resetting and finite-interval first-passage statistics, without the joint large-interval mark limit. Radice and Cristadoro (arXiv:2403.12727) derive an exact leapover distribution for a **discrete-time one-sided** myopic target search under per-step resetting; this is directly relevant to overshoots but does not give a two-sided continuous-time interval limit nor independent exponential time/exit marks. Klinger, Voituriez and Bénichou (arXiv:2212.06609) treat exit-side/time asymptotics for discrete-time jump processes **without resetting**. Högele (arXiv:1706.07745) treats small heavy-tailed noise near **attracting deterministic reaction-diffusion equilibria**, a different mechanism from pure Lévy flights restarted to a fixed location. These works supply close phenomena, not the present joint statement under its exact hypotheses.

## Limitations
No quantitative convergence rate, simultaneous \(r,L\)-limit, result at \(\alpha=2\), or finite-\(L\) independence is asserted. For \(\alpha\le1\), the limiting conditional overshoot mean is infinite; no assertion about convergence of overshoot means follows. Priority against every possible general regenerative heavy-tail exit theorem has not been independently certified. The Poissonian reset clock is essential to the exact Laplace calculation; other reset distributions are outside scope.

## References
1. B. Żbik and Z. Palmowski, *Asymptotic behaviour for escaping an interval by Lévy flights under stochastic resetting*, arXiv:2610.20410v1 (first available 2026-10-14), https://arxiv.org/html/2610.20410v1.
2. M. Radice and G. Cristadoro, *Optimizing Leapover Lengths of Lévy Flights with Resetting*, arXiv:2403.12727; Physical Review E 110, L022103 (2024), https://arxiv.org/abs/2403.12727.
3. B. Żbik and B. Dybiec, *Lévy flights and Lévy walks under stochastic resetting*, arXiv:2311.16014, https://arxiv.org/pdf/2311.16014.
4. J. Klinger, R. Voituriez and O. Bénichou, *Leftward, Rightward and Complete Exit Time Distributions of Jump Processes*, arXiv:2212.06609, https://arxiv.org/abs/2212.06609.
5. M. A. Högele, *The first exit problem of reaction-diffusion equations for small multiplicative Lévy noise*, arXiv:1706.07745, https://arxiv.org/abs/1706.07745.
