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

# Verification and replay

Run `python3 verify.py` using the Python 3 standard library from the directory containing the file. The script computes exact integer binomial coefficients modulo the field characteristic and independently tests the base-prime carry criterion. It checks the Zinbiel identity for all admissible basis triples through degree 13, for five primes, and checks maximal square-zero suffixes in 40 admissible dimension cases through degree 96. Expected output begins with `PASS: Zinbiel identity` and reports `40 parameter triples`.

The unbounded theorem is proved using the explicit Jordan-shift ideal classification, Lucas divisibility of one binomial coefficient for every internal product, and a nonzero sharpness witness. Finite computations do not certify all infinite parameters. No independent audit or validation is claimed.
