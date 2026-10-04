# Review

## Correctness

PASS. The scalar compressed MARINA estimator is exactly multiplicative between full-gradient refreshes. With density-matched refresh probability \(1/2\), refresh cycles are iid and the cycle sum obeys a one-line perpetuity recursion. Its first two moments give the exact squared refresh multiplier \(\psi_n(s)\). The sign of \(\psi_n(s)-1\) is controlled by the quadratic \((n+2)s^2-ns-2n\), and the within-cycle second moment is finite throughout the candidate stable interval. This makes the positive root a necessary-and-sufficient all-time mean-square boundary.

Risk: the regenerative reduction depends crucially on identical scalar client curvatures and independent compression.

## Originality

PASS. The defining MARINA paper supplies the algorithm, density-matched refresh choice, and general sufficient stepsizes, but the inspected full text does not derive an exact scalar mean-square frontier. The later permutation-compressor paper refines MARINA theory and studies quadratic tasks empirically, including larger tolerated stepsizes, but does not state the regenerative half-dropout formula. Focused semantic searches over MARINA, scalar quadratics, Bernoulli compression, random products, regeneration, and exact mean-square stability found no covering statement.

The closest published database results concern other stochastic quadratic recurrences or unrelated sharp stability frontiers and do not imply the MARINA cycle law.

## Value

PASS. MARINA's main design feature is the alternation between exact-gradient refreshes and compressed gradient differences. The exact scalar frontier quantifies how those two mechanisms interact and shows a non-obvious parallelism effect: independent client averaging pushes the true stability ceiling from \(1\) at one client to the uncompressed gradient-descent ceiling \(2\). This gives a sharp benchmark for interpreting general stepsize theorems and for testing implementations of compressed MARINA.

Same-model review: passed. Independent audit: not yet performed.
