# Review of Domination-polynomial rigidity of complete multipartite graphs

## Correctness
PASS. The bivariate formula follows from the exhaustive dichotomy that a nonempty subset is contained in one part or meets at least two parts. In the second case it dominates the whole graph; in the first case its external neighborhood size is determined exactly by the containing part. The ordinary polynomial formula follows from the same support dichotomy. The inverse is triangular: after setting \(Q=(1+x)^N-D\), the top positive degree of \(Q-1\) is one less than the largest non-singleton part, with leading coefficient equal to that part size times its multiplicity. Peeling this contribution recursively is exact. Independent computation verifies both formulas and inverses on all tested types.

## Originality
PASS. The 2017 bivariate-polynomial source supplies the definition, recurrence machinery, the complete-graph case, path and cut reductions, and collision families; full-text search found no complete-multipartite treatment. The 2020 complete-multipartite domination-polynomial source proves unimodality and gives the dependent-set decomposition, but the inspected text does not state restricted-class injectivity or the descending-degree reconstruction. Targeted literature and database searches found no equivalent complete-multipartite rigidity theorem. Residual risk remains for differently phrased or non-indexed work.

## Value
PASS. Polynomial reconstruction is a central structural question because both ordinary and bivariate domination polynomials admit collisions on general graphs. The theorem identifies a broad canonical class on which collisions disappear and gives an explicit inverse, not merely a closed polynomial formula. The ordinary-polynomial reconstruction is stronger than the bivariate statement and extracts the multipartite decomposition from a one-variable counting invariant.

Same-model review: passed. Independent audit: not yet performed.
