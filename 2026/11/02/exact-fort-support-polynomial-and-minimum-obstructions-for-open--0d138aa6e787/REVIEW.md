# Review of exact open-ladder fort enumerators

**Correctness — PASS.** The transfer recurrence is literally the zero/one exterior-neighbor test for each row. Row-swap orbit reduction retains all weights. Exact rational symbolic identities derive the full generating function and three minimum-slack coefficient series. The triple-window and endpoint inequalities prove a global minimum, attained by explicit words and a length-three extension. Direct neighbor-based enumeration of 87,380 subsets and exact integer dynamic-programming checks through length 44 agree with the closed formulas. Computations are reproducible in `verify.py` and do not substitute for the infinite proof.

**Originality — PASS, qualified.** An October 2026 primary paper establishes a general fort-support formalism but neither states nor specializes to an exact open-ladder polynomial. The 2024 minimal-fort paper mentions an example on the four-rung ladder without an all-length count. The 2023 graph-product fort paper supplies generic inequalities rather than the size distribution. Ordinary zero-forcing polynomials count hitting sets instead of fort supports. Direct bibliographic comparisons, searches of alternate terminology and an available mathematical-results database identified no equivalent or stronger covering statement. Residual risks include a 2019 thesis on the ladder zero-forcing polynomial whose full text was not accessible, and possible unpublished or differently named enumerations. Lack of a database match alone is not a novelty certificate.

**Value — PASS.** Forts are exact obstructions to the standard zero-forcing process and supports for graph-pattern null vectors. Their all-cardinality distribution and the sharp minimum obstruction size are motivated invariants, while the exact mod-three multiplicity gives the complete extremal layer. The infinite rational law goes strictly beyond a known algorithmic possibility or a single small-graph example.

The result covers ordinary forts on labelled open two-row ladders. A separate independent mathematical review and comprehensive historical-priority review have not occurred.

Self-review: passed. Independent audit: not yet performed.
