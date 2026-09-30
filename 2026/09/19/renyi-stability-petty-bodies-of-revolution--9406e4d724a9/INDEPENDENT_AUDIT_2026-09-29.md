# Independent Audit — 2026/09/19/renyi-stability-petty-bodies-of-revolution--9406e4d724a9

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `153301a653cd06132ff7326f7d9e5a0a94c6616f`
- Disposition: **PASSED**

## Correctness

**PASS** — The quantitative reorganization of the Mielke-Sulz proof is correct. Their profile-measure factorization gives B(rho,...,rho) as a positive constant times the weighted integral of A_rho^(n-1), while the mixed identity makes B(rho,rho0,...,rho0)/B(rho0,...,rho0) equal to the profile-mass, hence to the normalized volume. With mu_n proportional to t^n/sqrt(1-t^2)dt and Y=X/E X, the source determinant estimate therefore becomes exactly Q(K^B)/Q(B)>=E_mu[Y^p]=exp((p-1)D_p), p=n-1. Blaschke symmetrization contributes the exact factor A(K)^p, so the two-channel bound follows. Rényi monotonicity, the D_2 identity and Pinsker give the stated CV and TV corollaries. For a right circular cylinder, the profile measure is an atom at 1, A_rho is proportional to 1/t, and direct projection-body volume agrees with the beta-integral moment ratio, confirming exact saturation of the strongest divergence bound.

## Originality

**PASS** — Mielke-Sulz prove the qualitative Petty inequality and equality cases and explicitly use the same weighted Hölder moment inside their proof, so the underlying transform inequality is not new. However, the inspected paper does not formulate the normalized Hölder slack as a Rényi divergence, does not state any deficit/stability, variance, total-variation or Pinsker consequence, and does not identify cylinders as exact non-ellipsoidal saturators of the strongest transformed-profile lower bound. Targeted searches did not locate this quantitative package. Originality is therefore limited to the information-theoretic normalization, explicit stability corollaries and cylinder sharpness—not to Petty's inequality or the profile transform itself.

## Scientific value

**PASS** — Although algebraically close to the source proof, the result extracts an explicit, sharp quantitative observable from what was used only as a qualitative Hölder step. It separates central-asymmetry and profile-shape channels, gives dimension-explicit CV/TV control, and proves that the order-(n-1) profile-divergence bound is globally sharp on every right circular cylinder. This is a useful stability statement in the transformed profile space, while appropriately stopping short of a geometric inverse-transform modulus.

## Sources

- **The Petty Conjecture for Convex Bodies of Revolution** — Florian Mielke-Sulz. https://arxiv.org/abs/2609.13517 — Primary 2026 source for the qualitative theorem, profile measure/transform, multilinear factorization and Hölder inequality used here.
- **Volumes of projection bodies** — Noah Samuel Brannen. https://doi.org/10.1112/S002557930001175X — Earlier quantitative work on the Petty quotient for special classes; no matching transformed-profile Rényi stability theorem was located.
- **On the shape of a convex body with respect to its second projection body** — Christos Saroglou. https://arxiv.org/abs/1409.4347 — Earlier lower-bound/background work for bodies of revolution, distinct from the audited profile-divergence refinement.

## Limitations

- The principal divergence inequality is a quantitative reinterpretation of slack already present in the Mielke-Sulz Hölder step; the novelty claim is deliberately narrow.
- Stability is measured only in transformed one-dimensional profile space, not in Hausdorff, Banach-Mazur, symmetric-difference or Wasserstein distance between bodies.
- No quantitative inverse modulus for the profile transform or for Blaschke asymmetry is proved.
- The theorem remains restricted to bodies of revolution.

## Independent checks

```json
{
  "source_pdf_checked": true,
  "source_pdf_screenshot_checked": true,
  "source_holder_factorization_checked": true,
  "profile_measure_mixed_identity_checked": true,
  "renyi_normalization_reconstructed": true,
  "cylinder_projection_body_formula_checked": true,
  "source_fulltext_terms_absent": [
    "stability",
    "Rényi",
    "variance",
    "Pinsker"
  ],
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
