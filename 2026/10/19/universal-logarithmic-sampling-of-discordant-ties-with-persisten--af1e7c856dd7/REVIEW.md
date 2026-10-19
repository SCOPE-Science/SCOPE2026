# Self-review

**Correctness — PASS.** The exact conditional selection hazard of a negative edge after its \(n\)-th encounter is trapped between positive constants times \(\delta_e^n\). Its next waiting time has two summable geometric tail bounds. Borel–Cantelli converts these bounds into the almost-sure logarithmic encounter law. The bounded-martingale strong law then yields uniform limiting use of receptive edges, and the exact weight recursions give both weight exponents. Countable coupling transfers the conclusions to any eventually fixed mixed receptive/unreceptive partition. The numerical program was run successfully; experiments support but do not replace this proof.

**Originality — PASS, with residual risk.** The 2026 Thompsky–Wu–Porter–Luo paper [1] proves almost-sure binary edge-weight limits and stabilization of effective graphs; it does not derive exact calendar-time logarithmic contact counts. McNulty–Raban [2], Sections 2.1–2.3 and Appendix B.2, obtains positive sampling frequencies for *strictly discounted coordinates only*, which does not cover the stated mixed positive/negative updates. Earlier negatively reinforced urn results [3] use different occupancy-weighted mechanisms. Primary texts and mathematical-record searches did not reveal an implication covering the stated result; general stochastic sampling theorems or unindexed studies might still subsume it.

**Mathematical value — PASS.** The theorem distinguishes the limiting disappearance of a social tie from its ongoing interaction burden: discordant contacts persist logarithmically even as their weights decay with a universal inverse-time exponent. The count coefficient reveals individual forgetting parameters while the surviving receptive graph receives asymptotically all contacts. This is a natural rate question raised by the model's binary-limit theorem, with an explicit three-agent realization and heterogeneous edge-rate robustness.

The conclusion requires finite graphs, strictly interior initial weights and both eventual classes nonempty. It does not imply the effective graph always stabilizes, nor give finite-window statistical guarantees. No novelty or correctness claim has been independently audited.

Self-review: passed. Independent audit: not yet performed.

**Closest sources:** [1] arXiv:2605.20418v1, Sections III–IV; [2] arXiv:2607.20818v1, Sections 2.1–2.3 and Appendix B.2; [3] arXiv:1808.00796, main definitions and laws.
