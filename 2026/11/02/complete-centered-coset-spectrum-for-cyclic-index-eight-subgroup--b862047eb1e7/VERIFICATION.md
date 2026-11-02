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

The standalone `verify.py` uses exact integer modular arithmetic. Executing it checks the eight local cosets modulo 41, their five-element sums, 60 admissible primes below 400, full multiplicative coset enumeration for 480 lifted cosets, cyclicity by generator comparison, the 15 reduced residue classes modulo 205 for each of eight shifts, and all five explicit witnesses. Expected output:

`VERIFY_OK admissible_primes=60 direct_coset_sums=480 witness_counts=5`

The eight possible shift indices are checked implicitly over the prime examples. The code verifies finite cases only. The global spectrum follows from pairing cosets by negation; infinite realizations and the asymptotic densities follow from CRT and the prime number theorem for arithmetic progressions, not from the finite test. No independent audit has been performed.
