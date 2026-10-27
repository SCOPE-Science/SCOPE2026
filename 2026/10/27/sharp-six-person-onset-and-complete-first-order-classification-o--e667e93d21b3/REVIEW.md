# Self-review

## Correctness — PASS

The equilibrium criterion is derived from each player's buy-versus-free-ride incentives: all nonbuyers must be nominated, no buyer can be nominated by another buyer, and each buyer nominates exactly its degree-capped quota. The embedded verifier visits **every** edge mask at each order two through six, every buyer subset, every feasible exact nominee subset and every relabeling of each reversing six-vertex graph. The finite mathematical exhaustion justifies all reported counts, while the source's DP-Nash characterization confirms the game interpretation. The script ran to completion with passing assertions and integer-only checks. Scope is explicitly finite.

## Originality — PASS (residual bibliographic risk)

Gerke–Gutin–Hwang–Neary's Example 2 already proves *existence* of a capacity paradox on a six-vertex double-star; that is deliberately excluded from the novelty claim. The same source does not classify all connected graphs of orders at most six, show sharp absence below six, or list all eight first-order obstruction classes. Gutin–Neary–Yeo addresses uniqueness and computational complexity of DP-Nash subgraphs rather than this comparative-static finite classification. An earlier buyer-spectrum calculation for balanced complete bipartite graphs includes instances of the first-order layer but does not subsume the all-graph result. Semantic published-record searches for exact, equivalent and stronger forms returned related domination and social-choice problems, but no full covering result. There remains a risk of an unlocated enumeration or equivalent exact-capacity table.

## Mathematical value — PASS

The paper's core economic question is whether relaxing share constraints can perversely increase *minimum equilibrium* purchases. This theorem settles the earliest possible network size, identifies all obstructions at that boundary, and proves the original double-star is the unique least-edge obstruction. This is an exact natural threshold and structural boundary classification, not an arbitrary isolated small statistic or a restatement of the known example. Counts provide a reproducible measure of the phenomenon's frequency among first-order networks.

## Limits and source relationship

An exhaustive finite certificate is not an infinite-graph proof. The classification is confined to positive uniform integer capacities and binary exact-nomination equilibria. The original six-agent example and related graph-family results are prior art; this review asserts novelty only for the complete sharp threshold census. The earliest paper appearance is the 5 May 2019 preprint. Independent checking remains outstanding.

Self-review: passed. Independent audit: not yet performed.
