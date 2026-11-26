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

# Computational and analytical verification

Run `python verify.py` with SymPy installed as specified in `requirements.txt`. This exact arithmetic check solves the tilted eigenvalue perturbation equations through order four using the full generator, and compares the result with the variance of the harmonic-coordinate corrector. A separate calculation of the parallel-arc resistances checks the variance deficit of the Kirchhoff index. The analytic argument in `RESULT.md` is the proof for all finite periods and strictly positive symmetric rates; the checks are finite corroboration and do not establish historical priority.
