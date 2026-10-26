# Mathematical review: priced unicyclic determinant design

## Correctness — PASS

The weighted matrix-tree factorization is exact for every unicyclic graph: every tree uses every bridge and all but one cycle edge. The positive-definite reduced Laplacian is an injective linear pencil in independent conductances, making its log determinant strictly concave on connected feasible designs. Euler homogeneity fixes the KKT multiplier \(\lambda=(N-1)/B\), and the bridge equations give an exact equal-expenditure law. The absent-cycle-edge derivative yields the *if and only if* dominant-price deletion condition. For positive cycles, the normalized reciprocal-resistance variables satisfy \(x_i(1-x_i)=t c_i\); the small-root / one-large-root dichotomy and a strictly monotone scalar ratio establish existence and uniqueness. Both branches satisfy all global KKT conditions. Exact determinant comparisons and randomized numerical stress tests supplement, but do not replace, the proof.

## Originality — PASS, with stated residual risk

The closest primary material is Boyd (2006) for general convex Laplacian optimization and Osting--Brune--Osher (2012 initial preprint; Proposition 4.2 and §4) for D-optimal determinant design on weighted graph Laplacians. Theorem 4.1 in Bailey and Cameron's *Combinatorics of optimal designs* classifies unweighted unicyclic **graph topologies**, not independently priced conductances on a fixed graph. Sagnol--Harman (arXiv:1307.4953) gives general constrained D-optimal numerical machinery, not a family-specific edge-deletion frontier in its publicly inspected description. Published equal-price cycle examples are covered restrictions and are not asserted original. The full claimed parameterized allocation, arbitrary tree attachments, sharp dominant-price criterion, and one-variable exact solution are not implied by those inspected specific statements. Specialist optimal-design or electrical-network literature may nevertheless contain an equivalent parameterization; absence from searches cannot prove absolute priority.

## Mathematical value — PASS

The result completely solves a natural continuous D-optimal experiment/network-allocation problem for the infinite unicyclic graph class. It specifies every conductance uniquely under arbitrary edge prices, establishes a sharp and interpretable circumstance in which deleting a redundant cycle edge **improves** information per cost, and proves an invariant equal per-bridge expenditure independent of fringe-tree geometry. The arbitrary-cost scalar reduction and its exceptional-price closed form go beyond simple homogeneous rescaling or a finite small example. The result is directly reusable as a sharp benchmark for Laplacian log-determinant design and budget-dependent edge sparsification.

## Verification limitations

Four exact-rational determinants, 168 parameterized numerical instances, and 6,720 competing allocations were tested. These calculations cannot establish an infinite result on their own. Analytic proof relies on exact tree-polynomial factorization, strict log-determinant concavity, KKT, and scalar monotonicity. There remains historical-coverage uncertainty; no independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
