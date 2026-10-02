---
record_id: SCOPE-20260913-058
audit_date: 2026-10-01
disposition: passed
---

# Independent scientific audit

## Final claim

At \(alpha=1.25\) and \(F_0=lambda I_3\), the axis laminate has \(E_*=0.030120427271913\) and \(QW(F_0)<=E_*\); among two-atom diagonal measures matching first, cofactor and determinant moments it is the exact minimum, and zero-energy gradient Young measures are excluded by the trace obstruction.

## Correctness — PASS

The covariance identity forces an axis split. Independent calculus gives \(lambda=1.1387208644533735\), \(t_*=0.33534962655951794\), endpoints \(0.972558271093253\), \(1.222558271093253\), and \(E_*=0.030120427271912907\). The well switch is \(1.097558271093253\); the proper-rotation correction excludes negative-axis improvement. The trace obstruction is \(3.375<3lambda=3.41616259336\).

## Originality — PASS

General two-well literature does not give this 3D hydrostatic-point value or restricted classification.

### Equivalent formulations

**Searches.** two-well hydrostatic midpoint; two-atom diagonal minors

**Evidence.** No matching parameter-specific statement found.

**Reasoning.** Equivalent formulations did not reveal coverage.
### Broader coverage

**Searches.** polyconvex quasiconvex two-well; Conti Dolzmann

**Evidence.** Closest exact relaxation is two-dimensional and different.

**Reasoning.** Broader literature does not imply this result.
### Exact database or table

**Searches.** published hydrostatic midpoint search; exact constant 0.030120427271913

**Evidence.** No external table found.

**Reasoning.** No standard table yields the value.
### Claim versus prior implication

**Searches.** Procrustes versus branch minimization

**Evidence.** Procrustes gives the distance formula, not the optimizing mixture.

**Reasoning.** The parameter-specific reduction is necessary.

### Source inspections

- **Relaxation of a model energy for the cubic to tetragonal phase transformation in two dimensions** (https://arxiv.org/abs/1403.4877): Trigger — Closest two-well relaxation. Material read — Primary abstract and bibliographic statement. Method — Primary abstract inspection; full HTML unavailable. Assessment — NOT_COVERING. Evidence — It is explicitly two-dimensional and a different model.
- **A generalized solution of the orthogonal Procrustes problem** (https://doi.org/10.1007/BF02289451): Trigger — Nearest proper-rotation formula. Material read — Standard singular-value characterization. Method — Theorem comparison. Assessment — SUPPORTING_NOT_COVERING. Evidence — It supplies the distance formula only.

### Checked sources

- https://arxiv.org/abs/1403.4877
- https://doi.org/10.1007/BF02289451
- artifacts/order1_exact.py
- artifacts/final_verify.py
- artifacts/edge_check.py

### Residual risks

- No full-text survey dedicated to this exact 3D model surfaced.
- Result remains restricted.

## Scientific value — PASS

A sharp laminate, complete restricted classification and positive-energy obstruction are motivated structural constraints on an open envelope problem.

## Limitations

- No claim that \(PW(F_0)=QW(F_0)\).
- No global non-diagonal or higher-order optimality.

## Disposition

**PASSED**. Acceptance requires PASS on correctness, originality, and scientific value.
