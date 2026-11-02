# Independent mathematical audit

## correctness

PASS

PASS: Each predecessor block maps bijectively to a path of its output-label sequence in the four-pair De Bruijn overlap graph. Initial count at all start states is one; capping nonnegative path multiplicities at two before summation retains exactly the partition 0,1,>=2. A total capped state-sum of one is equivalent to exactly one entire finite predecessor, not just one terminal pair. Breadth-first search from (1,1,1,1) on at most 3^4=81 states is exhaustive for unbounded word lengths. Independent, separately implemented BFS for all 256 rule labels reproduced the exact length histogram, eight maximal witnesses, 92 never classes, right-boundary-only 42, and full-versus-boundary shortest gaps {0:132,1:20,2:8,3:4}. The inspected source verify.py additionally rederives and crosschecks CSV and all 32256 output words for n<=6 by direct input enumeration. Infinite absence of longer singleton words follows from finite-state closure, not merely length-six enumeration. Open-boundary definition is essential; no bilateral reversibility claim.

## originality

PASS

On the inspected primary sources and independent comparison, the specified new exact evaluation/classification is not supplied by a stronger known theorem; scope and residual priority limitations are stated explicitly. The equivalent path-count formulation is used directly; general predecessor-count machinery does not state the all-rule sharp finite minimum classification. Counting all whole-block antecedents prevents conflation with one-sided synchronization. The result has additional derived information not supplied by the general algorithm alone: exact class counts, optimal witnesses, and proof no never-rule can recover at any longer length.

## value

PASS

PASS: Gives the complete sharp cutoff and exact full-preimage observability classes for the canonical 256 elementary rules. The 42-rule gap distinguishes full finite-block reconstruction from terminal-pair synchronization, a natural invariant relevant to CA backward dynamics; finite-state classification is mathematically meaningful despite the finite rule universe.

The dated certificate retains the supplied scientific assessment, sources and limitations.
