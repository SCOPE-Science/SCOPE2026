# Scientific review

**Correctness — PASS.** The two positive equilibria satisfy the full source-model ODE exactly; the exponential softmax is evaluated by a logarithm chosen to yield a rational value. The graph Laplacian controls every homogeneous mode. The six-dimensional patterned Jacobian splits into one mean-chemical eigenvalue, an explicitly Hurwitz cubic, and an explicitly Hurwitz antisymmetric quadratic. Both hyperbolic equilibria survive small parameter perturbations. The embedded exact symbolic checker reproduces the critical identities; numerical eigenvalues are supplementary, not the proof.

**Originality — PASS under inspected evidence.** The closest paper develops the same graph equations, two-patch linear analysis, and graphon formal subcritical behavior, but does not establish an explicit hyperbolically stable patterned three-path equilibrium coexisting with a linearly stable uniform equilibrium. The two closest existing mathematical findings address two-patch and complete-graph local equilibria rather than stable finite sparse-graph bistability. Further historical coverage remains possible; no priority certification is asserted.

**Value — PASS.** A small sparse graph with a globally stable linearized homogeneous response can nevertheless possess another open positive attraction basin. This demonstrates a concrete nonlinear limit of modal pattern-suppression diagnostics in an exact instance of the motivating chemotaxis model. The rational and logarithmic witness permits independent symbolic verification rather than continuation.

**Scope and risks.** The theorem is existential on a three-node path; it does not imply arbitrary-graph bistability, characterize basin boundaries, or assert any patterns for all parameter choices. A general historical bistability theorem may cover some implications. Independent auditing is absent.

Self-review: passed. Independent audit: not yet performed.
