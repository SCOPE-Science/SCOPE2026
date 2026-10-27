# Rare-survivor exponential clock and moment bifurcation under weak synthesis–degradation

## Finding

Let \(\tau\) be the strictly positive, almost surely finite first-passage time of one nondegrading searcher and suppose \(\mathbb E[e^{a\tau}]<\infty\) for some \(a>0\). Write \(m=\mathbb E\tau>0\). Start one searcher at time zero; recruit independent identical searchers according to a Poisson process of rate \(b=\beta\varepsilon\); kill each at an independent exponential rate \(d=\delta\varepsilon\), where \(\beta,\delta>0\) are fixed and \(\varepsilon\downarrow0\). Let \(T_\varepsilon\) be the first successful arrival of any searcher. Then the following statements hold simultaneously:

1. The laws converge in total variation, with the quantitative estimate
   \[d_{\mathrm{TV}}(\mathcal L(T_\varepsilon),\mathcal L(\tau))\le(\beta+\delta)m\varepsilon.\]
2. For every fixed \(u>0\), the exceptional survival probability has the sharp scaling
   \[\lim_{\varepsilon\downarrow0}\varepsilon^{-1}\Pr(T_\varepsilon>u/\varepsilon)=\delta m e^{-\beta u}.\]
   Conditional on the event \(H_\varepsilon\) that the initially present searcher dies before its own unimpeded first passage, the long waiting clock satisfies
   \[\varepsilon T_\varepsilon\mid H_\varepsilon\ \Longrightarrow\ \operatorname{Exp}(\beta).\]
3. Every real moment order has a sharp transition at one: for \(0<q<1\),
   \[\mathbb E[T_\varepsilon^q]\longrightarrow\mathbb E[\tau^q];\]
   for \(q=1\),
   \[\mathbb E[T_\varepsilon]\longrightarrow m(1+\delta/\beta);\]
   and for every real \(q>1\),
   \[\lim_{\varepsilon\downarrow0}\varepsilon^{q-1}\mathbb E[T_\varepsilon^q]=\frac{\delta m\Gamma(q+1)}{\beta^q}.\]
   In particular,
   \[\lim_{\varepsilon\downarrow0}\varepsilon\,\mathrm{CV}^2(T_\varepsilon)=\frac{2\delta}{m(\beta+\delta)^2}.\]

The first-moment limit and the finite-rate survival identity are prior published results; the quantified exceptional-clock limit and real-order moment classification above are the additional conclusions under assessment. Total-variation convergence and divergent variance can therefore coexist in one and the same family of first-passage distributions.

## Assumptions and scope

Each searcher, in isolation, has an independent copy of \(\tau\) as its target-arrival time, and a separate independent exponential mortality time; all searcher trajectories, mortalities and Poisson recruitment events are mutually independent. Searchers cannot continue after death. Target detection by any surviving searcher stops the system. The initial searcher is alive at time zero. The parameters \(\beta,\delta\) are positive and do not depend on \(\varepsilon\). The theorem permits any spatial dimension or search mechanism admitting this independent-searcher reduction and the exponential moment assumption. The diffusion-in-a-bounded-domain example satisfies this moment condition; unbounded-domain searches with heavy-tailed bare first-passage times are not covered.

## Proof

**Exact starting identity (published).** Denote \(S(t)=\Pr(\tau>t)\), and for \(d>0\) set
\[g_d(t)=\mathbb E[(1-e^{-d\tau})\mathbf1_{\{\tau\le t\}}],\qquad J_d(t)=\mathbb E[e^{-d\tau}(t-\tau)_+].\]
The single-mortal-searcher non-arrival probability is \(S(t)+g_d(t)\). The Poisson probability generating functional for the immigrant searches yields the exact survival expression
\[\Pr(T_\varepsilon>t)=\{S(t)+g_{\delta\varepsilon}(t)\}\exp[-\beta\varepsilon J_{\delta\varepsilon}(t)].\tag{1}\]
This formula was obtained in the cited prior studies and is not itself the novel result.

**Total-variation coupling.** Construct \(T_\varepsilon\) and \(\tau\) on the same space, using the initial searcher's trajectory in both. Unless a birth or the initial death occurs before time \(\tau\), both completion times are identical. The total rate of such competing events is \((\beta+\delta)\varepsilon\), hence
\[\Pr(T_\varepsilon\ne\tau)\le\mathbb E[1-e^{-(\beta+\delta)\varepsilon\tau}]\le(\beta+\delta)m\varepsilon.\]
The coupling inequality proves assertion 1.

**Exceptional clock.** Fix \(u>0\). Exponential integrability gives \(S(u/\varepsilon)=o(\varepsilon)\). Dominated convergence gives
\[\varepsilon^{-1}g_{\delta\varepsilon}(u/\varepsilon)\longrightarrow\delta m,\qquad \varepsilon J_{\delta\varepsilon}(u/\varepsilon)=\mathbb E[e^{-\delta\varepsilon\tau}(u-\varepsilon\tau)_+]\longrightarrow u.\]
Substitute into (1) to get assertion 2's rare-tail limit. Also,
\[\Pr(H_\varepsilon)=\mathbb E[1-e^{-\delta\varepsilon\tau}]\sim\delta m\varepsilon.\]
On \(H_\varepsilon^c\), the initial searcher is certain to arrive by \(\tau\), so \(\Pr(T_\varepsilon>u/\varepsilon,H_\varepsilon^c)\le S(u/\varepsilon)=o(\varepsilon)\). Dividing the rare-tail asymptotic by \(\Pr(H_\varepsilon)\) proves the conditional exponential survival function at every positive \(u\); convergence in distribution follows (including at zero by continuity of the exponential distribution).

