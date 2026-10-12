# Review

## Correctness

PASS. The original server-momentum update reduces exactly to a scalar second-order recurrence. The fixed-workload and two-period classifications both use the complete second-order Jury criterion. The two-period condition is necessary and sufficient, and the rational witness is independently reconstructed from the client and server updates.

Risk: only deterministic two-period switching is classified.

## Originality

PASS. The defining FedAvgM source gives the server recurrence and fixed-local-epoch experiments but no switched-workload stability result. The closest dedicated server-momentum analysis allows time-varying local work only after normalizing heterogeneous client updates by their local-step counts, and its convergence theorem assumes much smaller client steps. Focused searches of federated and momentum literature found no implication-equivalent exact criterion.

Residual risk: a generic switched-control result may contain an equivalent matrix-product calculation under different terminology.

## Value

PASS. The result exposes a sharp robustness limitation precisely at the intersection of server momentum and varying local computation. It shows that momentum can convert two individually stable workload regimes into an unstable periodic system, while vanilla FedAvg remains stable under the same local computation.

Self-review: passed. Independent audit: not yet performed.
