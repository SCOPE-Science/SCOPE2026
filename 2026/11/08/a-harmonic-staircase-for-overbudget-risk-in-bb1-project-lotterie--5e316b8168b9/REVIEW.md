# Scientific review: a harmonic staircase for overbudget risk

## Correctness — PASS

The exact scope is a lottery over \(k\) unit-cost projects and one project of noninteger cost \(1<c<k\), with equal cheap-project marginals \(1-cq/k\) and exceptional-project marginal \(q\). The omitted-cheap count \(Z\) satisfies \(\mathbb E Z=cq\). The cap forces \(Z\ge\max\{0,\lceil c-\delta\rceil\}\) when the exceptional project is selected, and a non-overbudget exceptional-project outcome needs \(Z\ge\lceil c\rceil\). The resulting moment lower bound on overrun probability is attained by a three-type lottery, using cyclic omission blocks to preserve **every** individual marginal. The proof checks BB1 separately in all types, not merely average spending. The integer-cost boundary is handled separately. Finite tests cover 2,940 exact rational constructions and 420 independent complete-distribution linear programs; these support but do not replace the infinite proof.

## Originality — PASS, subject to priority risk

Aziz et al. (2024), Definition 3.1 and Theorem 3.2, give the underlying BB1 requirement and general implementation existence. Their accessible full text, especially Sections 2–3 and Proposition 3.4, does not state an optimum probability of budget exceedance under a bounded permitted overspend or the associated harmonic thresholds. General dependent rounding, joint mixability, and Bernoulli-tail coupling are adjacent frameworks; the inspected evidence does not identify a theorem already deriving this particular risk-cap formula. The general fixed-marginal coupling linear program can of course represent the problem; the claim is its exact, sharp explicit solution on the specified project-cost family, not the existence of a computable finite linear program. Abstract-level sources do not rule out all stronger results, and unindexed or differently named exact formulas remain a priority risk.

## Value — PASS

BB1 alone limits each budget error by removing **some** project but does not quantify how often hard budget limits are exceeded. The theorem provides the complete exact tradeoff between that frequency and the maximum acceptable overrun, including a sharp infeasibility boundary, discontinuous policy thresholds, explicit optimal lotteries and a linear-size support bound. This is a natural interpretation issue for randomized participatory budgeting rather than an arbitrary numerical subinstance. The symmetry restriction is necessary for the stated simple sharp construction and is acknowledged.

## Sources and scope limitations

Primary: https://arxiv.org/abs/2404.05198 and https://doi.org/10.1609/aaai.v38i9.28801. Adjacent: https://doi.org/10.1145/1147954.1147956 ; https://doi.org/10.1287/ijoo.2019.0038 ; https://doi.org/10.1287/moor.2015.0755. The comparison with the latter three works is limited to accessible bibliographic descriptions and mathematical scope, not a full-text exclusion. The proposed risk frontier adds no voter-fairness axiom and does not apply to general heterogeneous cheap-project marginals.

Self-review: passed. Independent audit: not yet performed.
