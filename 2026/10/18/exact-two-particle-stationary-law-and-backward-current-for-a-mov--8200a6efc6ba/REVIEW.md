# Self-review

## Correctness — PASS

The result specifies a fixed-duration moving defect with rates \(p/2\) only for particle exits from the active site, exactly two particles, and a pre-dwell comoving observation convention. Writing \(z=e^{-p/(2v)}\), the one-dwell transition kernel has three explicitly derived alternatives: no hop, one permitted exit, or two permitted exits. The four-class weight formula is normalized by exact combinatorial counting, and seven disjoint target classes establish every stationarity balance equation for arbitrary ring length \(L\geq3\). The connected two-token graph and a positive-probability full tour implement every elementary exclusion move, establishing uniqueness when \(0<z<1\). The two adjacent-pair configurations yield the exact signed displacement and bond-current factor \(v/L\). All claimed limiting coefficients follow from direct expansions. Independent numeric solves for \(3\leq L\leq11\) and exact symbolic balances for \(3\leq L\leq20\) confirmed the formulas. These finite checks support but do not substitute for the all-size proof.

## Originality — PASS

The original moving-defect model (Chatterjee et al., 2014; DOI `10.1103/PhysRevE.89.022138`) gives hopping probabilities and exact identities involving *unknown* conditional correlations; its explicit transport predictions use mean-field factorization. Those identities do not evaluate the complete two-particle stationary distribution or its all-ring exact current. The 2016 multiple-defect and ordered-update treatment (DOI `10.1103/PhysRevE.93.062124`) and the 2023 moving-barrier interaction analysis (DOI `10.1103/PhysRevE.108.034107`) study related dynamics but do not imply the stated four-class distribution in the material examined. Indexed record comparisons found no matching statement or stronger result implying it; the highest semantic similarities concerned unrelated Markov/dynamical transport and topological particle-configuration problems. Residual risk remains from unindexed or differently phrased earlier work; absence from a search is not mathematical evidence of uniqueness.

## Value — PASS

This supplies a complete closed stationary law, rather than a small additional numerical sample, for the first genuinely interacting particle sector of a physically motivated periodically driven exclusion model. It converts previously correlation-dependent exact transport identities into a formula for every finite ring and driving speed, proves strict backward pumping without mean-field assumptions in this sector, and gives finite-size and slow-/fast-drive coefficients suitable as exact benchmarks. Two particles are the smallest sector in which exclusion affects the current: with one particle the local left/right exit probabilities cancel. The fixed particle count is dictated by this minimal-interaction gap, not an arbitrary parameter slice. The result does not claim a theorem for finite positive density or general interactions.

## Sources and limitations

Closest primary literature: Chatterjee et al. (2014), arXiv `1404.4144`; Chatterjee et al. (2016), arXiv `1602.02691`; Das et al. (2023), arXiv `2304.06606`. Supporting MSC2020 ownership is 82C22 (interacting particle systems). Explicit restrictions: exactly two particles; one defect; finite positive dwell and hop rates; no bulk or inward-defect hopping; one-dimensional ring with \(L\geq3\). Bibliographic incompleteness remains possible, and independent audit has not taken place.

Self-review: passed. Independent audit: not yet performed.
