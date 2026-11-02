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

Run `python3 verify.py` using Python 3 and only the standard library. For each field size \(q\in\{2,4,8,16,32,64\}\), the script constructs polynomial-basis field arithmetic, enumerates every monic cubic, computes the Möbius value by checking the formal derivative and counting roots in the ground field, and then directly tallies the nine joint signs for the selected shifts.

Observed run output:

```
PASS q=2 shifts=2 full_polynomials_per_shift=8
PASS q=4 shifts=12 full_polynomials_per_shift=64
PASS q=8 shifts=56 full_polynomials_per_shift=512
PASS q=16 shifts=240 full_polynomials_per_shift=4096
PASS q=32 shifts=36 full_polynomials_per_shift=32768
PASS q=64 shifts=6 full_polynomials_per_shift=262144
VERIFY_OK degrees=6 shifts=352 cubic_pairs=3765008
```

The script checks every nonconstant affine shift when \(q\le16\), plus selected shifts for \(q=32,64\). The software uses neither the Berlekamp formula nor additive-character orthogonality. The infinite field-size statement is justified by the algebraic proof in RESULT.md, not by the finite tests. The full result has not been independently audited.
