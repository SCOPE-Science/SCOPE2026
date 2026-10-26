# Self-review

## Correctness — PASS

The theorem has a precise domain \(n\ge4\), \(r,B>0\), and independently chosen nonnegative edge conductances. The grounded log determinant is strictly concave because the edge-weight-to-matrix map is injective, so averaging under the two endpoint and residual-vertex symmetries is sound. The four eigenspaces give \(\tau=b[2a+(n-2)b][2b+(n-2)c]^{n-3}\) exactly. Solving the three-class KKT equations gives all positive weights below \(r_c=(n-1)/(n-2)\) and a single inactive edge at and above it. The inactive-edge derivative inequality is exact, and strict concavity proves global uniqueness. Exact matrix-tree and full-edge KKT checks in `verify.py` corroborate, but do not substitute for, this proof.

## Originality — PASS, with residual risk

Osting–Brune–Osher (arXiv:1207.6430, complete available text inspected) give the broader pairwise-ranking Laplacian D-optimal criterion, not the explicit one-price complete-graph optimizer or its threshold. Harman–Benková (arXiv:1408.2698, complete available text inspected) develop generic cost-constrained D-optimality and removal conditions, but no explicit exceptional-edge complete-graph solution. Ghosh–Boyd (2006) covers symmetry reductions for spectral graph optimization rather than the present determinant price law. Prior related unicyclic and complete-bipartite design results do not imply the \(K_n\) one-edge solution for \(n\ge4\). Exact novelty is not guaranteed by a literature search; a specialized optimal-design precedent remains possible.

## Mathematical value — PASS

The objective measures Fisher-information determinant and weighted spanning-tree redundancy in an all-pairs comparison network. The threshold \(1+1/(n-2)\) is a sharp active-set transition: for large networks, even a small marginal price premium removes one otherwise redundant comparison while all other weighted edges remain active. The theorem gives a unique allocation across every edge, not merely a threshold or a computational instance, and an exact optimal determinant in both regimes. This is a natural, nontrivial complete classification under one heterogeneity parameter rather than an arbitrary numerical slice.

## Scope and remaining risks

The proof does not cover several exceptional prices, integer trial counts, or hard lower bounds on edge conductances. It explicitly acknowledges the classical matrix-tree, strict-concavity, and equivalence-theorem machinery. Full scholarly priority and publication-worthiness require independent specialist review.

Self-review: passed. Independent audit: not yet performed.
