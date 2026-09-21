# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The lower bound is witnessed by an explicit ten-word binary code and is directly checked against the complete three-word separating condition.

For the upper bound, the argument first reduces any hypothetical eleven-word code to minimum distance d in {2,3,4}: distance 1 contradicts the separating condition for a closest pair and any third word, while distance at least 5 contradicts the coordinatewise pair-distance sum bound 55d <= 8 floor(11^2/4).

After normalizing a closest pair to 0^8 and 1^d0^(8-d), every third word is classified by the two orbit parameters (alpha,beta) under S_d x S_(8-d). The listed inequalities 1 <= alpha <= d-1, alpha+beta >= d, and beta >= alpha are necessary and enumerate all feasible orbits. For every orbit representative, the standalone verifier exhaustively checks all completions. Pairwise compatibility is used only as a necessary condition; the search additionally verifies the separating condition for every newly formed triple. Its coloring step is solely an upper bound for safe pruning. Every orbit has maximum total size at most 10, so the upper bound is complete.

The verification artifact was also checked to reproduce the stated orbit maxima and the final value 10.

## Originality

PASS, to the best of our knowledge.

The 2023 Korže–Vesel paper establishes the coding-theory equivalence, reports gp(Q_8) >= 10, and states that exactness was confirmed only through dimension 7. More importantly, the August 2026 survey *The General Position Problem: A Survey* explicitly states that the only exact hypercube values known are gp(Q_1) through gp(Q_7), with gp(Q_7)=9, and again identifies the problem with maximum (2,1)-separating systems. This is strong current-status evidence that the exact Q_8 value remained open immediately before this record.

Searches also covered binary frameproof codes, wide-sense 2-frameproof codes, (2,1)-separating systems, hypercube general-position numbers, and the equivalent descendant formulation. Panoui's 2012 thesis was inspected at the relevant chapter: it treats exact small lengths 2, 3, 4 and separately length 5, not length 8. Zhao–Zhang (2024) was inspected at its definitions and stated general bounds; for binary alphabets it confirms that ordinary and wide-sense frameproof codes coincide. Sun–Wang (2025) is directly relevant because it gives newer general upper bounds, but the full theorem text was not accessible from the inspected publisher page; the abstract was inspected. The subsequent August 2026 survey still lists exact hypercube values only through Q_7, which substantially reduces but does not eliminate the residual risk that an equivalent length-8 statement is hidden under another formulation.

No matching SCOPE record was found under the direct or synonymous formulations checked before publication.

## Value

PASS.

The result closes the first unresolved dimension after the known exact sequence Q_1 through Q_7. It simultaneously determines an exact small parameter in three standard formulations: binary (2,1)-separating systems, binary 2-frameproof codes, and general-position sets in Q_8. The lower bound 10 was already known, so the substantive contribution is the matching upper bound and the resulting exact value.

## Scientific limitations

The upper bound is computer-assisted after an exact mathematical reduction; it does not yet supply a general formula for gp(Q_n) or a reusable closed-form upper bound for all larger n. The 2025 Sun–Wang full text was not inspected, leaving a specific residual originality uncertainty about consequences not visible from its abstract. Originality is therefore asserted only to the best of our knowledge.
