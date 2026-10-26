# Scientific review

## Correctness — PASS

The scheme is exactly the first-order positive exponential update of Bréhier and Cohen, with \(F=-a\), \(f(x)=\sigma x/(1+x)\), and \(f'(x)g(x)=\sigma^2x^2/(1+x)^3\). The bounded derivatives and linear growth give finite moments for the original SDE. A direct normal integral establishes the conditional \(p\)-moment criterion. The unique interior maximum at \(x=2\), positive density of the first iterate at that point, and quadratic contact at the endpoint complete both halves of the sharp classification. The proof separately addresses the exact equality case and moment persistence. Symbolic and numerical checks reproduce all critical identities; they are not substituted for proofs of divergence.

## Originality — PASS, with residual bibliographic risk

The 2026 source itself derives the normal exponential-moment identity and a sufficient small-step bound (Proposition 9); those are explicitly credited. The new result is the exact necessary-and-sufficient frontier for all positive initial states after two steps in a smooth, linearly growing nonlinear example, including a subtle critical case in which almost every conditional moment is finite but the unconditional moment diverges. The same method and statement were compared with accessible literature and mathematical research records. No equivalent complete published claim was identified, but further specialized work on exponential-of-quadratic Gaussian tails may exist.

The companion 2026 bounded-domain paper controls a different construction and works on a bounded state space. The earlier GBM-based exponential integrator and log-transformed truncated Euler method do not entail this specified quadratic-exponential moment threshold. The identity underlying the proof is elementary and pre-existing, so originality rests entirely on its sharp, global, two-step consequences.

## Mathematical value — PASS

Numerical moments and positivity can be essential diagnostics in SDE approximation. The theorem pinpoints the exact timestep beyond which a strictly positive simulation of an entirely well-behaved Lipschitz SDE has infinite expected numerical values. The boundary persists even when the first step has finite moments, so a check of a single timestep or finite Monte Carlo sample can miss the pathology. This is a substantive limitation on structural reliability, not a normalization or one-instance arithmetic check.

## Risks and scope

The claim addresses exact Gaussian increments, a scalar saturating diffusion, constant steps, fixed finite \(p\ge1\), and the source's first-order method. There is no theorem for alternate numerical methods, truncated increments, or the behavior of finite-sample estimators. Bibliographic searches cannot establish exhaustive uniqueness.

Self-review: passed. Independent audit: not yet performed.
