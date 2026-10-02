---
audit_date: 2026-09-30
status: passed
---

# Independent mathematical audit

## Final claim

The left Gog and left GOGAm trapezoids of shape (n,k)=(6,3) are equinumerous, with exactly 4862 objects on each side.

## Correctness — PASS

A fresh enumeration from the committed definitions generated exactly 7436 Gog triangles and 7436 Magog triangles of order 6. Applying the committed Schützenberger map and projecting the three leftmost diagonals gave exactly 4862 distinct Gog and 4862 distinct GOGAm trapezoids. The inspected canonical verifier additionally checks the published GOGAm inequality, the nearby n=4,5,6 projection table, an involution test at n=4, and the independent LGV determinant value 4862. The theorem is therefore a finite exhaustive result at exactly the claimed cell.

## Originality — PASS

Biane-Cheballah Conjecture 7.2 states equinumeration for all left (n,k) Gog/GOGAm trapezoids and their paper proves only k=1 and k=2. Their full text therefore leaves k=3 as the first unresolved width. Fischer develops constant-term formulas for related Gog/Magog refinements and determinant methods but does not resolve this left GOGAm cell. A published-corpus search returned the present (6,3)=4862 result as the sole direct match.

### Equivalent formulations

The audited (6,3) cell is literally a finite instance of that open left-trapezoid conjecture.

### Broader coverage

Those formulas do not state or mechanically identify the left GOGAm (6,3) equality.

### Exact database or table comparison

No prior table resolving this exact cell was located.

### Claim versus prior implication

Known one- and two-diagonal cases do not imply the three-diagonal (6,3) count.

## Value — PASS

This is an exact finite cell in a published open equinumeration conjecture, at the first width beyond the explicitly solved one- and two-diagonal cases. Such a first unresolved cell is a motivated finite cutoff and a useful regression datum for proposed bijections or formulas.

## Sources inspected

- Git tree/blobs: RESULT.md, gen.py, gogam.py, lgv_cert.py, lgv2.py and canonical verifier. Reconstructed the definitions and independently re-enumerated the headline cell.
- Biane-Cheballah, arXiv:1401.6516: full-text definitions and Section 7, including Conjecture 7.2 and the statement that k=1,2 are proved. Confirms the exact open conjectural context and that k=3 is not covered there.
- Fischer, arXiv:1804.07054: abstract and stated scope of constant-term/determinant formulas. Provides related enumeration machinery, not the audited left-GOGAm cell.

## Residual risks

- This is not an all-n theorem or a bijection. A later unindexed computation could contain the same cell, but the inspected primary conjecture paper and searches did not reveal one.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
