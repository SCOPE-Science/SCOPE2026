# Scientific review of the Coxeter critical-group decomposition

**Correctness — PASS.** Explicitly defined Fano–Kneser graph has 28 vertices, 42 edges, girth seven. The provided exact integer certificate establishes \(RB=56I\), so all invariant factors divide \(56\); the integer determinant \(2^{18}7^5\) and ranks 21 modulo two, 22 modulo seven uniquely force \(8,56,56,56,56,56\). Re-execution of a separate SymPy Smith computation confirms all factors. The vertex identification, matrix, and certificate are included, not inferred from a log.

**Originality — PASS, qualified.** The full accessible text of Dejter's arXiv:1002.1960 (Sections 1–4) addresses graph structure and seven-cycle ultrahomogeneity, not Laplacian Smith factors. MathWorld's Coxeter graph article gives its spectrum; the determinant follows but the full integral cokernel does not follow from the eigenvalue multiset alone. The 2003 Jacobson–Niedermaier–Reiner paper treats other graph families. Targeted bibliographic searches for Coxeter graph critical/sandpile/Jacobian/Smith and the exact factors found no matching published decomposition. A result for the McGee graph concerns a distinct 24-vertex cubic cage. Unindexed and historical tables remain a substantive residual priority risk.

**Value — PASS.** This is the full integral critical group, a canonical chip-firing and graph-Jacobian invariant, of the 28-vertex cubic distance-transitive hypohamiltonian Coxeter graph. The exact exponent, six-generator rank, and five-dimensional seven-torsion cannot be read off from the known spanning-tree count or spectral determinant; the certificate supplies an independently usable exact invariant for this benchmark graph. The result is an isolated exact classification, not a claimed family theorem.

**Limits.** Search results do not demonstrate global originality. No claim is made for other distance-regular graphs, and no external review has occurred.

Self-review: passed. Independent audit: not yet performed.
