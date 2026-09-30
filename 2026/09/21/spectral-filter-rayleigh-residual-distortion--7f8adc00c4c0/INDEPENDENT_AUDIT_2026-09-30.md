# Independent audit — 2026-09-30

**Record:** `2026/09/21/spectral-filter-rayleigh-residual-distortion--7f8adc00c4c0`  
**Repository:** `SCOPE-Science/SCOPE2026` at `253a0fe5d0217455660a277f9adb940030e567ad`  
**Audited tree:** `422807e270286710a0c75645b672dd8053bbb746`  
**Disposition:** **PASSED**

## Correctness

**PASS.** For a normal matrix, the squared Rayleigh residual is exactly the minimum weighted spectral variance. After filtering and normalization, weights are multiplied by g_i^2/s^2. Pointwise comparison by m^2 and M^2 before minimizing yields the m/s and M/s bounds. On two eigendirections with gains m and M the exact ratio mM/((1-p)m^2+pM^2) gives both sharp global constants. The zero-gain construction correctly gives unbounded relative amplification iff at least two distinct retained eigenspaces remain; single-eigenspace support produces zero output residual. The universal nonexpansiveness classification and the 1/eta minimax separation tradeoff follow directly. The generalized Hermitian-definite reformulation is valid in the B-inner product.

## Originality

**PASS (literature-bounded).** Filtered-subspace literature uses wanted/unwanted gain ratios for eigenspace convergence, and Ipsen's inverse-iteration monotonicity concerns the fixed-shift residual, not the updated Rayleigh residual. Searches did not locate the exact M/m one-step distortion law, its zero-gain classification, or the sharp reciprocal separation-versus-residual minimax statement. A September 2026 preprint on Rayleigh-residual flow discusses polynomial reweighting but does not, in the accessible statement, subsume this theorem. Older variance-comparison or spectral-transformation literature remains a meaningful historical-equivalence risk.

## Scientific value

**PASS.** The theorem isolates a simple but operationally important worst-case law: stronger spectral selectivity can force reciprocal raw-residual spikes before Rayleigh-Ritz extraction. It also cleanly separates pure-filter behavior from complete eigensolver convergence theory and supplies exact power/inverse-iteration corollaries.

## Literature and evidence

- Gopalakrishnan, Grubisic and Ovall, Spectral discretization errors in filtered subspace iteration: https://arxiv.org/abs/1709.06694
- Ipsen, Computing an Eigenvector with Inverse Iteration: https://doi.org/10.1137/S0036144596300773
- Shen, Rayleigh-Residual Flow I: Normal Matrices: https://arxiv.org/abs/2609.24901

## Limitations

- The main theorem assumes finite-dimensional normal matrices and exact arithmetic.
- It concerns one pure filtering-and-normalization step, not a complete filtered eigensolver.
- Degree/pole constraints and older spectral-transformation literature leave residual originality risk.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
