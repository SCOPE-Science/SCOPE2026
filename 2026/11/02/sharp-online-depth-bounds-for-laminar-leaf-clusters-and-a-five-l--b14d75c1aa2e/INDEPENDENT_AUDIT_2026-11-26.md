# Independent mathematical audit

## correctness

PASS

The frozen formulas are mathematically correct: a positive answer leaves at most H chain members, all ancestor thresholds are accessible by leaves in consecutive differences, and an opposite complete root-child subtree gives the required negative depth by induction. For the repaired finite claim, a leaf query can start depth three exactly when it has at least four ancestor clusters and misses a nonsingleton cluster. Indeed the positive chain needs four members and can then be bisected twice, while the negative branch either shatters a pair with the empty set and its two singletons or has only singleton and empty hypotheses. Hence a witnessing leaf has depth at least three with an off-path internal subtree, requiring at least five leaves. At equality its three off-path subtrees are two singletons and one cherry, giving exactly the three binary shapes. The root partition count 5+2+2+1+1+1 gives all twelve shapes. Ten hypotheses cannot support depth four. All pairs are statically shattered and laminarity forbids any triple.

## originality

PASS

The frozen originality claim fails as framed for its regular-tree centerpiece: the earlier descendant-cone record gives the same height law for regular trees at heights at least two, with a proof that directly adapts to leaf queries. The numerical shape counts themselves are independently known. The actual repair withdraws the height theorem as a contribution, credits it and the shape counts, and claims the first leaf-number threshold and its shape-by-shape adaptive rank classification. The compared height law gives only a range for irregular trees and does not control the negative branch required for that classification. No inspected claim supplies this retained result.

## value

PASS

The repaired theorem identifies the first hierarchy size at which adaptive membership learning is strictly harder than fixed-support shattering, and specifies exactly which geometries give the gap at the minimum size. The path-plus-off-path-cluster condition explains why a long positive chain by itself is not enough. This is a motivated exact boundary, not a recomputation of the twelve shapes or a relabeling of the earlier regular-tree height bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
