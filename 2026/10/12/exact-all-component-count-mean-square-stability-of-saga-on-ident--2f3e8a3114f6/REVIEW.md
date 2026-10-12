# Scientific review

## Correctness — PASS

The exact conditional four-moment matrix is derived directly from uniform sampling, rather than assumed from asymptotic stationarity. The explicit quadratic energy has a strictly positive \((x,m)\) principal minor for all integers \(n\ge2\), all \(s>0\), and strictly positive table-variance coefficient. The identity \(\mathbb E[\Delta V\mid\mathcal F_k]=sP_n(s)x_k^2\) is verified both symbolically for unrestricted formal variables and by independent exact rational update enumeration. Its negative sign yields mean-square convergence via summability and the independent stale-table recurrence; its nonnegative sign, together with positive definiteness, excludes convergence for every nonzero scalar state. Orthogonal eigendecomposition covers every finite SPD Hessian. No claim of linear rate or almost-sure endpoint divergence is made.

## Originality — PASS (qualified)

The earliest original SAGA paper and a major numerical-optimization survey establish algorithmic provenance, but neither supplies the all-sample-count exact necessary-and-sufficient inequality. The 2019 stepsize treatment optimizes **guaranteed sufficient** bounds from expected smoothness, not the exact second-moment stability frontier from arbitrary saved tables. The already-established two-component threshold is covered and expressly not presented as new. The original advance is the sharp formula for every \(n\ge3\), its strict sample-count decrease, and its finite-dimensional SPD extension. Comparisons were made against published closely related methods and relevant research records at the level of hypotheses, conclusions, and implication, not merely overlapping names. Remaining risk: a classical stochastic-systems or incremental-gradient analysis might contain an equivalent result under alternate terminology. No exhaustive absence-of-prior-work assertion is made.

## Value — PASS

The theorem gives a natural, complete stability boundary on the canonical identical-component SAGA test family, with an exact positive-definite Lyapunov witness and a matching impossibility direction. It quantitatively isolates an instability caused solely by gradient memory, shows its sample-count dependence, and permits a clean contrast with full-gradient descent and SAG. The question is motivated by safe stepsize selection rather than an arbitrary parameter slice; the all-\(n\) law and its large-\(n\) behavior are not obtained by substituting numbers into the known two-component calculation.

## Prior literature and residual limitations

Defazio–Bach–Lacoste-Julien (arXiv:1407.0202), Bottou–Curtis–Nocedal (arXiv:1606.04838; DOI:10.1137/16M1080173), and Gazagnadou–Gower–Salmon (PMLR 97, 2019) were compared in their relevant algorithmic and guarantee sections. The theorem has not been tested on unequal Hessians, asynchronous sampling, or nonlinear objectives. A literature-equivalent formulation outside the material examined remains possible.

Self-review: passed. Independent audit: not yet performed.
