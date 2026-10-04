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
# Verification

The classification is analytic. The universal step is the exact factorization of the collinearity determinant into the symmetric factor \(p-h\) and the radical factor \(Q\). The elimination of the radical is accompanied by a positivity check, and the discriminant condition is solved exactly; no finite sampling is used to infer the continuum statement.

`verify.py` uses exact rational arithmetic for the key algebraic identities after setting \(x=p+h\), \(y=ph\), and for the explicit branch value \(ph=3\). It also checks the center affine ratio and the nonorthogonality certificate in a symbolic coefficient representation of \(\sqrt7\). It prints `VERIFY_OK` only when all assertions pass.

The checker is supplemental and does not assess the literature comparison. It is not an independent audit.
