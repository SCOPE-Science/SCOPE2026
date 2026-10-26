# Self-review

## Correctness — PASS

The explicit diagonal equivalence with a Frobenius companion proves the linearization; a determinant identity fixes the small singular-value scale. Two nonzero limiting singular values, first-order singular-vector equations, and exact restricted Gram invariants establish the complete theorem. The supplementary checker validates critical identities and finite samples but the quantified limits are analytical.

## Originality — PASS, with remaining bibliographic risk

Pérez (2026), Sections 4–6, constructs the direct scaled pencil and analyzes **exact** eigenvectors, explicitly not claiming computed-vector recovery control. Higham, Li, and Tisseur (2007) give the general backward-error-transfer phenomenon and norms; neither inspected source yields this particular sharp pseudospectral separation or the two exact coordinate-loss thresholds. Related 2025 global-bounds work was available at abstract level only and remains an explicit comparison risk. Targeted research-index searches found no equivalent formula, but a failed search is not a novelty proof.

## Mathematical value — PASS

The explicit construction measures how small an unstructured pencil residual may be without any coefficientwise polynomial accuracy, simultaneously for both recovery channels. The sharp recovery-block loss thresholds are meaningful calibration targets for stable-eigenpair extraction diagnostics. No QZ failure, general degree bound, or floating-point behavior is inferred.

## Independent validation status

Self-review: passed. Independent audit: not yet performed.
