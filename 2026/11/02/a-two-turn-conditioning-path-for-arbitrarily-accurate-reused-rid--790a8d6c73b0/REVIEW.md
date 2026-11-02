# Scientific assessment: a two-turn ridge-preconditioner conditioning path

## Correctness — PASS

The exact domain is two columns, \(A^{\mathsf T}A=\operatorname{diag}(4,1)\), a fixed sketch with Gram matrix \(H_t=G+tD\), and \(t>0\), \(\lambda\ge0\). The Cholesky preconditioned condition number equals the square root of the condition number of a symmetric positive-definite congruence matrix. The two eigenvalues give the displayed rational-radical expression. Its derivative has the exact opposite sign to the specified cubic; signs at \(1\) and \(2\), the positive leading coefficient, and Descartes' rule prove precisely two simple positive roots. The explicit sketch construction and full-support Gaussian neighborhood argument verify attainability and persistence. The standalone verifier passed symbolic and independently constructed matrix comparisons. Numerical tests support, but do not replace, the proof. Potential risk: the Gaussian assertion is positive probability, not typicality, and is formulated accordingly.

## Originality — PASS, with stated limits

The closest primary source, Meier–Nakatsukasa (2022), contains exactly the Cholesky ridge preconditioner and a uniform spectral embedding bound. Its relevant algorithm and proof sections were read; they do not state the two-turn path or an arbitrary-embedding-accuracy counterexample to unimodality. The closely related Meier–Nakatsukasa–Townsend–Webb study addresses finite-precision stability, and LSRN concerns preconditioning rather than the two-turn exact ridge path. Prior mathematical research records were checked for ridge preconditioners, spectral pencils, nonmonotonicity, and aliases; the retrieved nearest records concern different algorithms and do not logically imply this condition-number classification. Remaining publication-priority risk: the example may be obtainable from older generalized eigenvalue pencil results, not identified by these searches. Search nonretrieval alone is not proof of novelty.

## Value — PASS

A reused sketch is intended to support a family of regularization parameters. The numerical solver's preconditioned condition number is a natural quality metric across this family. A sharp constructive obstruction shows that even arbitrary embedding accuracy does not guarantee monotonicity or unimodality of that metric, so parameter-path search simplifications require more assumptions. Both turning points and their locations are exact consequences of a single cubic, and the phenomenon is robust to Gaussian full-support perturbations. The example is deliberately minimal and does not imply large practical slowdowns.

## Boundaries and independent review

The conclusion is an exact-arithmetic two-column existence theorem, not a claim for all sketches, all dimensions, or large probability or amplitude. A separate independent verification would be required before relying on the result for publication priority or practical algorithm design.

Self-review: passed. Independent audit: not yet performed.
