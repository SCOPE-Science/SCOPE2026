# Review of All 2-secure dominating sets of complete multipartite graphs

## Correctness
PASS. The necessity of the inequality \(k-s_i\ge\min\{c_i,3\}\) is forced by attacking two omitted vertices in a part: two outside defenders are necessary, and when at least three vertices remain omitted a third outside selected vertex must remain after the move. Sufficiency follows by a complete same-part/different-part attack split. In the different-part case, the two defender neighborhoods cover all of \(S\), so two distinct representatives exist because \(|S|\ge2\), and the moved set automatically meets both attacked parts. The coefficient formulas are exact counts of the only possible bad events, with the unique \(k=4\) pairwise-overlap correction. Exhaustive definition-level verification agrees through order ten.

## Originality
PASS. The 2017 initiating paper was inspected in full: it defines 2-secure domination and proves complexity results for split and bipartite graphs, but gives no complete-multipartite classification or enumerator. The 2020 full preprint was also inspected and searched for complete bipartite, multipartite, and polynomial formulations; it develops algorithms, complexity, and approximation results but not the present theorem. The 2022 secure 2-domination paper was inspected specifically because of the alias risk and was confirmed to define a different one-attack invariant on 2-dominating sets. Targeted semantic-database and literature searches found no equivalent three-guard condition or coefficient formula.

## Value
PASS. Two-secure domination was introduced to model two simultaneous attacks and is NP-complete even on bipartite and split graphs. The complete multipartite theorem converts that global exchange condition into a sharp local guard-cap rule and then enumerates all feasible sets by size. This gives substantially more structural information than a minimum-value formula and supplies exact benchmark instances for an algorithmically hard parameter.

Same-model review: passed. Independent audit: not yet performed.
