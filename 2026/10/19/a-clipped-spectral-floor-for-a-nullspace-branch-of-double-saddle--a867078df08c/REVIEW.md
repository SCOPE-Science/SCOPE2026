# Scientific review

## Correctness — PASS

The claimed bound follows from the scaled eigen-equations of Liang and Huang, arXiv:2609.01031v1, equations (2.2)–(2.4). Testing the first and third equations against their eigenvector components gives the exact positive energy identity, which also handles a possible coincidence of the eigenvalue with the second diagonal block spectrum. Only in the sub-minimum-eigenvalue branch is the resolvent positive; Loewner inversion there yields the quadratic inequality and the stated clipped floor. The explicit parameter family satisfies every source block-size, rank, and SPD hypothesis; direct multiplication gives eigenvalue \(1\), and its coupling Gram matrix is diagonal with minimal eigenvalue \(3+7t^2\). The rational witness and boundary-equality construction were checked using the packaged exact-arithmetic verifier. Continuous claims are justified analytically, not by extrapolating finite tests.

## Originality — PASS (self-review)

The source's specific Lemma 2.2 asserts the opposite of the demonstrated unbounded family, so its statement cannot already contain this example as a covered positive result. Its cited scalarization step treats a resolvent Rayleigh quotient as if it were the inverse of a shifted ordinary Rayleigh quotient; the explicit eigenpair exposes the distinction. The open-access full text of Balani Bakrani et al. (2024), particularly Sections 2 and 4.1, treats another saddle-point ordering, Schur-complement normalization and triangular preconditioner; its explicit real-eigenvalue bounds do not imply the present counterexample or corrected floor. The published published-finding corpus search results located related spectral and preconditioning findings but no equivalent assertion for this pencil, and neither own ledger contains a direct source/claim match. This is a limited literature-supported originality judgment, not proof that no earlier equivalent counterexample exists.

## Value — PASS

The false bound appears in the motivating paper's spectral analysis of a preconditioner for PDE-constrained optimization and is used as an intermediate comparison in its subsequent real-eigenvalue argument. The example is not simply a parameter check: it gives a fully admissible exact eigenvector while holding the diagonal spectral conditioning fixed, makes the reported lower bound arbitrarily wrong, and identifies an operator-resolvent branch distinction that supplies a constructive corrected bound. The small-coupling equality example shows that the surviving resolvent estimate is attained, while explicit scoping avoids claims about algorithms or other parts of the source that have not been checked.

## Residual risks and limits

Older abstract matrix-pencil theorems may imply the safe enclosure, and an independent audit has not been performed. The 2026 symmetric-SPD preconditioning comparison was available primarily as an abstract; it is not treated as a full-text exclusion. The witness is deterministic and concerns the null-coupling real-eigenvalue branch, not the source randomized approximation scheme as implemented.

Self-review: passed. Independent audit: not yet performed.
