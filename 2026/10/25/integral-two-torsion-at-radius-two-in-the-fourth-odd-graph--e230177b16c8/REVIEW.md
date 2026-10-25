# Scientific review: integral two-torsion at radius two in the fourth Odd graph

**Correctness — PASS.** Every distance is recomputed by breadth-first search; the complete 35-vertex flag complex has 1,211 nonempty simplices; all 280 lexicographic free-face pairs are checked while the deletion is made. The resulting 246-by-336 integer relation matrix has exact column Hermite normal form with determinant two; an independent mod-two rank is 245. The cellular argument establishes integral first homology of order two and free second homology of rank 90. The proof does not claim a homotopy classification.

**Originality — PASS, subject to ordinary bibliographic uncertainty.** The closest general graph-power collapse result, Adamaszek's Proposition 2.2, needs girth at least seven at radius two and therefore does not apply to this girth-six Odd graph. The primary Odd-graph Terwilliger-algebra article treats adjacency algebra rather than simplicial homology. Direct indexed searches for graph names, set-family formulation, face-vector fingerprint and integral group invariants returned other complexes, not a stronger theorem. Independence complexes of Kneser graphs use a different edge condition. An unindexed synonymous computation remains possible.

**Value — PASS.** This exact, natural case occupies the first boundary beyond the graph-power high-girth stability theorem. Integral torsion exposes coefficient-dependent Rips persistence that rational Betti numbers alone cannot show. A completely reproducible finite chain model supplies a reference for distance-regular-graph persistent topology.

**Closest literature and limits.** M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011), and Q. Kong, B. Lv, K. Wang, *The Terwilliger algebra of Odd graphs*, arXiv:1112.0410 (2011). The exact computation depends on running the complete included verifier and SymPy's integer Hermite-normal-form algorithm. No independent scientific audit has occurred; no stronger homotopy conclusion is made.

Self-review: passed. Independent audit: not yet performed.
