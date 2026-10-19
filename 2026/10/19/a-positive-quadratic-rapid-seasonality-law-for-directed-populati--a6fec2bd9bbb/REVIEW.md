# Review of the rapid-period dispersal coefficient

## Correctness — PASS

The Floquet monodromy has an analytic continuation at zero period because the averaged Metzler matrix has a simple positive Perron eigenvalue. The normalized periodic-profile expansion gives an identically zero linear term. Periodic integration by parts and two separately vanishing weighted row/column sums of the shifted Perron matrix give the second-order Dirichlet formula. Strong connectivity characterizes its equality case. All critical assumptions, including piecewise-continuous growth, strict positivity of the left/right eigenvectors, and possible nonreversibility, are explicit. An exact rational three-season example produces coefficient \(1/18\); the embedded checker passes 36 assertions, including independent four-season nonreversible monodromy tests. The finite checks supplement the analytic all-size proof.

## Originality — PASS, subject to residual publication-priority risk

[1] analyzes the same fixed directed migration class and its small/large period limits, but its general comparison to the averaged eigenvalue is not the sharp signed quadratic expansion or local derivative. [2], Proposition 1, already obtains second-order formulas for **two** seasons; novelty therefore resides in the universal arbitrary-profile, any-number-of-seasons Dirichlet formula and the exact strictness/equality dichotomy for nonsymmetric migration. [2], Proposition 6, proves vanishing of the linear term in general but not this second-order positivity. [3] and [4] give global frequency monotonicity in symmetric settings, not the general nonsymmetric coefficient. Abstract-level [5] is potentially related but has not been conclusively compared throughout its full text. Search and implication comparisons found no direct dominating published statement. Hidden equivalence to a broader spectral monotonicity theorem remains possible; search absence alone is not a novelty proof.

## Value — PASS

Fast environmental switching is a natural persistence boundary. The exact positive coefficient quantifies the first **nonzero** ecological growth response where the previously proven linear correction vanishes, resolving local directionality even when known directed-network examples invalidate global monotonicity. Its edge decomposition isolates the temporal mismatch responsible for the effect, identifies a sharp zero-effect boundary, and applies to arbitrarily many habitats and seasonal phases, including asymmetric dispersal. This is a structural response law rather than a numerical gain or arbitrary parameter slice.

## Scientific limitations and closest literature

The proof is local near period zero and assumes constant irreducible dispersal and diagonal seasonal growth. The two-environment expansion and symmetric monotonicity are prior art, not newly claimed. A related 2024 nonlocal cooperative operator paper was accessible only through an abstract/introduction and is an explicit residual priority risk. Independent scientific priority and proof validation are outstanding.

Self-review: passed. Independent audit: not yet performed.
