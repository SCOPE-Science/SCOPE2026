# Review

## Correctness

PASS. The source vanilla-SGD FedNova update is reconstructed exactly. At the chosen client step, every local quadratic is solved after one gradient evaluation, so all later local gradients vanish. The normalized client directions and the server round therefore reduce to an exact affine scalar map. Its multiplier, fixed point, sharp stability interval, and the \(1:6\) witness follow by elementary exact algebra.

Scientific risk: the threshold is specific to the source default server scale and the locally exact client step.

## Originality

PASS. The defining FedNova source gives normalized aggregation and a convergence theorem with a horizon-dependent shrinking learning rate. The closest later source, FedShuffle, explicitly observes that FedNova diminishes the weight of a client making more progress and allows smaller theoretical local steps. The inspected literature does not state the exact fixed point, the \(3+2\sqrt2\) local-step-ratio boundary, or divergence with exact client-local solves.

Residual risk: a generic federated local-update appendix or unindexed note may contain the same scalar specialization.

## Value

PASS. The result exposes a sharp systems-heterogeneity boundary in the mechanism FedNova was designed to control. A global round can diverge solely from a \(1:6\) local-step imbalance even though every client locally reaches its minimizer after one step. The exact fixed point also quantifies how finite constant steps reintroduce an inverse-progress weighting before instability occurs.

Self-review: passed. Independent audit: not yet performed.
