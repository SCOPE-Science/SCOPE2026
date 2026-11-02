# Self-review

## Correctness — PASS

The proof independently derives genuine variable-coefficient BDF4 Lagrange derivative weights on five nonequispaced nodes. It reduces homogeneous zero stability to a three-dimensional difference monodromy, reconstructs the exact rational characteristic cubic, and applies four necessary-and-sufficient Schur–Jury inequalities. Three required polynomial numerators have strictly positive coefficients; the remaining numerator has the explicitly factored unique-positive-root polynomial. A separate exact singular asymptotic calculation yields the transition at \(s=2\). The embedded standalone symbolic verifier reproduced each critical identity and sign certificate. The boundary has a simple neutral \(-1\) multiplier and is not mislabeled strictly damped.

## Originality — PASS on inspected evidence, with risk

Skeel (1986), inspected in the actual full paper text, constructs the variable-coefficient family but does not present the claimed three-periodic threshold. Calvo–Grande–Grigorieff (1990) supply general mesh-ratio conditions, but the available abstract and metadata cannot exclude a hidden specialist comparison in their full paper. The 1983 Skeel–Jackson Nordsieck paper concerns a distinct coefficient adaptation and was not available in full. Söderlind–Fekete–Faragó (2018), inspected in its openly accessible full text, assumes smooth mesh deformation with neighboring ratios close to one and does not cover fixed high-contrast period-three meshes. Searches for BDF4 three-periodic Floquet multipliers and the exact threshold yielded no covering statement, but search silence is not itself a novelty certificate. The absent specialist full texts are explicit residual risks, not represented as having been read.

## Value — PASS

This is a complete sharp classification of a natural one-parameter three-periodic grid family rather than an isolated numerical counterexample. The value \(s=3\) is the smallest integer above the independently proved singular instability frontier \(s=2\), rather than an unmotivated slice. Its degree-seven threshold and the surrounding exact large-contrast frontier show how a fixed recurring step pattern can cross from strictly damped to unstable, which a generic sufficient adjacent-ratio condition cannot diagnose. The boundary also distinguishes neutral zero stability from asymptotic damping. The result is limited to homogeneous Floquet stability, not solution convergence for general ODEs.

Self-review: passed. Independent audit: not yet performed.
