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

# Verification of the characteristic-seven Howe-curve strata

The attached `verify.py` uses Python 3 and SymPy to reproduce the exact quartic Hasse coefficient identities, the genus-three Cartier–Manin determinant identity, the pairwise elimination resultants and their specialized gcds, and smoothness at every claimed exceptional parameter. It also verifies pairwise gradient independence and the complete finite-field sample, independently of the elimination proof.

Run `python3 verify.py`. Successful output ends in `VERIFY_OK` and reports the three common-zero pairs and the exact distribution among smooth symmetric rational parameters. The infinite geometric classification is proved algebraically by resultants and their complete fiber gcds, plus a prime-to-characteristic quotient isogeny. A finite table by itself would not prove the classification over the algebraic closure. No external or independent mathematical audit has been performed.
