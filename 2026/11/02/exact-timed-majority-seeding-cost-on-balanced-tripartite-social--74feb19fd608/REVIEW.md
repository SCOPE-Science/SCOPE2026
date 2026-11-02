# Scientific assessment

## Correctness — PASS

The full proof applies for every positive integer \(m\), with the special case \(m=1\) treated separately. The key homogeneity lemma is immediate from the false-twin structure of the three classes. The lower bound is established by classifying the first nonempty natural state and exhausting the possible use of any remaining intervention under a hypothetical budget of \(m+2\). This excludes all schedules, including schedules with repeated targeting and arbitrary delays. The upper bound gives explicit intervention times and natural states. The static comparison uses three necessary-and-sufficient pairwise initial count inequalities, with feasible balanced integers attaining their summed lower bound. The standalone verifier independently checks all labelled intervention actions for \(m\le4\), type-count shortest paths through \(m=60\), and static optima through \(m=30\). Finite checks do not establish the infinite theorem by themselves.

## Originality — PASS, with priority limitations

Closest published source: Soltani, Zehmakan, and Hushmandi, *Minimum Target Sets in Non-Progressive Threshold Models: When Timing Matters* (arXiv:2307.09111, July 18, 2023). Its formal model, general lower bounds, star and complete-bipartite examples, general algorithms, and tree-specialized solution were examined. The general bounds are not exact for the balanced tripartite family; the bipartite and tree constructions do not cover the graph with triangular type quotient. Also inspected: Dvořák, Knop, and Toufar, *Target Set Selection in Dense Graph Classes* (arXiv:1610.07530, October 24, 2016), whose irreversible progressive dynamics is not the studied timed non-progressive process. Targeted literature searches and mathematical-record comparisons identified no dominating or equivalent statement. This supports a best-knowledge originality assessment, not an assertion that all possible publications have been excluded. An unindexed prior exact tripartite calculation remains a risk.

## Value — PASS

Three interacting equal-size communities form the smallest complete multipartite family not bipartite. The exact all-size timing optimum \(m+3\) differs structurally from the best initial-only budget \(\lceil3(m+1)/2\rceil\); the intervention gap is unbounded, with an asymptotic one-third saving and sharp first strict saving at \(m=4\). This gives a meaningful dense-network benchmark for the effect of intervention timing and a nontrivial first-positive-state obstruction in the proof. No claim is made beyond the stated graph and threshold model.

## Scope and unresolved literature risks

The first public motivating source is dated July 18, 2023. The proof does not handle unequal community sizes, four or more communities, different thresholds, or interventions subject to an availability constraint. Targeted full-text inspection of the source and separate published-record searches cannot prove global publication uniqueness. Independent external validation has not been carried out.

Self-review: passed. Independent audit: not yet performed.
