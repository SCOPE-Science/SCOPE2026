# Independent Audit — 2026-09-28

**Record:** `2026/09/10/039`  
**Title:** Uniform Steklov bound 161π/76 on the symmetric circular-pants cell  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `6f3c48db74e50ee36bbf84c4ce65e7aa15c6eec9`  
**Disposition:** **PASSED**

## Independent checks

- Recomputed all integrals and the derivative polynomial independently from the geometry.
- Checked the endpoint arithmetic with exact rational fractions, not floating-point sampling.
- Compared the result with the actual statement of the Girouard–Polterovich topological bound.

## Three-axis assessment

- **Correctness — PASS**: The Rayleigh-test calculation checks exactly. For u=x on the symmetric circular-pants domain, the boundary mean is zero; ∫Ω|∇u|²=π(1−2r²), ∫∂Ωu²=π(1+r+2r³), and L=2π(1+2r). Hence σ1L≤2π(1+2r)(1−2r²)/(1+r+2r³). The derivative numerator 1−4r−20r²−16r³+4r⁴ is negative on [1/5,7/20], giving the maximum 161π/76 at r=1/5.
- **Originality — PASS**: The primary general Steklov source gives σ_k L≤2π(γ+l)k, which specializes to 6π here but does not contain the symmetric-cell quotient or the constant 161π/76. Focused searches for the exact constant/domain and equivalent 'circular pants' formulations found no covering theorem or table. The result is therefore a new cell-specific analytic certificate relative to the reviewed literature, not an instantiation of the general 6π bound.
- **Scientific Value — PASS**: Although nonsharp and elementary, the result gives a rigorous uniform enclosure on a motivated one-parameter triply connected family and improves the generic topological bound by a large margin. It is reusable as a benchmark in Steklov shape-optimization searches rather than merely a sampled computation.

## Sources compared

- Repository record 039 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/10/039/RESULT.md — Contains the cell definition, Rayleigh quotient and claimed monotonicity audited here.
- Girouard–Polterovich, Upper bounds for Steklov eigenvalues on surfaces: https://arxiv.org/abs/1202.5108 — Gives σ_k L≤2π(γ+l)k; for genus 0 and three boundary components this yields 6π, not the record's sharper cell-specific 161π/76.
- Colbois–Girouard–Gordon–Sher, Some recent developments on the Steklov eigenvalue problem: https://arxiv.org/abs/2212.12528 — Provides broader Steklov context but no covering statement for this exact symmetric one-parameter cell.

## Limitations

- The bound is not claimed sharp and identifies no extremizer.
- The originality finding is limited to the located literature and exact/equivalent-formulation searches; it is not proof of absence from every unpublished source.

This audit is independent of the repository's pre-existing `AUDIT.json`. GitHub was read only as evidence; no repository changes were made by this audit run.
