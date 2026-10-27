# Self-review

## Correctness — PASS

The nodal Vandermonde determinant and full-rank condition are explicit. A unique differentiation matrix follows from exactness on a three-dimensional space sampled at three nodes. The corner SBP equations force the endpoint weights and the off-diagonal equations force the middle weight; direct symbolic multiplication verifies the complete SBP identity. Singular trigonometric frequencies fail exactness rather than being handled by a limit. The norm-sign chart gives sharp open bands. A strict derivative inequality establishes exponential mass greater than the interval length; a positive logarithmic derivative and endpoint limits establish the sole normalized trigonometric frequency on the first period. The verifier independently checks the algebra with exact identities and finite tests. Limitations: floating-point spot checks are not proofs, and the problem is restricted to the specified nodes and function spaces.

## Originality — PASS, with priority risk

The closest prior literature establishes general FSBP existence through positive quadrature, construction algorithms, constant-mass requirements, and optimized movable nodes. Direct inspection of the relevant full papers found no classification of the fixed three-node family: unique forced norms, all oscillatory frequency bands, the exponential mass-normalization impossibility, or the unique normalized frequency in the fundamental period. Prior general existence theorems can motivate the calculation but do not already provide its explicit answer. Dedicated searches for equivalent exponential/trigonometric fixed-grid formulations found no covering statement. Risk: a specialized quadrature/oscillatory-mimetic discretization publication may contain an algebraically equivalent classification; publication priority remains open to independent verification.

## Value — PASS

This is a complete and sharp fixed-grid design classification at the minimal three-node dimension. It identifies an unexpected reentrant admissibility band for oscillatory fitting and a precise tradeoff between energy-stable exact differentiation and mass normalization for exponential fitting. The exact exceptional frequency and conditioning cost distinguish the finding from a routine existence check or a single counterexample. It is useful for deciding when three fixed nodes suffice and when changing the grid, basis or norm is unavoidable. It does not claim a downstream PDE convergence theorem.

## Closest literature and limits

The original FSBP paper (arXiv:2203.05479) provides general theory and different four-/five-node examples. The 2024 optimization paper (arXiv:2405.08770) explicitly imposes constant-mass normalization without addressing this forced three-node family. The second-derivative paper (arXiv:2306.16314) covers a distinct operator order. The 2026 generalized Gauss–Lobatto paper (arXiv:2604.23306) treats node optimization, not fixed-grid frequency-band feasibility. Nondiagonal norms, extra or movable nodes, other spaces, and higher-frequency normalization patterns lie outside the theorem.

Self-review: passed. Independent audit: not yet performed.
