# Scientific review: uniform-incidence closed neighborhoods

## Correctness

PASS. The concept class is explicitly the closed neighborhoods of the bipartite incidence graph joining points to all uniform blocks, with \(2\le k<n\). Point-centered neighborhoods contain one point vertex; block-centered neighborhoods contain one block vertex. The argument partitions all possible shattered supports into point-only, block-only and mixed types, proves the universal size bound \(\min\{k,n-k+2\}\), and constructs every point-only support at the upper bound. The non-singleton incidence signatures give strict exclusion of nonpoint maximum supports at dimension at least four. A complete support-type census proves all exceptional maximum-support formulas in dimensions two and three. The online rank-two proof gives a depth-three tree and excludes depth four by analyzing every possible first-query vertex type. The extracted standard-library checker validates the stated finite ranges, including all 256,813 maximum-size candidates tested and 36,582 triple candidates.

## Originality

PASS, with historical-priority limits. Adler, Benediktsson and Macpherson, arXiv:2007.16042, study open-neighborhood VC dimension and density on Johnson/Hamming graphs, not the full closed-neighborhood profile for point-to-uniform-block incidence graphs. Their Corollary 4.4 already recognizes the rank-two incidence graph as an induced subgraph of a Hamming graph's open distance-two neighborhood; that pre-existing graph identification is credited and is not a novelty claim. Axenovich and Zimmermann, arXiv:2401.11296, explicitly use the same complete-uniform incidence graph under the hedgehog notation \(H(n,k,1)\), but prove induced Turán and one-sided bipartite VC results rather than the present closed-neighborhood theorem. Comparisons with accessible previous research titles and published research searches did not identify a statement implying the exact maximum-support census. A previously published equivalent result under different graph-learning or hypergraph-incidence terminology remains possible; independent bibliographic confirmation is absent.

## Mathematical value

PASS. The exact rank/corank threshold and **every** maximum-support count solve a natural extremal question across all nondegenerate uniform hypergraph incidence graphs. The result isolates the mechanism by which including the neighborhood center can increase VC dimension by two, and exhibits a distinct adaptive/static separation on the subdivision of complete graphs. The structural statement that all maximum supports are point-only in dimensions at least four has potential reuse in support enumeration and model-theoretic trace counting. This goes beyond restating the generic VC dimension of a uniform set system.

## Limits

The theorem does not cover the degenerate ranks, does not enumerate lower-cardinality supports in arbitrary rank, and does not claim an all-rank Littlestone formula. The finite script is corroboration, not a proof of the infinite-family claims. Bibliographic uniqueness and independent mathematical validity remain unverified.

Self-review: passed. Independent audit: not yet performed.
