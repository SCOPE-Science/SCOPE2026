# Independent mathematical audit

## correctness

PASS

The Jacobi reduction M_s=2/||J_s|| uses the original weighted coefficient form and all approximant zeros (the cited 2016 reduction is prior); weights give edges ((j+3)/(j+2))^(s/2). After scaling first edge to 1, b=(8/9)^(s/2) and c=(5/6)^(s/2). The first two site Schur complement yields λ-1/λ=b²m(λ), λ>1; the tail norm <=2c<1/2 for sufficiently large s and its bipartite resolvent has m=λ^(-1)+c²λ^(-3)+O(c⁴). Thus λ²=1+b²+b²c²+O(b^6), since (160/243)^s and (50/81)^s are <=(512/729)^s, giving the three requested coefficients and uniform error. Principal 2×2 and 3×3 Jacobi compressions yield exact first-degree generator-degree-one/two formulae, not a claim about higher-degree approximants. Resolvent control gives O(b²) spectral mass outside coordinates 0 and 1. Independently diagonalized 1,301×1,301 Jacobi truncations at s=16,20,32,48,64; their absolute remainders divided by specified b^6 were bounded and their quadratic gaps positive. These finite sections corroborate but cannot replace the infinite tail estimate.

## originality

PASS

The foundational 2016 Jacobi norm theorem gives zero location reduction and an intentionally nonsharp negative-weight bound; the 2021 survey explicitly asks for its exact radius and extremal generator. The audited result supplies a partial large-s asymptotic with three separate scales, not a new Jacobi reduction. No matching negative-index expansion was identified in targeted indexed research searches or the full primary mathematical passages read. Older generic Jacobi operator perturbation formulas might entail the expansion after specialization, so originality is explicitly best-knowledge.

## value

PASS

This is a motivated asymptotic partial solution to an explicitly published problem about zero-free discs and extremal generating functions. The sharp factor two improves a standard bound, the (20/27)^s scale quantifies exactly when quadratic generators cease to capture the full radius, and the spectral two-site localization describes extremal functions; not a mere high-precision number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
