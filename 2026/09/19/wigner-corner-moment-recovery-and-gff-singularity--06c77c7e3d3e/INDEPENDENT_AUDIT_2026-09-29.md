# Independent Audit — 2026/09/19/wigner-corner-moment-recovery-and-gff-singularity--06c77c7e3d3e

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `98e823de0ef603f2cf06b2cd64929a23f6e8e0fa`
- Disposition: **PASSED**

## Correctness

**PASS** — The nested spectra give D_k=X_kk by trace differencing and T_k=sum_{i<k}|X_ik|^2 by the trace-of-square identity. The Z_k therefore use disjoint off-diagonal columns and are independent with variance b-1. The fourth-moment formula for a normalized sum of k-1 centered copies of Y-1 gives E Z_k^4=3v^2+(mu_4-3v^2)/(k-1), which yields exactly the submitted finite-n variance for b_hat and the universal leading variance 2(b-1)^2/n. Kolmogorov's strong law applies because the centered Z_k^2 have uniformly bounded variance; the all-moments hypothesis readily supplies a Lyapunov condition for the triangular CLT. Distinct limiting estimator values separate infinite nested-corner spectral laws. In the limiting field, once Raposo's first two angular modes are rescaled to Brownian motions with variances a and b-1, dyadic quadratic variation recovers those parameters pathwise, so different parameter pairs are singular. The finite-grid Gaussian Hellinger, KL and chi-square formulas are standard and were rederived.

## Originality

**PASS** — Raposo's September 2026 source constructs the two-parameter generalized Gaussian field and identifies the perturbation of its first two Fourier modes as the limit of a two-parameter Wigner corner process. Borodin supplies older Wigner-submatrix GFF fluctuation theory, and Feldman-Hajek supplies the general Gaussian equivalence/singularity framework. The trace identities and Brownian quadratic variation are elementary and are not claimed new. Targeted searches did not locate the combined source-specific result: explicit unbiased spectra-only estimators for both Wigner parameters, the exact finite-n variance with harmonic correction, infinite-corner singularity under nuisance-law changes, and the matching pathwise field separator. This is a legitimate inference theorem built from a new model rather than a new general Gaussian-measure principle.

## Scientific value

**PASS** — The result shows that the two interpolation parameters are statistically identifiable from very low-degree functions of nested spectra and become pathwise invariants in the continuum field. The exact variance calculation links finite-corner estimation to Brownian quadratic variation and makes the infinite-dimensional singularity operational rather than merely abstract.

## Sources

- **Interpolation of Gaussian Free Fields via Random Matrices** — Gabriel Raposo. https://arxiv.org/abs/2609.20707 — Primary 2026 source; constructs a two-parameter Wigner-corner field and describes the parameters through perturbations of the first two Fourier modes.
- **CLT for spectra of submatrices of Wigner random matrices** — Alexei Borodin. https://arxiv.org/abs/1010.0898 — Prior nested-Wigner/GFF fluctuation background.
- **Gaussian Measures** — Vladimir I. Bogachev. https://doi.org/10.1090/surv/062 — Classical Gaussian equivalence/singularity background; the record's pathwise separator is an explicit source-specific realization.

## Limitations

- The finite-matrix formulas use the complex Hermitian normalization of Raposo's model.
- The b estimator is explicit but not claimed minimax or efficient for the full nested-spectrum experiment.
- The CLT uses the source's all-moments assumption although weaker moment hypotheses would suffice.
- Continuum mutual singularity requires arbitrarily fine radial observation; positive-variance laws on any fixed finite grid are equivalent.

## Independent checks

```json
{
  "trace_identities_reconstructed": true,
  "exact_b_variance_rederived": true,
  "strong_law_and_clt_conditions_checked": true,
  "finite_grid_gaussian_divergences_checked": true,
  "raposo_model_abstract_and_first_two_mode_description_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked before institutional retrieval. Any inaccessible comparison is explicitly identified above rather than claimed read.
