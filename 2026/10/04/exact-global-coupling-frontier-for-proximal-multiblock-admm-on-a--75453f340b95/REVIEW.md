# Same-model review

## Correctness

PASS. The source proximal multiblock ADMM update was specialized directly to the scalar identity-dynamics chain. Exact elimination gives a five-state homogeneous linear map whose characteristic polynomial factors into one always-stable quadratic and one cubic. Recursive Schur reduction of the cubic yields two necessary-and-sufficient inequalities; the remaining Schur inequalities were proved redundant under those conditions. The block-Hessian convexity condition and the source bounded-level structural assumption were checked separately.

The bundled rational verifier reconstructs the matrix from the sequential updates, computes its characteristic polynomial independently, and checks the factorization and boundary identities. It is supporting evidence only; the all-parameter theorem is algebraic.

## Originality

PASS. The primary paper provides a general Lyapunov sufficient parameter procedure rather than an exact equal-parameter spectral frontier. The closest historical three-block quadratic paper has positive-semidefinite block Hessians and a nonproximal direct update. The closest weakly-convex three-block paper studies direct E-ADMM, while the closest proximal nonconvex three-block paper uses a different update architecture. An open-access multiblock QP linear-algebra treatment assumes a positive-definite objective Hessian.

Targeted database and web searches found no statement implying the two exact Schur inequalities, the \(\chi=4\) strong-convexity/stability gap, or the \(\chi=9\) no-common-parameter threshold.

Residual risk remains because complete theorem-level text of the 2018 quadratic paper was not obtainable through the available lawful access route, although its accessible model assumptions do not cover the negative-curvature middle block or the source proximal recurrence.

## Value

PASS. The finding gives a complete stability classification on the smallest genuinely multiblock dynamics chain and exposes a substantive parameter-design distinction: unique strongly convex block solves can coexist with an unstable coupled ADMM map. The exact gap \(p<1/10\) versus \(p<1/2\) at \(\chi=4\), and the disappearance of any stable equal proximal parameter at \(\chi\ge9\), are natural structural boundaries for interpreting and tuning the newly proposed method.

Same-model review: passed. Independent audit: not yet performed.
