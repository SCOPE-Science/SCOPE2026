# Independent Audit — A two-dimensional phase law for determinant comparisons of |AB| and |BA|

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `3d3e68e74868e0b95b4313a815992d972580f6b7`  
**Audited current source tree:** `3d3e68e74868e0b95b4313a815992d972580f6b7`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path has no changes from the assignment inventory snapshot, so the audited source tree remains exactly the assigned tree. GitHub was used read-only. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. After unitary diagonalization A=diag(a,b), |AB|^2=B A^2 B and |BA|^2=A B^2 A are the two Gram matrices of AB and therefore have the same two eigenvalues. In dimension two, functional calculus on a two-point spectrum gives X^{p/2}-Y^{p/2}=alpha_p(X-Y), and direct multiplication gives the diagonal difference ±(b^2-a^2)|z|^2. Because det(X^{p/2})=det(Y^{p/2}), the 2x2 determinant expansion yields exactly Delta=alpha_p |z|^2(b^2-a^2)(b^k-a^k). The divided difference has sign p and the remaining nonzero factor has sign k; equality for nonzero k,p is exactly a=b or z=0, i.e. AB=BA. I independently tested 200 random invertible Hermitian B and positive diagonal A across sixteen positive/negative exponent pairs; the formula agreed to numerical roundoff and no sign violation occurred. The stated positive-exponent singular extension follows by continuity.

## Originality — PASS

PASS, narrowly scoped. Ghabries's 2022 thesis explicitly formulates the all-k,p>=0 comparison det(A^k+|AB|^p)>=det(A^k+|BA|^p) as an open problem, while proving only k=2 for all p>=0 and k>=2 with 0<=p<=2; its nearby arbitrary-k results compare instead with A^pB^p or (AB)^2. The 2026 normal-matrix extension also retains the A*A/AA* (k=2-type) structure. Targeted searches did not locate the submitted exact 2x2 all-real-exponent phase law or its divided-difference gap formula. Classical two-point functional calculus and determinant identities receive no novelty credit.

## Scientific value — PASS

PASS. The theorem completely resolves, in order two, both the positive-exponent conjectural direction and the invertible negative-p reverse direction, with an exact gap and sharp equality condition rather than only an inequality. It also exposes precisely why the argument is dimension-specific. The result does not claim a higher-dimensional extension.

## Independent checks

- Re-derived |AB|^2=B A^2 B and |BA|^2=A B^2 A and the shared-spectrum step from AB and (AB)*.
- Re-derived the two-point divided-difference functional-calculus identity and the 2x2 determinant cancellation.
- Numerically checked 200 random examples over k in {-2.3,-0.7,0.5,1.8} and p in {-1.7,-0.3,0.6,2.2}; maximum absolute formula discrepancy was below 5e-9 and there were zero sign mismatches.
- Read the relevant full-text thesis passages: Conjecture 2.4/Problem 2 is the all-k,p nonnegative AB-vs-BA comparison; the thesis records only partial parameter ranges and the k=2 result.
- Compared with Ghabries arXiv:2607.21163, whose determinantal application is a normal-matrix extension of the k=2-type inequality rather than arbitrary A^k.
- GitHub compare from the assignment inventory commit to current main reports no changed files under this assigned path; therefore the current source tree remains exactly the assigned SHA, the dated audit pair is absent, and VERIFICATION.md remains at the verified blob SHA.

## Limitations

- The proof is genuinely two-dimensional and gives no higher-dimensional phase law.
- The singular extension is asserted only for k,p>0; negative powers require invertibility.
- Older low-dimensional matrix-inequality literature could contain an equivalent observation under different notation, so originality is intentionally limited to the exact located statement.

## Evidence and references

- https://theses.hal.science/tel-03936351
- https://doi.org/10.1016/j.laa.2020.03.009
- https://doi.org/10.7153/oam-2021-15-07
- https://arxiv.org/abs/2607.21163
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/21/two-dimensional-ab-ba-determinant-phase-law--f7e2a68c2439

This guarded change set changes only the independent-audit channel in `VERIFICATION.md`; the Lean-verification and expert-attestation channels remain exactly as previously recorded.
