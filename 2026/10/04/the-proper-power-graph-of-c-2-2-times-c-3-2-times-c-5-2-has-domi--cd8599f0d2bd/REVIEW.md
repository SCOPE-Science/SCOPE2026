# Review

## Correctness

PASS. The cyclic-subgroup reduction is exact: nontrivial cyclic subgroups are precisely nonempty partial choices of one line in coordinate sets of sizes \(3,4,6\), giving \(139\) types. Power-graph adjacency becomes inclusion comparability. The size-\(11\) dominating set is proved directly, and the standalone verifier exhaustively proves that no size-\(10\) family dominates the complete reduced graph.

Risk: the lower-bound certificate is computational. The computation is finite, exhaustive, independently replayable from source, and uses only logically safe coverage pruning.

## Originality

PASS. The closest published domination paper supplies the upper bound and states exact determination for nilpotent groups with at most two prime divisors. The present group has three. Searches by exact group, order, value, subgroup counts, and equivalent power-graph language did not locate the matching lower bound or equality. The closest comparison records concern different group-graph invariants or unrelated domination variants.

Risk: an unindexed article, thesis, note, or unpublished calculation may contain the same finite special case.

## Value

PASS. This is the smallest possible nilpotent group with three distinct prime divisors and all Sylow subgroups noncyclic, so it is a natural first test case beyond the published exact two-prime regime. The equality \(11\) shows that the general nilpotent upper bound is sharp in a genuine three-prime example.

Risk: this is one boundary case, not a classification of the three-prime regime.

Same-model review: passed. Independent audit: not yet performed.
