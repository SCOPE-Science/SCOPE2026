# Independent mathematical audit — SCOPE-20260920-457b47fc383f

Audited at: 2026-10-01T22:05:12.892464Z

Disposition: **passed**

## Correctness — PASS

For \(B=D^{-1}A\), Euclidean nonexpansiveness is equivalent to \(B+B^T-\omega B^TB\succeq0\). Congruence by \(B^{-1}\) yields \(B^{-T}+B^{-1}-\omega I\succeq0\), hence the exact ceiling \(\lambda_{\min}(A^{-1}D+DA^{-1})\). In two dimensions direct inversion gives the displayed closed form. After scaling the eigenvalues to \(1\) and \(\kappa\), the rotation parameter \(z=|c|\) ranges over \([0,(\kappa-1)/2]\), and the safety ceiling is a convex quadratic whose constrained minimizer yields the two branches and the crossings \(3+2\sqrt2\) and \(7+4\sqrt3\).

### Correctness sources

- assigned RESULT.md
- Arioli-Romani 1985 abstract/metadata
- Hadjidimos-Neumann 1998 Euclidean SOR paper

### Correctness risks

- The numerical artifact is corroborative only; the proof is exact algebra.
- The condition-number envelope is proved only in dimension two.

## Originality — PASS

The closest historical Jacobi source relates spectral radius and condition numbers under diagonal-dominance assumptions, while the closest Euclidean-norm optimization source treats SOR/MSOR with Property A. Searches for the exact ceiling, the two-dimensional robust envelope, and both radical thresholds found no prior weighted-Jacobi theorem. The full Arioli-Romani paper was authorization-restricted, and opening one archival SOR PDF timed out; those are recorded risks rather than novelty evidence.

### Equivalent formulations

The claim was searched both as a matrix inequality and as a relaxation-parameter optimization problem; no equivalent formulation was found.

Searches:
- Published-record semantic search: weighted Jacobi SPD Euclidean norm damping condition number two by two transient amplification
- Web search for \(\lambda_{\min}(A^{-1}D+DA^{-1})\), weighted Jacobi, and Euclidean nonexpansiveness

Evidence:
- No equivalent earlier published record or literature formula was located.
- Nearby exact results concern SOR/MSOR or spectral radius rather than the Euclidean norm of the weighted-Jacobi step.

### Broader coverage

Those papers are broader in classical iteration theory but do not cover the audited weighted-Jacobi one-step Euclidean criterion or its fixed-condition-number minimax frontier.

Searches:
- Arioli-Romani 1985
- Hadjidimos-Neumann 1998
- classical Varga/Young Jacobi references cited by the record

Evidence:
- Arioli-Romani bound the Jacobi spectral radius using condition numbers under extra hypotheses.
- Hadjidimos-Neumann minimize Euclidean norms for SOR/MSOR operators with Property A.

### Exact database or table

The constants result from an analytic minimization over rotated two-dimensional SPD matrices, not from a known condition-number table.

Searches:
- Published-record semantic query for the exact robust ceiling and threshold constants
- Exact-formula web queries for the two radical thresholds in a weighted-Jacobi context

Evidence:
- Only the assigned record appeared as an exact match.

### Claim versus prior implication

The fixed-matrix ceiling and robust threshold require the audited congruence identity and two-dimensional minimization.

Searches:
- Compared the final claim against the Arioli-Romani spectral-radius bounds and the Hadjidimos-Neumann Euclidean SOR objective

Evidence:
- Spectral convergence of a matrix similar to SPD does not imply Euclidean one-step nonexpansiveness because \(D^{-1}A\) is generally nonnormal.
- SOR/MSOR Euclidean minimizers do not specialize mechanically to simultaneous weighted Jacobi.

### Sources inspected

- **Relations between condition numbers and the convergence of the Jacobi method for real positive definite matrices** — https://doi.org/10.1007/BF01400253
  - Trigger: Most plausible historical same-method condition-number source.
  - Material read: Institutional abstract and theorem-scope metadata describing spectral-radius bounds for diagonally dominant positive-definite matrices.
  - Method: Primary repository metadata/abstract; full PDF restricted.
  - Assessment: NOT_COVERING_IN_AVAILABLE_MATERIAL
  - Evidence: The source concerns spectral radius and scaled condition numbers, not Euclidean one-step nonexpansiveness or damping.
- **Euclidean Norm Minimization of the SOR Operators** — https://doi.org/10.1137/S0895479896300498
  - Trigger: Closest primary source on Euclidean norm optimization of a relaxation iteration.
  - Material read: Primary abstract plus archival first-page/full-PDF index material identifying the SOR/MSOR, Property-A, one-step Euclidean optimization problem.
  - Method: Primary/archival source material; complete PDF reopening timed out.
  - Assessment: RELATED_NOT_COVERING
  - Evidence: The studied operators are SOR/MSOR, not weighted Jacobi, and the stated reduction is through block-Jacobi singular values rather than the audited matrix ceiling.

### Checked sources

- https://doi.org/10.1007/BF01400253
- https://doi.org/10.1137/S0895479896300498
- classical Varga/Young references
- published-record semantic search

### Residual risks

- The complete Arioli-Romani paper was not accessible without additional authorization.
- An archival copy of the Hadjidimos-Neumann paper timed out on reopening, so only the accessible primary abstract and indexed material were read.
- Broad historical monographs were not exhaustively searched theorem by theorem.

## Value — PASS

The theorem isolates a practically meaningful boundary between asymptotic spectral convergence and one-step Euclidean safety. The exact two-dimensional minimax frontier and two sharp condition-number thresholds give a natural, reusable diagnostic for damping rather than an arbitrary matrix calculation.

### Value sources

- Arioli-Romani 1985
- Hadjidimos-Neumann 1998

### Value risks

- No higher-dimensional condition-number-only frontier is established.

## Limitations

- Real SPD systems and simultaneous weighted Jacobi only.
- The exact condition-number minimax envelope is two-dimensional.
- The metric is Euclidean one-step error norm, not an energy norm, residual norm, or floating-point performance measure.
- Historical full-text access was incomplete for two older sources.
