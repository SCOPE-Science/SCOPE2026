# Independent mathematical audit

## correctness

PASS

Reconstructing the exact-line-search moment recursion gives \(\alpha=m_2/m_3\), the post-step moments, the second line-search parameter, and the stated two-step ratio. Fresh symbolic differentiation reproduces the derivative exactly. The cubic discriminant factors as \(4\kappa(\kappa-1)^2(\kappa+1)^2F(\kappa)\), the reciprocal substitution yields a single positive threshold, and the exact rational κ=14,s=5,ε=1/2000 witness has strictly positive excess over the balanced two-mode squared factor. The claim is correctly limited to this perturbation family, not a global worst-case theorem.

## originality

PASS

Best-of-knowledge originality passes for the finite two-step Euclidean third-mode sensitivity frontier. Yuan's full manuscript treats the same algorithm and Euclidean iterate norm, but its sharp result is one-step and reduces that one-step problem to two modes. Nocedal--Sartenaer--Zhu study the gradient norm, a different observable; the full accepted manuscript could not be retrieved and remains a risk. Resultary searches returned neighboring Richardson, CG_AOS, Jacobi, and Nesterov results but no statement with this exact-line-search two-step derivative or algebraic threshold.

## value

PASS

The theorem isolates a natural robustness boundary for the classical two-mode picture of exact steepest descent: beyond a sharp algebraic condition-number frontier, a third curvature mode immediately degrades the finite two-step Euclidean benchmark. The exact threshold and finite witness provide a meaningful structural boundary rather than an arbitrary perturbation computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
