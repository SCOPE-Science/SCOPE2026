# Same-model review

## Correctness

**PASS.** The tournament orientation is valid because each opposite off-diagonal pair contains at least one zero. A transitive subtournament of order \(r+1\) produces a triangular principal submatrix with nonzero diagonal, so the standard transitive-tournament induction gives the universal bound \(n\le2^r-1\).

For the rank-three equality case, the absence of a transitive four forces every vertex of a seven-vertex tournament to have indegree and outdegree three, with both neighborhoods directed 3-cycles. The common-outneighbor calculation then makes the seven in-neighborhood triples a Steiner triple system on seven points. Factoring a rank-at-most-three matrix through \(\mathbb F^3\) turns the selected zero incidences into seven distinct projective points and seven distinct projective lines carrying the Fano triples. The explicit coordinate normalization reduces the last Fano line to determinant \(-2\), proving that order seven requires characteristic two.

The lower constructions were checked independently from the symbolic upper-bound proof. The order-six integer matrix has a rank-three factorization and a unit \(3\times3\) minor, so it has rank exactly three over every field. The order-seven binary matrix factors through dimension three in characteristic two, has a nonzero \(3\times3\) minor, and satisfies every fooling-set product condition. The compact verification artifact reproduces these checks exactly.

## Originality

**PASS, to the best of our knowledge.** The closest classical result is the universal \(n\le r^2\) inequality of Dietzfelbinger--Hromkovič--Schnitger. Klauck--de Wolf supply the size-six rank-three construction, and Friesen--Hamed--Lee--Theis provide the known characteristic-zero and positive-characteristic construction families, including size seven at rank three in characteristic two. The located literature does not state the matching rank-three upper bound, the exclusion of size seven outside characteristic two, or the tournament-to-Fano equality mechanism.

Searches also covered the synonymous language of cross-free matchings and isolation sets and the neighboring small-real-rank literature. Parnas--Shraibman determine isolation sets for 0/1 matrices constrained to have small ordinary real rank; that does not imply the present weighted arbitrary-field extremal statement. The residual risk is terminological: a short version of the rank-three obstruction could exist in older sign-pattern, minimum-rank, projective-incidence, or tournament literature without being indexed as a fooling-set result.

## Value

**PASS.** The theorem closes the first nontrivial low-rank case of the classical fooling-set-versus-rank extremal problem and shows an exact field-characteristic split already at rank three. It simultaneously proves optimality of two previously known constructions in their respective characteristic regimes and identifies the Fano plane as the equality structure behind the exceptional characteristic-two case. The general tournament bound gives a concise structural explanation for the seven-point threshold.

## Scientific limitations

The theorem does not determine \(f_{\mathbb F}(r)\) for \(r\ge4\), classify all extremal matrices, or improve the asymptotic \(r^2\) theory. Bibliographic originality remains to the best of our knowledge.

**Same-model review: passed. Independent audit: not yet performed.**
