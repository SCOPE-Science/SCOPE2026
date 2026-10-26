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

# Verification

Run `python3 verify_rankone_nijenhuis.py` using a standard Python 3 interpreter. The standalone program enumerates all nonzero rank-one maps on \(M_2(\mathbb F_q)\) for \(q=2,3,4\) by selecting the unique normalized image-generator representative, then testing the operator identities on all \(16\) ordered matrix-unit pairs for every functional. The identities are bilinear, so the basis checks are exhaustive for those three fields.

Expected counts (weight-zero Rota–Baxter, Nijenhuis, exceptional): \(q=2\): \((15,27,12)\); \(q=3\): \((56,128,72)\); \(q=4\): \((135,375,240)\). Expected terminal marker: `RANKONE_NIJENHUIS_BOUNDARY_OK`. The run used only the Python standard library and completed successfully.

The all-fields proof is the source of the universal assertion. The finite census is a separate reproducibility check, not an exhaustive check over arbitrary finite fields or infinite fields. Literature searches do not establish absolute priority. No independent verification is claimed.
