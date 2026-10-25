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

# Reproduction of finite certificates

Place `verify.py`, `coverings.json`, and `obstructions.json` in the same directory and run `python3 verify.py` using an ordinary Python 3 interpreter. No third-party packages, network access, computer algebra, or randomness are required.

The verification reconstructs the multiplicative image of primes satisfying each cutoff, tests \(32+128=160\) explicit unit-class witness pairs and verifies complete coverage, checks \(129\) smaller-modulus obstruction entries and two adjacent-prime cutoff obstructions, and independently checks each absent class using modular inverses. Its second method does not rely on the witness-finding algorithm. The expected terminal line is `CERTIFICATE_OK upper_units=160 obstruction_moduli=131 first_general=96 first_prime_power=256 thresholds=47,127`.

All arithmetic is exact and all quantified moduli and classes are enumerated. The certificate cannot establish behavior for larger moduli or the truth of the general conjecture. Public claims have undergone self-review only; independent audit has not been performed.
