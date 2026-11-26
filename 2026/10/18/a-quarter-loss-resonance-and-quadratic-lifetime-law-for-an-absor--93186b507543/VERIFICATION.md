---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

# Reproduction and scope

The retained analytical result is the near-resonance linewidth and survival limit for a single corner absorber. The exact static absorption identities are credited background. The fixed finite-size proof in `RESULT.md` derives the linewidth from a rank-one characteristic determinant and the survival law from spectral projection and a uniform bound for the fast transients near the collision. The detector term is normalized to \(-i\gamma|0,0\rangle\langle0,0|/2\).

The accompanying programs require Python, NumPy, SciPy and SymPy as listed in `artifacts/requirements.txt`. In a directory containing the artifacts, `python artifacts/verification.py` checks 170 static projector formulas and 24 finite-detuning linewidth examples (relative tolerance 0.022). `python artifacts/test_survival.py` compares 32 finite-time matrix-exponential evaluations with the proposed limiting profile (absolute tolerance 0.025). Neither program establishes the small-detuning asymptotics or an error estimate uniform in size or sink strength.
