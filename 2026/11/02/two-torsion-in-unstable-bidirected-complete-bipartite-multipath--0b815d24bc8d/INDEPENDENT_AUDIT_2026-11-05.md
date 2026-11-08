# Independent mathematical audit

## correctness

PASS

For fully bidirected K_{2,n}, enumerating all arc sets of size≤4 with in/out-degree≤1 and no directed cycle gives complete simplices. Independently enumerated f-vectors n=1..6, including n4 (16,80,144,72), n5 (20,130,320,240), n6 (24,192,600,600), and separately computed mod-2/mod-3 original boundary ranks. Independently reconstructed the specified greedy discrete-Morse matching with original arc order and its signed integral cancellations: n4 151 pairs, critical (0:1,2:8,3:1), six boundary entries ±2/gcd2; n5 338 pairs, (0:1,2:1,3:32), 26 even entries/gcd2; n6 623 pairs, (0:1,3:169). Read the source verify_moore.py: full Hasse orientation topological sort verifies acyclicity, not just matching cardinalities. The Morse complexes have simply connected 2-skeleta, so signed rank-one integer boundary Smith factor 2 yields Moore-space wedges; no all-n homotopy claim. For the module assertion, a region containing an arc must contain its reverse by 2-cycle closure, then no endpoint can be boundary; connectedness propagates to all arcs. Hence the unique module is unstable, contradicting the literal 2022 v1 conjecture.

## originality

PASS

The 2022 introduction explicitly conjectures stable modules as necessary for torsion. The exact bidirected K_{2,4}, K_{2,5} signed Moore homotopy decompositions and single-unstable-module counterexample are not implied by cited alternating-orientation or acyclic-digraph results.

## value

PASS

A concrete finite, reproducible counterexample to a published stability–torsion conjecture is intrinsically important, and its full integral homotopy types and within-family first occurrence sharply identify the obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
