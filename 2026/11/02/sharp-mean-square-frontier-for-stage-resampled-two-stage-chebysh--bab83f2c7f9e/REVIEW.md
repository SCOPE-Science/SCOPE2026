# Scientific assessment

## Correctness — PASS

The method's coefficients follow by substituting the two-stage, zero-damping Chebyshev parameters into the published equations. Independent stage client curvatures produce an exact bilinear random multiplier. Because its square is at most quadratic in each independent curvature, its expectation depends only on the curvature mean and variance. Expanding gives the displayed product of two polynomials and proves all necessary and sufficient cases, including the special mean-four line and equality. The four ordered two-client outcomes reconstruct the entire finite law without approximation; an iid strong law proves the separate negative almost-sure exponent. Exact symbolic and finite rational checks of the derived identities are reproducible from the embedded verifier. No finite computation is treated as an infinite proof.

## Originality — PASS (qualified best-knowledge assessment)

The closest primary work is Stillfjord–Williamson (arXiv:2201.12782v1), equations (3.1)–(3.2), section 3.4, and the same-batch experimental implementation in section 4. That publication establishes the source recurrence, its deterministic stability principles, and convergence conditions with diminishing steps. It specifies one shared minibatch per full Runge–Kutta step and therefore does not present the independent-client-per-stage random curvature product or the exact variance frontier here. Bochacik et al. (arXiv:2006.12131) provide a more general randomized Runge–Kutta mean-square stability background, but with stage-time randomization and a different information model; generic iid-multiplier stability alone does not state the exact sharp coefficient product or shared-versus-fresh contrast. Relevant neighboring mathematical results address deterministic stagewise-safe Richardson steps or mean-square stability of different stochastic optimization schemes and do not imply the derived Chebyshev boundary. Residual risk: an older general random-coefficient Runge–Kutta treatment may already derive an equivalent Chebyshev identity under different terminology; mathematical priority remains independently unvalidated.

## Value — PASS

The result provides a complete necessary-and-sufficient distribution-free criterion for mean-square stability of a natural sampling modification to a published stabilized stochastic optimizer. The two-client instance exhibits simultaneous stability of all deterministic fixed-client updates, first-moment convergence, almost-sure exponential convergence, and exponential expected-loss explosion, whereas the original shared-minibatch update contracts in mean square. The distinction offers a concrete numerical-design safeguard: the common-batch choice cannot casually be replaced by per-stage independent batches while relying on deterministic RKC stability intuition. The motivating choice of staging and the exact phase boundary give the result structural relevance beyond a one-off numerical example.

## Closest literature and limits

The sharp frontier is specific to two-stage undamped unit-step scalar quadratics with independent stage sampling. It does not invalidate Stillfjord–Williamson's same-client algorithm or claim a problem in their diminishing-step convergence theorem. The full SRKCD primary source was inspected; randomized Runge–Kutta ODE stability sources and neighboring numerical stability records were compared at the level of their mathematical objects, randomness, and implications. The stochastic Brownian forcing literature is less directly comparable and has not been exhaustively excluded.

Self-review: passed. Independent audit: not yet performed.
