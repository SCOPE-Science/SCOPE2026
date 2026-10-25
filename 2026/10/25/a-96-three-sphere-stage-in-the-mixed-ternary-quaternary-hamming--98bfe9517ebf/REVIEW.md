# Scientific assessment: A 96-three-sphere stage in the mixed ternary–quaternary Hamming box

## Correctness — PASS

The exact matching described in `RESULT.md` has a supplied executable certificate, `verify.py`, which re-enumerates all \(30,992\) augmented independent faces and checks all \(178,704\) directed cover relations. It verifies \(15,448\) matched pairs, a complete acyclic topological sort, and exactly \(96\) critical cardinality-four faces, along with a distinguished empty-to-vertex matched pair. Deleting the empty element makes the ordinary critical-cell vector \((1,0,0,96)\), which suffices for the wedge-of-three-spheres homotopy type. The 33-coordinate-simplex decomposition proves the scale-one wedge-of-40-circles stage independently of computation. This is a complete proof for the single finite object, not an assertion about all triple products.

## Originality — PASS, qualified

Closest primary literature: Antolín Camarena–Carnero Bravo (arxiv:2307.12401), Sections 1 and 4, **conjectures** the all-three-factor sphere-wedge claim and **proves** the version having a factor of size two; the predicted multiplicity for the current triple is already \(96\). Goyal–Shukla–Singh (arxiv:1905.06926) treats two factors; Adamaszek–Adams (arxiv:2103.01040) treats all-binary Hamming cubes. The closest indexed previous finite case is the 27-vertex triple \((3,3,3)\), not the 36-vertex triple \((3,3,4)\). Research-database and primary-literature comparisons looked for exact, dual and broader formulations, with scientific search details recorded in `AUDIT.json`. The public indexed (3,3,3) result's full text was unavailable; an unindexed or implicit covering proof remains possible.

## Mathematical value — PASS

A canonical first mixed-alphabet case settles a substantive finite instance of a published infinite-family homotopy conjecture, supplying homotopy type rather than merely the conjecturally predicted sphere count. It also yields complete integral persistence for the corresponding 36-point graph-metric Hamming space. The case is motivated by the explicit 2023 conjecture and is not an arbitrary graph slice.

## Limits

The conclusion does not solve the general three-factor conjecture; only the \((3,3,4)\) case is proved. The certificate is finite exhaustive computation whose correctness can be independently replayed, not an external mathematical audit. No group-representation result is asserted.

Self-review: passed. Independent audit: not yet performed.
