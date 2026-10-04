# Review

## Correctness

PASS. Source Algorithm 2 reduces on every SPD Hessian eigenmode to a three-state linear recurrence. Direct determinant expansion gives the stated cubic. Schur reduction proves that the only active upper stability inequality is \(\eta_0h<2/(1+2\beta_0)\); the remaining Schur inequality is strictly weaker for the source range. The equality root and the unstable root beyond the boundary follow from direct evaluation at \(r=-1\).

Risk: the theorem is deterministic and does not classify stochastic mean-square stability.

## Originality

PASS. The defining paper supplies the recurrence, noise normalization, stochastic convergence theorem, and default noise setting, but does not state an exact quadratic spectral frontier. Focused published-record searches and direct full-text searches found no implication-equivalent PNM result. Later practical reuse in Ranger21 also did not surface a covering theorem in the inspected material.

Residual risk: an equivalent short root calculation may exist in unindexed implementation notes.

## Value

PASS. The source explicitly introduces \(\beta_0\) to control noise and claims that dividing the learning rate by the noise amplitude reduces retuning. The exact law shows what that normalization does not remove: a strictly decreasing deterministic stability margin. Expressing the ceiling directly in the source noise factor \(\Gamma\) gives a usable tradeoff and the cancellation of \(\beta_1\) is structurally informative.

Same-model review: passed. Independent audit: not yet performed.
