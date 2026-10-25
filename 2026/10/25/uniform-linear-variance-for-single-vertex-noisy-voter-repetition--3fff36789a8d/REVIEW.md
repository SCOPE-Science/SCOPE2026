# Scientific review

## Correctness — PASS
A successful local refresh at an observation time, an all-neighborhood refresh one step later, and matching independent refresh bits at the two lag endpoints force a two-indicator contribution equal to twice a fair Bernoulli. The all-neighborhood refresh severs every possible onward influence of the selected random bit. Sparse times allow simultaneous conditioning and give one full unit of independent conditional variance per favorable site, producing the exact stated finite-sample lower bound. The source's Lemma 2.3 and Theorem 2.7 are used only for the limit/CLT consequence. One hundred fifty exact rational checks independently verified the inequality on small graphs, without being presented as an infinite proof.

## Originality — PASS (best-knowledge, residual historical-priority risk)
The original 2022 preprint expressly identifies potential sublinear growth as unanswered; its later variance dichotomy and conditional CLT do not imply positivity of the variance coefficient. The neighbor-refresh barrier provides a quantitative degree-local argument valid even on infinite locally finite graphs. The examined related noisy-voter papers concern different update schedules or observables. Semantic searches for the same statement, alternate formulations, and general lower bounds did not reveal a dominating result. Earlier general bounded-difference/innovation positivity theorems may in principle imply the conclusion; such an implicit equivalent has not been definitively excluded.

## Value — PASS
The lower bound resolves the explicit variance-growth question for the original statistic in an infinite class of potentially infinite graphs and establishes the nondegenerate normal-limit regime without thinning. Its dependence only on the observation vertex degree and noise parameter gives a useful quantitative estimate uniform in the rest of the graph.

## Closest literature and limits
Benjamini–Helman Tov–Zhukovskii (arXiv:2207.01224), Sections 2.2–2.3, is the exact motivating source. Pymar–Rivera (arXiv:2112.01478) studies a different model/observable. The bound is not claimed sharp; the noise-free and infinite-degree settings are excluded, and independent historical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
