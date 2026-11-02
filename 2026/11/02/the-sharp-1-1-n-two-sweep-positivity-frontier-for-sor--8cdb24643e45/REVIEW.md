# Review of the sharp dimension-dependent two-sweep SOR positivity frontier

## Correctness

**PASS.** The exact response \(\omega[R+(1-\omega)R^2+\omega RUR]D^{-1}b\) follows from two forward SOR sweeps. Nilpotence gives coefficients \(j+2-(j+1)\omega\), nonnegative simultaneously for \(\omega\le1+1/q\). The path witness has strictly negative leading term \(\omega^n\varepsilon^{n-1}(n+1-n\omega)\) when \(\omega>1+1/n\), while any upper-step correction has two extra powers of \(\varepsilon\). The embedded exact-rational verifier passed 11,368 assertions. The argument covers all dimensions analytically; no inference from finite sampling is made.

## Originality

**PASS, with a specific historical risk.** Vigna (arXiv:1404.3327, 2014), whose mathematical body and main theorems were inspected, treats \(M\)-matrix SOR error-norm convergence, not two-sweep coordinatewise positivity. The published 2026 two-dimensional result has the \(n=2\) specialization and explicitly excludes a general-dimensional assertion, so its conclusion does not imply the new all-dimensional threshold. James–Riha (1975) and Yun (2005) address convergence and weak-regular splitting respectively; only abstracts were accessible for these two papers, leaving residual historical uncertainty. No retrieved published-finding corpus result or recoverable prior research claim covered the all-dimensional frontier. Failed searches are not treated as uniqueness proofs.

## Mathematical value

**PASS.** The property is a natural finite-horizon safety requirement for overrelaxed solvers with nonnegative data. The sharp \(1/n\) margin quantifies an asymptotic conflict between overrelaxation and early-step sign preservation, despite convergence of SPD SOR for \(0<\omega<2\). The nilpotency-index refinement gives an actionable ordering- and sparsity-sensitive guarantee, and path matrices establish dimension-sharp necessity in the convergent SPD subclass. This is more than recomputation of the known two-dimensional special case.

## Nearest literature and limitations

The exact two-dimensional SOR positivity frontier is already published. General convergence and \(M\)-matrix splitting results address related but logically different properties. Some older complete texts could not be inspected, so originality remains provisional pending independent literature review. Only the second iterate from zero is covered. There is no claim of positivity for subsequent sweeps, a sharp fixed-matrix threshold, or a universal convergence result for nonsymmetric matrices.

Self-review: passed. Independent audit: not yet performed.
