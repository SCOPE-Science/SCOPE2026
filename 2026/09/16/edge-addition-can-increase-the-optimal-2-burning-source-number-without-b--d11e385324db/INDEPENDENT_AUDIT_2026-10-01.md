# Independent mathematical audit — SCOPE-20260916-013

Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Correctness
**PASS** — The proof was reconstructed from the definitions. On each unchanged source-free arm, propagation can advance by at most one arm vertex per round after both universal vertices are blue, so its endpoint cannot be blue before round L+2. The two-source schedule proves b_2(H)=L+2 and t_2(H)=2. The displayed G schedule finishes by L+1, so every time-optimal G schedule must seed each of the k=q+2 unchanged arms, giving t_2(G)>=q+2. A fresh exhaustive seven-vertex implementation independently reproduced (b_2,t_2)=(4,2) for H and (3,3) for G.

## Originality
**PASS** — The current published source itself still states Lemma 2.4 claiming t_2 monotonicity under spanning supergraphs; its proof only transfers a schedule and therefore controls completion time, not the secondary optimum evaluated at the new minimum time. Searches for corrections, counterexamples, fixed-deadline formulations, generalized burning, and the exact universal-vertex/spider construction found no prior equivalent or stronger counterexample. The inspected parent-process paper remains a residual access risk rather than positive coverage evidence.

### Equivalent formulations
The equivalent constrained-optimization formulation explains exactly why schedule transfer does not imply the published t_2 inequality and was not located as a prior counterexample.

### Broader coverage
The directly relevant published theorem is contradicted, not a stronger covering theorem.

### Exact database or table check
This is a theorem/counterexample claim rather than a database lookup; absence of a hit is used only as supporting search evidence, not as novelty proof.

### Claim versus prior implication
The claim is logically incompatible with the cited prior assertion and therefore cannot be a corollary of it; the new content is the correction and unbounded witness.

## Value
**PASS** — An explicit unbounded counterfamily corrects a published comparison principle for a named parameter and isolates the changing-deadline mechanism. That is a motivated structural counterexample, not a tiny-instance anomaly.

## Source inspections
- **The 2-burning number of a graph** (https://doi.org/10.61091/ars161-16): COVERED ASSERTION, NOT COVERED CORRECTION. Current publisher HTML through Definitions 2.1--2.3, Lemma 2.4 and its proof, path/cycle consequences, and surrounding discussion. Lemma 2.4 explicitly states both b_2 and t_2 monotonicity under spanning supergraphs; the proof transfers a sequence but does not preserve optimal completion time.
- **The generalized burning number of graphs** (https://doi.org/10.1016/j.amc.2021.126306): ACCESS RISK. Bibliographic/abstract-level material only; full theorem text was not available during this audit. Related parent process; no concrete theorem implying the audited t_2 counterfamily was identified.

## Residual risks
- A related 2021 generalized-burning paper was not available in full text during this audit; no specific covering theorem was identified.
- The correction is tied to the currently published 2024 article text inspected on 2026-10-01 UTC; a future erratum would change the historical framing.

The accompanying JSON file records the four structured originality checks, source inspections, checked sources, and residual risks.
