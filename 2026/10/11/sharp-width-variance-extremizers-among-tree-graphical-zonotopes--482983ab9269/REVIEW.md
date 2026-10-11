# Scientific review: sharp width-variance extremizers among tree graphical zonotopes

## Correctness — PASS

The Euclidean width is exactly the sum of the absolute root-coordinate projections. A standard Gaussian direction, normalized by its independent radius, reduces all second moments to the absolute bivariate Gaussian pair integral. Disjoint edges have zero root correlation; edges sharing one endpoint have absolute correlation \(1/2\). This gives the exact coefficient \(\delta=1/3+(2\sqrt3-4)/\pi>0\) multiplying the incident-edge-pair count. For a tree the degree excesses sum to \(n-2\); their sum of squares is minimized only by path degrees and maximized only by star degrees. The resulting exact gap, equal-volume statement, and limits follow algebraically. The standalone exact-count and finite Monte Carlo diagnostics reproduced `VERIFY_OK`; no probabilistic experiment is used as a proof.

## Originality — PASS, subject to residual priority risk

Grujić's *Counting faces of graphical zonotopes* (arXiv:1604.06931, Theorem 1.1 and Sections 2 and 5) classifies face numbers and identifies tree graphical zonotopes as combinatorial cubes; the inspected full text does not provide spherical width variance or its tree extremizers. Dall and Pfeifle's *A Polyhedral Proof of the Matrix Tree Theorem* (arXiv:1404.3876, Theorems 3 and 17) concerns zonotope volume, not width fluctuation. Padrol–Pilaud–Poullot's *Deformed Graphical Zonotopes* (arXiv:2111.12422, accessible structural treatment) develops deformation geometry, not this moment identity. Targeted searches for width variance, Gaussian graph total variation, degree-square/Zagreb descriptions and implied general zonoid correlations returned no established theorem implying this path–star classification. Classical Gaussian pair integrals and tree degree inequalities are acknowledged as ingredients rather than claimed as new. Unindexed or differently formulated prior work remains possible.

## Value — PASS

Every tree graphical zonotope has identical dimension, face vector, Euclidean volume \(\sqrt n\), and mean width, making the observed sharp difference in width fluctuations genuinely geometric rather than a trivial size normalization. The exact graph-theoretic variance invariant rigorously distinguishes tree branching, with path variances converging to a finite constant but star variances increasing linearly with vertex number. The all-graph moment formula permits wider applications to graph-indexed geometric anisotropy.

## Limits and verification

The theorem does not imply stochastic ordering, complete width laws, weighted-edge or non-Euclidean versions. Direct inspection covered the complete relevant graphical-zonotope face-enumeration paper and the matrix-tree volume treatment; a later deformation paper was inspected for its structural portions. Classical general zonoid correlation literature might independently imply the formula and constitutes a priority uncertainty. A standard-library verifier checks the finite consequences but does not establish the infinite theorem.

Same-model review: passed. Independent audit: not yet performed.
