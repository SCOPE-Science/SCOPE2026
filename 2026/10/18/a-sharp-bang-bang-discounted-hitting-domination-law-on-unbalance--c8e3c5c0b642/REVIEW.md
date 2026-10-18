# Scientific review: discounted hitting domination on unbalanced complete bipartite graphs

## Correctness — PASS

The exact support equations reduce a labeled biclique to two rational values only when each part has an unselected vertex; the proof handles the full-part boundaries separately. The crucial inequality is transformed into a concave rational graph \(s=f(t)\) and minimized on its endpoints. This proves a genuine lower bound for every integral selection, while direct one-side or balanced rounding gives sharp upper bounds. The endpoint \(\tau=\lambda\) and the all-source regime \(\tau>\lambda\) are proved separately. An independent rational pinned-transition solver checked 1,860 graph/subset systems against the reduction and 11,160 exact feasibility decisions; 4,770 profile checks tested the discrete bounds. Finite checking is corroboration rather than the universal proof.

## Originality — PASS, residual risk retained

The closest work is Allagan–Pereyra–Massey, arXiv:2609.31535v1, whose sections on graph families cover spiders, stars and complete graphs; its general mixed-integer formulation is acknowledged, but does not give the biclique-specific sharp two-mechanism bound, parameter-independent aspect-ratio phase boundary, or the exactly sharp additive-one integer gap. Earlier group-hitting query and finite-horizon random-walk domination work use different optimization objectives. Search-index comparisons revealed no covering biclique formula. The theorem is restricted to \(2\le a<b\). The equal-size and star boundaries are excluded from the originality scope; the published star formula does not imply the new unequal-size aspect-ratio-dependent bound or optimizer polynomial. Full text of one historical group-hitting-probability article was not obtainable, and equivalent unindexed literature cannot be ruled out.

## Value — PASS

The minimum number of verified sources subject to an *every-vertex* discounted random-walk floor is newly motivated. The theorem supplies an analytic near-exact optimizer law valid for every unbalanced part-size pair \(2\le a<b\) and every real fidelity/threshold pair, a sharp design regime switch at a threshold-independent aspect ratio, and an exact optimizer count without enumerating vertex subsets. The small strict integrality-gap example shows why a simple floor of a continuous optimum is insufficient. These are structural conclusions, not merely substitution into a generic pinned matrix equation.

## Boundaries

No result is claimed for other bipartite graphs, asymmetric or heterogeneous walks, or an exact single closed ceiling formula in the balanced regime. The general-purpose linear-solver and MILP methods of the originating work remain prior art. The independent scientific review status is unperformed.

Self-review: passed. Independent audit: not yet performed.
