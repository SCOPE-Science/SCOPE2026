# Self-review

## Correctness — PASS

For the strictly positive balanced two-atom family, the gauge-free Sinkhorn log-potential derivative is exactly \(s^2\). Differentiating the two source-specified accelerated state updates yields a \(2\times2\) matrix with trace \((a^2+a-1+(a+3)s^2)/(1+a)^2\) and determinant \(s^2/(1+a)^2\). Schur/Jury inequalities prove local stability. A unique increasing-quadratic root yields the only spectral-radius minimizer: the determinant bounds all smaller parameters, and the characteristic polynomial evaluated at the optimal repeated root excludes all larger parameters. An exact algebraic sign calculation gives the \(s^2=1/4\) frontier. Standalone exact-rational and high-precision calculations and nonlinear finite-difference checks support the analytic derivation, but do not replace it.

## Originality — PASS, with residual risk

Xu and Chen, arXiv:2605.30267v1, introduce the specific accelerated two-state algorithm but do not optimize its local spectral radius on the two-atom family. Gao, Qu, Ye, and Udell, arXiv:2608.11760, study local rates of standard Sinkhorn and a distinct preconditioned accelerated-gradient method. Thibault, Chizat, Dossal, and Papadakis, arXiv:1711.01851, optimize a different SOR-based overrelaxation. Full primary texts were compared at the algorithm and theorem level. Search of published mathematical-result records found no covering exact statement; this is not proof that other indexed or unindexed work cannot subsume the finding. In particular, the sharp spectral minimax may have an undiscovered equivalent general linear-recurrence formulation.

## Value — PASS

The sharp threshold distinguishes an acceleration benefit from an acceleration **penalty**, even after optimizing the parameter of the newly introduced method. The explicit parameter formula and proof apply to every positive symmetric two-atom coupling, giving a natural complete minimal-instance benchmark. The result does not claim global convergence from arbitrary points, optimality across different algorithms, finite-horizon objective ordering, or practical algorithmic speedups beyond this local benchmark.

Self-review: passed. Independent audit: not yet performed.
