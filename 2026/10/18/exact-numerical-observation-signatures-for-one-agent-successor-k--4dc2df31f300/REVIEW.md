# Scientific review

## Correctness — PASS

All admissible equalities of successor terms reduce to Boolean constants or designated numeral tests; every knowing-value target reduces to the one non-rigid constant or a rigid target. A structural induction calculates modal truth only from the local observed value tag, the set of available named values, and the count of unnamed distinct values truncated at two. Depth-one characteristic formulas show that this invariant is complete, and directly force every member of the sharp \(|T|+r\) minimal representative. Counting all realizable characteristic triples gives the exact finite theory and formula spectrum. A standalone checker independently tested the original and signature semantics on 82,880 finite rooted instances; see `VERIFICATION.md`. The induction, not the checker, covers arbitrary modal depth, infinite world sets, and every \(k\ge0\).

## Originality — PASS, with priority uncertainty

The primary 2026 Wang article establishes general decidability and finite-model properties, not the restricted numeral-observation equivalence signature or sharp linear cutoff. Wang–Fan (2014) proves a complete S5 knowing-value calculus; Gu–Wang (2016) supplies general bisimulation machinery. These older theorems provide conceptual background but the inspected statements do not establish the explicit observation-truncated invariant together with the exact classification, optimal model size, and formula-theory census. The closest checked published quantitative certificate result bounds unrestricted formula-size complexity, not this observation parameter. Targeted searches found no equivalent exact theorem; absence in search is not a uniqueness certificate, and a bisimulation-theoretic specialization may remain in older literature.

## Value — PASS

The result is a complete expressivity classification for a natural bounded numerical-observation fragment of a recently introduced logic. It determines the exact information preserved under arbitrary nesting of the interacting knowledge and knowing-value operators, gives a constructive depth-one translation, proves the optimal smallest model in each theory, and enumerates all pointed theories and formula classes. The threshold of two unobserved values is semantically forced by the conditional knowing-value operator, not an arbitrary finite-model cutoff.

## Closest literature and limitations

Sources: Hongyi Wang (2026), arXiv:2606.31891; Wang and Fan (2014), *Conditionally Knowing What*; Gu and Wang (2016), arXiv:1604.08709; published quantitative certificate result linked in `RESULT.md`. The result excludes multiple constants or agents, additional propositions, unbounded numerator observations, and announcement dynamics. Broader characterization theorems of knowing-value bisimulation are a residual originality risk. Finite testing is supporting evidence only.

Self-review: passed. Independent audit: not yet performed.
