# Independent mathematical audit

## correctness

PASS

In a cactus, every simple cycle is exactly one cycle block and the block-vertex incidence graph F is a forest after bridges are omitted. Cycle-convex activation of v requires every other vertex on one incident cycle C to be active. An essential certificate for v must pass through one selected incident cycle, yielding a_{v->C}=max(1,max_{D≠C}b_{D->v}); an essential C-side certificate uses disjoint branches for all other vertices, yielding b_{C->v}=sum_{u∈C\{v}}a_{u->C}. Acyclicity ensures removing any one chosen seed cannot be compensated by another branch; hence c_cc(G)=max_v max(1,max_{C∋v}b_{C->v}). Bottom-up/top-down edge-message passes with top-two maxima and cycle sums run O(V+E) and reconstruct an optimum witness. Independent brute force over every subset and cycle closure confirmed all 103 connected cactus graphs of the NetworkX atlas through 7 vertices; the general proof uses the acyclic incidence decomposition, not this finite enumeration.

## originality

PASS

Best-of-knowledge priority comparison on the exact final statement, allowing explicit inaccessible-primary-source risks; known related first-moment, connectivity, single-class and one/two-factor theorems are acknowledged as prior, not claimed new.

## value

PASS

A closed structural recurrence and full maximum-witness linear-time algorithm on the natural broad cactus graph class, explaining why long chains of cycles increase the invariant but friendship graphs do not. Distinguishes cycle convexity from the unrelated P3/triangle variants and advances a newly studied Carathéodory problem beyond forest and single-cycle cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
