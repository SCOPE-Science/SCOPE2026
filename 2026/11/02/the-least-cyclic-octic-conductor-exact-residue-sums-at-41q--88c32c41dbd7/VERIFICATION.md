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
The standalone `verify.py` uses only Python's standard library. Execute with `python3 verify.py`; it should emit:

`VERIFY_OK prime_moduli=51 cosets=408 density_classes=160:120:60:15:45 witness_modulus=123`

The checker independently constructs \(K\), all eight cosets modulo \(41\), and their sums. It performs a direct least-positive-representative enumeration of each of eight CRT cosets for each of 51 primes \(q<251\), including noncyclic cases (the exact sum identity does not assume cyclicity). It checks all 408 exact deviations, the explicit witness modulo \(123\), the no-nonzero-period property of the coset sum word, the 160 reduced progression classes modulo 205 and their split into 120 cyclic, 60 cyclic centered, 15 all-coset centered, and 45 centered-not-all-coset centered classes. It also checks the elementary first-conductor candidates.

These are exact finite-arithmetic tests. The all-prime statement, uniqueness of the subgroup, and prime densities are established by the written proof, not extrapolated from enumerated primes. No independent mathematical audit or certification is claimed.
