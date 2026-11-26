# Independent mathematical audit

## correctness

PASS

The graph is cubic, so at least five closed neighborhoods are needed, and a perfect matching forces even cardinality and balance between the two sides. Each proposed point-column and line-slope pair dominates and induces three disjoint edges. I independently enumerated disjoint subsets of edges of the original 27-edge graph, took their endpoints and tested closed-neighborhood coverage, deduplicating the endpoint sets. This domain is exhaustive because every feasible set of size k has a k/2-edge perfect matching in the original graph. It confirms exactly the nine stated cores at size six and 216 size-eight states with unique contained cores. The direct/crossed alternatives in RESULT.md are exhaustive: if the two new vertices do not match each other, each has only one incident partner in the core, and those two core vertices must have been partners. At c=m=0 the excluded edges satisfy b=y+ux; the displayed walk has all twelve distinct vertices before closing, and the forbidden graph has degree two. A jump cannot change the full triple on either side; after a change at most five distinct vertices could occur in the union on that side, not the six needed for two disjoint triples. Within a core a jump is exactly an edge adjacency in the extension graph's line graph. The four-neighbors-in-six property gives paths of length at most three; both crossed incidences of the displayed pair of edges are forbidden, so the diameter is exactly three. Independent enumeration also verified all 9 forbidden cycles and all component sizes (24), edge counts (72), degree (6), diameters (3), and the edgeless minimum layer.

## originality

PASS

The supported distinct claim is the full structural classification of the size-eight token-jump paired-domination layer and its relation to the frozen minimum cores. None of the inspected closest statements provides it or implies it. This does not certify priority for a standalone minimum-number computation or for the underlying graph model.

## value

PASS

The first feasible augmentation of minimum paired domination is a motivated finite layer on a canonical cubic bipartite incidence graph. Its nine recoverable cores explain a sharp mobility/connectivity split: 216 states are locally mobile but confined to nine sectors, each with an exact line-graph structure and diameter. This goes beyond an arbitrary finite count and gives concrete reachability information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
