# Scientific review

## Correctness: PASS
The exact projection identity follows from the source algorithm and the previous-step line-search orthogonality. For a nonzero Gaussian projected direction, zero error is equivalent to alignment with the current error. Hyperplane dimension distinguishes two-dimensional almost-sure termination from higher-dimensional measure-zero alignment. In the isotropic regime the conditional direction is uniform on a sphere of deterministic dimension and its squared complement is beta-distributed with a history-free conditional law. This proves independence, expectation and the logarithmic almost-sure limit. Exact rational and 40,000 simulated path checks corroborate specific finite cases; simulations are not used to prove universal results.

## Originality: PASS under accessible published-source comparison
The May 2026 RCGLS paper establishes expected-rate bounds and states the exact method, not an independent beta product law. The May 2025 Sun–Han–Xie projection framework closely subsumes the *algorithmic construction* and already implies the two-dimensional finite-termination endpoint. Therefore the dimension-two result is explicitly credited as prior knowledge; the candidate's proposed contribution is the sharp higher-dimensional obstruction and particularly the full independent-factor distribution and its exact asymptotics. The earlier projection-based least-squares solver retains more projection history, changing its finite-termination mechanism. Targeted research-record and literature searches returned no known matching stronger distributional theorem. Full historical priority is not independently established.

## Value: PASS
The distributional theorem quantifies the actual error-reliability profile of a current randomized solver, including all moments computable from its beta factors, its almost-sure speed and the precise distinction from conjugate gradients' finite-step termination. The separation at dimension three is natural: a single previous-direction constraint leaves an at-least-two-dimensional random search space, preventing exact alignment almost surely while still giving exponential contraction. This is not an arbitrary numeric slice. The beta law is limited to orthonormal design, and the finite-step obstruction remains valid for general full-column-rank design.

## Sources and remaining limits
Zeng et al. (arXiv:2605.25034v1), especially Algorithm 1 and Theorem 2.4; Sun et al. (arXiv:2505.20602v1), especially Remarks 3.5–3.6; and Brust and Saunders (arXiv:2207.07615) were inspected as principal comparisons. Generic spherical beta identities are classical, and specialized unpublished or less discoverable randomized-projection formulas may still overlap. The result assumes independent continuous rank-one Gaussian sketches and exact arithmetic.

Self-review: passed. Independent audit: not yet performed.
