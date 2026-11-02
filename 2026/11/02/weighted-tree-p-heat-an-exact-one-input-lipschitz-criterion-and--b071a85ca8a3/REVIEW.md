# Scientific review

## Correctness — PASS

The tree incidence map is surjective onto independent edge-gradient coordinates, making each face-bound maximization exact rather than an estimate with unrealizable signs. The monotone finite-dimensional flow makes the invariant-box criterion valid for all \(1<p<\infty\); a strictly outward face gives necessity. The gauge statement is equivalent to \(Bx\le x\) and follows from left/right Perron–Frobenius eigenvectors; the single-edge case is separately treated. Two-input rigidity uses a smooth base state with nonzero gradients and the off-diagonal Jacobian dependence on the background gradient, which can overwhelm the diagonal whenever \(p\ne2\). The standard-library checker reproduced exact face identities and explicit smooth witnesses. Boundary conditions \(|E|=1\), \(p=2\), and \(1<p<2\) were addressed separately. The checker is not an infinite proof.

## Originality — PASS, qualified

The closest fully examined nonlinear graph semigroup paper is Mugnolo, arXiv:1207.1996: it treats vertex-space contractivity rather than the exact weighted edge-Lipschitz invariant boxes or a two-input impossibility theorem. Münch–Wojciechowski, arXiv:1712.00875, provides linear heat-flow Lipschitz/curvature theory; no nonlinear \(p\ne2\) implication was found in its inspected text. Earlier edge-total-variation theory has the same star mass-balance threshold but in a different norm, and does not imply the all-tree condition or the two-input rigidity. Mathematical record searches covered aliases involving graph \(p\)-Laplacian, tree gradient maximum principle, nonlinear Lipschitz contraction and two-solution nonexpansivity. Novelty is not logically proved by these searches; unindexed prior derivations are a risk.

## Mathematical value — PASS

The difference between one-input regularization and two-input metric nonexpansivity is consequential in nonlinear semigroup theory. The theorem gives a complete criterion for the former on every weighted tree, a spectral design test for metric lengths, and a universal sharp dichotomy for the latter. Already the three-vertex path is individually Lipschitz-contracting but not two-input nonexpansive unless \(p=2\), so the obstruction is structural rather than an artificial large parameter example. The known star threshold is presented as a consistency boundary rather than claimed as an independent novelty.

## Closest literature and limitations

Full-text inspections: D. Mugnolo, arXiv:1207.1996 (graph nonlinear heat semigroup); F. Münch and R. K. Wojciechowski, arXiv:1712.00875 (linear heat Lipschitz contraction and curvature). The theorem excludes graphs with cycles, treats only positive coefficients and finite graphs, and does not determine the sharp positive-time gain when the one-input inequalities fail. An independent originality assessment and independent mathematical validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
