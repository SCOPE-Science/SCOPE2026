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

Run `python3 verify_pd_curvature.py` in the package directory with Python 3 and no third-party modules. The exact-rational checker enumerates all surviving-leaf subsets on six weighted stars (three to eight tips), a weighted quartet, and a weighted five-tip tree; compares the complete polynomials to the edge formula and checks curvature and Jensen signs at rational arguments. It also checks the quartet polynomial and selected second derivatives. The unlimited-size uniqueness, sharp bound, and environmental comparisons are analytically proved in RESULT.md, not inferred from enumeration. Independent audit has not been performed.
