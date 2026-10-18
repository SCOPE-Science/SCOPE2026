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

# Reproducibility

Run `python verify_star.py` with Python 3. The program enumerates all partial maps on stars with one through five leaves and independently tests every vertex/edge inverse image. It checks the exact formulas for all elements, noninjective elements, regular elements, nonregular elements, and idempotents; it also tests the complete rank profiles. Its regularity test constructs all set-theoretic sections and directly checks continuity, rather than relying on the theorem's classification. It checks the partial-bijection recurrence through index 149.

The terminal success message is `VERIFY_OK: exhaustive continuous maps on stars m=1..5, regular sections, idempotents, rank distributions, Laguerre recurrence.`

# Mathematical boundaries

Exhaustive tests are finite. The all-size assertions follow from the normal forms, fibre-section criterion, and exact combinatorial identities proved in `RESULT.md`. The asymptotic concentration statement uses the explicitly shown weight ratio and an exponential-tail argument, not an experimental fit. The literature assessment and proof have received self-review only; independent audit has not been performed.
