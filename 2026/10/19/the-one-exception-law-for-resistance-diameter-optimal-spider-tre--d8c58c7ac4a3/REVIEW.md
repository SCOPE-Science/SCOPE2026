# Scientific review

## Correctness — PASS
The tree resistance metric reduces the global diameter to the maximum of sums of two hub-to-leaf resistances. Strict convexity of the reciprocal-power expenditure fixes every individual edge resistance once an arm radius is specified. A second strictly convex normalized program over the arm radii is solved by separating the all-radii-at-most-one-half face from the single-radius-over-one-half face; no candidate regimes are omitted. The unique interior critical point exists exactly when one price aggregate is more than half the total. Budget homogeneity then fixes the exact minimum and every edge conductance. The exponent transition follows by a strictly decreasing ratio of powers. The independent numerical matrix checks supplement but do not replace this proof.

## Originality — PASS, with residual risk
The broad minimax pairwise effective-resistance objective **is not new**: Ghosh–Boyd–Saberi (2006), section VII, explicitly propose its convex semidefinite optimization for a linear budget. Their 2008 article, section 5.1, solves a different **sum** objective on trees, while section 8 repeats the general minimax suggestion. The new claim is limited to closed-form uniqueness, the all-priced spider classification for every positive power exponent, its sharp one-dominant-arm boundary, and the exponent-induced transition. The actual problem statements and algorithm of Chepoi–Noltemeier–Vaxès treat linear shortening of bounded fixed lengths; Hambrusch–Lim is an older tree-diameter edge-reduction framework whose accessible abstract also describes reductions rather than reciprocal-conductance power-law budgets. The latter full text was inaccessible, and equivalent unindexed derivations remain possible. Relevant semantic result searches found polytopal diameter, spider curvature and spider power-domination results rather than the stated physical network design; these negative results are not uniqueness proof.

## Value — PASS
The theorem characterizes all optimal individual conductances for an infinite, heterogeneous network family with adversarial source–sink placement. The one-exception boundary is a structural constraint on **every** optimum, not a numerically selected symmetric candidate. A nontrivial exponent threshold on one fixed topology demonstrates that changes in the budget's nonlinear price rule can switch the optimal geometry even when no edge is removed. Exact extremal cutoffs and uniqueness answer a natural fixed-topology sizing question.

## Remaining scientific limitations
No results for cyclic graphs, arbitrary branched trees, capacities or disconnected solutions. Prior work could imply the all-parameter formula by specialization; the abstract-only tree-upgrading source could not be fully compared. Numerical experiments are finite, and independent expert audit has not been done.

Self-review: passed. Independent audit: not yet performed.
