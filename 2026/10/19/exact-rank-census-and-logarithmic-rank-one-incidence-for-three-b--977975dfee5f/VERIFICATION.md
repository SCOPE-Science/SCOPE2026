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

Execute `python3 checker.py` with Python 3.9 or newer. The script uses only the standard library. Its final success marker is `VERIFY_OK`.

The exact-cyclotomic determinant test uses the coefficient-fiber characterization of divisibility by the prime-power cyclotomic polynomial, without floating-point thresholds. The six exhaustive cases and four seeded tests listed in `RESULT.md` were run successfully from the included checker. The global multiplicities and local rank incidence were compared against independently evaluated exact cyclotomic ranks in the exhaustive cases.

The proof for every prime and power follows from unit-modulus matrix rigidity, modular valuation geometry, and finite combinatorial counting. The tests do not establish the theorem by extrapolation, do not address determinants' conditioning, and do not constitute independent mathematical review.
