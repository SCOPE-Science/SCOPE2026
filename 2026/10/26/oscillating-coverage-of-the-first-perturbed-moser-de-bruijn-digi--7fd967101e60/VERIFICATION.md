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

Run `python3 verify.py` (standard library only). It enumerates the Moser–de Bruijn set by an independent base-four-digit predicate; enumerates each \(x+6y<131072\) and checks that no two ordered pairs collide; compares membership with the explicit carry transducer at every tested integer; and verifies the three carry-state counts together with both cutoff formulas for every \(1\le L\le8\). Expected output: `VERIFY_OK: unique representations and independent carry decisions for all n<131072; eight exact scale-pair counts and carry histograms`.

No finite computation certifies the infinite assertion that the natural density does not exist. That conclusion follows from the symbolic recurrences and limits in `RESULT.md`. No independent external audit was performed.
