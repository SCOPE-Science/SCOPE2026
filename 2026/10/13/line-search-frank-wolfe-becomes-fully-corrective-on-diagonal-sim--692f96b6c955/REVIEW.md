# Self-review
## Correctness
PASS. The face minimizer is uniquely determined by the KKT equations \(a_i x_i=\lambda\). At that point all active gradient coordinates equal \(Z_S^{-1}\) and every inactive coordinate equals zero, forcing a standard vertex oracle to choose an unseen atom. The exact one-dimensional quadratic line search has the unique minimizer \(\gamma=a_j^{-1}/(Z_S+a_j^{-1})\), and direct substitution gives the exact minimizer on the enlarged face. Induction proves the finite-termination statement. The objective and Frank–Wolfe gap formulas follow by direct substitution. The exact-rational checker corroborates, but does not replace, the general proof.

## Originality
PASS with residual literature risk. The closest inspected Frank–Wolfe sources distinguish segment line search from fully corrective current-face re-optimization rather than identifying them. Jaggi gives both variants separately and includes the unweighted squared-norm simplex as a benchmark, but the inspected statement does not imply the arbitrary positive-diagonal face-invariant trajectory. Clarkson likewise treats greedy line search and current-face optimization as distinct operations. Targeted published-result and own-record searches under Frank–Wolfe, conditional-gradient, diagonal/separable quadratic, exact line search, fully corrective, inverse-curvature weights, and finite-termination aliases found no implication-equivalent statement. Older resource-allocation or separable-quadratic literature remains a genuine residual risk.

## Value
PASS. The probability-simplex diagonal quadratic is a natural weighted allocation problem, and fully corrective Frank–Wolfe normally requires a higher-dimensional active-set re-optimization. Here the cheap segment line search silently performs that correction exactly, yielding condition-number-independent finite termination and explicit active-set weights, objectives, and gaps. The result is a structural equivalence for an entire positive-diagonal family, not a single numerical coincidence.

## Closest literature and limitations
The closest direct comparison is Jaggi's separation of exact line search and fully corrective Frank–Wolfe. Clarkson provides earlier simplex line-search/current-face context, while Lan and Zhou provide conditional-gradient classification and an exact-line-search subroutine. The theorem is restricted to positive diagonal Hessians aligned with simplex vertices, face-minimizer starts, exact line search, and a vertex oracle.

Self-review: passed. Independent audit: not yet performed.
