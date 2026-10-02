# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-e5bf17359b11`

## Correctness — PASS

The final rectangular privacy package survives independent reconstruction. For additive masking of a uniform matrix, matrix characters diagonalize the conditional-expectation operator. For a factor mask \(UV\), a rank-\(s\) character survives exactly when all \(r\) columns of \(U\) lie in a codimension-\(s\) kernel, giving coefficient \(q^{-rs}\) and hence maximal correlation \(q^{-r}\). For the rank ball, the block Schur-complement recurrence reduces a nonzero character sum to \(q^r\) times the rank-\(r\) sum on the \((m-1)\)-by-\((n-1)\) block; the absolute maximum is attained at character rank one and equals the displayed formula. The kernel-size covariance count gives the stated rectangular lower bound, tensor-product singular values give the two-upload maximum law, and the conditional-atom entropy argument plus the rank-factorization support bound gives the differential-privacy obstruction. Independent exact enumeration over the audited small binary rectangles reproduced the reported rank-ball values and the \(3\)-by-\(4\) kernel correlation \(41/105\).

### Correctness sources

- assigned RESULT.md
- artifacts/verify_rectangular_privacy.py
- artifacts/verification.txt
- current published exact-minimax rectangular masking theorem

### Correctness risks

- The finite enumerations only corroborate the general algebra.
- Uniform inputs and input-independent additive rank-bounded masks are essential hypotheses.

## Originality — PASS

The package is not wholly covered by the stronger current exact-minimax shell theorem. That later theorem covers and sharpens the rectangular universal-converse component for most fields, but it does not state the exact factor-mask coefficient \(q^{-r}\), the exact uniform-rank-ball formula, the two-independent-upload bottleneck law, or the rectangular differential-privacy obstruction. The motivating low-rank-masking preprint publicly advertises its strongest maximal-correlation privacy theorems for square uniform inputs, while its protocol itself is rectangular. Thus the surviving final package contains genuine rectangular statements not implied by the located stronger result.

### equivalent_formulations

Searches:
- Resultary semantic search: rectangular low-rank masking maximal correlation rank ball privacy
- arXiv:2609.18876 title/abstract and rectangular-protocol searches

Evidence:
- The exact audited record and a later exact-minimax shell theorem were located.
- The latter shares the kernel-count lower bound but uses uniform exact-rank masks and does not provide the rank-ball/factor-mask/DP package.

Reasoning:
Equivalent formulations through Fourier coefficients of rank-radial additive channels and through maximal-correlation singular values were compared, not only titles.

### broader_coverage

Searches:
- Resultary record SCOPE-exact-minimax-nonbinary-low-rank-masking--518b6bf1d437
- Cohen–D'Oliveira–Sprintson arXiv:2609.18876

Evidence:
- The current exact-minimax theorem gives the same rectangular kernel-count bound and a stronger achievability result for exact-rank shells.
- The motivating source gives square privacy theorems despite a rectangular multiplication protocol.

Reasoning:
Broader current coverage is real for the converse clause, but it does not dominate the final package's exact factor-mask and rank-ball evaluations or its differential-privacy extension.

### exact_database_or_table

Searches:
- bilinear-forms association-scheme eigenvalue literature and current Resultary masking records

Evidence:
- Classical schemes tabulate rank-metric character eigenvalues, but no inspected table itself states the protocol-level rectangular rank-ball maximal-correlation formula and DP consequence as a privacy theorem.

Reasoning:
The algebraic eigenvalues are ingredients; the privacy interpretation and several consequences require additional statements.

### claim_vs_prior_implication

Searches:
- claim-by-claim implication comparison with the current exact-minimax theorem

Evidence:
- The exact-minimax theorem implies a stronger optimum than the audited factor-two converse in its field range, but it neither fixes the Fourier spectrum of the factor-mask distribution nor the uniform rank-ball distribution nor the DP entropy bound.

Reasoning:
Because acceptance is for the final theorem package, partial current coverage does not imply every final claim.

### source_inspections
- **Low-Rank Masking for Single-Server Matrix Multiplication** — https://arxiv.org/abs/2609.18876. Trigger: Primary motivating source with the same protocol. Material read: Accessible abstract/metadata and theorem-scope information; full arXiv/OA text was not obtainable in this run and the authorized download route was unavailable. Method: Primary-source scope comparison without treating the unavailable full text as a whole-document exclusion. Assessment: Supports the square-versus-rectangular motivation but leaves residual near-simultaneous-work risk. Evidence: The accessible scope describes square uniform-input maximal-correlation theorems for the privacy analysis.
- **Exact minimax maximal correlation for low-rank matrix masking** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-exact-minimax-nonbinary-low-rank-masking--518b6bf1d437. Trigger: Highly relevant stronger current rectangular theorem. Material read: Complete published RESULT.md. Method: Full theorem-and-proof implication comparison. Assessment: PARTIAL COVERAGE: it sharpens the rectangular converse but does not cover the other exact distributions or DP theorem. Evidence: Its theorem is minimax exact-rank-shell masking over most rectangular bilinear-form spaces.
- **Assigned rectangular verifier** — artifacts/verify_rectangular_privacy.py. Trigger: Critical finite sanity checks. Material read: Complete source and saved output. Method: Line-by-line inspection plus independent exact reimplementation. Assessment: Corroborates the rank-ball Fourier formula and kernel covariance at small parameters. Evidence: The \(3\)-by-\(4\), rank-one check reproduces maximal rank-ball coefficient \(21/53\) and kernel correlation \(41/105\).

### checked_sources

- https://arxiv.org/abs/2609.18876
- https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-exact-minimax-nonbinary-low-rank-masking--518b6bf1d437
- artifacts/verify_rectangular_privacy.py
- current Resultary masking search

### residual_risks

- Classical bilinear-forms association schemes may contain equivalent raw character identities under different notation.
- The motivating preprint is recent and full text was not available through the attempted access routes in this run.

## Scientific value — PASS

Removing the square restriction from an intrinsically rectangular secure-multiplication protocol is mathematically motivated. The result gives exact leakage for two natural masking laws, an aspect-ratio-aware converse, the exact two-upload bottleneck, and a rectangular differential-privacy impossibility bound. These are reusable privacy statements rather than a parameter renaming.

### Value sources

- motivating low-rank-masking protocol
- current exact-minimax masking comparison
- assigned analytic proof

### Value risks

- The factor-two converse itself has since been sharpened by a current exact-minimax result, but the rest of the package remains useful.

## Limitations

- Uniform inputs and input-independent additive masks are assumed.
- The simple factor-two converse is only asserted in the stated rank range.
- Current published work now sharpens the converse clause for many fields; that partial overlap is recorded explicitly.
- Originality remains best-of-knowledge for the uncovered package components.

## Disposition

**PASSED**
