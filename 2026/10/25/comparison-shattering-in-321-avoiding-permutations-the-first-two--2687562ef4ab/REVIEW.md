# Scientific review

## Correctness — PASS

The domain is the set of unordered pairs of *positions*, queried as smaller-entry comparisons. The VC upper bound is forced by an impossible directed cycle on any cyclic set of comparisons; the explicit first-position pivot construction shatters an \(n-1\)-edge star and always avoids 321. The finite adaptive classification is supported by two independently implemented exhaustive dynamic recurrences with different avoider enumerations. The complete depth-nine tree has all 512 leaves explicitly witnessed and separately checked. Direct sums preserve 321-avoidance and independently concatenate block shattering strategies. This proves the unbounded lower gap without any extrapolation of the finite table.

## Originality — PASS, with residual priority risk

The inspected primary work on 321-avoiders develops Catalan/Dyck/RSK bijections and rowmotion [1], without comparison-query dimension statements. The general zero-set theorem [2] assumes a linear-algebraic concept representation absent here. The generic dimension-complexity study [3] does not compute these pattern-restricted exact values. Public research-record searches for thicket/Littlestone dimensions, Catalan permutations, 321 avoidance, comparison queries, and direct sums did not return an implication covering the claim. Previously accessible total-order comparison results concern the full permutation class and therefore do not determine the dimension of the restricted 321-avoiding subfamily. Absence from searched sources is not a proof of absolute priority.

## Mathematical value — PASS

The same canonical class exhibits two qualitatively distinct measures of query complexity: VC dimension is fixed by a forest obstruction, while adaptive shattering can exceed it already at six positions and by two at eight. The explicit eight-position witness then supplies a linear lower gap in the full connected-by-pattern permutation family, not an arbitrary union of unrelated learning problems. The mechanism is reusable for studying online inference on other hereditary permutation classes. The finite transition and the asymptotic amplification are distinct substantive pieces of one theorem.

## Closest literature and limitations

[1] B. Adenbaum and S. Elizalde, *Rowmotion on 321-avoiding permutations*, arXiv:2212.11347 (2022).

[2] V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (2021).

[3] P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443 (2022).

The classification of adaptive ranks is exact only through eight positions. Larger-size Littlestone ranks are bounded below on multiples of eight, not calculated exactly. Further unindexed or unpublished overlap is possible.

Self-review: passed. Independent audit: not yet performed.
