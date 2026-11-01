# Scientific review

## Correctness (C): PASS

The claim fixes the sampling distribution, the entire moment target and the allowed weights. Convex hull geometry proves that the feasible second moment at fixed zero mean is the full interval between products of the closest and farthest opposite-sign sample pairs. Two unconditional order-statistic densities prove the exact finite-sample integral; two matching exponential event bounds prove the sharp large-sample rate without extrapolating from experiments. Boundary cases have probability zero for fixed \(q\in(0,1)\). The standalone exact-arithmetic checker passed \(4,800\) random rational configuration comparisons against Carathéodory enumeration and the \(n=3,4\) symbolic identities. The proof, not those samples, establishes the universal statements.

## Originality (O): PASS within evidence limits

The direct source, Neumayer–Schäfer–Ullrich, arXiv:2610.32699v1, guarantees high-probability positive quadrature for a general finite-dimensional space with an explicit sample-size sufficient bound and weights constrained near importance-sampling weights. It does not calculate the exact feasibility event for independent uniform quadratic-node sampling. Bělík–Narayan–Turnage study randomized least-squares quadrature; van den Bos–Sanderse study deterministic node insertion. Hayakawa–Lyons–Oberhauser study general random convex hull probabilities, but their inspected results do not give the two exact product tails or this sharp crossover. The convex-hull formulation is standard and receives no novelty claim. Search evidence cannot rule out all earlier specialist probabilistic computations; an independent historical literature audit remains necessary.

## Mathematical value (V): PASS

Positive quadrature is an established numerical-stability design constraint. The smallest nonlinear moment model has a nontrivial positive-weight success probability, and a precise transition between extreme-sample shortage and central unsampled gaps. The finite-sample probability and sharp exponential rate give concrete sample-budget diagnostics beyond general high-probability existence theorems. They are meaningful even absent downstream solver estimates.

## Limitations and closest literature

The result does not prescribe or compute particular weight sizes, sampling algorithms, floating-point error, nonuniform node distributions or multivariate moments. The rate holds at fixed \(q\) as the number of samples tends to infinity. The reviewed direct primary full texts support, but cannot certify, absence of equivalent historical statements. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
