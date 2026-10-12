# Self-review

## Correctness
**PASS.** The metric was reconstructed in two independent ways on all \(7140\) unordered pairs of \(S_5\): longest-common-subsequence dynamic programming and shortest paths in the single-translocation graph. Exhaustive four-clique enumeration gives \(4020\) candidates; each has empty common-neighbor intersection, so a five-code is impossible. The identity-normalized count \(134\), incidence identity, universal distance profile, and all natural-group orbits were independently recomputed by the packaged verifier.

Risk: the proof is a finite exhaustive computation, so reproducibility depends on the supplied verifier; it uses only the Python standard library and was freshly replayed from the packaged path.

## Originality
**PASS.** The exact same-parameter 2015 source gives the optimum \(4\) and a maximum-clique search description, but not the number or symmetry structure of equality cases. Later Ulam/deletion literature inspected for broader coverage gives general sphere-size results, bounds, and constructions rather than this census. Exact-number, alias, and implication searches found no statement covering the \(4020\) maxima, the \(134\) identity-normalized maxima, their equidistance, or the \(24\) natural symmetry orbits.

Risk: an obscure or unindexed historical enumeration could remain undiscovered.

## Value
**PASS.** The parameter is a literature-selected benchmark: the 2015 paper uses \(n=5,d=3\) to exhibit a strict gap between its integer-program bound and the true optimum. Classifying every equality case adds nontrivial structure beyond the known value. The universal equidistance and \(24\)-orbit decomposition give compact, reusable benchmark information for exact algorithms and structural work on Ulam/translocation codes.

Self-review: passed. Independent audit: not yet performed.
