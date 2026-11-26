# Independent mathematical audit

## correctness

PASS

The graph defined by disjoint noncollinear triples is cubic on 28 vertices, so a total dominating set has size at least 10. The shell transitions show that S0∪S1∪S4 has size 10 and covers every vertex by open neighborhoods, with a unique triply covered center. An independent lexicographic 10-subset traversal discarded only branches where fewer than three new vertices per remaining choice would not suffice even at the maximum of three (equivalently, uncovered > 3 times remaining). It reached 3730 leaves after safe pruning, returned 28 covers, and verified equality of the full sets of masks with the 28 shell witnesses. It also computed all 378 pair costs, with (distance,cost,count)=(1,6,42),(2,9,84),(3,7,168),(4,4,84), and all distance-four graph profiles (1,6,15,6). This proves the sharp exchange threshold under simultaneous replacements preserving optimality at endpoints. Replay: python3 /workspace/reproductions/finite_checks.py 4.

## originality

PASS

The classical graph and distance regularity are prior knowledge. The inspected sources do not cover the complete minimum open-neighborhood cover family and its exchange geometry. The reported numerical disagreement with Jeyanthi–Hemalatha is not used as decisive novelty evidence because Lemma 2.2 was not independently retrieved.

## value

PASS

This is a complete optimum-family classification in a canonical symmetric cubic graph, not an isolated number produced by enumeration. Each optimum has a geometric center, and the complete exchange obstruction makes the gap between no moves and connectivity at four replacements precise. The result is useful independently of whether the reported prior numerical error is confirmed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
