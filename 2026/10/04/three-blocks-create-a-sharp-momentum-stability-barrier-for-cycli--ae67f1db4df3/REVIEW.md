# Independent mathematical audit

## correctness

PASS

Exact block minimization reconstructs the displayed three-by-three cyclic sweep matrix. Its nonzero eigenvalues have product c^3 and real part c^2(3-c)/2 and form a conjugate pair for 0<c<1. Applying Schur--Cohn to the lifted modal quadratic gives exactly the factor (1-c)P_c(alpha), while the remaining zero sweep eigenvalue contributes only zero lifted roots. The derivative bracket of P_c is convex in alpha and negative at both endpoints, hence P_c is strictly decreasing on [0,1]. The unit-momentum value factors as (c-1)(7c^4+2c^3-3c^2-2c-1), whose quartic has one positive root by Descartes and endpoint signs. The two-block Jury conditions are strictly satisfied throughout the parameter rectangle. The inspected verifier and an independent symbolic reconstruction reproduced the characteristic polynomial, factorization and numerical threshold.

## originality

PASS

Chambolle--Pock establish accelerated alternating minimization in the two-block setting and explicitly discuss the difficulty of extending such acceleration to general deterministic alternating schemes, but do not give this three-block momentum boundary. Hong--Yavneh supply the generic Nesterov/stationary-iteration modal recurrence and complex-spectrum framework, which is treated here as prior; their inspected results do not state the exact cyclic-sweep spectrum or P_c phase diagram for this family. The 2025 cyclic-block paper studies a different auxiliary-sequence per-coordinate acceleration. Targeted Resultary search for cyclic alternating minimization with fixed global momentum returned related iterative-method records but no implication-equivalent three-block threshold.

## value

PASS

The theorem identifies a sharp structural transition in a natural acceleration attempt: the same global fixed momentum that is unconditionally stable for the two-block family develops a complete algebraic instability boundary at three blocks. This gives a compact adversarial benchmark for deterministic cyclic acceleration and directly addresses a limitation highlighted by the motivating two-block literature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
