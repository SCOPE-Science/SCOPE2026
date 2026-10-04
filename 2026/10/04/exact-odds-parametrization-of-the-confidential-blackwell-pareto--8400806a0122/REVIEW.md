# Same-model scientific review

## Correctness
PASS. The proof starts from the exact confidential Blackwell region in arXiv:2609.26750v1. The weighted support functional has an explicit negative second variation; on the simplex tangent space it is strictly negative except at the zero perturbation. Positive weights force an interior optimizer, so the Lagrange system is necessary and sufficient. Eliminating the multiplier gives the two logarithmic odds equations, their product gives \(\psi(x)\psi(y)=1\), and the converse reconstructs the unique support weight. The strict monotonicity of \(\psi\) proves the one-dimensional parametrization is single-valued. The verifier confirms representative stationary points and numerical global maximization, but the analytic argument is the proof.

Risk: all entropy rates are base two while natural logarithms are used in differentiation. This changes derivatives by the same positive factor \(1/\ln 2\) and therefore does not change optimizers or stationarity.

## Originality
PASS. The closest source, arXiv:2609.26750v1, gives the exact union-of-rectangles capacity formula, the symmetric optimum \(2\log_2\varphi\), and a numerically sampled curved boundary. It does not state the exact odds involution, the unique optimal input for every positive supporting weight, or the converse parametrization of every non-axis Pareto point. Claim-specific semantic searches, exact-source searches, aliases involving conditional entropies and Pareto frontiers, and the cumulative own ledger found no equivalent or stronger statement.

The nearby 2017 cooperative-broadcast secrecy paper is a different communication model; its abstract/model description was inspected only to establish that specific inapplicability, not as a whole-document novelty exclusion. Residual risk remains that an equivalent KKT parametrization occurs in older literature under different terminology.

## Value
PASS. The source itself represents the curved confidential Blackwell boundary through repeated numerical weighted maximization. The new theorem turns that into a canonical one-dimensional monotone involution and identifies every supporting input distribution and weight. This gives a reusable exact description of the full tradeoff curve, with the golden-ratio point and axis endpoints appearing as intrinsic fixed/limit cases. The result is a structural refinement of an exact capacity region rather than a routine recomputation of one numerical point.

Same-model review: passed. Independent audit: not yet performed.
