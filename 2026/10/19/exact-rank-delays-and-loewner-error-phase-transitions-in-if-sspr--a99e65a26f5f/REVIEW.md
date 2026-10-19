# Review: rank and Loewner sign of integrating-factor Gramian quadrature

## Correctness — PASS

The published IF-SSPRK2 and IF-SSPRK3 stage algebra, when the forcing is constant and independent of the state, reduces respectively to composite trapezoidal and Simpson integration of the integrating-factor derivative. All corresponding outer-product weights are positive. The exact Vandermonde span proves rank saturation for the controllable integrator chain; the polynomial squared-integral proves positivity of its exact finite-time Gramian. Exact quadrature errors for the quadratic and quartic monomials yield nonzero signed principal minors and a complete classification. The Cauchy--Binet determinant corroborates the rank threshold. A separate rational-arithmetic verifier executes 289 checks. No finite test is used in place of the universal proof.

## Originality — PASS, subject to stated search limits

Zhang--Lan--Jing (arXiv:2606.15703v1), inspected through their method formulas, positivity theorem and error analysis, give the methods and semidefinite preservation, but not the dimension-sharp Loewner-inertia diagram or attainment of the exact rank thresholds. Bertram--Faßbender (arXiv:1903.05383v1 and arXiv:2003.03101v1), inspected at their relevant empirical-Gramian and Runge--Kutta sections, already provide the general quadrature/low-rank viewpoint. Consequently the finite-node rank ceiling and the scalar quadrature formulas themselves are not claimed as new ideas. The assessed contribution is their sharp simultaneous specialization to these specific newly introduced methods and a complete all-positive-step signed error classification. Plausible residual risk: an earlier specialized analysis may have explicitly worked out the same polynomial Gramian error matrices; search non-detection cannot rule it out.

## Mathematical value — PASS

The integrator chain is the canonical exactly controllable linear system, not an arbitrary selected matrix. Numerical rank matters for covariance inversion, observability/controllability diagnostics and Cholesky computations, while the Loewner sign determines whether an approximate variance is conservatively above or below exact variance in every direction. The result shows that semidefinite positivity can mask delayed strict definiteness and that neither scheme supplies even a one-sided universal covariance bound above a sharp dimension. The barriers persist under every positive mesh refinement; they are not numerical anecdotes or a trivial size-one endpoint.

## Scope and remaining limitations

Rank-one constant forcing, fixed uniform positive time step and exact exponentials. The sharp sign thresholds are for nilpotent integrator chains; sampled-exponential aliasing can prevent rank attainment for a general pair. No floating-point or general stiff-system result. Only self-review has occurred; the bibliographic and computational caveats remain.

Self-review: passed. Independent audit: not yet performed.
