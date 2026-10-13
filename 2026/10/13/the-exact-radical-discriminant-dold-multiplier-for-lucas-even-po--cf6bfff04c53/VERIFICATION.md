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

# Verification and limits

The exact prime-power congruences are proved by separable Frobenius, nilpotent reduction at discriminant primes (including \(p=2\)), and a commuting-matrix binomial lifting argument. The Möbius pairing then proves the Dold congruence for every positive index. Necessity follows from the single index \(n=p\) for each discriminant prime; with zero discriminant this obstruction appears at every prime.

Run `python3 verify.py` in the directory containing the standalone package files. The script uses the Python standard library only and computes modular companion-matrix powers, Möbius sums, squarefree discriminant radicals and finite prime obstructions. The actual check output is `verification_output.txt`.

Finite checks cover 220 integer parameter pairs, 18,700 square-index Dold congruences, 14,268 higher even-power congruences (exponents \(4\), \(6\), \(8\)), and 104 zero-discriminant prime obstructions. They do **not** enumerate every prime, parameter, exponent, or index. The unrestricted assertions rest on the mathematical proof, not the test log. Independent audit has not been performed.
