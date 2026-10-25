# Self-review

## Correctness — PASS
The backward system specifies the gate and boundary conventions explicitly. Stationary averaging diagonalizes the PDE into a diffusion mode and a gate-relaxation mode, giving the full Laplace transform. Expansion supplies the exact mean and variance. Strict logarithmic convexity follows analytically from a positive Laplace integral representation and proves that the inversion parameter has one and only one positive solution. The two endpoint limits give the exact open feasible region. Fifteen independent Laplace-boundary comparisons and five moment-recovery tests passed. These numerical checks are corroboration, not proof of uniqueness.

## Originality — PASS (with residual priority risk)
The 2015 switching-boundary work establishes forward mean calculations, and the 2020 gated-target full text establishes a general transform and moment framework for the same target mechanism. Those results determine the underlying moments in principle, but do not state the injectivity of two scalar moments at one initial location or the complete open feasible moment region. The 2022/2023 inference work studies recovery from richer short-time detection information; no demonstration of the stated two-moment global criterion was identified in its inspected relevant sections and supplement. Direct implication from the forward formulas requires the additional strict log-convexity and onto-range argument. A specialized paper might contain an equivalent inverse derivation, which remains a priority risk.

## Mathematical value — PASS
The fact that only two coarse absorption-time statistics identify both rates, together with an exact realizability inequality, resolves a natural inverse problem for intermittent reaction targets. The sharp variance floor and unbounded fixed-mean variance distinguish physically possible data from impossible data. The value does not depend on numerical enumeration or a general downstream theorem.

## Limitations
The inversion assumes known diffusion/length scales and stationary independent gate preparation. It is exact-data identifiability, not measurement-error robustness. General resetting and nonstationary-gate cases are outside scope. Literature screening cannot establish unconditional historical priority.

Self-review: passed. Independent audit: not yet performed.
