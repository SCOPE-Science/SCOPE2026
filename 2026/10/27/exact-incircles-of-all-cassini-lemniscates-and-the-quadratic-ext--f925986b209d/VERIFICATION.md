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

The exact proof is in `RESULT.md`. The standalone `verify.py` uses only Python 3's standard library and checks the quartic identity at rational planar inputs, rational trigonometric-coefficient identities for nine parameter choices, and supplemental circle samples. The command actually executed for this package was `python3 verify.py`; it completed with `VERIFY_OK squared_parameter_cases=9 exact_quartic_evaluations=2025 supplemental_circle_samples=9360`.

The analytic argument, not the samples, handles uncountably many points, all disk centers, all real \(s\ge0\), and the strict sublevel boundary. Checks do not prove historical originality. Independent validation is not performed.
