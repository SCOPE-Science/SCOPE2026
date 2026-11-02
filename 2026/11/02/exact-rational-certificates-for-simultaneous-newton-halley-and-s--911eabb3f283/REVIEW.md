# Mathematical review: certified triple-method quartic cycles

**Correctness — PASS.** The statement is a single theorem about one squarefree quartic and three standard rational iterations. The proof includes exact Newton substitutions, rational derivative identities checked in integer polynomial arithmetic, five root/pole-free intervals, strict image inclusions, contractions, and an exact discriminant check. A standalone verifier using no packages beyond the Python standard library passed on the embedded source. The finite certificate gives an infinite-periodic-orbit existence proof via contraction; finite numerical trajectories are not treated as proof.

**Originality — PASS with stated priority risk.** Basti and Cremaschi, *Simultaneous Global Convergence Failure of Newton's and Halley's Methods in Degree Four* (arXiv:2610.03246v1), already published this exact quartic and numerical evidence of all three cycles. Their Section 5 expressly omits the Halley and Schröder interval certificates, which are the precise new contribution. Collins and Hunter's degree-at-least-five three-method construction does not cover fixed degree four. Published-record searches and accessible prior claim comparisons yielded no exact Q-specific proof. Full-text priority beyond the inspected sources, including inaccessible Collins–Hunter material, is not certified.

**Mathematical value — PASS.** The new exact rational enclosures close the specifically identified numerical-to-theorem gap for three simultaneous classical root-finding failures in the smallest dimension presently known for the pair. The result proves actual attracting cycles and nonempty complex open failure basins, not just near-recurrence. It does not claim a new quartic construction, an entirely new existence prediction, generic dynamics, or intersecting basins.

The two non-Newton cycles and their approximate locations were previously predicted; the proof step supplied here is exact and independently replayable. This mathematical assessment is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
