# Review of Self- and solid-location-domination of half graphs

## Correctness
PASS. Strict nesting of same-side neighborhoods means two omitted vertices from the same side would have comparable identifying sets, which is forbidden for a solid-locating-dominating code. Hence at least \(2n-2\) codewords are required. Omitting one vertex per side works for solid location-domination exactly away from the two leaf corners, giving the complete \(n^2-2\) optimum family. Self-location-domination is stronger. The forced-codeword characterization forces every \(a_i\) with \(i\ge2\) and every \(b_j\) with \(j\le n-1\), leaving only \(a_1,b_n\) omittable. Their identifying-set neighborhood intersections are exactly the omitted singleton vertices when \(n\ge3\), proving existence and uniqueness. Exhaustive evaluation of all \(87{,}376\) vertex subsets for \(2\le n\le8\) agrees with the theorem and the stated boundary.

## Originality
PASS. The 2018 introducing paper was inspected at the definitions and its stated exact-family sections; it studies rook graphs and binary Hamming spaces. The open 2018 follow-up was inspected at the structural characterizations, forced-codeword theorem, tree results, and Cartesian-product scope; targeted full-text searches found no half-graph or chain-graph occurrence. Semantic published-result searches under both code names with half-graph and chain-graph aliases returned no equivalent theorem. The closest indexed same-invariant result concerns complete multipartite graphs, while the closest chain-graph results use different locating-code notions. Neither implies the nested half-graph optimum classification.

## Value
PASS. Half graphs are canonical twin-free chain graphs whose strictly nested neighborhoods make them a natural test family for stronger locating codes. The result exposes a structural contrast invisible at the scalar level: both parameters equal \(2n-2\), yet self-location-domination has a unique optimum while solid location-domination has \(n^2-2\) optima. This connects the antichain requirement for solid codes with the forced-codeword mechanism for self-locating codes.

Self-review: passed. Independent audit: not yet performed.
