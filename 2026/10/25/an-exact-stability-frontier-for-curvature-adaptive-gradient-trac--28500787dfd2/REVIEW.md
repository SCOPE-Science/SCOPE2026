# Review

## Correctness

PASS. The local-gradient estimate equals the exact scalar curvature whenever the primal difference is nonzero; the stated initialization therefore holds the steps at \(q/h_i\). The tracker invariant reduces the consensus trajectory to the stated second-order recurrence. The quadratic Schur/Jury inequalities give a necessary-and-sufficient stability test, and `verify.py` checks the characteristic polynomial and boundary examples symbolically and numerically.

## Originality

PASS, narrowly scoped. The primary AdGT source proves a sufficient generic convergence condition, not the exact necessary-and-sufficient two-agent boundary for reciprocal-curvature steps. The closest indexed graph-tuning result concerns homogeneous local curvature and a common step. Classical gradient-tracking results use common fixed steps and do not state this heterogeneous recurrence. Residual risk remains because the closest indexed record was only available as a summary and an unindexed equivalent could exist.

## Value

PASS. The formula gives a sharp tuning boundary for the minimal connected network and separates a flip-mode loss of stability from a unit-circle pair as curvature mismatch increases. This supplies an exact diagnostic for the role of heterogeneous local curvature that a conservative general-network bound does not provide.

Closest literature: arXiv:2504.15196; arXiv:1605.07112; indexed homogeneous graph-tuning record 2026/10/4/SCOPE-exact-sign-aware-graph-specific-tuning-for-homogeneous-distribut--4bef30512fd6.

Limitations: scalar quadratics, two agents, complete averaging, and the specified update only. No general-network or nonlinear claim is made.

Self-review: passed. Independent audit: not yet performed.
