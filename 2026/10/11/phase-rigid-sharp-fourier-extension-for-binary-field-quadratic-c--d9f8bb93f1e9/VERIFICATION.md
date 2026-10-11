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

## Reproducible finite checks

Run `python3 verify.py`. The script uses only Python 3 standard-library modules and implements binary fields of sizes \(2,4,8,16,32\) via explicitly listed irreducible polynomials. Both split and nonsplit quadratic forms are tested over every nonzero level in each field. The script checks exact conic cardinalities, exact representation multiplicities for every pair sum, all sumset cardinalities, the polynomial convolution fourth-moment identity for two deterministic nonconstant complex inputs at every level, and the exact \(2^{M-1}\)-family's sign-pattern equality witness. It also evaluates the Fourier transform directly at every ambient frequency for eight smaller-field cases.

Expected replay line:

`VERIFY_OK level_sets=114 pair_fibers=114 convolution_patterns=228 direct_fourier=8`

## Analytic verification and boundaries

The all-size proof uses the projective-line cardinality calculation, a nondegenerate polar line, the two-root equation \(t^2+t=c\), additive-character orthogonality, and equality in the triangle and Cauchy–Schwarz inequalities. The finite checks confirm arithmetic and normalization in representative fields but cannot certify the all-size claim independently. No formal external certification has been performed.
