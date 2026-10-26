# Review of the two-agent curvature–mixing frontier

## Correctness

**PASS.** The linear recurrence is exactly derived from the specified update for positive scalar curvatures and consistent gradient initialization; the cubic Schur reduction, four inequalities and exact radical boundary are proved without unverified numerical extrapolation. Initial-state directions \(v_1,v_2\) and their image have determinant \(\lambda-1\ne0\), so an unstable eigenmode cannot be invisible to all allowed initial primal data. The full identity checker reproduces the polynomial and reduction.

## Originality

**PASS, narrowly scoped.** Wang et al. (arXiv:2608.03548v1) motivate the canonical step and give a general reduced matrix and conservative heterogeneous sufficient certificate. A published signed-spectrum result for this algorithm addresses homogeneous curvature only. Tian et al. (arXiv:2607.23601v1) study different tracker update placements and worst-case function/graph classes. The combined strict necessary-and-sufficient heterogeneous two-agent criterion was not found in the searched indexed records or inspected primary texts. The external full text of one close published record was not available; its complete recoverable statement and published abstract were compared, leaving a disclosed originality risk.

## Value

**PASS.** A previously optimally fast complete-network step need not converge when the network has a sufficiently negative non-consensus eigenvalue. The exact \(\lambda=-1/3\) immunity threshold, curvature-mismatch transition, and golden-ratio terminal mixing boundary supply a sharp, mathematically motivated classification for tuning two-agent communication weights at that step. No general network or free-stepsize optimality is claimed.

## Limitations

Assumes two agents, scalar strictly convex quadratic costs, symmetric positive mixing, one fixed common stepsize and correctly initialized trackers. No independent validation. The current search cannot rule out unindexed equivalent literature, and a close published homogeneous study was not readable in its remote complete package.

Self-review: passed. Independent audit: not yet performed.
