# Self-review

## Correctness — PASS

The proof identifies the exact hypothesis family, handles height zero in the induction and all positive branching degrees, and proves both directions of VC and online dimension. The essential argument is a one-sided online-rank upper bound: conditioning on a positive vertex query leaves a product of independently chosen sibling-subtree frontiers, whose online ranks add. The resulting sum telescopes to one less than the number of penultimate vertices. No computational check is used to infer the infinite-parameter theorem. The finite verifier independently recomputes version-space depth and, on small examples, every shattering projection.

## Originality — PASS under accessible comparisons

Bhaskar (2017) and Walker (2022) define the underlying adaptive notions and prove general shatter bounds, without calculating the exact dimensions of the class of all maximal prefix-code antichains of complete level-regular trees. Darnstädt, Ries and Simon (2017 preprint/2018 journal) use precisely such maximal antichains to encode hierarchical partitions and prove weighted-optimization recursions, but their inspected sections do not derive the stated VC or Littlestone formula. Ghazi et al. (2020), Sections 2--3, prove general aggregation bounds, with no exact complete-frontier formula in the inspected full HTML text. Published research record and accessible prior-claim comparisons did not locate an equivalent or stronger statement; this is not a proof of absolute novelty.

## Mathematical value — PASS

Complete prefix-code frontiers are a standard, non-arbitrary family of hierarchical partitions. The exact dimensions apply to infinitely many depths and all positive branching profiles, establish an optimal online mistake budget, and prove an unbounded, quantitatively controlled slack in the naive logarithmic hypothesis-count bound. This is not an arbitrary small-case table, and it contrasts sharply with related classes of all rooted-tree ideals. The result remains limited to level-regular trees and ordinary vertex-membership queries.

Self-review: passed. Independent audit: not yet performed.
