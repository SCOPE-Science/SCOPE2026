# Scientific review

## Correctness — PASS

The source's Theorem 3(ii) and Corollary 8 reduce the full, unrestricted largest-area embedded-isosceles problem in a Euclidean triangle to three canonical constructions; the three relative areas are reconstructed directly from a coordinate construction. At fixed normalized triangle slack, both increasing branches and the one decreasing branch have explicitly signed derivatives, so their crossing gives a unique global minimizer. The two candidate crossing equations, quartic transition, and nonzero one-sided derivative jump follow by exact algebra. The globally sharp linear coefficient follows from an explicit polynomial with four strictly positive radical coefficients and an implicit-function boundary derivative. The standalone checker independently verifies these new algebraic identities and direct-coordinate constructions. No finite experiment is used as an infinite proof.

## Originality — PASS (provisional historical priority)

Closest antecedent: Á. Ambrus, M. Csikós, G. Kiss, J. Pach and G. Somlai, *Optimal Embedded and Enclosing Isosceles Triangles* (arXiv:2205.11637, 2022), Theorem 3(ii) and Corollary 8. That result is stronger in the sense that it determines the best special candidate separately for every given triangle; it is used as a premise here. It does **not** give the sharp infimum subject to a fixed normalized triangle-inequality slack, uniqueness of the worst host at each slack, the quartic transition between active constructions, the derivative jump, or the optimal global stability slope. These require an additional constrained minimax analysis. The 2020 *Minimum Area Isosceles Containers* theorem concerns **enclosing**, rather than embedded, triangles; its sharp factor \(\sqrt2\) is acknowledged without assuming a duality principle. Targeted published-mathematics searches did not reveal an equivalent refinement. A specialized earlier inequality or a derivation not indexed by the searches remains a residual originality risk.

## Mathematical value — PASS

This result converts an already useful pointwise geometric construction theorem into the **complete shape-robust guarantee** at a natural measure of triangle nondegeneracy: normalized slack of the longest-side triangle inequality. It identifies the unique worst similar shape at every allowed slack, shows a genuine change of active geometric mechanism at one algebraic threshold, and gives a strict optimal linear lower improvement over the limiting universal \(1/\sqrt2\) guarantee. The sharp threshold and slope are structural, not a tiny numerical gain or an arbitrary one-off example.

## Scope and limitations

The source's pointwise classification is not new and the quantitative refinement must not be represented as an independent geometric embedding classification. The statement excludes zero-area host triangles, non-Euclidean metrics and general convex bodies. Exact formulae do not establish finite-precision sensitivity or independent historical priority.

Self-review: passed. Independent audit: not yet performed.
