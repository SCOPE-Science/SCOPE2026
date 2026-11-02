# Independent mathematical audit

## correctness

PASS

Inspected complete RESULT.md and verification_checker.py. On the generic nonzero-sketch branch, w_1=e_1 and w_j=e_j-proj_H(w_{j-1})e_j are triangularly supported and form a basis. Each exact line search is the H-orthogonal projection Q_j off w_j. A product of exactly d codimension-one orthogonal projections on a d-space vanishes iff the removed lines are pairwise orthogonal: if zero, rank must drop at every stage, which forces the kernel line of each step to lie in the preceding image. Induction on w_j shows full H-conjugacy iff all H_ij=0 for |i-j|>=2. Generic nonzero coefficients follow by coordinate-j invariance of Q_1...Q_{j-1} e_j, and nongeneric or early-solved starts are expressly excluded. For d=3, after first two line searches the error is H-orthogonal to e_1 and w_2 and hence proportional to w_3-(c/a)e_1; Pythagoras gives R^2=c^2/(aW), positivity gives 0<=R<1. Independently reran exact rational rho=9/10 example and a separate tridiagonal 4-dimensional Gram calculation. No finite test substitutes for the all-d algebraic argument.

## originality

PASS

Zeng–Cai–Han–Xie define the one-step predecessor-corrected RCGLS direction and study expected convergence under random sketches; classical H-conjugate direction theory already supplies finite termination for any fully conjugate basis. The nontrivial independent assertion is the necessary-and-sufficient *coordinate ordering* structural characterization and exact 3-coordinate off-band energy defect. Full accessible RCGLS primary text, including Algorithm 1 and convergence results, was compared. No identified primary result implies these particular structural and exact-ratio claims, subject to residual risk from sparse short recurrence literature.

## value

PASS

The local-only correction of a randomized least-squares algorithm presents a natural finite-termination gap: an exact characterization of when its coordinate sweep becomes a full conjugate basis is directly useful for sparse normal equations. The sharp 3x3 equality quantifies a precise otherwise hidden nonlocal coupling loss and shows drastic order sensitivity. Both results have structural content beyond textbook mutual-conjugacy sufficiency or a routine sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
