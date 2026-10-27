# Scientific assessment

## Correctness

**PASS.** The regular-graph edge identity excludes every forest on eleven or more vertices. For a ten-vertex forest the six deleted vertices must induce at most one edge. Exhaustive parity-profile reasoning rules out the five mixed deletion profiles; the surviving pure-parity profiles are forests precisely for antipodal surviving pairs. This yields eight and proves one-swap isolation. The three-cube count and connectivity are proved by its complete deletion-triple classification and an explicit bridge between the parity cores. Two independent acyclicity predicates in `verify.py` agree on all 65,536 labelled subsets of the four-cube, and a separate exchange reconstruction confirms both dimensions.

## Originality

**PASS with expressly bounded residual risk.** Focardi–Luccio–Peleg and Pike establish hypercube decycling bounds and numerical extrema, while Pike–Zou determine the scalar decycling number for all products of two cycles; the last paper covers the value for the isomorphic toroidal four-by-four cube. These established numerical conclusions are not claimed as new. The precise eight equality configurations and their zero-edge exchange graph are not logical consequences of a scalar optimum, existence of one extremizer or the general bound, and no indexed covering statement was located by searches for antipodal minima, exact decycling-set classifications and single-vertex reconfiguration. The accessible full text of Gunderson–Meagher–Morris–Pantangi was examined for relevant theorem coverage, but the older full papers could not be read: they remain material originality risks rather than presumed negatives.

## Value

**PASS.** This is a complete equality and optimum-reconfiguration classification at the first canonical hypercube dimension exhibiting fragmentation. The contrast with connected dimensions two and three distinguishes an optimum's numerical size from the mobility of optimal configurations and provides a small exact benchmark for feedback-vertex-set reconfiguration. The mathematical point is the forced pure-parity antipodal structure and exchange rigidity, not merely recomputing a known decycling number.

## Limitations

The result is finite-dimensional and does not claim a higher-dimensional analogue. Indexed searches cannot prove novelty; published complete texts for the closest older sources were not accessible. All computational outputs are independently reproducible, but no independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
