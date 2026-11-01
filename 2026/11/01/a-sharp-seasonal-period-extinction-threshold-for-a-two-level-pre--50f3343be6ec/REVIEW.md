# Scientific review

## Correctness — PASS

The inverse-prey substitution makes the phasewise logistic flow affine and contracting, giving a unique periodic orbit with explicit endpoints. Integrating the phasewise logarithmic derivative gives the exact mean; strict concavity of the hyperbolic composition proves monotonicity without relying on numerics. The triangular variational equation gives the two exact Floquet multipliers. A scalar logistic comparison bounds every prey solution from above by a solution converging exponentially to the boundary cycle, causing global predator decay whenever the mean is below one; the inverse-prey equation then gives prey convergence. Endpoint mean asymptotics and the strict crossing were independently reconstructed and checked. See RESULT.md Proof steps 1–5 and verify.py for numerical sanity checks.

## Originality — PASS with residual priority risk

The source model arXiv:2511.03521v1 treats sinusoidal forcing and coexistence/chaos, not this quantitative predator-invasion classification. The very close earlier arXiv:2002.10372, Supplemental S2.3, already gives the scalar logistic periodic profile; that mathematical object and formula are prior art. Our mean formula is algebraically implied by it, and is not the standalone novelty. The remaining contribution is strict all-period monotonicity combined with the necessary-and-sufficient single-crossover classification and its full-positive-cone extinction conclusion for the nonlinear two-species model. These are not provided by the inspected earlier primary statements, but specialized unindexed results may exist. The 2026 Axioms paper's full publisher text remained inaccessible; this is an explicit priority risk.

## Mathematical value — PASS

In periodically forced predator–prey systems, two limiting effective capacities often give insufficient information about intermediate forcing periods, including the possibility of multiple disjoint invasion windows. Here exact mean monotonicity proves there can be precisely one crossing, with no other intermediate frequency windows, and the stable side enjoys global predator extinction rather than only perturbative Floquet stability. This is a motivated all-period dynamical classification across an unrestricted positive capacity contrast, not a numerical example or a repeated calculation of an already-published scalar solution. It does not assert nonlinear persistence on the invasion side or a new stochastic conclusion.

## Close literature and limitations

Closest: arXiv:2002.10372 Eq. (S17) explicitly covers scalar logistic periodic profiles; arXiv:2211.09276 analyzes periodic carrying-capacity switching; arXiv:2511.03521v1 provides the normalized coupled equations; Axioms 15 (2026), 355 treats scalar periodic logistic solutions. The main risk is an unindexed explicit global-invasion result or a stronger general theorem rendering the period-uniqueness comparison immediate. The proof is for deterministic equal-duration seasons and does not certify behavior at the nonhyperbolic boundary.

Self-review: passed. Independent audit: not yet performed.
