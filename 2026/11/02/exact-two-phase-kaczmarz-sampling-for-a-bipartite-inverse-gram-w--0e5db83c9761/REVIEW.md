# Scientific review

## Correctness — PASS

The exact object is the sharp one-step expected squared-error decrement of ordinary fixed-probability randomized Kaczmarz on a square, nonsingular, unit-row matrix. Invertible congruence converts the eigenvalue maximization to a diagonal-majorant trace minimization. A rank-one or rank-two positive-semidefinite correlation matrix gives the exact lower bound. The proposed diagonal majorant has explicit sum-of-squares certificates in both regimes; matrix complementarity proves equality and all-optimizer uniqueness without assuming symmetric probabilities. All boundaries, including \(p=q=2\) and \(v=wq/2\), are covered. The standalone checker passed 450 rational parameter identity tests, 20 models with random and perturbed feasible probability vectors, and three normalized-row fixtures. Its finite tests support the algebra but do not replace the proof.

## Originality — PASS on inspected evidence, with residual risks

Strohmer–Vershynin (arXiv:math/0702226) establish the randomized Kaczmarz baseline; Gower–Richtárik (arXiv:1506.03296, section 5.1) give a general SDP optimization but not the specialized bipartite signed-precision closed form. Zelazo–Bürger (arXiv:1408.2187, theorem III.3) establish a signed-Laplacian effective-resistance boundary, which can explain the subcritical certificate but not the explicit supercritical optimal probabilities or rank-two certificate. Agaskar–Wang–Lu (2014) study probability optimization; its accessible metadata and abstract do not settle the specific two-regime formula. Related signed-cycle, forest, complete-graph and two-block Kaczmarz formulations were compared at the level of implication: their supports, signs or optimization domains do not give this complete-bipartite-with-one-negative-chord family. A possible specialized equivalent derivation in uninspected literature remains the principal risk. No failed search is asserted to prove uniqueness in the literature.

## Mathematical value — PASS

This is a natural nonconvex-looking sampling-design problem that the generic SDP does not answer explicitly. Its full two-regime solution supplies every optimal row probability, a sharp frustration ratio \(v/w=q/2\), a rank-one-to-rank-two dual transition and uniqueness even with unrestricted individual row probabilities. The threshold depends only on the opposite part size and not on the size of the part containing the exceptional pair; that distinction can guide exact choice of sampling rates for structured inverse Grams. The result is a closed-form model classification, not merely a recomputed known table or a finite experiment.

## Sources and limitations

See RESULT.md and AUDIT.json for precise comparisons and source inspections. The result does not optimize full multistep MSE or almost-sure convergence, and assumes the inverse Gram sign pattern rather than general sparse or arbitrary signed structures. The 2014 Agaskar–Wang–Lu paper was available as an abstract/record in this review, not as inspected full text. Scholarly priority is subject to further specialist review.

Self-review: passed. Independent audit: not yet performed.
