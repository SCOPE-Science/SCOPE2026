# Independent audit — 2026-09-30

**Record:** `2026/09/20/sharp-steiner-disk-hausdorff-stability-constant-width--49cee8c667fb`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `250f4a85ab9e81ef4c7b8aed4b713627f87bacba`  
**Disposition:** **PASSED**

## Correctness — PASS

Steiner centering removes the first support-function harmonics and constant width removes all positive even harmonics, so h=w/2+q with odd modes n>=3. The support-function area identity gives ε=(π/2)Σ(n^2-1)(a_n^2+b_n^2), while Hausdorff distance to the Steiner disk is ||q||∞. Weighted Cauchy–Schwarz and the telescoping identity Σ_{k>=1}1/((2k+1)^2-1)=1/4 yield ε>=2πρ^2. The finite Fourier kernels q_N have positive curvature after the stated scaling and give ε_N/ρ_N^2=2π(N+1)/N, proving sharpness. Equality in the point-evaluation inequality forces the reproducing-kernel profile; applying 1+∂_θ^2 creates antipodal Dirac masses of opposite signs, incompatible with a nonnegative curvature measure unless q=0, so only the disk attains equality.

## Originality — PASS (literature-bounded)

Groemer's 1988 stability paper gives Hausdorff control by some diameter-w disk near maximal area, while Cufí–Gallego–Reventós use the Steiner disk in Fourier/L2-type deficit inequalities. Searches combining constant width, Steiner disk, Hausdorff distance, area deficit and the exact 2π constant did not locate the sharp canonical-center inequality or its smooth asymptotic extremizers. The proof is essentially a sharp restricted Fourier/Sobolev evaluation estimate, so an older approximation-theory formulation remains a plausible residual risk.

## Scientific value — PASS

The theorem strengthens a classical stability statement by fixing a canonical center, improving the explicit coefficient for that comparison, and determining the best possible constant with a smooth sharpness sequence. The nonattainment mechanism also cleanly separates the analytic extremal kernel from convex admissibility.

## Evidence and literature

- Groemer, Stability Theorems for Convex Domains of Constant Width (1988): https://doi.org/10.4153/CMB-1988-048-3
- Cufí, Gallego, Reventós, A note on Hurwitz’s inequality (2018): https://doi.org/10.1016/j.jmaa.2017.09.017
- Thäle, A note on a problem posed by Linderholm (2026): https://doi.org/10.1007/s00022-025-00783-4

## Limitations

- The result is planar and Euclidean and concerns the canonical Steiner disk, not the best translated disk.
- The sharp constant is approached by noncircular smooth bodies but attained only by the disk.
- Differently phrased older Fourier/approximation-theory coverage remains the main originality uncertainty.

The independent audit finds the record scientifically complete on all three axes at the audited tree. The literature verdict is bounded by the sources and searches explicitly described above; it is not inferred merely from failure to find a match.
