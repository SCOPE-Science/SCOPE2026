# Scientific review: parallel low-rank inertia and truncation sign transition

## Correctness — PASS

The proof starts with the precise parallel basis and coefficient updates in Ceruti--Kusch--Lubich (2023), equations (6)--(10). For matched symmetric augmented bases, the new-old coefficient has full row rank exactly when new basis directions are generated. With a positive definite old-old block, a Schur-complement congruence gives the complete inertia, not just a negative determinant. For the positive linear gradient flow, the reduced substeps are solved explicitly, giving eigenvalues \(1+d\), \(1\), and \(-d\), where \(d(d+1)=\gamma^2(1-e^{-h})^2\). This proves the sharp SVD threshold and accounts for singular-value ties. The source's rank selection and both optional rejection criteria were evaluated for the witness, without pretending the criteria are always inactive. Numerical checks are supplementary; the universal statements are analytical.

## Originality — PASS (best-knowledge, with residual risk)

The 2023 paper itself supplies the zero-corner block formula and explicitly notes losses of exactness and some energy properties; none of these starting facts is credited as new. Its inspected algorithm, rationale, rejection analysis, convergence discussion, numerical examples, and conclusion do not state the signed inertia count, rank-two SVD sign-order transition, or the concrete example passing rejection. The 2021 augmented-Galerkin BUG integrator, 2023 rank-reduced Kalman filtering construction, and 2024 positive Kraus low-rank integrator use different updates and do not cover the full statement. Searches of publicly indexed mathematical findings did not reveal a matching implication or stronger statement. Standard Schur complements and SVD facts are not claimed as new. The main residual originality risk is that the first inertia observation is an elementary consequence of the published block formula, or that a related positivity-aware low-rank analysis contains the same sharp rank-two cutoff without using the algorithm's name.

## Value — PASS

Positive semidefiniteness is a basic feasibility property for covariance and density-matrix dynamics. The result identifies a systematic incompatibility between symmetric nontrivial rank growth and positivity for the parallel zero-corner augmentation, then shows why ordinary magnitude-based SVD rank reduction can retain the negative mode even while discarding a positive mode. The exact transition is a natural algorithmic boundary, and the nonrejected three-state witness demonstrates that the method's normal-component safeguard does not itself certify positivity. This motivates sign-aware truncation or different coefficient updates, without asserting a universal replacement algorithm.

## Limits and closest literature

The scope is exact reduced-substep integration with transpose-equivariant vector fields and matched symmetric bases; the rank-two cutoff belongs only to the stated three-dimensional positive gradient flow. The boundary of singular-value equality is nonunique. The original paper's explicit zero new-new block is a substantial predecessor and the algebraic inference could have been made elsewhere. No global-in-time failure or incompatibility with independently positivity-preserving schemes is proved.

Self-review: passed. Independent audit: not yet performed.
