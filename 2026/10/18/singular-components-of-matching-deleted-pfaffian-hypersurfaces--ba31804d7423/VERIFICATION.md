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

Execute `python3 verification/check_pfaffian.py` with Python 3 and no additional packages. The program uses exact finite-field arithmetic modulo \(101\) with a fixed random seed. It tests all \(k\) for sizes \(N=6,8\), sampling generic alternating matrices, symplectic factorizations of both relevant rank strata, and zero-row-pair points, and computes the Hessian ranks of the two transverse forms. A successful check prints `VERIFY_OK`. These checks are finite corroboration, not a proof for all \(N\) or characteristic zero, which is supplied separately in `RESULT.md`.

Mathematical limitations: only the reduced singular locus and generic transverse quadratic forms are established. The full nonreduced Jacobian scheme is not determined, and independently reproduced computations do not constitute independent validation of the general theorem.
