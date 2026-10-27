# Scientific review

## Correctness

**PASS.** The full graph/team equivalence follows from splitting functional dependencies into edges oriented with outdegree at most one. A deletion-minimal non-pseudoforest is connected, has no degree-one vertex and has exactly one more edge than vertices. The two shore-degree inequalities force the sizes of the occupied shores to differ by at most one. These observations provide all upper bounds and edge cases. Explicit even and odd theta-graph families attain every intermediate size; every single-edge deletion of a theta graph leaves a pseudoforest. The packaged checker enumerates all subteams of eight small alphabet rectangles and checks constructions through forty occupied vertices on the smaller shore. Its finite checks do not replace the unrestricted proof.

## Originality

**PASS within the identified evidence, with residual priority risk.** Fröhlich--Kolaitis--Meier (CSL 2026, Lemma 15 and Theorem 25) already establish the graph equivalence and unbounded odd-size obstruction witnesses, which are not claimed new. The precise gap-free spectrum with sharp rectangular alphabet bounds, including the difference between balanced and imbalanced alphabets, does not follow as an explicit published statement in the inspected primary text. Barlag et al. (2026) address general coherence rather than these finite-domain extremal lengths. The 2003 complete-bipartite bicircular-matroid article enumerates bases, not explicitly circuits in its accessible abstract; Putnam's 2014 dissertation studies circuit spectra and is a genuine residual overlap risk because only its abstract was accessible. The exact claim would be covered if an older theorem already identifies the same circuit-size interval for every complete bipartite graph.

## Value

**PASS.** Unbounded incoherence leaves open how large a smallest failure can be when attribute value ranges are fixed, a natural parameter in finite database instances. The theorem settles both the largest necessary counterexample size and every attainable size for all pairs of ranges. It gives a sharp certificate-size threshold, a genuine square-versus-rectangle discontinuity, and a complete natural classification rather than a single sample count. Its utility is bounded-domain error-witness analysis, not a new model-checking complexity bound.

## Limitations and closest sources

The proof is specific to the opposite-dependence disjunction on binary teams. No all-formulas coherence theorem, witness-counting polynomial, or priority beyond inspected evidence is asserted. The full text of the 2003 bases paper and the 2014 dissertation was not inspected; their relevant circuit-spectrum implications remain uncertain. No independently performed audit is claimed.

Self-review: passed. Independent audit: not yet performed.
