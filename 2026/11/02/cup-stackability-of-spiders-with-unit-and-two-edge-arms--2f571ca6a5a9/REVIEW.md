# Scientific review

## Correctness — PASS
The obstruction is a proved occupancy bottleneck: the center cannot be repopulated after it empties, and accepting two short-leaf cups freezes it with three cups at eccentricity two. Since a short leaf at distance two from the selected inner target cannot clear a stack of three cups, a second short arm destroys target stackability. The constructive half gives all four target orbits, including explicit odd/even sequences for an outer endpoint. BFS-rule replay verifies 476 cases, and independent exhaustive search rejects nine finite obstruction cases. The proof, not these finite tests, establishes the entire parameter range.

## Originality — PASS
Fay–Hurlbert–Tennant, *Cup Stacking in Graphs* (arXiv:2310.06192, 2023), explicitly left mixed-arm spiders open apart from those with just one longer arm. Their theorem for spiders whose arms all have length at least two does not cover the unit arm. Gregor–Merino–Mütze–Verciani, *Graphs that admit a Hamilton path are cup-stackable* (arXiv:2401.06189, 2024), does not subsume the result: the present spiders have more than two leaves and no Hamilton path, while their tree-power and diameter-three obstruction statements do not provide the necessary positive constructions. Literature and mathematical-record searches did not find an equivalent theorem. The 2022 frog-jumping thesis was not read directly, and priority relative to inaccessible or unindexed work is not certified.

## Mathematical value — PASS
The classification resolves a natural infinite collection within the explicitly identified unsolved mixed spider regime; it exhibits a sharp one-versus-two-short-arm change and provides checkable winning strategies for every target in the positive case. This goes beyond a small finite census or a trivial specialization of the Hamilton-path sufficient condition.

## Scope and risks
Only \(a\ge1,b\ge2\) and arm lengths one/two are classified. The precise set of stackable targets for \(a\ge2\), other mixed arm lengths, independent mathematical review, and publication priority remain open.

Self-review: passed. Independent audit: not yet performed.
