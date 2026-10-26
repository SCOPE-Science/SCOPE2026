# Self-review

## Correctness — PASS

The model fixes independent uniform parent choices and the target statistics before analysis. The ancestor-event decomposition is valid because an ancestral event for vertex \(t\) depends only on choices later than \(t\). Its exact probability is \(1/t\) for any later target, yielding the local covariance identity. A discrete partial summation proves the exact cross-vertex covariance. Subtraction of consecutive rational formulas proves monotonicity; the Euler–Maclaurin inverse-square tail yields the two scaling limits and sign transition. The standalone verifier independently enumerated every parent array through nine vertices and checked 4791 exact assertions and ancillary numerical threshold comparisons. Finite checks do not prove the infinite assertion.

## Originality — PASS (provisional priority)

Full accessible treatments by Devroye–Fawzi–Fraiman and Kuba–Wagner establish depth results but not the exact prescribed-label outdegree versus last-depth covariance. Lodewijks develops asymptotic joint properties of degrees and depths of prescribed vertices, not this order-\(1/n\) finite covariance sign transition. The closest identified research records concern root attachment versus aggregate path length or root degree versus leaf count, neither of which implies the newest-vertex covariance profile. Publication priority remains at risk from older general recursive-tree covariance identities and inaccessible historical literature, and merits independent expert comparison.

## Mathematical value — PASS

Root attachments intuitively shorten remote ancestral paths, but children of late vertices carry a competing direct ancestor effect. The proven sign reversal pinpoints the exact boundary between these phenomena for every tree size, and the nontrivial \(\sqrt n\) crossover with lattice-scale \(1/6\) correction shows a structural transition invisible in marginal depth or degree expectations and in leading asymptotic joint normality. It is a natural conditional-dependence question rather than an arbitrary small-parameter tabulation.

## Limitations

Uniform recursive trees only; degree and depth are related by covariance, not an asserted stochastic ordering. There is no independent scientific audit and historical priority is provisional.

Self-review: passed. Independent audit: not yet performed.
