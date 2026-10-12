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

The executable check uses Python 3 standard library only. Run `python3 verify.py --csv minimal_fiber.csv`; compare standard output byte-for-byte with `verification_output.txt` and the generated CSV with the embedded `minimal_fiber.csv`.

The program enumerates every divisor of 57600 and trial-tests primality of each divisor plus one. Its exact recursive search examines every strictly increasing four-prime selection whose predecessor product equals 57600. It checks all 37 output rows and establishes the minimum 75361 among them. An independent sieve covers all 11386 integers below 75361 that have exactly four distinct prime divisors, without restricting exponent vectors, and detects no solution.

The mathematical reason for considering 57600 is established in the proof: squarefree four-prime solutions require an even totient with 2-adic valuation at least 3 and exactly 81 divisors. The enumerated finite fiber is not assumed to contain all solutions of the original equation. The exhaustive scan of numbers below the explicit witness is sufficient only for the claimed first-entry result.
