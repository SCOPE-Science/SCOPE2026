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

The proof uses a truncated crossed-product realization of the modular dihedral group algebra, an explicit Lie bracket table, induction on the Lie lower central series, and the finite Lazard correspondence for nilpotency class strictly smaller than the characteristic.

The standalone standard-library program `verify.py` reproduces Lie-series dimensions for the primes 3, 5, 7, 11, 13, and 17 directly from the multiplication rules. It separately tests all 6561 radical-unit ordered pairs for the prime 3, checking that the commutator set has size 3 and is central. It further checks 45 reproducible pseudorandom exponential/logarithm/commutator cases at each of the primes 3, 5, and 7. Execute `python3 verify.py`; the expected final line is `VERIFY_OK_LOWER_CENTRAL`.

These are finite checks only. Arbitrary primes, field extensions, and the complete series follow from the symbolic bracket argument and the class-below-characteristic correspondence, not from extrapolation. Independent external audit has not been performed.
