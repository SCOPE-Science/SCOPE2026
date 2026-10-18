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
# Reproducible checks and their limits

Run `python3 verify.py` in Python 3. The script reconstructs \(\mathbb F_{s^2}\) for the primes \(s=3,5,7\), directly checks the matrix congruence \(T^*AT=A\) for each proposed automorphism, confirms pairwise uniqueness and the sole rational point, and obtains respectively \(108,750,2744\) elements. For \(s=3\), it additionally enumerates **all** projective matrices fixing the rational point and checks the form equation up to scalar, recovering exactly the proposed \(108\) matrices. The exact output terminates in `VERIFY_OK`.

The finite experiments are exhaustive only for the explicitly stated finite fields and cannot prove the all-prime-power theorem. That theorem follows from the projective-automorphism theorem for Hermitian curves and the symbolic norm/trace equations in `RESULT.md`. No external independent audit or certification has been conducted.
