# Independent audit — 2026-10-01

## Final claim

Crossing-only switch geometry in a threshold-controlled dengue model

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

The threshold normals are both the symptomatic coordinate normal. Direct substitution in the source vector field shows equal one-sided normal components on both \(I=kC\) and \(I=C\), so no ordinary attracting or repelling codimension-one Filippov sliding region occurs. At \(I=C\) the vector field itself is continuous. At a transversal fogging crossing, the jump affects only the mosquito \(U,V\) equations while the switching normal is in the \(I\) coordinate, so the saltation update is a rank-one nilpotent shear, hence unipotent with determinant one; the induced mosquito infection-fraction perturbation cancels exactly.

## Originality

The motivating dengue paper explicitly leaves Filippov sliding-mode analysis of the two switching manifolds as future work. Full-text inspection found no source result giving the crossing-only classification, the source-specific unipotent saltation form, or the Floquet determinant and mosquito-fraction consequences. Generic Filippov and saltation theory supplies the framework but does not imply these conclusions without evaluating this model's jump geometry.

### Equivalent formulations

Searches:
- Resultary semantic search for crossing-only dengue switching, Filippov sliding, saltation, hospital-capacity and fogging thresholds
- Web searches combining the exact source title with Filippov, sliding and saltation

Evidence:
- The exact published-record hit was the audited record; no independent source-specific theorem with the same conclusions was located.

Reasoning: The audited claim is not merely a renaming of generic saltation theory: it depends on the particular support and tangency of the dengue vector-field jump.

### Broader coverage

Searches:
- Aldila et al., arXiv:2607.18140 full text
- Kong et al., Proceedings of the IEEE 112 (2024), DOI 10.1109/JPROC.2024.3440211
- You et al., Math. Methods Appl. Sci. 47 (2024), DOI 10.1002/mma.10192

Evidence:
- Aldila et al. explicitly request a future Filippov sliding-mode analysis; Kong et al. give the general saltation matrix; You et al. study a different threshold-policy dengue model.

Reasoning: These sources cover the generic machinery or different models, not the evaluated geometry of the two switches in the 2026 hospital-capacity/fogging system.

### Exact database or table

This is an analytic model-specific theorem rather than a database/table lookup.

Searches:
- Resultary and web searches for source-specific threshold classifications and event matrices

### Claim versus prior implication

The final claim requires the source-specific calculation that the jump is tangent to the switching normal and proportional in the two mosquito coordinates; it is therefore not mechanically stated by either prior source alone.

Evidence:
- The source supplies the piecewise vector field but does not evaluate the two normal jumps; the saltation survey supplies the formula but not the model substitution.

### Source inspections

- **A Mathematical Model of Dengue Transmission Incorporating Hospital Capacity and Threshold-Based Fogging Interventions** — INPUT_NOT_COVERING. Material read: Full-text model formulation including the recovery function, fogging threshold, six ODEs, switching-regime description, and Conclusion/Future Works. Evidence: The paper defines the switches and explicitly lists a Filippov-based sliding-mode analysis of \(I=kC\) and \(I=C\) as future work. Source: https://arxiv.org/abs/2607.18140
- **Saltation Matrices: The Essential Tool for Linearizing Hybrid Dynamical Systems** — GENERAL_MACHINERY_NOT_COVERING. Material read: Abstract and section scope describing the general saltation sensitivity update. Evidence: It supplies the generic saltation framework, not the dengue-specific tangency, unipotence, determinant, or infection-fraction cancellation. Source: https://doi.org/10.1109/JPROC.2024.3440211

### Residual risks

- The literature search cannot prove global novelty, but the decisive primary source itself labels the Filippov analysis as future work and no later source-specific treatment was found.

## Value

This resolves an explicit analytical gap in a current nonsmooth epidemic model and supplies exact event geometry relevant to the periodic-orbit/Floquet computations already performed for that model. The result distinguishes the two operational thresholds and rules out a commonly expected sliding mechanism rather than merely recomputing an equilibrium.

## Limitations

The theorem excludes ordinary codimension-one sliding/escaping regions but not degenerate common tangencies; saltation conclusions require transversal crossings and do not prove periodic-orbit existence or stability.