**Real-order moments.** For any \(q>0\), write the tail integral \(\mathbb ET_\varepsilon^q=A_\varepsilon(q)+B_\varepsilon(q)\), with
\[A_\varepsilon(q)=q\int_0^\infty t^{q-1}S(t)e^{-\beta\varepsilon J_{\delta\varepsilon}(t)}\,dt,\qquad B_\varepsilon(q)=q\int_0^\infty t^{q-1}g_{\delta\varepsilon}(t)e^{-\beta\varepsilon J_{\delta\varepsilon}(t)}\,dt.\]
The first term converges by dominated convergence to \(\mathbb E\tau^q\). For the second term, change variables \(u=\varepsilon t\):
\[\varepsilon^{q-1}B_\varepsilon(q)=q\int_0^\infty u^{q-1}\frac{g_{\delta\varepsilon}(u/\varepsilon)}{\varepsilon}\exp[-\beta\varepsilon J_{\delta\varepsilon}(u/\varepsilon)]\,du.\tag{2}\]
To justify domination, choose \(M>0\) with \(\Pr(\tau\le M)>0\), and \(\varepsilon_0>0\). Uniformly for \(\varepsilon\le\varepsilon_0\),
\[0\le g_{\delta\varepsilon}(t)/\varepsilon\le\delta m,\qquad J_{\delta\varepsilon}(t)\ge c(t-M)_+\]
where \(c=e^{-\delta\varepsilon_0 M}\Pr(\tau\le M)>0\). Thus the integrand of (2) is bounded by a constant times \(u^{q-1}e^{-\beta c u}\), integrable for every real \(q>0\). Dominated convergence yields
\[\lim_{\varepsilon\downarrow0}\varepsilon^{q-1}B_\varepsilon(q)=q\delta m\int_0^\infty u^{q-1}e^{-\beta u}\,du=\frac{\delta m\Gamma(q+1)}{\beta^q}.\]
If \(q<1\), this means \(B_\varepsilon(q)\to0\); if \(q=1\), it yields \(B_\varepsilon(1)\to\delta m/\beta\); if \(q>1\), it gives the asserted leading moment after multiplying by \(\varepsilon^{q-1}\), because \(A_\varepsilon(q)=O(1)\). Finally apply the results for \(q=1,2\) and subtract the bounded squared mean from the diverging second moment. This proves the coefficient-of-variation law and completes the theorem.

## Verification

The standalone script `verify.py` checks the unexpanded exact survival function in two independent bare-search examples: exponential first-passage time and deterministic first-passage time. For rates \(\varepsilon=0.002\) and \(0.0003\), it compares three rescaled tail probabilities, the first moment, and the rescaled second and third moments against the asymptotic expressions for each example. There are 24 finite-parameter comparisons, all passing. The numerical examples check consistency only; equations (1)–(2), the coupling and the dominated-convergence bounds supply the infinite-parameter proof.

Run with `python verify.py` in an environment with Python, SciPy and its dependencies installed. The script requires no data downloads.

## Relationship to prior work

Mercado-Vásquez and Boyer (2026), arXiv:2602.11095v1, give the exact survival representation (equation (7)), the first-moment small-rate expansion (equation (14)), and the low-rate mean discontinuity (equation (15)); their discussion qualitatively notes rare early mortality and a long wait for immigration. Linn and Kumar (2026), arXiv:2601.07096v1, independently obtain the same general recruitment–mortality survival expression (their equation (2)) and discuss coefficient of variation in the **high-turnover** regime in supplementary section S2. These prior identities and the mean discontinuity are not novelty claims.

The additional mathematical assertion is the **joint** sharp, low-turnover rare-tail profile and conditional exponential law for an exceptional subpopulation, together with the real-order \(q=1\) moment bifurcation and its exact constants. These singular statements require nonuniform treatment of time scales and moment integrals; they are not equivalent to simply restating an ordinary fixed-rate survival formula. General consequences of the earlier exact survival identity nevertheless create an originality risk, and independent priority checking is advisable.

## Limitations

The underlying isolated search must have some finite exponential moment, ensuring sufficiently small intrinsic survival probability on the inverse-turnover scale. All immigration and mortality clocks are independent and Poisson/exponential. The asymptotics hold with a fixed positive ratio \(\beta/\delta\), not when the two rates vanish on different orders. No result is asserted for heavy-tailed bare completion times, correlated searchers, or spatially distributed birth locations. The conclusion is distributional and analytic, not an experimental identification of a physical system. All prior first-moment results are explicitly excluded from novelty.

## References

- G. Mercado-Vásquez and D. Boyer, *Stochastic synthesis-degradation processes: first-passage properties and connections with resetting*, arXiv:2602.11095v1 (first public version 11 February 2026), https://arxiv.org/html/2602.11095v1.
- S. Linn and A. Kumar, *Dynamic redundancy and mortality in stochastic search*, arXiv:2601.07096v1 (11 January 2026), https://arxiv.org/abs/2601.07096; Physical Review Letters 137, 097102 (2026).
