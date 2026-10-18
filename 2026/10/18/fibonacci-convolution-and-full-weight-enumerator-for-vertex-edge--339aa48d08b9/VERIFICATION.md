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

# Verification performed

Run the standalone Python 3 program `python verify_paths.py`. It checks the original vertex–edge condition directly for all label vectors on paths of order zero through twelve. Every coefficient is compared with the recurrence extracted from the proved rational generating function. It then checks the stated minimum weights and optimal multiplicities through length \(160\), and hand-checks the first two boundary polynomials. The printed result is copied exactly to `verification_output.txt`.

# Limits

The script establishes finite consistency only. The all-orders theorem is established by the zero-run bijection, exact two-by-two transfer and formal Laurent coefficient extraction in `RESULT.md`. The public source date and bibliographic claims are distinct from mathematical verification. Independent audit has not been performed.
