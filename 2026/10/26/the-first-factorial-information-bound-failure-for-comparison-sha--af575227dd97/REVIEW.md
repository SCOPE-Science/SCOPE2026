# Independent mathematical audit

## correctness

PASS

Each binary response path constrains the candidate permutations to the linear extensions of the comparisons' transitive closure. A depth-d tree has 2^d mutually disjoint, nonempty leaf classes, and each feasible root split must leave two depth-(d−1) classes. I independently decoded every stored certificate by response-path bits, using direct position comparisons in the lexicographic permutations (not the supplied split code). The numbers of checked leaves were 1,2,4,16,64,512,2048 and all were distinct within each tree. To exclude depth 12, it suffices by relabeling to test depth 11 for one oriented first response. I exhaustively split tuples of ranks in the 2520-permutation half-class, allowing every unordered comparison and pruning only if either child lacked 2^(d−1) permutations; depth 11 failed (766 memoized states). Thus the profile is (0,1,2,4,6,9,11), strictly below the factorial leaf bound first at seven labels. For VC shattering every graph orientation must extend to a total order, equivalent to having no undirected cycle; a forest on n vertices has at most n−1 edges and spanning trees attain this. Replay: python3 /workspace/review-replay.py 5 with the frozen comparison_certificates.json path. Only the VC identity is all-n.

## originality

PASS

The model and linear-extension bookkeeping are established, with closer prior art than the frozen bibliography: Goldman–Rivest–Schapire studied adversarial comparison mistakes on total orders in 1993, and Feng et al. treat the same one-pair case within a broader feedback model. Neither inspected treatment derives the exact seven-label deficit or its minimality. Two later-listed catalogue entries explicitly cover the seven-label result, and one covers the whole profile. These are real overlaps, not evidence of an earlier source for the frozen record or of any particular provenance. This pass is limited to the exact finite result, not the model, cardinality argument, or an absolute priority claim.

## value

PASS

The first non-tight cardinality upper bound is the motivated stopping criterion, not a selected example size. The positive trees and exhaustive seven-label exclusion locate the first time the constraints of realizable comparisons reduce the optimal mistake bound below what a count of concepts suggests. This is useful for the comparison model independently of the accompanying VC observation and is not a claim about optimal sorting comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
