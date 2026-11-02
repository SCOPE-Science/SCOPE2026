# Scientific review

## Correctness — PASS
The wheel's hub-grounded Laplacian uniquely determines all edge conductances, making log determinant strictly concave in individual weights on connected feasible designs. Dihedral invariance therefore yields the unique globally symmetric optimum. Fourier diagonalization and an exact root-of-unity product reduce its determinant to a scalar. A rational derivative identity, strict monotonicity of the scalar root map and an exact finite-size identity prove the price threshold, optimizer and asymptotic scaling without extrapolating finite computations. The standalone verifier checks 2,725 exact identities/determinants and 2,092 supplementary numerical instances/competitors; the theorem rests on the proof.

## Originality — PASS, with historical overlap risk
The prior published wheel Löwner-ellipsoid result explicitly solves the cost-equal D-optimal instance \(r=1\), including \(2-t_m\sim18\,2^{-m}\). That specialization is covered and is **not** asserted to be original. General graph D-optimality, the matrix-tree theorem and root-of-unity product methods are also known. The assessed contribution is the exact sharp cost-ratio screening boundary \(r=2\), unique all-price optimum and price-dependent exponential law, not implied by the inspected earlier wheel equal-cost statement or by prior wheel designs optimizing other objectives. Search cannot certify historical uniqueness; specialist continuous experimental-design publications may contain equivalent price-parametric conclusions.

## Value — PASS
The result answers a concrete conductance-budget design question with a complete decision rule for whether a publicly available edge class deserves **any** investment, despite the graph remaining connected without that class. The sharp transition \(Q/P=2\) is independent of wheel size, and the exact price-dependent finite-size law quantifies convergence to large-network optimal allocations. These are motivated design properties beyond the already-known equal-price baseline.

## Closest literature and limitations
Khosoussi et al. (arXiv:1604.01116v1, 2016) study weighted spanning-tree optimization mainly through edge-selection algorithms. The published October 2026 wheel symmetric-edge-polytope Löwner ellipsoid result covers the equal-price D-optimal case. Suliman–Weinstein (2023) discuss general graph Lewis-weight and ellipsoid formulations; Boyd (2006) provides general Laplacian convex optimization background. No claim is made for arbitrary within-orbit prices, integer edge selection, non-wheel graphs, or joint asymptotic limits as the price ratio approaches an endpoint. Independent specialist verification and exhaustive historical priority review remain open.

Self-review: passed. Independent audit: not yet performed.
