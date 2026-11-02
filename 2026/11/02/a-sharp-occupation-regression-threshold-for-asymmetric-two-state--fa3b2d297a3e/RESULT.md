# A sharp occupation-regression threshold for asymmetric two-state Markov bridges

## Finding
Let \(X_s\in\{+,-\}\) be a continuous-time Markov chain with jump rate \(\alpha>0\) from \(+\) to \(-\) and rate \(\beta>0\) from \(-\) to \(+\). Start at \(+\), observe for fixed \(t>0\), and condition on return \(X_t=+\). Write \(N\) for the jump count and \(U=t^{-1}\int_0^t\mathbf 1_{\{X_s=+\}}ds\) for the positive-state occupation fraction. With \(\delta=(\alpha-\beta)t\), set \(m_k=\mathbb E[U\mid N=2k,X_t=+]\). Then \(m_0=1\). The sequence \((m_k)_{k\ge0}\) is strictly decreasing exactly when \(\delta\le2\). For \(\delta>2\), it initially decreases but is not monotone; its terms eventually rise to \(1/2\) from below, with
\[
m_k=\frac12+\frac{2-\delta}{8k}+O_\delta(k^{-2})\qquad(k\to\infty).
\]
For every real \(\delta\), the absolute occupation imbalance \(A=|2U-1|\) is strictly decreasing in monotone likelihood-ratio order as the positive return-cycle count \(k\ge1\) increases. The endpoint \(k=0\) is deterministic at \(A=1\).

## Assumptions and scope
Only the stated finite two-state, time-homogeneous chain, \(t>0\), and \(\alpha,\beta>0\) are assumed. At positive probability \(N=2k\), return is automatic because the chain alternates. All conditional means are well defined for every integer \(k\ge0\). This claim concerns occupation time **conditioned on a fixed even jump count and a returning state**, not an unconditional occupation distribution, an integrated spatial telegraph bridge, or a Brownian-motion bridge.

## Proof
**Conditional occupation law.** For \(k\ge1\), there are \(k+1\) positive-state sojourns and \(k\) negative-state sojourns, with total lengths \(tu\) and \(t(1-u)\). The path-density product contributes \(\alpha^k\beta^k\exp[-\alpha tu-\beta t(1-u)]\). The two simplex volumes contribute \((tu)^k/k!\) and \((t(1-u))^{k-1}/(k-1)!\). Consequently the conditional density of \(U\) is
\[
p_{k,\delta}(u)=\frac{u^k(1-u)^{k-1}e^{-\delta u}}{Z_{k,\delta}},\qquad
Z_{k,\delta}=\int_0^1 v^k(1-v)^{k-1}e^{-\delta v}\,dv,
\quad0<u<1.
\]
For \(k=0\) no jump occurs and \(U=1\).

**Folding and likelihood ratios.** For \(a=|2u-1|\in(0,1)\), the density of \(A\mid N=2k\) is proportional to
\[
(1-a^2)^{k-1}\Big[(1+a)e^{-\delta(1+a)/2}+(1-a)e^{-\delta(1-a)/2}\Big].
\]
The bracket is strictly positive and does not depend on \(k\). For successive \(k\ge1\), the density ratio is therefore a positive constant times \(1-a^2\), strictly decreasing in \(a\in(0,1)\). Thus \(A\) is strictly stochastically decreasing in \(k\), independently of the rate asymmetry.

**A sharp monotonicity threshold.** Condition further on \(A=a\). Comparing the two signs of \(2U-1\) yields
\[
\mathbb E[U\mid A=a,N=2k]=g_\delta(a):=\frac12+\frac a2\tanh\!\left(\operatorname{artanh}a-\frac{\delta a}{2}\right),
\]
independent of \(k\ge1\). If \(\delta\le2\), then \(h_\delta(a):=\operatorname{artanh}a-\delta a/2\) is strictly positive and strictly increasing for \(0<a<1\): its derivative \(1/(1-a^2)-\delta/2\) is positive. Hence \(g_\delta\) is strictly increasing on \((0,1)\). Since the imbalance \(A\) is strictly stochastically decreasing in \(k\), \(m_{k+1}<m_k\) for all \(k\ge1\). Also \(m_1<1=m_0\).

