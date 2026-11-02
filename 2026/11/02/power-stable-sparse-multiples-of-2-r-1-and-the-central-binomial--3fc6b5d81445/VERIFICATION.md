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

# Checks and scope

Run `python verify_mersenne_power.py` with Python 3.8+. The independent integer-arithmetic verifier checks 23 pairs of Mersenne exponents and powers using modular exponentiation, explicit sparse bit positions, modular divisibility, and binary-weight measurements. It also constructs odd-prime noncarry witnesses, checks base-2 Legendre valuations, and tests lower bounds against many initial multiples. Observed run: `VERIFY_OK lifted_Mersenne_powers= 23 odd_prime_zero_carry_witnesses=checked initial_multiple_minimal_weight=checked central_binomial_carry_identity=checked`.

All claims over infinitely many \(r,k,n\) rely on the proof, not exhaustive computation. The proof invokes the classical odd-prime lifting-the-exponent identity and Kummer/Legendre valuations. The exact order of powers under modular maps is established prime-by-prime. No independent scientific audit has been performed.
