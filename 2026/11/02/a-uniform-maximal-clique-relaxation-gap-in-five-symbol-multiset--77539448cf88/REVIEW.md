# Scientific review

## Correctness — PASS

The theorem's domain is the full quinary multiset unit-transfer graph at every integer length \(n\ge8\). All maximal cliques are covered by either lower deletion cliques or upper shared-insertion cliques. The explicit rational perturbation of the constant \(1/5\) point has exactly five disjoint corner supports at this threshold, and no clique meets two supports. Every lower-clique perturbation is nonpositive; every upper-clique perturbation is within the support-dependent slack, as verified by the complete outside-profile table in RESULT.md. Each corner adds \(4/15\) in total mass, giving a rigorous bound of \(\binom{n+4}{4}/5+4/3\). The known exact integer optimum yields the strictly positive gap. The standalone exact-rational verification replay confirms seven finite instances; infinity follows from the proof, not the replay.

## Originality — PASS, with residual risk

The July 2026 preprint by Zabokritskiy is decisive prior work: its Section 6 proves the *integer* quinary independence number exactly for the full length range, and its Section 3 formulates the general fractional local-cover and clique-packing LP. Its Remark 9.7 exhibits a *different* maximal-clique defect at alphabet 32 and degree 28. Neither statement implies the current uniform, explicit five-symbol maximal-clique relaxation defect, and the five-symbol proof uses non-clique templates without claiming that all clique-only certificates must fail. The January and March 2026 Kreindel–Essayag–Zabokritskiy papers give channel constructions and volume bounds, not this conclusion. The original full text of the 2016 Kovačević–Tan source remains uninspected; unindexed equivalent work remains a realistic priority risk. See AUDIT.json for actual scientific source comparisons and searches.

## Value — PASS

This is not an incremental refinement of a known integer code size. It identifies a uniform structural limitation of an entire major class of coding bounds: even *all* maximal-clique inequalities leave an additive gap of at least \(8/15\) for every length from eight onward. It explains why stronger, non-clique tile inequalities are genuinely needed in the contemporary sharp quinary theory, and the rational boundary construction provides a reusable proof pattern rather than a single numerical experiment.

## Scientific limitations and evidence

The exact optimum of the fractional clique LP is not determined, only a universal strict lower bound. The theorem is for five symbols and one deletion, not all alphabets or deletion radii. The checker enumerates only the displayed finite lengths and cannot prove the infinite claim by itself. Full independent audit and exhaustive publication-priority review have not occurred.

Self-review: passed. Independent audit: not yet performed.
