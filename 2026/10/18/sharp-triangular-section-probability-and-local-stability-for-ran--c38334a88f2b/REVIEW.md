# Scientific assessment

## Correctness — PASS

**Claim-to-proof:** The affine hitting-plane measure is explicitly normalized via projected widths; two extremal vertex intervals prove the formula for triangular cuts. Concavity plus a positive-measure strict exchange argument prove strict Schur concavity and cube rigidity. A 48-sector spherical vector-area calculation gives the cube constant. Coarea on the six pair-tie great-circle pieces, accounting for all octants, gives the exact second variation. Triple ties are codimension two and contribute only third-order error. The proof distinguishes the moving affine section law from central-section sampling.

**Reproducibility:** `triangular_box_checker.py` computes independent spherical quadrature and local-difference checks, which pass. Numerical checks do not replace the continuum argument.

## Originality — PASS, with residual risks

Bray (2009) already computes the cube's Crofton-type section probabilities: the endpoint is correctly attributed, not novel by itself. The present **global normalized side-length majorization law, unique extremality and exact Hessian constant** are not implied by cube-only data. Related published central rectangular-box hexagon section results use different conditioning and cannot be substituted for the invariant **affine** triangular-section probability. The recent combinatorial cube-slicing papers classify/reconstruct section structures, not their translation-rotation invariant aspect-ratio probabilities; the 2026 cube-reconstruction preprint could only be compared through accessible metadata/abstract. The possibility of an equivalent older stereological optimization result remains.

## Mathematical value — PASS

The result gives a sharp global shape extremal classification for a natural integral-geometric observable under the canonical invariant plane measure, and its isotropic **exact second variation** quantifies susceptibility to anisotropic deformations. These jointly yield a meaningful aspect-ratio stability benchmark beyond a single known cube probability. The setting is limited to rectangular boxes and does not claim a general convex-body extremum.

Self-review: passed. Independent audit: not yet performed.
