# Independent audit — 2026-10-01

## Final claim

Exact Rényi-2 total correlation of Gaussian magnitudes

## Correctness — PASS

Expanding the folded-normal likelihood ratio over sign vectors and squaring under the independent Gaussian reference reduces \(e^{D_2}\) to Gaussian quadratic integrals with precision matrices \(B_s=R^{-1}+D_sR^{-1}D_s-I\). The all-positive sign term is finite exactly when \(2R^{-1}-I\succ0\), i.e. \(\lambda_{\max}(R)<2\); that inequality then makes every \(B_s\) positive definite. The bivariate determinant simplification gives \(-\log(1-ho^4)\). The even-Hermite projection removes odd coordinate degrees, so doubled edges give the quartic term and triangles the sixth-order term with factor eight. The inspected verifier independently checks representative determinant, bivariate, local-expansion and threshold cases.

Checked sources: Ouimet–Greaves, A proof of the strong Gaussian product inequality conjecture, arXiv:2609.20234; Benko–Hübnerová–Witkovský, Characteristic function and moment generating function of multivariate folded normal distribution, Statistical Papers (2025); van Erven–Harremoës, Rényi Divergence and Kullback-Leibler Divergence, IEEE TIT 60 (2014); Resultary 2026-09-19: Rényi integrability spectrum of Gaussian magnitudes

Residual risks: The result assumes positive-definite correlation matrices; singular support requires a different density formulation.

## Originality — PASS

Best-of-knowledge originality passes. The folded-normal density and generic Gaussian integration are prior art, and Ouimet–Greaves introduce the same Rényi-2 total-correlation quantity only as a lower-bounded certificate. No checked pre-2026-09-18 source states the exact sign-determinant formula, the sharp \(\lambda_{\max}<2\) integrability threshold, or the quartic-edge/sixth-order-triangle expansion. A later Resultary record generalizes this result rather than predating it.

### Equivalent formulations

Searches: Resultary: Gaussian magnitudes Renyi-2 total correlation folded normal determinant finiteness; Ouimet–Greaves arXiv:2609.20234; Benko et al. 2025 folded normal

Evidence: Resultary's closest exact record is the assigned result; the all-order spectrum appears one day later. Benko et al. provide the \(2^n\)-term folded density but not the Rényi calculation. Ouimet–Greaves discuss the quantity without evaluating the density ratio exactly.

Reasoning: The relevant equivalent formulations are chi-square divergence, \(L^2(Q)\) likelihood ratio, and Gaussian-mixture overlap; none of the checked sources states the resulting threshold and expansion.

### Broader coverage

Searches: generic Gaussian-mixture overlap identities; folded-normal density formulas

Evidence: Generic overlap integration explains the determinant mechanism, but no checked stronger theorem packages the sharp sign-averaged integrability criterion and local graph expansion for magnitudes.

Reasoning: Generic integration alone does not mechanically supply the theorem's full final claim.

### Exact database or table

Searches: bivariate absolute Gaussian Renyi divergence -log(1-rho^4); lambda_max(R)<2 folded Gaussian chi-square

Evidence: No independent pre-assignment exact table/formula was located.

Reasoning: This supports best-of-knowledge originality only.

### Claim versus prior implication

Searches: Ouimet–Greaves Corollary on Rényi total correlation; Benko folded-normal density

Evidence: Those ingredients allow a derivation, but the exact determinant evaluation, finiteness equivalence and Hermite cycle expansion require additional argument.

Reasoning: The final claim is not a mere parameter substitution into a stronger checked theorem.

### Source inspections

- **Characteristic function and moment generating function of multivariate folded normal distribution** (DOI:10.1007/s00362-025-01711-z): Provides a key input but not the Rényi-2 determinant theorem. Material read: Open-access full-text portions giving the sign-reflected multivariate folded-normal formula and transform setup. Evidence: The source formulates the folded density as a sign sum.
- **A proof of the strong Gaussian product inequality conjecture** (arXiv:2609.20234): Introduces/lower-bounds the information quantity but does not give the exact formula in the inspected material. Material read: Abstract and relevant description of the Rényi certificate. Evidence: The work uses normalized product moments as a certificate rather than direct density-ratio evaluation.
- **Rényi integrability spectrum of Gaussian magnitudes** (https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-renyi-integrability-spectrum-gaussian-magnitudes--5d956edf6d4a): Later generalization to all Rényi orders; chronology does not cover the 2026-09-18 result. Material read: Search summary and implication comparison. Evidence: Its summary explicitly includes order two as a special case while extending the integrability threshold to general order.

Checked sources: Ouimet–Greaves, A proof of the strong Gaussian product inequality conjecture, arXiv:2609.20234; Benko–Hübnerová–Witkovský, Characteristic function and moment generating function of multivariate folded normal distribution, Statistical Papers (2025); van Erven–Harremoës, Rényi Divergence and Kullback-Leibler Divergence, IEEE TIT 60 (2014); Resultary 2026-09-19: Rényi integrability spectrum of Gaussian magnitudes

Residual risks: Generic Gaussian-mixture \(L^2\) overlap formulas could contain an equivalent determinant specialization under different terminology. The later 2026-09-19 Resultary record generalizes the theorem, but it postdates and explicitly extends this earlier order-two finding.

## Scientific value — PASS

The theorem exactly evaluates a natural dependence measure already motivated by recent Gaussian-product work, identifies a sharp divergence boundary inside the correlation cone, and exposes a meaningful graph-structured weak-dependence expansion. This is a natural exact invariant with plausible reuse, not an arbitrary finite computation.

Checked sources: Ouimet–Greaves, A proof of the strong Gaussian product inequality conjecture, arXiv:2609.20234; Benko–Hübnerová–Witkovský, Characteristic function and moment generating function of multivariate folded normal distribution, Statistical Papers (2025); van Erven–Harremoës, Rényi Divergence and Kullback-Leibler Divergence, IEEE TIT 60 (2014); Resultary 2026-09-19: Rényi integrability spectrum of Gaussian magnitudes

Residual risks: Generic Gaussian-mixture \(L^2\) overlap formulas could contain an equivalent determinant specialization under different terminology. The later 2026-09-19 Resultary record generalizes the theorem, but it postdates and explicitly extends this earlier order-two finding.

## Limitations

- Positive-definite correlation matrices only; singular laws need a support-level formulation.
- The determinant sum is exponential in dimension.
- Only Rényi order two is claimed here; a later record generalizes it.

## Conclusion

Disposition: **passed**. A validated finding requires all three axes to pass.
