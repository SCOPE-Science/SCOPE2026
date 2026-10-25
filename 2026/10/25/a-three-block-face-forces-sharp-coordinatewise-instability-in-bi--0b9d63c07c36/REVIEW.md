# Self-review

## Correctness — PASS

The six-group rational dipole potential solves every Kirchhoff equation on the connected bipartite support. This directly reconstructs the orthogonal tangent projector's distinguished row and its six blocks of absolute mass. KKT strict complementarity makes that linear projector the **actual finite-input local derivative**, not just a formal bound. The sign of the row realizes the norm, and the positive-coefficient polynomial identity establishes the all-dimension threshold. A standard-library exact-rational checker independently re-solves reduced graph Laplacians in small dimensions (3,625 passed assertions). Finite computations alone are not asserted to prove an infinite-range statement.

## Originality — PASS within inspected evidence

Paffenholz, *Faces of Birkhoff Polytopes* (arXiv:1304.3948v1), covers elementary bipartite face supports but not endpoint perturbation amplification. Li–Sun–Toh, *On the efficient computation of a generalized Jacobian of the projector over the Birkhoff polytope* (arXiv:1702.05934), establishes the general Jacobian projection formula that implies how to **set up** the present tangent projection; it does not state/evaluate the rational family or compare it with full support. The closest related finite-dimensional cyclic-band study treats *contiguous cyclic bands*, not three complete blocks joined by matchings. A 2010 symmetric bi-stochastic data-similarity projection study treats a different symmetric feasible set and does not determine this coefficient. The possibility of older alternative terminology or an unstated straightforward corollary of a broader result remains a priority risk.

## Value — PASS

Doubly stochastic least-squares fitting is a natural constrained approximation problem, and stability in entrywise maximum norm is practically and mathematically distinct from the automatically nonexpansive Frobenius norm. The explicit rational law establishes **dimension-twelve boundary amplification exceeding every full-support derivative**, with a robust infinite-family contrast of limiting constants \(6\) and \(4\). The fact is not a generic Jacobian substitution: proving and explaining the boundary effect requires a nonband support, a dipole computation and a sharp sign input. It is a structural lower bound; it does not purport to solve the global sharp Lipschitz constant.

## Limits and source context

Only the specified face and output-coordinate sharpness are established. The published general Jacobian formula is the closest methodological coverage. A complete priority certificate is unavailable; independent review is not performed. `verify.py` provides reproducible exact-rational supplementary checks.

Self-review: passed. Independent audit: not yet performed.
