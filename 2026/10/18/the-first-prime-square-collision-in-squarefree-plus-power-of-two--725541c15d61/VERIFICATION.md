---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The standalone `verify.py` checks the prime-square collision exhaustively for differences \(1\le d\le20\), enumerates all \(2^{18}\) exponent subsets for the special modulus \(25\), and checks the correction in a finite rational product model with sixteen other primes. Its success line is `VERIFY_OK 18 1 39 262144 16`. The infinite product-model identification in `RESULT.md` uses the prime number theorem in fixed progressions and a Brun–Titchmarsh bound for the square-divisor tail. The strict sign follows from the positive infinite-product event in the proof, not from an extrapolation of the finite computation.
