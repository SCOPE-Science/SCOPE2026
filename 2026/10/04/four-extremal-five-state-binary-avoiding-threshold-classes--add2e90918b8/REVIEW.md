# Independent mathematical audit

## correctness

PASS

The inspected C census enumerates all 3125^2=9,765,625 ordered transition pairs, performs exact BFS in the 32-subset power automaton, records the first reachable subset omitting each state, and tests singleton reachability for synchronization. Its deterministic output gives 8,063,385 synchronizing pairs and histogram ending in exactly 960 threshold-eight pairs. Canonicalization enumerates all 5! state permutations and optional letter swap. The Python verifier recompiles/reruns the census, checks byte-for-byte output, verifies the four representatives, their exact avoidance vectors, four disjoint 240-element symmetry orbits, and A_5 membership. An independent replay of the four representatives/orbits reproduced the avoidance vectors and orbit sizes. The finite claim is exhaustive, not extrapolated.

## originality

PASS

Ferens--Szykuła--Vorel already give the exceptional five-state automaton A_5 with 1-avoiding threshold 8 and report small-state experimentation, so the numerical maximum 8 and one extremal orbit are prior. The inspected primary paper does not state the complete labeled census 960 or the four symmetry classes. A fresh Resultary search for the exact five-state classification returned no covering published theorem.

## value

PASS

This is the complete extremal classification at the first published exceptional five-state threshold, not merely a verification of A_5. The exact multiplicity and three additional symmetry classes are natural finite extremal data for the avoiding-threshold problem and provide reusable test cases for general conjectures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
