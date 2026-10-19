# Scientific assessment — optimal reset placement for Brownian interval coverage

## Correctness — PASS

The claim is restricted to reflected Brownian motion with fixed positive diffusion coefficient, interval length and Poisson reset rate, resetting to the chosen initial position. The proof verifies the pathwise two-target cover identity, the three nonreset first-passage Laplace transforms and the renewal means, then reduces the full spatial optimization to one rational function. The differentiated rational function has a quadratic numerator with one negative and one positive root, ruling out hidden off-center minima. The exact endpoint-versus-midpoint comparison gives the global threshold; the midpoint derivative and endpoint sign give the distinct local-stability threshold and the number of barriers. Exact symbolic checks and an independent finite-difference boundary-value solver agree. Numerical tests are not used as infinite-domain proofs.

## Originality — PASS, qualified

Linn and Lawley (arXiv:2406.12154, Section 4.1, equation (38)) already supply the arbitrary-location **mean cover-time function**; it is not a newly derived observable. Ghosh and Sabhapandit (arXiv:2605.31207, equation (21)) already supply the midpoint function and its rate optimum. The assessed contribution is only the **complete exact argmin over deterministic reset/start positions at each fixed positive rate**, its unexpected discontinuous change from endpoints to center, the exact separate spinodal, and an exhaustive proof excluding off-center global optima. A general single-target distributed-reset paper by Julián-Salgado et al. (arXiv:2507.14483) concerns optimization of resetting rate rather than cover-time resetting position. Focused index and literature searches found no equivalent claim, but non-detection is not a proof of uniqueness. The 2024 exact all-position objective makes implicit prior coverage a substantial documented risk, although deriving the claimed minimizer and bistability classification still requires a nontrivial global analysis.

## Value — PASS

Reset location is a natural controllable variable in exhaustive scanning. Starting at an endpoint makes one target already visited but makes the remaining traversal long; starting at the midpoint balances both. The sharp switch, absence of intermediate compromises, exact metastability interval and barrier pattern distinguish the practical search designs at fixed resetting rate. This complete classification has an interpretable physical mechanism and is more than checking a normalization or selecting an arbitrary parameter slice.

## Limitations and closest literature

The result optimizes spatial placement but not the rate jointly, assumes reflection, zero detection radius, symmetric diffusion, and Poisson resetting to the chosen starting point. The published mean-function expression is stronger with respect to *available function values*, but does not state this optimized phase diagram; whether a still-broader optimization theorem implicitly contains it remains a residual originality risk. There has been no independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
