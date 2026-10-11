# Independent mathematical audit

## correctness

PASS

The power-automaton distance from each nonempty subset to the singleton layer exactly equals the shortest merging-word length. The repository census visits all \(3125^2=9,765,625\) ordered transition-map pairs and applies reverse BFS on the 31 nonempty subsets. An independent compiled implementation reproduced 8,063,385 synchronizing automata, the exact histogram \(1:4183905,2:3369480,3:387600,4:93600,5:23760,6:4800,7:240\), maximum seven, and a single canonical orbit among all extremals. The package verifier separately checks the canonical representative, all ten triple distances, reset word and orbit size 240.

## originality

PASS

Gonze--Jungers and Behague--Johnson develop the triple-rendezvous parameter and general upper bounds, not an exact binary five-state census. Zhang's 2026 paper constructs a binary family only for \(n\ge9\); its public record says the paper includes computational notes and links a supplement, but accessible statements do not give a global five-state census or unique extremal orbit. Resultary and exact small-state searches found no prior equivalent. The inaccessible supplement is retained as a concrete residual risk rather than treated as negative evidence.

## value

PASS

The triple-rendezvous time is a standard intermediate synchronization invariant. A complete smallest-scale binary extremal census with an exact maximum and unique symmetry orbit gives a natural finite benchmark for the recent construction and bound literature; it is not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
