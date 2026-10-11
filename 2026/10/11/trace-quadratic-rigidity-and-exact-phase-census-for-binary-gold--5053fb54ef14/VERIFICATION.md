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

The theorem for all finite-field sizes follows from the finite-difference and trace-pairing proof, not from experiments. The standalone `artifacts/verify.py` (Python 3 standard library) constructs the complete homogeneous affine-line phase constraints and computes their exact binary rank. The predicted dimension includes the constant direction; removing that direction counts complex projective sign-extremizer lines. For independent Fourier checks, the script constructs pair-sum fibers and compares convolution fourth moments to direct Walsh averages in small fields. Its floating-point arithmetic checks use explicit error tolerances; those computations are corroboration, not exact complex-number certificates. The linear algebra over binary integers and finite-field operations are exact. The supplied script and all arguments are self-contained; no external data files or internet access are required.

The significant unproved limit is priority: abstract lifted-code theory or older coding-theoretic literature might imply the same trace-quadratic phase-code formula without highlighting Fourier extremizers. There is no independent external audit, proof-assistant certification, or claim that finite checks extend by enumeration to all fields.
