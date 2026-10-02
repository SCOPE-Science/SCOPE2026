# Independent audit — 2026-10-01

## Finding

**Disposition: passed.** The final claim was reassessed on correctness, originality, and scientific value.

## Correctness — PASS

The frame space of four independent central hyperplanes has dimension 12. Evenness reduces the 16 cone volumes to 7 independent defects and each of four 8-piece central sections to 3 defects, for 19 total. Even interior bump pairs can span the 7 cone defects while avoiding all four hyperplanes; for each section, four bump pairs supported on that hyperplane away from the other three span its 3-dimensional sum-zero section-defect space. The h-derivative is therefore block-triangular and onto. Parametric transversality then makes the partial 12-dimensional frame map transverse to 0 for a comeager set of small even C^2 perturbations, which is impossible at a zero because 12<19. Small perturbations preserve smooth strict convexity.

## Originality — PASS

The closest four-dimensional result found is Soberon's nonequipartition theorem for a smooth mass and affine hyperplanes; it neither imposes origin symmetry/centrality nor simultaneous section equipartition. The 3D symmetric-Mahler paper is motivation, while Abraham supplies only the general transversality tool.

### Equivalent formulations

Soberon's affine mass result is not equivalent because the density need not be an even indicator of a centrally symmetric convex body and it imposes no simultaneous section equipartitions.

### Broader coverage

None of these sources implies the exact 19-defect versus 12-frame simultaneous-section obstruction for symmetric convex bodies.

### Exact database or table

The claim is an analytic generic-existence theorem, not a finite database result.

### Claim versus prior implication

The audited theorem requires an independent transversality argument and is not a corollary of the identified prior results.

### Sources inspected

- Equipartitions and Mahler volumes of symmetric convex bodies — https://arxiv.org/abs/1904.10765: BACKGROUND_NOT_COVERING. It concerns the 3D symmetric construction, not the claimed 4D generic failure.
- Four hyperplanes do not always equipartition a mass in R^4 — https://arxiv.org/abs/2608.23312: RELATED_NOT_COVERING. It treats a smooth positive mass and affine hyperplanes, with no simultaneous central-section requirement or origin-symmetric convex-body indicator.
- Transversality in manifolds of mappings — https://doi.org/10.1090/S0002-9904-1963-10969-6: GENERAL_METHOD_ONLY. It supplies parametric transversality, not the problem-specific defect map or surjectivity construction.

## Scientific value — PASS

The theorem rules out the direct four-dimensional analogue of a concrete simultaneous equipartition mechanism used in the symmetric Mahler program. The generic obstruction is structural, applies arbitrarily close to the ball, and is not merely a tiny-instance calculation.

## Limitations and residual risks

The theorem is generic-existential rather than an explicit coordinate counterexample. It concerns exact simultaneous central equipartition and does not address approximate, affine, or relaxed variants.
