# Scientific review

## Correctness — PASS

The normalized-cube affine Gram matrix is diagonal, giving the exact reproducing kernel \(1+3\sum_i x_i y_i\). Convexity forces the maximum absolute kernel mass to a vertex, and the sign function attains it. The Irwin--Hall volume formula gives the alternating rational expression without numerical approximation. Conditioning and strict Jensen inequality prove monotonicity; the two exact fractions force the dimension-five cutoff. The second asymptotic coefficient follows from a Fourier integral with a controlled small-/intermediate-/large-frequency split. The included checker independently integrates recursively convolved uniform densities for the first nine dimensions.

## Originality — PASS within reviewed evidence

Closest known exact record: *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (published 2026-10-04). Its Dirichlet kernel determines simplex norms but not the parallelepiped/Irwin--Hall norm; the different growth rates prohibit implication by affine equivalence. A published reverse-projection calculation of a centered Irwin--Hall absolute first moment does not cover the shift \(1/6\), the projector norm, or the positivity classification. The primary Hangelbroek--Narcowich--Sun--Ward paper (arXiv:1005.2424) concerns manifold-kernel projector bounds; Foucart concerns one-dimensional splines. Defant et al. (arXiv:2208.06467, Chapter 8) analyze counting-measure projections on the discrete Boolean cube, not continuous uniform-cell affine projection. Searches for cube/parallelepiped aliases and the displayed finite rational values found no covering exact statement. Historical priority remains uncertain because classical polynomial projection literature is extensive.

## Value — PASS

Local unconstrained least-squares affine reconstruction is a standard approximation component. The complete all-dimensional sharp norm and attaining bounded sign input give a meaningful robustness invariant; the first dimension that permits an output below \(-1\) despite input in \([0,1]\) is an exact natural cutoff. A two-term law distinguishes \(\sqrt d\) amplification on parallelepipeds from \(d\)-order amplification on simplices, a mathematically motivated geometry-dependent stability difference. No extension to global finite-element coupling or higher polynomial degree is asserted.

Self-review: passed. Independent audit: not yet performed.
