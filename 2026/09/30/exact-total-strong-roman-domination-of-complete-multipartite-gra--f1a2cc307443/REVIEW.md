# Same-model review

## Correctness assessment
PASS. The proof reduces every feasible labeling to its positive support and defender parts, handles separately the presence or absence of a fully positive part, proves the parity lemma for the remaining two-defender optimization, and supplies explicit constructions meeting both candidate bounds. Edge cases including complete graphs, stars, bicliques, and graphs with only one non-singleton part are covered by the same formulas. The executable checks agree with the theorem for all 359 complete multipartite isomorphism types through order 13 at the support level and for all 37 types through order 7 by direct enumeration of the defining labels.

## Originality assessment
PASS. The introducing paper for total strong Roman domination develops general bounds and tree results and contains no complete-multipartite, complete-bipartite, or complete-graph exact treatment. The closest located neighboring literature concerns ordinary strong Roman domination, ordinary total domination, signed total strong Roman domination, or unique-response strong Roman domination; these use different feasibility conditions or different graph classes. No equivalent or stronger complete-multipartite formula was found in the compared literature. The contribution is therefore recorded as a best-of-knowledge exact specialization, not as a claim about unrelated Roman variants.

## Value assessment
PASS. The theorem gives a closed finite formula for an infinite graph class from only the part sizes, separates two genuinely different optimal mechanisms, and identifies a one-unit parity effect that is invisible in generic bounds. It yields immediate exact values for complete graphs, stars, complete bipartite graphs, and balanced or unbalanced Turán-type graphs.

## Closest literature
The primary source is Nazari-Moghaddam, Soroudi, Sheikholeslami, and Yero, *On the total and strong version for Roman dominating functions in graphs*, arXiv:1912.01093v1 / DOI 10.1007/s00010-021-00778-x. Hajjari and Sheikholeslami's 2022 signed total strong Roman paper studies a different signed parameter. Work on ordinary strong Roman domination and on total domination alone is not equivalent because one of the two defining constraints is missing.

## Scientific limitations
The theorem gives the minimum weight but not a classification or count of all minimum functions. The complete multipartite structure is used essentially, and no extension to arbitrary diameter-two graphs is asserted.

Same-model review: passed. Independent audit: not yet performed.
