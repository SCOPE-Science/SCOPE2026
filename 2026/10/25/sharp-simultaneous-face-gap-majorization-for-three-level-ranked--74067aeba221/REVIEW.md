# Self-review

## Correctness
The proof uses explicitly defined vertex-indexed face polynomials, the free-join geometry of the order polytope, and the pyramid/subdirect-sum geometry of the chain polytope. The exact face polynomial subtraction is independently checked, as is the generating-function identity for the complete homogeneous functions. Jacobi–Trudi and a specific semistandard tableau establish strictly positive coefficients at every required degree, including the sharp equality cases and the boundary singleton layer. The standalone verifier tests 169 symbolic pairs, 68 balancing identities and eight independently enumerated small face lattices; finite checks are supplementary to the all-integer proof.

## Originality
The 2024 subdirect-sum formula already implies the factorization, which is expressly attributed rather than claimed as new. The inspected 2023/2025 maximal-ranked-poset paper compares interpolation choices on a *fixed* poset. The September 2026 universal result compares chain versus order polytopes for one poset. The new result compares *different* ranked posets at the same dimension and proves strict **simultaneous** face-gap majorization with a Schur-positive difference. The closest relevant paper is Freij-Hollanti–Lundström, arXiv:2312.13890, Proposition 8; that result does not give the dimension-fixed balancing law. Residual priority risk remains because this is a short consequence of their general formula and classical symmetric-function identities, and older formulas may implicitly encode it.

## Mathematical value
The X-obstruction is the natural first family in which order and chain polytopes differ combinatorially. A full hierarchy of dimension-by-dimension inequalities is a much stronger quantitative question than nonnegativity, and the unique common extremal split at fixed dimension explains how this obstruction is amplified. The sharp Schur-positive formula provides coefficientwise certificates rather than numerical extremal lists. Scope is limited to complete ranked three-level posets; no general conjecture is implied.

Self-review: passed. Independent audit: not yet performed.
