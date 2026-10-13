# Scientific review: exact random-time mixing on the five-vertex path

## Correctness — PASS
The proof uses the adjacency spectrum \(\{\sqrt3,1,0,-1,-\sqrt3\}\), exact spectral idempotents, and the bipartite sign conjugation to represent all 15 independent mixing entries by six real moments. Six selected entries give a nonsingular exact linear system (determinant \(\sqrt3/972\)) with unique solution \((-1/5,0,2/5,2/5,0,0)\); substitution checks every remaining entry. The two explicitly positive torus densities realize these moments. An everywhere-positive barycentric integral is in the relative interior; dense irrational time flow plus finite-dimensional convexity and Carathéodory then yield exact strictly late physical observations with support at most seven. `verify.py` recomputes the nonstandard algebra from the original path adjacency operator. Numerical quadrature is corroboration, not proof of an exact finite distribution.

## Originality — PASS, residual risks below
Baptista–Coutinho–Marques (arXiv:2308.16378, Sections 3.2 and 4.3) solve \(P_3\) and \(P_4\) under arbitrary sampling and explicitly leave larger paths as a question in Section 7. Coutinho–Guo (arXiv:2404.02236, Section 4.2) still describes \(P_n\) for \(n\ge5\) as open in 2024. Their statements do not logically imply this exact six-moment characterization or seven-support late-time realization for \(P_5\). Earlier weighted universal mixing and discrete-time Szegedy averaging are inequivalent settings. Targeted searches of indexed publications and semantic research findings found no known exact same claim; this is not a proof of global uniqueness. A post-2024 equivalent theorem using a different phrasing remains possible.

## Value — PASS
This addresses the first unresolved order of the explicit larger-path open question, not an arbitrary numerical sample. The theorem provides a complete necessary-and-sufficient criterion for *every* sampling distribution on \(P_5\), a positive full-support phase witness, exact finite physical sampling, a universal seven-atom upper bound, and the ability to postpone all observations. The incommensurate spectral frequencies make a direct fixed-time algebraic construction unavailable; the strict-convexity argument turns dense approximation into exact expectation. The result does not resolve longer paths or optimal support size.

## Scientific limitations
Existential sampling times and weights are not output by a finite explicit formula. No independent review has occurred; the symbolic replay addresses algebra only. Additional literature under alternative names for random-time averaged transition matrices may exist.

Self-review: passed. Independent audit: not yet performed.
