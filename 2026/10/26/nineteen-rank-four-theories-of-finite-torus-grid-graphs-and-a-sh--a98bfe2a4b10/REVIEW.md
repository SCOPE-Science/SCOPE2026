# Scientific review of the rank-four torus-grid classification

**Correctness — PASS.** The four-round cycle cutoff is taken from Brown and Hoshino (2007, Theorem 4.9). A coordinatewise Ehrenfeucht–Fraïssé strategy is given explicitly for the Cartesian product, reducing every integer dimension to at most 11. The atomic-diagram type recurrence is proved complete for bounded quantifier rank. Two independently encoded exhaustive classifiers agree on all 45 canonical graphs, on the 19 classes, and on their least sizes. `classification.json` provides the exact finite partition, and `verify.py` reconstructs it. Sharpness follows from the representative table and the fact that dimension truncation never enlarges a graph.

**Originality — PASS, with residual risk.** Brown and Hoshino classify games between individual cycles but neither classify their Cartesian products nor imply the sharpened product stabilization at dimension eight. The MathWorld torus-grid entry describes the graph family and its graph-theoretic properties, not first-order theories. Related published work on toroidal-grid topology or marked-vertex color refinement concerns different structures/invariants and does not imply an unmarked rank-four classification. No exact equivalent was found in the examined sources; unindexed historical treatments remain a genuine possibility. Absence of a search result is not considered proof of novelty.

**Value — PASS.** The classification is a complete finite-rank invariant of a natural, infinite two-parameter graph family. The reduction of the factorwise known cutoff 11 to the product cutoff eight is mathematically nontrivial and yields the sharp finite testing bound of 64 vertices. The exact separation of 19 classes is not supplied by the known cycle classification alone.

**Limits.** The theorem concerns simple undirected two-factor torus grids at quantifier rank four, without named coordinates or counting operators. Historical coverage cannot be ruled out absolutely. The review checks only the present claim, not independent scientific certification.

Self-review: passed. Independent audit: not yet performed.
