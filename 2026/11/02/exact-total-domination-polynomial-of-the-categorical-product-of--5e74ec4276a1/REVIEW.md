# Mathematical review: exact total-domination enumerator

## Correctness — PASS

The stated invariant uses **open-neighborhood total domination** on the categorical product \(K_m\times K_n\). The key lemma is an exact biconditional: \(S\) fails if and only if it is a subset of a row-column cross. The proof then divides every failure by its unique active-row and active-column support counts. The six exhaustive regimes have independent counts; uniqueness of the singleton row or the paired-star centers avoids multiplicity. The displayed polynomial covers the boundaries \(m=2\), \(n=2\), and \(m=n=2\), and the corollaries follow directly. An independent adjacency-based verifier compares all coefficients in eleven finite graphs, checks the obstruction lemma directly in three graphs, and performs 625 larger-parameter arithmetic checks. Testing corroborates the all-parameter proof; it is not treated as an infinite certificate.

## Originality — PASS under accessible evidence

The closest foundational product papers are Defant–Iyer, arXiv:1708.01305 (2017), and Vemuri, arXiv:1908.02445 (2019). Their inspected proofs address scalar domination and total-domination bounds and selected structural cases; no direct all-size polynomial is stated. Hu et al., arXiv:1607.00400 (2016), provide general polynomial reduction techniques but not an evaluated categorical complete-graph-product enumerator. Mertens, arXiv:2401.00716 (2024), derives the ordinary domination polynomial of the *Cartesian* rook graph. The latter is not the graph or invariant here and its formula does not imply the present one merely by taking a complement. Narrow mathematical-record and web searches for categorical products, rook complements, cross-avoidance and full cardinality polynomials returned no equivalent all-size result. An enumeration of completed ordered total-domination histories, even when available, does not determine the number of unordered total-dominating vertex subsets at each cardinality. The current result is not presented as a discovery of the scalar optimum or the defining cross criterion alone.

## Mathematical value — PASS

Exact all-cardinality total-domination counts measure redundancy and robustness of open-neighborhood coverage in this natural dense graph product. The full formula yields the independent random-activation reliability for arbitrary probe availability, locates the complete failure boundary, and identifies all maximum failures without restricting to minimum sets. A disjoint support/paired-star decomposition provides structure, not just tabulated values. The two-row factorization and three-matching extremal coefficient are useful checks, but the substantive result is the two-parameter distribution itself. Its value does not depend on speculative downstream theorems.

## Residual risks and scientific limits

Unindexed edge-subset or complement-rook enumerations might cover the formula. A related older product-domination source was not inspected in full; available metadata describes scalar bounds, making direct polynomial coverage possible but not specifically indicated. Further independent priority and proof review would be useful. No result for three or more product factors, polynomial zeros, or coefficient log-concavity is asserted.

Self-review: passed. Independent audit: not yet performed.
