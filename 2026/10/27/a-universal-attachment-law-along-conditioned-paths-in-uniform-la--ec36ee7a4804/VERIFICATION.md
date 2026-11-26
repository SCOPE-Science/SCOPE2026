---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The unchanged `geodesic_degree_checker.py` enumerates Prüfer words for all orders from 2 through 8 and checks the joint path-attachment probabilities used in the coupling against the enumerated probabilities. Run `python3 geodesic_degree_checker.py` with the standard library. The recorded marker is `PASS 648 exact rational Prüfer/path/joint-law checks for n=2..8`. Finite enumeration does not verify the order for all sizes or the existence of a common coupling. That conclusion follows analytically from the nested random ordering and common trial prefixes in `RESULT.md`.
