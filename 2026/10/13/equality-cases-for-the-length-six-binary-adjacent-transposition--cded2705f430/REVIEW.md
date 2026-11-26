# Independent mathematical audit

## correctness

PASS

The closed ball includes no error and precisely the five allowable adjacent swaps (counting repetitions only once), all at the same weight as the center. Thus different layers never conflict, and a full maximum must choose an optimum in every layer. In the within-layer token graph two closed radius-one balls intersect exactly when the centers are at distance at most two. The independent replay does not need this reformulation: it generates balls directly and checks all subsets in each layer from largest size down to the first feasible size, visiting every subset at that size. It obtains sizes (1,2,4,6,4,2,1), choice counts (1,6,14,1,14,6,1), and the one listed weight-three set. The sum and product give 20 and 7056, and all 7056 products were rechecked for disjointness. Complement and reversal commute and preserve the balls. The declared action has 84, 16 and 84 fixed codes for C, R and CR respectively; Burnside gives (7056+84+16+84)/4=1810, and direct orbit partition gives 4 singleton, 86 size-two and 1720 size-four orbits. This reproduces the recorded central claims, not a statement about the full graph automorphism group. Replay: python3 /workspace/branches/a507e681-a394-4067-914b-785ce7b92552/direct_ball_reproduction.py; saved output direct_ball_reproduction.json. The uploaded verification and certificate were inspected as evidence and the script was not executed. The auxiliary coverage histogram is not needed for the scientific finding.

## originality

PASS

The exact optimum 20, the standard benchmark graph and its Hamming-weight decomposition are prior. The supported distinct result is the complete equality classification at this benchmark: 7056 optima with specified layer choices, a forced central layer, and 1810 orbits for the stated symmetry action. Neither the benchmark's exhibited optimum nor the available token-graph packing results yield that complete classification. The inaccessible later token-graph paper remains a layer-level comparison risk, not negative evidence.

## value

PASS

This resolves the complete equality question for the standard 64-vertex benchmark rather than repeating its known maximum size. A researcher comparing or generating optimal codebooks can use the seven-layer factorization and forced middle set, and the orbit sizes quantify exactly which optima have extra channel symmetries. The structure is useful at this benchmark without requiring a general result for all lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
