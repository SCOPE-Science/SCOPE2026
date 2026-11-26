---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

# Reproducibility and scope

The analytical proof in `RESULT.md` covers global absorption, contraction on the absorbing sublevel, periodicity and half-period antisymmetry, and the integrable axial transient. The accompanying `verify.py` has recorded symbolic checks of the energy and difference identities, and finite numerical checks of periodic responses and drift signs. It contains additional checks of the perturbative cycle drift, a comparison result rather than a separate claim here. The finite checks do not establish the global quantifiers. The all-initial-data result, and not the local-branch expansion, is the scope of the theorem.
