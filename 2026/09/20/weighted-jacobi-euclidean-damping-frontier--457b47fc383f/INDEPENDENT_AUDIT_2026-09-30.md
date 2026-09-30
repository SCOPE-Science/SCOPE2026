# Independent Audit — Sharp Euclidean damping frontier for weighted Jacobi on 2x2 SPD systems

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `4c340cf1c82addf669744d213bb844ffc854360e`  
**Audited current source tree:** `4c340cf1c82addf669744d213bb844ffc854360e`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned source tree. GitHub was used read-only, and the dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. With B=D^{-1}A, Euclidean nonexpansiveness is equivalent to B+B^T-omega B^T B positive semidefinite; congruence by B^{-T},B^{-1} gives B^{-T}+B^{-1}-omega I positive semidefinite and hence the exact ceiling lambda_min(A^{-1}D+DA^{-1}). For A=[[a,c],[c,d]], direct inversion yields (2ad-|c|(a+d))/(ad-c^2). Fixing eigenvalues 1 and kappa gives |c|=z in [0,(kappa-1)/2], ad=kappa+z^2, and the ceiling becomes the convex quadratic 2+[2z^2-(kappa+1)z]/kappa. Its constrained vertex changes at kappa=3, giving exactly the two submitted branches. The zero and unit crossings are 7+4sqrt(3) and 3+2sqrt(2). An independent dense rotation scan reproduced the envelope numerically at kappa=1,2,3,4,9,7+4sqrt(3),20.

## Originality — PASS

PASS, narrowly scoped. Arioli–Romani relate condition numbers to the spectral radius of the Jacobi matrix under diagonal-dominance assumptions; that is an asymptotic-convergence result, not a Euclidean one-step norm frontier. Hadjidimos–Neumann optimize Euclidean norms for SOR/MSOR operators with Property A, not weighted Jacobi over fixed-condition-number SPD classes. Targeted searches for the exact certificate A^{-1}D+DA^{-1}, the 2x2 robust envelope, and the two radical thresholds found no matching theorem. Standard stationary-iteration algebra and classical spectral convergence receive no novelty credit.

## Scientific value — PASS

PASS. The result cleanly separates spectral convergence from one-step Euclidean safety for a basic stationary method, gives an exact fixed-matrix certificate in all dimensions, and completely resolves the robust condition-number question in dimension two. The sharp no-positive-damping threshold is a useful benchmark for nonnormal transient amplification.

## Independent checks

- Re-derived the matrix inequality and congruence proving the fixed-matrix ceiling.
- Re-derived the 2x2 inverse formula and the condition |c|<=min(a,d) for undamped Euclidean nonexpansiveness.
- Reparameterized every 2x2 SPD matrix of condition number kappa by a rotation of diag(1,kappa) and minimized the resulting convex quadratic.
- Independently scanned 10,001 rotations for representative kappa values; the numerical minima agreed with the exact piecewise formula to grid precision.
- Compared with Arioli–Romani (1985), whose accessible full text studies condition-number bounds for Jacobi spectral radius, and Hadjidimos–Neumann (1998), whose theorem concerns SOR/MSOR Euclidean-norm minimization.
- Targeted searches for the exact matrix certificate and radical thresholds found no covering weighted-Jacobi theorem.
- GitHub current main has exactly the assigned directory tree SHA; the dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The condition-number-only sharp envelope is proved only in dimension two.
- The metric is the Euclidean one-step error norm; energy norms, residual norms, and asymptotic optimal damping are different questions.
- Broad historical monographs on stationary iterations were not inspected exhaustively theorem by theorem; originality is limited to the exact certificate/envelope actually compared.

## Evidence and references

- https://doi.org/10.1007/BF01400253
- https://doi.org/10.1137/S0895479896300498
- https://doi.org/10.1137/1.9780898718003.ch4
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/weighted-jacobi-euclidean-damping-frontier--457b47fc383f

This guarded change set changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
