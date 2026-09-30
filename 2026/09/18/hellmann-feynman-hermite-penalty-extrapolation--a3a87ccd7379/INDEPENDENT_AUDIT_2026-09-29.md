# Independent audit — 2026-09-29

Record: `2026/09/18/hellmann-feynman-hermite-penalty-extrapolation--a3a87ccd7379`  
Assigned and audited source tree: `5657ca5e4f80f4fdb805ea7fff64fe85ba15d939`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The analytic and interpolation claims check. In the [U,Z] basis, the finite spectral branch is governed by the analytic Schur complement D-λI-tE^T[C+t(B-λI)]^{-1}E. Simplicity of λ_* makes the relevant zero simple and gives a real-analytic branch in t=1/ρ. Expanding the inverse yields the symmetric effective operator D-tG+t^2J+O(t^3), and ordinary simple-eigenvalue perturbation gives b=v^T(J-GSG)v with S=(D-λ_*I)^†. Independently solving the cubic Hermite exactness equations at nodes t and t/q reproduces every coefficient in the displayed two-level formula after using g'(t)=-t^{-2}f'(1/t). The 2×2 witness has the stated expansion, and the archived random-matrix check is consistent with an O(ρ^-3) remainder after the explicit second coefficient is removed.

## Originality

**qualified_incremental_extension**. Wang–Xia already prove the first-order expansion, explicitly state the two-level value extrapolation 2f(2ρ)-f(ρ)=λ_*+O(ρ^-2), and use Hellmann–Feynman data to form a one-level corrected value with O(ρ^-2) error. Those ingredients materially narrow the novelty. The record goes further by proving simple-branch analyticity, writing the second coefficient in closed form, and using value/derivative Hermite interpolation at p geometric levels to obtain O(ρ^-2p), including the explicit two-level fourth-order estimator. Targeted searches did not locate that coefficient or p-level Hermite construction for this projected-Hessian path. The contribution is therefore a higher-order continuation/extrapolation refinement, not a new penalty framework.

## Scientific value

**useful_higher_order_refinement**. The result turns the source paper's first-order penalty asymptotics into a systematic higher-order extrapolation mechanism and supplies an explicit second coefficient useful for analysis and diagnostics. Its practical value is conditional: fixed-order asymptotics improve the idealized truncation error, but the record correctly does not claim numerical superiority once eigensolver error or cancellation dominates.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/hellmann-feynman-hermite-penalty-extrapolation--a3a87ccd7379
- https://arxiv.org/abs/2609.18538
- https://doi.org/10.1137/21M1397349
- https://doi.org/10.4208/csiam-am.2021.nla.01
- https://doi.org/10.1137/1013092

## Limitations

- The scalar analytic expansion assumes the constrained minimum eigenvalue is simple; a multiple target requires degenerate perturbation theory.
- Wang–Xia already contain both a two-level value extrapolation and an O(ρ^-2) Hellmann–Feynman corrected-value diagnostic, so novelty is confined to the explicit higher-order formulas and Hermite order doubling.
- The result is asymptotic for fixed p and q and provides no finite-precision stability or optimal-node theorem.
- No claim is made that derivative-enhanced extrapolation is preferable to direct projected certification in a practical eigensolver.
