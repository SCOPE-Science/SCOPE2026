# Assessment of the integral pendant-leaf controllability theorem

## Correctness — PASS

The general statement is proved by a block recurrence for \(\widetilde L^j\widetilde e\). Its top columns factor exactly as \(-tK(G,r)U\) for a unimodular integer upper triangular matrix \(U\). Elementary row/column operations give \(\operatorname{diag}(1,tK(G,r))\) and the signed determinant identity. The finite sharpness component follows from a fully enumerated generator of all free trees through nine vertices and exact Bareiss determinant tests for every possible actuator site; no floating-point cutoff or extrapolation is used. The index-two parity restriction follows from an explicit mod-two annihilator plus index equality. The arbitrary-order continuation follows formally from the transfer theorem. Risk: independent replication of the full finite census has not been formally certified, though the included self-contained checker regenerates it.

## Originality — PASS, with historical risk

The nearest direct prior statement is Hsu and Yang (2019), Corollary 3: it covers rank preservation under exactly the same pendant extension. Rank preservation is therefore **not** claimed as new. The stronger integer unimodular equivalence, preservation of Smith torsion, and nine-vertex minimum with an index-two congruence are not implied by that rank statement; matrices can share rank yet have different Smith invariants. Parlangeli and Notarstefano (2011) treat path/cycle rank criteria, while Parlangeli (2025) focuses on rank conditions for starlike trees. The published search results examined do not supply the combined integral transfer and sharp all-tree threshold. Historical risk remains that equivalent integral Kalman-matrix results may be indexed using alternate terminology; this is not a certification of global priority.

## Value — PASS

Integer-valued inputs are a natural restriction in quantized discrete control. Two networks can be fully controllable over the rationals or reals yet have different finite-horizon reachable integer lattices. The exact integral extension rule preserves the full obstruction group, while the smallest nine-vertex example exhibits a nontrivial \(\mathbb Z/2\mathbb Z\) obstruction and provides witnesses at every larger order. The finite sharp threshold is independent mathematical information, not just a restatement of a rank-controllability result. No broad downstream application is asserted without evidence.

Independent external originality and correctness confirmation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
