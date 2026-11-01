# Scientific review

## Correctness — PASS
The canonical restricted-growth representation is unique up to permutation of the ternary alphabet. Admissibility is prefix-closed, and adding one digit changes only adjacent intervals ending at that digit; testing those intervals exhausts the next level. Two independent integer-arithmetic LCS methods agree on every level cardinality through length \(33\). Ten weak length-\(32\) representatives have exactly thirty terminal extensions, all supplied with a violating split. A length-\(32\) witness has minimum strict integer margin \(1\), proving attainability for every shorter length by prefix inheritance. The computational check is exact and its scope is finite; the reduction makes the no-longer-words consequence rigorous.

## Originality — PASS
Xu et al., arXiv:2609.04122, establish ternary existence for parameters exceeding \(226/227\), while explicitly leaving the optimal parameter open. Camungol and Rampersad, arXiv:1308.1620, test only equal-length adjacent blocks and report a lower similarity threshold near \(0.888\), not an all-adjacent \(9/10\) obstruction. Full-text, mathematical-record and historical-claim comparison found no dominating result or equivalent finite cutoff. A possibly unindexed older finite computation remains a genuine priority risk.

## Value — PASS
This is a sharp, interpretable finite boundary for a natural quantitative synchronization parameter, together with the consequent necessary lower bound \(\varepsilon>9/10\) for unbounded ternary index strings. It addresses a current open optimization question without pretending to settle its still-large constructive gap. Finite computation is valuable here because prefix inheritance converts it into a universal obstruction.

## Limitations
The optimum feasible parameter above \(9/10\) is not determined. The programs are independent implementations, not an independent external mathematical audit. The theorem does not claim the analogous cutoff for other alphabets or other parameters.

Self-review: passed. Independent audit: not yet performed.
