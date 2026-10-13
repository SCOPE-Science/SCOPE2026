# Review of the frozen-Sylvester square-root finding

## Correctness — PASS

The derivative calculation is an exact generalized positive-definite operator-pencil argument: strict \(2Z-X\succ0\) puts its eigenvalues in \((0,2)\). The commuting assertion is an exact scalar reduction to a logistic map with parameter in \((1,3)\), including a direct proof that the orbit from \(1/2\) remains in the positive-root basin. The noncommuting counterexample uses two exact symmetric rational Sylvester solves. The first iterate has positive first pivot and positive determinant; the second determinant is strictly negative. Actual embedded `verify.py` was executed successfully. Strictness proves a neighborhood of similar witnesses. The results are about exact arithmetic, and neither a numerical sweep nor a transient negative eigenvalue is promoted to global divergence.

## Originality — PASS (residual risk noted)

The closest source is Gao–Kressner–Shao, arXiv:2607.12430, Sections 2.1, 2.3, and 3.1, which defines the identical frozen Jacobian recurrence and gives sufficient local error-norm control. Its local theorem is not a cone-invariance statement and does not yield the commuting global result or the strict noncommuting second-step witness. The source's SPD finite-precision theorem is conditional on a small initial error; the present example neither contradicts nor repairs it. Li–Shen (2014) handles Newton/Samanskii on a transformed matrix equation; Higham (1986) deals with Newton square-root variants; Ortega–Rheinboldt explains the general chord method. These supply background and possible proof ingredients rather than the exact comparison established here. Published-literature searches did not identify a matching claim. Older equivalent fixed-Jacobian or positive-cone results remain a real, not dismissed, risk.

## Value — PASS

Positive definiteness of intermediate iterates matters when square-root refinement is embedded in algorithms that require a positive-definite factor at every stage. The theorem identifies a clean, checkable strong order premise that provides both a locally attractive target and global positive convergence for commuting seeds, yet cannot be used as a noncommutative positivity safeguard. The strict rational witness has dimension two, the minimum dimension in which real symmetric matrices fail to commute, and is robust to perturbation; this isolates noncommutativity rather than rounding or singularity. It is a structural boundary, not an arbitrary isolated sign experiment. No extension to arbitrary noncommuting or finite-precision implementations is claimed.

## Closest literature and limitations

- Gao, Kressner, Shao, *A mixed precision algorithm for the matrix square root*, arXiv:2607.12430, https://academ.us/article/2607.12430/ (relevant accessible full-text sections examined, especially algorithms and Theorem 1).
- Li and Shen, *Newton's Method for the Matrix Nonsingular Square Root* (2014), https://doi.org/10.1155/2014/267042 (method section and conclusions examined).
- Higham (1986), https://doi.org/10.2307/2007992 (only abstract and accessible bibliographic information examined; full paper not established as read).
- Ortega–Rheinboldt, Chapter 7, https://doi.org/10.1137/1.9780898719468.ch7 (accessible overview only).

The example may be distant from a practical low-precision initialization; the source's sufficient local convergence hypotheses are not being contradicted. Literature novelty is not established independently by a database search alone.

Self-review: passed. Independent audit: not yet performed.
