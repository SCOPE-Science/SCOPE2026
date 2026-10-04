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
The theorem itself is proved algebraically in `RESULT.md`. The critical steps are that the common fixed field is \(\mathbb F_{q^d}\), both the image map and trace adjoint are linear over that field, and a nonzero kernel of a two-term Frobenius map is a one-dimensional \(\mathbb F_{q^d}\)-space.

`artifacts/verify.py` performs finite exact stress tests over \(\mathbb F_{2^m}\) for several pairs \((m,k)\) with \(d>1\). It enumerates every projective parameter, constructs the two binary linear maps, and computes the hull as an exact intersection. The observed hull dimensions and counts are checked against `artifacts/certificate.json`.

The finite tests do not certify the infinite theorem; they are boundary checks for the algebraic proof. No floating-point arithmetic or solver is used.
