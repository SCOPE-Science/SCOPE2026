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

# Verification and reproduction

Execute `python verify_rank_one_relu.py` with Python 3 and NumPy available. The standalone script enumerates the sign-partition score for each test matrix, takes two nonnegative leading singular-vector outer products, assembles the signed factors and the rectified result, and checks that its squared Frobenius error matches the full matrix energy minus the two spectral gains. It includes an exhaustive small binary collection, eight identity cases, and reproducible seeded rectangular nonnegative inputs, plus specific two-by-two data from prior work.

Observed check: `PASS 146 certificate cases; enumeration, reconstruction, identity family and prior 2x2 example`.

The exact theorem for all dimensions and real entries follows from the accompanying elementary determinantal, sign-partition, compactness, and nonnegative singular-vector proof. Finite numerical tests do not establish the universal statement or completeness of a literature search. Leading singular vector multiplicities and empty blocks are permitted by the theorem; floating-point tests use numerical tolerances and do not certify exact arithmetic globally.
