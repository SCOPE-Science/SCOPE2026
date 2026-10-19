# Self-review

## Correctness — PASS

The left tracking formula is an exact solution until the switching ceiling \(n_0=\lceil(1-a)^{-1}\rceil\). The right orbit has an exact weighted-geometric expression, including the neutral limit. Uniform Riemann-sum convergence on the time scale \(n\sqrt{\varepsilon}\) and the strict monotonicity of \(H_\kappa\) prove first-passage convergence, with an \(O(1)\) index remainder at exact critical scaling. In the near-neutral hyperbolic regime, comparing trial indices with \((1+\delta)^n/(L\delta^2/\varepsilon)\to e^{\pm\eta}\) gives the asserted little-o normalized logarithm. Separately implemented recurrence calculations and exact-rational checks pass. Numerical tests do not establish the infinite asymptotic claim.

## Originality — PASS with residual priority uncertainty

The most direct paper, Simpson (arXiv:2406.04587, sections 3 and 8), establishes global forward divergence for frozen nonsmooth folds under nondegeneracy; it supplies no nonautonomous sweep time and excludes a singular unit right multiplier. Budd and Kuske (arXiv:2305.09902, Lemma A and section 2) obtain logarithmic drift delay for a continuous-time absolute-value flow with fixed slopes, but not the stated joint discrete multiplier–sweep function. Chu, Lin and Tsai (arXiv:2311.07242, Theorems 1-2) examine discrete *quadratic smooth* saddle-node passage with a different scaling. The available abstract of Kiers (arXiv:1907.11601) is qualitative; its full text was not accessible. Searches of equivalent titles, mathematical statements, border-collision aliases and related indexed records disclosed no dominating claim, but do not establish uniqueness. Implicit coverage through another normal form remains the main priority risk.

## Mathematical value — PASS

The right multiplier approaching one is the natural breakdown boundary of the frozen border equilibrium, and it changes the physical number of steps needed to reach a fixed post-fold threshold. A complete two-parameter crossover \(\delta/\sqrt{\varepsilon}\) and an exact near-neutral logarithmic balance are motivated dynamical quantities rather than numerical enumeration or a rephrased static bifurcation. The result remains deliberately limited to the stated affine scalar model, without claims of nonlinear perturbation robustness.

## Limitations

The theorem treats only one explicitly chosen negative-time tracking history, fixed left contraction and positive observation level. An inaccessible general discrete tipping paper and nonexhaustive older-literature coverage leave documented originality uncertainty; independent assessment is still necessary.

Self-review: passed. Independent audit: not yet performed.
