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

# Verification and reproducibility

Run `python3 checker.py` from the extracted directory. This script uses only Python standard-library rational arithmetic and emits one JSON object. Its exact bytes (plus one line feed) must match the included `certificate.json`.

The script checks: (i) the exact two-age trace comparison with fixed determinant; (ii) exact componentwise five-age inequalities certifying one periodic multiplier above one and the other below one; (iii) equality of characteristic polynomials over all permutations for the finite test grid of periods three and four and viable seed age counts just below or divisible by each period and twice the period.

The universal spectral identities follow instead from the displayed analytic Floquet reconstruction and removable-root formulas. No finite computation is claimed to establish them for unbounded periods or ages. There is no independent audit, observational-data fit, or external certification.
