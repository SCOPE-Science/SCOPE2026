# Self-review

**Correctness — PASS.** The exact score equivalence \(|a_{ij}|^2\le\varepsilon(|d_i-d_j|+\varepsilon)\) feeds a positive-semidefinite decomposition indexed by the current nonzero edges. The determinant estimate is valid at repeated diagonals and zero determinant. Upper and lower extreme eigenvalue enclosures apply to every principal submatrix; interlacing then compares *each* ordered eigenvalue with the corresponding ordered diagonal. The complete bipartite family makes the \(\Delta^2\) coefficient asymptotically necessary, even after a positive-definite shift. Deterministic numerical tests support, but do not prove, the universal statement.

**Originality — PASS, subject to independent bibliographic assessment.** Shao and Nakatsukasa introduce the score and obtain \(2n(n-1)\varepsilon\); this paper supplies the stronger optimal maximum-degree law \(\Delta^2\varepsilon\), which the dimension-dependent estimate does not imply. The Li–Li block perturbation bound and graded multiple-eigenvalue literature supply components of the background but do not directly establish the stated graph-degree all-index theorem. Matrix-localization literature might contain an equivalent general statement; the search was bounded and cannot rule this out.

**Mathematical value — PASS.** Sparse matrices can have order \(n\) arbitrarily large while retaining degree \(\Delta\) bounded, so the result changes the usable accuracy certificate from quadratic-in-size to size-independent. The matching extremal construction supplies a sharp obstruction, not only an improved estimate.

**Closest literature and limitations.** Main comparison: arXiv:2607.23187v1, Section 3.1, Theorem 1; Li and Li (2005); Li, Nakatsukasa, Truhar and Wang (2012). The proof concerns the current support graph, exact-arithmetic scores and absolute eigenvalue accuracy. It does not imply runtime gains, floating-point guarantees or sparse support preservation under Jacobi rotations. The full text of every potentially relevant older componentwise perturbation publication was not accessible for complete comparison.

Self-review: passed. Independent audit: not yet performed.
