# Self-review

## Correctness

PASS. The final claim is proved by an exact tensor-product expansion of Eq. (18), followed by trace-norm convexity. Every coefficient is nonnegative on \([-1,1]\), the coefficients sum to \(1\), and every partial-transpose subset is realized at a cube vertex. Complementary subsets have identical trace norms because they differ by full transposition. No numerical experiment is used to infer an infinite statement.

## Originality

PASS. The defining paper states the one-factor identity-transpose convex decomposition and uses endpoint partial transposes in examples, but its multipartite section retains continuous parameters, phase diagrams, and numerical analysis. Focused searches for equivalent formulations, stronger coverage, exact database matches, and claim-to-prior implications did not locate the general theorem that the whole parameter cube is the convex hull of subset partial transposes and that the source-style trace-norm maximum is therefore exactly the largest vertex negativity.

Closest literature: arXiv:quant-ph/0509006 is the defining source and the main residual-overlap risk because Eq. (18) is the key ingredient. arXiv:quant-ph/0102117 defines negativity and proves convexity, but does not discuss the partial-scaling family. The residual originality risk is an unindexed later remark deriving the same short convexity consequence.

## Value

PASS. The theorem removes a continuous optimization and parameter-plane scan from the Eq. (18) method for arbitrary multipartite states, replacing it by finitely many ordinary bipartition negativities. It also shows that no interior parameter can detect a state missed by all corresponding PPT tests. This directly clarifies the mathematical content and practical scope of the proposed multipartite criterion.

## Limitations

The claim does not apply to the broader anisotropic positive-map families proposed in the source's outlook, does not detect PPT entanglement, and does not assert that the resulting maximum is a distinguished multipartite LOCC monotone.

Self-review: passed. Independent audit: not yet performed.
