# Independent Audit — 2026/09/19/renyi-integrability-spectrum-gaussian-magnitudes--5d956edf6d4a

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `89783d47a4c827fde33fffe6862e7a0db068e347`
- Disposition: **PASSED**

## Correctness

**PASS** — The folded-likelihood argument is correct. Extending the magnitude likelihood evenly gives the coordinate-sign average bar L=2^{-(n-1)} sum_S L_R(Sx). Positivity and convexity yield 2^{(n-1)(1-gamma)} E[L_R^gamma] <= E[bar L^gamma] <= E[L_R^gamma], so folding has exactly the same integrability threshold as the full Gaussian likelihood. The Gaussian integral is finite exactly when gamma R^{-1}-(gamma-1)I is positive definite, equivalently lambda_max(R)<gamma/(gamma-1). The additive divergence gap is bounded by (n-1)log2, so the top-eigenvalue determinant singularity gives the stated critical logarithmic coefficient. For integer m, expanding the sign average and fixing one common sign produces the submitted determinant sum. At order two, coordinate-sign averaging is the orthogonal projection onto even Hermite multiindices, giving the Parseval series; Wick's formula yields the pair and triangle terms. In two dimensions the surviving terms sum as sum_{j>=1}rho^{4j}, hence D_2=-log(1-rho^4).

## Originality

**PASS** — Ouimet-Greaves introduce a lower-bound certificate for order-two Rényi total correlation of Gaussian magnitudes, not the exact folded likelihood analysis here. The accessible 2023 and 2025 multivariate folded-normal papers focus respectively on marginals/conditionals/estimation and characteristic/moment-generating functions; targeted full-text searches found no Rényi or entropy-divergence treatment there. The 2013 folded-normal paper and its later correction concern distributional moments rather than the spectral Rényi threshold. Searches did not locate the exact integrability criterion, determinant formula, even-Hermite decomposition, or bivariate -log(1-rho^4) identity. The novelty claim is therefore narrow but supported.

## Scientific value

**PASS** — The theorem identifies a sharp and somewhat counterintuitive phenomenon: discarding all Gaussian signs can reduce divergence without extending its Rényi integrability range. It gives exact integer-order formulas, a critical blow-up law, and explicit weak-dependence structure. The bivariate closed form and equicorrelation threshold make the result directly interpretable and substantially strengthen the source's one-sided certificate.

## Sources

- **A proof of the strong Gaussian product inequality conjecture** — Frédéric Ouimet; Dylan Greaves. https://arxiv.org/abs/2609.20234 — Primary 2026 source for the strong product inequality and its Rényi total-correlation lower-bound certificate.
- **Properties and Estimations of a Multivariate Folded Normal Distribution** — X. Liu; Y. Jin; Y. Yang; X. Pan. https://doi.org/10.3390/math11234860 — Open-access 2023 folded-normal paper on marginals, conditionals, independence and estimation; no Rényi/entropy-divergence statement was located.
- **Characteristic function and moment generating function of multivariate folded normal distribution** — Matej Benko; Zuzana Hübnerová; Viktor Witkovský. https://doi.org/10.1007/s00362-025-01711-z — Open-access 2025 distributional paper; full-text search found no Rényi or entropy treatment.
- **On multivariate folded normal distribution** — Ashis Kumar Chakraborty; Moutushi Chatterjee. https://doi.org/10.1007/s13571-013-0064-5 — Earlier multivariate folded-normal distribution paper; its abstract and later correction concern moments/distributional properties rather than information divergence.

## Limitations

- The main theorem assumes positive-definite R; singular Gaussian laws are not classified.
- Closed determinant sums are provided for integer Rényi orders, while noninteger orders receive only the exact finiteness threshold and critical asymptotic.
- The Hermite/Wick expansion is specialized to order two.
- Older folded-normal literature is broad, so a differently phrased information-divergence calculation remains a residual originality risk despite targeted searches.

## Independent checks

```json
{
  "likelihood_sign_average_reconstructed": true,
  "two_sided_convexity_bound_checked": true,
  "critical_coefficient_checked": true,
  "integer_determinant_formula_checked": true,
  "hermite_projection_checked": true,
  "bivariate_series_sum_checked": true,
  "liu_2023_open_access_checked": true,
  "benko_2025_open_access_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
