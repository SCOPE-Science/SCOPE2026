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
# Verification details

Run `python3 verify.py` with Python 3.8 or later. The script has no external dependencies and emits a JSON summary. `verification_output.json` records the exact expected result.

The run enumerates 33 odd prime-power moduli at most 1,500 (including exponent one as a boundary control), verifies all 33 even-unit moment identities and gcd conditions, checks 272 primitive-root choices among bounded bases, and tests the least period and half-period complement of each of the associated binary words (75,882 positions). It separately checks 355 individual Diophantine-solvability predicates by bounded exact integer search against the modular-inverse parity formula. A non-dyadic example modulo \(49\) verifies that base \(2\) has order \(21\), whereas primitive base \(3\) has output least period \(42\). The nonprimitive base \(3\) modulo \(121\) is verified to have state order \(5\) but output period \(1\).

The tests are finite and not a certificate for unbounded primes, exponents or bases. Universal correctness instead rests on the explicit parity characterization, invertible even-unit sum, group action on the parity partition, and unique involution proved in `RESULT.md`. No automated test assesses mathematical originality or independent validation.
