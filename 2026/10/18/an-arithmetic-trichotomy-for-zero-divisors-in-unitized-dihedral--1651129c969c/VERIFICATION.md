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

# Verification of the exact finite-field zero-divisor count

The standalone `verify.py` uses elementary polynomial-quotient finite-field arithmetic and Gaussian elimination, independently of the determinant formula in the proof. For each chosen field it constructs all elements of the unitized quandle algebra, builds the left multiplication operator from the multiplication table, and checks its rank. It enumerates all \(q^4\) elements for \(q\in\{2,3,4,5,7,8,9\}\) with predicted nonzero zero-divisor counts \(14,62,138,320,852,1400,2024\), respectively. It verifies the full \(a=0\) hyperplane is singular and that every nonzero \(a\) has the same singularity count under coefficient scaling. The run completed and printed `VERIFY_OK`.

To replay: save the attached `verify.py` beside this file and invoke `python3 verify.py` from that directory. No external packages are needed. Separate symbolic determinant expansion checked the polynomial factorization. These computational checks are finite; the proof uses Fourier/norm counting to cover every finite field, including all extension degrees.

The first public motivating source was posted 2026-08-10. Closest literature establishes the binary example and general background, not independently validated uniqueness of the all-field formula. Independent audit: not performed.
