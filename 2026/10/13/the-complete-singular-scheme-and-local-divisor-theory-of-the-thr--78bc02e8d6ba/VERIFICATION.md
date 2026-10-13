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

# Reproducibility and verification

Execute `python3 check_birkhoff.py` with the Python standard library. Its recorded stdout is included as `check_output.txt`; a fresh replay reproduced it exactly. The checker establishes rank five for the augmented six exponents and their primitive circuit, exhaustively checks all 64 binary supports of the projective equation, checks Hilbert dimensions in degrees 1 through 12, verifies the rank-four saturated local divisor relation matrix using the gcd of exact maximal minors, and verifies the nondegenerate node Hessian.

The general proof in `RESULT.md` supplies the essential unbounded arguments: the unique primitive toric relation, the complete prime decomposition of the squarefree Jacobian ideal, Cohen--Macaulay tensor factorization, the local analytic forms, and the toric class-group exact sequences. Finite numerical tests alone do not verify a theorem for all closed points. The public source date is the verified first arXiv version of the principal Birkhoff cubic reference. Independent mathematical audit has not been performed.
