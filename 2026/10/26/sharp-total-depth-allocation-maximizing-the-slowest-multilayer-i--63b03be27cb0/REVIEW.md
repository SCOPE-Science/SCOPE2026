# Self-review

## Correctness — PASS
For every positive depth vector, the alternating reciprocal-jump test vector has generalized weight \(S\) and total interface variation \(2S\). Weighted Cauchy–Schwarz gives the global lower eigenvalue bound \(4S/H\); its strict equality condition forces the unique allocation. Direct substitution produces the predicted eigenpair at that allocation, and the sign-conjugated irreducible tridiagonal matrix has a positive Perron eigenvector, proving the eigenvalue is the largest. This also proves the bound holds for all integers \(N\ge2\), not merely checked small dimensions. The exact three-layer speed ratio follows from the generalized matrix trace. All positivity, endpoint conditions, and mode index conventions were checked. The numerical checker passes 13,200 assertions but does not replace the analytical proof.

## Originality — PASS, with residual priority risk
The classical multilayer modal problem is documented by Shimizu (2011) and the three-layer forward problem by de Melo Viríssimo–Milewski (2019). Their examined material describes modal construction, orthogonality, and nonlinear three-layer dynamics, not the global fixed-total-depth allocation across arbitrary layer number and independently prescribed interface buoyancies. Indexed scientific source/parameter/alias comparisons did not show an equivalent or dominating optimization. The novelty claim is confined to the explicit sharp all-\(N\) design theorem and strict uniqueness. The complete original Shimizu publisher PDF remained inaccessible, and an equivalent derivation in older specialized literature cannot be excluded without independent historical review. A failed search is not proof of priority.

## Value — PASS
Layer thickness is a genuine physical design variable constrained by a natural fixed total column depth. The exact optimizer proves that the interior depths balance adjacent inverse reduced gravities and gives a strong invariant consequence: a three-layer optimal column always places half its depth in the middle layer, independent of the two unequal interface strengths. This is a complete closed-form modal-control classification for arbitrary layer count; it is not merely a restatement of a standard inequality. The result neither predicts nonlinear wave behavior nor optimizes finite-wavelength dispersion, so those are explicit physical limits.

## Closest prior sources and access limits
- K. Shimizu, *A Theory of Vertical Modes in Multilayer Stratified Fluids* (2011), https://doi.org/10.1175/2011JPO4546.1. Publisher-indexed sections and summary were reviewed, not the inaccessible full PDF.
- F. de Melo Viríssimo and P. A. Milewski, *Three-layer Flows in the Shallow Water Limit* (2019), https://nora.nerc.ac.uk/id/eprint/527073/1/2018-SAPM-deMeloVirissimoMilewskiREVISION.pdf. Full accessible manuscript examined in the relevant sections.
- Additional comparison included two-layer quasigeostrophic thickness-instability optimization (different dynamics and objective) and publicly indexed graph-spectral optimization results (different operators and constraints).

Self-review: passed. Independent audit: not yet performed.
