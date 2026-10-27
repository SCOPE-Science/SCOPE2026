# Scientific review

## Correctness — PASS
The block Schur complement is positive for \(0<\varepsilon<1/2\). A uniform spectral bound makes Type II with unit scaling strictly Euclidean contracting. Two explicit unit test vectors give incompatible inequalities for *any* positive Type-III scaling when \(\delta\le\varepsilon^6/4\). The sharp limiting gain follows from bounded near-minimizers and a constructive matching scaling. The spectral-radius and minimal-dimension claims follow from SPD similarity and one-dimensional complement equivalence. The rational example independently checks all parameter inequalities.

## Originality — PASS
The motivating 2026 article defines Type III and proves its nonsingularity; its displayed Richardson bounds concern Type I. Earlier additive coarse-grid comparisons chiefly concern spectra, conditioning, and deflation. Closely related scalar-complement Type-II classifications do not imply the anisotropic exact-fine Type-III separation or the sharp limiting gain. Published mathematical records were compared by implication, not just matching terminology. A fuller survey of older broad preconditioning theory could reveal a dominating general norm result; one relevant 2009 full text was not completely accessible.

## Value — PASS
A supposedly stronger exactly inverted fine block can destroy *all* scalar-tunable Euclidean one-step nonexpansion even though plain identity completion is safe and a spectrally convergent Type-III setting exists. The dimension-three minimality and sharp nonzero minimax amplification distinguish it from an isolated numerical anomaly. This informs preconditioner choice and transient-error diagnostics; no full-PDE performance claim is made.

## Limits
Exactly specified real SPD three-mode arrow matrices, a fixed one-dimensional reduced space, an exact complementary basic inverse, an unrelaxed fixed Richardson step, and exact arithmetic. The explicit finite-parameter cutoff is sufficient, not claimed optimal. Independent verification is not performed.

Self-review: passed. Independent audit: not yet performed.
