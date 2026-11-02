# Self-review

## Correctness — PASS

The graph has precisely three paths and edge loads \((q-h_D,h_U,h_D,q-h_U,h_M)\). Verify the Wardrop baseline identity \(\Psi(f)=qL\), the unit-coefficient case split for all signs with at least one nonnegative outer-flow difference, and the exact cancellation \(c_U(g)+c_D(g)=c_M(g)+L-R\) when both differences are negative. Four terms in \(R\) are nonnegative from Wardrop and monotonicity. Regret on the used center path and the two-path sum yield the global bound with deficit. For positive-regret equality all intervening inequalities are equalities: only the center path remains used at \(g\), and each nonnegative slack term vanishes. The converse and a nonzero-middle-flow sharp witness are explicitly verified. Exact-rational finite tests cover 600 models and 85,800 flows, plus 12 equality instances; they supplement rather than replace the universal proof.

## Originality — PASS, with residual priority risk

The closest 2024 paper explicitly establishes \(2\varepsilon\) for a *specified* Wheatstone latency example and states qualitative universal topology-dependent bounds; it does not state the all-latency rigidity iff or the explicit nonnegative deficit certificate. The 2014 mean-risk paper proves a related factor \(2\) for multiplicative price of risk aversion, not the classification of positive additive-regret extremizers or the exact plateau slack. The 2019 satisficing paper derives multiplicative ratio bounds. Searches for equality classifications, plateaus, additive-regret extremizers, and source/claim aliases did not find an indexed equivalent. Di et al. (2014) addresses BRUE on the same network, making it a substantial residual source risk: publisher full text was not obtained, and its abstract alone cannot settle noncoverage. The result's originality lies in rigidity and the \(R\) certificate rather than reasserting the factor or witness as novel.

## Mathematical value — PASS

This is a natural complete characterization of saturation for a topology that first exhibits the factor \(2\) in bounded-rationality routing. It identifies the unique saturating support pattern and an exact structural obstruction: latency changes on three particular links reduce the achievable excess by a quantitative nonnegative margin. These facts distinguish merely possible worst-case loss from actually attainable loss, and identify how generic strictly increasing latencies prevent exact saturation. They are not arbitrary parameter substitutions or a numerical restatement of the known example.

## Limits and literature

Single commodity, directed five-edge graph, continuous nonnegative nondecreasing latencies, and positive regret for the iff. Open priority risk: full text of Di, He, Guo and Liu (2014), doi:10.1016/j.trb.2014.04.005. Also compare Massicot–Langbort arXiv:2406.00295 §3.2 and Appendix A, Nikolova–Stier-Moses arXiv:1411.0059 §4–5, and Takalloo–Kwon arXiv:1911.07914 §4. No claim of independent scientific validation is made.

Self-review: passed. Independent audit: not yet performed.
