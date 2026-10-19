# Scientific review

## Correctness — PASS
For each pair of integers \(q\ge2,r\ge1\), the exact recursive identity \(W_{j+1}=W_j0^{rq^j}W_j\) both produces and locates the proposed factors. The longest zero run internal to \(W_j\) is \(rq^{j-1}\) when \(j\ge1\); hence \(0^{rq^j}W_j\) is smaller than every nonempty proper suffix. The leading zero runs increase strictly, so the Lyndon factors decrease strictly. Finite factorization uniqueness proves completeness, and the recurrence for factor starts gives the closed forms and generating function, including the repeated-root case \(q=2\). The attached direct substitution/Duval checker independently corroborates finite test instances; it is not the infinite proof.

## Originality — PASS against inspected sources, with residual risk
The most pertinent comparison is the full paper by Goč, Saari, and Shallit (arXiv:1207.5124, 2012), which supplies general algorithmic properties of Lyndon factors in automatic sequences, but not the present exact family of Lyndon blocks, its recurrence, or critical-scale generating function. Lü, Chen, Guo, and Wen (doi:10.1016/j.tcs.2015.12.022; first online 2015) study ordinary/permutation complexity in the uniform Cantor subfamily, not its Lyndon decomposition. Published period-doubling factorization concerns a different substitution. The specific structural statements do not follow as stated from the compared theorems without additional analysis. Direct relevant title, alias, and parameter searches identified no equivalent result; this is **not** proof that no unindexed treatment exists.

## Mathematical value — PASS
A natural two-parameter family of recursive binary words receives an exact decomposition into all Lyndon blocks at every substitution depth, with **no unspecified factors**, plus an explicit boundary generating function. The transition between \(q=2\) (double characteristic root and \(j2^j\) scale) and \(q>2\) (\(q^j\) scale) is a nontrivial structural consequence, and the familiar generalized Cantor words fall out as an exact special case. The claim is narrower than a classification of arbitrary morphic words and does not concern intermediate prefix decompositions.

## Residual limitations
Potential equivalent results for sparsely supported substitutions in inaccessible or differently indexed publications remain a risk. A generic factorization algorithm can compute individual examples but does not, by itself, assert the present all-parameter closed formula. Numerical verification is finite; the induction is the decisive argument.

Self-review: passed. Independent audit: not yet performed.
