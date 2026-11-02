---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks and limits

Run `python verify.py` with Python 3.11 or later, without external dependencies. The supplied `check_output.txt` is a captured successful run.

For \((q,n)=(2,2),(3,2),(2,3)\), the checker exhaustively enumerates all \(q^{n^2}\) matrices and all ordered pairs of matrices as potential conjugators. It computes each domain \(D_{g,h}\) from its defining two-sided equations, groups all one-dimensional matrix-line domains, classifies the lines by whether the square of a nonzero element is zero, and enumerates every image map arising from a single generator. It independently compares the resulting maps with the predicted \(E_n^2+(q-1)Z_n^2\) line-map count. It separately checks \(|\operatorname{GL}_n(q)|\) and the stated skeleton formula.

Expected log:

```
q=2, n=2: |GL|=6, idempotent lines=6, square-zero lines=3, one-line maps=45, skeleton=52: VERIFY_OK
q=3, n=2: |GL|=48, idempotent lines=12, square-zero lines=4, one-line maps=176, skeleton=201: VERIFY_OK
q=2, n=3: |GL|=168, idempotent lines=28, square-zero lines=21, one-line maps=1225, skeleton=1394: VERIFY_OK
VERIFY_OK
```

The checker supports the prime fields of orders two and three only. It tests the generator layer, not an enumeration of all compositions. The proof in `RESULT.md` establishes the requisite general rectangular-composition lemma and universal prime-power formulas. Neither finite testing nor the supplied log alone certifies the complete mathematical theorem. No independent audit is recorded.
