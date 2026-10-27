# Scientific review

## Correctness — PASS

For the specified update, \(\Delta_i\) is exactly the indicator that colour \(i\) appears in the two draws, so \(\mathbb E[\Delta_i\mid\mathcal F_n]=2x_i-x_i^2\) and \(\mathbb E[\Delta T\mid\mathcal F_n]=2-\sum_i x_i^2\). Expanding the bounded random denominator gives the stated drift with a uniform \(O(T_n^{-2})\) remainder. Cauchy–Schwarz yields \(G\ge0\), with equality exactly at uniform-on-subset states. The weighted Lyapunov argument forces the state to converge to one of these finitely many equilibria. The logarithmic-coordinate argument then excludes every proper subset; it uses \(U_i(n)\to\infty\), a conditional variance bound \(O(T_n^{-1})\), and a martingale strong law. The proof explicitly distinguishes the equilibrium classification from the necessary boundary-exclusion step.

## Originality — PASS, with priority risk

Lasmar–Mailler–Selmi (arXiv:1611.09090; published 2018) treat balanced multicolour urns and non-balanced two-colour urns, and explicitly identify the non-balanced multicolour extension as open. The exact rule here is non-balanced because its total increment is one or two, and non-affine because its expected color increment is quadratic. The affine multicolour urn paper (arXiv:2403.12423) treat a balanced affine multicolour class. Dahiya–Sahasrabudhe (arXiv:2308.12528) treat graph-coupled two-colour urns, not this single urn with \(d\ge3\) colours. Searches of the research record and prior accessible ledgers found no exact match. A distinct formulation of the same update may exist, so priority is not claimed as independently certified.

## Value — PASS

This is a complete almost-sure limit classification for a natural duplicate-suppressed sampling rule, rather than merely a local stability calculation. The variable-total, nonlinear multicolour setting is outside the balanced multicolour theorem and the one-dimensional non-balanced theorem in the closest inspected work. The proof shows why a simple Lyapunov function identifies several possible boundary equilibria and why a separate logarithmic argument is needed to show that every initially present colour survives in positive limiting proportion.

## Closest literature and residual risk

The most relevant primary source is Lasmar–Mailler–Selmi, especially its model definition and discussion of the non-balanced multicolour problem. The affine multicolour paper is excluded by its fixed total addition and affine conditional expectation assumptions. The graph-based two-colour paper has a different state space. An older or differently named model could still contain the exact update; targeted searches did not find one.

Self-review: passed. Independent audit: not yet performed.
