# Scientific assessment

## Correctness — PASS

The proof solves the exact two-dimensional Lyapunov equation for a positive-definite drift, differentiates an explicit rational variance, and proves the number and type of critical points for all positive-semidefinite noise covariance matrices. Its delicate step, \(C\ge0\Rightarrow A\ge0\), is proved by the covariance determinant bound and a monotone convex polynomial. The inability of both patches to have variance minima follows separately from the negative-semidefinite trace derivative. The independent-noise threshold, boundary cases, and radical example were recomputed by the included symbolic verifier. Finite parameter checks supplement rather than replace the all-parameter proof.

## Originality — PASS (with residual risk)

Closest indexed and literature results address spatial synchronization, nonlinear extinction/persistence, or aggregate environmental-dispersion response rather than this exact local stationary-variance shape classification with arbitrary correlated forcing. The earlier aggregate two-patch variance claim is logically distinct: in the new witness its regional variance is constant but its local variance has a strict finite minimum. Primary mathematical sections of Colombo–Anteneodo (arXiv:1503.08168) and Hening–Nguyen–Yin (arXiv:1605.02027) were inspected. The full Lande–Engen–Sæther (1999) article was not accessible; there remains a risk that an equivalent local covariance statement appears in that paper, another stochastic metapopulation study, or OU literature under another formulation.

## Value — PASS

Local-patch variability and regional aggregate variability give different ecological management signals. The theorem gives a complete, parameter-robust answer for the smallest spatial system: a habitat's risk proxy cannot have an intermediate maximum, only one habitat can have an optimal finite dispersal intensity, and the exact criterion is an interpretable ratio of local noise strengths and return rates. The example where aggregate variance is unchanged while a single patch has a sharp optimum demonstrates a consequential information loss from regional-only assessment. This is an exact model-specific result, not a prediction of nonlinear extinction risk.

Self-review: passed. Independent audit: not yet performed.
