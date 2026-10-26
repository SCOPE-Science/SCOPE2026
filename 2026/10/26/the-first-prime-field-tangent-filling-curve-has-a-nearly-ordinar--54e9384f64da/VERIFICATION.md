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

# Exact mathematical checks

Both executables use only Python standard-library arbitrary-precision integers. With the scripts extracted into a directory, execute `python3 check_singularity.py`, then `python3 verify.py`.

`check_singularity.py` normalizes \(s=X+Y+Z=1\) and constructs the ideal \((x^9-3,y^9-3,(1-x-y)^9-3)\) in \(\mathbb F_{11}[x,y]\). It processes all Buchberger S-pairs, checks its reduced zero is \((4,4)\), and checks the original generators vanish there. Its exact result is `GEOMETRY_OK` with 26 generators and 325 S-pairs; the complement \(s=0\) has no projective gradient zero. The local tangent cone has discriminant 8, which is nonsquare over \(\mathbb F_{11}\).

`verify.py` calculates \(F^{10}\) using sparse polynomial powering and separately evaluates the required coefficients via a multinomial expansion of the four summands. All entries of the \(36\times36\) Cartier coefficient matrix agree. The matrix has rank 35 and constant column sum 10. Restriction to the adjoint hyperplane of coefficient sum zero gives a \(35\times35\) matrix whose rank and square's rank both equal 34, so the normalized Jacobian has \(11\)-rank 34 and \(a\)-number 1. A top-left \(35\times35\) minor has determinant 10 mod 11; full-matrix left/right null vectors have pairing 8 mod 11. The exact list of basis exponents, minor indices, rank witnesses, and serialized matrix checksum are retained in `CERTIFICATE.json`.

The computer checks are complete for the finite matrix and local ideal, not experimental inference over different field sizes. A full zeta-function numerator and independent mathematical audit are not supplied. The conversion from Cartier stable rank to \(p\)-rank and from Newton symmetry to slopes invokes standard theorems.
