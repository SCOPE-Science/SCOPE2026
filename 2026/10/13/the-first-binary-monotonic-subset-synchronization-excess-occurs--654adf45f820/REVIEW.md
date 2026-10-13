# Self-review

## Correctness
PASS. In a monotonic automaton, synchronizing a subset is equivalent to synchronizing its minimum and maximum, so the problem reduces exactly to state pairs. The verifier enumerates every nondecreasing chain map and all binary map pairs through nine states. It obtains the exact threshold sequence \(0,1,2,3,4,5,6,7,9\), isolates exactly two unordered normalized nine-state extremals, and independently replays the length-\(9\) witness by forward breadth-first search.

## Originality
PASS. Ryzhikov and Shemyakov give the general quadratic upper bound and a binary quadratic lower-bound family, but do not give exact binary small-state thresholds. The later weakly acyclic paper cites only the asymptotic monotonic result. Searches using exact values, first-excess language, fixed-binary-alphabet terminology, transition tables, and the witness word found no published covering statement.

Residual risk remains for an unindexed or unpublished computation.

## Value
PASS. The source makes binary monotonic subset synchronization a distinct extremal regime, yet its bounds do not say when behavior first exceeds the elementary \(n-1\) scale. The exact first excess at nine states, plus the one-orbit normalized extremal classification, identifies a natural structural boundary for the onset of longer subset synchronization.

Self-review: passed. Independent audit: not yet performed.
