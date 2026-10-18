# Scientific review

## Correctness — PASS

The loss of one pebble in each ordinary pebbling move makes the reachable-target recurrence acyclic and exhaustive. For fourteen vertices and initial weights zero through six, the number of states is exactly \(\binom{20}{6}=38{,}760\); both recursive state-mask evaluation and an independent breadth-first reachability algorithm identify no solvable distribution of weight below six and exactly 161 at weight six. The complete geometric predicates match the exact optimum list in both directions, and the local/all-pairs one-pebble exchange check yields exactly 42 edges partitioned into 21 three-vertex paths and 98 isolated vertices. A separate construction of all 336 graph automorphisms gives orbit sizes 21, 42, 42, and 56. The packaged certificate regenerates without discrepancies. All claims are finite and correctly quantified.

## Originality — PASS, with residual risk

The foundational optimal-pebbling treatment of Bunde et al. (arXiv:math/0510621, 2005) supplies general bounds and methods, but no Heawood-specific optimum census or relocation theorem. Belford and Sieben (arXiv:0707.4256, 2007) permit an additional strict-rubbling move and do not establish this ordinary-pebbling result. Targeted indexed queries for Heawood/Fano/Levi graph optimal pebbling and prior mathematical-record searches did not identify a logically covering result. Indexed search cannot establish worldwide priority; unindexed manuscripts or data tables remain a possible overlap.

## Value — PASS

Optimal pebbling measures the least initial resource allocation that can serve every possible target under a lossy transport rule. For the highly symmetric Fano-incidence graph, the theorem supplies all optimal placements, separates four symmetry classes, and demonstrates that nearly every minimum configuration is frozen under a capacity-preserving one-pebble relocation. The exact correspondence of the mobile configurations to the 21 incidence flags gives a structural answer rather than an arbitrary count. These distinctions are not implied by the known general size bounds.

## Limits

Only the fourteen-vertex Heawood graph is treated. Solvability means separate target-reaching sequences, while reconfiguration is a separate fixed-weight relocation operation. The work neither classifies all cubic graphs nor computes rubbling or simultaneous cover-pebbling optima. All verification is deterministic and same-model; no independent external audit has occurred.

Self-review: passed. Independent audit: not yet performed.
