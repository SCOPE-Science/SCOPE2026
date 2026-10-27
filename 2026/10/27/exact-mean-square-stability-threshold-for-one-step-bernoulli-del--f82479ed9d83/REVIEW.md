# Review

## Correctness — PASS

The update matrices and second-moment recurrence are derived explicitly. The characteristic-polynomial value at \(1\) proves necessity, including the boundary case. In the strict region, the explicit matrix \(P\) satisfies \(P-\mathbb{E}[A_d^\top P A_d]=I\); its leading principal minor and determinant are positive, yielding exponential mean-square decay. The included exact-rational checks corroborate the algebra but are not used as a substitute for the proof.

## Originality — PASS

The closest inspected full-text source, Arjevani, Shamir, and Srebro, treats a fixed delay. The present update uses an iid mixture of zero and one-step delay, and its exact frontier for intermediate delay probability is not implied by the fixed-delay endpoint cases. Related exact delay-distribution results located in the literature search concern different algorithms and different state recurrences. A plausible later paper on delayed-SGD generalization was available only as an abstract, so this is retained as a residual literature-overlap risk rather than treated as excluded.

## Value — PASS

The theorem provides a sharp, distribution-aware step-size ceiling for asynchronous optimization on positive-definite quadratics. The exact threshold is useful for selecting a stable step size and for benchmarking more conservative bounds that assume a worst-case delay.

## Closest literature and limitations

The fixed-delay baseline is Y. Arjevani, O. Shamir, and N. Srebro, “A Tight Convergence Analysis for Stochastic Gradient Descent with Delayed Updates,” ALT 2020; arXiv:1806.10188v1. A later related source, arXiv:2308.09430v1, was inspected only at the abstract level because full-text retrieval failed. The theorem applies only to iid delays supported on \(\{0,1\}\), deterministic gradients, and a quadratic objective; it does not cover correlated delays, multi-step delay distributions, gradient noise, or nonlinear objectives.

Self-review: passed. Independent audit: not yet performed.
