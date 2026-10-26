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

# Verification record

Run `python3 verify_peeling.py` using the Python standard library only. The program constructs all seven nonempty supports on three coordinates, computes the fixed point of the iterative peeling procedure for each of the 128 support-observation sets, and expands the exact failed-observation probability as a polynomial in three independent exponential survival variables. There are exactly 28 failing sets. It checks the expected seven-term polynomial coefficient-by-coefficient. A separately implemented rational recurrence for first-arrival support sampling is compared to integration of the survival polynomial for six rational degree distributions, including two boundary cases and the explicit finite witness. Exact fraction identities establish the quartic numerator and a positive global convexity certificate. The program exits without errors and prints `CHECK_OK`.

The verification scope is exact finite symbolic and rational arithmetic on seven packet support types; the proof handles every legal probability distribution and does not infer it from numerical sampling. No external audit has been carried out. The tiny strict improvement is a mathematical witness, not a measured application benefit.
