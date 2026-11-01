# Scientific review

## Correctness — PASS

The primary finite-dimensional formula follows from a complete classification of generic simplex-section vertices as crossed original edges. For a Haar normal the probability of crossing an edge is exactly its subtended Euclidean angle divided by \(\pi\). Both angle classes are derived from the regular-simplex Gram matrix; differentiation produces an explicit derivative whose sign reduces to \((n-2)(n+1)(2t+nt^2)\). This proves monotonicity and the second derivative at the centroid without numerical assumptions.

The Gaussian representation of the normal gives an exact sign-count identity for each interior point. At the endpoint, all \(n\) edges incident to the distinguished vertex collapse to a single vertex, and exchangeable Gaussian ranks supply the separate exact finite law; substituting the endpoint into the generic formula would be invalid. Empirical Gaussian CDF convergence yields the fixed-displacement distribution. The local empirical-CDF argument and an iid central-limit theorem, with explicit independence from the distinguished Gaussian coordinate, prove the critical-window chi-square law. The proof covers all stated dimensions, endpoints, quantifiers, and limiting regimes. The standalone checker yielded 2,183 successful finite assertions; these are diagnostics, not a proof of asymptotic or infinite-dimensional statements.

## Originality — PASS with priority risk

The closest published research records give the exact central random-section mean and central chi-square fluctuations, as well as joint central face counts. The present axial noncentral law does not follow from their centroid-only models: its finite derivative, vertex collision, and critical displacement produce genuinely different conclusions. The motivating arXiv paper treats deterministic extreme section volume, not random section-vertex distributions; Dirksen and König likewise study section volumes. The old random regular-simplex projection literature uses projections instead of sections through a prescribed off-center point. Search queries included noncentral orientation, vertex-section expectation, affine displacement, aliases in Gaussian sign counts, and the critical empirical-process formulation. No dominating identical statement was identified. An equivalent unindexed Gaussian-threshold or stochastic-geometry result remains a residual historical-priority risk.

## Value — PASS

The off-center displacement of a canonical regular simplex is a natural noncentral extension of a studied random-section problem. The exact finite-dimensional profile answers the geometric monotonicity question, with a separate combinatorial endpoint. The two different fluctuation scalings explain a genuine qualitative breakdown of the central chi-square law at a dimension-dependent displacement and give a quantitatively sharp interpolation of its coefficient. This is not a simple parameter substitution into the central case or a numerical invariant with no geometric use.

## Remaining limitations

The theorem is specific to Haar orientation and vertex-axis displacement. The macroscopic and critical-window limits are not stated uniformly over arbitrary dimension-dependent shifts. Older or inaccessible relevant literature could affect priority; independent verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
