# Independent mathematical audit — SCOPE-20260921-7f8adc00c4c0

Final disposition: **PASS**.

## Correctness
**PASS** — For a normal matrix, the squared Rayleigh residual is the spectral variance \(\min_z\sum_i w_i|\lambda_i-z|^2\). Normalized filtering replaces \(w_i\) by \(w_i g_i^2/s^2\). Pointwise bounds \(m^2\le g_i^2\le M^2\), followed by minimization, give the state-dependent and global distortion bounds. A two-eigenvalue calculation gives the exact ratio \(mM/((1-p)m^2+pM^2)\), proving both constants sharp. The zero-gain dichotomy, universal nonexpansiveness classification, and \(1/\eta\) minimax separation tradeoff then follow directly. Independent symbolic/numerical reconstruction reproduced the two-state formula and the critical corollaries; the saved artifact is supplementary.

## Originality
**PASS** — The open 23-page Gopalakrishnan-Grubišić-Ovall primary paper was inspected at the filter-definition and convergence sections: it measures wanted/unwanted separation by the usual gain ratio and analyzes filtered subspace/Rayleigh-Ritz approximation, but it contains no raw one-vector Rayleigh-residual law. Ipsen's classical inverse-iteration result concerns residual monotonicity for the inverse-iteration diagnostic and does not state the updated-Rayleigh-residual distortion under arbitrary spectral multipliers. Searches across power/inverse iteration, polynomial/rational filtering, spectral transformations, and bounded change-of-measure variance comparisons found no earlier exact \(M/m\) law, zero-gain classification, or sharp reciprocal minimax tradeoff. Originality therefore passes to the best of current knowledge.

### Equivalent formulations
Both numerical-linear-algebra and probability-style aliases were searched.

### Broader coverage
The closest broader theories address adjacent diagnostics or convergence objectives, not the exact theorem here.

### Exact database or table
This supports the primary-source implication analysis but is not used alone.

### Claim versus prior implication
No inspected prior statement mechanically implies the assigned law.

## Value
**PASS** — The theorem identifies an exact and unavoidable diagnostic cost of spectral selectivity: improving wanted/unwanted filter separation can force proportionally large worst-case spikes in the raw Rayleigh residual before Rayleigh-Ritz extraction. The sharp law, endpoint dichotomy, and power/inverse-iteration corollaries are natural and practically interpretable structural facts.

## Source inspections
- **Spectral discretization errors in filtered subspace iteration** (https://arxiv.org/pdf/1709.06694): complete 23-page primary PDF retrieved; Sections 1-2, the spectral-gain separation definition, Rayleigh-Ritz context, and residual terminology were inspected Method: primary PDF inspection and full-text search. Assessment: FILTER_SEPARATION_NOT_RAYLEIGH_RESIDUAL_COVERAGE. Evidence: The paper defines a supremum-unwanted/infimum-wanted gain ratio below one and studies eigenspace/eigenvalue approximation; full-text search found no theorem for the raw Rayleigh residual.
- **Computing an Eigenvector with Inverse Iteration** (https://doi.org/10.1137/S0036144596300773): primary publisher abstract/theorem summary and author-provided full-text landing material Method: primary-source comparison. Assessment: DIFFERENT_RESIDUAL_DIAGNOSTIC. Evidence: The source states monotone residual decrease for normal inverse iteration, but does not state the arbitrary spectral-filter \(M/m\) updated-Rayleigh-residual theorem.

## Residual risks
- The variance comparison is elementary and may exist in older probability or spectral-transformation literature under a more abstract name.
- The theorem concerns the pure filtering step in exact arithmetic, not residuals after orthogonalization or Rayleigh-Ritz extraction.
