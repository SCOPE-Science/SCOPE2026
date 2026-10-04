# Same-model review

## Correctness
PASS. The power-set computation uses the defining transition action directly. Reverse breadth-first search from singleton subsets gives exact shortest merging lengths, not heuristic estimates. All \(9{,}765{,}625\) ordered pairs of five-state maps are tested; the synchronizing criterion is the finite distance of the full state set. The exact histogram sums to the independently reported synchronizing count. Canonicalization explicitly checks all \(120\) state relabelings and both letter orders for every extremal, and a separate orbit construction confirms that the displayed representative has \(240\) distinct labeled realizations. Packaged replay returns `VERIFY_OK`.

## Originality
PASS with a material residual risk. Behague--Johnson formulate the same triple-merging parameter and general extremal problem but the inspected 2020/2022 source does not state the exact global five-state binary value or classify all binary extremals. Targeted published-finding corpus and web searches for the exact value, state count, binary restriction, and orbit count returned no equivalent statement. Zhang's 2026 preprint is highly relevant: its public description concerns two-letter permutation/rank-\((n-1)\) automata for \(n\ge9\) and explicitly advertises additional finite restricted-class enumerations. The technical supplement was not accessible, so overlap with its restricted-class finite data cannot be excluded. That accessible description does not imply the present global census over every binary transition pair or its one-orbit classification.

## Value
PASS. Exact small-state values are natural calibration points for the triple-rendezvous problem, and the result does more than exhibit a slow automaton: it certifies the global binary five-state maximum, counts every labeled extremal, and reduces all extremals to one symmetry class. This gives a compact benchmark for future bounds, constructions, and census implementations.

## Closest literature and limitations
The closest middle-cohort source is Behague--Johnson, arXiv:2008.12166, first public 27 August 2020, which asks for and bounds shortest words merging some \(k\)-set. Gonze--Jungers supplies earlier triple-rendezvous background. Zhang 2026 gives a later lower-bound construction and advertises restricted finite computations; because its supplement was inaccessible, that source remains the main residual originality risk. The claim is confined to exactly two letters and five states.

Same-model review: passed. Independent audit: not yet performed.
