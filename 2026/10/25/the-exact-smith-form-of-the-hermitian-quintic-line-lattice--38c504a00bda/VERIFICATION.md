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

The standalone script `verification/hermitian_quintic_smith.py` was executed with the standard Python interpreter. It enumerated all normalized projective points over \(\mathbb F_{16}\), all isotropic points, and all totally isotropic lines; reconstructed the integer line-intersection matrix; and computed ranks modulo 2 and 3 plus the 2-adic Smith counts by exact elimination modulo 4.

Observed output: `POINTS=4369`, `ISOTROPIC_POINTS=1105`, `TOTALLY_ISOTROPIC_LINES=325`, `RANK_MOD_2=37`, `RANK_MOD_3=53`, `SMITH_2_ADIC_EXPONENT_COUNTS: e0=37, e1=16, e2=0`, `VERIFY_OK`.

The rational rank is 53 because rank modulo 3 is 53 and the middle Betti number is 53. The absence of odd-prime invariant factors uses Shimada's general characteristic-primary discriminant theorem. The full text of Shimada (2001) was not fetched, and the exact index of the line lattice in the full numerical cycle lattice is not determined here. Independent audit and independent validation remain unperformed.
