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

# Reproducibility and boundaries

Run `python verify_jones.py` with Python 3. The script generates all noncrossing matchings of size `2*n` for `n=2,...,9`, composes them by explicit three-layer connectivity, computes their first stabilization exponent, and checks every prescribed one-cap power and rank. The resulting Catalan counts are 2, 5, 14, 42, 132, 429, 1430, 4862; total 6916. The maximal-exponent multiplicities are 2, 5, 2, 6, 2, 6, 2, 6, respectively (the first two sizes have maximal exponent one). The routine checks all enumerated diagrams, not all diagrams for unbounded n. The proof in RESULT.md provides the universal argument. No independent audit is asserted.
