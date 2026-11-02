# Independent mathematical audit

## correctness

PASS

The exact affine Gram inverse yields w_i=1/M-t(X_i-t)/S, sum_i w_i=1, sum_i w_i X_i=0 and sum_i w_i²=1/M+t²/S. Orthogonal polar coordinates X=t*1+r*omega have Jacobian sqrt(M)r^(M-2); setting r=s/u in the tail event and applying dominated convergence on a bounded rescaled cylinder gives P(kappa_M>u)~C_M u^-(M-1), with the displayed sphere integral C_M. Layer-cake integration gives finite p-th moment iff p<M-1. A six-arc centered-circle calculation gives C_3=1/2+pi/(3sqrt3). Exact ordered triple integration and disjoint endpoint negative-weight events give all-positive probability (14-pi)/16. Conditional independent homoscedastic noise variance is sigma²(1/M+t²/S), whose radial singularity int r^(M-4)dr is finite iff M>=4. Independent sample/moment tests had maximum residual below 3.6e-11, and 300000 new triples gave positive fraction 0.6798567 against exact 0.6786505 (1.41 standard errors); numerical sampling is only corroboration.

## originality

PASS

The randomized least-squares cubature work of Bělík–Narayan–Turnage and Migliorati–Nobile focuses on construction and high-probability stability/positivity, which is logically compatible with these exact fixed-sample heavy tails. The affine Gramian identity is established background, not claimed new. Exact near-coincident radial exponent, C_3, three-point positivity volume and noise cutoff need further distributional analysis. Bělík full 2026 manuscript and Wilson 1970 full source were inaccessible; possible stronger formula or regression-theoretic aliases remain priority risk.

## value

PASS

The total variation of quadrature weights is a natural bounded-data amplification norm and positivity is a natural non-overshoot property. A three-node rule can have positive weights with probability about 0.679 while having infinite unconditional squared-noise amplification; exactly four nodes mark the first finite-variance case. This is a motivated sharp reliability cutoff, not routine identity-only algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
