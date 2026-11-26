# Independent mathematical audit

## correctness

PASS

Reconstructed Petersen independently as KG(5,2) and verified the explicit outer-cycle, spoke and pentagram identification with P(5,2). A white set fails exactly when it contains a nonempty fort: no first force into a fort can occur, and the nonempty remaining white set at a stalled closure is itself a fort. Exhausting all 1024 white sets by this test gives coefficients 132, 190, 120, 45, 10, 1 in degrees 5 through 10 and zero below. The 252 five-sets have type census C5:12, P5:60, P4 plus isolate:60, fork:60, P3 plus two isolates:30, and two edges plus isolate:30. These six degree sequences identify the types in this girth-five graph; each member of the first three types and no member of the last three passes the fort test. Replay: python3 /workspace/branches/independent_exact_checks.py, check_petersen(). The packaged closure checker and stored output were inspected, not executed. This is exhaustive only for the stated ten-vertex graph.

## originality

PASS

The supported distinct claim is the full Petersen census together with the induced-type partition of all minimum forcing sets. The scalar minimum, an outer C5 witness, and generic top coefficients are established prior coverage, not original components. The checked sources do not give or imply the remaining census and classification without additional graph-specific analysis.

## value

PASS

Petersen is a canonical small regular test graph for ordinary forcing and propagation time. The exact enumerator gives fixed-cardinality forcing probabilities as a reference for comparisons. More substantively, the minimum-family classification distinguishes cycle, connected path and disconnected configurations and rules out the same-size fork and other shapes; it answers which minimum seeds work, not just the previously known size or a count obtained from a single witness. The scope is a benchmark and exact structural classification for one natural graph, not a family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
