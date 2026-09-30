# Independent Audit — Exact conditioning-dependent stability threshold for affine reflected gradient

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `5acb10b994fc7d26f584b385bc208bd39dd83375`  
**Audited current source tree:** `5acb10b994fc7d26f584b385bc208bd39dd83375`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used read-only as evidence; this is a guarded publication-plan payload and is not claimed to be already published.

## Correctness — PASSED

PASS. For affine B, the two-step companion spectrum is exactly governed by (r²-r)+λ(2r-1)μ=0 for μ∈spec(M), including defective M. Strong monotonicity and the operator-norm bound imply Re(μ/L)≥q and |μ/L|≤1. Solving the unit-circle condition r=e^{iθ} gives the submitted A(c), B(c), and t=√B(c)∈[1/√3,2/3]. The feasibility inequalities reduce to q≤φ(t)=t(3t²−1)/(2(1−2t²)), whose derivative is positive on the interval; hence the first possible contact is the unique τ_*(q) solving 3τ³+4qτ²−τ−2q=0. The rotation-dilation matrix has symmetric part qLI, norm L, and eigenvalue on the extremal boundary, so it realizes sharpness. Small-step stability plus absence of earlier unit-circle contact yields R-linear convergence below threshold.

## Originality — PASSED

PASS, narrowly scoped. Frequency-domain/root-locus analysis of OGD and reflected gradient is established prior art, and Shehu’s 2026 paper already gives the sharp monotone affine constant 1/√3 plus strong-monotonicity rates. Anagnostides–Panageas give sharp OGD analysis under the different strongly-monotone-and-cocoercive hypothesis. Targeted searches did not locate the submitted exact interpolation depending only on q=σ/L, its cubic, or the matching rotation-dilation witness for the full affine class with symmetric part ≥σI and ||M||≤L. Novelty is limited to that exact universal affine phase boundary.

## Scientific value — PASSED

PASS. The result replaces a conditioning-blind monotone threshold by a sharp condition-dependent boundary ranging continuously from 1/√3 to 2/3 and supplies an extremizer. It materially sharpens the admissible affine reflected-gradient step under a common and natural pair of operator bounds, while clearly separating itself from nonlinear/projected guarantees.

## Independent checks

- Re-derived the companion characteristic determinant without assuming diagonalizability.
- Re-derived A(c), B(c), the t-parameterization, φ(t), and its monotonicity.
- Numerically checked representative q values and the extremal boundary geometry as a sanity check.
- Checked the q→0 and q=1 endpoint constants and the explicit rotation-dilation witness.
- Compared with Shehu 2026, Malitsky 2015, and Anagnostides–Panageas 2021/2022, avoiding novelty claims for standard frequency-domain methodology.
- Verified the current main tree equals the assigned tree and that dated independent-audit files are absent.

## Limitations

- The theorem is finite-dimensional, affine, unconstrained, deterministic, and constant-step.
- It does not enlarge the sharp general nonlinear or projected reflected-gradient ranges.
- Root-locus methodology itself is prior art; originality is only the exact q-dependent affine threshold under the stated norm/strong-monotonicity class.

## Evidence and references

- https://arxiv.org/abs/2609.18355
- https://arxiv.org/abs/2109.04603
- https://doi.org/10.1137/14097238X
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/strongly-monotone-prg-sharp-threshold--63a985cd76f4

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
