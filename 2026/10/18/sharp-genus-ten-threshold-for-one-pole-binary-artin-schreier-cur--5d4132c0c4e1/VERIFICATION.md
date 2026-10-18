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
# Exact reproducibility

Run `python3 verify_onepole.py` (Python 3 standard library; no third-party dependencies). The checker verifies the irreducible-field encoding and Frobenius orbit degrees, all twenty-two moments of the explicit seven-place dual certificate, the nine degree-six and two degree-three witness evaluations, and the extension point counts \(N_1=5\), \(N_2=5\), \(N_3=17\), \(N_6=17\). It printed PASS for every stage.

The universal impossibility for odd polynomial degree at most nineteen follows algebraically from the dual certificate, not from model enumeration. Smoothness, geometric connectedness, genus and closed-place splitting use standard Artin–Schreier covering theory. The checker does not certify the theorem for unrelated higher-degree or multiple-pole models, and no independent external verification is represented.
