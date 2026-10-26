# Scientific review

## Correctness — PASS

The resistance metric on the star reduces exactly to the maximum sum of two reciprocal edge conductances. The homogeneous change of variables reduces the constrained original problem to minimizing a separable reciprocal-price objective subject to pair-sum inequalities. The proof exhausts all feasible vectors: either every normalized resistance is at most one half or exactly one exceeds one half. It verifies the boundary, the square-root stationary point, strict equality conditions, and the globally attained budget lower bound. Hence the optimizer is unique without assuming edge symmetry. Deterministic exact-matrix, constrained numerical, and competitor checks support the normalization and formulas. Numerical tests are supplementary, not an infinite proof.

## Originality — PASS (qualified)

The closest inspected primary paper is Ghosh–Boyd–Saberi (2006; 2008), which derives tree effective resistances, convexity and a semidefinite framework for minimizing maximum pairwise resistance, but does not state the unique heterogeneously priced star optimizer, the dominant-price threshold, or its nearly twofold equal-weight gap. The authors' analytical star result addresses total effective resistance under equal prices. Dedicated meaning-based searches for star resistance diameter and price-constrained maximization were also compared with indexed records, without a covering claim. This is a best-knowledge mathematical comparison rather than proof of literature-wide uniqueness. The broad convex formulation is acknowledged, and a previously unindexed equivalent calculation is a residual risk.

## Mathematical value — PASS

The maximum pairwise resistance is a natural robustness/latency design objective, distinct from average resistance. The theorem gives an exact optimizer for every positive price vector and every star size, exhibits a nonobvious equality regime despite heterogeneous prices, identifies the unique sharp price-imbalance transition, and quantifies a sharp improvement factor approaching two. It solves a complete infinite natural design family, rather than presenting a numerical example or a known-table recomputation.

## Limitations and neighboring literature

The proof applies only to fixed star graphs and linear positive unit conductance prices. The inspected conference and journal papers solve a different aggregate-resistance objective and merely formulate the maximum-resistance SDP. Independent literature review and independent proof audit have not been performed. The 2006 conference date is used as the earliest positively verified public date for the focal source, not inferred from a journal acceptance or revision date.

Self-review: passed. Independent audit: not yet performed.
