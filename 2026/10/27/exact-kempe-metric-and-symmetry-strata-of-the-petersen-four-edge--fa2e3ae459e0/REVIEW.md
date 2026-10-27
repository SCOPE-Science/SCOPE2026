# Review of the exact Petersen four-edge-colouring Kempe graph

## Correctness

PASS. Complete state enumeration using canonical restricted-growth colours yields exactly \(2080\) classes; a fixed-star enumeration produces the identical set. Two edge-component traversals reconstruct the same Kempe neighbours for every state. The resulting undirected simple graph has degree counts \(1840\) at \(12\) and \(240\) at \(13\), giving \(12600\) edges. BFS from every state establishes connectivity and the full eccentricity profile. Enumerating all \(120\) Petersen graph automorphisms yields the listed \(21\) state orbits, with constant eccentricity on each.

## Originality

PASS, subject to a finite-data literature risk. McDonald–Mohar–Scheide proved four-edge-colouring Kempe *connectivity* of all subcubic graphs, which does not imply an exact distance metric or symmetry strata. Published work on three-edge-coloured cubic graphs does not cover proper three-edge-colourings of the Petersen graph, as none exist. General vertex-colouring Kempe-diameter results use another state space. Targeted exact-value, equivalent-formulation and database searches did not identify these numerical orbits; that failure alone does not establish novelty. Unindexed tables remain possible.

## Value

PASS. The Petersen graph is the smallest standard class-II cubic test case, making its four-edge Kempe reconfiguration the first natural nontrivial edge-colouring benchmark. Its radius–diameter distinction and automorphism-transitivity of the centre, but not the periphery, expose quantitative structure unaddressed by connectivity alone. These are exact, reproducible invariants of a naturally defined graph, not an unmotivated parameter slice.

## Scope and remaining limits

Exactly four edge colours; the state space is modulo global colour permutations. Distance in the fully colour-labelled graph can be different. There is no claimed extension to other snarks. Some related literature was available only in summary or bibliographic form; this is explicitly a residual originality risk. The attached verifier gives complete finite checks but not an external independent certification.

Self-review: passed. Independent audit: not yet performed.
