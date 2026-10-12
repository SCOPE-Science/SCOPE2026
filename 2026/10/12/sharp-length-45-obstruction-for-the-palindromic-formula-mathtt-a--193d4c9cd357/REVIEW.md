# Self-review

## Correctness
PASS. The restricted language is factorial, so exhaustive prefix extension is complete. One exact engine uses suffix-only checks for newly created squares and restricted formula occurrences; a second engine independently rescans each candidate for every square factor and all \(3834\) allowed morphisms. The engines agree at every length through \(46\), with exactly \(18\) words at length \(45\) and none at length \(46\). The boundary words are directly rechecked and split into two symmetry orbits of sizes \(6\) and \(12\).

## Originality
PASS. The primary 2019 source states only that the restricted square-free language has no infinite word. It does not state a finite maximum, extremizer count, or symmetry classification. The 2021 follow-up cites \(\mathtt{ABCA.ACBA}\) as the known index-\(4\) palindrome example and proves a different strengthened formula, without giving the cutoff \(45\). Alias, exact-string, broader-coverage, and implication searches found no covering publication.

A residual risk is that unpublished source-author search output or an unindexed auxiliary file contains the same boundary data.

## Value
PASS. The restriction is the explicit finite search certificate used in a published avoidability-index proof, not an arbitrary parameter slice. Giving the sharp cutoff and all equality cases makes that finite obstruction exact and independently reproducible.

Self-review: passed. Independent audit: not yet performed.
