# Review of the robust angular spectral preconditioner finding

## Correctness — PASS

For any real SPD \(2\times2\) matrix with two distinct eigenvalues, the inverse preconditioner is SPD whenever \(q>0\). The split-preconditioned trace and determinant follow by a direct rank-one calculation, and the exact one-step worst energy loss follows from the sharp two-point Kantorovich inequality, including explicit equality weights. Directional uncertainty reduces to the endpoints \(t=0\) or \(t=T\). Branchwise optimization is global and gives a unique multiplier for the full admissible domain. The nominal-scaling frontier and singular-spectrum asymptotics follow from exact algebra. The packaged independent matrix-level checks passed, and no infinite claim depends on simulation.

## Originality — PASS, subject to independent confirmation

The closest identified work is Diouane et al., arXiv:2603.28969v1, Section 3; its spectral placement arguments use exact eigenvector directions. The earlier arXiv:2410.02204v1 (Section 4) defines scaled spectral inverse preconditioning on exact eigenspaces. Kahl and Rittich (2016, Section 4) treat approximate invariant spaces in projective deflated CG, not the robust finite positive rank-one multiplier tuned for first-step worst-case energy loss. The elementary steepest-descent contraction formula is prior knowledge and not a new result. The combined \(45^\circ\) minimax rule, nominal-parameter hazard threshold, and singular-spectrum accuracy scaling are not directly covered by the inspected statements. A related but inaccessible broad survey and an undiscovered equivalent angle-condition theorem remain originality risks.

## Value — PASS

Spectral preconditioning with estimated eigenvectors is a natural short-budget numerical-linear-algebra design problem. The theorem completely resolves its two-mode robust first-step variant, including a sharp point at which the best correction changes to no correction, and separates this possibility threshold from the more demanding angular scaling required for condition-number-independent contraction. These distinctions guide robust tuning and identify what cannot be certified from a coarse approximate spectral direction. The result does not establish practical high-dimensional acceleration or approximate-eigenvector estimation costs.

Self-review: passed. Independent audit: not yet performed.
