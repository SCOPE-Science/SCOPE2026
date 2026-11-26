# Independent mathematical audit

## correctness

PASS

Re-audit of the complete corrected RESULT.md in repairs/4: the theorem is unchanged. The frozen proof incorrectly claimed that with bridge triangle {x,y,z}, y in T and z outside T, the two y-layer special triples had Johnson distance at least two. For n=7, x=1, S={2,3,4}, T={5,6,7}, y=5, z=2, the bridge-side {1,2,6} and goal-side {1,6,7} are at distance one. The corrected proof requires only distance at least one: disjoint mandatory pairs {x,z} and T minus {y} cannot fit together in one triple. Since the x-side also needs to insert y into S, at least two Johnson moves in total are still necessary. If z lies in T, both y and z must be inserted on the x-side. Any path of length at most four to A(T) needs a two-edge change of center to a center in T plus its final edge; it can therefore use at most one Johnson move, a contradiction. Between disjoint triangles at most four steps would either use a single common center or an intermediate triangle sharing two elements with each endpoint, both impossible. For the upper bound within a center use Johnson distance at most three; between centers insert one desired center into the starting special triple, bridge through the triangle formed with a retained point, then choose a special triple meeting the target so at most two Johnson moves remain. The triangle-to-triangle and mixed routes give at most five using the exact adjacency rules. Inclusion–exclusion on pairs in a fixed center layer gives the stated same-center and mixed overlaps; direct bounds for distinct centers and triangle pairs are all strict below 2n-4. The equality types from Hilton–Milner exhaust the vertices even at n=7; the two equality overlap cases give degree 3(n-3), and label count plus handshaking give both totals. Independently replayed n=7 from the defining triple families in branches/1f1f1d1b-ae1a-4c4b-89bf-5cf3ec32458b/n7_hilton_milner_exchange_check.py and its .out: minimum exchange 3, 175 vertices, 630 fixed-center edges, 420 mixed edges, no other edges, and all 175 eccentricities 5. This finite replay does not replace the corrected all-n path and overlap proof. Frozen evidence was preserved.

## originality

PASS

The repaired proof leaves the same exchange-graph finding. The classical extremal classification and triangle examples are not new; the exact batch threshold, adjacency and all-vertex eccentricities of the restricted optimum graph remain distinct from the compared results.

## value

PASS

The quantitative contrast is substantive: every nontrivial optimal state is isolated until exchanges grow linearly in n, yet the first admissible graph is regular and every vertex has maximum distance exactly five. The Johnson-layer and triangle-incidence rules explain this jump and give explicit transformations, beyond the classification of isolated extremizers. The repaired proof preserves this interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
