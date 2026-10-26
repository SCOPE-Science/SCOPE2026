# Scientific review

## Correctness — PASS

The conditional first-flip event has a direct coupling to a uniformly random permutation of the initially opposite-majority agent classes, yielding the hypergeometric probability. At the first tip both community majorities agree forever, so the final consensus is determined unambiguously. The binomial weighting and red/blue symmetry recover the unconditional reversal formula, excluding initial global ties. The continuous-time exponential-clock representation and exponential-order-statistic concentration justify the Gaussian comparison; the limiting Cauchy ratio gives the arcsine expression. The encoded `verify.py` independently checks an absorbing Markov recurrence and explicitly enumerates small initial profiles, with exact rational arithmetic. These checks establish finite consistency but are not the universal proof.

## Originality — PASS, subject to stated limits

The directly inspected 2018 node-dynamics paper considers random asynchronous opinion updates on complete and dense random graphs, not the exact complete-bipartite reversal problem. The inspected 2023 asynchronous majority paper has initially absent public opinions and treats binomial random graphs, not publicly initialized complete bipartite networks. A spectral result on voter dynamics treats stochastic neighbor copying rather than deterministic neighborhood majority. Published research searches and current own-history comparison did not reveal a theorem implying the exact finite hypergeometric probability together with the fixed-ratio arcsine limit. A claim with equivalent statement in unindexed work remains an originality risk. A negative search is not proof of uniqueness.

## Value — PASS

The quantitative gap between global vote majorities and final local-interaction consensus is a natural measure of distortion in two-community social aggregation. An exact finite probability law and a nontrivial aspect-ratio phase curve distinguish balanced communities (vanishing asymptotic reversal) from unequal ones (positive asymptotic reversal), with a memorable one-sixth level at three-to-one sizes. This is not just a computational count at a selected graph size: the theorem covers all odd community sizes and explains a structural asymptotic phenomenon.

## Scope of review

Only the single main claim in RESULT.md was assessed. Finite tests cannot establish full generality; the proof handles it. Secondary literatures using alternative update or initialization rules have been distinguished, and inaccessible or unindexed equivalent statements remain a limitation.

Self-review: passed. Independent audit: not yet performed.
