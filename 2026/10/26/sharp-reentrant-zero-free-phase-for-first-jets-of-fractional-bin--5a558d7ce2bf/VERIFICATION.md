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

# Reproducibility and verification

The complete proof is in `RESULT.md`. It derives the Gram kernel from the Hilbert-space kernel and establishes the exact zero-free classification without substituting a finite check for a universal argument.

To reproduce the supplementary checks, execute `python3 check_fractional_jet.py` with the standard Python library. The script was executed from the embedded artifact source and returned:

`CHECK_OK: rational factorization, boundary zeros, Jacobian checks, derivative identities`

The script verifies the factorization of the boundary threshold polynomial in exact rational arithmetic on a parameter grid; evaluates representative torus zeros, the two nonzero angular Jacobian factors, and limiting torus contacts; and cross-checks the numerator against independent derivative expressions. These computations do **not** certify all complex-parameter cases. The general proof instead uses phase reduction, a real implicit-function argument, two zero counts by the argument principle, and Rouché's theorem at the endpoint.

The primary full text and mathematically closest complete published proofs were compared for differences of domain, kernel exponent, functional coefficient ratio, and implication direction. Historical priority outside inspected material remains an acknowledged limitation. Independent audit has not been performed.
