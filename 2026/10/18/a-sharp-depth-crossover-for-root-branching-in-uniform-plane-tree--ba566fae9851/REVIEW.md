# Scientific review

## Correctness — PASS

The exact covariance follows from rooted-plane-tree decomposition and formal Lagrange inversion: \(T=z/(1-T)\), \(A_h=T(T/(1-T))^h\), and the independently root-degree-marked identity \(B_h=A_h+2A_{h+1}\). Explicit coefficient evaluation produces the sign factor \(n+1-h-2h^2\); a log-product expansion gives the limit at depths of order \(\sqrt n\). Edge cases include \(n=2\), the highest possible depth \(h=n-1\), and the deterministic depth-zero population. Direct exhaustive rational-arithmetic checks over 82,499 trees and 45,024 assertions supplement, but do not substitute for, the symbolic proof.

## Originality — PASS, qualified by residual priority risk

The full-text 2011 Janson survey supplies conditioned Galton–Watson/plane-tree models and root-degree marginal laws. The 2003 Janson paper establishes mixed path-length/Wiener moments, not root-degree versus every generation. The full later distance-profile article includes root-degree-conditioned forests and limiting profiles but does not explicitly provide this exact finite mixed-moment identity or its depth-dependent sign classification. Searches covered aliases for profile, generation size, level width, root offspring, degree–profile covariance, and the exact polynomial. None of the consulted statements implies the displayed finite covariance without an additional calculation. Earlier general generating-function technology may nonetheless encode this result; independent historical-priority determination remains open.

## Value — PASS

Root offspring and depth-profile widths are natural complementary statistics of a random tree. A complete finite-size sign theorem, with isolated exact zeros and a continuum crossover at \(t=1/\sqrt2\), resolves a coherent structural dependence question rather than an arbitrary statistic: extra first-generation branching raises shallow population but has the opposite association with deep population under total-size conditioning. This sharp dependence reversal is not determined by separately known root-degree and profile marginals.

## Closest literature and scientific limitations

Sources: S. Janson, arXiv:1112.0510; S. Janson, DOI:10.1002/rsa.10074; *The distance profile of rooted and unrooted simply generated trees* (Cambridge full-text HTML); S. Wagner, DOI:10.1017/S0963548314000443 (abstract). The fourth reference was not inspected as full text; broad earlier frameworks may yield the formula as an unstated special computation. The asymptotic limit is only pointwise in depth scale, not a uniform quantitative bound. No independent scientific review is asserted.

Self-review: passed. Independent audit: not yet performed.
