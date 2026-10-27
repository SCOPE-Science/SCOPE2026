# Scientific review of the three-orbit tangent-filling cubic classification

## Correctness — PASS
The full \(3^{10}-1\) coefficient-space incidence sieve and an independent NumPy implementation agree on exactly \(7488\) rationally nonsingular tangent-filling forms; the generated candidate-code lists agree entry-for-entry. Explicit projective group generators give three exhaustive scalar-normalized orbits of sizes \(936,936,1872\), verified by a separate algebraic substitution implementation. Direct algebraic-closure arguments, not finite extension testing, establish smoothness of every orbit representative. The conic exclusion establishes the minimum degree without conflating blocking in the original and dual planes. Risks: executable finite loops are part of the proof; the classification is not a general-field theorem.

## Originality — PASS, qualified
The closest primary source is Asgarli--Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, especially Theorems 1.1–1.3 and Question 1.5. It develops the property, bounds, and constructions but not the exact three-class \(\mathbf F_3\) census or its dual incidence configurations. Asgarli--Ghioca--Yip, arXiv:2208.13299, studies blocking by original curve points; it does not imply tangent-line coverage, and the three curves here are nonblocking in that distinct sense. Full small-field elliptic-curve catalogues might encode enough information to reconstruct the census; an unindexed exact predecessor is the principal residual publication-priority risk.

## Value — PASS
The least degree for the small nonsquare field \(\mathbf F_3\) is a precise instance of an explicit open-ended question about tangent-filling curves. The result does more than exhibit an example: it exhausts the smooth minimum-degree locus, gives its projective automorphism stabilizers and distinct rational dual blocking configurations, and exhibits smooth nonblocking curves whose tangents nevertheless cover the plane.

Self-review: passed. Independent audit: not yet performed.
