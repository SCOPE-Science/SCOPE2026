# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**Assessment: passed.**

The necessity and sufficiency arguments were checked separately.

For necessity, an independent triple in any interval-sandwich representation has disjoint extreme intervals when ordered by centre: the middle centre cannot lie in either extreme interval. In a hypothetical interval-sandwich representation of K_{3,3}, every interval on one side must intersect the two extreme intervals on the other side and therefore must contain the separating middle centre. This forces a common point in an independent triple, contradicting the same extreme-interval observation. Heredity then excludes every complete multipartite graph with two parts of size at least three.

For sufficiency, the stated explicit radii and centres were checked against the exact same-colour adjacency criterion |c_u-c_v| <= max(r_u,r_v). Within the distinguished part, centre gaps are at least 2 while radii are 1. Within the k-th two-vertex part, the centre gap is exactly one larger than its common radius. Across the distinguished part and a two-vertex part, the latter radius covers all distinguished centres. Across two doubleton parts j<k, the larger radius R_k=D+2k-1 dominates both same-side gaps and the cross-side gap D+j+k because j<=k-1. Singleton intervals contain every constructed centre. These checks establish exactly the required complete multipartite adjacency pattern.

The equivalence with induced K_{3,3}-freeness follows because an independent set of size three in a complete multipartite graph lies inside a single part.

No empirical computation is needed for the theorem.

## Originality

**Assessment: passed, to the best of our knowledge, with stated residual risk.**

The closest source found is Basit--Suter--Zhang, arXiv:2609.12293 (2026), which introduces the two graph classes and whose abstract explicitly states that complete bipartite graphs are determined for both classes. Searches were made for the exact and synonymous combinations of bicoloured-interval / bicolored-interval, interval-sandwich, complete multipartite, K_{n_1,...,n_r}, centre-containment / center-containment, central interval catch, and max-point-tolerance terminology. No source was found stating the complete multipartite equivalence or the monochromatic shell construction.

Older literature on central interval catch digraphs and central max-point tolerance graphs was also checked at the title/abstract/search-result level because a monochromatic bicoloured-interval representation is naturally adjacent to those notions. No matching complete-multipartite classification was located.

### Access limitation and residual risk

The arXiv abstract of Basit--Suter--Zhang was inspected, but the full theorem text of that 40-page preprint was not inspected. Therefore an internal remark or corollary in that very recent preprint could in principle overlap with the present extension even though the abstract advertises only complete bipartite graphs. This is the strongest identified originality risk. The 2022 interval-catch paper abstract was accessible, but no source found in the search stated the present undirected complete-multipartite theorem.

No inaccessible source provided concrete evidence that the theorem was already known.

## Value

**Assessment: passed.**

The result gives an exact characterization on a classical dense graph family immediately adjacent to a class explicitly treated in the introducing paper. It also identifies a sharp structural collapse that is not visible from the definitions: on complete multipartite graphs the bicoloured-interval and interval-sandwich classes coincide, and the positive cases need no second colour at all. The obstruction is reduced to a single induced graph, K_{3,3}, and the positive direction is constructive with integer coordinates of linear magnitude.

## Scope

The result does not claim a forbidden-subgraph characterization for either class beyond complete multipartite graphs, nor does it claim that K_{3,3} is the only obstruction in general.
