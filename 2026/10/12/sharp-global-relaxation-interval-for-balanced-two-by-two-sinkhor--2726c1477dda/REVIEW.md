# Self-review

## Correctness
PASS. The row and column log-ratio updates are exact affine overrelaxations toward their respective one-coordinate minimizers. Their conditional potential profiles are shifted \(\log\cosh\) functions, so the same potential strictly decreases for all \(0<\omega<2\), is exactly invariant at \(\omega=2\), and never decreases for \(\omega>2\). The potential is coercive and has positive-definite Hessian. A compact-cluster-point descent argument gives global convergence of ratios. The remaining common scaling product obeys a forced stable scalar recursion, proving actual coupling convergence. The checker tests representative kernels and the boundary but is not used to infer universality.

## Originality
PASS, with residual terminology risk. The pre-2016 entropic diagonal scaling framework is known. The complete relevant parts of the original overrelaxation paper were inspected: its global guarantee uses adaptive safeguards. The later complete fixed-parameter analysis proves local convergence throughout \((0,2)\) but global convergence only below the kernel-dependent Birkhoff bound. No searched primary full text or targeted semantic record supplied this special-case *global* all-start interval. A potential older two-by-two nonlinear SOR derivation is identified as a remaining risk.

## Value
PASS. The result settles exactly when constant-parameter Sinkhorn overrelaxation can be trusted globally on the first nontrivial balanced transport problem, for every positive kernel and initialization. The conditional-cosh symmetry removes a restrictive Birkhoff-based global bound, including examples where that bound ends near one despite the true sharp endpoint being two. The excluded endpoint provides a genuine global boundary, not just an experimental divergence.

## Closest literature and limitations
Peyré provides the entropic diagonal-scaling setting (primary MSC \(90C25\)); Thibault and collaborators introduce adaptive safeguarded overrelaxation; Lehmann and collaborators provide the closest fixed-parameter global sufficient interval and a full local \((0,2)\) statement. None of those located statements implies this exact special-case global conclusion. The theorem does not treat unequal marginals, larger dimensions, zero kernel entries, varying parameters, or finite-precision numerical effects.

Self-review: passed. Independent audit: not yet performed.
