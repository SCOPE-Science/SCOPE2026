# Scientific review

## Correctness — PASS
The theorem covers every integer parameter \(d\ge3\), \(q_i\ge2\), with at least two alphabet sizes unequal. The proof starts with the exact graph Laplacian, constructs its resolvent on an edge-eigenvector factor, and verifies positivity and marginal identities that give each full projection column norm. The diagonal entry is evaluated by a finite exponential expansion. The comparison of two unequal directions is algebraic, with a separate rigorous bound for the potentially adverse pair \((2,3)\) in the presence of a third factor. Since both projection matrices are real symmetric, the endpoint \(\ell_\infty\) equality follows without an extra assumption.

An independent exact-rational construction of the grounded graph Laplacian and each complete edge projection column agrees for 579 edge columns on seven mixed Cartesian clique products. These computations corroborate the symbolic proof and do not establish its infinite quantifiers independently.

## Originality — PASS, with residual risk
The most relevant original literature is Dilworth–Kutzarova–Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (arXiv:2305.12582v1). Sections 2.6–2.7 were inspected beyond their abstracts. Their Hamming graphs have the same alphabet size in each coordinate, and the sharp binary cube cut norm is a special case. The predecessor covers neither general unequal sizes in three or more factors nor simultaneous smallest-factor maximization of the cut and cycle orthogonal projection column norms. The foundational graph-quotient treatment in arXiv:1807.03814 is also distinct. Known equal-alphabet and two-factor cases are expressly outside the new contribution.

Meaning-based scientific database searches and public literature searches included Hodge and transfer-current aliases, exact endpoint values, Cartesian complete-graph products, and possible dominating theorems. None yielded a covering statement. This is best-knowledge originality; absence from search is not proof of uniqueness, and unindexed sources remain a risk.

## Mathematical value — PASS
The result classifies two natural operator invariants on all nonuniform Hamming products with at least three factors and gives exact computable finite formulas. More substantially, despite different factor sizes and loss of coordinate-swap symmetry, the worst-case column for **each** of the two complementary projections is always along a smallest alphabet. A separate positivity argument resolves the otherwise exceptional two-factor comparison. The classification is relevant to norms of canonical Hodge decompositions in finite graph transportation spaces, not a claim about all possible projections.

## Limitations
All graph edges have unit conductance and the edge space is real. Interior \(\ell_p\) exponents, weighted variants, arbitrary Cartesian factors, and unrestricted minimum projection constants are not determined. Independent verification remains outstanding.

Self-review: passed. Independent audit: not yet performed.
