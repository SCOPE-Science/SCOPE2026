# Universal inverse-time ceiling for open-chain quantum-walk spatial entanglement

## Finding

For the independent distinguishable-walker model in Goyal and Chandrashekar, write \(p_{ij}\) for the probability that walker \(i\in\{1,\ldots,M}\) occupies lattice site \(j\) after \(t\) discrete-time quantum-walk steps. Use the subsystem count
\[
L=2t+M+1
\]
that appears in their Meyer--Wallach expression. Their configuration law states that the probability of a bit pattern \(\ell=(\ell_1,\ldots,\ell_M)\in\{0,1}^M\) at site \(j\) is the product of the corresponding presence/absence probabilities. It follows exactly that
\[
\operatorname{tr}\rho_j^2
=\prod_{i=1}^M\left[p_{ij}^2+(1-p_{ij})^2\right].
\]
Therefore the source's spatial Meyer--Wallach quantity obeys
\[
E_{\mathrm{MW}}(t)
\le
\frac{2^M}{2^M-1}\frac{2}{L}
\sum_{i=1}^M
\left(1-\sum_j p_{ij}^2\right)
\le
\frac{2^M}{2^M-1}\frac{2M}{2t+M+1}.
\]
In particular, at fixed \(M\), this open-chain quantity necessarily vanishes as \(O(t^{-1})\), for every allowed coin choice and every detailed one-particle profile covered by the independent-walker/product-distribution model.

## Assumptions and scope

The result uses exactly the probabilistic product structure stated in Eq. (26) of arXiv:0901.0671 and the source's site-mode Meyer--Wallach normalization in Eq. (24). The walkers are distinguishable and noninteracting, as in the source's many-particle model. For each walker, \(p_{ij}\ge0\) and \(\sum_j p_{ij}=1\). No ballistic-scaling assumption, Hadamard-coin assumption, symmetry assumption, continuum approximation, or large-
\(t\) approximation is used.

The theorem concerns the open-chain prescription whose subsystem count grows with \(t\). It does not assert the same decay on a fixed closed cycle, where the source keeps the number of lattice subsystems fixed.

## Proof

At one site \(j\), label a configuration by \(\ell=(\ell_1,\ldots,\ell_M)\in\{0,1}^M\). Put
\[
a_{ij}^{(1)}=p_{ij},
\qquad
a_{ij}^{(0)}=1-p_{ij}.
\]
The product law in the source gives
\[
q_{j,\ell}=\prod_{i=1}^M a_{ij}^{(\ell_i)}.
\]
Since the reduced state \(\rho_j\) is diagonal in this configuration basis,
\[
\operatorname{tr}\rho_j^2
=\sum_{\ell\in\{0,1}^M}q_{j,\ell}^2
=\prod_{i=1}^M
\left[p_{ij}^2+(1-p_{ij})^2\right].
\]
Define
\[
x_{ij}=2p_{ij}(1-p_{ij}),
\qquad 0\le x_{ij}\le\frac12.
\]
Then
\[
1-\operatorname{tr}\rho_j^2
=1-\prod_{i=1}^M(1-x_{ij})
\le\sum_{i=1}^M x_{ij},
\]
where the inequality is the elementary union bound \(1-\prod_i(1-x_i)\le\sum_i x_i\) for \(0\le x_i\le1\). Summing over sites gives
\[
\sum_j\left(1-\operatorname{tr}\rho_j^2\right)
\le
2\sum_{i=1}^M\sum_j p_{ij}(1-p_{ij})
=2\sum_{i=1}^M\left(1-\sum_j p_{ij}^2\right)
\le2M.
\]
Substitution into the source's Eq. (24) proves both displayed bounds. Since \(M\) is fixed while \(L=2t+M+1\to\infty\), the final \(O(t^{-1})\) statement follows.

## Verification

The standalone script `verify_spatial_decay.py` independently enumerates all \(2^M\) site configurations on an exact rational grid for \(1\le M\le5\), compares the direct purity sum with the factorized expression, and checks the finite-site inequality. It also tests normalized rational position distributions and the global inverse-participation-ratio bound. The replay output is:

`VERIFY_OK`

`factorization_grid_checks = 19607`

`global_distribution_checks = 3`

These computations are supplementary. The theorem for arbitrary \(M\) and \(t\) is established by the analytic factorization and inequality above.

## Relationship to prior work

Goyal and Chandrashekar introduce the independent many-particle walk, the site-mode Meyer--Wallach quantity, the diagonal local density matrix, and the product configuration probabilities. They numerically observe that on an open chain the spatial entanglement first rises and later decreases as the number of occupied lattice positions grows, while a fixed closed chain behaves differently. The source does not provide the factorized purity formula above or a coin-independent finite-time upper bound.

A later two-walker study, arXiv:2203.00873, investigates spatial entanglement under exchange-symmetry choices and post-selection. It addresses a different two-walker symmetry problem and does not supply the all-
\(M\) Meyer--Wallach inverse-time ceiling stated here in the inspected material.

## Limitations

The bound is tied to the source's independent-walker product law. It need not hold for interacting walkers, initially correlated particle positions, or alternative spatial-entanglement measures. The upper bound is not claimed to be sharp for every coin or initial condition, and no matching lower bound is asserted. The source's subsystem count \(L=2t+M+1\) is used as printed; this result does not audit indexing conventions outside the accepted claim.

## References

1. S. K. Goyal and C. M. Chandrashekar, *Spatial entanglement using a quantum walk on a many-body system*, arXiv:0901.0671, first public 6 January 2009; *Journal of Physics A: Mathematical and Theoretical* 43 (2010) 235303, DOI: 10.1088/1751-8113/43/23/235303.
2. I. Y. Muhammad, T. Deesuwan, S. Yoo-Kong, S. Tangwancharoen, and M. Tanasittikosol, *Spatial entanglement between two quantum walkers with exchange symmetric coins*, arXiv:2203.00873; *Physics Letters A* 521 (2024) 129758.
