# Scientific review

## Correctness
PASS. The update matrix follows exactly from the declared primal-first, unit-extrapolation recurrence. Its eigenvalues lie strictly in the open unit disk for every individually permitted step product. Direct matrix multiplication gives the full-period trace and determinant. All degree-two Jury inequalities are reduced analytically, with the only potentially failing inequality equal to a quadratic polynomial. Its discriminant, double-zero threshold, admissible roots, endpoint crossing and strict/marginal/unstable classifications are explicitly proved. The rational witness is independently checked. The included verifier passed 1,941 exact symbolic/rational comparisons; none is treated as an exhaustive infinite proof.

## Originality
PASS on inspected evidence, subject to a material bibliographic risk. Goldstein et al. already explicitly assert that nonconstant PDHG steps may destroy convergence despite safe products; that qualitative observation is acknowledged, not claimed. Wang–Lan–Ye analyze nonstationary steps under summable variation and a different extrapolation rule for the convergence theorem. Published constant-step scalar classifications optimize a single matrix; they do not imply the noncommuting two-matrix stability boundary. No covering formula for the exact universal jump threshold and full two-parameter phase diagram was found in the inspected primary papers, published mathematical records and accessible same-slot claims. An earlier switched-systems computation could contain the equivalent quadratic; novelty remains provisional without independent review.

## Value
PASS. The exact universal threshold and two-dimensional parameter classification resolve a concrete design question: how far reciprocal primal-dual steps may alternate before the usual pointwise sufficient product condition ceases to ensure stability. The distinction between individually Schur-stable phases and unstable periodic composition is relevant to adaptive-solver safeguards and illustrates why boundedness and control of parameter variation enter convergence theorems. The result is naturally complete for the bilinear two-cycle model rather than an arbitrary numerical example.

## Closest literature and limitations
Wang–Lan–Ye (arXiv:2402.00311v1), Goldstein et al. (arXiv:1305.0546v2), Lorenz–Tran-Dinh (arXiv:1801.03765), and the published constant-step scalar PDHG classification were compared. This is a predetermined periodic, unit-extrapolation test, not an execution of the convergence-assured tuning-free algorithm; conclusions do not extend to general switching or nonlinear problems. Equivalent historical statements and independent scientific priority remain unresolved.

Self-review: passed. Independent audit: not yet performed.
