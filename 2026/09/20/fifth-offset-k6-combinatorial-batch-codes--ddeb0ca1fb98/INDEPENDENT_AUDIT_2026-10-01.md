---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For every \(m\ge10\), the ordinary \(t=1\) combinatorial batch-code optimum satisfies \(N(m+5,6,m)=m+18\).

## Correctness — PASS

The exact preceding diagonal and the degree/deletion lemma give the lower bound. The displayed 15-item, 10-server family has storage 28; an independent recomputation checked all 9,948 request subsets through size six, with minimum union sizes \(1,2,3,4,5,6\). Singleton extension then propagates the valid base code to every \(m\ge10\).

**Checked sources.** assigned RESULT.md; artifacts/verify_base.py; Shen--Jia--Zhang 2018; Jia--Zhang--Yuan 2016; independent exhaustive Hall recomputation

**Residual risks.** 

## Originality — PASS

The exact-value literature located reaches the preceding \(m+3\) and \(m+4\) diagonals for \(k=6\), but no earlier fifth-offset equality or the displayed base construction was found. The generalized 2026 paper's accessible abstract concerns a broader model.

### Equivalent formulations

Equivalent Hall/set-system formulations were included.

### Broader coverage

Prior work supplies the lower bound but not the new base construction.

### Exact database or table

The new base construction is not a known table lookup.

### Claim versus prior implication

The explicit \((15,28,6,10)\) Hall-valid construction is the non-mechanical ingredient.

**Checked sources.** https://doi.org/10.3934/amc.2018040; https://doi.org/10.12386/A2016sxxb0024; https://doi.org/10.1016/j.dam.2026.04.038; Resultary assigned-record hit

**Residual risks.** The unread full generalized-CBC text remains a small residual risk.

## Value — PASS

The result closes the next natural infinite exact diagonal in a sequence of established CBC storage problems, using a compact independently checkable base construction.

**Checked sources.** 2016 and 2018 exact CBC papers; CBC survey context

**Residual risks.** The boundary \(m=8,9\) remains open.

## Limitations

- The boundary cases \(m=8,9\) are not determined.
- The 2026 generalized-CBC paper was available only at abstract/metadata level.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
