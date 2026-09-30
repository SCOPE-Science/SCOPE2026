# Independent audit — Design-independent physical loads need a moving-load term in parameterized EIFEM compliance sensitivities

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/eifem-moving-load-compliance-sensitivity--da9e20416613`  
**Audited tree:** `6bbbab9de43e2f381a4459a89ff7b4a14d14c391`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The calculus and invariance diagnosis are exact. Differentiating J=F_c^T K_c^{-1}F_c with F_c=T^T F gives J'=2(F_c')^Tq-q^T K_c'q, so a fixed physical F does not imply fixed reduced coordinates when T varies. Expanding K_c' and using T^T(F-KTq)=0 yields J'=-y^T K'y+2r^T T'q. Under T->TR the full derivative is invariant, while the stiffness-only term shifts by -2q^T K_c(R'R^{-1})q and hence by -2cJ under scalar gauge. Independent numerical recomputation of the supplied examples gives the stated +0.16 true derivative versus -0.24 stiffness-only derivative and exact cancellation -1.5+1.5 in the full-space rotation example.

## Originality

**PASS.** The novelty claim is appropriately narrow. Chain-rule terms, parameter-dependent reduced bases, and Pulay-type corrections are prior art and are not claimed. What remains is the source-specific identification of the fixed-fine-load/fixed-coarse-load mismatch in the 2026 EIFEM optimization formulation, plus the coordinate-gauge obstruction and explicit exact-ROM/wrong-sign counterexamples. The public preprint abstract confirms that the framework uses parameter-dependent reduced operators and inexact optimization gradients; targeted searches and the SCOPE repository found no earlier record of this specific correction.

## Scientific Value

**PASS.** The omitted term can reverse the sign of a compliance gradient and can create a spurious nonzero sensitivity even when the reduced model spans the full physical space. The gauge calculation shows the issue is structural rather than a small ROM error, and the correction requires no additional state or adjoint solve once T' is available. This is directly actionable for the motivating method.

## Independent checks

- Differentiated the reduced compliance independently and re-derived the residual/Pulay representation and gauge transformation law.
- Recomputed the rank-one example at mu=pi/4: J=0.2, exact derivative 0.16, stiffness-only -0.24, missing load term +0.40.
- Recomputed the full-space rotation example: J=1.25 is constant, residual is zero, stiffness-only contribution -1.5 and load contribution +1.5.
- Reviewed the public arXiv/SSRN metadata: the source explicitly uses parameter-dependent reduced operators and describes inexact gradients as the optimization mechanism; no public equivalent correction was found.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.20053 — Rubio, Ferrer, Hernández and Antolin (2026), parameterized EIFEM structural-optimization source.
- https://ssrn.com/abstract=7483258 — Public SSRN record for the same 2026 EIFEM manuscript.
- https://doi.org/10.1002/nme.5998 — Nair and Balajewicz (2019), prior art for parameter-dependent/transported reduced bases.
- https://doi.org/10.1063/1.4728026 — Ruiz-Serrano, Hine and Skylaris (2012), representative Pulay-correction prior art.

## Limitations

- The audit does not assert that the paper’s benchmark implementations actually violate T_j^T F=0; no source-code audit was performed.
- If a fixed coarse-coordinate load is intentionally prescribed, the stiffness-only derivative is correct for that surrogate model; the correction concerns the fixed-physical-load interpretation.
- The full equation-level source claims in the package were not independently re-extracted from the PDF in this run; the mathematical correction itself is independently verified.

## Repository identity

The assigned source-tree SHA `6bbbab9de43e2f381a4459a89ff7b4a14d14c391` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
