# Independent Audit — Sharp one-step Frobenius growth under complete-pivot ACA

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `3bfd24d814dec51b158143033dea67ee02785d83`  
**Audited current source tree:** `3bfd24d814dec51b158143033dea67ee02785d83`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence, and the dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. After moving/scaling the complete pivot to A_11=1, the residual is X-rc^T. Triangle inequality followed by the exact scalar identity gives ||E||_F^2/||A||_F^2 <= 1+R^2C^2/(1+R^2+C^2), and the complete-pivot bounds R^2<=n-1, C^2<=m-1 yield nm/(n+m-1). The explicit square family makes X antiparallel to rc^T and selects ||X||_F=(1+R^2+C^2)/(RC), so both inequalities are equalities; alpha approaching one gives N/sqrt(2N-1) while beta<1 preserves a unique largest pivot for N>=4. Direct expansion confirms the exact Frobenius-change identity. The PSD contrast follows from the diagonal-pivot Schur complement and 0<=E<=A.

## Originality — PASS

PASS, narrowly scoped. Complete-pivot ACA, Schur complements, Gaussian-elimination entry-growth factors, maximum-volume methods, and poor greedy behavior are established prior art. Loe--Huang--Needell analyze ACA through exterior algebra and give an angle-based rank-one description; modern complete-pivoting literature continues to frame worst-case growth mainly entrywise. Searches using the exact constants nm/(n+m-1), N^2/(2N-1), Frobenius residual growth, Schur complements and complete pivoting did not locate an equivalent sharp consecutive-residual theorem. The originality credit is confined to this one-step dimension-only Frobenius factor and its unique-pivot sharpness family.

## Scientific value — PASS

PASS. The theorem quantifies a concrete failure mode of greedy largest-entry ACA: one exact step can increase residual Frobenius mass by almost sqrt(N/2) despite a unique largest pivot. The sharp factor provides a clean diagnostic distinct from classical max-entry growth and the PSD contrast identifies an important structured setting where the obstruction disappears.

## Independent checks

- Re-derived the scalar maximization identity and monotonicity in R^2,C^2.
- Rechecked the sharp family: beta=(1+2s alpha^2)/(s^2 alpha^2), beta<1 near alpha=1 for N>=4, and equality holds in both the triangle and scalar inequalities.
- Numerically recomputed the sharp ratios for N=4,5,10,100; the N=100 alpha=0.999999 value is 7.088805067425 versus N/sqrt(2N-1)=7.088812050083.
- Re-derived the exact one-step norm-change certificate by direct Frobenius expansion.
- Checked the positive-semidefinite Schur-complement monotonicity argument.
- Compared with Loe--Huang--Needell 2026 and modern/classical complete-pivot growth literature; no matching Frobenius consecutive-residual bound was located.
- Verified the current main record tree equals the assigned source-tree SHA and the 2026-09-30 audit markers are absent.

## Limitations

- One exact-arithmetic rank-one step only; no sharp multi-step product is claimed.
- The extremizing family is adversarial and does not predict typical application behavior.
- Classical Gaussian-elimination norm-growth literature is extensive; an older equivalent Schur-complement inequality under different terminology remains a residual priority risk.
- No floating-point backward-stability theorem follows from this result.

## Evidence and references

- https://arxiv.org/abs/2609.17947
- https://doi.org/10.1016/j.laa.2020.02.010
- https://doi.org/10.1112/blms.70034
- https://doi.org/10.1137/23M1597733
- https://doi.org/10.1145/321075.321076
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/sharp-frobenius-growth-complete-pivot-aca--71dd3abf0659

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
