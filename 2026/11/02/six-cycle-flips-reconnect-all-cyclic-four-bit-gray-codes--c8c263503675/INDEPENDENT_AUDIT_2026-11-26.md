# Independent mathematical audit

## correctness

PASS

The exact state-space and move definitions are respected. Rooting a Hamilton cycle at 0 and selecting the orientation with second vertex smaller than the last counts it once. Membership after XOR with one simple cycle forces alternating removal and insertion at every affected vertex because both endpoints have degree two; checking each Hamiltonian pair for one connected 2-regular symmetric difference is equivalent. The frozen Python and C++ sources were inspected, not executed. An independent exhaustive replay enumerated all 272 perfect matchings by pairing the least free vertex, then counted connected unions of disjoint matching pairs; each Hamilton cycle has exactly two alternating matchings, giving a unique unordered pair. It scanned unordered state pairs for the specified differences and ran full BFS for the metric. Replay: python3 /workspace/branches/5cb0dcc0-3db2-418e-aad3-5679b2cc8bd4/reproduce.py; saved reproduction.txt in that directory. Results: 1344 Hamilton cycles; 1920 square edges with 240 singleton components and one of size 1104; 9408 hexagon-only edges and 11328 combined edges, each connected and with 432 eccentricities 5 and 912 eccentricities 6. Bipartiteness and simplicity preclude a shorter simple cycle than four, and square-only disconnection shows six is the least allowed sufficient length (including if all shorter moves are allowed). This proves the statement only on the fixed four-cube.

## originality

PASS

The accepted distinct contribution is the hexagon-only and combined Hamilton-cycle reachability and exact metric, including the sharp six-move diameter. The scalar cycle count, square-switch move, and existence of square-isolated cases are already known. A separate indexed record gives the precise square-only census as well. Neither that record nor the inspected matching and grid reconfiguration literature gives or implies the hexagon/mixed Hamilton-cycle claims. No claim of historical priority is made for the square-only data.

## value

PASS

Square switches are a natural Gray-code generation move with an established obstruction from isolated configurations. The next possible local exchange length is six, so finding that hexagon moves alone reconnect all labeled states resolves a motivated obstruction in this small benchmark, not an arbitrary slice. The exact worst-case of six moves and the fact that admitting squares does not improve any eccentricity (pointwise monotonicity plus the identical distributions) distinguish the two permitted move sets in a way connectivity alone could not. The result is useful at this fixed cube and does not assert a higher-dimensional theorem or mixing bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
