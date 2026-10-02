# Independent mathematical audit — SCOPE-20260919-30698826464a

Final disposition: **PASS**.

## Correctness
**PASS** — Equation (28b) of the source makes every row of \(K=M_y^{-1/2}BM_w^{-1/2}\) have Euclidean norm one, hence \(\|K\|_F^2=m\) and \(\|K\|_2\le\sqrt m\). For the displayed residual-form family, direct block multiplication gives \(KK^T=(a/(a+1))\mathbf 1\mathbf 1^T+(1/(a+1))I\), so the top squared singular value is \((ma+1)/(a+1)\) and tends to \(m\). Source equation (29) cancels the balancing parameter in the normalized coupling, and the top singular vectors have the sign pattern needed to turn the absolute coupling term in equation (31) into \(0.99\|K\|_2\), forcing rejection when that exceeds one. The supplied numerical program was read, and the central formulas were also reconstructed independently.

## Originality
**PASS** — The source gives the diagonal masses and adaptive acceptance test but does not analyze normalized row coherence, a sharp \(\sqrt m\) coupling defect, or a full-row-rank equilibrated family that triggers rejection. Standard diagonal-preconditioning and Ruiz-scaling literature explains operator-norm safety but does not supply this source-specific counterexample. published-record database searches found no earlier published record with the same PDNQP defect or acceptance-failure certificate.

### Equivalent formulations
The source-specific obstruction is an operator-norm/coherence formulation of the actual acceptance inequality, not a change of title.

### Broader coverage
The general theory does not mechanically yield the explicit family or its failure certificate.

### Exact database or table
No finite database is intrinsic; the search targeted prior theorem/counterexample coverage.

### Claim versus prior implication
A new adversarial construction and spectral calculation are needed; the claim is not a direct source corollary.

## Value
**PASS** — The result identifies exactly what the new initialization fails to control and proves the omission can be dimensionally large even for linearly independent, already infinity-equilibrated constraints. The explicit rejected direction explains why the source's adaptive safeguard is substantively necessary. This is a motivated algorithmic boundary/counterexample rather than a generic row-normalization observation.

## Source inspections
- **PDNQP: A GPU-based Factorization-free Method for Large-scale Nonconvex Quadratic Programming** (https://arxiv.org/abs/2609.19557): complete primary PDF with focused inspection of Section 3.3.5-3.3.6 and equations (28)-(31) Assessment: SOURCE_SETUP_NOT_COVERING_OBSTRUCTION. Evidence: The paper defines the masses, the 0.99 steps, and the acceptance inequality but does not provide the coherence analysis or sharp family.
- **Assigned row-coherence verification program** (repository artifact artifacts/verify_row_coherence.py): complete source and saved output; formulas independently reconstructed rather than accepted from the log Assessment: SUPPLEMENTARY_REPRODUCIBILITY_EVIDENCE. Evidence: The program matches the closed-form singular value and evaluates the source acceptance inequality on the top singular direction.

## Residual risks
- The \(\sqrt m\) bound for unit-row matrices is classical; originality is only claimed for the source-specific defect, sharp residual-form realization, and acceptance-failure certificate.
- Later revisions of the very recent solver may change the initialization or safeguard.
