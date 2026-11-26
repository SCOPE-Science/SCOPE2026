# Independent mathematical audit

## correctness

PASS

Exhaustively reconstructed the matching state set independently: combine each partial matching of the ten outer edges with every partial matching of the ten inner edges covering exactly the same labels modulo 10, and fill all remaining labels with spokes. This gives exactly and uniquely all 36 matchings. Enumerated simple cycles by starting at their least vertex and taking one orientation. The 12 pentagons give a spherical embedding: every edge occurs twice, each vertex link is a triangle, and the connected complex has Euler characteristic 2. There are zero 4- and 6-cycles and exactly 30 octagons, equal to the boundaries of the 30 edge-sharing face pairs. Each octagon alternates at exactly eight matchings and toggles to another enumerated matching. Verified all 120 undirected edges, the exact complementary-factor and distance layers at every state, both exceptional incidence multiplicities, independence and all six induced C10 links. Every state has eccentricity 3. The canonical arrays agree entrywise with states_edges.json, and the digest is a70573c1719c0680ca78fc3919e5fc78b77a442c557fc17916c5968f7b23790c. Replay with python3 -B /workspace/branches/dodecahedron-independent.py <frozen-record-directory>/states_edges.json. Inspected both reference programs and their recorded outputs without executing uploaded code. The conclusion is exhaustive only for GP(10,2).

## originality

PASS

The supported distinct claim is the full octagon-only graph, including how the six exceptional states attach and alter its distances, not the perfect matching count or an assertion of novelty for the Hamiltonian sector in isolation.

## value

PASS

The first nonvacuous even-length flip is a motivated local move on the dodecahedron, unlike unrestricted switches whose connectivity follows directly from the symmetric-difference decomposition. The full restricted graph answers whether these moves suffice and gives sharp routing distances and exceptional attachment structure not determined by the matching or Hamiltonian counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
