# Self-review

## Correctness — PASS
Direct graph-walk expansion gives all diagonal and off-diagonal entries of the cubic Runge–Kutta completed step. The edge-entry quadratic has negative discriminant, each diagonal cubic decreases strictly, and distance-two entries have a single explicit sign transition. These facts prove the exact all-tree cutoff, rather than inferring it from finite experiments. The convex-forward-Euler identity proves the universal degree bound, and diagonal comparison plus direct star entries proves unique star maximality. `check_tree_coefficients.py` independently replays exact integer formulas on 18,248 labelled trees of orders two through seven; its finite scope is explicitly non-probative for infinite families.

## Originality — PASS, with residual priority risk
The closest checked primary texts are Horváth (2005), Gottlieb–Grant–Higgs (2014), and Horváth–Song–Terlaky (2014). Their respective contributions are general RK positivity radii, SSP coefficients, and polyhedral invariance thresholds, not the exact local all-tree third-order cutoff with a unique star maximizer and the saturated-three-hub equality classification. Related exact graph results use different rational maps or the fourth-order polynomial on small-degree graph families. Alternative descriptions via graph heat generators, stochastic matrices and stability polynomials were searched. No equivalent covering statement was found; absence from accessed literature is not proof of universal priority. See AUDIT.json for specific semantic comparisons and source-inspection scope.

## Value — PASS
Sharp positive time steps for tree-structured diffusion have direct mathematical motivation. The result supplies a linear-time local certificate and two complete fixed-degree extremal classifications, proving exactly when SSP Euler inheritance is conservative and how much structure is needed for sharpness. It is neither a finite lookup table nor merely the generic sufficient SSP constraint.

## Limits
Only the completed three-stage third-order step on unweighted undirected trees with at least three vertices is covered. No assertion is made for stagewise positivity, weighted graphs, or general nonlinear systems. Cubic roots may require numerical approximation. The proof handles arbitrary sizes; computations are supplementary. Possible unindexed prior coverage remains a risk. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
