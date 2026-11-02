# Scientific review of optimal signed-cycle Kaczmarz sampling

## Correctness — PASS

The exact row-projection squared-error identity reduces the worst-direction decrement to a minimum eigenvalue. Invertible congruence gives the diagonal-majorant SDP, and its elliptope dual supplies matching objective certificates. For weak closing edges, sharp Cauchy–Schwarz on the remaining path proves positive semidefiniteness; for strong edges, a strictly positive Dirichlet interior Schur complement and an exact sine-ratio cancellation prove it for every dimension and positive coupling. Complementary slackness proves uniqueness even at threshold. An implicit-function argument produces genuine matrices whose rows are normalized. The standalone Python program independently recomputed 3,060 finite numerical assertion groups in 56 examples; finite checks are supporting evidence, not proof.

The scope is precisely real invertible unit-row square systems with sparse *inverse* row Gram, fixed iid sampling, and the worst one-step expected squared-error decrement. No claims on adaptive or finite-horizon optimality follow.

## Originality — PASS on the inspected sources, with residual risks

Dai–Soltanalian–Pelckmans formulated generic optimized randomized Kaczmarz sampling using semidefinite methods, but their inspected work does not evaluate this signed-cycle infinite family. The Strohmer–Vershynin randomized Kaczmarz theory does not supply these optimized probabilities. Zelazo–Bürger's signed-Laplacian effective-resistance theorem explains the threshold in the weak-edge regime but not the exact supercritical optimizer. Classical graph-elliptope/cycle-completion theory is related to the feasible set without providing the particular sampling law and its uniqueness in the inspected material. A previously established four-variable specialization is deliberately excluded; the all-dimension construction uses a distinct nonconstant Dirichlet interpolation and a dimension-dependent trigonometric root.

The Agaskar–Wang–Lu (2014) complete conference article was inspected in an accessible Harvard repository; its optimization targets the annealed multistep MSE exponent, rather than this precise one-step worst-direction criterion. The original 1993 cycle-completion article and analogous 1986 frustrated-spin paper were not accessible in full text. Their possible direct coverage remains an explicit historical novelty risk. A failed search does not prove novelty.

## Value — PASS

For a natural sparse signed inverse-correlation family, row normalization alone does not determine optimal randomized projections. The theorem replaces a generic SDP with an exact, unique, implementable probability vector for every dimension at least five; it identifies a sharp \(1/(n-1)\) phase threshold, certificate-rank transition, and global sign-sensitive extremal geometry. The result is an exact meaningful network of numerical linear algebra benchmarks, rather than a numerical example or a generic SDP restatement.

Self-review: passed. Independent audit: not yet performed.
