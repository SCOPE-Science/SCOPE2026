# Review of Minimum quasi-total Roman functions of connected chain graphs

## Correctness
PASS. Published prior work fixes the minimum at \(4\) when both bipartition classes have order at least \(2\). At weight \(4\), the only positive-label multisets are \(\{2,2\}\), \(\{2,1,1\}\), and \(\{1,1,1,1\}\). The first forces one universal label-\(2\) vertex in each part. The second forces the label-\(2\) vertex's part to have order exactly \(2\), forces that defender to be universal, and leaves one arbitrary positive support vertex in the opposite part. The third forces the graph to have four vertices. These cases are disjoint and exhaustive, and their converses are immediate. Exhaustive definition-level checking of \(114\) canonical chain-graph types through order \(8\) matches the classification and count.

## Originality
PASS. The 2019 introducing paper develops general quasi-total Roman theory but does not treat chain graphs. The 2021/2022 algorithmic chain-graph paper was inspected in full at its chain section: Theorem 7 gives only the scalar minimum and Theorem 8 a linear-time optimization algorithm. It does not classify or count all optimum functions. The prior complete-multipartite all-function theorem concerns a different graph class and does not imply the nested-neighborhood chain result. Targeted chain/Ferrers/half-graph searches did not locate the optimizer formula. The scalar value is explicitly excluded from the originality claim.

## Value
PASS. The optimizer multiplicity of a chain graph collapses to four structural families and depends only on the two side sizes and the sizes of the universal twin classes. This gives, for example, a unique optimum on every half graph of order at least six while complete four-vertex bipartite graphs have thirteen. The classification also identifies the universally valid weight-four construction behind the published scalar theorem and exposes why the endpoint displayed in that proof is not valid for every chain ordering.

Self-review: passed. Independent audit: not yet performed.
