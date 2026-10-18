# Independent mathematical audit

## correctness

PASS

For 3-state automata, 512 possible 0-1 matrices per letter produce exactly 262,144 labeled ordered pairs. Ordinary integer matrix products count labeled paths, so a generator pair is strongly unambiguous iff all word products remain 0-1. BFS on finite 512-state product graph from identity both detects the first zero product and visits every reachable product; rejecting any invalid product tests unambiguity exhaustively. Independently implemented C++ pair/product BFS (not the source C++), compiled and evaluated all 262,144 pairs: exactly 12,502 unambiguous, 7,699 mortal, length histogram 271,3552,3192,540,132,12, exactly 12 length-six maxima, and direct product for abaaba is zero; a separately generated symmetry orbit of (10,98) contains exactly all 12 maxima by invariance and cardinality. The submitted C++ explicitly canonicalizes the 12 pairs under all six state permutations and both letter orders, yielding only (10,98); an independent Python symmetry orbit of representative (10,98) has size exactly 12, matching the total exhaustive count and proving there can be no other class; source independent Boolean composition corroborates every valid product. Exhaustion of all finite cases, not timeout or sample, establishes the finite universal result.

## originality

PASS

Best-of-knowledge non-coverage after primary statement and implication comparisons. The claim is not made new merely because a text query lacked an identical title.

## value

PASS

A sharp threshold and the entire equality-class census for the smallest meaningful strongly unambiguous binary automata give a natural finite base case in the active uncompletable-word/matrix-mortality problem. The exact all-pair enumeration and symmetry classification are independently useful despite not extending to arbitrary state counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