Conversely, if \(\delta>2\), the following asymptotics show that the sequence cannot be decreasing. The density above equals a \(\operatorname{Beta}(k+1,k)\) density exponentially tilted by \(e^{-\delta u}\). Its untilted mean is \((k+1)/(2k+1)=1/2+1/(4k)+O(k^{-2})\), and its variance is \(k(k+1)/[(2k+1)^2(2k+2)]=1/(8k)+O(k^{-2})\). Taylor-expanding numerator and denominator of the bounded exponential tilt around the mean (the third and fourth centered moments are \(O(k^{-2})\)) gives the tilted mean
\[
m_k=\frac12+\frac{2-\delta}{8k}+O_\delta(k^{-2}).
\]
For \(\delta>2\), all sufficiently large \(m_k\) are below \(1/2\), yet tend to \(1/2\). A decreasing sequence converging to \(1/2\) cannot have a term below \(1/2\). The first step is always a strict decrease from \(m_0=1\). Thus strict decrease of every consecutive pair holds if and only if \(\delta\le2\); for \(\delta>2\) there must be at least one upward step.

## Verification
The accompanying `verify.py` independently evaluates the tilted-beta integrals by composite Simpson quadrature, checks their monotone and nonmonotone regimes at finite parameters, and checks the exact \(\delta=0\) beta moments. The complete mathematical conclusion is the analytic argument above, not a numerical extrapolation.

## Relationship to prior work
Classical occupation-time formulas for Markov processes, including Kovchegov–Meredith–Nir (2008), provide the background for occupation functionals. Bogachev–Ratanov (2010) analyze another telegraph occupation functional. A published finite-speed telegraph return-bridge note obtains a \(\operatorname{Beta}(k+1,k)\) law for a **midpoint displacement** under equal switching rates and a different endpoint condition; it does not discuss a two-rate occupation fraction or the threshold \((\alpha-\beta)t=2\). Roldán–Vivo (2019) address discrete-time Markov bridges and joint additive functionals. Colwell (2023) discusses continuous-time jump counts and occupation functionals, but its accessible abstract does not identify a sharp monotonicity threshold. The theorem here is specifically a **signed-occupation regression phase transition in an asymmetric returning continuous-time chain**, stronger than the equal-rate beta identity and distinct from marginal or joint-moment formulas alone.

## Limitations
The threshold describes only conditional means indexed by complete return cycles and does not establish stochastic monotonicity of signed \(U\) when \(\delta\le2\). Even if a previously published joint generating function permits derivation of this result, the exact phase transition could be historically implicit; this remains a priority risk. The closest Colwell paper could not be inspected in full in this review, and equivalent coverage in older specialized literature has not been excluded. The verifier uses finite quadrature and therefore cannot independently certify asymptotics or the all-parameter theorem.

## References
- Y. Kovchegov, N. Meredith and E. Nir, *Occupation times via Bessel functions*, arXiv:0812.1775 (first posted 2008-12-09), https://arxiv.org/abs/0812.1775.
- L. Bogachev and N. Ratanov, *Occupation time distributions for the telegraph process*, arXiv:1007.3139 (first posted 2010-07-19), https://arxiv.org/abs/1007.3139.
- E. Roldán and P. Vivo, *Exact distributions of currents and frenesy for Markov bridges*, Physical Review E 100, 042108 (2019), https://doi.org/10.1103/PhysRevE.100.042108.
- D. B. Colwell, *Hitting times, number of jumps, and occupation times for continuous-time finite state Markov chains*, Statistics & Probability Letters 195 (2023), https://ideas.repec.org/a/eee/stapro/v195y2023ics016771522300010x.html.
- *A finite-speed return bridge: cuts and midpoint crossover*, https://arivero.github.io/navstokgap/notes/telegraph-return-bridge.html (online technical note; date of first public appearance not verified).
