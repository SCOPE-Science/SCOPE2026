# Scientific review: exact asynchronous star consensus covariance

**Correctness — PASS.** The graph, activation rule and complete-confidence hypotheses are fixed and explicit. Direct hub/leaf updates give a two-dimensional conditional-moment closure, and the coefficients in the harmonic quadratic are verified symbolically. A bounded martingale supplies almost-sure consensus and the exact second moment. The included checker passed 872 independently evaluated exact-rational assertions, while the proof—not finite checking—covers all finite star sizes and arbitrary opinion dimension.

**Originality — PASS, with residual priority uncertainty.** The exact model appears in Berenbrink et al. (arXiv:2201.12923), which addresses convergence bounds rather than exact consensus variance. Elboim–Peres–Peretz (arXiv:2209.05764) is the most important broader source: it applies general random-updating martingale theory and bounds consensus variance for arbitrary reversible networks, but its inspected Corollary 2.4 does not determine the present exact coefficients or the \(1/18\) limit. The *Distributed Averaging* NodeModel (arXiv:2211.17125) instead fixes a common self-weight and samples neighbors. An unexamined general exact covariance result remains a material priority risk; search cannot establish unique priority.

**Value — PASS.** The exact variance law answers how much randomness in activation order survives after agreement on a hub-dominated social network. The nonzero large-star limit is quantitatively informative even when adding arbitrarily many unanimous leaves. All initial star configurations are covered by a two-term covariance expression; this is a motivated structural question, not merely a small graph sample.

**Limits.** Only fully active confidence edges, uniform asynchronous activation and equal self-plus-neighbor averaging are proved. The full limit law, arbitrary graphs, switching neighborhoods and independent publication-priority validation remain outside scope.

Self-review: passed. Independent audit: not yet performed.
