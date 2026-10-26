# Scientific review: four-point Sobolev stability of isotonic regression

## Correctness — PASS

The exact domain is the four-point real increasing-sequence cone, ordinary Euclidean isotonic least squares, and the quadratic perturbation norm \(\|z\|_\gamma^2=\|z\|_2^2+\gamma\sum_{i=1}^3(z_{i+1}-z_i)^2\) with \(\gamma>0\). The proof verifies eight possible consecutive pooling partitions; every partition has a nonempty open data cell. The global map is a continuous piecewise-linear selection of its block-averaging matrices, so the global Lipschitz constant is the maximum matrix norm. Exact generalized characteristic determinants and rational comparisons yield the two formulas and the unique crossing at \(\gamma=1/2\). The degree-bounded interpolation checker certifies the requisite polynomial identities over all parameters, rather than extrapolating from a finite numerical sample. Two explicit rational input pairs independently demonstrate exact attainment at distinct couplings. The universal open-cell argument proves attainment at all positive couplings.

## Originality — PASS with residual risks

The closest published contraction theorem of Yang and Barber (arXiv:1706.01852) characterizes **when** ordinary isotonic projection is contractive in an arbitrary seminorm via the neighbor-averaging condition; it neither computes this noncontractive Sobolev modulus nor distinguishes the pooling patterns across a coupling threshold. The full texts of Yeganova–Wilbur (2009, DOI:10.1007/s10957-008-9477-0) and Németh–Németh (arXiv:1503.08458) concern fitting methodology and projection order properties, respectively. The publicly available finite-chain \(\ell_p\) stability result treats a permutation-invariant coordinate metric rather than the neighbor-coupled path norm here. The accessible previous findings on convex regression, anti-Monge projection, and graph-Sobolev truncation concern different operators or metrics and do not imply this exact isotonic modulus. An unindexed prior finite-dimensional matrix-norm computation could remain equivalent; priority is not independently established.

## Mathematical value — PASS

This is the first chain length with competing pooling geometries and a sharp switch in the optimizer. The explicit \(\gamma=1/2\) phase transition and norm cusp quantify a genuine condition-number effect that cannot be read from ordinary Euclidean contractivity or a yes/no Sobolev contraction criterion. It is a small but complete and motivated stability model with actual maximizing perturbations, useful as a diagnostic for shape-constrained regression under correlated, gradient-weighted error metrics. No theorem for longer chains is asserted.

Self-review: passed. Independent audit: not yet performed.
