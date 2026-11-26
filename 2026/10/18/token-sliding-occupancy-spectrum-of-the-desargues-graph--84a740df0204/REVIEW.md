# Independent mathematical audit

## correctness

PASS

For the repaired finding, the explicit vertex permutation identifies the disjoint-pair host with GP(10,3); the ten spokes are a perfect matching, so no independent state has more than ten tokens. Direct enumeration inspects each subset of each stated size exactly once. Membership of a toggled host-edge mask in the same independent size layer is exactly a legal slide; a second pair-based test independently checks the slide counts. Traversal recovers the whole component partition and all-source BFS gives each component's minimum and maximum eccentricity. The original component census and all original metric entries reproduce. The original metric table described all nontrivial components but omitted occupancies 1–3, and the frozen verifier at lines 161–177 printed rather than asserted the metric values. The repaired table adds (order,radius,diameter) = (20,5,5), (160,5,7), (660,8,9) at k=1,2,3. The replacement checker confirms every census and metric entry and verifies equal metrics across components of each reported order and occupancy. Combinatorially, every slide target for a four-token star touches two star members, so the star stays frozen even with a fifth token. Its allowed fifth-token positions are precisely the six other same-side pairs avoiding the center and four opposite-side pairs containing it; the six vertices are distinct two-valent subdivisions of the six pairs of opposite-side vertices. The two different stars cannot occur in one five-set. Enumeration verifies no additional four-token isolates or ten-state five-token components, and checks the order-four claws at k=7 and 8. Both fresh computations agree, and the corrected checker completed with ALL_CHECKS_OK.

## originality

PASS

The distinct final claim is the exact full component, exceptional geometry and distance census of the independent-set slide graph. The known face counts are only the state counts. A later indexed minimum-independent-domination calculation addresses a restricted induced subgraph of one layer and does not give the full component or metric data. The repaired rows use the same exhaustive scope and proof, not a new priority claim.

## value

PASS

The Desargues graph is a natural cubic bipartite benchmark outside the claw-free setting. Measuring how connectivity is lost over the full occupancy range gives actual barriers and path-length scales for multi-token reconfiguration, not just a static size vector or arbitrary slice. In particular the first isolated star states and their persistence as separate subdivided K4 components provide structural explanations for the first two disconnected layers, and the complete corrected metric table quantifies the distances inside components.

The dated certificate retains the supplied scientific assessment, sources and limitations.
