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

Execute `python3 verify_c5.py` using Python 3 and no third-party packages. The expected terminal output begins `CERTIFICATE_OK` and states that 243 averaging choices were covered, 238 have strict rational \(LDL^{\mathsf T}\) bounds, and five rotational choices are maximizing.

The certificate constructs balls from breadth-first shortest-path distances, not from hard-coded averaging matrices. All matrix entries, pivots, determinant checks, and root isolation comparisons are rational. The proof of the cubic's largest-root characterization and the full equality class is in `RESULT.md`.

The finite enumeration is exhaustive only because five vertices each admit precisely three distinct centered graph balls. The independent audit status is unperformed. This is not a claim of machine-formal proof for arbitrary graphs.
