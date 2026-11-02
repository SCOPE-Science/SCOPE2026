# Scientific assessment

## Correctness — PASS

For every integer \(n\ge5\), the theorem defines one family of unit-row randomized Kaczmarz matrices with positive complete inverse-Gram interactions except a single negative edge. Congruence reduces the worst-direction one-step optimization exactly to a minimum-trace diagonal semidefinite majorant. The weak-edge slack is a sum of squares with coefficient \(m/2-t\), so is positive semidefinite on precisely the claimed branch; the dual rank-one all-ones correlation matrix matches its objective. On the strong branch, the slack factors as a rank-one positive form plus a positive multiple of a complete-graph Laplacian on interior indices. A matching rank-two correlation matrix has diagonal one, is positive semidefinite, and exactly matches the primal trace. Complementary slackness fixes every diagonal, proving uniqueness without restricting other probability vectors to be symmetric. Kernel dimensions are obtained from the displayed factorizations, including the threshold. An implicit-function argument guarantees nonempty normalized examples for small weights. The standard-library verifier passed 47,263 assertion checks across 124 rational certificate cases and 28 normalized-system eigenvalue cases. Finite verification supports but does not establish the universal formulas. No correctness blocker was identified.

## Originality — PASS on checked evidence, with residual risk

Dai, Soltanalian and Pelckmans, arXiv:1402.2863, supply the general SDP optimized-sampling formulation, but inspection of their statements, derivation, approximation section, experiments, and conclusion found no complete-graph single-negative-edge closed-form optimizer, antagonism threshold, uniqueness or rank transition. Wang, Agaskar and Lu, arXiv:1502.00190, analyze exact MSE for inconsistent systems via a lifted recursion rather than the constrained one-step phase law. The 2014 Agaskar–Wang–Lu paper's title and accessible abstract are relevant, but its complete text could not be obtained despite lawful open-access and institutional attempts; no whole-document absence claim is made. An adjacent published result on inverse-positive coordinate sampling does not cover a graph whose signed triangles prevent diagonal sign switching to an entrywise nonnegative inverse. Existing sparse signed triangle, four-cycle, forest and signed-cycle Kaczmarz results do not imply the dense clique solution. Specialized older elliptope/spin-system treatments could conceivably contain an equivalent scalar optimization. Search absence is not proof of novelty, so the positive assessment is bounded to the available inspected evidence.

## Mathematical value — PASS

The mathematical question is motivated by robust fixed-iid row selection for correlated equation systems, especially an otherwise homogeneous dense interaction structure disrupted by one antagonistic pair. The exact transition \(t=(n-2)/2\) is structural: the optimizer changes from a signed row-sum rule to a rational two-level rule, and the optimal slack nullity changes from one to two. Dense positive redundancy makes the threshold grow linearly with dimension; the corresponding sparse-cycle threshold shrinks with dimension, so neither model is a mere reparameterization. A closed-form, uniquely specified sampling law removes the general SDP solve for an infinite family. No multistep or practical performance claims beyond the sharp one-step rate are needed for this value assessment.

## Closest prior work and remaining limitations

- Dai–Soltanalian–Pelckmans (2014), arXiv:1402.2863: general SDP, no inspected specialized closed-form phase law.
- Agaskar–Wang–Lu (2014), DOI:10.1109/GlobalSIP.2014.7032145: complete text inaccessible; residual overlap risk.
- Wang–Agaskar–Lu (2015), arXiv:1502.00190: exact iterative MSE, different objective.
- *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics* (2026): nonnegative-inverse setting, whereas the present negative triangles preclude switching to it.

The result requires the stated inverse-Gram pattern, unit-norm rows and fixed iid one-step minimax objective. General long-horizon and adaptive optimizers are not addressed. Comprehensive historical-source coverage is not asserted.

Self-review: passed. Independent audit: not yet performed.
