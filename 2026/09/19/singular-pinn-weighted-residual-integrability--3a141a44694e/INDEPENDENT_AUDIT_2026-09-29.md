# Independent Audit — 2026/09/19/singular-pinn-weighted-residual-integrability--3a141a44694e

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `da359bbd9857dcacf970a7fa69730abecf09456e`
- Disposition: **PASSED**

## Correctness

**PASS** — For every fixed finite smooth hard-constrained trial with a simple boundary zero, Softplus positivity gives u_hat(y,d)=a(y)d+O(d^2) with a(y)>0, while Delta u_hat stays bounded. Hence the singular source dominates and R=-a(y)^(-alpha)d^(-alpha)(1+o(1)). Multiplication by 1+beta u_hat^(-p) gives the leading density beta a(y)^(-(2 alpha+p))d^(-(2 alpha+p)); a smooth codimension-one collar has measure comparable to d sigma dd, so local finiteness is exactly 2 alpha+p<1. This yields the unweighted alpha<1/2 threshold and the source-weight p=alpha threshold alpha<1/3. The stated one-dimensional exact-solution correction follows by twice integrating u''~-a^(-alpha)x^(-alpha). The grid laws are ordinary generalized-harmonic-sum asymptotics. As an independent numerical check for u_hat=log(2)x(1-x), alpha=1/2, the weighted loss divided by sqrt(N) increases toward the predicted 2(log 2)^(-3/2)zeta(3/2)=9.0537267105 and the standard loss divided by log N toward 2/log 2=2.8853900818.

## Originality

**PASS** — Oulgiht's September 2026 preprint proposes the hard boundary factor, Softplus positivity and singularity-aware inverse-solution residual weighting, but its public description does not identify the continuum integrability threshold or the fixed-trial resolution blow-up. The broad principle that strong least-squares/minimum-residual formulations can exclude non-square-integrable singular data is established prior work, including Führer-Heuer-Karkulik, and classical singular elliptic theory supplies boundary regularity background. The audited contribution is therefore narrow and source-specific: the exact 1/2 versus 1/3 thresholds for this architecture/weight, the sharp collocation scaling, and the fractional boundary term explaining the mismatch. Targeted searches did not locate those source-specific statements.

## Scientific value

**PASS** — The result exposes a concrete failure mode in a newly proposed numerical objective: the extra singularity-aware factor can make population integrability strictly worse. The explicit grid-resolution law distinguishes finite-sample numerical well-definedness from an infinite-expectation objective, and the missing fractional boundary term points to a principled architecture or weak-form repair. It does not overclaim training failure or convergence theory.

## Sources

- **Deep Learning for Singular PDEs: A Weighted Neural Network Approach** — Badr Oulgiht. https://arxiv.org/abs/2609.19335 — Primary 2026 source; proposes hard Dirichlet enforcement, Softplus positivity and a singularity-aware weighted residual loss.
- **MINRES for Second-Order PDEs with Singular Data** — Thomas Führer; Norbert Heuer; Michael Karkulik. https://doi.org/10.1137/21M1457023 — Prior minimum-residual literature explicitly noting that standard least-squares/DPG formulations usually exclude non-square-integrable loads.
- **On a Dirichlet problem with a singular nonlinearity** — Michael G. Crandall; Paul H. Rabinowitz; Luc Tartar. https://doi.org/10.1080/03605307708820029 — Classical singular-elliptic background; not a PINN weighted-loss threshold result.

## Limitations

- The theorem is a fixed-finite-smooth-trial statement; a parameter sequence can develop resolution-dependent boundary layers and requires separate analysis.
- The multidimensional claim assumes a smooth boundary patch and a hard factor with a simple zero.
- The enrichment cancels only the leading singular residual and is not a complete architecture or convergence theorem.
- General singular-data least-squares obstructions and singular-PDE boundary asymptotics are prior art; novelty is limited to the source-specific thresholds and resolution law.

## Independent checks

```json
{
  "boundary_asymptotic_reconstructed": true,
  "collar_integrability_checked": true,
  "exact_1d_fractional_correction_checked": true,
  "harmonic_sum_grid_scaling_checked": true,
  "numeric_trial": {
    "trial": "log(2)*x*(1-x)",
    "alpha": 0.5,
    "predicted_standard_log_constant": 2.8853900817779268,
    "predicted_weighted_sqrt_constant": 9.053726710487835,
    "weighted_ratio_at_N_262144": 8.920842496263983
  },
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence; no repository mutation or separate dispatcher report was performed. Preprints and lawful open-access sources were checked first. No decisive originality comparison remained inaccessible, so Oxford Download was not required.
