# Mathematical assessment

## Correctness
The equilibrium proof exhausts boundary and interior states. Writing the opinion difference as \(s\), it reduces unequal-opinion equilibria to \(\rho=s^2/(a-s)^2\). The discriminant \(s(4a-3s)\) yields the exact cutoff \(\rho=16\). A symmetry decomposition proves the polarized-state eigenvalue crossing. At the rational parameter example, exact characteristic polynomials and strict Routh–Hurwitz determinants prove three exponential local attractors and positive eigenvalues for the two additional equilibria. `verify.py` is reproducible using SymPy. No inference from finite simulations supports a global claim.

## Originality
The closest parent result is Alutto et al., arXiv:2603.24381v1, whose full HTML has been examined. Its implicit cubic equations and conservative contraction theorem neither state the complete two-person count nor the sharp ratio-16 transverse stability transition. A later same-author paper, arXiv:2606.05825, has a different multiplicative replicator rule. Related 2021 nonlinear-potential work studies a different ODE and was available only at abstract level. Model-specific and semantic literature/record searches did not identify a stronger result that directly implies the complete finding. A hidden equivalent reduction remains a genuine risk.

## Mathematical value
The smallest mutual social network already exhibits a sharp count/stability transition and three locally attracting states at an exact parameter point. This gives a tractable test case for understanding the interplay of initial conviction, social pressure, and dynamic leadership, and directly sharpens a stability-boundary question left conservative in the source.

## Scope and limitations
Only equilibria in the fixed-anchor autonomous system are exhaustively classified. Attracting equilibria are local, and proof does not assert all three basins intersect the narrower physical initial-opinion plane. The full dynamics, critical center manifold at equality, and empirical relevance remain open.

Self-review: passed. Independent audit: not yet performed.
