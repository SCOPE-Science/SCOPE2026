# Independent audit — 2026-10-01

**Record:** SCOPE-20260920-89eb763dddfc — A sharp Euclidean solution-error barrier for symmetric GMRES(1)

**Disposition:** passed

## Final claim

For exact unpreconditioned GMRES(1)/minimal residual iteration on every real symmetric nonsingular system, one cycle satisfies \(\|e_{k+1}\|_2/\|e_k\|_2\le2/\sqrt3\), and the constant is sharp. A two-eigenvalue indefinite equality case returns to the same error direction after two steps with factor \(2/3\), while its residual decreases on each step.

## C — correctness

Diagonalizing the symmetric matrix and writing squared error coordinates as weights gives \(\alpha=m_3/m_4\) and the constraint \(\sum_iw_i z_i^3(1-z_i)=0\) for \(z_i=\alpha\lambda_i\). The exact identity \(4/3-(1-z)^2-12z^3(1-z)=(6z^2-3z-1)^2/3\) then averages to the squared-error bound \(4/3\). Independent symbolic recomputation gave zero residual in this identity, reproduced \(\alpha_0=1\), squared ratio \(4/3\), \(\alpha_1=-2\), and the two-step factor \(2/3\) for the stated \(\sqrt{33}\) witness. The definite and nonsymmetric boundary statements also follow from the displayed moment and triangular examples.

## O — originality

He’s full arXiv text analyzes GMRES(1) residual root/q-linear convergence and states worst-case factor one for symmetric indefinite systems; it does not give the Euclidean solution-error one-step bound. Meurant gives formulas and estimators for solution-error norms in full FOM/GMRES, and Weiss emphasizes that residuals may decrease while errors increase, but neither inspected source states the sharp \(2/\sqrt3\) GMRES(1) transient bound or equality cycle. Resultary searches likewise found no covering record.

### Source inspections

- **The worst-case root-convergence factor of GMRES(1)** (arXiv:2501.10248): NOT_COVERING. The paper studies residual root/q-linear convergence. For symmetric indefinite matrices it reports worst-case residual factor one, but it does not state the audited Euclidean solution-error transient bound.
- **Estimates of the Norm of the Error in Solving Linear Systems with FOM and GMRES** (DOI:10.1137/100795565): PARTIAL_COVERAGE. It provides error-norm formulas and estimators for FOM/GMRES but not the sharp one-step GMRES(1) factor or equality cycle.
- **The method of minimum iterations with minimum errors for a system of linear algebraic equations with a symmetrical matrix** (DOI:10.1016/0041-5553(63)90412-9): INACCESSIBLE_PLAUSIBLE. No theorem-level comparison is possible from the material obtained; this remains a residual originality risk rather than evidence of novelty.

## V — value

The theorem gives a sharp dimension-free cap on a practically important failure mode of residual minimization, with exact equality geometry and a recurring spike example. It cleanly separates residual contraction from solution-error transients and contrasts symmetric with nonsymmetric behavior, making it a motivated numerical-linear-algebra boundary theorem rather than a routine estimate.

## Residual risks

- Fridman’s 1963 paper is historically plausible but its full text could not be inspected: open routes yielded metadata only and the authorized institutional retrieval reached human verification. That verification block was not retried or bypassed.
- Older minimum-error/minimum-residual literature could contain an equivalent one-step inequality under different terminology; no decisive implication was found in the material read.

This audit is a mathematical review, not external peer review, formal verification, or a guarantee of priority.
