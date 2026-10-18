# Scientific review

**Correctness — PASS.** The incidence-matrix identity transfers inertia and determinant of the line graph to the shifted signless Laplacian plus known \(-2\) eigenvalues. The base cycle inverse diagonal and each Schur complement are computed explicitly. A one-scalar boundary resolvent proves that every matrix is nonsingular, tracks the unique possible rank-one sign change, and telescopes determinants. The independently implemented exact rational and integer verifier checked 1,254 cases. Finite checks supplement, rather than replace, the proof; the boundary case with branching was independently calculated.

**Originality — PASS, with acknowledged residual risk.** Francis–Uptain's 2026 results concern a bridge-connected cactus gadget and positive-signature constructions; Paone–Paone completely analyze roses/theta graphs but present only partial bridgeless-cactus bounds. This formula applies to arbitrarily long non-rose block paths with distinct articulations; its exact determinants and nonsingularity are not consequences of a signature upper bound. Prior single- and two-cycle cases are excluded from novelty. No semantically equivalent record appeared in targeted indexed searches; unindexed or inaccessible work could still coincide.

**Value — PASS.** The theorem computes every inertia component and the determinant for a natural infinite family, with unexpectedly small dependence on all cycle lengths and articulation positions. The change at the first \(1\pmod4\) block identifies the exact structural spectral transition, while a computed branching counterexample locates the family boundary. This goes beyond a routine value for a single small graph and complements general cactus bounds.

Closest literature: Francis–Uptain arXiv:2607.22874, Paone–Paone DOI:10.5281/zenodo.21744051, and Wang–Fan arXiv:1310.1003. The proof covers odd block paths only, not branched cacti or bridges. Some historical literature may be unindexed; no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
