# Scientific review

## Correctness — PASS
The proof reconstructs the conditional law by independent column states of probabilities \(t,t,1-2t\) and excludes two disjoint row-empty events of probability \(t^n\) each. This gives all one- and two-edge moments without numerical inference. Orthogonal symmetric/antisymmetric row modes and constant/contrast column modes yield four explicitly positive covariance eigenvalues. Inversion gives the claimed precision entries. The non-obvious strict sign of the same-column precision is proved by \(AB-(n-1)uh^2=A^2+(n-1)h(2tA-uh)>0\). Exact rational direct enumeration and matrix multiplication passed 2250 assertions for \(2\le n\le6\) at three distinct fugacities. Full-size validity is from the algebraic argument rather than the finite checker.

## Originality — PASS with explicit priority risk
The closest primary papers are Chen–Liu–Vigoda (arXiv:2106.03366), Eppstein–Frishberg (arXiv:2111.03898), and Chen–Gu (arXiv:2304.14289). Their inspected definitions and theorems concern edge-cover Gibbs sampling, zero-free conditions, spectral independence and mixing. These claims neither state nor algebraically imply the exact \(K_{2,n}\) three-orbit inverse-covariance signs. Related published mathematical findings about occupied-box precision concern iid occupancy rather than edge-cover constraints. Searches for exact weighted-cover covariances, precision, partial correlations, and related aliases did not yield an equivalent statement. Existing partition-function techniques could nevertheless contain an overlooked elementary specialization; historical priority is not conclusively established.

## Value — PASS
Conditioning on every vertex being covered creates competing local endpoint constraints and global row constraints. Their net effect cannot be read off from independent-edge probabilities: incident edges repel, vertex-disjoint edges attract, and the same strict sign pattern survives regression on *all other edges*. The complete all-parameter precision law is a structural dependence statement for a basic bounded-treewidth but unbounded-degree graph family, not a collection of isolated small-case computations.

## Limitations
No statement about non-linear conditional independence, full association, graph families with a larger left part, or arbitrary vertex degree thresholds is claimed. Historical priority and an independent audit remain open.

Self-review: passed. Independent audit: not yet performed.
