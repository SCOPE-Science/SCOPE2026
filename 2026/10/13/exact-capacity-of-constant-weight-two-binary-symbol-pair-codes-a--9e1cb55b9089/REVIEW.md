# Scientific review — binary weight-two symbol-pair codes

## Correctness — PASS

The cyclic pair-read definition is explicit for every integer \(n\ge3\). A support-symmetric-difference identity proves that two weight-two words are incompatible at distance four precisely when they share one one-position and their other positions are adjacent on the cycle. This gives an *if and only if* graph reduction. Cycle independence bounds every graph degree by \(\lfloor n/2\rfloor\); degree summation establishes the claimed upper bound. The constructions have exactly the target number of edges: a complete bipartite graph for even length; a degree-\(k\) circulant for \(n=2k+1\) with even \(k\); and a degree-\(k-1\) circulant plus a step-\(k\) maximum matching for odd \(k\). The circular gap checks cover the two odd cases, including \(n=3\).

A standalone script verifies all constructed families through length 120, directly re-evaluates pair distances through length 15, and exhaustively determines the true independent-set optima for lengths 3 through 11. The general theorem relies on the mathematical argument, not on a numerical induction.

## Originality — PASS, with risk

The object is a constant **Hamming-weight-two** code, not a homogeneous constant **pair-weight** code. Earlier foundational and MDS papers give the pair-distance framework and much broader unrestricted bounds, but those statements do not themselves imply the exact constrained maximum. A closely relevant later paper treats separate fixed pair-weight layers; its abstract and preview are available, but its complete text was inaccessible. Because the current code may mix pair-weight-three and pair-weight-four words, a homogeneous-layer result does not directly classify it. A substantially stronger uninspected result could nevertheless contain the formula, and absence of an indexed match is not proof of priority.

Searches covered direct formulas, the graph-neighborhood equivalence, aliases for constant-composition and sparse support code families, published mathematical findings, and exact enumerations. The nearest results and residual risk are documented in `AUDIT.json`.

## Value — PASS

This determines an exact natural capacity function for **every** binary block length under a fixed sparse-data constraint and one symbol-pair-error-correcting distance requirement. The all-length upper bound is sharp via structurally distinct parity cases, with a matching repair of the odd-degree parity obstruction by a maximum matching in a circulant cycle. The result is a complete infinite family, not a single small-case computation or a routine repackaging of unrestricted MDS bounds. It establishes no results for larger support weights or stronger distance requirements.

Self-review: passed. Independent audit: not yet performed.
