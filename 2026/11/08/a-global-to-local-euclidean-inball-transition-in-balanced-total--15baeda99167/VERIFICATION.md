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

# Reproducibility and verification

The accompanying `scripts/check_total_matching.py` was executed using Python, NumPy, and SciPy in the same package workspace. It enumerates every facet normal of the published original-coordinate description, including the full lifted nonbalanced family, for \(n=2,3,4\), with \(17\), \(52\), and \(341\) inequalities respectively. The computed Euclidean inradii were \(0.18469903125906464\), \(0.15895738076846547\), and \(0.1381966011250105\). The tangent types were coordinate (8) and full balanced (1) at \(n=2\); coordinate (15) and full balanced (1) at \(n=3\); and coordinate (24) and degree (8) at \(n=4\). The checker also fixed the radius and independently minimized and maximized every candidate center coordinate, finding equality with the predicted uniform center, and screened lifted inequality size orbits for \(2\le n\le30\). The successful final marker was `BALANCED_TOTAL_MATCHING_INBALL_VERIFIED`.

Reproduction: install the versions compatible with `requirements.txt` and invoke `python scripts/check_total_matching.py`. The script relies only on stated numerical tolerances for floating-point LP checks. No finite sample proves the all-integer statement; the separately written analytical proof addresses it. No external audit or external formal verification was performed.
