# Independent mathematical audit — SCOPE-20260913-062

Audit date: 2026-10-01 (UTC) UTC

Disposition: **passed**

## Final claim assessed

For the stated Kummer K3, non-split extension and Goldstein-Prokushkin/Fu-Yau balanced class, the pullback line subbundle and rank-two bundle have equal zero slope at every finite positive fiber scale; the pulled-back extension stays non-split, hence is strictly semistable and non-polystable and cannot carry a Hermitian-Yang-Mills metric in that balanced class.

## Correctness: PASS

The K3 intersection calculation gives \(D^2=-4\) and \(H\cdot D=0\); Riemann-Roch then gives \(\chi(L^2)=-6\), while ampleness and zero nontrivial degree exclude sections of \(L^{\pm2}\), so non-split extensions exist. In the Goldstein-Prokushkin/Fu-Yau ansatz, wedging the pullback of \(D\) with the balanced \((2,2)\)-form kills the purely horizontal term by base dimension and leaves a positive fiber coefficient times \(H\cdot D=0\). The Leray edge map is injective because the connected torus fibration has pushforward of the structure sheaf equal to the base structure sheaf, so the extension class stays nonzero after pullback. Extensions of equal-slope line bundles are semistable, and a non-split such extension cannot be polystable; the Gauduchon Kobayashi-Hitchin correspondence therefore rules out an HYM metric in this class.

## Originality: PASS

The Fu-Yau/Goldstein-Prokushkin literature supplies the balanced ansatz and HYM framework, but the inspected sources do not state this specific Kummer difference-class non-split pullback obstruction. Resultary returned only the audited record as the exact match.

### Originality comparisons

**equivalent_formulations.** Equivalent formulations would identify the same pullback as strictly semistable/non-polystable or exclude its HYM metric in the same balanced class; none was found.

Searches: Resultary: Goldstein Prokushkin Fu Yau pullback semistable extension degree zero balanced slope HYM; web: Goldstein-Prokushkin semistable pullback Hermitian-Yang-Mills

Evidence: No distinct exact obstruction for this extension was returned.; The primary Fu-Yau ansatz literature gives the metric/balanced form, not the chosen extension class.

**broader_coverage.** General ansatz and correspondence theorems provide the tools but do not imply the example until its slope and extension class are checked.

Searches: Phong-Picard-Zhang arXiv:1610.02740; Hull-Strominger bundle literature for GP/Fu-Yau fibrations

Evidence: The Fu-Yau ansatz formula is broad geometric infrastructure.; Standard HYM existence results cover polystable bundles but do not assert polystability for this non-split pullback.

**exact_database_or_table.** The claim is a geometric obstruction, not a tabulated invariant.

Searches: Resultary exact semantic search for the Kummer class \(e_1-e_2\) pullback

Evidence: No exact database/table entry was found.

**claim_vs_prior_implication.** The prior general machinery plus the new explicit class computation yields the result; the latter is not mechanically stated by the prior theorems.

Searches: arXiv:1610.02740 full-text Fu-Yau ansatz formulas; arXiv:2303.05274 for later Hull-Strominger obstruction context

Evidence: The inspected ansatz shows how the balanced form separates horizontal and fiber terms.; The later obstruction paper does not supply this particular extension-class calculation.

### Primary source inspections

- **The Anomaly flow and the Fu-Yau equation** (https://arxiv.org/abs/1610.02740): SUPPORTS the slope calculation but does not state the chosen extension obstruction. Material read: accessible arXiv full-text formulas and surrounding discussion of the Fu-Yau ansatz and norm-weighted square of the Hermitian form. Evidence: The ansatz decomposes the relevant balanced form into base and mixed fiber terms, which makes the pullback slope proportional to the base intersection \(H\cdot D\).


Checked sources: https://arxiv.org/abs/1610.02740; https://arxiv.org/abs/2303.05274; Resultary semantic search


Residual originality risks: Best-of-knowledge novelty remains subject to specialized non-Kähler bundle literature not surfaced by the searches.

## Scientific value: PASS

The result is a motivated obstruction for a concrete gauge-bundle construction in the Hull-Strominger setting: it separates the bundle/HYM issue from the anomaly equation and holds uniformly over every finite positive fiber scale in the stated ansatz. The exact class is geometrically natural on a Kummer K3 rather than a post-selected numerical slice.

## Limitations

The obstruction is confined to the stated Kummer class, extension, Goldstein-Prokushkin torus bundle and Fu-Yau balanced conformal class; other bundles/classes and the anomaly equation are outside scope.
