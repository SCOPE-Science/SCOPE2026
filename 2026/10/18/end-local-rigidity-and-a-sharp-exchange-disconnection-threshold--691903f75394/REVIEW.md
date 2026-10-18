# Scientific review

## Correctness

**PASS.** The structural argument first proves that the zero forcing number is three, then uses the degree-two/degree-three first-force alternatives to confine every minimum set to three columns at an end. Prefix monotonicity reduces all candidates to 84 explicit triples of the five-column graph. Exhaustive enumeration finds precisely 13 left-end triples, and independently checks a bounded forcing history for each that fills all three initial columns without help from columns to its right; column-by-column forcing extends these results to every larger grid. The exchange graph is obtained from intersection size two. The complete thirteen-vertex edge list has 24 edges, radius three and diameter five. Separate set-based and bit-mask programs agree for all checked finite widths. The infinite conclusion depends on the written degree-and-prefix proof, not on extrapolating the tests.

## Originality

**PASS with residual risk.** The 2011 paper arXiv:1105.1492 already gives the *size* of a minimum zero forcing set on Cartesian grids, and the 2020 paper arXiv:2009.00220 already defines and analyzes exchange graphs of minimum zero forcing sets. Neither inspected source presents or implies the structural claim that all three-row grid minima live in three-column end windows, the exactly 26 labeled sets, or the connected-to-disconnected transition at length five. Searches for the row-width aliases, basis count, connectivity and exchange graph turned up related rather than covering literature. No search guarantees exhaustive global priority; equivalent unindexed classifications are possible.

## Value

**PASS.** This is a complete classification for an infinite natural family of Cartesian product graphs. The sharp threshold distinguishes short grids in which optimal forcing placements are mutually reachable from all longer grids in which no optimal single-token exchanges can move a placement from one end to the other. The constant-size 13-state component, exact diameter and end-local support are structural information directly relevant to optimal sensor or control placement under no-extra-resource reconfiguration.

## Scope and limitations

The result concerns three-row ordinary zero forcing, minimum cardinality three, and single-token jumps only. The boundary classification is finite and reproducible, whereas the all-length guarantee is proved separately. A full independent external mathematical audit and unrestricted literature-priority certification have not been performed.

Self-review: passed. Independent audit: not yet performed.
