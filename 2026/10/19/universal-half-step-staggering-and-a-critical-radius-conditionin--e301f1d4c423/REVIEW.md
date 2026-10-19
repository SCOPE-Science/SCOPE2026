# Self-review: two-ring polynomial sampling

## Correctness — PASS

The relative phase enters every two-dimensional Fourier Gram block only through the same factor \(\delta(\theta)=|s^ne^{in\theta}-r^n|^2\); block traces are phase independent. For fixed trace, increasing the determinant increases the smaller eigenvalue and decreases the larger one. Positive monomial weights make this strict for all blocks, and the determinant is their product. Hardy trace/determinant reduction gives the displayed exact extreme eigenvalues, with monotonicity of both branches in the positive variable \(u\). The asymptotic argument tracks the smallest root through the determinant identity, avoiding numerical cancellation. The 160 direct-Gram spectral comparisons and 480 phase comparisons corroborate but are not relied upon for the theorem's quantifiers.

## Originality — PASS, best knowledge

Gröchenig–Ortega-Cerdà (2021, arXiv:2109.11825v1) develop normalized finite-polynomial/Fock sampling and asymptotic array criteria; Cruz–Massaneda–Ortega-Cerdà (2024, arXiv:2405.19945v1) develop geometric sampling/interpolation conditions for Bombieri polynomials. The exact two-regular-ring phase/spectrum and Hardy critical-radius law are not among their inspected main statements. The 2010 MathOverflow two-circle Fekete question proposes interlaced regular polygons but does not solve its unrestricted angular arrangement problem. The nearest indexed Szegő-orbit design result concerns a fixed-radius Blaschke-zero geometry. Its full text was not accessible, so any hidden overlapping general lemma remains a bibliographic risk. No claim of publication-priority certainty is made.

## Mathematical value — PASS

The result gives a common universal optimum of three competing linear sampling objectives, independent of positive radial coefficient weights, and isolates the exact boundary scale at which optimal Hardy reconstruction changes from exponentially ill-conditioned to bounded. The regular-grid restriction is mathematical substance: unrestricted Fekete arrangements, radius optimization and general nonlinear sampling are not resolved.

Self-review: passed. Independent audit: not yet performed.
