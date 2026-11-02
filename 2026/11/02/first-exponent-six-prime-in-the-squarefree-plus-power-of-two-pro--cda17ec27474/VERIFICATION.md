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

# Reproduction and limits

Execute `python3 verify.py` from the same directory. No nonstandard packages, downloads, or auxiliary data are required.

The checker enumerates every residue \(36k+7\le10^9\) and marks each of the five admissible exponents by the congruence \(36k+7\equiv2^a\pmod{q^2}\) for every prime \(q\ge5\) with \(q^2\le10^9\). The proof explains why no other squared obstruction is possible. It confirms the complete list of nine integers with all five marks, tests all nine by deterministic trial division, and checks exact factors of both successful sixth-exponent remainders.

This is an exhaustive finite arithmetic certificate within the stated bound; it does not establish any infinite prime-distribution result or the general squarefree-plus-power-of-two conjecture. An independent audit has not been performed.

Observed executable output includes `VERIFY_OK`, `all_integer_five_obstruction_candidates` (nine values), `prime_candidates` (the two stated primes), and `exact_modular_congruence_sieve=PASS deterministic_trial_division=PASS`.
