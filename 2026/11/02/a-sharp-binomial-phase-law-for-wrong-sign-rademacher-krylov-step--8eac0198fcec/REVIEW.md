# Assessment

## Correctness — PASS
The coefficient normal equation reduces its sign to \(k(x^2+\kappa y^2)+(1+\kappa)Bxy\). AM–GM gives a necessary condition on the row-product sum \(B\) and the fixed residual \(b=(\sqrt\kappa,1)\) simultaneously attains it for every row-product outcome. The binomial distribution then gives an exact probability, not an empirical estimate. The \(k=3\) endpoint, zero-denominator convention, embedded high-dimensional scope and limiting near-identity residual ratio are derived explicitly. The included checker passed 352 exact-rational enumerations, 16 floor checks, and both sides of the first phase boundary. The finite tests support but do not establish the infinite claim.

## Originality — PASS, conditional on documented literature coverage
The motivating randomized Krylov study [1] states the sketched minimal-residual objective and lists sign sketches but does not report the sharp sign-reversal binomial phase diagram in the inspected relevant sections. Güttel–Pearson [2] studies stabilizing sketched GMRES through FGMRES; Nakatsukasa–Tropp [3] provides sketch-and-solve and embedding guarantees. Gaussian sketch-and-solve [4] handles a different continuous ensemble. The exact staircase and its \(\kappa\downarrow1\) failure floor are not entailed by these inspected conclusions. Related numerical-method records with deterministic GMRES error bounds do not imply the discrete sign-sketch law. There remains an ordinary risk of older specialized calculations on sign sketches; no exhaustive claim of historical uniqueness is made.

## Value — PASS
The sharp binomial failure risk answers a natural safety question for a practical oblivious sketch distribution and identifies a persistent \(2^{-k}\) failure floor arbitrarily near identity conditioning. At \(k=3\), a specific curvature threshold changes the risk from \(1/8\) to \(1/2\); on the rare all-opposite-sign event the true residual norm tends to twice the previous norm even as the matrix becomes arbitrarily well conditioned. This exact finite-sample dimension/condition-number tradeoff is not supplied by ordinary embedding bounds and is useful for calibrating sketch confidence and safeguards. No guarantee is asserted for all residual-growth mechanisms.

## Scope and references
The theorem is restricted to one exact-arithmetic step, two diagonal active modes and iid Rademacher entries; arbitrary SPD rotations or other ensembles may behave differently. Sources: [1] arXiv:2610.34964v1, [2] arXiv:2506.18408v2, [3] arXiv:2111.00113, [4] Epperly (2024) Gaussian sketch-and-solve note. Independent priority and mathematics reviews remain open.

Self-review: passed. Independent audit: not yet performed.
