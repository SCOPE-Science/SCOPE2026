# Scientific review

## Correctness

PASS. Each burning run is over by the third spreading step when both bipartition sizes are at least three: the first ignition burns the opposite part in the second spreading step, one further ignition is then possible, and the last remaining vertices face strict signed majorities. The proof explicitly classifies every attainable green set, proves the switching conjugation directly, and derives the Hamming-distance and covering-radius formulas by a two-star cut analysis. In particular, it separately checks the odd-order, equal-part even-order, and unequal-part even-order boundaries. Exact independent state enumeration passed for twenty parameter profiles, and complete switching checks passed on two small graphs. The experiments are finite corroboration only.

## Originality

PASS under accessible-literature comparison, with residual risk. Fallat et al., *Burning Signed Graphs*, arXiv:2610.02506v1, explicitly formulate reachability codes and their covering-radius relation, so neither notion is new. Their relevant primary full-text sections address general switching and signed paths, not the exact one-negative-edge biclique code or the two-star radius transition. Semantic indexed-record comparisons and title/alias/parameter searches did not reveal equivalent or stronger coverage. Unindexed work on graph burning or nonlinear covering codes could still contain an equivalent characterization.

## Value

PASS. The result identifies the complete reachable set and exact plurality for every switching of a canonical unbalanced signing, as well as an all-size covering-radius phase boundary. The weight enumerator stays fixed for different bipartition shapes of the same total order even though the covering radius changes; this separates code-weight information from worst-case pluralities. The minimum-degree-three boundary is structurally necessary for the proof's strict-majority mechanism, not an arbitrary finite slice. No theorem is claimed for degree-two boundary cases or other frustration classes.

Self-review: passed. Independent audit: not yet performed.
