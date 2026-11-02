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

Run `python3 verify.py` in a directory containing the extracted result package. It uses only the Python standard library and recomputes the model and objective from the stated sitewise recurrence, rather than using stored numerical logs.

At packaging, the script passed 7,193 exact-rational assertions. It checks the continuous equality constructions for sample rational lengths, many filter counts and efficiencies, the exact mass and squared-load identities, discrete objective identities for all eligible pairs in several small-size grids, the square-completion correspondence, and efficiency thresholds including exact ties. Mathematical proofs of all real-parameter and unbounded-integer conclusions are in `RESULT.md`; finite tests are not an infinite proof. No external expert review or independent validation was performed.
