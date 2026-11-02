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

# Reproducibility

Run the standalone script `python verify_projection.py` using Python standard library only. The script was run and returned:

`CHECK_OK 71 exact full-matrix cases including idempotence, cycles, row/column constraints, symmetry, and endpoint norms`

The checks reconstruct \(Q_{(i,j),(k,l)}\) over complete matrices with rational coefficients for 71 small pairs \((m,n)\), compare exact row/column and entrywise norms of the projection and complement to formulas, check matrix idempotence and symmetry, and test the image on oriented elementary four-cycle vectors. The code uses exact integer/rational arithmetic, not floating-point tolerances.

# Logical limitations

Finite parameter tests do not certify the universal result. The proof for all integers \(m,n\ge2\) is the stabilizer-orbit classification and averaging argument in `RESULT.md`. The \(p\in[1,\infty]\) extension follows from permutation-isometry averaging; the rank-one tensor calculation proves factorization. No external or independent mathematical audit was performed.
