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

# Reproducibility and bounds

Run `python3 verify.py` with the Python standard library. The checker independently reconstructs the coefficients using the exact integral functional equation, and verifies normalized first-unit digits and valuations for eight configurations and 12,900 indices. It also checks finite samples of the formal logarithm coefficient identity and Legendre estimates. The symbolic proof in `RESULT.md` establishes the unrestricted theorem; finite tests do not certify uniqueness or priority. The published source's prime-base results are treated as known. The 2023 related paper's full text was inaccessible, so the priority assessment retains that uncertainty.
