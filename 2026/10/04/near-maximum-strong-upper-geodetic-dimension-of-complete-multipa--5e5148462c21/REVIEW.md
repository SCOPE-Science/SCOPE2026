# Review of Near-maximum strong upper geodetic dimension of complete multipartite graphs

## Correctness
PASS. In a complete multipartite graph, only selected endpoints from the same part can produce a shortest path with an internal vertex, and one fixed geodesic can cover only one omitted vertex. For a size-\(N-1\) candidate, minimality is therefore decided by every possible second deletion. Splitting according to whether the first omitted vertex lies in a singleton or a non-singleton part yields exactly the four stated families. The counting formulas follow from the admissible omitted vertices. A definition-level matching checker exhaustively agrees on all complete multipartite types through order ten.

## Originality
PASS. The 2021 defining paper treats the strong upper geodetic parameter generally and has no complete-multipartite occurrence in its full text. The 2018/2019 complete-multipartite strong-geodetic paper studies the minimum strong geodetic number rather than the maximum size of a minimal set. A prior exact complete-bipartite strong-upper result covers the \(K_{1,m}\) and \(K_{2,m}\) slices, so those slices are explicitly not claimed as new individually. The surviving statement is the arbitrary multipartite near-maximum classification, including the extra \(K_{2,1^t}\) and \(K_{2,2,1^t}\) families and the sharp exclusion of every other multipartite type from value \(N-1\).

## Value
PASS. The strong upper geodetic number was introduced specifically to study extremal minimal strong-geodetic sets and is NP-complete in general. Determining when it is within one of the graph order is a natural structural boundary problem. The theorem completely resolves that boundary on the canonical complete multipartite class and identifies exactly how singleton parts change the bipartite picture, while also enumerating every maximum set at the threshold.

Same-model review: passed. Independent audit: not yet performed.
