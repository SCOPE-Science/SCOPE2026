# Review status

Fresh independent mathematical audit completed on 2026-10-01 UTC.

Disposition: **passed**.

- Correctness: **PASS** — The proof was reconstructed from the definitions. On each unchanged source-free arm, propagation can advance by at most one arm vertex per round after both universal vertices are blue, so its endpoint cannot be blue before round L+2. The two-source schedule proves b_2(H)=L+2 and t_2(H)=2. The displayed G schedule finishes by L+1, so every time-optimal G schedule must seed each of the k=q+2 unchanged arms, giving t_2(G)>=q+2. A fresh exhaustive seven-vertex implementation independently reproduced (b_2,t_2)=(4,2) for H and (3,3) for G.
- Originality: **PASS** — The current published source itself still states Lemma 2.4 claiming t_2 monotonicity under spanning supergraphs; its proof only transfers a schedule and therefore controls completion time, not the secondary optimum evaluated at the new minimum time. Searches for corrections, counterexamples, fixed-deadline formulations, generalized burning, and the exact universal-vertex/spider construction found no prior equivalent or stronger counterexample. The inspected parent-process paper remains a residual access risk rather than positive coverage evidence.
- Value: **PASS** — An explicit unbounded counterfamily corrects a published comparison principle for a named parameter and isolates the changing-deadline mechanism. That is a motivated structural counterexample, not a tiny-instance anomaly.

Full evidence, structured originality comparisons, source inspections, and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.

The earlier same-model assessment remains historical evidence and is not relabeled as this independent assessment.
