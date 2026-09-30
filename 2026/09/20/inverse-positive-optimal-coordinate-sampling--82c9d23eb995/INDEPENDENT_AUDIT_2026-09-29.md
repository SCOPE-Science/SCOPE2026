# Independent audit — 2026-09-29 UTC

Record: `2026/09/20/inverse-positive-optimal-coordinate-sampling--82c9d23eb995`  
Assigned source tree: `85bf9ea8e05acc6af84149c56ed4599d62fcddd7`  
Audited current source tree: `85bf9ea8e05acc6af84149c56ed4599d62fcddd7`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `dd9fb6454fa42574e67fca3ca74cf391e28bf315`  
Disposition: **passed**

## Correctness

**independently_supported**. The closed-form fixed-sampling optimizer is correct. Exact coordinate minimization reduces the sharp one-step A-energy decrement to rho(p)=lambda_min(P^{1/2}CP^{1/2}). For q=C^{-1}1>0 and S=1^Tq, the Rayleigh test vector P^{-1/2}q gives rho(p)<=S/(sum q_i^2/p_i)<=1/S. Equality in Cauchy-Schwarz requires p_i=q_i/S. At this choice the inverse scaled matrix P^{-1/2}C^{-1}P^{-1/2} is entrywise nonnegative and has a strictly positive eigenvector of eigenvalue S; Collatz-Wielandt therefore identifies S as its spectral radius even without irreducibility, proving the smallest eigenvalue is 1/S. Boundary samplings are singular. For the Dirichlet Poisson matrix, solving Cq=1 gives q_i=i(n+1-i), the displayed parabolic probabilities and rho*=6/[n(n+1)(n+2)], with improvement ratio tending to 12/pi^2.

## Originality

**qualified_supported_with_classical_design_risk**. General optimal fixed sampling for randomized linear-system/coordinate methods and the equivalent saturated E-optimal design problem are established prior frameworks. Pukelsheim-Torsney's open 1991 paper was inspected: it develops optimal weights for linearly independent support points and matrix-mean criteria, but the checked closed-form corollary applies to finite matrix-mean parameters and does not state this inverse-positive E-optimal endpoint formula. Likewise, the coordinate-descent literature commonly leaves the exact fixed sampling as an SDP. No checked source gave p proportional to C^{-1}1 under C^{-1}>=0. The claim is thus supported as a closed-form specialization, with substantial older optimal-design/matrix-scaling equivalence risk.

## Scientific value

**meaningful_closed_form_optimization**. The theorem converts a generic semidefinite probability optimization into one linear solve on a natural class containing SPD Stieltjes matrices, proves uniqueness, and yields a concrete Poisson profile with a quantified sharp-rate gain over uniform sampling.

## Independent checks

- Re-derived the exact expected energy-decrement matrix and the Rayleigh/Cauchy upper bound.
- Checked that the Perron-Frobenius step remains valid for reducible nonnegative inverses via Collatz-Wielandt.
- Verified the discrete-Poisson q, normalization and asymptotic 12/pi^2 ratio.
- Inspected the open Pukelsheim-Torsney 1991 optimal-design paper as the closest classical structural comparator.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/inverse-positive-optimal-coordinate-sampling--82c9d23eb995
- https://doi.org/10.1137/15M1025487
- https://arxiv.org/abs/1802.03703
- https://doi.org/10.1007/s11590-015-0916-1
- https://doi.org/10.1214/aos/1176348265
- https://doi.org/10.1007/s11075-022-01431-7
- https://doi.org/10.1137/25M177446X

## Limitations

- The optimizer is for fixed iid single-coordinate sampling and sharp one-step expected A-energy only.
- Adaptive, without-replacement, block, accelerated, greedy, spectral and conjugate-direction methods are outside scope.
- Computing p* for a generic dense matrix requires a linear solve.
- The inverse-positive condition is sufficient, not claimed necessary.
- Older E-optimal-design or diagonal-scaling literature may contain an equivalent specialization under different terminology.
