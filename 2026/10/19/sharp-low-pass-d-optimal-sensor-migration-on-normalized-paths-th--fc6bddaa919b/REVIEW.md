# Review of the low-band path sensor classification

## Correctness
**PASS.** The normalized-path eigenvectors and eigenvalues are given explicitly, and the observation determinant factors into an evolution-only Vandermonde factor and a site-only Fourier coefficient product. This verifies the all-evolution quantifiers and the endpoint normalization, including the full-band small-path boundary cases. The two- and three-mode placements follow from monotonicity and an exact one-variable extremum; the four-mode placements follow from the cubic cosine identity, a strict analytic bound against the other critical region, and a finite list of exact small-path evaluations. The limiting determinant ratio is \(16\). The executable checker confirms the stated finite illustrations but does not replace the proof for unbounded path size.

## Originality
**PASS, qualified.** Full-text comparison with the published *Universal endpoint optimality for dynamical sampling on normalized paths* establishes that its determinant theorem assumes the entire \(N\)-mode path space. That statement does not imply the very different fixed low-band \(m=4\) optimality asserted here: in fact its endpoint placement contrasts with our first-interior optimizer for \(N\ge10\). The published cycle-graph two-sensor result has a different operator, graph and objective. Huang–Needell–Tang's 2024 randomized sampling article does not establish this exact deterministic classification. The motivating September 2026 preprint's abstract and provenance were checked, but the complete manuscript remained inaccessible; an exact claim hidden in its uninspected sections is the leading residual priority risk.

## Value
**PASS.** A single vertex observed across consecutive times is a canonical minimal dynamical-sampling design on graph Paley–Wiener spaces. This theorem determines the D-optimal placement and every tie for the first two, three and four low-pass bands; the four-mode migration and the asymptotic sixteen-fold information gain distinguish genuine low-pass geometry from existing full-spectrum endpoint optimality. The exceptional path sizes and universal spectral-filter independence are practically and structurally interpretable, not isolated numerical curiosities.

## Limitations and nearest literature
No result is asserted for more than four active modes, E-optimality, arbitrary observation schedules or multiple sensors. The complete paper arXiv:2609.25472 was not readable via the attempted lawful routes, limiting the priority assessment. The relevant full-spectrum path theorem and the cycle two-sensor theorem were inspected in their publicly available complete result texts. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
