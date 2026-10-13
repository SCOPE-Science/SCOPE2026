# Review

## Correctness

PASS. The two client differences and their average follow directly from one local gradient step. Substitution into the published server rule gives the exact odd piecewise-rational map. Its fixed-point derivative yields the sharp threshold, and solving \(T(x)=-x\) gives the exact symmetric cycle. Differentiating at that cycle gives the claimed local-attraction interval. The exact witness is independently replayed.

Scientific risk: only local stability and local cycle attraction are classified; no global basin theorem is claimed.

## Originality

PASS. The defining FedExP paper already reports oscillating loss, recommends averaging the last two iterates, warns that update cancellation can make the server step blow up, and studies sensitivity to \(\epsilon\). Those facts are treated as prior work. The surviving claim is the exact underparameterized stability switch, the attracting nonzero two-cycle, and the exact-local-solve separation from FedAvg. The closest later extrapolation theory focuses on interpolation and does not imply this phase boundary.

Residual risk: an unindexed dynamical-systems analysis of FedExP may contain an equivalent scalar calculation.

## Value

PASS. The result turns a practical safeguard parameter into a sharp mathematical stability scale. It distinguishes transient oscillation from a stable periodic orbit and shows that extrapolation can destroy a one-round exact FedAvg solve purely because heterogeneous client updates cancel near the global optimum.

Self-review: passed. Independent audit: not yet performed.
